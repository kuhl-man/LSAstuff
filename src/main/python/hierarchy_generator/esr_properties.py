from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class ESR_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "ESR"
        self._particle_transfer = "ESR_RING"
        self._version = "1.0.0"
        
if __name__ == '__main__':

  h = ESR_PROPERTIES()
  
  print h.accelerator