from generic_line_hierarchy_generator import GenericLineHierarchy

from init_lh_builder import INIT_LH_BUILDER

from cryring_tey1_properties import CRYRING_TEY1_PROPERTIES

from cryring_tey1_devices import CRYRING_TEY1_DEVICES

class GENERATOR_CRYRING_TEY1(GenericLineHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        if not hasattr(self, 'lh_builder'):
            cryring_tey1_properties = CRYRING_TEY1_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, cryring_tey1_properties)
        
        CRYRING_device_groups = CRYRING_TEY1_DEVICES()
        GenericLineHierarchy.__init__(self, CRYRING_device_groups)

        self.yrme_bp = False
        self.yrle_bp = False

        self.standalone_acczone = True


    def __buildSpecial(self):
        # build special part of hierarchy for CRYRING

	## link to hardware parameters
	self.lh_builder.create_child_node('GHTYQD21/Setting#current', 'GHTYQD21/I')
	self.lh_builder.create_child_node('GHTYQD22/Setting#current', 'GHTYQD22/I')
	self.lh_builder.create_child_node('GHTYQD31/Setting#current', 'GHTYQD31/I')
	self.lh_builder.create_child_node('GHTYQD32/Setting#current', 'GHTYQD32/I')

	self.lh_builder.create_child_node('GHTYMH2/Setting#current', 'GHTYMH2/I')

	self.lh_builder.create_child_node('GHTYKV2/Setting#current', 'GHTYKV2/I')
	self.lh_builder.create_child_node('GHTYKH2/Setting#current', 'GHTYKH2/I')


    def build(self):
        
        # build generic part of hierarchy
        GenericLineHierarchy.build(self)
        
        # build special part of hierarchy
        self.__buildSpecial()
        
        GenericLineHierarchy.generate_linkrules(self)

    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_CRYRING_TEY1()
    h2.build()
    h2.generate()
