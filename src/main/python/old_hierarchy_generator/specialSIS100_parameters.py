#!/bin/env python2.6

from lh_builder_utils import LHBuilderUtils


class SpecialSIS100Parameters:

    def __init__(self, lh_builder, csv_filename):
        self.lh_builder = lh_builder
        self.reader = LHBuilderUtils()
        self.all_devices = self.reader._read_devices(csv_filename)

    def setkicker(self, kicker):
        self.kicker = kicker

    def setq_kicker(self, q_kicker):
        self.q_kicker = q_kicker

    def build(self, particle_transfer):

        beam_device = self.reader.find_unique_string(particle_transfer.replace('_RING','BEAM'), self.all_devices)
        optics_device = self.reader.find_unique_string(particle_transfer.replace('_RING','OPTICS'), self.all_devices)
        timeparam_device = self.reader.find_unique_string(particle_transfer.replace('_RING','TIMEPARAM'), self.all_devices)
        kicker_device = self.reader.find_unique_string(particle_transfer.replace('_RING','KICKER'), self.all_devices)

        incorpip_parameter = self.reader.find_unique_string(timeparam_device + '/INCORPIP$', self.lh_builder.lh.get_parameters())

        opticsip_parameter = self.reader.find_unique_string(optics_device + '/OPTICSIP$', self.lh_builder.lh.get_parameters())
        tau_start_end_parameter = self.reader.find_unique_string(optics_device + '/TAU_START_END$', self.lh_builder.lh.get_parameters())
        brho_start_end_parameter = self.reader.find_unique_string(beam_device + '/BRHO_START_END$', self.lh_builder.lh.get_parameters())
        brho_parameter = self.reader.find_unique_string(beam_device + '/BRHO$', self.lh_builder.lh.get_parameters())

        t_wait_parameter = self.reader.find_unique_string(timeparam_device + '/T_WAIT$', self.lh_builder.lh.get_parameters())
        tgrid_parameter = self.reader.find_unique_string(timeparam_device + '/TGRID$', self.lh_builder.lh.get_parameters())
        tround_parameter = self.reader.find_unique_string(timeparam_device + '/TROUND$', self.lh_builder.lh.get_parameters())
        t_bp_length_parameter = self.reader.find_unique_string(timeparam_device + '/T_BP_LENGTH$', self.lh_builder.lh.get_parameters())
        bp_length_parameter = self.reader.find_unique_string(timeparam_device + '/BP_LENGTH$', self.lh_builder.lh.get_parameters())
        bdot_parameter = self.reader.find_unique_string(timeparam_device + '/BDOT$', self.lh_builder.lh.get_parameters())

        gamma_parameter = self.reader.find_unique_string(beam_device + '/GAMMA$', self.lh_builder.lh.get_parameters())

        ## Kicker parameters
        kicker_inj_kick_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/INJ_KICK', 'SCALAR_INJ_KICK', kicker_device)
        kicker_ext_kick_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/EXT_KICK', 'SCALAR_EXT_KICK', kicker_device)
        kicker_qh_kick_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/QH_KICK', 'SCALAR_Q_KICK', kicker_device)
        kicker_qv_kick_parameter = self.lh_builder.lh.define_physics_parameter(kicker_device + '/QV_KICK', 'SCALAR_Q_KICK', kicker_device)


        ## Optics parameters

        #SIS100
        self.lh_builder.create_child_node(opticsip_parameter, [ tau_start_end_parameter, incorpip_parameter, tgrid_parameter, tround_parameter, t_wait_parameter, gamma_parameter ])

        ## Timeparam Parameters
        ##SIS100
        self.lh_builder.create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, tau_start_end_parameter, tround_parameter, bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
        self.lh_builder.create_child_node(incorpip_parameter, bp_length_parameter )

        ## Kicker
        for device in self.kicker:
            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(kl_parameter, [ kicker_ext_kick_parameter , opticsip_parameter ])

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , brho_parameter ])

            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(ukick_parameter, bl_parameter )

        ## Q_Kicker
        for device in self.q_kicker:
            kl_parameter = self.reader.find_unique_string(device + '/KL$', self.lh_builder.lh.get_parameters())

            number = int(device[6:7])
            if (number == 1) :
                self.lh_builder.create_child_node(kl_parameter, [ opticsip_parameter, kicker_qh_kick_parameter ])
            elif (number == 2) :
                self.lh_builder.create_child_node(kl_parameter, [ opticsip_parameter, kicker_qv_kick_parameter ])

            bl_parameter = self.reader.find_unique_string(device + '/BL$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(bl_parameter, [ kl_parameter , brho_parameter ])

            ukick_parameter = self.reader.find_unique_string(device + '/UKICK$', self.lh_builder.lh.get_parameters())
            self.lh_builder.create_child_node(ukick_parameter, bl_parameter )

        return self.lh_builder
