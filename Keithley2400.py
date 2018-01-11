#Keithley2400.py
'''
@author: Jackson Anderson
ander906@purdue.edu
HybridMEMS
'''

import visa
import numpy as np

class Keithley2400:
    def __init__(self, resource):
        rm = visa.ResourceManager()
        
        # VisaIOError VI_ERROR_RSRC_NFOUND
        try:
          self.visaobj = rm.open_resource(resource)
        except visa.VisaIOError as e:
          print(e.args)
          exit  
    
    def connect(self):

        rm = visa.ResourceManager()
        
        # VisaIOError VI_ERROR_RSRC_NFOUND
        try:
          self.visaobj = rm.open_resource(resource)
        except visa.VisaIOError as e:
          print(e.args)
          exit

    def smuSetup(self, voltRange = 21, comp = 0.000105):
        '''
        A function for all general smu setup.
        System configures the compliance to the default
        Parameters:
        -----------
        smu
            The SMU to be set up.
        comp : float
            The current compliance to be set.
        
        Returns:
        ----------
        N/A
        '''
       # smu.write(':DISPlay:ENABle 1; CNDisplay')
        
        if comp: # set compliance if given. Default for 2400 is 105uA, 21V
#            self.visaobj.write(':SENSe:VOLTage:RANGe ' + str(voltRange))
            self.visaobj.write(':SENSe:CURRent:PROTection:LEVel ' + str(comp))

    def setVoltage(self,voltage):
        self.visaobj.write('SOURce:VOLTage:LEVel {}'.format(str(voltage)))
        self.visaobj.write(':CONFigure:VOLTage:DC')
        self.visaobj.query('*OPC?')

    def readError(self):
        print(self.visaobj.query('SYSTem:ERRor:NEXT?'))

    def outputOff(self):
        self.setVoltage(0)
        self.visaobj.write(':OUTPut:STATe OFF')        
        
    def disconnect(self):
        self.outputOff()
        self.visaobj.close()
        