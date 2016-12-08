from generic_line_hierarchy_generator import GenericLineHierarchy

from init_lh_builder import INIT_LH_BUILDER

from cryring_yrle_properties import CRYRING_YRLE_PROPERTIES

from cryring_yrle_devices import CRYRING_YRLE_DEVICES

class GENERATOR_CRYRING_YRLE(GenericLineHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        self.standalone_acczone = True
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            cryring_yrle_properties = CRYRING_YRLE_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, cryring_yrle_properties)
        
        CRYRING_device_groups = CRYRING_YRLE_DEVICES()
        GenericLineHierarchy.__init__(self, CRYRING_device_groups)

        self.yrle_bp = True
        self.yrme_bp = False

    def __buildSpecial(self):
        # build special part of hierarchy for CRYRING

	### special parameters ----------------------------------------------------------------------------------------------------------

        for device in self.devices.electrostatic_quadrupole:

	    if (device == 'YRT1LE1'):

			unull_parameter      = self.lh_builder.lh.define_physics_parameter(device + '/U0','U_QUAD', device)
			u_parameter          = self.lh_builder.lh.define_physics_parameter(device + '/U', 'SCALAR_U', device)

            		system = self.devices.devicesystemmap.get(device)
            		print (device , system)
            
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, system)
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, '-TOPLEVEL')
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, 'generation')
            		self.lh_builder.lh.add_parameter_to_system(u_parameter,  system)


	    if (device == 'YRT1LD21'):

			unull_parameter   = self.lh_builder.lh.define_physics_parameter(device + '/U0', 'U_QUAD',   device, y_prec=4)
			knob_parameter    = self.lh_builder.lh.define_physics_parameter(device + '/KNOB', 'SCALAR_ASYMMETRY_KNOB', device)
			knobhor_parameter = self.lh_builder.lh.define_physics_parameter(device + '/HORSTEER', 'SCALAR_HOR_STEER_KNOB', device)
			knobver_parameter = self.lh_builder.lh.define_physics_parameter(device + '/VERSTEER', 'SCALAR_VER_STEER_KNOB', device)
           		uright_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/URIGHT',  'U_RIGHT', device)
           		uleft_parameter   = self.lh_builder.lh.define_physics_parameter(device + '/ULEFT',   'U_LEFT',  device)
           		ubottom_parameter = self.lh_builder.lh.define_physics_parameter(device + '/UBOTTOM', 'U_BOTTOM',   device) 
           		utop_parameter    = self.lh_builder.lh.define_physics_parameter(device + '/UTOP',    'U_TOP',device)

           		# urightsetting_parameter   = self.lh_builder.lh.define_physics_parameter(device + '/URIGHT#',   'HVPowerSupply/Setting#voltage', device)
           		# uleftsetting_parameter    = self.lh_builder.lh.define_physics_parameter(device + '/ULEFT#',    'HVPowerSupply/Setting#voltage', device)
           		# utopsetting_parameter     = self.lh_builder.lh.define_physics_parameter(device + '/UTOP#',     'HVPowerSupply/Setting#voltage', device)
           		# ubottomsetting_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/UBOTTOM#',  'HVPowerSupply/Setting#voltage', device)

            		system = self.devices.devicesystemmap.get(device)
            		print (device , system)
            
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, system)
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, '-TOPLEVEL')
            		self.lh_builder.lh.add_parameter_to_system(unull_parameter, 'generation')
            		self.lh_builder.lh.add_parameter_to_system(knob_parameter, system)
            		self.lh_builder.lh.add_parameter_to_system(knob_parameter, '-TOPLEVEL')
            		self.lh_builder.lh.add_parameter_to_system(knob_parameter, 'generation')
            		self.lh_builder.lh.add_parameter_to_system(knobhor_parameter, system)
            		self.lh_builder.lh.add_parameter_to_system(knobhor_parameter, '-TOPLEVEL')
            		self.lh_builder.lh.add_parameter_to_system(knobhor_parameter, 'generation')
            		self.lh_builder.lh.add_parameter_to_system(knobver_parameter, system)
            		self.lh_builder.lh.add_parameter_to_system(knobver_parameter, '-TOPLEVEL')
            		self.lh_builder.lh.add_parameter_to_system(knobver_parameter, 'generation')
            		self.lh_builder.lh.add_parameter_to_system(uright_parameter,  system)
            		self.lh_builder.lh.add_parameter_to_system(uleft_parameter,  system)
            		self.lh_builder.lh.add_parameter_to_system(ubottom_parameter,  system)
            		self.lh_builder.lh.add_parameter_to_system(utop_parameter,  system)
            		# self.lh_builder.lh.add_parameter_to_system(urightsetting_parameter,  system)
            		# self.lh_builder.lh.add_parameter_to_system(uleftsetting_parameter,  system)
            		# self.lh_builder.lh.add_parameter_to_system(ubottomsetting_parameter,  system)
            		# self.lh_builder.lh.add_parameter_to_system(utopsetting_parameter,  system)


	    if (			     (device == 'YRT1LD22')
		or (device == 'YRT1LT31') or (device == 'YRT1LT32') or (device == 'YRT1LT33') 
		or (device == 'YRT1LT41') or (device == 'YRT1LT42') or (device == 'YRT1LT43')
	       ):
			unull_parameter = self.lh_builder.lh.define_physics_parameter(device + '/U0',   'U_QUAD',   device, y_prec=4)
			knob_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/KNOB', 'SCALAR_ASYMMETRY_KNOB', device)
			uhor_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/UHOR', 'U_HOR', device)
			uver_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/UVER', 'U_VER', device)
           		# uhorsetting_parameter   = self.lh_builder.lh.define_physics_parameter(device + '/UHOR#',   'HVPowerSupply/Setting#voltage', device)
           		# uversetting_parameter   = self.lh_builder.lh.define_physics_parameter(device + '/UVER#',   'HVPowerSupply/Setting#voltage', device)

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
            		# self.lh_builder.lh.add_parameter_to_system(uhorsetting_parameter,  system)
            		# self.lh_builder.lh.add_parameter_to_system(uversetting_parameter,  system)


        for device in self.devices.chopper:

		u_parameter       = self.lh_builder.lh.define_physics_parameter('YRT1LC1_V/U', 'U', 'YRT1LC1_V', y_prec=8)
		kl_parameter      = self.lh_builder.lh.define_physics_parameter('YRT1LC1_V/KL', 'K0L', 'YRT1LC1_V', y_prec=8)
	        thigh_parameter   = self.lh_builder.lh.define_physics_parameter('YRT1LC1_V/TCHOP', 'SCALAR_THIGH', 'YRT1LC1_V', y_prec=8)
	        toffset_parameter = self.lh_builder.lh.define_physics_parameter('YRT1LC1_V/TOFFSET', 'SCALAR_TOFFSET', 'YRT1LC1_V', y_prec=8)
	        uchop_parameter   = self.lh_builder.lh.define_physics_parameter('YRT1LC1_V/UCHOP', 'UCHOP', 'YRT1LC1_V', y_prec=8)

	        system = self.devices.devicesystemmap.get('YRT1LC1_V')
	        print ('YRT1LC1_V' , system)

	        self.lh_builder.lh.add_parameter_to_system(u_parameter, system)
	        self.lh_builder.lh.add_parameter_to_system(u_parameter, '-TOPLEVEL')
	        self.lh_builder.lh.add_parameter_to_system(u_parameter, 'generation')
	        self.lh_builder.lh.add_parameter_to_system(thigh_parameter, system)
	        self.lh_builder.lh.add_parameter_to_system(thigh_parameter, '-TOPLEVEL')
	        self.lh_builder.lh.add_parameter_to_system(thigh_parameter, 'generation')
	        self.lh_builder.lh.add_parameter_to_system(toffset_parameter, system)
	        self.lh_builder.lh.add_parameter_to_system(toffset_parameter, '-TOPLEVEL')
	        self.lh_builder.lh.add_parameter_to_system(toffset_parameter, 'generation')
	        self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
	        self.lh_builder.lh.add_parameter_to_system(uchop_parameter, system)

 
	### special relations ----------------------------------------------------------------------------------------------------------
        ### Creation of relations

        ## electrostatic quadrupole
        for device in self.devices.electrostatic_quadrupole:

	    if (device == 'YRT1LE1'):
            		unull_parameter = self.reader.find_unique_string(device + '/U0',  self.lh_builder.lh.get_parameters())

            		u_parameter = self.reader.find_unique_string(device + '/U$',  self.lh_builder.lh.get_parameters())
		    	self.lh_builder.create_child_node(u_parameter, [ self.erho_parameter, unull_parameter ])


	    if (device == 'YRT1LD21'):

            		unull_parameter   = self.reader.find_unique_string(device + '/U0',      self.lh_builder.lh.get_parameters())
	    		knob_parameter    = self.reader.find_unique_string(device + '/KNOB',    self.lh_builder.lh.get_parameters())
	    		knobhor_parameter = self.reader.find_unique_string(device + '/HORSTEER', self.lh_builder.lh.get_parameters())
	    		knobver_parameter = self.reader.find_unique_string(device + '/VERSTEER', self.lh_builder.lh.get_parameters())

	            	uright_parameter  = self.reader.find_unique_string(device + '/URIGHT$', self.lh_builder.lh.get_parameters())
	            	uleft_parameter   = self.reader.find_unique_string(device + '/ULEFT$',  self.lh_builder.lh.get_parameters())
	            	ubottom_parameter = self.reader.find_unique_string(device + '/UBOTTOM$',self.lh_builder.lh.get_parameters())
	            	utop_parameter    = self.reader.find_unique_string(device + '/UTOP$',   self.lh_builder.lh.get_parameters())

	            	# urightsetting_parameter  = self.reader.find_unique_string(device + '/URIGHT#$', self.lh_builder.lh.get_parameters())
	            	# uleftsetting_parameter   = self.reader.find_unique_string(device + '/ULEFT#$',  self.lh_builder.lh.get_parameters())
	            	# ubottomsetting_parameter = self.reader.find_unique_string(device + '/UBOTTOM#$',self.lh_builder.lh.get_parameters())
	            	# utopsetting_parameter    = self.reader.find_unique_string(device + '/UTOP#$',   self.lh_builder.lh.get_parameters())

		    	self.lh_builder.create_child_node(uright_parameter,  [ self.epercharge_parameter, unull_parameter, knob_parameter, knobhor_parameter, knobver_parameter ])
		    	self.lh_builder.create_child_node(uleft_parameter,   [ self.epercharge_parameter, unull_parameter, knob_parameter, knobhor_parameter, knobver_parameter ])
		    	self.lh_builder.create_child_node(ubottom_parameter, [ self.epercharge_parameter, unull_parameter, knob_parameter, knobhor_parameter, knobver_parameter ])
		    	self.lh_builder.create_child_node(utop_parameter,    [ self.epercharge_parameter, unull_parameter, knob_parameter, knobhor_parameter, knobver_parameter ])

		    	# self.lh_builder.create_child_node(urightsetting_parameter,  [ uright_parameter  ])
		    	# self.lh_builder.create_child_node(uleftsetting_parameter,   [ uleft_parameter   ])
		    	# self.lh_builder.create_child_node(ubottomsetting_parameter, [ ubottom_parameter ])
		    	# self.lh_builder.create_child_node(utopsetting_parameter,    [ utop_parameter    ])


	    if (			     (device == 'YRT1LD22')
		or (device == 'YRT1LT31') or (device == 'YRT1LT32') or (device == 'YRT1LT33')
		or (device == 'YRT1LT41') or (device == 'YRT1LT42') or (device == 'YRT1LT43')
	       ):

            		unull_parameter = self.reader.find_unique_string(device + '/U0',    self.lh_builder.lh.get_parameters())
	    		knob_parameter  = self.reader.find_unique_string(device + '/KNOB',  self.lh_builder.lh.get_parameters())
	            	uhor_parameter  = self.reader.find_unique_string(device + '/UHOR$', self.lh_builder.lh.get_parameters())
	            	uver_parameter  = self.reader.find_unique_string(device + '/UVER$', self.lh_builder.lh.get_parameters())

		    	self.lh_builder.create_child_node(uhor_parameter, [ self.epercharge_parameter, unull_parameter, knob_parameter ])
		    	self.lh_builder.create_child_node(uver_parameter, [ self.epercharge_parameter, unull_parameter, knob_parameter ])

