from sis18_esr_hierarchy_generator import SIS18ESRHierarchy

from init_lh_builder import INIT_LH_BUILDER

from esr_properties import ESR_PROPERTIES

from esr_devices import ESR_DEVICES

class ESRGenerator(SIS18ESRHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):
        
        if not hasattr(self, 'lh_builder'):
            ESR_properties = ESR_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, ESR_properties)
        
        esr_device_groups = ESR_DEVICES()
        SIS18ESRHierarchy.__init__(self, esr_device_groups)
        
    def __buildSpecial(self):
        # build special part of hierarchy for ESR

        for device in self.devices.polefacewindings:
            self.lh_builder.lh.define_physics_parameter(device + '/IPFW', 'IPFW', device)

        ## relations

        ## Optics Parameters
        # remove some relations for opticsip parameter
        self.lh_builder.remove_child_node(self.opticsip_parameter, [ self.tau_start_end_parameter, self.tgrid_parameter, self.tround_parameter, self.t_wait_parameter, self.gamma_parameter ])

        self.lh_builder.create_child_node(self.opticsip_parameter, [ self.bp_length_parameter, self.tau_start_end_parameter, self.incorpip_parameter ])

        ## Timeparam Parameters
        self.lh_builder.create_child_node(self.bp_length_parameter, [ self.t_bp_length_parameter, self.t_wait_parameter, self.tau_start_end_parameter, self.tround_parameter,  self.bdot_parameter, self.brho_start_end_parameter, self.tgrid_parameter ], parent_parameter_order={self.t_bp_length_parameter : 1})

        ## Magnets
        for device in self.devices.polefacewindings:
            ipfw_parameter = self.reader.find_unique_string(device + '/IPFW$', self.lh_builder.lh.get_parameters())

            for dipol_device in self.devices.main_dipoles:
                bl_parameter = self.reader.find_unique_string(dipol_device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(ipfw_parameter, [ bl_parameter , self.incorpip_parameter ])

    def build(self):
        
        # build generic part of hierarchy
        SIS18ESRHierarchy.build(self)
                
        # build special part of hierarchy for ESR
        self.__buildSpecial()
        
        SIS18ESRHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = ESRGenerator()
    h2.build()
    h2.generate()
