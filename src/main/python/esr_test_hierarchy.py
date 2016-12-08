#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller
@author: dondreka
@author: hlieberm
'''

from __future__ import print_function # Python 3.x style print function

from lsa_hierarchy import LsaHierarchy

###
# Actual definitions
###   
accelerator = 'ESR'
particle_transfer = 'ESR_RING'
hierarchy = 'DEFAULT'
version = '1.0.0'

lh = LsaHierarchy(accelerator, particle_transfer, version)
        
def create_child_node(parameter_name, parameter_parent_names):
    if (parameter_name == None) or (parameter_parent_names is None):
        return
    if (type(parameter_parent_names) is str):
        lh.add_parameter_relations(parameter_name, [ parameter_parent_names ] )
    else:
        lh.add_parameter_relations(parameter_name, parameter_parent_names )

## Standard beam and logical devices
beam_device = '%sBEAM' % accelerator 
optics_device = '%sOPTICS' % accelerator
rf_device = '%sRF' % accelerator
timeparam_device = '%sTIMEPARAM' % accelerator
kicker_device = '%sKICKER' % accelerator

hf_cavity_first_amplitude = lh.define_hardware_parameter("E02BE1A", "RAMPVALS", "data", is_trimable=False)

## Beam parameters
a_parameter = lh.define_physics_parameter(beam_device + '/A', 'SCALAR_A', beam_device, belongs_to_function_bproc=False)
alphac_parameter = lh.define_physics_parameter(beam_device + '/ALPHAC', 'ALPHAC', beam_device, is_trimable=False)
aoq_parameter = lh.define_physics_parameter(beam_device + '/AOQ', 'SCALAR_AOQ', beam_device, is_trimable=False, belongs_to_function_bproc=False)
brho_parameter = lh.define_physics_parameter(beam_device + '/BRHO', 'BRHO', beam_device, is_trimable=False)
brhodot_parameter = lh.define_physics_parameter(beam_device + '/BRHODOT', 'BRHODOT', beam_device, is_trimable=False)
brho_start_end_parameter = lh.define_physics_parameter(beam_device + '/BRHO_START_END', 'SCALAR_BRHO', beam_device, is_trimable=False)
bucketfill_parameter = lh.define_physics_parameter(beam_device + '/BUCKETFILL', 'SCALAR_BUCKETFILL', beam_device)
bunchfactor_parameter = lh.define_physics_parameter(beam_device + '/BUNCHFACTOR', 'BUNCHFACTOR', beam_device)
bunchpattern_parameter = lh.define_physics_parameter(beam_device + '/BUNCHPATTERN', 'SCALAR_BUNCHPATTERN', beam_device)
ch_parameter = lh.define_physics_parameter(beam_device + '/CH', 'CHROMATICITY', beam_device)
cv_parameter = lh.define_physics_parameter(beam_device + '/CV', 'CHROMATICITY', beam_device)
deltar_parameter = lh.define_physics_parameter(beam_device + '/DELTAR', 'DELTAR', beam_device)
e_parameter = lh.define_physics_parameter(beam_device + '/E', 'SCALAR_E', beam_device)
element_parameter =  lh.define_physics_parameter(beam_device + '/ELEMENT', 'SCALAR_ELEMENT', beam_device, belongs_to_function_bproc=False)
erho_parameter =  lh.define_physics_parameter(beam_device + '/ERHO', 'ERHO', beam_device, is_trimable=False)
eta_parameter =  lh.define_physics_parameter(beam_device + '/ETA', 'ETA', beam_device, is_trimable=False)
frev_parameter = lh.define_physics_parameter(beam_device + '/FREV', 'FREV', beam_device, is_trimable=False)
gamma_parameter =  lh.define_physics_parameter(beam_device + '/GAMMA', 'GAMMA', beam_device, is_trimable=False)
geofact_parameter =  lh.define_physics_parameter(beam_device + '/GEOFACT', 'GEOFACT', beam_device)
h_parameter = lh.define_physics_parameter(beam_device + '/H', 'SCALAR_H', beam_device)
inj_emih_parameter = lh.define_physics_parameter(beam_device + '/INJ_EMIH', 'SCALAR_INJ_EMIH', beam_device, belongs_to_function_bproc=False)
inj_emil_parameter =  lh.define_physics_parameter(beam_device + '/INJ_EMIL', 'SCALAR_INJ_EMIL', beam_device, belongs_to_function_bproc=False)
inj_emiv_parameter =lh.define_physics_parameter(beam_device + '/INJ_EMIV', 'SCALAR_INJ_EMIV', beam_device, belongs_to_function_bproc=False)
isotope_parameter = lh.define_physics_parameter(beam_device + '/ISOTOPE', 'SCALAR_ISOTOPE', beam_device, belongs_to_function_bproc=False)
kl_ampl_parameter = lh.define_physics_parameter(beam_device + '/KL_AMPL', 'SCALAR_KL_AMPL', beam_device)
kl_harm_parameter =  lh.define_physics_parameter(beam_device + '/KL_HARM', 'SCALAR_KL_HARM', beam_device)
kl_offset_parameter =  lh.define_physics_parameter(beam_device + '/KL_OFFSET', 'SCALAR_KL_OFFSET', beam_device)
kl_phase_parameter = lh.define_physics_parameter(beam_device + '/KL_PHASE', 'SCALAR_KL_PHASE', beam_device)
maxrh_parameter =  lh.define_physics_parameter(beam_device + '/MAXRH', 'MAXRH', beam_device, is_trimable=False)
maxrv_parameter = lh.define_physics_parameter(beam_device + '/MAXRV', 'MAXRV', beam_device, is_trimable=False)
nparticles_parameter = lh.define_physics_parameter(beam_device + '/NPARTICLES', 'SCALAR_NPARTICLES', beam_device, belongs_to_function_bproc=False)
nperbunch_parameter =  lh.define_physics_parameter(beam_device + '/NPERBUNCH', 'SCALAR_NPERBUNCH', beam_device, is_trimable=False)
phis_parameter = lh.define_physics_parameter(beam_device + '/PHIS', 'PHIS', beam_device, is_trimable=False)
q_parameter =  lh.define_physics_parameter(beam_device + '/Q', 'SCALAR_Q', beam_device, belongs_to_function_bproc=False)
qh_parameter = lh.define_physics_parameter(beam_device + '/QH', 'TUNE', beam_device)
qv_parameter = lh.define_physics_parameter(beam_device + '/QV', 'TUNE', beam_device)
tbunch_parameter =  lh.define_physics_parameter(beam_device + '/TBUNCH', 'SCALAR_TBUNCH', beam_device, is_trimable=False)
trev_parameter = lh.define_physics_parameter(beam_device + '/TREV', 'TREV', beam_device, is_trimable=False)

## RF parameters
abkt_parameter =  lh.define_physics_parameter(rf_device + '/ABKT', 'ABKT', rf_device)
dualh_parameter = lh.define_physics_parameter(rf_device + '/DUALH', 'SCALAR_DUALH', rf_device)
dualhip_parameter = lh.define_physics_parameter(rf_device + '/DUALHIP', 'DUALHIP', rf_device)
frfring_parameter = lh.define_physics_parameter(rf_device + '/FRFRING', 'FRFRING', rf_device)
prfring_parameter = lh.define_physics_parameter(rf_device + '/PRFRING', 'PRFRING', rf_device, is_trimable=False)
urfring_parameter = lh.define_physics_parameter(rf_device + '/URFRING', 'URFRING', rf_device, is_trimable=False)
urfsc_parameter = lh.define_physics_parameter(rf_device + '/URFSC', 'URFSC', rf_device, is_trimable=False)

## Optics parameters
opticsip_parameter = lh.define_physics_parameter(optics_device + '/OPTICSIP', 'OPTICSIP', optics_device)
tau_start_end_parameter = lh.define_physics_parameter(optics_device + '/TAU_START_END', 'SCALAR_TAU', optics_device)

## Timeparam parameters
bdot_parameter = lh.define_physics_parameter(timeparam_device + '/BDOT', 'SCALAR_BDOT', timeparam_device)
bp_length_parameter = lh.define_physics_parameter(timeparam_device + '/BP_LENGTH', 'SCALAR_BP_LENGTH', timeparam_device, is_trimable=False)
incorpip_parameter = lh.define_physics_parameter(timeparam_device + '/INCORPIP', 'INCORPIP', timeparam_device, is_trimable=False)
tgrid_parameter = lh.define_physics_parameter(timeparam_device + '/TGRID', 'SCALAR_TGRID', timeparam_device)
tround_parameter = lh.define_physics_parameter(timeparam_device + '/TROUND', 'SCALAR_TROUND', timeparam_device)
t_bp_length_parameter = lh.define_physics_parameter(timeparam_device + '/T_BP_LENGTH', 'SCALAR_T_BP_LENGTH', timeparam_device)
t_wait_parameter = lh.define_physics_parameter(timeparam_device + '/T_WAIT', 'SCALAR_T_WAIT', timeparam_device)


## Kicker parameters
kicker_knob_parameter = lh.define_physics_parameter(kicker_device + '/KNOB', 'SCALAR_KICKER_KNOB', kicker_device)
kicker_mode_parameter = lh.define_physics_parameter(kicker_device + '/MODE', 'SCALAR_KICKER_MODE', kicker_device)
nbunch1_parameter = lh.define_physics_parameter(kicker_device + '/NBUNCH1', 'SCALAR_NBUNCH1', kicker_device)
start_parameter = lh.define_physics_parameter(kicker_device + '/START', 'SCALAR_KICKER_START', kicker_device)
thigh1_parameter = lh.define_physics_parameter(kicker_device + '/THIGH1', 'SCALAR_KICKER_THIGH1', kicker_device)
thigh2_parameter = lh.define_physics_parameter(kicker_device + '/THIGH2', 'SCALAR_KICKER_THIGH2', kicker_device)
toffset1_parameter = lh.define_physics_parameter(kicker_device + '/TOFFSET1', 'SCALAR_KICKER_TOFFSET1', kicker_device)
toffset2_parameter = lh.define_physics_parameter(kicker_device + '/TOFFSET2', 'SCALAR_KICKER_TOFFSET2', kicker_device)



### Creation of relations

## Beam Parameters
create_child_node(a_parameter, [ isotope_parameter, element_parameter ])
create_child_node(alphac_parameter, opticsip_parameter )
create_child_node(aoq_parameter, [ a_parameter, q_parameter ])
create_child_node(brho_parameter, bp_length_parameter )
create_child_node(brhodot_parameter, bp_length_parameter )
create_child_node(brho_start_end_parameter, [ e_parameter, aoq_parameter ])
create_child_node(bunchfactor_parameter, phis_parameter )
create_child_node(ch_parameter, opticsip_parameter )
create_child_node(cv_parameter, opticsip_parameter )
create_child_node(deltar_parameter, bp_length_parameter )
create_child_node(erho_parameter, [ brho_parameter, aoq_parameter ])
create_child_node(eta_parameter, [ gamma_parameter, alphac_parameter ])
create_child_node(frev_parameter, gamma_parameter )
create_child_node(gamma_parameter, [ brho_parameter, aoq_parameter ])
create_child_node(geofact_parameter, [ brho_start_end_parameter, brho_parameter, inj_emiv_parameter, inj_emih_parameter ])
create_child_node(inj_emil_parameter, [ e_parameter, h_parameter ])
create_child_node(maxrh_parameter, [ inj_emih_parameter, inj_emiv_parameter, brho_parameter, opticsip_parameter, brho_start_end_parameter ])
create_child_node(maxrv_parameter, [ inj_emih_parameter, inj_emiv_parameter, brho_parameter, opticsip_parameter, brho_start_end_parameter ])
create_child_node(nperbunch_parameter, [ nparticles_parameter, h_parameter, bunchpattern_parameter ])
create_child_node(phis_parameter, [ aoq_parameter, h_parameter, eta_parameter, abkt_parameter, brhodot_parameter, gamma_parameter, inj_emil_parameter, dualhip_parameter, geofact_parameter, e_parameter, nperbunch_parameter, q_parameter ])
create_child_node(qh_parameter, opticsip_parameter )
create_child_node(qv_parameter, opticsip_parameter )
create_child_node(tbunch_parameter, [ h_parameter, trev_parameter ])
create_child_node(trev_parameter, frev_parameter )

## RF Parameters
create_child_node(abkt_parameter, [ bp_length_parameter, bucketfill_parameter, inj_emil_parameter, tgrid_parameter ])
create_child_node(dualhip_parameter, [ dualh_parameter, bp_length_parameter ])
create_child_node(frfring_parameter, [ frev_parameter, h_parameter ])
create_child_node(prfring_parameter, phis_parameter )
create_child_node(urfring_parameter, phis_parameter )
create_child_node(urfsc_parameter, phis_parameter )

## Optics Parameters
create_child_node(opticsip_parameter, [ incorpip_parameter ])

## Timeparam Parameters
create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, tau_start_end_parameter, tround_parameter, bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
create_child_node(incorpip_parameter, bp_length_parameter )

## Kicker Parameters
create_child_node(thigh1_parameter, [ nbunch1_parameter, tbunch_parameter, h_parameter ])
create_child_node(thigh2_parameter, [ tbunch_parameter, h_parameter, nbunch1_parameter ])
create_child_node(toffset2_parameter, [ toffset1_parameter, thigh1_parameter ])

lh.export()

