#!/bin/env python2.6

from lh_builder_utils import LHBuilderUtils


class SpecialSIS18Parameters:

    def __init__(self, lh_builder, csv_filename):
        self.lh_builder = lh_builder
        self.reader = LHBuilderUtils()
        self.all_devices = self.reader._read_devices(csv_filename)

    def sethardware_fs_system(self, hardware_fs_system):
        self.hardware_fs_system = hardware_fs_system

    def sethardware_rf_system(self, hardware_rf_system):
        self.hardware_rf_system = hardware_rf_system

    def settgx_system(self, tgx_system):
        self.tgx_system = tgx_system

    def settiming_device(self, timing_device):
        self.timing_device = timing_device

    def setmaindipole(self, main_dipoles):
        self.main_dipoles = main_dipoles

    def sethorizontal_correctors(self, horizontal_correctors):
        self.horizontal_correctors = horizontal_correctors
    def setvertical_correctors(self, vertical_correctors):
        self.vertical_correctors = vertical_correctors
   
    def setmain_sextupoles(self, main_sextupoles):
        self.main_sextupoles = main_sextupoles

    def sethorizontal_correction_coils(self, horizontal_correction_coils):
        self.horizontal_correction_coils = horizontal_correction_coils

    def setextraction_bump_correction_coils(self, extraction_bump_correction_coils):
        self.extraction_bump_correction_coils = extraction_bump_correction_coils

    def setextra_correction_coils(self, extra_correction_coils):
        self.extra_correction_coils = extra_correction_coils

    def sethorizontal_orbit_correction_coils(self, horizontal_orbit_correction_coils):
        self.horizontal_orbit_correction_coils = horizontal_orbit_correction_coils

    def setsis18_cavities_ampl(self, sis18_cavities_ampl):
        self.sis18_cavities_ampl = sis18_cavities_ampl

    def setsis18_cavities_freq(self, sis18_cavities_freq):
        self.sis18_cavities_freq = sis18_cavities_freq

    def setsis18_cavities_phase(self, sis18_cavities_phase):
        self.sis18_cavities_phase = sis18_cavities_phase

    def setsis18_bypass(self, sis18_bypass):
        self.sis18_bypass = sis18_bypass

    def setsis18_ko_exiter(self, sis18_ko_exiter):
        self.sis18_ko_exiter = sis18_ko_exiter

    def setkicker(self, kicker):
        self.kicker = kicker

    def setbumper(self, bumper):
        self.bumper = bumper

    def build(self, particle_transfer):

        beam_device = self.reader.find_unique_string(particle_transfer.replace('_RING','BEAM'), self.all_devices)
        optics_device = self.reader.find_unique_string(particle_transfer.replace('_RING','OPTICS'), self.all_devices)
        orbit_device = self.reader.find_unique_string(particle_transfer.replace('_RING','ORBIT'), self.all_devices)
        bumper_device = self.reader.find_unique_string(particle_transfer.replace('_RING','BUMPER'), self.all_devices)
        kicker_device = self.reader.find_unique_string(particle_transfer.replace('_RING','KICKER'), self.all_devices)

        ## Beam parameters
        dp_over_p_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/DP_OVER_P', 'SCALAR_DP_OVER_P', beam_device, belongs_to_function_bproc=False)

        for device in self.main_sextupoles:
            self.lh_builder.lh.define_physics_parameter(device + '/KLDELTA', 'DELTA_K2L', device) ## KLDELTA soll nicht fuer S02KM5SS und S08KM5SS 

        ## Optics parameters
        ext_sigma_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/EXT_SIGMA', 'SCALAR_EXT_SIGMA', optics_device, belongs_to_function_bproc=False)
        sigma_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/SIGMA', 'SIGMA', optics_device)
        tau_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/TAU', 'TAU', optics_device)
        tau_endpoint_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/TAU_ENDPOINT', 'SCALAR_TAU_ENDPOINT', optics_device)
        tau_nlp_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/TAU_NLP', 'SCALAR_TAU_NLP', optics_device)


        ## Kicker parameters
        for device in self.kicker:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BL', 'SCALAR_B0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/UKICK', 'SCALAR_UKICK', device)
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
        kicker_knob_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', kicker_device)
        kicker_mode_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/MODE', 'SCALAR_KICKER_MODE', kicker_device)
        nbunch1_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/NBUNCH1', 'SCALAR_NBUNCH1', kicker_device)
        start_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/START', 'SCALAR_KICKER_START', kicker_device)
        thigh1_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/THIGH1', 'SCALAR_KICKER_THIGH1', kicker_device)
        thigh2_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/THIGH2', 'SCALAR_KICKER_THIGH2', kicker_device)
        toffset1_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/TOFFSET1', 'SCALAR_KICKER_TOFFSET1', kicker_device)
        toffset2_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/TOFFSET2', 'SCALAR_KICKER_TOFFSET2', kicker_device)


        ## Bumper parameters
        curvature_parameter = self.lh_builder.lh.define_physics_parameter(bumper_device + '/CURVATURE', 'SCALAR_BUMPER_CURVATURE', bumper_device)
        bumper_knob_parameter = self.lh_builder.lh.define_physics_parameter(bumper_device + '/KNOB', 'SCALAR_BUMPER_KNOB', bumper_device)
        tfall_parameter = self.lh_builder.lh.define_physics_parameter(bumper_device + '/TFALL', 'SCALAR_TFALL', bumper_device)


        for device in self.bumper:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BL', 'SCALAR_B0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/I', 'SCALAR_I', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'CURRENTS', 'currents')
            #self.lh_builder.lh.define_hardware_parameter(device, 'FTIMES', 'ftimes')
            #self.lh_builder.lh.define_hardware_parameter(device, 'PARA', 'reference_parameters')
        

        ## Hardware rf system parameters
        #for parameter in self.hardware_fs_system:
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
        timeout_unilac_parameter = self.lh_builder.lh.define_physics_parameter(self.timing_device + '/TIMEOUT_UNILAC', 'SCALAR_TIMEOUT_UNILAC', self.timing_device, belongs_to_function_bproc=False)
        tmeasure_parameter = self.lh_builder.lh.define_physics_parameter(self.timing_device + '/TMEASURE', 'SCALAR_TMEASURE', self.timing_device)
        toffset_unilac_parameter = self.lh_builder.lh.define_physics_parameter(self.timing_device + '/TOFFSET_UNILAC', 'SCALAR_TOFFSET_UNILAC', self.timing_device, belongs_to_function_bproc=False)


        for device in self.sis18_cavities_ampl:
            self.lh_builder.lh.define_physics_parameter(device + '/URF', 'URF', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            #self.lh_builder.lh.define_hardware_parameter(device, 'BROTAMPL', 'highValue')


        for device in self.sis18_cavities_freq:
            self.lh_builder.lh.define_physics_parameter(device + '/FRF', 'FRF', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        for device in self.sis18_cavities_phase:
            self.lh_builder.lh.define_physics_parameter(device + '/PRF', 'PRF', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')


        ## Orbit parameters
        coh01_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH01', 'ORBITBUMP', orbit_device)
        coh02_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH02', 'ORBITBUMP', orbit_device)
        coh03_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH03', 'ORBITBUMP', orbit_device)
        coh04_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH04', 'ORBITBUMP', orbit_device)
        coh05_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH05', 'ORBITBUMP', orbit_device)
        coh06_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH06', 'ORBITBUMP', orbit_device)
        coh07_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH07', 'ORBITBUMP', orbit_device)
        coh08_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH08', 'ORBITBUMP', orbit_device)
        coh09_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH09', 'ORBITBUMP', orbit_device)
        coh10_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH10', 'ORBITBUMP', orbit_device)
        coh11_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH11', 'ORBITBUMP', orbit_device)
        coh12_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COH12', 'ORBITBUMP', orbit_device)
        cov01_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV01', 'ORBITBUMP', orbit_device)
        cov02_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV02', 'ORBITBUMP', orbit_device)
        cov03_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV03', 'ORBITBUMP', orbit_device)
        cov04_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV04', 'ORBITBUMP', orbit_device)
        cov05_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV05', 'ORBITBUMP', orbit_device)
        cov06_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV06', 'ORBITBUMP', orbit_device)
        cov07_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV07', 'ORBITBUMP', orbit_device)
        cov08_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV08', 'ORBITBUMP', orbit_device)
        cov09_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV09', 'ORBITBUMP', orbit_device)
        cov10_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV10', 'ORBITBUMP', orbit_device)
        cov11_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV11', 'ORBITBUMP', orbit_device)
        cov12_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/COV12', 'ORBITBUMP', orbit_device)
        extesep_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/EXTESEP', 'FLATBUMP', orbit_device)
        extmsep_parameter = self.lh_builder.lh.define_physics_parameter(orbit_device + '/EXTMSEP', 'FLATBUMP', orbit_device)

        coh_list = [coh01_parameter, coh02_parameter, coh03_parameter, coh04_parameter, coh05_parameter, coh06_parameter, coh07_parameter, coh08_parameter, coh09_parameter, coh10_parameter, coh11_parameter, coh12_parameter]

        cov_list = [cov01_parameter, cov02_parameter, cov03_parameter, cov04_parameter, cov05_parameter, cov06_parameter, cov07_parameter, cov08_parameter, cov09_parameter, cov10_parameter, cov11_parameter, cov12_parameter]

        ## Correction coils
        for device in self.extraction_bump_correction_coils:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'FLAT_K0L', device)

        for device in self.horizontal_orbit_correction_coils:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device)

        for device in self.horizontal_correction_coils:
            self.lh_builder.lh.define_physics_parameter(device + '/BLCORR', 'CORR_B0L', device)   
            self.lh_builder.lh.define_physics_parameter(device + '/ICORR', 'ICORR', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        for device in self.extra_correction_coils:
            self.lh_builder.lh.define_physics_parameter(device + '/ICORRDOT', 'ICORRDOT', device)
            self.lh_builder.lh.define_physics_parameter(device + '/UCORR', 'UCORR', device)

        ## SIS18 Bypass
        for device in self.sis18_bypass:
            self.lh_builder.lh.define_physics_parameter(device + '/KLBYP', 'SCALAR_KLBYP', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BLBYP', 'SCALAR_BLBYP', device)
            self.lh_builder.lh.define_physics_parameter(device + '/IBYP', 'IBYP', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        ## SIS18 KO
        for device in self.sis18_ko_exiter:
            self.lh_builder.lh.define_physics_parameter(device + '/DQH', 'SCALAR_DQHKO', device)
            self.lh_builder.lh.define_physics_parameter(device + '/QHFR', 'SCALAR_QHFRKO', device)
            self.lh_builder.lh.define_physics_parameter(device + '/START_TAU', 'SCALAR_START_TAUKO', device)
            self.lh_builder.lh.define_physics_parameter(device + '/END_TAU', 'SCALAR_END_TAUKO', device)
            self.lh_builder.lh.define_physics_parameter(device + '/START_AMPL', 'SCALAR_START_AMPLKO', device)
            self.lh_builder.lh.define_physics_parameter(device + '/END_AMPL', 'SCALAR_END_AMPLKO', device)
            self.lh_builder.lh.define_physics_parameter(device + '/UPP', 'UPPKO', device) 
            self.lh_builder.lh.define_physics_parameter(device + '/UCTRL', 'UCTRLKO', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        ### Creation of relations

        incorpip_parameter = self.reader.find_unique_string('SIS18TIMEPARAM/INCORPIP$', self.lh_builder.lh.get_parameters())

        opticsip_parameter = self.reader.find_unique_string('SIS18OPTICS/OPTICSIP$', self.lh_builder.lh.get_parameters())
        tau_start_end_parameter = self.reader.find_unique_string('SIS18OPTICS/TAU_START_END$', self.lh_builder.lh.get_parameters())
        brho_start_end_parameter = self.reader.find_unique_string('SIS18BEAM/BRHO_START_END$', self.lh_builder.lh.get_parameters())

        t_wait_parameter = self.reader.find_unique_string('SIS18TIMEPARAM/T_WAIT$', self.lh_builder.lh.get_parameters())
        tgrid_parameter = self.reader.find_unique_string('SIS18TIMEPARAM/TGRID$', self.lh_builder.lh.get_parameters())
        tround_parameter = self.reader.find_unique_string('SIS18TIMEPARAM/TROUND$', self.lh_builder.lh.get_parameters())
        t_bp_length_parameter = self.reader.find_unique_string('SIS18TIMEPARAM/T_BP_LENGTH$', self.lh_builder.lh.get_parameters())
        bp_length_parameter = self.reader.find_unique_string('SIS18TIMEPARAM/BP_LENGTH$', self.lh_builder.lh.get_parameters())
        bdot_parameter = self.reader.find_unique_string('SIS18TIMEPARAM/BDOT$', self.lh_builder.lh.get_parameters())
        frev_parameter = self.reader.find_unique_string('SIS18BEAM/FREV$', self.lh_builder.lh.get_parameters())

        h_parameter = self.reader.find_unique_string('SIS18BEAM/H$', self.lh_builder.lh.get_parameters())

        urfring_parameter = self.reader.find_unique_string('SIS18RF/URFRING$', self.lh_builder.lh.get_parameters())
        frfring_parameter = self.reader.find_unique_string('SIS18RF/FRFRING$', self.lh_builder.lh.get_parameters())
        prfring_parameter = self.reader.find_unique_string('SIS18RF/PRFRING$', self.lh_builder.lh.get_parameters())
        rf_mode_parameter = self.reader.find_unique_string('SIS18RF/MODE$', self.lh_builder.lh.get_parameters())

        brho_parameter = self.reader.find_unique_string('SIS18BEAM/BRHO$', self.lh_builder.lh.get_parameters())
        erho_parameter = self.reader.find_unique_string('SIS18BEAM/ERHO$', self.lh_builder.lh.get_parameters())

        tbunch_parameter = self.reader.find_unique_string('SIS18BEAM/TBUNCH$', self.lh_builder.lh.get_parameters())

        ch_parameter = self.reader.find_unique_string('SIS18BEAM/CH$', self.lh_builder.lh.get_parameters())
        cv_parameter = self.reader.find_unique_string('SIS18BEAM/CV$', self.lh_builder.lh.get_parameters())

        kl_ampl_parameter = self.reader.find_unique_string('SIS18BEAM/KL_AMPL$', self.lh_builder.lh.get_parameters())
        kl_harm_parameter = self.reader.find_unique_string('SIS18BEAM/KL_HARM$', self.lh_builder.lh.get_parameters())
        kl_offset_parameter = self.reader.find_unique_string('SIS18BEAM/KL_OFFSET$', self.lh_builder.lh.get_parameters())
        kl_phase_parameter = self.reader.find_unique_string('SIS18BEAM/KL_PHASE$', self.lh_builder.lh.get_parameters())

        ## Beam parameters
        inj_emil_parameter = self.reader.find_unique_string('SIS18BEAM/INJ_EMIL$', self.lh_builder.lh.get_parameters())
        e_parameter = self.reader.find_unique_string('SIS18BEAM/E$', self.lh_builder.lh.get_parameters())
        self.lh_builder.create_child_node(inj_emil_parameter, [ dp_over_p_parameter, e_parameter, h_parameter ])

        ## Optics Parameters
        self.lh_builder.create_child_node(opticsip_parameter, [ sigma_parameter, tau_parameter, incorpip_parameter ])
        self.lh_builder.create_child_node(sigma_parameter, [ brho_start_end_parameter, ext_sigma_parameter, bp_length_parameter, t_wait_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])
        self.lh_builder.create_child_node(tau_parameter, [ tau_nlp_parameter, tau_start_end_parameter, bp_length_parameter, t_wait_parameter, brho_start_end_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])

        ## Timeparam Parameters
        self.lh_builder.create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, ext_sigma_parameter, tau_start_end_parameter, tround_parameter,  bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
        self.lh_builder.create_child_node(incorpip_parameter, bp_length_parameter )


        ## Hardware rf system parameters
        #self.lh_builder.create_child_node(hardware_fs_rampvals_parameter, frev_parameter)

        #self.lh_builder.create_child_node(mhbpar_damp1_parameter, h_parameter )
        #self.lh_builder.create_child_node(mhbpar_damp2_parameter, h_parameter )
        #self.lh_builder.create_child_node(mhbpar_delay_parameter, h_parameter )
        #self.lh_builder.create_child_node(mhbpar_harm1_parameter, h_parameter )
        #self.lh_builder.create_child_node(mhbpar_harm2_parameter, h_parameter )
        #self.lh_builder.create_child_node(syncmode_hfssync_parameter, h_parameter )
        #self.lh_builder.create_child_node(workmode_workmode_parameter, h_parameter )

        #self.lh_builder.create_child_node(delay_trgdelay_parameter, [ tbunch_parameter, h_parameter, start_parameter ])
        #self.lh_builder.create_child_node(harmonic_harmonic_parameter, h_parameter )
        #self.lh_builder.create_child_node(mode_kickmode_parameter, [ kicker_mode_parameter, nbunch1_parameter, h_parameter ])
        #self.lh_builder.create_child_node(rftrig_rftrig_parameter, h_parameter )

        #self.lh_builder.create_child_node(chansequ_chancount_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter,    kicker_mode_parameter ])
        #self.lh_builder.create_child_node(chansequ_chansequ_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter,   kicker_mode_parameter ])
        #self.lh_builder.create_child_node(evtarray_chanarray_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter, kicker_mode_parameter ])

        ## Main sextupoles:
        for device in self.main_sextupoles:
            kldelta_parameter = self.reader.find_unique_string(device + '/KLDELTA$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kldelta_parameter, [ incorpip_parameter, kl_harm_parameter, kl_phase_parameter, kl_ampl_parameter, kl_offset_parameter ])

            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())    
            self.lh_builder.create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter, kldelta_parameter ]) 

        ## Horizontal_orbit_correction_coils
        self.horizontal_orbit_correction_coils.sort()
        for device in self.horizontal_orbit_correction_coils:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            sector = int(device[1:3])
            index = sector - 1
            if (sector == 5) :
                self.lh_builder.create_child_node(kl_parameter, [ extesep_parameter, opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
            elif (sector == 7) :
                self.lh_builder.create_child_node(kl_parameter, [ extmsep_parameter, opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
            else:
                self.lh_builder.create_child_node(kl_parameter, [ opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])

        ## Extraction_bump_correction_coils
        for device in self.extraction_bump_correction_coils:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            sector = int(device[1:3])
            if ((sector == 10) | (sector == 11) | (sector == 12)) :
                self.lh_builder.create_child_node(kl_parameter, opticsip_parameter)
            elif ((sector == 4) | (sector == 5)) :
                self.lh_builder.create_child_node(kl_parameter, [ opticsip_parameter, extesep_parameter ])
            else:
                self.lh_builder.create_child_node(kl_parameter, [ opticsip_parameter, extmsep_parameter ])


        ## Orbit Parameters
        self.lh_builder.create_child_node(coh01_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh02_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh03_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh04_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh05_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh06_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh07_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh08_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh09_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh10_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh11_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(coh12_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov01_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov02_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov03_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov04_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov05_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov06_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov07_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov08_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov09_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov10_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov11_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(cov12_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(extesep_parameter, incorpip_parameter )
        self.lh_builder.create_child_node(extmsep_parameter, incorpip_parameter )


        for device in self.sis18_cavities_ampl:
            urf_parameter = self.reader.find_unique_string(device[:-1] + 'A/URF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_parameter, [ h_parameter, incorpip_parameter, urfring_parameter, rf_mode_parameter ])
            #rampvals_a_parameter = self.reader.find_unique_string(device[:-1] + 'A/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_a_parameter, urf_parameter )

            frf_parameter = self.reader.find_unique_string(device[:-1] + 'FS/FRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(frf_parameter, [ h_parameter, incorpip_parameter, frfring_parameter, rf_mode_parameter ])
            #rampvals_fs_parameter = self.reader.find_unique_string(device[:-1] + 'FS/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_fs_parameter, frf_parameter )

            prf_parameter = self.reader.find_unique_string(device[:-1] + 'P/PRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(prf_parameter, [ h_parameter, incorpip_parameter, prfring_parameter, rf_mode_parameter ])
            #rampvals_p_parameter = self.reader.find_unique_string(device[:-1] + 'P/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_p_parameter, prf_parameter )

            #brotampl_parameter = self.reader.find_unique_string(device[:-1] + 'A/BROTAMPL#highValue$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(brotampl_parameter, urf_parameter )

        ## Magnets

        for device in self.vertical_correctors:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            sector = int(device[1:3])
            index = sector - 1
            self.lh_builder.create_child_node(kl_parameter, [ opticsip_parameter, cov_list[index], cov_list[index - 1], cov_list[index + 1 - len(cov_list)] ])

            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, i_parameter)

        for device in self.horizontal_correction_coils:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            blcorr_parameter = self.reader.find_unique_string(device + '/B[0-3]?LCORR$', self.lh_builder.lh.get_parameters())
            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            if device in self.extraction_bump_correction_coils:
                self.lh_builder.create_child_node(blcorr_parameter, [ brho_parameter, kl_parameter ])
            else:
                self.lh_builder.create_child_node(blcorr_parameter, [ brho_parameter, kl_parameter, incorpip_parameter ])

            for dipol_device in self.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                bl_parameter = self.reader.find_unique_string(dipol_device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(icorr_parameter, [ i_parameter, blcorr_parameter, bl_parameter ])

        for device in self.extra_correction_coils:
            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            icorrdot_parameter = self.reader.find_unique_string(device + '/ICORRDOT$', self.lh_builder.lh.get_parameters())
            ucorr_parameter = self.reader.find_unique_string(device + '/UCORR$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(icorrdot_parameter, icorr_parameter )

            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, [ icorr_parameter, ucorr_parameter ])
    
            for dipol_device in self.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                idot_parameter = self.reader.find_unique_string(dipol_device + '/IDOT$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(ucorr_parameter, [ icorr_parameter, icorrdot_parameter, i_parameter, idot_parameter ])

        for device in list(set(self.horizontal_correction_coils) - set(self.extra_correction_coils)):
            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, icorr_parameter)

        ## Kicker
        kicker_ukick_parameters = []
        for device in self.kicker:
            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            kicker_ukick_parameters.append(ukick_parameter)



        self.kicker.sort()
        for device in self.kicker:
            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ kicker_knob_parameter , opticsip_parameter ])

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , brho_parameter ])

            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(ukick_parameter, bl_parameter )

            #if (device == self.kicker[0]):
                #timdelrf_time_parameter = self.reader.find_unique_string(device + '/TIMDELRF#time$', self.lh_builder.lh.get_parameters())
                #self.lh_builder.create_child_node(timdelrf_time_parameter, toffset1_parameter)
        
                #timdeltg_time_parameter = self.reader.find_unique_string(device + '/TIMDELTG#time$', self.lh_builder.lh.get_parameters())
                #self.lh_builder.create_child_node(timdeltg_time_parameter, toffset2_parameter)
        
                #timftrf_time_parameter = self.reader.find_unique_string(device + '/TIMFTRF#time$', self.lh_builder.lh.get_parameters())
                #self.lh_builder.create_child_node(timftrf_time_parameter, [ toffset1_parameter, thigh1_parameter ])
        
                #timfttg_time_parameter = self.reader.find_unique_string(device + '/TIMFTTG#time$', self.lh_builder.lh.get_parameters())
                #self.lh_builder.create_child_node(timfttg_time_parameter, [ toffset2_parameter, thigh2_parameter ])
        
                #voltrfs_voltages_parameter = self.reader.find_unique_string(device + '/VOLTRFS#voltages$', self.lh_builder.lh.get_parameters())
                #self.lh_builder.create_child_node(voltrfs_voltages_parameter, kicker_ukick_parameters)
        
                #voltris_voltages_parameter = self.reader.find_unique_string(device + '/VOLTRIS#voltages$', self.lh_builder.lh.get_parameters())
                #self.lh_builder.create_child_node(voltris_voltages_parameter, kicker_ukick_parameters)
        
                #volttgs_voltages_parameter = self.reader.find_unique_string(device + '/VOLTTGS#voltages$', self.lh_builder.lh.get_parameters())
                #self.lh_builder.create_child_node(volttgs_voltages_parameter, kicker_ukick_parameters)


        ## Bumper
        for device in self.bumper:
            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ opticsip_parameter, bumper_knob_parameter ])

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ brho_parameter, kl_parameter ])

            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter )

            #currents_currents_parameter = self.reader.find_unique_string(device + '/CURRENTS#currents$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(currents_currents_parameter, i_parameter )

            #ftimes_ftimes_parameter = self.reader.find_unique_string(device + '/FTIMES#ftimes$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(ftimes_ftimes_parameter, tfall_parameter )

            #para_reference_parameter = self.reader.find_unique_string(device + '/PARA#reference_parameters$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(para_reference_parameter, curvature_parameter )


        ## SIS18 Bypass
        for device in self.sis18_bypass:
            kl_parameter = self.reader.find_unique_string(device + '/KLBYP$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, opticsip_parameter )

            bl_parameter = self.reader.find_unique_string(device + '/BLBYP$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , brho_parameter ])

            ibyp_parameter = self.reader.find_unique_string(device + '/IBYP$', self.lh_builder.lh.get_parameters())
            for dipol_device in self.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(ibyp_parameter, [ bl_parameter , incorpip_parameter , i_parameter ])

            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, i_parameter )

        ## SIS18 KO
        for device in self.sis18_ko_exiter:
            start_tau_parameter = self.reader.find_unique_string(device + '/START_TAU$', self.lh_builder.lh.get_parameters())
            end_tau_parameter = self.reader.find_unique_string(device + '/END_TAU$', self.lh_builder.lh.get_parameters())
            start_ampl_parameter = self.reader.find_unique_string(device + '/START_AMPL$', self.lh_builder.lh.get_parameters())
            end_ampl_parameter = self.reader.find_unique_string(device + '/END_AMPL$', self.lh_builder.lh.get_parameters())
            upp_parameter = self.reader.find_unique_string(device + '/UPP$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(upp_parameter, [ start_tau_parameter, end_tau_parameter, start_ampl_parameter, end_ampl_parameter, erho_parameter, tgrid_parameter, bp_length_parameter ])

            uctrl_parameter = self.reader.find_unique_string(device + '/UCTRL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(uctrl_parameter, [ upp_parameter, incorpip_parameter ])

            dqh_parameter = self.reader.find_unique_string(device + '/DQH$', self.lh_builder.lh.get_parameters())
            qhfr_parameter = self.reader.find_unique_string(device + '/QHFR$', self.lh_builder.lh.get_parameters())
            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, [ h_parameter, frev_parameter, dqh_parameter, uctrl_parameter, qhfr_parameter ])



        return self.lh_builder
