#!/bin/env python2.6

from lh_builder_utils import LHBuilderUtils


class GenericParameters:

    def __init__(self, lh_builder, csv_filename):
        self.lh_builder = lh_builder
        self.reader = LHBuilderUtils()
        self.all_devices = self.reader._read_devices(csv_filename)

    def setmaindipole(self, main_dipoles):
        self.main_dipoles = main_dipoles

    def sethorizontal_correctors(self, horizontal_correctors):
        self.horizontal_correctors = horizontal_correctors
    def setvertical_correctors(self, vertical_correctors):
        self.vertical_correctors = vertical_correctors

    def setmain_quadrupoles(self, main_quadrupoles):
        self.main_quadrupoles = main_quadrupoles
    def setextraction_quadrupoles(self, extraction_quadrupoles):
        self.extraction_quadrupoles = extraction_quadrupoles
    def setcorrection_quadrupoles(self, correction_quadrupoles):
        self.correction_quadrupoles = correction_quadrupoles

    def setmain_sextupoles(self, main_sextupoles):
        self.main_sextupoles = main_sextupoles
    def setchromaticity_sextupoles(self, chromaticity_sextupoles):
        self.chromaticity_sextupoles = chromaticity_sextupoles
    def setresonance_sextupoles(self, resonance_sextupoles):
        self.resonance_sextupoles = resonance_sextupoles
    def setcorrection_sextupoles(self, correction_sextupoles):
        self.correction_sextupoles = correction_sextupoles

    def setcorrection_octupoles(self, correction_octupoles):
        self.correction_octupoles = correction_octupoles

    def setcavities(self, cavities):
        self.cavities = cavities

    def setkicker(self, kicker):
        self.kicker = kicker


    def getdevices(self):
        return self.all_devices

    def build(self, particle_transfer):

        all_correctors = self.horizontal_correctors + self.vertical_correctors

        ## Standard beam and logical devices
        beam_device = self.reader.find_unique_string(particle_transfer.replace('_RING', 'BEAM'), self.all_devices)
        optics_device = self.reader.find_unique_string(particle_transfer.replace('_RING','OPTICS'), self.all_devices)
        orbit_device = self.reader.find_unique_string(particle_transfer.replace('_RING','ORBIT'), self.all_devices)
        rf_device = self.reader.find_unique_string(particle_transfer.replace('_RING','RF'), self.all_devices)
        timeparam_device = self.reader.find_unique_string(particle_transfer.replace('_RING','TIMEPARAM'), self.all_devices)
        kicker_device = self.reader.find_unique_string(particle_transfer.replace('_RING','KICKER'), self.all_devices)
        #bumper_device = reader.find_unique_string(particle_transfer.replace('_RING','BUMPER'), self.all_devices)


        ## Beam parameters
        a_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/A', 'SCALAR_A', beam_device, belongs_to_function_bproc=False)
        alphac_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/ALPHAC', 'ALPHAC', beam_device, is_trimable=False)
        aoq_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/AOQ', 'SCALAR_AOQ', beam_device, is_trimable=False, belongs_to_function_bproc=False)
        brho_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/BRHO', 'BRHO', beam_device, is_trimable=False)
        brhodot_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/BRHODOT', 'BRHODOT', beam_device, is_trimable=False)
        brho_start_end_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/BRHO_START_END', 'SCALAR_BRHO', beam_device, is_trimable=False)
        bucketfill_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/BUCKETFILL', 'SCALAR_BUCKETFILL', beam_device)
        bunchfactor_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/BUNCHFACTOR', 'BUNCHFACTOR', beam_device)
        bunchpattern_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/BUNCHPATTERN', 'SCALAR_BUNCHPATTERN', beam_device)
        ch_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/CH', 'CHROMATICITY', beam_device)
        cv_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/CV', 'CHROMATICITY', beam_device)
        deltar_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/DELTAR', 'DELTAR', beam_device)
        e_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/E', 'SCALAR_E', beam_device)
        element_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/ELEMENT', 'SCALAR_ELEMENT', beam_device, belongs_to_function_bproc=False)
        erho_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/ERHO', 'ERHO', beam_device, is_trimable=False)
        eta_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/ETA', 'ETA', beam_device, is_trimable=False)
        frev_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/FREV', 'FREV', beam_device, is_trimable=False)
        gamma_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/GAMMA', 'GAMMA', beam_device, is_trimable=False)
        geofact_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/GEOFACT', 'GEOFACT', beam_device)
        h_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/H', 'SCALAR_H', beam_device)
        inj_emih_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/INJ_EMIH', 'SCALAR_INJ_EMIH', beam_device, belongs_to_function_bproc=False)
        inj_emil_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/INJ_EMIL', 'SCALAR_INJ_EMIL', beam_device, belongs_to_function_bproc=False)
        inj_emiv_parameter =self.lh_builder.lh.define_physics_parameter(beam_device + '/INJ_EMIV', 'SCALAR_INJ_EMIV', beam_device, belongs_to_function_bproc=False)
        isotope_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/ISOTOPE', 'SCALAR_ISOTOPE', beam_device, belongs_to_function_bproc=False)
        kl_ampl_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/KL_AMPL', 'SCALAR_KL_AMPL', beam_device)
        kl_harm_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/KL_HARM', 'SCALAR_KL_HARM', beam_device)
        kl_offset_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/KL_OFFSET', 'SCALAR_KL_OFFSET', beam_device)
        kl_phase_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/KL_PHASE', 'SCALAR_KL_PHASE', beam_device)
        maxrh_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/MAXRH', 'MAXRH', beam_device, is_trimable=False)
        maxrv_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/MAXRV', 'MAXRV', beam_device, is_trimable=False)
        nparticles_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/NPARTICLES', 'SCALAR_NPARTICLES', beam_device, belongs_to_function_bproc=False)
        nperbunch_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/NPERBUNCH', 'SCALAR_NPERBUNCH', beam_device, is_trimable=False)
        phis_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/PHIS', 'PHIS', beam_device, is_trimable=False)
        q_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/Q', 'SCALAR_Q', beam_device, belongs_to_function_bproc=False)
        qh_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/QH', 'TUNE', beam_device)
        qv_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/QV', 'TUNE', beam_device)
        tbunch_parameter =  self.lh_builder.lh.define_physics_parameter(beam_device + '/TBUNCH', 'SCALAR_TBUNCH', beam_device, is_trimable=False)
        trev_parameter = self.lh_builder.lh.define_physics_parameter(beam_device + '/TREV', 'TREV', beam_device, is_trimable=False)


        ## RF parameters
        abkt_parameter =  self.lh_builder.lh.define_physics_parameter(rf_device + '/ABKT', 'ABKT', rf_device)
        dualh_parameter = self.lh_builder.lh.define_physics_parameter(rf_device + '/DUALH', 'SCALAR_DUALH', rf_device)
        dualhip_parameter = self.lh_builder.lh.define_physics_parameter(rf_device + '/DUALHIP', 'DUALHIP', rf_device)
        frfring_parameter = self.lh_builder.lh.define_physics_parameter(rf_device + '/FRFRING', 'FRFRING', rf_device, is_trimable=False)
        rf_mode_parameter = self.lh_builder.lh.define_physics_parameter(rf_device + '/MODE', 'SCALAR_CAVITY_MODE', rf_device)
        prfring_parameter = self.lh_builder.lh.define_physics_parameter(rf_device + '/PRFRING', 'PRFRING', rf_device, is_trimable=False)
        urfring_parameter = self.lh_builder.lh.define_physics_parameter(rf_device + '/URFRING', 'URFRING', rf_device, is_trimable=False)
        urfsc_parameter = self.lh_builder.lh.define_physics_parameter(rf_device + '/URFSC', 'URFSC', rf_device, is_trimable=False)

        for device in self.cavities:
            self.lh_builder.lh.define_physics_parameter(device + '/URF', 'URF', device)
            self.lh_builder.lh.define_physics_parameter(device + '/FRF', 'FRF', device)
            self.lh_builder.lh.define_physics_parameter(device + '/PRF', 'PRF', device)

        ## Optics parameters
        #ext_sigma_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/EXT_SIGMA', 'SCALAR_EXT_SIGMA', optics_device)
        opticsip_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/OPTICSIP', 'OPTICSIP', optics_device)
        #sigma_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/SIGMA', 'SIGMA', optics_device)
        #tau_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/TAU', 'TAU', optics_device)
        #tau_endpoint_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/TAU_ENDPOINT', 'SCALAR_TAU_ENDPOINT', optics_device)
        #tau_nlp_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/TAU_NLP', 'SCALAR_TAU_NLP', optics_device)
        tau_start_end_parameter = self.lh_builder.lh.define_physics_parameter(optics_device + '/TAU_START_END', 'SCALAR_TAU', optics_device)

        ## Timeparam parameters
        bdot_parameter = self.lh_builder.lh.define_physics_parameter(timeparam_device + '/BDOT', 'SCALAR_BDOT', timeparam_device)
        bp_length_parameter = self.lh_builder.lh.define_physics_parameter(timeparam_device + '/BP_LENGTH', 'SCALAR_BP_LENGTH', timeparam_device, is_trimable=False)
        incorpip_parameter = self.lh_builder.lh.define_physics_parameter(timeparam_device + '/INCORPIP', 'INCORPIP', timeparam_device, is_trimable=False)
        tgrid_parameter = self.lh_builder.lh.define_physics_parameter(timeparam_device + '/TGRID', 'SCALAR_TGRID', timeparam_device)
        tround_parameter = self.lh_builder.lh.define_physics_parameter(timeparam_device + '/TROUND', 'SCALAR_TROUND', timeparam_device)
        t_bp_length_parameter = self.lh_builder.lh.define_physics_parameter(timeparam_device + '/T_BP_LENGTH', 'SCALAR_T_BP_LENGTH', timeparam_device)
        t_wait_parameter = self.lh_builder.lh.define_physics_parameter(timeparam_device + '/T_WAIT', 'SCALAR_T_WAIT', timeparam_device)

        ## Kicker parameters
        #kicker_knob_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', kicker_device)
        kicker_mode_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/MODE', 'SCALAR_KICKER_MODE', kicker_device)
        nbunch1_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/NBUNCH1', 'SCALAR_NBUNCH1', kicker_device)
        start_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/START', 'SCALAR_KICKER_START', kicker_device)
        thigh1_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/THIGH1', 'SCALAR_KICKER_THIGH1', kicker_device)
        thigh2_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/THIGH2', 'SCALAR_KICKER_THIGH2', kicker_device)
        toffset1_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/TOFFSET1', 'SCALAR_KICKER_TOFFSET1', kicker_device)
        toffset2_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/TOFFSET2', 'SCALAR_KICKER_TOFFSET2', kicker_device)


        ## Magnet groups according to multipole
        all_dipoles = self.main_dipoles + self.horizontal_correctors + self.vertical_correctors
        all_quadrupoles = self.main_quadrupoles + self.extraction_quadrupoles + self.correction_quadrupoles
        all_sextupoles = self.main_sextupoles + self.correction_sextupoles
        all_octupoles = self.correction_octupoles

        all_magnets = all_dipoles + all_quadrupoles + all_sextupoles + all_octupoles
        main_magnets = self.main_dipoles + self.main_quadrupoles

        kicker = self.kicker

        for device in all_dipoles:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B0L', device)

        for device in all_quadrupoles:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K1L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B1L', device)

        for device in all_sextupoles:
            #self.lh_builder.lh.define_physics_parameter(device + '/KLDELTA', 'DELTA_K2L', device) ## KLDELTA soll nicht fuer S02KM5SS und S08KM5SS angelegt werden, hier muss noch eine extra gruppe / hierarchie erstellt werden
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K2L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B2L', device)

        for device in all_octupoles:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K3L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B3L', device)

        for device in kicker:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BL', 'SCALAR_B0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/UKICK', 'SCALAR_UKICK', device)
            #if device == 'S05MK2E': # Skip these parameters for the seconds kicker in SIS18
                #continue
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMDELRF', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMDELTG', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMFTRF', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMFTTG', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTRFS', 'voltages')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTRIS', 'voltages')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTTGS', 'voltages')

        for device in all_magnets:
            self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        for device in main_magnets:
            self.lh_builder.lh.define_physics_parameter(device + '/IDOT', 'IDOT', device)
            self.lh_builder.lh.define_physics_parameter(device + '/UEDDY', 'UEDDY', device)
            self.lh_builder.lh.define_physics_parameter(device + '/U', 'U', device)

        ### Creation of relations

        ## Beam Parameters
        self.lh_builder.create_child_node(a_parameter, [ isotope_parameter, element_parameter ])
        self.lh_builder.create_child_node(alphac_parameter, opticsip_parameter )
        self.lh_builder.create_child_node(aoq_parameter, [ a_parameter, q_parameter ])
        self.lh_builder.create_child_node(brho_parameter, bp_length_parameter )
        self.lh_builder.create_child_node(brhodot_parameter, bp_length_parameter )
        self.lh_builder.create_child_node(brho_start_end_parameter, [ e_parameter, aoq_parameter ])
        self.lh_builder.create_child_node(bunchfactor_parameter, phis_parameter )
        self.lh_builder.create_child_node(ch_parameter, opticsip_parameter )
        self.lh_builder.create_child_node(cv_parameter, opticsip_parameter )
        self.lh_builder.create_child_node(deltar_parameter, bp_length_parameter )
        self.lh_builder.create_child_node(erho_parameter, [ brho_parameter, aoq_parameter ])
        self.lh_builder.create_child_node(eta_parameter, [ gamma_parameter, alphac_parameter ])
        self.lh_builder.create_child_node(frev_parameter, gamma_parameter )
        self.lh_builder.create_child_node(gamma_parameter, [ brho_parameter, aoq_parameter ])
        self.lh_builder.create_child_node(geofact_parameter, [ brho_start_end_parameter, brho_parameter, inj_emiv_parameter, inj_emih_parameter ])
        self.lh_builder.create_child_node(maxrh_parameter, [ inj_emih_parameter, brho_parameter, opticsip_parameter, brho_start_end_parameter ])
        self.lh_builder.create_child_node(maxrv_parameter, [ inj_emiv_parameter, brho_parameter, opticsip_parameter, brho_start_end_parameter ])
        self.lh_builder.create_child_node(nperbunch_parameter, [ nparticles_parameter, h_parameter, bunchpattern_parameter ])
        self.lh_builder.create_child_node(phis_parameter, [ aoq_parameter, h_parameter, eta_parameter, abkt_parameter, brhodot_parameter, gamma_parameter, inj_emil_parameter, dualhip_parameter, geofact_parameter, e_parameter, nperbunch_parameter, q_parameter ])
        self.lh_builder.create_child_node(qh_parameter, opticsip_parameter )
        self.lh_builder.create_child_node(qv_parameter, opticsip_parameter )
        self.lh_builder.create_child_node(tbunch_parameter, [ h_parameter, trev_parameter ])
        self.lh_builder.create_child_node(trev_parameter, frev_parameter )


        ## RF Parameters
        self.lh_builder.create_child_node(abkt_parameter, [ bp_length_parameter, bucketfill_parameter, inj_emil_parameter, tgrid_parameter ])
        self.lh_builder.create_child_node(dualhip_parameter, [ dualh_parameter, bp_length_parameter ])
        self.lh_builder.create_child_node(frfring_parameter, [ frev_parameter, h_parameter ])
        self.lh_builder.create_child_node(prfring_parameter, phis_parameter )
        self.lh_builder.create_child_node(urfring_parameter, phis_parameter )
        self.lh_builder.create_child_node(urfsc_parameter, phis_parameter )

        ## Optics Parameters
        #self.lh_builder.create_child_node(opticsip_parameter, [ sigma_parameter, tau_parameter, incorpip_parameter ])
        #self.lh_builder.create_child_node(sigma_parameter, [ brho_start_end_parameter, ext_sigma_parameter, bp_length_parameter, t_wait_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])
        #self.lh_builder.create_child_node(tau_parameter, [ tau_nlp_parameter, tau_start_end_parameter, bp_length_parameter, t_wait_parameter, brho_start_end_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])


        ## Timeparam Parameters
        #self.lh_builder.create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, ext_sigma_parameter, tau_start_end_parameter, tround_parameter,  bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
        #self.lh_builder.create_child_node(incorpip_parameter, bp_length_parameter )

        ## Kicker Parameters
        self.lh_builder.create_child_node(thigh1_parameter, [ nbunch1_parameter, tbunch_parameter, h_parameter ])
        self.lh_builder.create_child_node(thigh2_parameter, [ tbunch_parameter, h_parameter, nbunch1_parameter ])
        self.lh_builder.create_child_node(toffset2_parameter, [ toffset1_parameter, thigh1_parameter ])


        ## Magnets
        for device in all_magnets:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ brho_parameter, kl_parameter, incorpip_parameter])

        for device in all_dipoles:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

        for device in self.main_dipoles:
            kl_parameter = self.reader.find_unique_string(device + '/K0?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, opticsip_parameter )

        for device in self.main_quadrupoles:
            kl_parameter = self.reader.find_unique_string(device + '/K1?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ qh_parameter, qv_parameter, opticsip_parameter ])

        for device in self.main_sextupoles:
            #kldelta_parameter = self.reader.find_unique_string(device + '/KLDELTA$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(kldelta_parameter, [ incorpip_parameter, kl_harm_parameter, kl_phase_parameter, kl_ampl_parameter, kl_offset_parameter ])

            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())

            if (device in self.resonance_sextupoles):
                self.lh_builder.create_child_node(kl_parameter, opticsip_parameter)
            else: 
                self.lh_builder.create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter ]) 
                #self.lh_builder.create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter, kldelta_parameter ]) 

            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, i_parameter ) 

        for device in (self.correction_quadrupoles + self.extraction_quadrupoles):
            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, opticsip_parameter )

            bl_parameter = self.reader.find_unique_string(device + '/B[1]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, i_parameter)

        for device in self.chromaticity_sextupoles:
            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())
            if (device in self.resonance_sextupoles):
                self.lh_builder.create_child_node(kl_parameter, opticsip_parameter )
            else:
                self.lh_builder.create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter ])

        for device in main_magnets:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

            idot_parameter = self.reader.find_unique_string(device + '/IDOT$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(idot_parameter, i_parameter)

            ueddy_parameter = self.reader.find_unique_string(device + '/UEDDY$', self.lh_builder.lh.get_parameters())
            u_parameter = self.reader.find_unique_string(device + '/U$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(ueddy_parameter, idot_parameter )   
            self.lh_builder.create_child_node(u_parameter, [ ueddy_parameter, i_parameter, idot_parameter ])

            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, [ u_parameter, i_parameter ])

        for device in all_correctors:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, opticsip_parameter )

        for device in self.correction_sextupoles:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, opticsip_parameter)

            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, i_parameter)

        for device in self.resonance_sextupoles:
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            #rampvals_parameter = self.reader.find_unique_string(device + '/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_parameter, i_parameter)

        for device in self.correction_octupoles:
            kl_parameter = self.reader.find_unique_string(device + '/K0?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, opticsip_parameter )

            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)


        ## Cavities
        for device in self.cavities:
            urf_parameter = self.reader.find_unique_string(device + '/URF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_parameter, [ h_parameter, incorpip_parameter, urfring_parameter, rf_mode_parameter ])

            frf_parameter = self.reader.find_unique_string(device + '/FRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(frf_parameter, [ h_parameter, incorpip_parameter, frfring_parameter, rf_mode_parameter ])

            prf_parameter = self.reader.find_unique_string(device + '/PRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(prf_parameter, [ h_parameter, incorpip_parameter, prfring_parameter, rf_mode_parameter ])


        return self.lh_builder
 
