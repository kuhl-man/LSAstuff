from init_lh_builder import INIT_LH_BUILDER

from sis18_ts_hhd_properties import SIS18_TS_HHD_PROPERTIES

from sis18_ts_hhd_devices import SIS18_TS_HHD_DEVICES

from Generator_SIS18_EXTRACTION import GENERATOR_SIS18_EXTRACTION

from Generator_SIS18_TO_TS1MU1 import GENERATOR_SIS18_TO_TS1MU1

from Generator_TS1MU1_TO_TS3MU1 import GENERATOR_TS1MU1_TO_TS3MU1

from Generator_TS3MU1_TO_HHD import GENERATOR_TS3MU1_TO_HHD

class GENERATOR_SIS18_TS_HHD(INIT_LH_BUILDER, GENERATOR_SIS18_EXTRACTION, GENERATOR_SIS18_TO_TS1MU1, GENERATOR_TS1MU1_TO_TS3MU1, GENERATOR_TS3MU1_TO_HHD):
    
    def __init__(self):
        

        sis18_ts_hhd_properties = SIS18_TS_HHD_PROPERTIES()
        INIT_LH_BUILDER.__init__(self, sis18_ts_hhd_properties)
        
    def __buildSpecial(self):
        self.lh_builder.create_child_node(self.e_parameter_sis18_to_ts1mu1, self.e_parameter_sis18_extraction)
        self.lh_builder.create_child_node(self.element_parameter_sis18_to_ts1mu1, self.element_parameter_sis18_extraction)
        self.lh_builder.create_child_node(self.isotope_parameter_sis18_to_ts1mu1, self.isotope_parameter_sis18_extraction)
        self.lh_builder.create_child_node(self.q_parameter_sis18_to_ts1mu1, self.q_parameter_sis18_extraction)
        
        self.lh_builder.create_child_node(self.e_parameter_ts1mu1_to_ts3mu1, self.e_parameter_sis18_to_ts1mu1)
        self.lh_builder.create_child_node(self.element_parameter_ts1mu1_to_ts3mu1, self.element_parameter_sis18_to_ts1mu1)
        self.lh_builder.create_child_node(self.isotope_parameter_ts1mu1_to_ts3mu1, self.isotope_parameter_sis18_to_ts1mu1)
        self.lh_builder.create_child_node(self.q_parameter_ts1mu1_to_ts3mu1, self.q_parameter_sis18_to_ts1mu1)
        
        self.lh_builder.create_child_node(self.e_parameter_ts3mu1_to_hhd, self.e_parameter_ts1mu1_to_ts3mu1)
        self.lh_builder.create_child_node(self.element_parameter_ts3mu1_to_hhd, self.element_parameter_ts1mu1_to_ts3mu1)
        self.lh_builder.create_child_node(self.isotope_parameter_ts3mu1_to_hhd, self.isotope_parameter_ts1mu1_to_ts3mu1)
        self.lh_builder.create_child_node(self.q_parameter_ts3mu1_to_hhd, self.q_parameter_ts1mu1_to_ts3mu1)
    # build special part of hierarchy for SIS18_TS_HHD


    def build(self):
        
        GENERATOR_SIS18_EXTRACTION.__init__(self)
        GENERATOR_SIS18_EXTRACTION.build(self)
        
        GENERATOR_SIS18_TO_TS1MU1.__init__(self)
        GENERATOR_SIS18_TO_TS1MU1.build(self)

        GENERATOR_TS1MU1_TO_TS3MU1.__init__(self)
        GENERATOR_TS1MU1_TO_TS3MU1.build(self)
        
        GENERATOR_TS3MU1_TO_HHD.__init__(self)
        GENERATOR_TS3MU1_TO_HHD.build(self)

        
        
        # build special part of hierarchy
        self.__buildSpecial()

        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_SIS18_TS_HHD()
    h2.build()
    h2.generate()
