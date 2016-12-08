from init_generic_devices import INIT_GENERIC_DEVICES
from FRS_device_groups import FRSDeviceGroups

class FRS_MAIN_DEVICES(INIT_GENERIC_DEVICES, FRSDeviceGroups):
    
    def __init__(self):
        INIT_GENERIC_DEVICES.__init__(self)
        self._accelerator_zone = "FRS_MAIN"
        
        self._targetladders = []
        self._targets = []
        self._degraders = []
        self._degrader_disks = []       
 
 
        INIT_GENERIC_DEVICES.buildalldevices(self)
        INIT_GENERIC_DEVICES.buildsystemmap(self)
        INIT_GENERIC_DEVICES.buildlinkrulemap(self)    
        
    
    @property
    def targetladders(self):
        return self._targetladders()
    
    @property
    def targets(self):
        return self._targets()   
    
    @property
    def degraders(self):
        return self._degraders()
    
    @property
    def degrader_disks(self):
        return self._degrader_disks()
    
if __name__ == '__main__':

  h = FRS_MAIN_DEVICES()

#  print h.main_quadrupoles

