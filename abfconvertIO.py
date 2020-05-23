# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:25:47 2020

@author: wnight
"""

import datetime
from axonio import Abf_io
import numpy as np
import scipy.io as sio
from nptdms import TdmsWriter, RootObject, ChannelObject

# read file name


def form_time(date, microscend):
    s, ms = divmod(microscend, 1000)
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    dt = datetime.datetime(int(str(date)[0:4]), int(
        str(date)[4:6]), int(str(date)[-2:]), h, m, s, ms)
    return np.datetime64(dt)


class Convert():
    def __init__(self, filename):
        self.fn = Abf_io(filename)
        self.data, self.sam, self.sweeps = self.fn.read_abf()
        if self.sweeps==0:
            self.sweeps +=1
        self.abf_info = self.fn.read_header()
        self.filesignature = self.abf_info['fFileSignature'].decode()
        self.fileVersion = self.abf_info['fFileVersionNumber']
        self.chanles = len(self.abf_info['listADCInfo'])
        self.groups = self.abf_info['lActualEpisodes']
        self.new_filebase = filename.rsplit('.', 1)[0]

    def gene_rootobj(self):
        root_object = RootObject(properties={
            "fileVersion": self.filesignature+'/'+str(self.fileVersion)
        })
        return root_object

    def gene_channelobj(self, channelNum):

        per = {'unit_string': self.abf_info['listADCInfo'][channelNum]['ADCChUnits'].decode(),
               'NI_ChannelName': self.abf_info['listADCInfo'][channelNum]['ADCChNames'].decode(),
               'NI_UnitDescription': self.abf_info['listADCInfo'][channelNum]['ADCChUnits'].decode(),
               'wf_increment': float(1/self.sam),
               'wf_samples': int(1),
               'wf_start_offset': float(0),
               'wf_start_time': form_time(self.abf_info['uFileStartDate'],
                                          self.abf_info['uFileStartTimeMS'])
               }
        channel_name = per['NI_ChannelName']
        return channel_name, per

    def toTdms(self):
        with TdmsWriter(self.new_filebase+'.tdms') as tdms_writer:
            tdms_writer.write_segment([self.gene_rootobj()])
            for i in range(self.sweeps):
                group = 'sweep'+str(i)
                for j in range(self.chanles):
                    channel, proper = self.gene_channelobj(j)
                    channel_object = ChannelObject(
                        group, channel, self.data[i][:, j], properties=proper)
                    tdms_writer.write_segment([channel_object])

    def toMat(self):
        temp = {}
        for i in range(self.sweeps):
            time = np.arange(0, len(self.data[i])/self.sam, 1/self.sam)
            time = time[0:len(self.data[i])]
            temp.update(
                {'sweep{}'.format(i): np.vstack((time, self.data[i].T)).T})
        sio.savemat(self.new_filebase+'.mat', temp)

    def toCsvTxt(self, suffix='csv', issplit=True, timesteps=60):
        header='time/s'
        for i in range(self.chanles):
            header += ','+self.abf_info['listADCInfo'][i]['ADCChNames'].decode()+ \
                          '/'+self.abf_info['listADCInfo'][i]['ADCChUnits'].decode()
                        
        if issplit is not True:
            print('split')
            for i in range(self.sweeps):
                time = np.arange(0, len(self.data[i]) / self.sam, 1 / self.sam)
                time = time[0:len(self.data[i])]
                np.savetxt(self.new_filebase + '_sweep{}.'.format(i) + suffix,
                            X=np.vstack((time, self.data[i].T)).T,
                            delimiter=',',
                            comments='',
                            header=header
                           )
                           
        else:
            for i in range(self.sweeps):
                blocksize = int(self.sam*timesteps)
                time = np.arange(0, len(self.data[i]) / self.sam, 1 / self.sam)
                time = time[0:len(self.data[i])]
                for j in range(int(np.ceil(len(self.data[i])/blocksize))-1):
                    np.savetxt(self.new_filebase + '_sweep{}_cut{}.'.format(i,j) + suffix, 
                                X=np.vstack((time[j*blocksize:(j+1)*blocksize], self.data[i][j*blocksize:(j+1)*blocksize,:].T)).T,
                                delimiter=',',
                                comments='',
                                header=header)                               
                np.savetxt(self.new_filebase + '_sweep{}_cut{}.'.format(i,j+1) + suffix,
                            X=np.vstack((time[(j+1)*blocksize:], self.data[i][(j+1)*blocksize:,:].T)).T,
                            delimiter=',',
                            comments='',
                            header=header
                          )

                




if __name__ == "__main__":
    pass
