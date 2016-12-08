from init_generic_devices import INIT_GENERIC_DEVICES

class CRYRING_LINAC_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
       INIT_GENERIC_DEVICES.__init__(self)
        
        self._rigidity = 0.029
        self._accelerator_zone = "CRYRING_LINAC"

        INIT_GENERIC_DEVICES.buildalldevices(self)
        INIT_GENERIC_DEVICES.buildsystemmap(self)
        INIT_GENERIC_DEVICES.buildlinkrulemap(self)       

if __name__ == '__main__':

  h = CRYRING_LINAC_DEVICES()

#  print h.main_quadrupoles

