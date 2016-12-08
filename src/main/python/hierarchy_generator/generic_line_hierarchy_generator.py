#!/bin/env python2.6

from lh_builder import LHBuilder

from lh_builder_utils import LHBuilderUtils

from devicedata_xml_parser import XMLParser

class GenericLineHierarchy:

    def __init__(self, devices):
        self.devices = devices
        self.reader = LHBuilderUtils()
        self.y_prec_parser = XMLParser(self.devices.accelerator_zone , self.devices.rigidity)

    def generate_linkrules(self):
        
        # print ('LinkRules:')
        # print ('device is under study')
        for device in self.devices.alldevices:
            # print ('device is in alldevices')
            
            ##print (self.devices._devicelinkrulemap)
            if device in self.devices.devicelinkrulemap:
                linkrule = self.devices.devicelinkrulemap.get(device)
                
                self.lh_builder.lh.add_linkrule_for_device(device,linkrule)
                # print (device , linkrule)
                # print ('device ', device, 'is in devicelinkrulemap')

            else:
                print ('device ', device, ' not in devicelinkrulemap')


    def build(self):

        ## Standard beam and logical devices
        self.beam_device = self.devices.accelerator_zone + '_BEAM'
        self.timeparam_device = self.devices.accelerator_zone + '_TIMEPARAM'
        # self.rf_device = self.devices.accelerator_zone + '_RF'

        self.lh_builder.lh.define_device(self.beam_device,      'BEAM',      self.devices.accelerator_zone, description= self.beam_device + ' Transfer Line Beam')
        self.lh_builder.lh.define_device(self.timeparam_device, 'TIMEPARAM', self.devices.accelerator_zone, description= self.timeparam_device + ' Transfer Line Beam')
        # self.lh_builder.lh.define_device(self.rf_device,        'RF',      self.devices.accelerator_zone, description= self.beam_device + ' Transfer Line Beam')  



        ## Beam parameters
        self.a_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/A', 'SCALAR_A', self.beam_device, belongs_to_function_bproc=True)
        self.aoq_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/AOQ', 'SCALAR_AOQ', self.beam_device, is_trimable=False, belongs_to_function_bproc=True)
        self.brho_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/BRHO', 'BRHO', self.beam_device, is_trimable=True)
        self.chopped_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/CHOPPED_BEAM', 'SCALAR_ACTIVE', self.beam_device) # boolean
        self.e_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/E', 'SCALAR_E', self.beam_device, y_prec=8)
        self.element_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ELEMENT', 'SCALAR_ELEMENT', self.beam_device, belongs_to_function_bproc=True)
        self.erho_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ERHO', 'ERHO', self.beam_device, is_trimable=True)
        self.isotope_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ISOTOPE', 'SCALAR_ISOTOPE', self.beam_device, belongs_to_function_bproc=True)
        self.q_parameter =  self.lh_builder.lh.define_physics_parameter(self.beam_device + '/Q', 'SCALAR_Q', self.beam_device, belongs_to_function_bproc=True)

        self.lh_builder.lh.add_parameter_to_system(self.a_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.aoq_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.brho_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.chopped_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.e_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.element_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.erho_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.isotope_parameter, 'BEAM')
        self.lh_builder.lh.add_parameter_to_system(self.q_parameter, 'BEAM')

	if not self.yrle_bp:
          self.lh_builder.lh.add_parameter_to_system(self.e_parameter, '-TOPLEVEL')
          self.lh_builder.lh.add_parameter_to_system(self.e_parameter, 'generation')

	if self.yrle_bp:
          self.epercharge_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/E_PER_CHARGE', 'SCALAR_E_PER_CHARGE', self.beam_device)
          self.source_hv_parameter = self.lh_builder.lh.define_physics_parameter(self.beam_device + '/ION_SOURCE_HIGH_VOLTAGE', 'SCALAR_U', self.beam_device, y_prec=8)

          self.lh_builder.lh.add_parameter_to_system(self.epercharge_parameter, 'BEAM')
          self.lh_builder.lh.add_parameter_to_system(self.source_hv_parameter, 'BEAM')
          self.lh_builder.lh.add_parameter_to_system(self.source_hv_parameter, '-TOPLEVEL')
          self.lh_builder.lh.add_parameter_to_system(self.source_hv_parameter, 'generation')

	if not (self.yrme_bp):
          self.lh_builder.lh.add_parameter_to_system(self.element_parameter, '-TOPLEVEL')
          self.lh_builder.lh.add_parameter_to_system(self.element_parameter, 'generation')
                
          self.lh_builder.lh.add_parameter_to_system(self.isotope_parameter, '-TOPLEVEL')
          self.lh_builder.lh.add_parameter_to_system(self.isotope_parameter, 'generation')
        
          self.lh_builder.lh.add_parameter_to_system(self.q_parameter, '-TOPLEVEL')
          self.lh_builder.lh.add_parameter_to_system(self.q_parameter, 'generation')
        
	  self.lh_builder.lh.add_parameter_to_system(self.chopped_parameter, '-TOPLEVEL')
	  self.lh_builder.lh.add_parameter_to_system(self.chopped_parameter, 'generation')



        ## Timing parameters
        if self.standalone_acczone:
	  self.t_master_parameter    = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/TIMING_MASTER', 'SCALAR_TIMING_MASTER', self.timeparam_device, belongs_to_function_bproc=True)
	  self.t_sequence_parameter  = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_SEQUENCE_KEY','SCALAR_TIMING_SEQUENCE_KEY', self.timeparam_device, belongs_to_function_bproc=True)
	  self.t_process_parameter   = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_PROCESS_KEY', 'SCALAR_TIMING_PROCESS_KEY', self.timeparam_device, belongs_to_function_bproc=True)
	  self.t_pulse_parameter     = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_PULSE',       'SCALAR_TIMING_BEAM_PULSE_LENGTH', self.timeparam_device, belongs_to_function_bproc=True)

	  # self.lh_builder.lh.add_parameter_to_system(self.t_pulse_parameter, '-TOPLEVEL')
	  # self.lh_builder.lh.add_parameter_to_system(self.t_pulse_parameter, 'generation')

	  self.lh_builder.lh.add_parameter_to_system(self.t_master_parameter, 'TIMEPARAM')
	  self.lh_builder.lh.add_parameter_to_system(self.t_pulse_parameter, 'TIMEPARAM')

	  self.lh_builder.lh.add_parameter_to_system(self.t_sequence_parameter, 'TIMEPARAM')
	  self.lh_builder.lh.add_parameter_to_system(self.t_sequence_parameter, '-TOPLEVEL')
	  self.lh_builder.lh.add_parameter_to_system(self.t_sequence_parameter, 'generation')

	  self.lh_builder.lh.add_parameter_to_system(self.t_process_parameter, 'TIMEPARAM')
	  self.lh_builder.lh.add_parameter_to_system(self.t_process_parameter, '-TOPLEVEL')
	  self.lh_builder.lh.add_parameter_to_system(self.t_process_parameter, 'generation')

	  if self.yrle_bp:
	        self.t_bi_delay_parameter  = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_BI_DELAY',    'SCALAR_TIMING_BI_DELAY', self.timeparam_device, belongs_to_function_bproc=True, y_prec=8)
	        self.t_bi_window_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_BI_WINDOW',   'SCALAR_TIMING_BI_WINDOW', self.timeparam_device, belongs_to_function_bproc=True, y_prec=8)

	        self.lh_builder.lh.add_parameter_to_system(self.t_bi_delay_parameter, 'TIMEPARAM')
	        self.lh_builder.lh.add_parameter_to_system(self.t_bi_delay_parameter, '-TOPLEVEL')
	        self.lh_builder.lh.add_parameter_to_system(self.t_bi_delay_parameter, 'generation')

	        self.lh_builder.lh.add_parameter_to_system(self.t_bi_window_parameter, 'TIMEPARAM')
	        self.lh_builder.lh.add_parameter_to_system(self.t_bi_window_parameter, '-TOPLEVEL')
	        self.lh_builder.lh.add_parameter_to_system(self.t_bi_window_parameter, 'generation')

	  if self.yrme_bp:
	        self.t_rf_pulse_parameter  = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_RF_PAUSE','SCALAR_TIMING_RF_PAUSE_PULSE_LENGTH', self.timeparam_device, belongs_to_function_bproc=True, y_prec=8)
	        self.lh_builder.lh.add_parameter_to_system(self.t_rf_pulse_parameter, 'TIMEPARAM')



        ## Cavities
        for device in self.devices.cavities:
            urf_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/URF', 'SCALAR_URF', 		device, y_prec=8)
            prf_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/PHASE_OFFSET', 'SCALAR_PHASE_OFFSET',device, y_prec=1)
            act_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/ACT_ON_BEAM', 'SCALAR_ACTIVE',       device, y_prec=1)
            tpause_parameter = self.lh_builder.lh.define_physics_parameter(device + '/T_PAUSE_PULSE_LENGTH', 'SCALAR_THIGH', device, y_prec=8)
            upause_parameter = self.lh_builder.lh.define_physics_parameter(device + '/U_PAUSE_PULSE_AMPL','U', 		device, y_prec=8)
            utohardware_parameter = self.lh_builder.lh.define_physics_parameter(device + '/U_TO_HARDWARE','SCALAR_U', device, y_prec=8)

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(urf_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(utohardware_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(prf_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(prf_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(prf_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(act_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(act_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(act_parameter, 'generation')

            self.lh_builder.lh.add_parameter_to_system(tpause_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(tpause_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(tpause_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(upause_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(upause_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(upause_parameter, 'generation')



        ## Magnet groups according to multipole
        for device in self.devices.main_dipoles:

            y_prec_KL = 6
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
            y_prec_BL = 6
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B0L', device, y_prec=y_prec_BL)
            y_prec_I  = 6
            i_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/I',  'I',   device, y_prec=y_prec_I)
                        
            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(i_parameter,  system)


        for device in self.devices.horizontal_correctors + self.devices.vertical_correctors:

            y_prec_KL = 6
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
            y_prec_BL = 6
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B0L', device, y_prec=y_prec_BL)
            y_prec_I  = 6
            i_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/I',  'I',   device, y_prec=y_prec_I)
            
            system = self.devices.devicesystemmap.get(device)
            print (device , system)

            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)            
            self.lh_builder.lh.add_parameter_to_system(i_parameter,  system)


        for device in self.devices.main_quadrupoles:
                    
            y_prec_KL = 6
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K1L',      device, y_prec=y_prec_KL)
            y_prec_BL = 6
            bl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BL', 'B1L',      device, y_prec=y_prec_BL)
            y_prec_I  = 6
            i_parameter  = self.lh_builder.lh.define_physics_parameter(device + '/I',  'I', 	   device, y_prec=y_prec_I)

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(bl_parameter, system)           
            self.lh_builder.lh.add_parameter_to_system(i_parameter,  system)


        for device in self.devices.septa:

            y_prec_KL = 6
            kl_parameter = self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device, y_prec=y_prec_KL)
            usep_parameter = self.lh_builder.lh.define_physics_parameter(device + '/USEP', 'USEP', device, y_prec=y_prec_KL)

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(kl_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(usep_parameter, system)



        ## Beam diagnostics
#        for device in self.devices.cavities:
        for device in self.devices.faraday_cups:

            q_parameter		= self.lh_builder.lh.define_physics_parameter(device + '/Q', 'SCALAR_Q', device) # integer
            t_parameter		= self.lh_builder.lh.define_physics_parameter(device + '/TIME_OF_FLIGHT', 'SCALAR_TIME_OF_FLIGHT', device) # double
            chopped_parameter	= self.lh_builder.lh.define_physics_parameter(device + '/CHOPPED_BEAM', 'SCALAR_ACTIVE', device, y_prec=1) # boolean
            semiauto_parameter	= self.lh_builder.lh.define_physics_parameter(device + '/SEMI_AUTOMATIC_GAIN_RANGE', 'SCALAR_ACTIVE', device, y_prec=1) # boolean
            gain_parameter	= self.lh_builder.lh.define_physics_parameter(device + '/GAIN', 'SCALAR_TAU_NLP', device, y_prec=3) # double

            system = self.devices.devicesystemmap.get(device)
            print (device , system)
            
            self.lh_builder.lh.add_parameter_to_system(q_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(t_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(chopped_parameter, system)

            self.lh_builder.lh.add_parameter_to_system(semiauto_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(semiauto_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(semiauto_parameter, 'generation')

            self.lh_builder.lh.add_parameter_to_system(gain_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(gain_parameter, '-TOPLEVEL')
            self.lh_builder.lh.add_parameter_to_system(gain_parameter, 'generation')
                        


        ### Creation of relations

        ## Beam Parameters
        self.lh_builder.create_child_node(self.a_parameter, [ self.isotope_parameter, self.element_parameter ])
        self.lh_builder.create_child_node(self.aoq_parameter, [ self.a_parameter, self.q_parameter ])
        self.lh_builder.create_child_node(self.brho_parameter, [ self.e_parameter, self.aoq_parameter ])
        self.lh_builder.create_child_node(self.erho_parameter, [ self.brho_parameter, self.aoq_parameter ])
	if self.yrle_bp:
          self.lh_builder.create_child_node(self.epercharge_parameter, [ self.source_hv_parameter ])
          self.lh_builder.create_child_node(self.e_parameter, [ self.epercharge_parameter, self.isotope_parameter, self.q_parameter ])


        ## Timeparam Parameters
        if self.standalone_acczone:
	  self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_pulse_parameter ])
	  self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_sequence_parameter ])
	  self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_process_parameter ])

	  if self.yrme_bp:
	        self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_rf_pulse_parameter ])

	  if self.yrle_bp:
	        self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_bi_delay_parameter ])
	        self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_bi_window_parameter ])


        ## Magnets
        for device in self.devices.main_dipoles + self.devices.horizontal_correctors + self.devices.vertical_correctors + self.devices.main_quadrupoles:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-1]?L$', self.lh_builder.lh.get_parameters())
            bl_parameter = self.reader.find_unique_string(device + '/B[0-1]?L$', self.lh_builder.lh.get_parameters())
            i_parameter  = self.reader.find_unique_string(device + '/I$',        self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ self.brho_parameter, kl_parameter ])
            self.lh_builder.create_child_node(i_parameter, bl_parameter)

        for device in self.devices.septa:
            kl_parameter = self.reader.find_unique_string(device + '/KL', self.lh_builder.lh.get_parameters())
            usep_parameter = self.reader.find_unique_string(device + '/USEP', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(usep_parameter, [ self.erho_parameter, kl_parameter ])


        ## Cavities
        for device in self.devices.cavities:
            urf_parameter = self.reader.find_unique_string(device + '/URF$', self.lh_builder.lh.get_parameters()) 
            self.lh_builder.create_child_node(urf_parameter, [self.q_parameter, self.isotope_parameter ])
            prf_parameter = self.reader.find_unique_string(device + '/PHASE_OFFSET$', self.lh_builder.lh.get_parameters())
            act_parameter = self.reader.find_unique_string(device + '/ACT_ON_BEAM$', self.lh_builder.lh.get_parameters())
            tpause_parameter = self.reader.find_unique_string(device + '/T_PAUSE_PULSE_LENGTH$', self.lh_builder.lh.get_parameters()) 
            upause_parameter = self.reader.find_unique_string(device + '/U_PAUSE_PULSE_AMPL$', self.lh_builder.lh.get_parameters()) 
            utohardware_parameter = self.reader.find_unique_string(device + '/U_TO_HARDWARE$', self.lh_builder.lh.get_parameters()) 
            self.lh_builder.create_child_node(utohardware_parameter, [ act_parameter, urf_parameter, upause_parameter ])


        ## Beam diagnostics
#        for device in self.devices.cavities:
        for device in self.devices.faraday_cups:
            q_parameter = self.reader.find_unique_string(device + '/Q$', self.lh_builder.lh.get_parameters()) 
            self.lh_builder.create_child_node(q_parameter, [self.q_parameter ])
            t_parameter = self.reader.find_unique_string(device + '/TIME_OF_FLIGHT$', self.lh_builder.lh.get_parameters()) 
            self.lh_builder.create_child_node(t_parameter, [self.e_parameter, self.a_parameter])
            chopped_parameter = self.reader.find_unique_string(device + '/CHOPPED_BEAM$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(chopped_parameter, [self.chopped_parameter ])
            semiauto_parameter = self.reader.find_unique_string(device + '/SEMI_AUTOMATIC_GAIN_RANGE$', self.lh_builder.lh.get_parameters())
            gain_parameter = self.reader.find_unique_string(device + '/GAIN$', self.lh_builder.lh.get_parameters())

