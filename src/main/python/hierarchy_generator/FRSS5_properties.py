from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class FRSS5_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "SIS18"
        self._particle_transfer = "FRSS5"
        self._version = "1.0.0"
        
if __name__ == '__main__':

  h = FRSS5_PROPERTIES()
  
  print h.accelerator