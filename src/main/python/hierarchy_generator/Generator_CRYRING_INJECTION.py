from init_lh_builder import INIT_LH_BUILDER

from cryring_injector_properties import CRYRING_INJECTOR_PROPERTIES

from Generator_CRYRING_YRLE import GENERATOR_CRYRING_YRLE

from Generator_CRYRING_YRME import GENERATOR_CRYRING_YRME

class GENERATOR_CRYRING_INJECTOR(INIT_LH_BUILDER, GENERATOR_CRYRING_YRLE, GENERATOR_CRYRING_YRME):
    
    def __init__(self):
        
        cryring_injector_properties = CRYRING_INJECTOR_PROPERTIES()
        INIT_LH_BUILDER.__init__(self, cryring_injector_properties)
        
    def build(self):
        
        GENERATOR_CRYRING_YRME.__init__(self)
        GENERATOR_CRYRING_YRME.build(self)
        
        GENERATOR_CRYRING_YRLE.__init__(self)
        GENERATOR_CRYRING_YRLE.build(self)
                
    def generate(self):
        self.lh_builder.export()

      
if __name__ == '__main__':

  h = GENERATOR_CRYRING_INJECTOR()
  
  h.build()
  h.generate()
