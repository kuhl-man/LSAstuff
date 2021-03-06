from generic_hierarchy_generator import GenericHierarchy

_winding_number_rations = {
                           'SIS18' : 38 / 10 ,
                           'ESR'   : 40 / 28 ,
			   'CRYRING' : 72 / 32,
			   'HESR' : 100 / 1
                           }

_coil_length_factors = {
                        'SIS18' : 1 ,
                        'ESR'   : 4 ,
			'CRYRING' : 1 ,
			'HESR' : 1
                        } 


from init_lh_builder import INIT_LH_BUILDER

from hesr_ring_properties import HESR_RING_PROPERTIES

from hesr_ring_devices import HESR_RING_DEVICES

class HESRGenerator(GenericHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):
        
        if not hasattr(self, 'lh_builder'):
            HESR_ring_properties = HESR_RING_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, HESR_ring_properties)

        
        HESR_device_groups = HESR_RING_DEVICES()
        GenericHierarchy.__init__(self, HESR_device_groups)
        self.eddycurrents = False
        
#    def __buildSpecial(self):

        # build special part of hierarchy for CRYRING

	### special parameters ----------------------------------------------------------------------------------------------------------
        ## Beam parameters
###        self.dp_over_p_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DP_OVER_P', 'SCALAR_DP_OVER_P', self.beam_device, belongs_to_function_bproc=False)


        ## Bumper
#        self.lh_builder.lh.define_device(self.bumper_device, 'BUMPER', self.devices.particle_transfer)

        # Bumper parameters --- do the power supplies provide any curvature other than a linear ramp down to 0 volts? 
#        self.curvature_parameter = self.lh_builder.lh.define_physics_parameter(self.bumper_device + '/CURVATURE', 'SCALAR_BUMPER_CURVATURE', self.bumper_device)
#        self.bumper_knob_parameter = self.lh_builder.lh.define_physics_parameter(self.bumper_device + '/KNOB', 'SCALAR_BUMPER_KNOB', self.bumper_device)
#        self.tfall_parameter = self.lh_builder.lh.define_physics_parameter(self.bumper_device + '/TFALL', 'SCALAR_TFALL', self.bumper_device)
        
#        self.lh_builder.lh.add_parameter_to_system(self.curvature_parameter, 'BUMPER') 
#        self.lh_builder.lh.add_parameter_to_system(self.bumper_knob_parameter, 'BUMPER') 
#        self.lh_builder.lh.add_parameter_to_system(self.tfall_parameter, 'BUMPER') 

#        for device in self.devices.bumper:
#            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
####            el_parameter = self.lh_builder.lh.define_physics_parameter(device + '/EL', 'SCALAR_E0L', device)
#            u_parameter = self.lh_builder.lh.define_physics_parameter(device + '/U', 'SCALAR_U', device)
#            tfall_parameter = self.lh_builder.lh.define_physics_parameter(device + '/TFALL', 'SCALAR_TFALL', device)
#            
#            system = self.devices.devicesystemmap.get(device)
#            print (device , system)
#            
#            self.lh_builder.lh.add_parameter_to_system(kl_parameter, '-TOPLEVEL')
#            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
#            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
####            self.lh_builder.lh.add_parameter_to_system(el_parameter, system)
#            self.lh_builder.lh.add_parameter_to_system(u_parameter, system)
#            self.lh_builder.lh.add_parameter_to_system(tfall_parameter, '-TOPLEVEL')
#            self.lh_builder.lh.add_parameter_to_system(tfall_parameter, 'generation')
#            self.lh_builder.lh.add_parameter_to_system(tfall_parameter, system)
#
#	## backleg winding correction coil
#        for device in self.devices.horizontal_correction_coils:
#            main_dipole_device = self.devices.main_dipoles[0]
#            y_prec_KL = self.y_prec_parser.findYPrec(main_dipole_device, 'KL', 5.0e-5)
#            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
#            main_dipole_device = self.devices.main_dipoles[0]
#            y_prec_BLCORR = self.y_prec_parser.findYPrec(main_dipole_device, 'BL', 5.0e-5 / _coil_length_factors.get(self.devices.accelerator))
#            blcorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BLCORR', 'CORR_B0L', device, y_prec=y_prec_BLCORR)
#            y_prec_ICORR = self.y_prec_parser.findYPrec(device, 'ICORR', 1.0e-2)   
#            icorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ICORR', 'ICORR', device, y_prec=y_prec_ICORR)
#        
#            system = self.devices.devicesystemmap.get(device)
#            print (device , system)
#            
#            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
#            self.lh_builder.lh.add_parameter_to_system(blcorr_parameter, system)
#            self.lh_builder.lh.add_parameter_to_system(icorr_parameter, system)
#


	### special relations ----------------------------------------------------------------------------------------------------------
        ### Creation of relations

        ## Beam parameters
###        self.lh_builder.create_child_node(self.inj_emil_parameter, [ self.dp_over_p_parameter, self.e_parameter, self.h_parameter ])

        ## Bumper
#        for device in self.devices.bumper:
#            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
#            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter )
#            self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, self.bumper_knob_parameter ])

###		makerule is missing! work around: set el  top level parameter 
###            el_parameter = self.reader.find_unique_string(device + '/EL$', self.lh_builder.lh.get_parameters())
###            self.lh_builder.create_child_node(el_parameter, [ self.erho_parameter, kl_parameter ])

#            u_parameter = self.reader.find_unique_string(device + '/U$', self.lh_builder.lh.get_parameters())
#            self.lh_builder.create_child_node(u_parameter, [ self.erho_parameter, kl_parameter ])
###            self.lh_builder.create_child_node(u_parameter, el_parameter )

        ## backleg winding correction coil
#        for device in self.devices.horizontal_correction_coils:
#            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
#            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter)#
#
#            blcorr_parameter = self.reader.find_unique_string(device + '/B[0-3]?LCORR$', self.lh_builder.lh.get_parameters())
#            self.lh_builder.create_child_node(blcorr_parameter, [ self.brho_parameter, kl_parameter, self.incorpip_parameter ], parent_parameter_order={self.brho_parameter : 1 , kl_parameter : 1})
#
#            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
#            for dipol_device in self.devices.main_dipoles:
#                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
#                bl_parameter = self.reader.find_unique_string(dipol_device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
#                self.lh_builder.create_child_node(icorr_parameter, [ i_parameter, blcorr_parameter, bl_parameter ])
#
#
#
#
    def build(self):
        
        # build generic part of hierarchy
        GenericHierarchy.build(self)
        
        # build special part of hierarchy for CRYRING
#        self.__buildSpecial()

        GenericHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = HESRGenerator()
    h2.build()
    h2.generate()
