from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class FRS_MAIN_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "SIS18"
        self._particle_transfer = "FRS_MAIN"
        self._version = "1.0.0"
        
if __name__ == '__main__':

  h = FRS_MAIN_PROPERTIES()
  
  print h.accelerator