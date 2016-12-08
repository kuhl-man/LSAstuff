#!/bin/env python2.6

from lh_builder_utils import LHBuilderUtils


class SpecialESRParameters:

    def __init__(self, lh_builder, csv_filename):
        self.lh_builder = lh_builder
        self.reader = LHBuilderUtils()
        self.all_devices = self.reader._read_devices(csv_filename)

    def setmaindipole(self, main_dipoles):
        self.main_dipoles = main_dipoles

    def sethorizontal_correction_coils(self, horizontal_correction_coils):
        self.horizontal_correction_coils = horizontal_correction_coils

    def setesr_cavities_ampl(self, esr_cavities_ampl):
        self.esr_cavities_ampl = esr_cavities_ampl

    def setesr_cavities_freq(self, esr_cavities_freq):
        self.esr_cavities_freq = esr_cavities_freq

    def setpolefacewindings(self, polefacewindings):
        self.polefacewindings = polefacewindings

    def build(self, particle_transfer):

        kicker_device = self.reader.find_unique_string(particle_transfer.replace('_RING','KICKER'), self.all_devices)

        for device in self.horizontal_correction_coils:
            self.lh_builder.lh.define_physics_parameter(device + '/KL', 'K0L', device)
            self.lh_builder.lh.define_physics_parameter(device + '/BLCORR', 'CORR_B0L', device)   
            self.lh_builder.lh.define_physics_parameter(device + '/ICORR', 'ICORR', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        for device in self.esr_cavities_ampl:
            self.lh_builder.lh.define_physics_parameter(device + '/URF', 'URF', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
            #self.lh_builder.lh.define_hardware_parameter(device, 'BROTAMPL', 'highValue')


        for device in self.esr_cavities_freq:
            self.lh_builder.lh.define_physics_parameter(device + '/FRF', 'FRF', device)
            #self.lh_builder.lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

        for device in self.polefacewindings:
            self.lh_builder.lh.define_physics_parameter(device + '/IPFW', 'IPFW', device)

        ## Kicker parameters
        kicker_knob_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', kicker_device)

        ## relations

        incorpip_parameter = self.reader.find_unique_string('ESRTIMEPARAM/INCORPIP$', self.lh_builder.lh.get_parameters())
        brho_parameter = self.reader.find_unique_string('ESRBEAM/BRHO$', self.lh_builder.lh.get_parameters())
        brho_start_end_parameter = self.reader.find_unique_string('ESRBEAM/BRHO_START_END$', self.lh_builder.lh.get_parameters())

        h_parameter = self.reader.find_unique_string('ESRBEAM/H$', self.lh_builder.lh.get_parameters())

        opticsip_parameter = self.reader.find_unique_string('ESROPTICS/OPTICSIP$', self.lh_builder.lh.get_parameters())
        tau_start_end_parameter = self.reader.find_unique_string('ESROPTICS/TAU_START_END$', self.lh_builder.lh.get_parameters())

        t_wait_parameter = self.reader.find_unique_string('ESRTIMEPARAM/T_WAIT$', self.lh_builder.lh.get_parameters())
        tgrid_parameter = self.reader.find_unique_string('ESRTIMEPARAM/TGRID$', self.lh_builder.lh.get_parameters())
        tround_parameter = self.reader.find_unique_string('ESRTIMEPARAM/TROUND$', self.lh_builder.lh.get_parameters())
        t_bp_length_parameter = self.reader.find_unique_string('ESRTIMEPARAM/T_BP_LENGTH$', self.lh_builder.lh.get_parameters())
        bp_length_parameter = self.reader.find_unique_string('ESRTIMEPARAM/BP_LENGTH$', self.lh_builder.lh.get_parameters())
        bdot_parameter = self.reader.find_unique_string('ESRTIMEPARAM/BDOT$', self.lh_builder.lh.get_parameters())

        urfring_parameter = self.reader.find_unique_string('ESRRF/URFRING$', self.lh_builder.lh.get_parameters())
        frfring_parameter = self.reader.find_unique_string('ESRRF/FRFRING$', self.lh_builder.lh.get_parameters())
        rf_mode_parameter = self.reader.find_unique_string('ESRRF/MODE$', self.lh_builder.lh.get_parameters())

        ## Optics Parameters
        self.lh_builder.create_child_node(opticsip_parameter, [ bp_length_parameter, tau_start_end_parameter, incorpip_parameter ])

        ## Timeparam Parameters
        self.lh_builder.create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, tau_start_end_parameter, tround_parameter,  bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
        self.lh_builder.create_child_node(incorpip_parameter, bp_length_parameter )

        ## Magnets
        for device in self.horizontal_correction_coils:
            kl_parameter = self.reader.find_unique_string(device + '/K[0-3]?L$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, opticsip_parameter)
            blcorr_parameter = self.reader.find_unique_string(device + '/B[0-3]?LCORR$', self.lh_builder.lh.get_parameters())
            icorr_parameter = self.reader.find_unique_string(device + '/ICORR$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(blcorr_parameter, [ brho_parameter, kl_parameter, incorpip_parameter ])

            for dipol_device in self.main_dipoles:
                i_parameter = self.reader.find_unique_string(dipol_device + '/I$', self.lh_builder.lh.get_parameters())
                bl_parameter = self.reader.find_unique_string(dipol_device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(icorr_parameter, [ i_parameter, blcorr_parameter, bl_parameter ])

        for device in self.polefacewindings:
            ipfw_parameter = self.reader.find_unique_string(device + '/IPFW$', self.lh_builder.lh.get_parameters())

            for dipol_device in self.main_dipoles:
                bl_parameter = self.reader.find_unique_string(dipol_device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
                self.lh_builder.create_child_node(ipfw_parameter, [ bl_parameter , incorpip_parameter ])

        for device in self.esr_cavities_ampl:
            urf_parameter = self.reader.find_unique_string(device[:-1] + 'A/URF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(urf_parameter, [ h_parameter, incorpip_parameter, urfring_parameter, rf_mode_parameter ])
            #rampvals_a_parameter = self.reader.find_unique_string(device[:-1] + 'A/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_a_parameter, urf_parameter )

            frf_parameter = self.reader.find_unique_string(device[:-1] + 'FS/FRF$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(frf_parameter, [ h_parameter, incorpip_parameter, frfring_parameter, rf_mode_parameter ])
            #rampvals_fs_parameter = self.reader.find_unique_string(device[:-1] + 'FS/RAMPVALS#data$', self.lh_builder.lh.get_parameters())
            #self.lh_builder.create_child_node(rampvals_fs_parameter, frf_parameter )


        return self.lh_builder
