from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class CRYRING_LINAC_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "CRYRING"
        self._particle_transfer = "CRYRING_LINAC"
        self._version = "1.0.0"
        self._timeparam_device = 'CRYRING_LINAC_TIMEPARAM'
        
if __name__ == '__main__':

  h = CRYRING_LINAC_PROPERTIES()
  
  print h.accelerator