from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy

from init_lh_builder import INIT_LH_BUILDER

from sis18_extraction_properties import SIS18_EXTRACTION_PROPERTIES

from sis18_extraction_devices import SIS18_EXTRACTION_DEVICES

class GENERATOR_SIS18_EXTRACTION(GenericTransferlineHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):
        
        if not hasattr(self, 'lh_builder'):
            sis18_extraction_properties = SIS18_EXTRACTION_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, sis18_extraction_properties)

        
        SIS18_EXTRACTION_device_groups = SIS18_EXTRACTION_DEVICES()
        GenericTransferlineHierarchy.__init__(self, SIS18_EXTRACTION_device_groups)

    def __buildSpecial(self):
        
        self.e_parameter_sis18_extraction = self.e_parameter
        self.element_parameter_sis18_extraction = self.element_parameter
        self.isotope_parameter_sis18_extraction = self.isotope_parameter
        self.q_parameter_sis18_extraction = self.q_parameter
    # build special part of hierarchy for SIS18_EXTRACTION
    
        self.lh_builder.create_child_node(self.e_parameter, 'SIS18BEAM/E_START_END')
    
        for device in self.devices.septum:
            usep_parameter = self.reader.find_unique_string(device + '/USEP', self.lh_builder.lh.get_parameters())
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)

            
            voltages_parameter = (device + '/VOLTAGES#voltages')
            self.lh_builder.create_child_node(voltages_parameter, usep_parameter)
            self.lh_builder.lh.add_parameter_to_system(voltages_parameter, system)

            clvoltls1_parameter = (device + '/CLVOLTLS#cl1voltl')
            self.lh_builder.create_child_node(clvoltls1_parameter, voltages_parameter)
            self.lh_builder.lh.add_parameter_to_system(clvoltls1_parameter, system)

            clvoltls2_parameter = (device + '/CLVOLTLS#cl2voltl')
            self.lh_builder.create_child_node(clvoltls2_parameter, voltages_parameter)
            self.lh_builder.lh.add_parameter_to_system(clvoltls2_parameter, system)

            voltlows_parameter = (device + '/VOLTLOWS#voltlows')
            self.lh_builder.create_child_node(voltlows_parameter, voltages_parameter)
            self.lh_builder.lh.add_parameter_to_system(voltlows_parameter, system)

            clvolts1_parameter = (device + '/CLVOLTS#cl1volt')
            self.lh_builder.create_child_node(clvolts1_parameter, voltages_parameter)
            self.lh_builder.lh.add_parameter_to_system(clvolts1_parameter, system)

            clvolts2_parameter = (device + '/CLVOLTS#cl2volt')
            self.lh_builder.create_child_node(clvolts2_parameter, voltages_parameter)
            self.lh_builder.lh.add_parameter_to_system(clvolts2_parameter, system)


    def build(self):
        
        # build generic part of hierarchy
        GenericTransferlineHierarchy.build(self)
        
        # build special part of hierarchy
        self.__buildSpecial()

        GenericTransferlineHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_SIS18_EXTRACTION()
    h2.build()
    h2.generate()
