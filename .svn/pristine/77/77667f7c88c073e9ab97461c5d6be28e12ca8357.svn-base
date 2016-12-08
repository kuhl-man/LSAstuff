from init_lh_builder import INIT_LH_BUILDER

from sis18_th_hht_properties import SIS18_TH_HHT_PROPERTIES

from sis18_th_hht_devices import SIS18_TH_HHT_DEVICES

from Generator_SIS18_EXTRACTION import GENERATOR_SIS18_EXTRACTION

from Generator_SIS18_TO_TS1MU1 import GENERATOR_SIS18_TO_TS1MU1

from Generator_TS1MU1_TO_TE3MU1 import GENERATOR_TS1MU1_TO_TE3MU1

from Generator_TE3MU1_TO_HHTMU1 import GENERATOR_TE3MU1_TO_HHTMU1

from Generator_HHTMU1_TO_HHT import GENERATOR_HHTMU1_TO_HHT

class GENERATOR_SIS18_TH_HHT(INIT_LH_BUILDER, GENERATOR_SIS18_EXTRACTION, GENERATOR_SIS18_TO_TS1MU1, GENERATOR_TS1MU1_TO_TE3MU1, GENERATOR_TE3MU1_TO_HHTMU1, GENERATOR_HHTMU1_TO_HHT):
    
    def __init__(self):
        

        sis18_th_hht_properties = SIS18_TH_HHT_PROPERTIES()
        INIT_LH_BUILDER.__init__(self, sis18_th_hht_properties)
        
    def __buildSpecial(self):
        self.lh_builder.create_child_node(self.e_parameter_sis18_to_ts1mu1, self.e_parameter_sis18_extraction)
        self.lh_builder.create_child_node(self.element_parameter_sis18_to_ts1mu1, self.element_parameter_sis18_extraction)
        self.lh_builder.create_child_node(self.isotope_parameter_sis18_to_ts1mu1, self.isotope_parameter_sis18_extraction)
        self.lh_builder.create_child_node(self.q_parameter_sis18_to_ts1mu1, self.q_parameter_sis18_extraction)
        
        self.lh_builder.create_child_node(self.e_parameter_ts1mu1_to_te3mu1, self.e_parameter_sis18_to_ts1mu1)
        self.lh_builder.create_child_node(self.element_parameter_ts1mu1_to_te3mu1, self.element_parameter_sis18_to_ts1mu1)
        self.lh_builder.create_child_node(self.isotope_parameter_ts1mu1_to_te3mu1, self.isotope_parameter_sis18_to_ts1mu1)
        self.lh_builder.create_child_node(self.q_parameter_ts1mu1_to_te3mu1, self.q_parameter_sis18_to_ts1mu1)
        
        self.lh_builder.create_child_node(self.e_parameter_te3mu1_to_hhtmu1, self.e_parameter_ts1mu1_to_te3mu1)
        self.lh_builder.create_child_node(self.element_parameter_te3mu1_to_hhtmu1, self.element_parameter_ts1mu1_to_te3mu1)
        self.lh_builder.create_child_node(self.isotope_parameter_te3mu1_to_hhtmu1, self.isotope_parameter_ts1mu1_to_te3mu1)
        self.lh_builder.create_child_node(self.q_parameter_te3mu1_to_hhtmu1, self.q_parameter_ts1mu1_to_te3mu1)
        
        self.lh_builder.create_child_node(self.e_parameter_hhtmu1_to_hht, self.e_parameter_te3mu1_to_hhtmu1)
        self.lh_builder.create_child_node(self.element_parameter_hhtmu1_to_hht, self.element_parameter_te3mu1_to_hhtmu1)
        self.lh_builder.create_child_node(self.isotope_parameter_hhtmu1_to_hht, self.isotope_parameter_te3mu1_to_hhtmu1)
        self.lh_builder.create_child_node(self.q_parameter_hhtmu1_to_hht, self.q_parameter_te3mu1_to_hhtmu1)
        
        
    # build special part of hierarchy for SIS18_TH_HHT


    def build(self):
        
        GENERATOR_SIS18_EXTRACTION.__init__(self)
        GENERATOR_SIS18_EXTRACTION.build(self)
        
        GENERATOR_SIS18_TO_TS1MU1.__init__(self)
        GENERATOR_SIS18_TO_TS1MU1.build(self)

        GENERATOR_TS1MU1_TO_TE3MU1.__init__(self)
        GENERATOR_TS1MU1_TO_TE3MU1.build(self)
        
        GENERATOR_TE3MU1_TO_HHTMU1.__init__(self)
        GENERATOR_TE3MU1_TO_HHTMU1.build(self)
        
        GENERATOR_HHTMU1_TO_HHT.__init__(self)
        GENERATOR_HHTMU1_TO_HHT.build(self)

        
        
        # build special part of hierarchy
        self.__buildSpecial()

        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_SIS18_TH_HHT()
    h2.build()
    h2.generate()
