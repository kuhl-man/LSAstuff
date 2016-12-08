from generic_line_hierarchy_generator import GenericLineHierarchy

from init_lh_builder import INIT_LH_BUILDER

from cryring_tyr1_properties import CRYRING_TYR1_PROPERTIES

from cryring_tyr1_devices import CRYRING_TYR1_DEVICES

class GENERATOR_CRYRING_TYR1(GenericLineHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        if not hasattr(self, 'lh_builder'):
            cryring_tyr1_properties = CRYRING_TYR1_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, cryring_tyr1_properties)
        
        CRYRING_device_groups = CRYRING_TYR1_DEVICES()
        GenericLineHierarchy.__init__(self, CRYRING_device_groups)

        self.yrle_bp = False
        self.yrme_bp = False
        self.standalone_acczone = True

    def __buildSpecial(self):
        # build special part of hierarchy for CRYRING

	print (' build special part of TYR1')

        for device in self.devices.vertical_correctors:

		## link to hardware parameters
		self.lh_builder.create_child_node('YRT1MH2/Setting#current', 'YRT1MH2/I')
		self.lh_builder.create_child_node('GHTYKV3/Setting#current', 'GHTYKV3/I')
		self.lh_builder.create_child_node('GHTYQD41/Setting#current','GHTYQD41/I')
		self.lh_builder.create_child_node('GHTYQD42/Setting#current','GHTYQD42/I')

		#self.lh_builder.create_child_node('YR01MP1/Setting#current','YR01MP1/I')	
		#self.lh_builder.create_child_node('YR01LP1/Setting#voltage','YR01LP1/I')
		#self.lh_builder.create_child_node('YR01LP2/Setting#voltage','YR01LP2/I')

	print (' finish build special part of TYR1')


    def build(self):
        
	print (' build generic part of TYR1')
        # build generic part of hierarchy
        GenericLineHierarchy.build(self)
        
	print (' call build special part of TYR1')

        # build special part of hierarchy
        self.__buildSpecial()
	print (' generate link rules of TYR1')

        GenericLineHierarchy.generate_linkrules(self)
      

	print (' done build of TYR1')


    def generate(self):
	print (' generate TYR1')
        self.lh_builder.export()

	print (' done generate TYR1')
        

if __name__ == '__main__':
        
    print (' def generator TYR1')
    h2 = GENERATOR_CRYRING_TYR1()
    print (' call build TYR1')
    h2.build()
    print (' call generate TYR1')
    h2.generate()
