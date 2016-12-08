from sis18_esr_hierarchy_generator import SIS18ESRHierarchy

from init_lh_builder import INIT_LH_BUILDER

from sis18_properties import SIS18_PROPERTIES

from sis18_devices import SIS18_DEVICES

class SIS18Generator(SIS18ESRHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):
        
        if not hasattr(self, 'lh_builder'):
            SIS18_properties = SIS18_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, SIS18_properties)
        
        SIS18_device_groups = SIS18_DEVICES()
        SIS18ESRHierarchy.__init__(self, SIS18_device_groups)
        
    def __buildSpecial(self):
        
        # remove inj emil parameter from system '-TOPLEVEL' and 'generation'
        self.lh_builder.remove_system(self.inj_emil_parameter, '-TOPLEVEL')
        self.lh_builder.remove_system(self.inj_emil_parameter, 'generation')
        
        # build special part of hierarchy for SIS18
        self.timing_device = 'GS00ZZ'
        self.kicker_timing_device = 'GS00ZGT'
        self.hardware_rf_device = 'GS00BE_F'
        self.cavity_sync_device = 'GS00BE_S'
        
        self.q_kicker = [ 'GS05MQ1' ]
        
        #self.q_kicker_device = self.devices.particle_transfer.replace('_RING','QKICKER')
        #self.lh_builder.lh.define_device(self.q_kicker_device, 'KICKER', self.devices.particle_transfer)

        # add kicker S05MK2E as logical device
        self.lh_builder.lh.define_device('S05MK2E', 'KICKER', self.devices.accelerator_zone)

        # define bumper device
        self.lh_builder.lh.define_device(self.bumper_device, 'BUMPER', self.devices.accelerator_zone)

        ## Beam parameters
        self.dp_over_p_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DP_OVER_P', 'SCALAR_DP_OVER_P', self.beam_device, belongs_to_function_bproc=False)

#        for device in self.devices.main_sextupoles:
#            kldelta_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KLDELTA', 'DELTA_K2L', device) ## KLDELTA soll nicht fuer S02KM5SS und S08KM5SS
#
#            system = self.devices.devicesystemmap.get(device)
#            print (device , system)
#            
#            self.lh_builder.lh.add_parameter_to_system(kldelta_parameter, system)
 

        ## Optics parameters
        self.scalar_sigma_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/SCALAR_SIGMA', 'SCALAR_SIGMA', self.optics_device)
        self.scalar_sigma_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/SIGMA_START_END', 'SCALAR_SIGMA_START_END', self.optics_device)
        self.sigma_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/SIGMA', 'SIGMA', self.optics_device)
        self.tau_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/TAU', 'TAU', self.optics_device)
        self.tau_endpoint_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/TAU_ENDPOINT', 'SCALAR_TAU_ENDPOINT', self.optics_device)
        self.tau_nlp_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/TAU_NLP', 'SCALAR_TAU_NLP', self.optics_device)

        self.lh_builder.lh.add_parameter_to_system(self.scalar_sigma_parameter, 'OPTICS')
        self.lh_builder.lh.add_parameter_to_system(self.scalar_sigma_start_end_parameter, 'OPTICS')
        self.lh_builder.lh.add_parameter_to_system(self.sigma_parameter, 'OPTICS')
        self.lh_builder.lh.add_parameter_to_system(self.tau_parameter, 'OPTICS')
        self.lh_builder.lh.add_parameter_to_system(self.tau_endpoint_parameter, 'OPTICS')
        self.lh_builder.lh.add_parameter_to_system(self.tau_nlp_parameter, 'OPTICS')
        
        self.lh_builder.lh.add_parameter_to_system(self.scalar_sigma_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.tau_endpoint_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.tau_nlp_parameter, '-TOPLEVEL')
        
        self.lh_builder.lh.add_parameter_to_system(self.scalar_sigma_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.tau_endpoint_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.tau_nlp_parameter, 'generation')        

        ## Kicker parameters
        for device in self.devices.ext_kicker:
            if device == 'S05MK2E': # Skip these parameters for the seconds kicker in SIS18
                continue
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMDELRF', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMDELTG', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMFTRF', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMFTTG', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTRFS', 'voltages')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTRIS', 'voltages')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTTGS', 'voltages')


        ## Kicker parameters
