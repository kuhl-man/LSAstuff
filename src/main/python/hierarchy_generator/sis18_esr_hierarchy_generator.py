from generic_hierarchy_generator import GenericHierarchy

_winding_number_rations = {
                           'SIS18_RING' : 38 / 10 ,
                           'ESR_RING'   : 40 / 28
                           }

_coil_length_factors = {
                        'SIS18_RING' : 1 ,
                        'ESR_RING'   : 4
                        } 

class SIS18ESRHierarchy(GenericHierarchy):
    
    def __init__(self, device_groups):
        
        GenericHierarchy.__init__(self, device_groups)
        
    def generate_linkrules(self):
        
        GenericHierarchy.generate_linkrules(self)
    
    def build(self):
        GenericHierarchy.build(self)
        #build special generic part for SIS18 and ESR
        
        self.devices.horizontal_orbit_correction_coils = list(set(self.devices.horizontal_correction_coils)-set(self.devices.extraction_bump_correction_coils))
        
        for device in self.devices.extraction_bump_correction_coils:
            main_dipole_device = self.devices.main_dipoles[0]
            y_prec_KL = self.y_prec_parser.findYPrec(main_dipole_device, 'KL', 5.0e-7)
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'FLAT_K0L', device, y_prec=y_prec_KL)
            main_dipole_device = self.devices.main_dipoles[0]
            y_prec_BLCORR = self.y_prec_parser.findYPrec(main_dipole_device, 'BL', 5.0e-7 / _coil_length_factors.get(self.devices.accelerator_zone))
            blcorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BLCORR', 'CORRFLAT_B0L', device, y_prec=y_prec_BLCORR)
            y_prec_ICORR = self.y_prec_parser.findYPrec(device, 'ICORR', 1.0e-4)   
            icorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ICORR', 'ICORRFLAT', device, y_prec=y_prec_ICORR)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(blcorr_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(icorr_parameter, system)

        for device in self.devices.horizontal_orbit_correction_coils:
            main_dipole_device = self.devices.main_dipoles[0]
            y_prec_KL = self.y_prec_parser.findYPrec(main_dipole_device, 'KL', 5.0e-8)
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
            main_dipole_device = self.devices.main_dipoles[0]
            y_prec_BLCORR = self.y_prec_parser.findYPrec(main_dipole_device, 'BL', 5.0e-8 / _coil_length_factors.get(self.devices.accelerator_zone))
            blcorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BLCORR', 'CORR_B0L', device, y_prec=y_prec_BLCORR)
            y_prec_ICORR = self.y_prec_parser.findYPrec(device, 'ICORR', 1.0e-5)   
            icorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ICORR', 'ICORR', device, y_prec=y_prec_ICORR)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
        
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(blcorr_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(icorr_parameter, system)
        
        for device in self.devices.old_cavities_ampl:
            y_prec_URF = self.y_prec_parser.findYPrec(device, 'URF', 5.0e-5)
            urf_parameter = self.lh_builder.lh.define_physics_parameter(device + '/URF', 'URF', device, y_prec=y_prec_URF)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            #self.lh_builder.lh.define_hardware_parameter(device, 'BROTAMPL', 'highValue')

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(urf_parameter, system)

        for device in self.devices.old_cavities_freq:
            y_prec_FRF = self.y_prec_parser.findYPrec(device, 'FRF', 1.0e-6)
            frf_parameter = self.lh_builder.lh.define_physics_parameter(device + '/FRF', 'FRF', device, y_prec=y_prec_FRF)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(frf_parameter, system)
            
        for device in self.devices.old_cavities_phase:
            prf_parameter = self.lh_builder.lh.define_physics_parameter(device + '/PRF', 'PRF', device, y_prec=1)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(prf_parameter, system)

        ## Kicker parameters
#        self.kicker_knob_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', self.kicker_device)
#        self.lh_builder.lh.add_parameter_to_system(self.kicker_knob_parameter, 'KICKER')

        # relations
        ## Magnets
        for device in self.devices.horizontal_correction_coils:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter)
            blcorr_parameter = self.reader.find_unique_string(device + '/B[0-3]?LCORR$', self.lh_builder.lh.get_parameters())
            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            if device in self.devices.extraction_bump_correction_coils:
                self.lh_builder.create_child_node(blcorr_parameter, [ self.brho_parameter, kl_parameter ])
            else:
                self.lh_builder.create_child_node(blcorr_parameter, [ self.brho_parameter, kl_parameter, self.incorpip_parameter ], parent_parameter_order={self.brho_parameter : 1 , kl_parameter : 1})

            for dipol_device in self.devices.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                bl_parameter = self.reader.find_unique_string(dipol_device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(icorr_parameter, [ i_parameter, blcorr_parameter, bl_parameter ])
        
        ## old cavities
        for device in self.devices.old_cavities_ampl:
            urf_parameter = self.reader.find_unique_string(device + '/URF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_parameter, [ self.cavity2harmonic_parameter, self.incorpip_parameter, self.urfring_parameter, self.rf_manipulation_parameter ], parent_parameter_order={self.urfring_parameter : 1 , self.cavity2harmonic_parameter : 1})
            #rampvals_a_parameter = self.reader.find_unique_string(device[:-1] + 'A/RAMPVALS#data$', self.lh_builder.lh.get_parameters())

        for device in self.devices.old_cavities_freq:
            frf_parameter = self.reader.find_unique_string(device + '/FRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(frf_parameter, [ self.cavity2harmonic_parameter, self.incorpip_parameter, self.frev_parameter ], parent_parameter_order={self.frev_parameter : 1 , self.cavity2harmonic_parameter : 1})
            #rampvals_fs_parameter = self.reader.find_unique_string(device[:-1] + 'FS/RAMPVALS#data$', self.lh_builder.lh.get_parameters())

        for device in self.devices.old_cavities_phase:
            prf_parameter = self.reader.find_unique_string(device + '/PRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(prf_parameter, [ self.cavity2harmonic_parameter, self.incorpip_parameter, self.prfring_parameter], parent_parameter_order={self.prfring_parameter : 1 , self.cavity2harmonic_parameter : 1})
            #rampvals_p_parameter = self.reader.find_unique_string(device[:-1] + 'P/RAMPVALS#data$', self.lh_builder.lh.get_parameters())

            #brotampl_parameter = self.reader.find_unique_string(device[:-1] + 'A/BROTAMPL#highValue$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(brotampl_parameter, urf_parameter )

