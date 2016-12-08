from generic_line_hierarchy_generator import GenericLineHierarchy

from init_lh_builder import INIT_LH_BUILDER

from cryring_yrme_properties import CRYRING_YRME_PROPERTIES

from cryring_yrme_devices import CRYRING_YRME_DEVICES

class GENERATOR_CRYRING_YRME(GenericLineHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):
        
        self.standalone_acczone = True
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            cryring_yrme_properties = CRYRING_YRME_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, cryring_yrme_properties)
        
        CRYRING_device_groups = CRYRING_YRME_DEVICES()
        GenericLineHierarchy.__init__(self, CRYRING_device_groups)

        self.yrme_bp = True
        self.yrle_bp = False

    def __buildSpecial(self):
        # build special part of hierarchy for CRYRING

        for device in self.devices.cavities:
	    if (device == 'YRT1BR1'):
		    if self.standalone_acczone:
		      self.lh_builder.create_child_node(self.t_rf_pulse_parameter, [ device+'/T_PAUSE_PULSE_LENGTH' ] )
		      self.lh_builder.create_child_node(self.t_pulse_parameter, [ 'YRT1LC1_V/TCHOP' ] )

            	    self.lh_builder.create_child_node(self.element_parameter, [ 'YRLE_BEAM/ELEMENT' ] )
            	    self.lh_builder.create_child_node(self.isotope_parameter, [ 'YRLE_BEAM/ISOTOPE' ] )
            	    self.lh_builder.create_child_node(self.q_parameter, [ 'YRLE_BEAM/Q' ] )
            	    self.lh_builder.create_child_node(self.chopped_parameter, [ 'YRLE_BEAM/CHOPPED_BEAM' ] )

          	    epercharge_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/E_PER_CHARGE', 'SCALAR_E_PER_CHARGE', self.beam_device)
          	    self.lh_builder.lh.add_parameter_to_system(epercharge_parameter, 'BEAM')
                    self.lh_builder.create_child_node(epercharge_parameter, [ self.e_parameter, self.isotope_parameter, self.q_parameter ])


        for device in self.devices.electrostatic_quadrupole:

			unull_parameter = self.lh_builder.lh.define_physics_parameter(device + '/U0',   'U_QUAD',   device, y_prec=4)
			knob_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/KNOB', 'SCALAR_ASYMMETRY_KNOB', device)
			uhor_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/UHOR', 'U_HOR', device)
			uver_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/UVER', 'U_VER', device)

            		system = self.devices.devicesystemmap.get(device)
            		print (device , system)
            
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, system)
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, '-TOPLEVEL')
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, 'generation')
            		self.lh_builder.lh.add_parameter_to_system(knob_parameter, system)
            		self.lh_builder.lh.add_parameter_to_system(knob_parameter, '-TOPLEVEL')
            		self.lh_builder.lh.add_parameter_to_system(knob_parameter, 'generation')
            		self.lh_builder.lh.add_parameter_to_system(uhor_parameter,  system)
            		self.lh_builder.lh.add_parameter_to_system(uver_parameter,  system)

		    	self.lh_builder.create_child_node(uhor_parameter, [ epercharge_parameter, unull_parameter, knob_parameter ])
		    	self.lh_builder.create_child_node(uver_parameter, [ epercharge_parameter, unull_parameter, knob_parameter ])


	## link to hardware parameters
	# magnets
	self.lh_builder.create_child_node('YRT1KH2/Setting#current', 'YRT1KH2/I')
	self.lh_builder.create_child_node('YRT1KV2/Setting#current', 'YRT1KV2/I')

	self.lh_builder.create_child_node('YRT1QD61/Setting#current', 'YRT1QD61/I')
	self.lh_builder.create_child_node('YRT1QD62/Setting#current', 'YRT1QD62/I')
	self.lh_builder.create_child_node('YRT1QD71/Setting#current', 'YRT1QD71/I')
	self.lh_builder.create_child_node('YRT1QD72/Setting#current', 'YRT1QD72/I')

	# RFQ
	self.lh_builder.create_child_node('YRT1BR1/Setting#phase', 'YRT1BR1/PHASE_OFFSET')
	self.lh_builder.create_child_node('YRT1BR1/Setting#amplitude', 'YRT1BR1/U_TO_HARDWARE' )
	self.lh_builder.create_child_node('YRT1BR1/Setting#pulse', 'YRT1BR1/ACT_ON_BEAM')

	# electrostatic devices
	#self.lh_builder.create_child_node('YRT1LD51/Setting#voltageH', 'YRT1LD51/UHOR')
	#self.lh_builder.create_child_node('YRT1LD51/Setting#voltageV', 'YRT1LD51/UVER')
	#self.lh_builder.create_child_node('YRT1LD52/Setting#voltageH', 'YRT1LD52/UHOR')
	#self.lh_builder.create_child_node('YRT1LD52/Setting#voltageV', 'YRT1LD52/UVER')



    def build(self):
        
        # build generic part of hierarchy
        GenericLineHierarchy.build(self)
        
        # build special part of hierarchy
        self.__buildSpecial()
        
        GenericLineHierarchy.generate_linkrules(self)

    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = GENERATOR_CRYRING_YRME()
    h2.build()
    h2.generate()