#        self.kicker_mode_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/MODE', 'SCALAR_KICKER_MODE', self.kicker_device)
#        self.nbunch1_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/NBUNCH1', 'SCALAR_NBUNCH1', self.kicker_device)
#        self.start_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/START', 'SCALAR_KICKER_START', self.kicker_device)
#        self.thigh1_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/THIGH1', 'SCALAR_KICKER_THIGH1', self.kicker_device)
#        self.thigh2_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/THIGH2', 'SCALAR_KICKER_THIGH2', self.kicker_device)
#        self.toffset1_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/TOFFSET1', 'SCALAR_KICKER_TOFFSET1', self.kicker_device)
#        self.toffset2_parameter = self.lh_builder.lh.define_physics_parameter(self.kicker_device + '/TOFFSET2', 'SCALAR_KICKER_TOFFSET2', self.kicker_device)


        ## Bumper parameters
        self.curvature_parameter = self.lh_builder.lh.define_physics_parameter(self.bumper_device + '/CURVATURE', 'SCALAR_BUMPER_CURVATURE', self.bumper_device)
        self.bumper_knob_parameter = self.lh_builder.lh.define_physics_parameter(self.bumper_device + '/KNOB', 'SCALAR_BUMPER_KNOB', self.bumper_device)
        self.tfall_parameter = self.lh_builder.lh.define_physics_parameter(self.bumper_device + '/TFALL', 'SCALAR_TFALL', self.bumper_device)
        self.bumper_slope_parameter = self.lh_builder.lh.define_physics_parameter(self.bumper_device + '/SLOPE', 'SCALAR_BUMPER_SLOPE', self.bumper_device)
        
        self.lh_builder.lh.add_parameter_to_system(self.curvature_parameter, 'BUMPER') 
        self.lh_builder.lh.add_parameter_to_system(self.bumper_knob_parameter, 'BUMPER') 
        self.lh_builder.lh.add_parameter_to_system(self.tfall_parameter, 'BUMPER') 
        self.lh_builder.lh.add_parameter_to_system(self.bumper_slope_parameter, 'BUMPER') 
        self.lh_builder.lh.add_parameter_to_system(self.curvature_parameter, '-TOPLEVEL') 
        self.lh_builder.lh.add_parameter_to_system(self.bumper_knob_parameter, '-TOPLEVEL') 
        self.lh_builder.lh.add_parameter_to_system(self.tfall_parameter, '-TOPLEVEL') 
        self.lh_builder.lh.add_parameter_to_system(self.bumper_slope_parameter, '-TOPLEVEL') 
        self.lh_builder.lh.add_parameter_to_system(self.curvature_parameter, 'generation') 
        self.lh_builder.lh.add_parameter_to_system(self.bumper_knob_parameter, 'generation') 
        self.lh_builder.lh.add_parameter_to_system(self.tfall_parameter, 'generation') 
        self.lh_builder.lh.add_parameter_to_system(self.bumper_slope_parameter, 'generation') 


        for device in self.devices.bumper:
            kl0_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL0', 'SCALAR_BUMPER_K0L0', device)
            dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'SCALAR_BUMPER_DK0L', device)
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'SCALAR_BUMPER_K0L', device)
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'SCALAR_BUMPER_B0L', device)
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'SCALAR_I', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'CURRENTS', 'currents')
            #self.lh_builder.lh.define_hardware_parameter(device, 'FTIMES', 'ftimes')
            #self.lh_builder.lh.define_hardware_parameter(device, 'PARA', 'reference_parameters')
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl0_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)


        ## Hardware rf system parameters
        #for parameter in self.devices.hardware_fs_system:
        #    hardware_fs_rampvals_parameter =  self.lh_builder.lh.define_hardware_parameter(self.hardware_fs_system, 'RAMPVALS', 'data')

        #mhbpar_damp1_parameter = self.lh_builder.lh.define_hardware_parameter(self.hardware_rf_system, 'MHBPAR', 'DAmp1')
        #mhbpar_damp2_parameter = self.lh_builder.lh.define_hardware_parameter(self.hardware_rf_system, 'MHBPAR', 'DAmp2')
        #mhbpar_delay_parameter = self.lh_builder.lh.define_hardware_parameter(self.hardware_rf_system, 'MHBPAR', 'Delay')
        #mhbpar_harm1_parameter = self.lh_builder.lh.define_hardware_parameter(self.hardware_rf_system, 'MHBPAR', 'Harm1')
        #mhbpar_harm2_parameter = self.lh_builder.lh.define_hardware_parameter(self.hardware_rf_system, 'MHBPAR', 'Harm2')
        #syncmode_hfssync_parameter = self.lh_builder.lh.define_hardware_parameter(self.hardware_rf_system, 'SYNCMODE', 'hfssync')
        #workmode_workmode_parameter = self.lh_builder.lh.define_hardware_parameter(self.hardware_rf_system, 'WORKMODE', 'workmode')

        #delay_trgdelay_parameter =  self.lh_builder.lh.define_hardware_parameter(self.tgx_system, 'DELAY', 'trgdelay')
        #harmonic_harmonic_parameter = self.lh_builder.lh.define_hardware_parameter(self.tgx_system, 'HARMONIC', 'harmonic')
        #mode_kickmode_parameter = self.lh_builder.lh.define_hardware_parameter(self.tgx_system, 'MODE', 'kickmode')
        #rftrig_rftrig_parameter = self.lh_builder.lh.define_hardware_parameter(self.tgx_system, 'RFTRIG', 'rftrig')

        #chansequ_chancount_parameter = self.lh_builder.lh.define_hardware_parameter(self.timing_device, 'CHANSEQU', 'chanCount')
        #chansequ_chansequ_parameter = self.lh_builder.lh.define_hardware_parameter(self.timing_device, 'CHANSEQU', 'chanSequ')
        #evtarray_chanarray_parameter = self.lh_builder.lh.define_hardware_parameter(self.timing_device, 'EVTARRAY', 'chanArray')
        self.timeout_unilac_parameter = self.lh_builder.lh.define_physics_parameter(self.timing_device + '/TIMEOUT_UNILAC', 'SCALAR_TIMEOUT_UNILAC', self.timing_device, belongs_to_function_bproc=False)
        self.tmeasure_parameter = self.lh_builder.lh.define_physics_parameter(self.timing_device + '/TMEASURE', 'SCALAR_TMEASURE', self.timing_device)
        self.toffset_unilac_parameter = self.lh_builder.lh.define_physics_parameter(self.timing_device + '/TOFFSET_UNILAC', 'SCALAR_TOFFSET_UNILAC', self.timing_device, belongs_to_function_bproc=False)

        self.lh_builder.lh.add_parameter_to_system(self.timeout_unilac_parameter, 'TIMING')
        self.lh_builder.lh.add_parameter_to_system(self.tmeasure_parameter, 'TIMING')
        self.lh_builder.lh.add_parameter_to_system(self.toffset_unilac_parameter, 'TIMING')
        self.lh_builder.lh.add_parameter_to_system(self.timeout_unilac_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.tmeasure_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.toffset_unilac_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.timeout_unilac_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.tmeasure_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.toffset_unilac_parameter, 'generation')

        ## Orbit parameters
        coh_list = []
        cov_list = []
        
        for count in range(1,13):
            
            coh_parameter = self.lh_builder.lh.define_physics_parameter(self.orbit_device + '/COH%02d' % count, 'ORBITBUMP', self.orbit_device)
            cov_parameter = self.lh_builder.lh.define_physics_parameter(self.orbit_device + '/COV%02d' % count, 'ORBITBUMP', self.orbit_device)
            
            self.lh_builder.lh.add_parameter_to_system(coh_parameter, 'ORBIT')
            self.lh_builder.lh.add_parameter_to_system(cov_parameter, 'ORBIT')
            self.lh_builder.lh.add_parameter_to_system(coh_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(cov_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(coh_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(cov_parameter, 'generation')
            
            coh_list.append(coh_parameter)
            cov_list.append(cov_parameter)

        self.extesep_parameter = self.lh_builder.lh.define_physics_parameter(self.orbit_device + '/EXTESEP', 'FLATBUMP', self.orbit_device)
        self.extmsep_parameter = self.lh_builder.lh.define_physics_parameter(self.orbit_device + '/EXTMSEP', 'FLATBUMP', self.orbit_device)

        self.ext_esms_parameter = self.lh_builder.lh.define_physics_parameter(self.orbit_device + '/EXT_ESMS', 'FLATBUMP', self.orbit_device)

        self.lh_builder.lh.add_parameter_to_system(self.extesep_parameter, 'ORBIT')
        self.lh_builder.lh.add_parameter_to_system(self.extmsep_parameter, 'ORBIT')
        self.lh_builder.lh.add_parameter_to_system(self.ext_esms_parameter, 'ORBIT')
        self.lh_builder.lh.add_parameter_to_system(self.extesep_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.extmsep_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.ext_esms_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.extesep_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.extmsep_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.ext_esms_parameter, 'generation')

        self.orbit_href_parameter = self.lh_builder.lh.define_physics_parameter(self.orbit_device + '/HREF', 'ORBIT_HREF', self.orbit_device, y_prec=6)
        self.orbit_vref_parameter = self.lh_builder.lh.define_physics_parameter(self.orbit_device + '/VREF', 'ORBIT_VREF', self.orbit_device, y_prec=6)

        self.lh_builder.lh.add_parameter_to_system(self.orbit_href_parameter, 'ORBIT')
        self.lh_builder.lh.add_parameter_to_system(self.orbit_vref_parameter, 'ORBIT')

        ## Correction coils
        
        for device in self.devices.horizontal_orbit_correction_coils:
            dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'DK0L', device)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)

        ## Extraction_bump_correction_coils
        for device in self.devices.extraction_bump_correction_coils:
            sector = int(device[2:4])
            if ((sector != 10) and (sector != 11) and (sector != 12)) :
                dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'FLAT_DK0L', device)
                
                system = self.devices.devicesystemmap.get(device)
                print (device , system)
                
                self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)


        for device in self.devices.vertical_correctors:
            dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'DK0L', device)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)
            

        for device in self.devices.extra_correction_coils:
            icorrdot_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ICORRDOT', 'ICORRDOT', device)
            ucorr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/UCORR', 'UCORR', device)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(icorrdot_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(ucorr_parameter, system)
 

        ## SIS18 Bypass
        for device in self.devices.sis18_bypass:
            klbyp_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KLBYP', 'SCALAR_KLBYP', device)
            blbyp_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BLBYP', 'SCALAR_BLBYP', device)
            ibyp_parameter = self.lh_builder.lh.define_physics_parameter(device + '/IBYP', 'IBYP', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(klbyp_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(blbyp_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(ibyp_parameter, system)
            
            self.lh_builder.lh.add_parameter_to_system(klbyp_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(klbyp_parameter, 'generation')

        ## SIS18 KO
        for device in self.devices.sis18_ko_exiter:
            dqh_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DQH', 'SCALAR_DQHKO', device)
            qhfr_parameter = self.lh_builder.lh.define_physics_parameter(device + '/QHFR', 'SCALAR_QHFRKO', device)
            start_tau_parameter = self.lh_builder.lh.define_physics_parameter(device + '/START_TAU', 'SCALAR_START_TAUKO', device)
            end_tau_parameter = self.lh_builder.lh.define_physics_parameter(device + '/END_TAU', 'SCALAR_END_TAUKO', device)
            start_ampl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/START_AMPL', 'SCALAR_START_AMPLKO', device)
            end_ampl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/END_AMPL', 'SCALAR_END_AMPLKO', device)
            upp_parameter = self.lh_builder.lh.define_physics_parameter(device + '/UPP', 'UPPKO', device) 
            uctrl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/UCTRL', 'UCTRLKO', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(dqh_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(dqh_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(dqh_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(qhfr_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(qhfr_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(qhfr_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(start_tau_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(start_tau_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(start_tau_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(end_tau_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(end_tau_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(end_tau_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(start_ampl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(start_ampl_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(start_ampl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(end_ampl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(end_ampl_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(end_ampl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(upp_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(uctrl_parameter, system)
            
        ## RF Parameter
        self.frf_sync = self.lh_builder.lh.define_physics_parameter(self.hardware_rf_device + '/FRF_SYNC', 'FRF_SYNC', self.hardware_rf_device)
        self.lh_builder.lh.add_parameter_to_system(self.frf_sync, 'RF')
        
        for device in self.devices.sis18_bunch_compressor_cavity:
            self.frf_bb = self.lh_builder.lh.define_physics_parameter(device + '/FRF_BB', 'FRF_BB', device)
            self.lh_builder.lh.add_parameter_to_system(self.frf_bb, 'RF')
        
        ## Q kicker parameter
        for device in self.q_kicker:
            
            self.q_kicker_kl = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_kl, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_kl, 'generation')
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_kl, 'KICKER')

            self.q_kicker_bl = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'SCALAR_B0L', device)
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_bl, 'KICKER')
        
            self.q_kicker_ukick = self.lh_builder.lh.define_physics_parameter(device + '/UKICK', 'SCALAR_UKICK', device)
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_ukick, 'KICKER')
            
            self.q_kicker_active = self.lh_builder.lh.define_physics_parameter(device + '/ACTIVE', 'SCALAR_ACTIVE', device)
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_active, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_active, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.q_kicker_active, 'generation')
        
        #self.q_kick_parameter = self.lh_builder.lh.define_physics_parameter(self.q_kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', self.q_kicker_device)
        #self.lh_builder.lh.add_parameter_to_system(self.q_kick_parameter, 'KICKER')
        #self.lh_builder.lh.add_parameter_to_system(self.q_kick_parameter, '-TOPLEVEL')
        #self.lh_builder.lh.add_parameter_to_system(self.q_kick_parameter, 'generation')
        
        self.segment_number = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/SEGMENT_NUMBER', 'SCALAR_SEGMENT_NUMBER', self.timeparam_device)
        
        self.lh_builder.lh.add_parameter_to_system(self.segment_number, 'TIMING')
  
        self.minimum_point_distance = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/MINPDIST', 'SCALAR_MINPDIST', self.timeparam_device)

        self.lh_builder.lh.add_parameter_to_system(self.minimum_point_distance, 'TIMING')
        self.lh_builder.lh.add_parameter_to_system(self.minimum_point_distance, 'generation')


        ### Creation of relations

        ## Beam parameters
        self.lh_builder.create_child_node(self.inj_emil_parameter, [ self.dp_over_p_parameter, self.e_start_end_parameter, self.rf_manipulation_parameter ])

        ## Optics Parameters
        # remove some relations for opticsip parameter
        self.lh_builder.remove_child_node(self.opticsip_parameter, [self.tau_start_end_parameter] )
        
        self.lh_builder.create_child_node(self.scalar_sigma_start_end_parameter, self.scalar_sigma_parameter)

        self.lh_builder.create_child_node(self.opticsip_parameter, [ self.sigma_parameter, self.tau_parameter, self.incorpip_parameter ])
        self.lh_builder.create_child_node(self.sigma_parameter, [ self.brho_start_end_parameter, self.scalar_sigma_start_end_parameter, self.bp_length_parameter, self.t_wait_parameter, self.tround_parameter, self.tgrid_parameter, self.tau_endpoint_parameter ])
        self.lh_builder.create_child_node(self.tau_parameter, [ self.tau_nlp_parameter, self.tau_start_end_parameter, self.bp_length_parameter, self.t_wait_parameter, self.brho_start_end_parameter, self.tround_parameter, self.tgrid_parameter, self.tau_endpoint_parameter ])

        ## Timeparam Parameters
        ## add special relation from ext_sigma to bp_length
        self.lh_builder.create_child_node(self.bp_length_parameter, [self.scalar_sigma_start_end_parameter, self.minimum_point_distance])
        #self.lh_builder.create_child_node(self.bp_length_parameter, [ self.t_bp_length_parameter, self.t_wait_parameter, self.ext_sigma_parameter, self.tau_start_end_parameter, self.tround_parameter,  self.bdot_parameter, self.brho_start_end_parameter, self.tgrid_parameter ], parent_parameter_order={self.t_bp_length_parameter : 1})


        delay_trgdelay_parameter = self.kicker_timing_device + '/DELAY#trgdelay'
        harmonic_harmonic_parameter = self.kicker_timing_device + '/HARMONIC#harmonic'
        mode_kickmode_parameter = self.kicker_timing_device + '/MODE#kickmode'
        rftrig_rftrig_parameter = self.kicker_timing_device + '/RFTRIG#rftrig'
        self.lh_builder.create_child_node(delay_trgdelay_parameter, [ self.tbunch_parameter, self.rf_manipulation_parameter, self.start_parameter ])
        self.lh_builder.create_child_node(harmonic_harmonic_parameter, self.rf_manipulation_parameter )
        self.lh_builder.create_child_node(mode_kickmode_parameter, [ self.kicker_mode_parameter, self.nbunch1_parameter, self.rf_manipulation_parameter ])
        self.lh_builder.create_child_node(rftrig_rftrig_parameter, self.rf_manipulation_parameter )

        chopper_toffset_parameter = 'GTK7BC1L/TOFFSET'
        chansequ_chancount_parameter = self.timing_device + '/CHANSEQU#chanCount'
        chansequ_chansequ_parameter = self.timing_device + '/CHANSEQU#chanSequ'
        evtarray_chanarray_parameter = self.timing_device + '/EVTARRAY#chanArray'
        self.lh_builder.create_child_node(self.segment_number, self.tmeasure_parameter)
        self.lh_builder.create_child_node(chansequ_chancount_parameter, [self.timeout_unilac_parameter, self.tmeasure_parameter, self.toffset_unilac_parameter, self.bp_length_parameter, self.kicker_mode_parameter, chopper_toffset_parameter, self.t_wait_parameter, self.segment_number, self.q_kicker_active])
        self.lh_builder.create_child_node(chansequ_chansequ_parameter, [self.timeout_unilac_parameter, self.tmeasure_parameter, self.toffset_unilac_parameter, self.bp_length_parameter, self.kicker_mode_parameter, chopper_toffset_parameter, self.t_wait_parameter, self.segment_number, self.q_kicker_active])
        self.lh_builder.create_child_node(evtarray_chanarray_parameter, [self.timeout_unilac_parameter, self.tmeasure_parameter, self.toffset_unilac_parameter, self.bp_length_parameter, self.kicker_mode_parameter, chopper_toffset_parameter, self.t_wait_parameter, self.segment_number, self.q_kicker_active])

        ## Hardware rf system parameters
        hardware_fs_rampvals_parameter = self.hardware_rf_device + '/RAMPVALS#data'
        self.lh_builder.create_child_node(hardware_fs_rampvals_parameter, [self.frf_sync ,self.segment_number, self.minimum_point_distance, self.minimum_point_distance])
        self.lh_builder.create_child_node(self.frf_sync, self.frev_parameter)
        
        for device in self.devices.sis18_bunch_compressor_cavity:
            bunch_compressor_rampvals_parameter = device + '/RAMPVALS#data'
            self.lh_builder.create_child_node(bunch_compressor_rampvals_parameter, [ self.frf_bb, self.segment_number, self.minimum_point_distance, self.minimum_point_distance])
            self.lh_builder.create_child_node(self.frf_bb, [self.frev_parameter, self.rf_manipulation_parameter])
        
        #mhbpar_damp1_parameter = self.cavity_sync_device + '/MHBPAR#DAmp1'
        #mhbpar_damp2_parameter = self.cavity_sync_device + '/MHBPAR#DAmp2'
        #mhbpar_delay_parameter = self.cavity_sync_device + '/MHBPAR#Delay'
        #mhbpar_harm1_parameter = self.cavity_sync_device + '/MHBPAR#Harm1'
        #mhbpar_harm2_parameter = self.cavity_sync_device + '/MHBPAR#Harm2'
        syncmode_hfssync_parameter = self.cavity_sync_device + '/SYNCMODE#hfssync'
        workmode_workmode_parameter = self.cavity_sync_device + '/WORKMODE#workmode'

        #self.lh_builder.create_child_node(mhbpar_damp1_parameter, self.rf_manipulation_parameter )
        #self.lh_builder.create_child_node(mhbpar_damp2_parameter, self.rf_manipulation_parameter )
        #self.lh_builder.create_child_node(mhbpar_delay_parameter, self.rf_manipulation_parameter )
        #self.lh_builder.create_child_node(mhbpar_harm1_parameter, self.rf_manipulation_parameter )
        #self.lh_builder.create_child_node(mhbpar_harm2_parameter, self.rf_manipulation_parameter )
        self.lh_builder.create_child_node(syncmode_hfssync_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(workmode_workmode_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )

        ## new MHBPAR2
        mhbpar2_delay_1_parameter = self.cavity_sync_device + '/MHBPAR2#Delay_1'
        mhbpar2_harm1_1_parameter = self.cavity_sync_device + '/MHBPAR2#Harm1_1'
        mhbpar2_harm2_1_parameter = self.cavity_sync_device + '/MHBPAR2#Harm2_1'
        mhbpar2_damp1_1_parameter = self.cavity_sync_device + '/MHBPAR2#DAmp1_1'
        mhbpar2_damp2_1_parameter = self.cavity_sync_device + '/MHBPAR2#DAmp2_1'
        
        mhbpar2_delay_2_parameter = self.cavity_sync_device + '/MHBPAR2#Delay_2'
        mhbpar2_harm1_2_parameter = self.cavity_sync_device + '/MHBPAR2#Harm1_2'
        mhbpar2_harm2_2_parameter = self.cavity_sync_device + '/MHBPAR2#Harm2_2'
        mhbpar2_damp1_2_parameter = self.cavity_sync_device + '/MHBPAR2#DAmp1_2'
        mhbpar2_damp2_2_parameter = self.cavity_sync_device + '/MHBPAR2#DAmp2_2'

        mhbpar2_delay_3_parameter = self.cavity_sync_device + '/MHBPAR2#Delay_3'
        mhbpar2_harm1_3_parameter = self.cavity_sync_device + '/MHBPAR2#Harm1_3'
        mhbpar2_harm2_3_parameter = self.cavity_sync_device + '/MHBPAR2#Harm2_3'
        mhbpar2_damp1_3_parameter = self.cavity_sync_device + '/MHBPAR2#DAmp1_3'
        mhbpar2_damp2_3_parameter = self.cavity_sync_device + '/MHBPAR2#DAmp2_3'
        
        self.lh_builder.create_child_node(mhbpar2_delay_1_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_harm1_1_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_harm2_1_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_damp1_1_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_damp2_1_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )

        self.lh_builder.create_child_node(mhbpar2_delay_2_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_harm1_2_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_harm2_2_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_damp1_2_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_damp2_2_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
 
        self.lh_builder.create_child_node(mhbpar2_delay_3_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_harm1_3_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_harm2_3_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_damp1_3_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
        self.lh_builder.create_child_node(mhbpar2_damp2_3_parameter, [evtarray_chanarray_parameter, self.cavity2harmonic_parameter, self.segment_number] )
  

        ## Main sextupoles:
#        for device in self.devices.main_sextupoles:
#            kldelta_parameter = self.reader.find_unique_string(device + '/KLDELTA$', self.lh_builder.lh.get_parameters())
#            self.lh_builder.create_child_node(kldelta_parameter, [ self.incorpip_parameter, self.kl_harm_parameter, self.kl_phase_parameter, self.kl_ampl_parameter, self.kl_offset_parameter ])
#
#            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())    
#            self.lh_builder.create_child_node(kl_parameter, [ self.ch_parameter, self.cv_parameter, self.opticsip_parameter, kldelta_parameter ]) 

        ## Reference orbit
        self.lh_builder.create_child_node(self.orbit_href_parameter, [self.qh_parameter, self.qh_theo_parameter, self.opticsip_parameter, self.dpbl_parameter, self.dpfrev_parameter, self.dpdr_parameter] )
        self.lh_builder.create_child_node(self.orbit_vref_parameter, [self.qv_parameter, self.qv_theo_parameter, self.opticsip_parameter] )

        ## Horizontal_orbit_correction_coils
        self.devices.horizontal_orbit_correction_coils.sort()
        for device in self.devices.horizontal_orbit_correction_coils:
            dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            sector = int(device[2:4])
            index = sector - 1
            if (sector == 4) :
                self.lh_builder.create_child_node(dkl_parameter, [ self.ext_esms_parameter, self.opticsip_parameter, coh_list[index], coh_list[index - 1] ])
            elif (sector == 5) :
                self.lh_builder.create_child_node(dkl_parameter, [ self.extesep_parameter, self.ext_esms_parameter, self.opticsip_parameter, coh_list[index], coh_list[index - 2], coh_list[index - 3] ])
            elif (sector == 6) :
                self.lh_builder.create_child_node(dkl_parameter, [ self.ext_esms_parameter, self.opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
            elif (sector == 7) :
                self.lh_builder.create_child_node(dkl_parameter, [ self.extmsep_parameter, self.ext_esms_parameter, self.opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2], coh_list[index - 3] ])
            else:
                self.lh_builder.create_child_node(dkl_parameter, [ self.opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
            
            ## All horizontal knobs over all horizontal orbit correction coils    
            for cohKnob in coh_list:
                self.lh_builder.create_child_node(dkl_parameter, cohKnob)
                
            self.lh_builder.create_child_node(self.orbit_href_parameter, dkl_parameter)
            self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, dkl_parameter])

        ## Extraction_bump_correction_coils
        for device in self.devices.extraction_bump_correction_coils:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            sector = int(device[2:4])
            if ((sector == 10) | (sector == 11) | (sector == 12)) :
                self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter)
            elif ((sector == 4) | (sector == 5)) :
                dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(dkl_parameter, [ self.opticsip_parameter, self.extesep_parameter, self.ext_esms_parameter ])
                self.lh_builder.create_child_node(self.orbit_href_parameter, dkl_parameter)
                self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, dkl_parameter ])
            else:
                dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(dkl_parameter, [ self.opticsip_parameter, self.extmsep_parameter, self.ext_esms_parameter ])
                self.lh_builder.create_child_node(self.orbit_href_parameter, dkl_parameter)
                self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, dkl_parameter ])
        
        ## Vertical correctors        
        for device in self.devices.vertical_correctors:
            dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(self.orbit_vref_parameter, dkl_parameter)

        ## Orbit Parameters
        for count in range(0,12):
            self.lh_builder.create_child_node(coh_list[count], self.incorpip_parameter )
            self.lh_builder.create_child_node(cov_list[count], self.incorpip_parameter )

        self.lh_builder.create_child_node(self.extesep_parameter, self.incorpip_parameter )
        self.lh_builder.create_child_node(self.extmsep_parameter, self.incorpip_parameter )
        self.lh_builder.create_child_node(self.ext_esms_parameter, self.incorpip_parameter )

        ## Magnets
        
        for device in self.main_magnets:
            u_parameter = self.reader.find_unique_string(device + '/U$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())

            rampvals_parameter = (device + '/RAMPVALS#data')
            self.lh_builder.create_child_node(rampvals_parameter, [ u_parameter, i_parameter, self.segment_number, self.minimum_point_distance ])

        for device in (self.devices.main_sextupoles + self.devices.correction_quadrupoles + self.devices.extraction_quadrupoles + self.devices.correction_sextupoles +self.devices.resonance_sextupoles + self.devices.chromaticity_sextupoles):
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())

            rampvals_parameter = (device + '/RAMPVALS#data')
            self.lh_builder.create_child_node(rampvals_parameter, [i_parameter, self.segment_number, self.minimum_point_distance])

        
        
        for device in self.devices.vertical_correctors:
            dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            sector = int(device[2:4])
            index = sector - 1
            self.lh_builder.create_child_node(dkl_parameter, [ self.opticsip_parameter, cov_list[index], cov_list[index - 1], cov_list[index + 1 - len(cov_list)] ])
            self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, dkl_parameter ])

            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            rampvals_parameter = (device + '/RAMPVALS#data')
            self.lh_builder.create_child_node(rampvals_parameter, [i_parameter, self.segment_number, self.minimum_point_distance])

        for device in self.devices.extra_correction_coils:
            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            icorrdot_parameter = self.reader.find_unique_string(device + '/ICORRDOT$', self.lh_builder.lh.get_parameters())
            ucorr_parameter = self.reader.find_unique_string(device + '/UCORR$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(icorrdot_parameter, icorr_parameter )

            rampvals_parameter = (device + '/RAMPVALS#data')
            self.lh_builder.create_child_node(rampvals_parameter, [ icorr_parameter, ucorr_parameter, self.segment_number, self.minimum_point_distance ])
    
            for dipol_device in self.devices.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                idot_parameter = self.reader.find_unique_string(dipol_device + '/IDOT$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(ucorr_parameter, [ icorr_parameter, icorrdot_parameter, i_parameter, idot_parameter ])

        for device in list(set(self.devices.horizontal_correction_coils) - set(self.devices.extra_correction_coils)):
            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            rampvals_parameter = (device + '/RAMPVALS#data')
            self.lh_builder.create_child_node(rampvals_parameter, [icorr_parameter, self.segment_number, self.minimum_point_distance])

        ## Kicker
        kicker_ukick_parameters = []
        for device in self.devices.ext_kicker:
            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            kicker_ukick_parameters.append(ukick_parameter)



        self.devices.ext_kicker.sort()
        for device in self.devices.ext_kicker:

            if (device == self.devices.ext_kicker[0]):
                timdelrf_time_parameter = (device + '/TIMDELRF#time')
                self.lh_builder.create_child_node(timdelrf_time_parameter, self.toffset1_parameter)
        
                timdeltg_time_parameter = (device + '/TIMDELTG#time')
                self.lh_builder.create_child_node(timdeltg_time_parameter, self.toffset2_parameter)
        
                timftrf_time_parameter = (device + '/TIMFTRF#time')
                self.lh_builder.create_child_node(timftrf_time_parameter, [ self.toffset1_parameter, self.thigh1_parameter ])
        
                timfttg_time_parameter = (device + '/TIMFTTG#time')
                self.lh_builder.create_child_node(timfttg_time_parameter, [ self.toffset2_parameter, self.thigh2_parameter ])
        
                voltrfs_voltages_parameter = (device + '/VOLTRFS#volt')
                self.lh_builder.create_child_node(voltrfs_voltages_parameter, kicker_ukick_parameters)
        
                voltris_voltages_parameter = (device + '/VOLTRIS#volt')
                self.lh_builder.create_child_node(voltris_voltages_parameter, kicker_ukick_parameters)
        
                volttgs_voltages_parameter = (device + '/VOLTTGS#volt')
                self.lh_builder.create_child_node(volttgs_voltages_parameter, kicker_ukick_parameters)


        ## Bumpers
        self.lh_builder.create_child_node(self.bumper_slope_parameter, self.opticsip_parameter )
        
        for device in self.devices.bumper:
            kl0_parameter = self.reader.find_unique_string(device + '/KL0$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl0_parameter, [ self.dqh_parameter, self.dqv_parameter, self.opticsip_parameter ], parent_parameter_order = {self.opticsip_parameter : 1})

            dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(dkl_parameter, [ self.dqh_parameter, self.dqv_parameter, self.opticsip_parameter ], parent_parameter_order = {self.opticsip_parameter : 1})

            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [self.bumper_knob_parameter, self.bumper_slope_parameter, kl0_parameter, dkl_parameter])

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ self.brho_parameter, kl_parameter ])

            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter )

            currents_currents_parameter = (device + '/CURRENTS#currents')
            self.lh_builder.create_child_node(currents_currents_parameter, i_parameter )

            ftimes_ftimes_parameter = (device + '/FTIMES#ftimes')
            self.lh_builder.create_child_node(ftimes_ftimes_parameter, self.tfall_parameter )

            para_reference_parameter = (device + '/PARA#reference_parameters')
            self.lh_builder.create_child_node(para_reference_parameter, self.curvature_parameter )


        ## SIS18 Bypass
        for device in self.devices.sis18_bypass:
            kl_parameter = self.reader.find_unique_string(device + '/KLBYP$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter )

            bl_parameter = self.reader.find_unique_string(device + '/BLBYP$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , self.brho_parameter ])

            ibyp_parameter = self.reader.find_unique_string(device + '/IBYP$', self.lh_builder.lh.get_parameters())
            for dipol_device in self.devices.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(ibyp_parameter, [ bl_parameter , self.incorpip_parameter , i_parameter ], parent_parameter_order={bl_parameter : 1 , i_parameter : 1})

            rampvals_parameter = (device + '/RAMPVALS#data')
            self.lh_builder.create_child_node(rampvals_parameter, [ibyp_parameter, self.segment_number, self.minimum_point_distance] )

        ## SIS18 KO
        for device in self.devices.sis18_ko_exiter:
            start_tau_parameter = self.reader.find_unique_string(device + '/START_TAU$', self.lh_builder.lh.get_parameters())
            end_tau_parameter = self.reader.find_unique_string(device + '/END_TAU$', self.lh_builder.lh.get_parameters())
            start_ampl_parameter = self.reader.find_unique_string(device + '/START_AMPL$', self.lh_builder.lh.get_parameters())
            end_ampl_parameter = self.reader.find_unique_string(device + '/END_AMPL$', self.lh_builder.lh.get_parameters())
            upp_parameter = self.reader.find_unique_string(device + '/UPP$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(upp_parameter, [ start_tau_parameter, end_tau_parameter, start_ampl_parameter, end_ampl_parameter, self.erho_parameter, self.tgrid_parameter, self.bp_length_parameter ])

            uctrl_parameter = self.reader.find_unique_string(device + '/UCTRL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(uctrl_parameter, [ upp_parameter, self.incorpip_parameter ], parent_parameter_order={upp_parameter : 1})

            dqh_parameter = self.reader.find_unique_string(device + '/DQH$', self.lh_builder.lh.get_parameters())
            qhfr_parameter = self.reader.find_unique_string(device + '/QHFR$', self.lh_builder.lh.get_parameters())

            rampvals_parameter = (device + '/RAMPVALS#data')
            self.lh_builder.create_child_node(rampvals_parameter, [ self.rf_manipulation_parameter, self.frev_parameter, dqh_parameter, uctrl_parameter, qhfr_parameter, self.segment_number, self.minimum_point_distance ])

        ## remove RAMPVALS for not installed H=2 cavity modules
        for device in self.devices.old_cavities_ampl:
            urf_parameter = self.reader.find_unique_string(device + '/URF$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(urf_parameter, self.cavity2harmonic_parameter )
            if not (device.endswith("3A")):
                rampvals_a_parameter = (device + '/RAMPVALS#data')
                self.lh_builder.create_child_node(rampvals_a_parameter, [urf_parameter, self.segment_number, self.minimum_point_distance] )

        for device in self.devices.old_cavities_freq:
            frf_parameter = self.reader.find_unique_string(device + '/FRF$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(frf_parameter, self.cavity2harmonic_parameter )

            if not (device.endswith("3F")):
                rampvals_fs_parameter = (device + '/RAMPVALS#data')
                self.lh_builder.create_child_node(rampvals_fs_parameter, [frf_parameter, self.segment_number, self.minimum_point_distance] )

        for device in self.devices.old_cavities_phase:
            if not (device.endswith("3P")):
                prf_parameter = self.reader.find_unique_string(device + '/PRF$', self.lh_builder.lh.get_parameters())
                rampvals_p_parameter = (device + '/RAMPVALS#data')
                self.lh_builder.create_child_node(rampvals_p_parameter, [prf_parameter, self.segment_number, self.minimum_point_distance] )
                
        ## Q kicker relations
        for device in self.q_kicker:
            
            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, self.q_kick_parameter ], parent_parameter_order = {self.opticsip_parameter : 1})

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , self.brho_parameter ])

            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(ukick_parameter, bl_parameter )
            
            q_kicker_active_parameter = self.reader.find_unique_string(device + '/ACTIVE$', self.lh_builder.lh.get_parameters())
        
            voltrfs_voltages_parameter = (device + '/VOLTRFS#volt')
            self.lh_builder.create_child_node(voltrfs_voltages_parameter, [ukick_parameter, q_kicker_active_parameter] )
        
            voltris_voltages_parameter = (device + '/VOLTRIS#volt')
            self.lh_builder.create_child_node(voltris_voltages_parameter, [ukick_parameter, q_kicker_active_parameter] )
        
            volttgs_voltages_parameter = (device + '/VOLTTGS#volt')
            self.lh_builder.create_child_node(volttgs_voltages_parameter, [ukick_parameter, q_kicker_active_parameter] )

        
    def build(self):
        
        # build generic part of hierarchy
        SIS18ESRHierarchy.build(self)
        
        # build special part of hierarchy for SIS18
        self.__buildSpecial()
        
        SIS18ESRHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
        
    h2 = SIS18Generator()
    h2.build()
    h2.generate()
