import xml.etree.ElementTree as ET
import xml
import math
import os

_values = {
          'KL' : ['blmin' , 'blmax'],
          'BL' : ['blmin' , 'blmax'],
          'I'  : ['imin' , 'imax'],
          'IDOT' : ['idotmax'],
          'U' : ['ffVoltagemin' , 'ffVoltagemax'],
          'FRF' : ['fmin' , 'fmax'],
          'URF' : ['umin' , 'umax'],
          'ICORR' : ['imin' , 'imax'],
              
          }

class XMLParser:
    
#    def __init__(self, accelerator, rigidity, particle_transfer):
#        self.tree = ET.parse('devicedata_' + accelerator + '_' + particle_transfer + '_python.xml')
    def __init__(self, particletransfer, rigidity):
        file = 'devicedata_' + particletransfer + '_python.xml'
        if os.path.isfile(file):
            self.tree = ET.parse(file)
            self.root = self.tree.getroot()
            self.rigidity = rigidity
        else:
            self.tree = ET.parse('devicedata_dummy_python.xml')
            self.root = self.tree.getroot()
            self.rigidity = 1

    def findYPrec(self, deviceName, value, relativPrec, fromMaxValue = True):
        
        valuesList = _values.get(value)
        
        returnvalue = None
                                
        for device in self.root.findall('system/device'):
            if (device.get('name') == deviceName):
                #print device.get('name') + ' [' + value + ']'
                
                if (valuesList != None):
                    usedValue = None
                
                    for minMax in valuesList:
                        for node in device.getchildren():
                            tag = node.tag
                            if tag == minMax:
                                getValue = abs(float(node.attrib['value']))
                                if (value == 'KL'):
                                    getValue = getValue / self.rigidity 
                                if (usedValue == None):
                                    usedValue = getValue
                                else:
                                    if (fromMaxValue):
                                        if (usedValue < getValue):
                                            usedValue = getValue
                                    else:
                                        if (usedValue > getValue):
                                            usedValue = getValue
                                            
                    if (value == 'KL'):
                        relativPrec = relativPrec / self.rigidity
                        
                    if usedValue != None:
                        absolutePrec = abs(usedValue * relativPrec)
                        precision = -1.0 * math.log10(absolutePrec)
                        returnvalue = int(math.ceil(precision))
                        #print precision , returnvalue
                   
        return returnvalue


if __name__ == '__main__':

    from sis100_devices import SIS100_DEVICES
      
    devices = SIS100_DEVICES()
    accelerator = devices.accelerator
    self.rigidity = 100
        
    xml = XMLParser(accelerator, 100)
    print 'KL'
    print '-----'
    for device in devices.main_dipoles:
        xml.findYPrec(device, 'KL', 5.0e-5)
    for device in devices.main_quadrupoles:
        xml.findYPrec(device, 'KL', 5.0e-5)
    for device in (devices.main_sextupoles + devices.resonance_sextupoles):
        xml.findYPrec(device, 'KL', 1.0e-3)
    for device in (devices.vertical_correctors + devices.horizontal_correctors):
        xml.findYPrec(device, 'KL', 1.0e-2)
    for device in (devices.correction_quadrupoles + devices.correction_sextupoles + devices.correction_octupoles):
        xml.findYPrec(device, 'KL', 1.0e-2)
    print '-----'

    print 'BL'
    print '-----'
    for device in devices.main_dipoles:
        xml.findYPrec(device, 'BL', 5.0e-5)
    for device in devices.main_quadrupoles:
        xml.findYPrec(device, 'BL', 5.0e-5)
    for device in (devices.main_sextupoles + devices.resonance_sextupoles):
        xml.findYPrec(device, 'BL', 1.0e-3)
    for device in (devices.vertical_correctors + devices.horizontal_correctors):
        xml.findYPrec(device, 'BL', 1.0e-2)
    for device in (devices.correction_quadrupoles + devices.correction_sextupoles + devices.correction_octupoles):
        xml.findYPrec(device, 'BL', 1.0e-2)
    print '-----'
    print 'I'
    print '-----'
    for device in devices.main_dipoles:
        xml.findYPrec(device, 'I', 5.0e-5)
    for device in devices.main_quadrupoles:
        xml.findYPrec(device, 'I', 5.0e-5)
    for device in (devices.main_sextupoles + devices.resonance_sextupoles):
        xml.findYPrec(device, 'I', 1.0e-3)
    for device in (devices.vertical_correctors + devices.horizontal_correctors):
        xml.findYPrec(device, 'I', 1.0e-2)
    for device in (devices.correction_quadrupoles + devices.correction_sextupoles + devices.correction_octupoles):
        xml.findYPrec(device, 'I', 1.0e-2)
    print '-----'
    print 'IDOT'
    print '-----'
    for device in devices.main_dipoles:
        xml.findYPrec(device, 'IDOT', 2.4e-2)
    for device in devices.main_quadrupoles:
        xml.findYPrec(device, 'IDOT', 2.4e-2)
    print '-----'
    print 'U'
    print '-----'
    for device in devices.main_dipoles:
        xml.findYPrec(device, 'U', 1.0e-3)
    for device in devices.main_quadrupoles:
        xml.findYPrec(device, 'U', 1.0e-3)
    print '-----'
    print 'FRF'
    print '-----'
    for device in (devices.cavities + devices.old_cavities_freq):
        xml.findYPrec(device, 'FRF', 1.0e-6)
    print '-----'
    print 'URF'
    print '-----'
    for device in (devices.cavities + devices.old_cavities_ampl):
        xml.findYPrec(device, 'URF', 1.0e-3)

    print '-----'

    #xml.findIMax('1S00MH', 5.0e-5)
    #xml.findIDotMax('1S00MH', 2.4e-2)
    
    #print ('iMin = ' , xml.imax)
#    print ('fMin = ' + xml.fmin)
    