###		    	self.lh_builder.create_child_node(uhor_parameter, [ self.e_parameter, self.q_parameter, self.isotope_parameter, unull_parameter, knob_parameter ])
###		    	self.lh_builder.create_child_node(uver_parameter, [ self.e_parameter, self.q_parameter, self.isotope_parameter, unull_parameter, knob_parameter ])


        ## as chopper use either electrostatic bender or bottom plate of first quadrupole
        for device in self.devices.chopper:
	    u_parameter  = self.reader.find_unique_string(device + '/U$', self.lh_builder.lh.get_parameters())
	    kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
            toffset_parameter = self.reader.find_unique_string(device + '/TOFFSET$', self.lh_builder.lh.get_parameters())
            thigh_parameter = self.reader.find_unique_string(device + '/TCHOP$', self.lh_builder.lh.get_parameters())
            uchop_parameter = self.reader.find_unique_string(device + '/UCHOP$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ self.erho_parameter, u_parameter ] )
            self.lh_builder.create_child_node(uchop_parameter, [self.erho_parameter, kl_parameter, thigh_parameter, toffset_parameter ] )

            if self.standalone_acczone:
	      self.lh_builder.create_child_node(self.t_pulse_parameter, [ thigh_parameter ] )


	## link to hardware parameters
	# magnets
	self.lh_builder.create_child_node('YRT1MH1/Setting#current', 'YRT1MH1/I')
	self.lh_builder.create_child_node('YRT1KH1/Setting#current', 'YRT1KH1/I')
	self.lh_builder.create_child_node('YRT1KV1/Setting#current', 'YRT1KV1/I')

	# electrostatic devices
	# self.lh_builder.create_child_node('YRT1LE1/Setting#voltage', 'YRT1LE1/U')

	self.lh_builder.create_child_node('YRT1LC1_V/Setting#voltageS', 'YRT1LC1_V/UCHOP')

	self.lh_builder.create_child_node('YRT1LD21O/Setting#voltageS', 'YRT1LD21/UTOP')
	self.lh_builder.create_child_node('YRT1LD21U/Setting#voltageS', 'YRT1LD21/UBOTTOM')
	self.lh_builder.create_child_node('YRT1LD21R/Setting#voltageS', 'YRT1LD21/URIGHT')
	self.lh_builder.create_child_node('YRT1LD21L/Setting#voltageS', 'YRT1LD21/ULEFT')

	self.lh_builder.create_child_node('YRT1LD22/Setting#voltageH', 'YRT1LD22/UHOR')
	self.lh_builder.create_child_node('YRT1LD22/Setting#voltageV', 'YRT1LD22/UVER')

	self.lh_builder.create_child_node('YRT1LT31/Setting#voltageH', 'YRT1LT31/UHOR')
	self.lh_builder.create_child_node('YRT1LT31/Setting#voltageV', 'YRT1LT31/UVER')
	self.lh_builder.create_child_node('YRT1LT32/Setting#voltageH', 'YRT1LT32/UHOR')
	self.lh_builder.create_child_node('YRT1LT32/Setting#voltageV', 'YRT1LT32/UVER')
	self.lh_builder.create_child_node('YRT1LT33/Setting#voltageH', 'YRT1LT33/UHOR')
	self.lh_builder.create_child_node('YRT1LT33/Setting#voltageV', 'YRT1LT33/UVER')

	self.lh_builder.create_child_node('YRT1LT41/Setting#voltageH', 'YRT1LT41/UHOR')
	self.lh_builder.create_child_node('YRT1LT41/Setting#voltageV', 'YRT1LT41/UVER')
	self.lh_builder.create_child_node('YRT1LT42/Setting#voltageH', 'YRT1LT42/UHOR')
	self.lh_builder.create_child_node('YRT1LT42/Setting#voltageV', 'YRT1LT42/UVER')
	self.lh_builder.create_child_node('YRT1LT43/Setting#voltageH', 'YRT1LT43/UHOR')
	self.lh_builder.create_child_node('YRT1LT43/Setting#voltageV', 'YRT1LT43/UVER')


    def build(self):
        
        # build generic part of hierarchy
        GenericLineHierarchy.build(self)
        
        # build special part of hierarchy
        self.__buildSpecial()

        GenericLineHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
    
    h2 = GENERATOR_CRYRING_YRLE()
    h2.build()
    h2.generate()
