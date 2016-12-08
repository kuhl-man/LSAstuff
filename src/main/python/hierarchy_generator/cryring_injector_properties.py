from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class CRYRING_INJECTOR_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "CRYRING"
        self._particle_transfer = "CRYRING_INJECTOR"
        self._version = "1.0.0"
        
if __name__ == '__main__':

  h = CRYRING_INJECTOR_PROPERTIES()
  
  print h.accelerator