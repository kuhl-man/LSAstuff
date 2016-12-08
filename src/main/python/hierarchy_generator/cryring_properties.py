from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class CRYRING_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "CRYRING"
        self._particle_transfer = "CRYRING_RING"
        self._version = "1.0.0"
        
if __name__ == '__main__':

  h = CRYRING_YRME_PROPERTIES()
  
  print h.accelerator
