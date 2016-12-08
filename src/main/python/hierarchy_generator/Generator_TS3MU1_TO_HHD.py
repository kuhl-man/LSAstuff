from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy

from init_lh_builder import INIT_LH_BUILDER

from ts3mu1_to_hhd_devices import TS3MU1_TO_HHD_DEVICES

class GENERATOR_TS3MU1_TO_HHD(GenericTransferlineHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):
        
        if not hasattr(self, 'lh_builder'):
            raise Exception("No particle transfer defined for stand alone generation.")
        
        TS3MU1_TO_HHD_device_groups = TS3MU1_TO_HHD_DEVICES()
        GenericTransferlineHierarchy.__init__(self, TS3MU1_TO_HHD_device_groups)

    def __buildSpecial(self):
        self.e_parameter_ts3mu1_to_hhd = self.e_parameter
        self.element_parameter_ts3mu1_to_hhd = self.element_parameter
        self.isotope_parameter_ts3mu1_to_hhd = self.isotope_parameter
        self.q_parameter_ts3mu1_to_hhd = self.q_parameter
    # build special part of hierarchy for TS3MU1_TO_HHD
        for device in self.devices.main_dipoles + self.devices.horizontal_correctors + self.devices.vertical_correctors + self.devices.main_quadrupoles + self.devices.main_sextupoles:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())

            fields_parameter = (device + '/FIELDS#fields')
            self.lh_builder.create_child_node(fields_parameter, bl_parameter)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(fields_parameter, system)

    def build(self):
        
        # build generic part of hierarchy
        GenericTransferlineHierarchy.build(self)
        
        # build special part of hierarchy
        self.__buildSpecial()

        GenericTransferlineHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_TS3MU1_TO_HHD()
    h2.build()
    h2.generate()
