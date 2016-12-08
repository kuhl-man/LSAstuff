from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from init_lh_builder import INIT_LH_BUILDER
from FRS_MAIN_properties import FRS_MAIN_PROPERTIES
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy

from Generator_FRSTS import GENERATOR_FRSTS
from Generator_FRSS1 import GENERATOR_FRSS1
from Generator_FRSS2 import GENERATOR_FRSS2
from Generator_FRSS3 import GENERATOR_FRSS3
from Generator_FRSS4 import GENERATOR_FRSS4
class GENERATOR_FRS_MAIN(INIT_LH_BUILDER,GENERATOR_FRSTS, GENERATOR_FRSS1, GENERATOR_FRSS2, GENERATOR_FRSS3, GENERATOR_FRSS4):
    
    def __init__(self):
        frs_main_properties = FRS_MAIN_PROPERTIES()
        INIT_LH_BUILDER.__init__(self, frs_main_properties)
        
    def __buildSpecial(self):
        
       self.lh_builder.create_child_node('FRSS1_BEAM/E','TS2ET2G/E_OUT')
       self.lh_builder.create_child_node('FRSS2_BEAM/E','TS3ED2O2G/E_OUT')
       self.lh_builder.create_child_node('FRSS3_BEAM/E','DetTPC22/E_OUT')
       self.lh_builder.create_child_node('FRSS4_BEAM/E','TS4ED4SG/E_OUT')


    def build(self):
        
       GENERATOR_FRSTS.__init__(self)
       GENERATOR_FRSTS.build(self)
       
       GENERATOR_FRSS1.__init__(self)
       GENERATOR_FRSS1.build(self)
       
       GENERATOR_FRSS2.__init__(self)
       GENERATOR_FRSS2.build(self)
       
       GENERATOR_FRSS3.__init__(self)
       GENERATOR_FRSS3.build(self)
       
       GENERATOR_FRSS4.__init__(self)
       GENERATOR_FRSS4.build(self)
       
       self.__buildSpecial()
              
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_FRS_MAIN()
    h2.build()
    h2.generate()
