from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from init_lh_builder import INIT_LH_BUILDER
from FRS_MAIN_properties import FRS_MAIN_PROPERTIES
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy

from Generator_FRSS3 import GENERATOR_FRSS3
from Generator_FRSS4 import GENERATOR_FRSS4
from Generator_FRSS5 import GENERATOR_FRSS5
from Generator_FRSS6 import GENERATOR_FRSS6
from Generator_FRSS7 import GENERATOR_FRSS7
from Generator_FRSS8 import GENERATOR_FRSS8
class GENERATOR_FRS_MAIN_REST(INIT_LH_BUILDER,GENERATOR_FRSS3, GENERATOR_FRSS4, GENERATOR_FRSS5, GENERATOR_FRSS6, GENERATOR_FRSS7, GENERATOR_FRSS8):
    
    def __init__(self):
        frs_main_properties = FRS_MAIN_PROPERTIES()
        INIT_LH_BUILDER.__init__(self, frs_main_properties)
        
    def __buildSpecial(self):
        self.lh_builder.create_child_node('FRSS4_BEAM/E','TS4ED4SG/E_OUT')
        #self.lh_builder.create_child_node('FRSS1_BEAM/Q','TS2ET2G/Q_OUT')
        
        self.lh_builder.create_child_node('FRSS5_BEAM/E','HFSET4SG/E_OUT')
        #self.lh_builder.create_child_node('FRSS2_BEAM/Q','TS3ED2O2G/Q_OUT')
        self.lh_builder.create_child_node('FRSS8_BEAM/E','TH4UFG/E_OUT')
        #self.lh_builder.create_child_node('AZ_BEAM/E','TS3ET7USG/E_OUT')


    def build(self):
        
       GENERATOR_FRSS3.__init__(self)
       GENERATOR_FRSS3.build(self)
       
       GENERATOR_FRSS4.__init__(self)
       GENERATOR_FRSS4.build(self)
       
       GENERATOR_FRSS5.__init__(self)
       GENERATOR_FRSS5.build(self)
       
       GENERATOR_FRST6.__init__(self)
       GENERATOR_FRST6.build(self)
       
       GENERATOR_FRST7.__init__(self)
       GENERATOR_FRST7.build(self)
       
       GENERATOR_FRST8.__init__(self)
       GENERATOR_FRST8.build(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_FRS_MAIN_REST()
    h2.build()
    h2.generate()
