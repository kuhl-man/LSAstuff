from init_generic_particletransfer_properties import INIT_GENERIC_PARTICLETRANSFER_PROPERTIES

class SIS18_TS_HHD_PROPERTIES(INIT_GENERIC_PARTICLETRANSFER_PROPERTIES):
    
    def __init__(self):
        INIT_GENERIC_PARTICLETRANSFER_PROPERTIES.__init__(self)
        
        self._accelerator = "SIS18"
        self._particle_transfer = "SIS18_TS_HHD"
        self._version = "1.0.0"
        
if __name__ == '__main__':

  h = SIS18_TS_HHD_PROPERTIES()
  
  print h.accelerator