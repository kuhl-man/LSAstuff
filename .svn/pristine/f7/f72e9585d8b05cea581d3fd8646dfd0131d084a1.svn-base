from init_lh_builder import INIT_LH_BUILDER

from cryring_linac_properties import CRYRING_LINAC_PROPERTIES

from Generator_CRYRING_YRLE import GENERATOR_CRYRING_YRLE

from Generator_CRYRING_YRME import GENERATOR_CRYRING_YRME

class GENERATOR_CRYRING_LINAC(INIT_LH_BUILDER, GENERATOR_CRYRING_YRLE, GENERATOR_CRYRING_YRME):
    
    def __init__(self):
        
        cryring_linac_properties = CRYRING_LINAC_PROPERTIES()
        INIT_LH_BUILDER.__init__(self, cryring_linac_properties)
        
    def __buildSpecial(self):
        # build special part of hierarchy for CRYRING

        ## Timing parameters
        self.timeparam_device = 'CRYRING_LINAC_TIMEPARAM'

        self.t_master_parameter    = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/TIMING_MASTER', 'SCALAR_TIMING_MASTER', self.timeparam_device, belongs_to_function_bproc=True)
        self.t_pulse_parameter     = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_PULSE',       'SCALAR_TIMING_BEAM_PULSE_LENGTH', self.timeparam_device, belongs_to_function_bproc=True)
	self.t_rf_pulse_parameter  = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_RF_PAUSE',    'SCALAR_TIMING_RF_PAUSE_PULSE_LENGTH', self.timeparam_device, belongs_to_function_bproc=True)
	self.t_bi_delay_parameter  = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_BI_DELAY',    'SCALAR_TIMING_BI_DELAY', self.timeparam_device, belongs_to_function_bproc=True)
	self.t_bi_window_parameter = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_BI_WINDOW',   'SCALAR_TIMING_BI_WINDOW', self.timeparam_device, belongs_to_function_bproc=True)
        self.t_sequence_parameter  = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_SEQUENCE_KEY', 'SCALAR_TIMING_SEQUENCE_KEY', self.timeparam_device, belongs_to_function_bproc=True)
        self.t_process_parameter   = self.lh_builder.lh.define_physics_parameter(self.timeparam_device + '/T_PROCESS_KEY', 'SCALAR_TIMING_PROCESS_KEY', self.timeparam_device, belongs_to_function_bproc=True)

        self.lh_builder.lh.add_parameter_to_system(self.t_master_parameter, 'TIMEPARAM')
        self.lh_builder.lh.add_parameter_to_system(self.t_pulse_parameter, 'TIMEPARAM')
	self.lh_builder.lh.add_parameter_to_system(self.t_rf_pulse_parameter, 'TIMEPARAM')

	self.lh_builder.lh.add_parameter_to_system(self.t_bi_delay_parameter, 'TIMEPARAM')
	self.lh_builder.lh.add_parameter_to_system(self.t_bi_delay_parameter, '-TOPLEVEL')
	self.lh_builder.lh.add_parameter_to_system(self.t_bi_delay_parameter, 'generation')

	self.lh_builder.lh.add_parameter_to_system(self.t_bi_window_parameter, 'TIMEPARAM')
	self.lh_builder.lh.add_parameter_to_system(self.t_bi_window_parameter, '-TOPLEVEL')
	self.lh_builder.lh.add_parameter_to_system(self.t_bi_window_parameter, 'generation')

	self.lh_builder.lh.add_parameter_to_system(self.t_sequence_parameter, 'TIMEPARAM')
	self.lh_builder.lh.add_parameter_to_system(self.t_sequence_parameter, '-TOPLEVEL')
	self.lh_builder.lh.add_parameter_to_system(self.t_sequence_parameter, 'generation')

	self.lh_builder.lh.add_parameter_to_system(self.t_process_parameter, 'TIMEPARAM')
	self.lh_builder.lh.add_parameter_to_system(self.t_process_parameter, '-TOPLEVEL')
	self.lh_builder.lh.add_parameter_to_system(self.t_process_parameter, 'generation')

        ## Timeparam Parameters
        self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_pulse_parameter ])
	self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_rf_pulse_parameter ])
	self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_bi_delay_parameter ])
	self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_bi_window_parameter ])
        self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_sequence_parameter ])
        self.lh_builder.create_child_node(self.t_master_parameter, [ self.t_process_parameter ])

        self.lh_builder.create_child_node(self.t_pulse_parameter, [ 'YRT1LC1_V/TCHOP' ] )
	self.lh_builder.create_child_node(self.t_rf_pulse_parameter, [ 'YRT1BR1/T_PAUSE_PULSE_LENGTH' ] )


    def build(self):
        
        GENERATOR_CRYRING_YRME.__init__(self)
        GENERATOR_CRYRING_YRME.build(self)
        
        GENERATOR_CRYRING_YRLE.__init__(self)
        GENERATOR_CRYRING_YRLE.build(self)

        # build special part of hierarchy
        self.__buildSpecial()
                
    def generate(self):
        self.lh_builder.export()

      
if __name__ == '__main__':

  h = GENERATOR_CRYRING_LINAC()
  
  h.build()
  h.generate()
