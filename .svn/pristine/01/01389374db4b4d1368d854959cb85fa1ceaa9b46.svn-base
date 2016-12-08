from generic_hierarchy_generator import GenericHierarchy

_winding_number_rations = {
                           'SIS18_RING' : 38 / 10 ,
                           'ESR_RING'   : 40 / 28 ,
			   'CRYRING_RING' : 72 / 32
                           }

_coil_length_factors = {
                        'SIS18_RING' : 1 ,
                        'ESR_RING'   : 4 ,
			'CRYRING_RING' : 1
                        } 

from init_lh_builder import INIT_LH_BUILDER

from cryring_properties import CRYRING_PROPERTIES

from cryring_ring_devices import CRYRING_RING_DEVICES

class CRYRINGGenerator(GenericHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        if not hasattr(self, 'lh_builder'):
            cryring_properties = CRYRING_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, cryring_properties)
        
        CRYRING_device_groups = CRYRING_RING_DEVICES()
        GenericHierarchy.__init__(self, CRYRING_device_groups)
        self.eddycurrents = False
        self.rfmanipualtion = False

    def __buildSpecial(self):
        # build special part of hierarchy for CRYRING

	### special parameters ----------------------------------------------------------------------------------------------------------

        ## Bumper

        ## logical devices to provide generic hardware parameters for voltage and fall time setting
	self.lh_builder.lh.define_device('YR01LB', 'BUMPER', self.devices.accelerator_zone)

        kl_parameter            = self.lh_builder.lh.define_physics_parameter('YR01LB/KL',                 'SCALAR_K0L',        'YR01LB')
	u_parameter             = self.lh_builder.lh.define_physics_parameter('YR01LB/U',                  'SCALAR_U',          'YR01LB') 
        tfall_parameter         = self.lh_builder.lh.define_physics_parameter('YR01LB/TFALL',              'SCALAR_TFALL',      'YR01LB')
        tfall_setting_parameter = self.lh_builder.lh.define_physics_parameter('YR01LB/TSET#',              'SCALAR_TAU_NLP',    'YR01LB')
        power_parameter         = self.lh_builder.lh.define_physics_parameter('YR01LB/USE_1K_POWER_SUPPLY','SCALAR_ACTIVE',     'YR01LB')
        power_int_parameter     = self.lh_builder.lh.define_physics_parameter('YR01LB/USED_POWER_SUPPLY#', 'SCALAR_KICKER_MODE','YR01LB')

	# does not work with old parammodi
	# t_master_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/TIMING_MASTER', 'SCALAR_TIMING_MASTER', self.timeparam_device, belongs_to_function_bproc=True)


        self.lh_builder.lh.add_parameter_to_system(kl_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'BUMPER')

        self.lh_builder.lh.add_parameter_to_system(tfall_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(tfall_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(tfall_parameter, 'BUMPER')

        self.lh_builder.lh.add_parameter_to_system(power_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(power_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(power_parameter, 'BUMPER')

	self.lh_builder.lh.add_parameter_to_system(u_parameter, 'BUMPER')
        self.lh_builder.lh.add_parameter_to_system(tfall_setting_parameter, 'BUMPER')
        self.lh_builder.lh.add_parameter_to_system(power_int_parameter, 'BUMPER')

        # does not work with old parammodi
        # self.lh_builder.lh.add_parameter_to_system(t_master_parameter, system)


	# use other parameter_types, it's only needed to get the link to the device
        for device in self.devices.bumper:
                link_parameter = self.lh_builder.lh.define_physics_parameter(device + '/LINK_TO_DEVICE', 'SCALAR_TAU_NLP', device)

                system = self.devices.devicesystemmap.get(device)
                print (device , system)
                self.lh_builder.lh.add_parameter_to_system(link_parameter, system)
	


	## backleg winding correction coil
        for device in self.devices.horizontal_correction_coils:
            main_dipole_device = self.devices.main_dipoles[0]
            y_prec_KL = self.y_prec_parser.findYPrec(main_dipole_device, 'KL', 5.0e-5)
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
            main_dipole_device = self.devices.main_dipoles[0]
            y_prec_BLCORR = self.y_prec_parser.findYPrec(main_dipole_device, 'BL', 5.0e-5 / _coil_length_factors.get(self.devices.accelerator_zone))
            blcorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BLCORR', 'CORR_B0L', device, y_prec=y_prec_BLCORR)
            y_prec_ICORR = self.y_prec_parser.findYPrec(device, 'ICORR', 1.0e-2)   
            icorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ICORR', 'ICORR', device, y_prec=y_prec_ICORR)
        
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(blcorr_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(icorr_parameter, system)

        for device in self.devices.cavities:
            eff_parameter = self.lh_builder.lh.define_physics_parameter(device + '/EFFICIENCY', 'EFFICIENCY', device)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(eff_parameter, system)


	### special relations ----------------------------------------------------------------------------------------------------------
        ### Creation of relations

        ## Beam parameters
###        self.lh_builder.create_child_node(self.inj_emil_parameter, [ self.dp_over_p_parameter, self.e_parameter, self.h_parameter ])

        ## Bumper
        for device in self.devices.bumper:

            kl_parameter = self.reader.find_unique_string('YR01LB/KL$', self.lh_builder.lh.get_parameters())
            u_parameter  = self.reader.find_unique_string('YR01LB/U$',  self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(u_parameter, [ self.erho_parameter, kl_parameter, tfall_parameter, power_parameter ])

            tfall_setting_parameter = self.reader.find_unique_string('YR01LB/TSET#$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(tfall_setting_parameter, [ tfall_parameter, power_parameter ] )

            power_int_parameter = self.reader.find_unique_string('YR01LB/USED_POWER_SUPPLY#$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(power_int_parameter, power_parameter )


	    # the timing master is a child of the selected power supply, because the delay times for the two power supplies are different
            # does not work with old parammodi
            # t_master_parameter = self.reader.find_unique_string(self.timeparam_device + '/TIMING_MASTER$', self.lh_builder.lh.get_parameters())
            # self.lh_builder.create_child_node(t_master_parameter, power_parameter)

        ## backleg winding correction coil
        for device in self.devices.horizontal_correction_coils:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter)

            blcorr_parameter = self.reader.find_unique_string(device + '/B[0-3]?LCORR$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(blcorr_parameter, [ self.brho_parameter, kl_parameter, self.incorpip_parameter ], parent_parameter_order={self.brho_parameter : 1 , kl_parameter : 1})

            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            for dipol_device in self.devices.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                bl_parameter = self.reader.find_unique_string(dipol_device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(icorr_parameter, [ i_parameter, blcorr_parameter, bl_parameter ])

        ## Cavity
        for device in self.devices.cavities:
            frf_parameter = self.reader.find_unique_string(device + '/FRF$', self.lh_builder.lh.get_parameters())
            urf_parameter = self.reader.find_unique_string(device + '/URF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_parameter, frf_parameter )


    def build(self):
        
        # build generic part of hierarchy
        GenericHierarchy.build(self)
        
        # build special part of hierarchy for CRYRING
        self.__buildSpecial()
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = CRYRINGGenerator()
    h2.build()
    h2.generate()
