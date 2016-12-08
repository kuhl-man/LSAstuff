from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class SIS100_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "SIS100"
        self._particle_transfer = "SIS100_RING"
        self._version = "1.0.0"
        
if __name__ == '__main__':

  h = SIS100_PROPERTIES()
  
  print h.accelerator