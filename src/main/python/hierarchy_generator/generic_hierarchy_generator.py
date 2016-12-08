#!/bin/env python2.6

#from lh_builder import LHBuilder

from lh_builder_utils import LHBuilderUtils

from devicedata_xml_parser import XMLParser

class GenericHierarchy:

    def __init__(self, devices):
        self.devices = devices
        self.reader = LHBuilderUtils()
        self.y_prec_parser = XMLParser(self.devices.accelerator_zone , self.devices.rigidity)
        
        self.eddycurrents = True
        
    def generate_linkrules(self):
        
        print ('LinkRules:')
        for device in self.devices.alldevices:
            
            ##print (self.devices._devicelinkrulemap)
            if device in self.devices.devicelinkrulemap:
                linkrule = self.devices.devicelinkrulemap.get(device)
                
                self.lh_builder.lh.add_linkrule_for_device(device,linkrule)
                print (device , linkrule)

    def build(self):

        all_correctors = self.devices.horizontal_correctors + self.devices.vertical_correctors

        ## Standard beam and logical devices
        self.beam_device = self.devices.accelerator_zone.replace('_RING', 'BEAM')
        self.optics_device = self.devices.accelerator_zone.replace('_RING','OPTICS')
        self.orbit_device = self.devices.accelerator_zone.replace('_RING','ORBIT')
        self.rf_device = self.devices.accelerator_zone.replace('_RING','RF')
        self.timeparam_device = self.devices.accelerator_zone.replace('_RING','TIMEPARAM')
        if self.devices.inj_kicker :
            self.inj_kicker_device = self.devices.accelerator_zone.replace('_RING','IKICKER')
        if self.devices.ext_kicker : 
            self.ext_kicker_device = self.devices.accelerator_zone.replace('_RING','EKICKER')
        if self.devices.q_kicker :
            self.qh_kicker_device = self.devices.accelerator_zone.replace('_RING','QHKICKER') 
            self.qv_kicker_device = self.devices.accelerator_zone.replace('_RING','QVKICKER') 
        self.bumper_device = self.devices.accelerator_zone.replace('_RING','BUMPER')

        self.lh_builder.lh.define_device(self.beam_device, 'BEAM', self.devices.accelerator_zone)
        self.lh_builder.lh.define_device(self.optics_device, 'OPTICS', self.devices.accelerator_zone)
        self.lh_builder.lh.define_device(self.orbit_device, 'ORBIT', self.devices.accelerator_zone)
        self.lh_builder.lh.define_device(self.rf_device, 'RF', self.devices.accelerator_zone)
        self.lh_builder.lh.define_device(self.timeparam_device, 'TIMEPARAM', self.devices.accelerator_zone)
        if self.devices.inj_kicker :
            self.lh_builder.lh.define_device(self.inj_kicker_device, 'KICKER', self.devices.accelerator_zone)
        if self.devices.ext_kicker :
            self.lh_builder.lh.define_device(self.ext_kicker_device, 'KICKER', self.devices.accelerator_zone)
        if self.devices.q_kicker :
            self.lh_builder.lh.define_device(self.qh_kicker_device, 'KICKER', self.devices.accelerator_zone)
            self.lh_builder.lh.define_device(self.qv_kicker_device, 'KICKER', self.devices.accelerator_zone)
#        self.lh_builder.lh.define_device(self.bumper_device, 'BUMPER', self.devices.accelerator_zone)


        ## Beam parameters
        self.a_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/A', 'SCALAR_A', self.beam_device)
        self.alphac_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ALPHAC', 'ALPHAC', self.beam_device, is_trimable=False)
        self.alphadr_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ALPHADR', 'ALPHADR', self.beam_device, is_trimable=False)
        self.aoq_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/AOQ', 'SCALAR_AOQ', self.beam_device, is_trimable=False)
        self.brho_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BRHO', 'BRHO', self.beam_device, is_trimable=False)
        self.brhodot_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BRHODOT', 'BRHODOT', self.beam_device, is_trimable=False)
        self.brho_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BRHO_START_END', 'SCALAR_BRHO', self.beam_device, is_trimable=False)
        self.bucketfill_raw_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BUCKETFILL_RAW', 'SCALAR_BUCKETFILL_RAW', self.beam_device)
        self.bucketfill_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BUCKETFILL', 'SCALAR_BUCKETFILL', self.beam_device)
        self.bunchfactor_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BUNCHFACTOR', 'BUNCHFACTOR', self.beam_device)
        self.inj_bunchpattern_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/INJ_BUNCHPATTERN', 'SCALAR_INJ_BUNCHPATTERN', self.beam_device)
        self.bunchpattern_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BUNCHPATTERN', 'SCALAR_BUNCHPATTERN', self.beam_device)
        self.ch_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CH', 'CHROMATICITY', self.beam_device, y_prec=4)
        self.ch_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CH_END', 'SCALAR_CHROMATICITY', self.beam_device)
        self.ch_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CH_START_END', 'SCALAR_CHROMATICITY_START_END', self.beam_device)
        self.ch_theo_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CH_THEO', 'CHROMATICITY_THEO', self.beam_device, y_prec=4)
        self.cv_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CV', 'CHROMATICITY', self.beam_device, y_prec=4)
        self.cv_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CV_END', 'SCALAR_CHROMATICITY', self.beam_device)
        self.cv_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CV_START_END', 'SCALAR_CHROMATICITY_START_END', self.beam_device)
        self.cv_theo_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CV_THEO', 'CHROMATICITY_THEO', self.beam_device, y_prec=4)
        self.dch_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DCH', 'DCHROMATICITY', self.beam_device, y_prec=4)
        self.dcv_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DCV', 'DCHROMATICITY', self.beam_device, y_prec=4)
        self.deltar_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DELTAR', 'DELTAR', self.beam_device)
        self.dpbl_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DPBL', 'DPBL', self.beam_device)
        self.dpdr_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DPDR', 'DPDR', self.beam_device)
        self.dpfrev_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DPFREV', 'DPFREV', self.beam_device)
        self.dqh_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DQH', 'DTUNE', self.beam_device, y_prec=8)
        self.dqv_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/DQV', 'DTUNE', self.beam_device, y_prec=8)
        self.e_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/E', 'SCALAR_E', self.beam_device)
        self.e_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/E_START_END', 'SCALAR_E_START_END', self.beam_device, is_trimable=False)
        self.element_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ELEMENT', 'SCALAR_ELEMENT', self.beam_device) 
        self.emil_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/EMIL', 'SCALAR_EMIL', self.beam_device)
        self.erho_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ERHO', 'ERHO', self.beam_device, is_trimable=False)
        self.eta_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ETA', 'ETA', self.beam_device, is_trimable=False)
        self.frev_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/FREV', 'FREV', self.beam_device, is_trimable=False)
        self.gamma_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/GAMMA', 'GAMMA', self.beam_device, is_trimable=False)
        self.gamma_t_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/GAMMA_T', 'GAMMA_T', self.beam_device, is_trimable=False)
        self.geofact_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/GEOFACT', 'GEOFACT', self.beam_device)
        self.h_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/H', 'SCALAR_H', self.beam_device)
        self.inj_emih_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/INJ_EMIH', 'SCALAR_INJ_EMIH', self.beam_device)
        self.inj_emil_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/INJ_EMIL', 'SCALAR_INJ_EMIL', self.beam_device)
        self.inj_emiv_parameter =self.lh_builder.lh.define_physics_parameter(self.beam_device + '/INJ_EMIV', 'SCALAR_INJ_EMIV', self.beam_device)
        self.isotope_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ISOTOPE', 'SCALAR_ISOTOPE', self.beam_device)
        self.kl_ampl_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/KL_AMPL', 'SCALAR_KL_AMPL', self.beam_device)
        self.kl_harm_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/KL_HARM', 'SCALAR_KL_HARM', self.beam_device)
        self.kl_offset_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/KL_OFFSET', 'SCALAR_KL_OFFSET', self.beam_device)
        self.kl_phase_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/KL_PHASE', 'SCALAR_KL_PHASE', self.beam_device)
        self.maxrh_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/MAXRH', 'MAXRH', self.beam_device, is_trimable=False)
        self.maxrv_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/MAXRV', 'MAXRV', self.beam_device, is_trimable=False)
        self.nparticles_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/NPARTICLES', 'SCALAR_NPARTICLES', self.beam_device)
        self.nperbunch_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/NPERBUNCH', 'SCALAR_NPERBUNCH', self.beam_device, is_trimable=False)
        self.phis_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/PHIS', 'PHIS', self.beam_device, is_trimable=False)
        self.q_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/Q', 'SCALAR_Q', self.beam_device)
        self.qh_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QH', 'TUNE', self.beam_device, y_prec=8)
        self.qh_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QH_END', 'SCALAR_TUNE', self.beam_device)
        self.qh_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QH_START_END', 'SCALAR_TUNE_START_END', self.beam_device)
        self.qh_theo_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QH_THEO', 'TUNE_THEO', self.beam_device, y_prec=8)
        self.qv_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QV', 'TUNE', self.beam_device, y_prec=8)
        self.qv_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QV_END', 'SCALAR_TUNE', self.beam_device)
        self.qv_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QV_START_END', 'SCALAR_TUNE_START_END', self.beam_device)
        self.qv_theo_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/QV_THEO', 'TUNE_THEO', self.beam_device, y_prec=8)
        self.tbunch_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/TBUNCH', 'SCALAR_TBUNCH', self.beam_device, is_trimable=False)
        self.trev_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/TREV', 'TREV', self.beam_device, is_trimable=False)

        self.lh_builder.lh.add_parameter_to_system(self.a_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.alphac_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.alphadr_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.aoq_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.brho_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.brhodot_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.brho_start_end_parameter, 'BEAM')

        self.lh_builder.lh.add_parameter_to_system(self.bucketfill_raw_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.bucketfill_raw_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.bucketfill_raw_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.bucketfill_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.bunchfactor_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.inj_bunchpattern_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.inj_bunchpattern_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.inj_bunchpattern_parameter, 'generation')

        self.lh_builder.lh.add_parameter_to_system(self.bunchpattern_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.ch_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.ch_end_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.ch_start_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.ch_theo_parameter, 'BEAM')

        self.lh_builder.lh.add_parameter_to_system(self.ch_parameter, 'BEAM')
        #self.lh_builder.lh.add_parameter_to_system(self.ch_parameter, 'generation')        
        
        self.lh_builder.lh.add_parameter_to_system(self.cv_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.cv_end_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.cv_start_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.cv_theo_parameter, 'BEAM')

        self.lh_builder.lh.add_parameter_to_system(self.cv_parameter, 'BEAM')
        #self.lh_builder.lh.add_parameter_to_system(self.cv_parameter, 'generation')

        self.lh_builder.lh.add_parameter_to_system(self.dch_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.dcv_parameter, 'BEAM')

        self.lh_builder.lh.add_parameter_to_system(self.deltar_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.deltar_parameter, 'generation')

        self.lh_builder.lh.add_parameter_to_system(self.dpbl_parameter, 'BEAM')

        self.lh_builder.lh.add_parameter_to_system(self.dpdr_parameter, 'BEAM')

        self.lh_builder.lh.add_parameter_to_system(self.dpfrev_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.dpfrev_parameter, 'generation')

        self.lh_builder.lh.add_parameter_to_system(self.dqh_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.dqv_parameter, 'BEAM')

        self.lh_builder.lh.add_parameter_to_system(self.e_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.e_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.e_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.e_start_end_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.element_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.element_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.element_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.emil_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.erho_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.eta_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.frev_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.frev_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.gamma_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.gamma_t_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.geofact_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.h_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.h_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.h_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.inj_emih_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.inj_emih_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.inj_emih_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.inj_emil_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.inj_emil_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.inj_emil_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.inj_emiv_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.inj_emiv_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.inj_emiv_parameter, 'generation')
       
        self.lh_builder.lh.add_parameter_to_system(self.isotope_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.isotope_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.isotope_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.kl_ampl_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.kl_ampl_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.kl_ampl_parameter, 'generation')
       
        self.lh_builder.lh.add_parameter_to_system(self.kl_harm_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.kl_harm_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.kl_harm_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.kl_offset_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.kl_offset_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.kl_offset_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.kl_phase_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.kl_phase_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.kl_phase_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.maxrh_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.maxrv_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.nparticles_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.nparticles_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.nparticles_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.nperbunch_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.phis_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.q_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.q_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.q_parameter, 'generation')

        self.lh_builder.lh.add_parameter_to_system(self.qh_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.qh_end_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.qh_start_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.qh_theo_parameter, 'BEAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.qh_parameter, 'BEAM')
        #self.lh_builder.lh.add_parameter_to_system(self.qh_parameter, 'generation')

        self.lh_builder.lh.add_parameter_to_system(self.qv_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.qv_end_parameter, 'generation')
        self.lh_builder.lh.add_parameter_to_system(self.qv_start_end_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.qv_theo_parameter, 'BEAM')
       
        self.lh_builder.lh.add_parameter_to_system(self.qv_parameter, 'BEAM')
        #self.lh_builder.lh.add_parameter_to_system(self.qv_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.tbunch_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.trev_parameter, 'BEAM')

        ## RF parameters
        self.abkt_parameter =  self.lh_builder.lh.define_physics_parameter(self.rf_device + '/ABKT', 'ABKT', self.rf_device)
        self.dualh_raw_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/DUALH_RAW', 'SCALAR_DUALH_RAW', self.rf_device)
        self.dualh_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/DUALH', 'SCALAR_DUALH', self.rf_device)
        self.dualhip_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/DUALHIP', 'DUALHIP', self.rf_device)
        self.rf_mode_2D_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/MODE2D', 'SCALAR_CAVITY_MODE_2D', self.rf_device)
        self.prfring_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/PRFRING', 'PRFRING', self.rf_device, is_trimable=False)
        self.urfring_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/URFRING', 'URFRING', self.rf_device, is_trimable=False)
        self.urfsc_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/URFSC', 'URFSC', self.rf_device, is_trimable=False)
        self.phase_offset_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/PHASE_OFFSET', 'SCALAR_PHASE_OFFSET', self.rf_device)

        self.cavity2harmonic_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/CAVITY2HARMONIC', 'SCALAR_CAVITY2HARMONIC', self.rf_device)

        self.cavitypattern_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/CAVITYPATTERN', 'SCALAR_CAVITYPATTERN', self.rf_device)
        
        self.lh_builder.lh.add_parameter_to_system(self.cavity2harmonic_parameter, 'RF')
        
        self.lh_builder.lh.add_parameter_to_system(self.cavitypattern_parameter, 'RF')
        self.lh_builder.lh.add_parameter_to_system(self.cavitypattern_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.cavitypattern_parameter, 'generation')

        self.lh_builder.lh.add_parameter_to_system(self.abkt_parameter, 'RF')
        
        self.lh_builder.lh.add_parameter_to_system(self.dualh_raw_parameter, 'RF')
        self.lh_builder.lh.add_parameter_to_system(self.dualh_raw_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.dualh_raw_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.dualh_parameter, 'RF')
        
        self.lh_builder.lh.add_parameter_to_system(self.dualhip_parameter, 'RF')
        
        self.lh_builder.lh.add_parameter_to_system(self.rf_mode_2D_parameter, 'RF')
        self.lh_builder.lh.add_parameter_to_system(self.rf_mode_2D_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.rf_mode_2D_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.prfring_parameter, 'RF')
        self.lh_builder.lh.add_parameter_to_system(self.urfring_parameter, 'RF')
        self.lh_builder.lh.add_parameter_to_system(self.urfsc_parameter, 'RF')
        
        self.lh_builder.lh.add_parameter_to_system(self.phase_offset_parameter, 'RF')
        self.lh_builder.lh.add_parameter_to_system(self.phase_offset_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.phase_offset_parameter, 'generation')

        self.rf_manipulation_raw_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/RF_MANIPULATION_RAW', 'SCALAR_RF_MANIPULATION_RAW', self.rf_device)
        self.lh_builder.lh.add_parameter_to_system(self.rf_manipulation_raw_parameter, 'RF')
        self.lh_builder.lh.add_parameter_to_system(self.rf_manipulation_raw_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.rf_manipulation_raw_parameter, 'generation')
            
        self.rf_manipulation_parameter = self.lh_builder.lh.define_physics_parameter(self.rf_device + '/RF_MANIPULATION', 'SCALAR_RF_MANIPULATION', self.rf_device)
        self.lh_builder.lh.add_parameter_to_system(self.rf_manipulation_parameter, 'RF')

        ## Optics parameters
        #ext_sigma_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/EXT_SIGMA', 'SCALAR_EXT_SIGMA', self.optics_device)
        self.opticsip_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/OPTICSIP', 'OPTICSIP', self.optics_device)

        self.lh_builder.lh.add_parameter_to_system(self.opticsip_parameter, 'OPTICS')
        
        #sigma_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/SIGMA', 'SIGMA', self.optics_device)
        #tau_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/TAU', 'TAU', self.optics_device)
        #tau_endpoint_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/TAU_ENDPOINT', 'SCALAR_TAU_ENDPOINT', self.optics_device)
        #tau_nlp_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/TAU_NLP', 'SCALAR_TAU_NLP', self.optics_device)
        self.tau_start_end_parameter = self.lh_builder.lh.define_physics_parameter(self.optics_device + '/TAU_START_END', 'SCALAR_TAU', self.optics_device)

        self.lh_builder.lh.add_parameter_to_system(self.tau_start_end_parameter, 'OPTICS')
        self.lh_builder.lh.add_parameter_to_system(self.tau_start_end_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.tau_start_end_parameter, 'generation')

        ## Timeparam parameters
        self.bdot_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/BDOT', 'SCALAR_BDOT', self.timeparam_device)
        self.bp_length_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/BP_LENGTH', 'SCALAR_TIME_PARTITION', self.timeparam_device, is_trimable=False)
        self.incorpip_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/INCORPIP', 'INCORPIP', self.timeparam_device, is_trimable=False)
        self.tgrid_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/TGRID', 'SCALAR_TGRID', self.timeparam_device)
        self.tround_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/TROUND', 'SCALAR_TROUND', self.timeparam_device)
        self.t_bp_length_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_BP_LENGTH', 'SCALAR_T_BP_LENGTH', self.timeparam_device)
        self.t_wait_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_WAIT', 'SCALAR_T_WAIT', self.timeparam_device)

        self.lh_builder.lh.add_parameter_to_system(self.bdot_parameter, 'TIMEPARAM')
        self.lh_builder.lh.add_parameter_to_system(self.bdot_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.bdot_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.bp_length_parameter, 'TIMEPARAM')
        self.lh_builder.lh.add_parameter_to_system(self.incorpip_parameter, 'TIMEPARAM')
        
        self.lh_builder.lh.add_parameter_to_system(self.tgrid_parameter, 'TIMEPARAM')
        self.lh_builder.lh.add_parameter_to_system(self.tgrid_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.tgrid_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.tround_parameter, 'TIMEPARAM')
        self.lh_builder.lh.add_parameter_to_system(self.tround_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.tround_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.t_bp_length_parameter, 'TIMEPARAM')
        self.lh_builder.lh.add_parameter_to_system(self.t_bp_length_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.t_bp_length_parameter, 'generation')
        
        self.lh_builder.lh.add_parameter_to_system(self.t_wait_parameter, 'TIMEPARAM')
        self.lh_builder.lh.add_parameter_to_system(self.t_wait_parameter, '-TOPLEVEL')
        self.lh_builder.lh.add_parameter_to_system(self.t_wait_parameter, 'generation')

        ## Kicker parameters
        # KICKER KNOB parameters
        if self.devices.inj_kicker :
            self.inj_kicker_knob_parameter = self.lh_builder.lh.define_physics_parameter(self.inj_kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', self.inj_kicker_device)
            self.lh_builder.lh.add_parameter_to_system(self.inj_kicker_knob_parameter, 'KICKER')
        if self.devices.ext_kicker : 
            self.ext_kicker_knob_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', self.ext_kicker_device)
            self.kicker_mode_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/MODE', 'SCALAR_KICKER_MODE', self.ext_kicker_device)
            self.nbunch1_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/NBUNCH1', 'SCALAR_NBUNCH1', self.ext_kicker_device)
            self.start_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/START', 'SCALAR_KICKER_START', self.ext_kicker_device)
            self.thigh1_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/THIGH1', 'SCALAR_KICKER_THIGH1', self.ext_kicker_device)
            self.thigh2_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/THIGH2', 'SCALAR_KICKER_THIGH2', self.ext_kicker_device)
            self.toffset1_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/TOFFSET1', 'SCALAR_KICKER_TOFFSET1', self.ext_kicker_device)
            self.toffset2_parameter = self.lh_builder.lh.define_physics_parameter(self.ext_kicker_device + '/TOFFSET2', 'SCALAR_KICKER_TOFFSET2', self.ext_kicker_device)

            self.lh_builder.lh.add_parameter_to_system(self.ext_kicker_knob_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.ext_kicker_knob_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.ext_kicker_knob_parameter, 'generation')

            self.lh_builder.lh.add_parameter_to_system(self.kicker_mode_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.kicker_mode_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.kicker_mode_parameter, 'generation')
        
            self.lh_builder.lh.add_parameter_to_system(self.nbunch1_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.nbunch1_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.nbunch1_parameter, 'generation')
        
            self.lh_builder.lh.add_parameter_to_system(self.start_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.start_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.start_parameter, 'generation')
        
            self.lh_builder.lh.add_parameter_to_system(self.thigh1_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.thigh2_parameter, 'KICKER')
        
            self.lh_builder.lh.add_parameter_to_system(self.toffset1_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.toffset1_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.toffset1_parameter, 'generation')
        
            self.lh_builder.lh.add_parameter_to_system(self.toffset2_parameter, 'KICKER')

        if self.devices.q_kicker :
            self.qh_kick_parameter = self.lh_builder.lh.define_physics_parameter(self.qh_kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', self.qh_kicker_device)
            self.lh_builder.lh.add_parameter_to_system(self.qh_kick_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.qh_kick_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.qh_kick_parameter, 'generation')
            self.qv_kick_parameter = self.lh_builder.lh.define_physics_parameter(self.qv_kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', self.qv_kicker_device)
            self.lh_builder.lh.add_parameter_to_system(self.qv_kick_parameter, 'KICKER')
            self.lh_builder.lh.add_parameter_to_system(self.qv_kick_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(self.qv_kick_parameter, 'generation')

        ## Cavities
        for device in self.devices.cavities:
            y_prec_FRF = self.y_prec_parser.findYPrec(device, 'FRF', 1.0e-6)
            y_prec_URF = self.y_prec_parser.findYPrec(device, 'URF', 1.0e-3)
            urf_parameter = self.lh_builder.lh.define_physics_parameter(device + '/URF', 'URF', device, y_prec=y_prec_URF)
            frf_parameter = self.lh_builder.lh.define_physics_parameter(device + '/FRF', 'FRF', device, y_prec=y_prec_FRF)
            prf_parameter = self.lh_builder.lh.define_physics_parameter(device + '/PRF', 'PRF', device, y_prec=1)
            
            frf_polynomial_parameter = self.lh_builder.lh.define_physics_parameter(device + '/FRF_POLYNOMIAL', 'FRF_POLYNOMIAL', device, y_prec=y_prec_FRF)
            urf_polynomial_parameter = self.lh_builder.lh.define_physics_parameter(device + '/URF_POLYNOMIAL', 'URF_POLYNOMIAL', device, y_prec=y_prec_URF)
            
            urf_time_partition_parameter = self.lh_builder.lh.define_physics_parameter(device + '/URF_TIME_PARTITION', 'SCALAR_RF_TIME_PARTITION', device)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(urf_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(frf_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(prf_parameter, system)
            
            self.lh_builder.lh.add_parameter_to_system(frf_polynomial_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(urf_polynomial_parameter, system)
            
            self.lh_builder.lh.add_parameter_to_system(urf_time_partition_parameter, system)

        ## Magnet groups according to multipole
        all_dipoles = self.devices.main_dipoles + self.devices.horizontal_correctors + self.devices.vertical_correctors
        all_quadrupoles = self.devices.main_quadrupoles + self.devices.extraction_quadrupoles + self.devices.correction_quadrupoles
        all_sextupoles = self.devices.main_sextupoles + self.devices.correction_sextupoles + self.devices.chromaticity_sextupoles + self.devices.resonance_sextupoles
        all_octupoles = self.devices.correction_octupoles
        
        all_corrections = self.devices.correction_quadrupoles + self.devices.correction_sextupoles + self.devices.correction_octupoles

        all_magnets = all_dipoles + all_quadrupoles + all_sextupoles + all_octupoles
        self.main_magnets = self.devices.main_dipoles + self.devices.main_quadrupoles

        ext_kicker = self.devices.ext_kicker

        for device in self.devices.main_dipoles:
            y_prec_KL = self.y_prec_parser.findYPrec(device, 'KL', 5.0e-7)
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
            y_prec_BL = self.y_prec_parser.findYPrec(device, 'BL', 5.0e-7)
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B0L', device, y_prec=y_prec_BL)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)
                        
        for device in all_correctors:
            y_prec_KL = self.y_prec_parser.findYPrec(device, 'KL', 1.0e-5)
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
            y_prec_BL = self.y_prec_parser.findYPrec(device, 'BL', 1.0e-6)
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B0L', device, y_prec=y_prec_BL)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)

        for device in all_quadrupoles:
            kl_parameter
            bl_parameter
            
            if device in self.devices.extraction_quadrupoles:
                kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K1L', device)
                bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B1L', device)
            else:
                y_prec_KL = self.y_prec_parser.findYPrec(device, 'KL', 5.0e-7)
                y_prec_BL = self.y_prec_parser.findYPrec(device, 'BL', 5.0e-7)
                
                if device in self.devices.correction_quadrupoles:
                    y_prec_KL = self.y_prec_parser.findYPrec(device, 'KL', 1.0e-4)
                    y_prec_BL = self.y_prec_parser.findYPrec(device, 'BL', 1.0e-4)
                    
                kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K1L', device, y_prec=y_prec_KL)
                bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B1L', device, y_prec=y_prec_BL)
                
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)

        for device in self.devices.main_dipoles:
            dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'DK0L_RADIAL', device)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)
            

        for device in self.devices.main_quadrupoles:
            dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'DK1L', device)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)

        for device in all_sextupoles:
            #self.lh_builder.lh.define_physics_parameter(device + '/KLDELTA', 'DELTA_K2L', device) ## KLDELTA soll nicht fuer S02KM5SS und S08KM5SS angelegt werden, hier muss noch eine extra gruppe / hierarchie erstellt werden
            y_prec_KL = self.y_prec_parser.findYPrec(device, 'KL', 1.0e-5)
            y_prec_BL = self.y_prec_parser.findYPrec(device, 'BL', 1.0e-6)

            if device in self.devices.correction_sextupoles:
                y_prec_KL = self.y_prec_parser.findYPrec(device, 'KL', 1.0e-4)
                y_prec_BL = self.y_prec_parser.findYPrec(device, 'BL', 1.0e-6)
            
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K2L', device, y_prec=y_prec_KL)
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B2L', device, y_prec=y_prec_BL)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)

        for device in (self.devices.chromaticity_sextupoles + self.devices.resonance_sextupoles):
            kldelta_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KLDELTA', 'DELTA_K2L', device) ## KLDELTA soll nicht fuer S02KM5SS und S08KM5SS

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kldelta_parameter, system)

        for device in (self.devices.chromaticity_sextupoles):
            dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'DK2L', device)

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)

        for device in all_octupoles:
            y_prec_KL = self.y_prec_parser.findYPrec(device, 'KL', 1.0e-5)
            y_prec_BL = self.y_prec_parser.findYPrec(device, 'BL', 1.0e-6)

            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K3L', device, y_prec=y_prec_KL)
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B3L', device, y_prec=y_prec_BL)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)

        for device in (self.devices.inj_kicker + self.devices.ext_kicker + self.devices.q_kicker):
            dkl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/DKL', 'SCALAR_DK0L', device)
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'SCALAR_B0L', device)
            ukick_parameter = self.lh_builder.lh.define_physics_parameter(device + '/UKICK', 'SCALAR_UKICK', device)
            #if device == 'S05MK2E': # Skip these parameters for the seconds kicker in SIS18
                #continue
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMDELRF', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMDELTG', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMFTRF', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'TIMFTTG', 'time')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTRFS', 'voltages')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTRIS', 'voltages')
            #self.lh_builder.lh.define_hardware_parameter(device, 'VOLTTGS', 'voltages')
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(dkl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(ukick_parameter, system)

#        for device in all_magnets:
#            self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device)
#            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        for device in self.devices.extraction_quadrupoles:
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)

        for device in self.main_magnets:
            y_prec_I = self.y_prec_parser.findYPrec(device, 'I', 1.0e-6, False)
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device, y_prec=y_prec_I)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            
            i_polynomial_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I_POLYNOMIAL', 'I_POLYNOMIAL', device, y_prec=y_prec_I)

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)
            
            self.lh_builder.lh.add_parameter_to_system(i_polynomial_parameter, system)
            

        for device in all_sextupoles:
            y_prec_I = self.y_prec_parser.findYPrec(device, 'I', 1.0e-6)
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device, y_prec=y_prec_I)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)

        for device in all_corrections + all_correctors:
            y_prec_I = self.y_prec_parser.findYPrec(device, 'I', 1.0e-7)
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device, y_prec=y_prec_I)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)

        if self.eddycurrents:
            for device in self.main_magnets:
                y_prec_IDOT = self.y_prec_parser.findYPrec(device, 'IDOT', 2.4e-4)
                y_prec_U = self.y_prec_parser.findYPrec(device, 'U', 5.0e-4)
                idot_parameter = self.lh_builder.lh.define_physics_parameter(device + '/IDOT', 'IDOT', device, y_prec=y_prec_IDOT)
                ueddy_parameter = self.lh_builder.lh.define_physics_parameter(device + '/UEDDY', 'UEDDY', device, y_prec=y_prec_U)
                u_parameter = self.lh_builder.lh.define_physics_parameter(device + '/U', 'U', device, y_prec=y_prec_U)
            
                system = self.devices.devicesystemmap.get(device)
                print (device , system)
            
                self.lh_builder.lh.add_parameter_to_system(idot_parameter, system)
                self.lh_builder.lh.add_parameter_to_system(ueddy_parameter, system)
                self.lh_builder.lh.add_parameter_to_system(u_parameter, system)

        ### Creation of relations

        ## Beam Parameters
        self.lh_builder.create_child_node(self.a_parameter, [ self.isotope_parameter, self.element_parameter ])
        self.lh_builder.create_child_node(self.alphac_parameter, self.opticsip_parameter )
        self.lh_builder.create_child_node(self.alphadr_parameter, self.opticsip_parameter )
        self.lh_builder.create_child_node(self.aoq_parameter, [ self.a_parameter, self.q_parameter ])
        self.lh_builder.create_child_node(self.brho_parameter, self.bp_length_parameter )
        self.lh_builder.create_child_node(self.brhodot_parameter, self.bp_length_parameter )
        self.lh_builder.create_child_node(self.brho_start_end_parameter, [ self.e_start_end_parameter, self.aoq_parameter ])
        self.lh_builder.create_child_node(self.bunchfactor_parameter, self.phis_parameter )
        self.lh_builder.create_child_node(self.bunchpattern_parameter, [ self.inj_bunchpattern_parameter, self.rf_manipulation_parameter ])

        self.lh_builder.create_child_node(self.ch_start_end_parameter, self.ch_end_parameter )
        self.lh_builder.create_child_node(self.cv_start_end_parameter, self.cv_end_parameter )

        self.lh_builder.create_child_node(self.ch_parameter, [self.ch_start_end_parameter, self.ch_theo_parameter, self.tgrid_parameter, self.bp_length_parameter] )
        self.lh_builder.create_child_node(self.cv_parameter, [self.cv_start_end_parameter, self.cv_theo_parameter, self.tgrid_parameter, self.bp_length_parameter] )
        self.lh_builder.create_child_node(self.ch_theo_parameter, self.opticsip_parameter )
        self.lh_builder.create_child_node(self.cv_theo_parameter, self.opticsip_parameter )
        self.lh_builder.create_child_node(self.dch_parameter, [self.ch_parameter, self.ch_theo_parameter] )
        self.lh_builder.create_child_node(self.dcv_parameter, [self.cv_parameter, self.cv_theo_parameter] )

        self.lh_builder.create_child_node(self.deltar_parameter, self.bp_length_parameter )

        self.lh_builder.create_child_node(self.dpbl_parameter, self.bp_length_parameter )
        self.lh_builder.create_child_node(self.dpdr_parameter, [self.deltar_parameter, self.alphac_parameter] )
        self.lh_builder.create_child_node(self.dpfrev_parameter, self.bp_length_parameter )
        
        self.lh_builder.create_child_node(self.e_start_end_parameter, self.e_parameter )
        
        self.lh_builder.create_child_node(self.emil_parameter, [ self.inj_emil_parameter, self.rf_manipulation_parameter, self.bunchpattern_parameter ])

        self.lh_builder.create_child_node(self.erho_parameter, [ self.brho_parameter, self.aoq_parameter ])
        self.lh_builder.create_child_node(self.eta_parameter, [ self.gamma_parameter, self.alphac_parameter ])
        self.lh_builder.create_child_node(self.frev_parameter, [ self.gamma_parameter, self.deltar_parameter, self.alphac_parameter, self.alphadr_parameter, self.eta_parameter, self.dpfrev_parameter ], parent_parameter_order = {self.gamma_parameter : 1} )
        self.lh_builder.create_child_node(self.gamma_parameter, [ self.brho_parameter, self.aoq_parameter ])
        self.lh_builder.create_child_node(self.gamma_t_parameter, self.alphac_parameter)
        self.lh_builder.create_child_node(self.geofact_parameter, [ self.brho_start_end_parameter, self.brho_parameter, self.inj_emiv_parameter, self.inj_emih_parameter ])
        self.lh_builder.create_child_node(self.maxrh_parameter, [ self.inj_emih_parameter, self.brho_parameter, self.opticsip_parameter, self.brho_start_end_parameter ])
        self.lh_builder.create_child_node(self.maxrv_parameter, [ self.inj_emiv_parameter, self.brho_parameter, self.opticsip_parameter, self.brho_start_end_parameter ])
        self.lh_builder.create_child_node(self.nperbunch_parameter, [ self.nparticles_parameter, self.bunchpattern_parameter ])
        
        self.lh_builder.create_child_node(self.phis_parameter, [ self.bunchpattern_parameter, self.nparticles_parameter, self.bp_length_parameter, self.bucketfill_parameter, self.aoq_parameter, self.eta_parameter, self.brhodot_parameter, self.gamma_parameter, self.emil_parameter, self.dualh_parameter, self.geofact_parameter, self.e_start_end_parameter, self.q_parameter, self.tgrid_parameter, self.phase_offset_parameter, self.rf_manipulation_parameter ])
            
        self.lh_builder.create_child_node(self.qh_start_end_parameter, self.qh_end_parameter )
        self.lh_builder.create_child_node(self.qv_start_end_parameter, self.qv_end_parameter )
        self.lh_builder.create_child_node(self.qh_parameter, [self.qh_start_end_parameter, self.qh_theo_parameter, self.tgrid_parameter, self.bp_length_parameter] )
        self.lh_builder.create_child_node(self.qv_parameter, [self.qv_start_end_parameter, self.qv_theo_parameter, self.tgrid_parameter, self.bp_length_parameter] )
        self.lh_builder.create_child_node(self.qh_theo_parameter, self.opticsip_parameter )
        self.lh_builder.create_child_node(self.qv_theo_parameter, self.opticsip_parameter )
        self.lh_builder.create_child_node(self.dqh_parameter, [self.qh_parameter, self.qh_theo_parameter] )
        self.lh_builder.create_child_node(self.dqv_parameter, [self.qv_parameter, self.qv_theo_parameter] )
        self.lh_builder.create_child_node(self.tbunch_parameter, [ self.rf_manipulation_parameter, self.trev_parameter ])
        self.lh_builder.create_child_node(self.trev_parameter, self.frev_parameter )


        ## RF Parameters
        self.lh_builder.create_child_node(self.abkt_parameter, self.phis_parameter)
        self.lh_builder.create_child_node(self.dualhip_parameter, self.phis_parameter )
        self.lh_builder.create_child_node(self.prfring_parameter, self.phis_parameter )
        self.lh_builder.create_child_node(self.urfring_parameter, self.phis_parameter )
        self.lh_builder.create_child_node(self.urfsc_parameter, self.phis_parameter )
        
        self.lh_builder.create_child_node(self.rf_manipulation_parameter, [ self.rf_manipulation_raw_parameter, self.bucketfill_raw_parameter, self.dualh_raw_parameter, self.bp_length_parameter, self.h_parameter, self.frev_parameter, self.cavitypattern_parameter])
        self.lh_builder.create_child_node(self.bucketfill_parameter, self.rf_manipulation_parameter)
        self.lh_builder.create_child_node(self.dualh_parameter, self.rf_manipulation_parameter)
        self.lh_builder.create_child_node(self.cavity2harmonic_parameter, [self.urfring_parameter, self.rf_manipulation_parameter, self.rf_mode_2D_parameter, self.cavitypattern_parameter] )
        
        ## Optics Parameters
        self.lh_builder.create_child_node(self.opticsip_parameter, [ self.tau_start_end_parameter, self.incorpip_parameter ])

        #self.lh_builder.create_child_node(self.opticsip_parameter, [ sigma_parameter, tau_parameter, self.incorpip_parameter ])
        #self.lh_builder.create_child_node(sigma_parameter, [ self.brho_start_end_parameter, ext_sigma_parameter, self.bp_length_parameter, self.t_wait_parameter, self.tround_parameter, self.tgrid_parameter, tau_endpoint_parameter ])
        #self.lh_builder.create_child_node(tau_parameter, [ tau_nlp_parameter, self.tau_start_end_parameter, self.bp_length_parameter, self.t_wait_parameter, self.brho_start_end_parameter, self.tround_parameter, self.tgrid_parameter, tau_endpoint_parameter ])


        ## Timeparam Parameters
        self.lh_builder.create_child_node(self.bp_length_parameter, [ self.t_bp_length_parameter, self.t_wait_parameter, self.tau_start_end_parameter, self.tround_parameter, self.bdot_parameter, self.brho_start_end_parameter, self.tgrid_parameter ], parent_parameter_order={self.t_bp_length_parameter : 1})

        #self.lh_builder.create_child_node(self.bp_length_parameter, [ self.t_bp_length_parameter, self.t_wait_parameter, ext_sigma_parameter, self.tau_start_end_parameter, self.tround_parameter,  self.bdot_parameter, self.brho_start_end_parameter, self.tgrid_parameter ])
        self.lh_builder.create_child_node(self.incorpip_parameter, self.bp_length_parameter )

        ## Kicker Parameters
        if self.devices.ext_kicker :
            self.lh_builder.create_child_node(self.thigh1_parameter, [ self.nbunch1_parameter, self.tbunch_parameter, self.rf_manipulation_parameter ])
            self.lh_builder.create_child_node(self.thigh2_parameter, [ self.tbunch_parameter, self.rf_manipulation_parameter, self.nbunch1_parameter ])
            self.lh_builder.create_child_node(self.toffset2_parameter, [ self.toffset1_parameter, self.thigh1_parameter ])


        ## Magnets
        for device in all_magnets:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ self.brho_parameter, kl_parameter, self.incorpip_parameter], parent_parameter_order={self.brho_parameter : 1 , kl_parameter : 1})


        for device in all_dipoles:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

        for device in self.devices.main_dipoles:
            dkl_parameter = self.reader.find_unique_string(device + '/DK0?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(dkl_parameter, [ self.opticsip_parameter, self.deltar_parameter, self.alphadr_parameter, self.alphac_parameter, self.gamma_parameter, self.dpbl_parameter ])
            
            kl_parameter = self.reader.find_unique_string(device + '/K0?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, dkl_parameter ] )

        for device in self.devices.main_quadrupoles:
            dkl_parameter = self.reader.find_unique_string(device + '/DK1?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(dkl_parameter, [ self.dqh_parameter, self.dqv_parameter, self.opticsip_parameter ])
            
            kl_parameter = self.reader.find_unique_string(device + '/K1?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ dkl_parameter, self.opticsip_parameter ])


        for device in all_sextupoles:
            #kldelta_parameter = self.reader.find_unique_string(device + '/KLDELTA$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(kldelta_parameter, [ self.incorpip_parameter, self.kl_harm_parameter, self.kl_phase_parameter, self.kl_ampl_parameter, self.kl_offset_parameter ])

            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())

            if (device in self.devices.chromaticity_sextupoles):
                dkl_parameter = self.reader.find_unique_string(device + '/DK2?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(kl_parameter, [ dkl_parameter, self.opticsip_parameter ], parent_parameter_order = {self.opticsip_parameter : 1}) 
            else:
                self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter)
                #self.lh_builder.create_child_node(kl_parameter, [ self.ch_parameter, self.cv_parameter, self.opticsip_parameter, kldelta_parameter ]) 

            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

        for device in (self.devices.chromaticity_sextupoles + self.devices.resonance_sextupoles):
            kldelta_parameter = self.reader.find_unique_string(device + '/KLDELTA$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kldelta_parameter, [ self.incorpip_parameter, self.kl_harm_parameter, self.kl_phase_parameter, self.kl_ampl_parameter, self.kl_offset_parameter ])

            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())
            if device in (self.devices.chromaticity_sextupoles):   
                dkl_parameter = self.reader.find_unique_string(device + '/DK2?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(dkl_parameter, [ self.dch_parameter, self.dcv_parameter, self.opticsip_parameter ])
                self.lh_builder.create_child_node(kl_parameter, [ dkl_parameter, self.opticsip_parameter, kldelta_parameter ])
            else:
                self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, kldelta_parameter ], parent_parameter_order = {self.opticsip_parameter : 1}) 


        for device in (self.devices.correction_quadrupoles + self.devices.extraction_quadrupoles):
            kl_parameter = self.reader.find_unique_string(device + '/K2?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter )

            bl_parameter = self.reader.find_unique_string(device + '/B[1]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

        for device in self.main_magnets:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)
            
            i_polynomial_parameter = self.reader.find_unique_string(device + '/I_POLYNOMIAL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_polynomial_parameter, [i_parameter, self.bp_length_parameter])

            if self.eddycurrents:
                idot_parameter = self.reader.find_unique_string(device + '/IDOT$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(idot_parameter, i_parameter)

                ueddy_parameter = self.reader.find_unique_string(device + '/UEDDY$', self.lh_builder.lh.get_parameters())
                u_parameter = self.reader.find_unique_string(device + '/U$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(ueddy_parameter, idot_parameter )   
                self.lh_builder.create_child_node(u_parameter, [ ueddy_parameter, i_parameter, idot_parameter ])


        for device in all_correctors:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter )

        for device in self.devices.correction_sextupoles:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter)

            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

        for device in self.devices.resonance_sextupoles:
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())

        for device in self.devices.correction_octupoles:
            kl_parameter = self.reader.find_unique_string(device + '/K0?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, self.opticsip_parameter )

            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
            i_parameter = self.reader.find_unique_string(device + '/I$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(i_parameter, bl_parameter)
            
        ## Ext. Kicker
        for device in self.devices.ext_kicker:
            dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(dkl_parameter, [ self.ext_kicker_knob_parameter , self.opticsip_parameter ])

            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ dkl_parameter , self.opticsip_parameter ])

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , self.brho_parameter ])

            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(ukick_parameter, bl_parameter )

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            #self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'KICKER')

        ## Q_Kicker
        for device in self.devices.q_kicker:
            dkl_parameter = self.reader.find_unique_string(device + '/DKL$', self.lh_builder.lh.get_parameters())

            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())

            number = int(device[6:7])
            if (number == 1) :
                self.lh_builder.create_child_node(dkl_parameter, [ self.opticsip_parameter, self.qh_kick_parameter ])
                self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, dkl_parameter ])
            elif (number == 2) :
                self.lh_builder.create_child_node(dkl_parameter, [ self.opticsip_parameter, self.qv_kick_parameter ])
                self.lh_builder.create_child_node(kl_parameter, [ self.opticsip_parameter, dkl_parameter ])

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , self.brho_parameter ])

            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(ukick_parameter, bl_parameter )

            system = self.devices.devicesystemmap.get(device)
            print (device , system)


        ## Cavities
        for device in self.devices.cavities:
            urf_parameter = self.reader.find_unique_string(device + '/URF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_parameter, [ self.cavity2harmonic_parameter, self.incorpip_parameter, self.urfring_parameter, self.rf_manipulation_parameter ], parent_parameter_order={self.cavity2harmonic_parameter : 1 , self.urfring_parameter : 1 })

            frf_parameter = self.reader.find_unique_string(device + '/FRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(frf_parameter, [ self.cavity2harmonic_parameter, self.incorpip_parameter, self.frev_parameter ], parent_parameter_order={self.cavity2harmonic_parameter : 1 , self.frev_parameter : 1 })

            prf_parameter = self.reader.find_unique_string(device + '/PRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(prf_parameter, [ self.cavity2harmonic_parameter, self.incorpip_parameter, self.prfring_parameter ], parent_parameter_order={self.cavity2harmonic_parameter : 1 , self.prfring_parameter : 1 })

            frf_polynomial_parameter = self.reader.find_unique_string(device + '/FRF_POLYNOMIAL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(frf_polynomial_parameter, [ frf_parameter, self.bp_length_parameter, self.rf_manipulation_parameter ])
            
            urf_time_partition_parameter = self.reader.find_unique_string(device + '/URF_TIME_PARTITION$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_time_partition_parameter, urf_parameter)
 
            urf_polynomial_parameter = self.reader.find_unique_string(device + '/URF_POLYNOMIAL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_polynomial_parameter, [ urf_parameter, self.bp_length_parameter, urf_time_partition_parameter, self.rf_manipulation_parameter])
