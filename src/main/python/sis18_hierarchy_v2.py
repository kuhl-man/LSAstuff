#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller
@author: dondreka
@author: hlieberm
'''

from __future__ import print_function # Python 3.x style print function
import re # Regular expressions
import csv
from lsa_hierarchy import LsaHierarchy

###
# Actual definitions
###   
accelerator = 'SIS18'
particle_transfer = 'SIS18_RING'
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

def _read_devices(file_name):
    _devices = []
    with open(file_name, 'rb') as in_file:
        reader = csv.reader(in_file)
        reader.next() # ignore header line
        for row in reader:
            _devices=_devices + row
    in_file.close()
    return _devices

# ------------------------ Old methods until here

def find_strings(reg_exp, in_list):
# Filtering lists with regular expressions. Note that the pattern
# matching is wrapped as a lambda expression (i.e. an anonymous
# function). If the function evaluates to 'None' on an element of the
# list to be filtered, this element is discarded, else it is retained.
    filtered_list = filter(lambda d: re.search(reg_exp, d), in_list)
    return filtered_list

def find_unique_string(reg_exp, in_list):
    filtered_list = find_strings(reg_exp, in_list)
    if not filtered_list: # python's way of testing for empty lists
        raise RuntimeError('List did not contain string value matching regular expression ' + reg_exp)
    elif len(filtered_list) > 1:
        raise RuntimeError('More than one string value found matching regular expression ' + reg_exp)
    else:
        return filtered_list[0]

### Instantiate devices and device groups

# For now, the list of all devices is read from a file. The file used
# here has been created by exporting an SQL query for device names for
# the given particle transfer.
# For the future, it is conceivable that this list could be read
# directly from the data base.
all_devices = _read_devices('sis18_devices.csv')

## Standard beam and logical devices
beam_device = find_unique_string(particle_transfer.replace('_RING', 'BEAM'), all_devices)
optics_device = find_unique_string(particle_transfer.replace('_RING','OPTICS'), all_devices)
orbit_device = find_unique_string(particle_transfer.replace('_RING','ORBIT'), all_devices)
rf_device = find_unique_string(particle_transfer.replace('_RING','RF'), all_devices)
timeparam_device = find_unique_string(particle_transfer.replace('_RING','TIMEPARAM'), all_devices)
kicker_device = find_unique_string(particle_transfer.replace('_RING','KICKER'), all_devices)
bumper_device = find_unique_string(particle_transfer.replace('_RING','BUMPER'), all_devices)

## Hardware
hardware_fs_system = find_unique_string('S00BE_FS', all_devices)
hardware_rf_system = find_unique_string('S00BE_PS', all_devices)
tgx_system = find_unique_string('S00ZGT', all_devices)
timing_device = find_unique_string('S00ZZ', all_devices)

## Standard device groups
main_dipoles = find_strings('S11MU2$', all_devices)
horizontal_correctors = [] # none for SIS18
vertical_correctors = find_strings('S[01][0-9]KM2DV$', all_devices)

main_quadrupoles = find_strings('S((01)|(12))QS((1F)|(2D)|(3T))$', all_devices)
extraction_quadrupoles = find_strings('S02KQ1E', all_devices)
correction_quadrupoles = find_strings('(S[01][0-9]KM[0-9]Q[SN])|(S[01][0-9]KQ[0-9])|(S[01][0-9]KQ[0-9]E)$', all_devices)

main_sextupoles = find_strings('S[01][0-9]KS[13]C$', all_devices)
chromaticity_sextupoles = main_sextupoles[:] # python's shallow copy for lists
resonance_sextupoles = find_strings('S[01][0-9]KS1C$', main_sextupoles)
correction_sextupoles = find_strings('S[01][0-9]KM[0-9]S[SN]$', all_devices)

correction_octupoles = find_strings('S[01][0-9]KM[0-9]O[SN]$', all_devices) # none for SIS18

horizontal_correction_coils = find_strings('S[01][0-9]MU[12]A$', all_devices)
extraction_bump_correction_coils = find_strings('(S((04)|(06))MU1A)|(S((05)|(07)|(10)|(11)|(12))MU2A)', horizontal_correction_coils)
extra_correction_coils = find_strings('(S((02)|(07)|(08))MU1A)|(S04MU2A)', horizontal_correction_coils)
horizontal_orbit_correction_coils = list(set(horizontal_correction_coils)-set(extraction_bump_correction_coils))

cavities = find_strings('S07BE[1-3]$', all_devices)

sis18_cavities_ampl = find_strings('S0[28]BE[12]A$', all_devices)
sis18_cavities_freq = find_strings('S0[28]BE[12]FS$', all_devices)
sis18_cavities_phase = find_strings('S0[28]BE[12]P$', all_devices)

bumper = find_strings('S[01][1-3]MB[1-4]$', all_devices)

kicker = find_strings('S0[45]MK[12]E$', all_devices)

sis18_bypass = find_strings('S06MU4$', all_devices)

sis18_ko_exiter = find_strings('S07BO1E$', all_devices)

## Magnet groups according to multipole
all_dipoles = main_dipoles + horizontal_correctors + vertical_correctors
all_quadrupoles = main_quadrupoles + extraction_quadrupoles + correction_quadrupoles
all_sextupoles = main_sextupoles + correction_sextupoles
all_octupoles = correction_octupoles

all_magnets = all_dipoles + all_quadrupoles + all_sextupoles + all_octupoles
main_magnets = main_dipoles + main_quadrupoles

### Creation of parameters

## Hardware rf system parameters
for parameter in hardware_fs_system:
    hardware_fs_rampvals_parameter =  lh.define_hardware_parameter(hardware_fs_system, 'RAMPVALS', 'data')

mhbpar_damp1_parameter = lh.define_hardware_parameter(hardware_fs_system, 'MHBPAR', 'DAmp1')
mhbpar_damp2_parameter = lh.define_hardware_parameter(hardware_fs_system, 'MHBPAR', 'DAmp2')
mhbpar_delay_parameter = lh.define_hardware_parameter(hardware_fs_system, 'MHBPAR', 'Delay')
mhbpar_harm1_parameter = lh.define_hardware_parameter(hardware_fs_system, 'MHBPAR', 'Harm1')
mhbpar_harm2_parameter = lh.define_hardware_parameter(hardware_fs_system, 'MHBPAR', 'Harm2')
syncmode_hfssync_parameter = lh.define_hardware_parameter(hardware_fs_system, 'SYNCMODE', 'hfssync')
workmode_workmode_parameter = lh.define_hardware_parameter(hardware_fs_system, 'WORKMODE', 'workmode')

delay_trgdelay_parameter =  lh.define_hardware_parameter(tgx_system, 'DELAY', 'trgdelay')
harmonic_harmonic_parameter = lh.define_hardware_parameter(tgx_system, 'HARMONIC', 'harmonic')
mode_kickmode_parameter = lh.define_hardware_parameter(tgx_system, 'MODE', 'kickmode')
rftrig_rftrig_parameter = lh.define_hardware_parameter(tgx_system, 'RFTRIG', 'rftrig')

chansequ_chancount_parameter = lh.define_hardware_parameter(timing_device, 'CHANSEQU', 'chanCount')
chansequ_chansequ_parameter = lh.define_hardware_parameter(timing_device, 'CHANSEQU', 'chanSequ')
evtarray_chanarray_parameter = lh.define_hardware_parameter(timing_device, 'EVTARRAY', 'chanArray')
timeout_unilac_parameter = lh.define_physics_parameter(timing_device + '/TIMEOUT_UNILAC', 'SCALAR_TIMEOUT_UNILAC', timing_device)
tmeasure_parameter = lh.define_physics_parameter(timing_device + '/TMEASURE', 'SCALAR_TMEASURE', timing_device)
toffset_unilac_parameter = lh.define_physics_parameter(timing_device + '/TOFFSET_UNILAC', 'SCALAR_TOFFSET_UNILAC', timing_device)


## Beam parameters
a_parameter = lh.define_physics_parameter(beam_device + '/A', 'SCALAR_A', beam_device)
alphac_parameter = lh.define_physics_parameter(beam_device + '/ALPHAC', 'ALPHAC', beam_device)
aoq_parameter = lh.define_physics_parameter(beam_device + '/AOQ', 'SCALAR_AOQ', beam_device)
brho_parameter = lh.define_physics_parameter(beam_device + '/BRHO', 'BRHO', beam_device)
brhodot_parameter = lh.define_physics_parameter(beam_device + '/BRHODOT', 'BRHODOT', beam_device)
brho_start_end_parameter = lh.define_physics_parameter(beam_device + '/BRHO_START_END', 'SCALAR_BRHO', beam_device)
bucketfill_parameter = lh.define_physics_parameter(beam_device + '/BUCKETFILL', 'SCALAR_BUCKETFILL', beam_device)
bunchfactor_parameter = lh.define_physics_parameter(beam_device + '/BUNCHFACTOR', 'BUNCHFACTOR', beam_device)
bunchpattern_parameter = lh.define_physics_parameter(beam_device + '/BUNCHPATTERN', 'SCALAR_BUNCHPATTERN', beam_device)
ch_parameter = lh.define_physics_parameter(beam_device + '/CH', 'CHROMATICITY', beam_device)
cv_parameter = lh.define_physics_parameter(beam_device + '/CV', 'CHROMATICITY', beam_device)
deltar_parameter = lh.define_physics_parameter(beam_device + '/DELTAR', 'DELTAR', beam_device)
dp_over_p_parameter = lh.define_physics_parameter(beam_device + '/DP_OVER_P', 'SCALAR_DP_OVER_P', beam_device)
e_parameter = lh.define_physics_parameter(beam_device + '/E', 'SCALAR_E', beam_device)
element_parameter =  lh.define_physics_parameter(beam_device + '/ELEMENT', 'SCALAR_ELEMENT', beam_device)
erho_parameter =  lh.define_physics_parameter(beam_device + '/ERHO', 'ERHO', beam_device)
eta_parameter =  lh.define_physics_parameter(beam_device + '/ETA', 'ETA', beam_device)
frev_parameter = lh.define_physics_parameter(beam_device + '/FREV', 'FREV', beam_device)
gamma_parameter =  lh.define_physics_parameter(beam_device + '/GAMMA', 'GAMMA', beam_device)
geofact_parameter =  lh.define_physics_parameter(beam_device + '/GEOFACT', 'GEOFACT', beam_device)
h_parameter = lh.define_physics_parameter(beam_device + '/H', 'SCALAR_H', beam_device)
inj_emih_parameter = lh.define_physics_parameter(beam_device + '/INJ_EMIH', 'SCALAR_INJ_EMIH', beam_device)
inj_emil_parameter =  lh.define_physics_parameter(beam_device + '/INJ_EMIL', 'SCALAR_INJ_EMIL', beam_device)
inj_emiv_parameter =lh.define_physics_parameter(beam_device + '/INJ_EMIV', 'SCALAR_INJ_EMIV', beam_device)
isotope_parameter = lh.define_physics_parameter(beam_device + '/ISOTOPE', 'SCALAR_ISOTOPE', beam_device)
kl_ampl_parameter = lh.define_physics_parameter(beam_device + '/KL_AMPL', 'SCALAR_KL_AMPL', beam_device)
kl_harm_parameter =  lh.define_physics_parameter(beam_device + '/KL_HARM', 'SCALAR_KL_HARM', beam_device)
kl_offset_parameter =  lh.define_physics_parameter(beam_device + '/KL_OFFSET', 'SCALAR_KL_OFFSET', beam_device)
kl_phase_parameter = lh.define_physics_parameter(beam_device + '/KL_PHASE', 'SCALAR_KL_PHASE', beam_device)
maxrh_parameter =  lh.define_physics_parameter(beam_device + '/MAXRH', 'MAXRH', beam_device)
maxrv_parameter = lh.define_physics_parameter(beam_device + '/MAXRV', 'MAXRV', beam_device)
nparticles_parameter = lh.define_physics_parameter(beam_device + '/NPARTICLES', 'SCALAR_NPARTICLES', beam_device)
nperbunch_parameter =  lh.define_physics_parameter(beam_device + '/NPERBUNCH', 'SCALAR_NPERBUNCH', beam_device)
phis_parameter = lh.define_physics_parameter(beam_device + '/PHIS', 'PHIS', beam_device)
q_parameter =  lh.define_physics_parameter(beam_device + '/Q', 'SCALAR_Q', beam_device)
qh_parameter = lh.define_physics_parameter(beam_device + '/QH', 'TUNE', beam_device)
qv_parameter = lh.define_physics_parameter(beam_device + '/QV', 'TUNE', beam_device)
tbunch_parameter =  lh.define_physics_parameter(beam_device + '/TBUNCH', 'SCALAR_TBUNCH', beam_device)
trev_parameter = lh.define_physics_parameter(beam_device + '/TREV', 'TREV', beam_device)

## RF parameters
abkt_parameter =  lh.define_physics_parameter(rf_device + '/ABKT', 'ABKT', rf_device)
dualh_parameter = lh.define_physics_parameter(rf_device + '/DUALH', 'SCALAR_DUALH', rf_device)
dualhip_parameter = lh.define_physics_parameter(rf_device + '/DUALHIP', 'DUALHIP', rf_device)
frfring_parameter = lh.define_physics_parameter(rf_device + '/FRFRING', 'FRFRING', rf_device)
rf_mode_parameter = lh.define_physics_parameter(rf_device + '/MODE', 'MODE', rf_device)
prfring_parameter = lh.define_physics_parameter(rf_device + '/PRFRING', 'PRFRING', rf_device)
urfring_parameter = lh.define_physics_parameter(rf_device + '/URFRING', 'URFRING', rf_device)
urfsc_parameter = lh.define_physics_parameter(rf_device + '/URFSC', 'URFSC', rf_device)

for device in cavities:
    lh.define_physics_parameter(device + '/URF', 'URF', device)
    lh.define_physics_parameter(device + '/FRF', 'FRF', device)
    lh.define_physics_parameter(device + '/PRF', 'PRF', device)

for device in sis18_cavities_ampl:
    lh.define_physics_parameter(device + '/URF', 'URF', device)
    lh.define_hardware_parameter(device, 'RAMPVALS', 'data')
    lh.define_hardware_parameter(device, 'BROTAMPL', 'highValue')


for device in sis18_cavities_freq:
    lh.define_physics_parameter(device + '/FRF', 'FRF', device)
    lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

for device in sis18_cavities_phase:
    lh.define_physics_parameter(device + '/PRF', 'PRF', device)
    lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

## Optics parameters
ext_sigma_parameter = lh.define_physics_parameter(optics_device + '/EXT_SIGMA', 'SCALAR_EXT_SIGMA', optics_device)
opticsip_parameter = lh.define_physics_parameter(optics_device + '/OPTICSIP', 'OPTICSIP', optics_device)
sigma_parameter = lh.define_physics_parameter(optics_device + '/SIGMA', 'SIGMA', optics_device)
tau_parameter = lh.define_physics_parameter(optics_device + '/TAU', 'TAU', optics_device)
tau_endpoint_parameter = lh.define_physics_parameter(optics_device + '/TAU_ENDPOINT', 'SCALAR_TAU_ENDPOINT', optics_device)
tau_nlp_parameter = lh.define_physics_parameter(optics_device + '/TAU_NLP', 'SCALAR_TAU_NLP', optics_device)
tau_start_end_parameter = lh.define_physics_parameter(optics_device + '/TAU_START_END', 'SCALAR_TAU', optics_device)

## Orbit parameters
coh01_parameter = lh.define_physics_parameter(orbit_device + '/COH01', 'ORBITBUMP', orbit_device)
coh02_parameter = lh.define_physics_parameter(orbit_device + '/COH02', 'ORBITBUMP', orbit_device)
coh03_parameter = lh.define_physics_parameter(orbit_device + '/COH03', 'ORBITBUMP', orbit_device)
coh04_parameter = lh.define_physics_parameter(orbit_device + '/COH04', 'ORBITBUMP', orbit_device)
coh05_parameter = lh.define_physics_parameter(orbit_device + '/COH05', 'ORBITBUMP', orbit_device)
coh06_parameter = lh.define_physics_parameter(orbit_device + '/COH06', 'ORBITBUMP', orbit_device)
coh07_parameter = lh.define_physics_parameter(orbit_device + '/COH07', 'ORBITBUMP', orbit_device)
coh08_parameter = lh.define_physics_parameter(orbit_device + '/COH08', 'ORBITBUMP', orbit_device)
coh09_parameter = lh.define_physics_parameter(orbit_device + '/COH09', 'ORBITBUMP', orbit_device)
coh10_parameter = lh.define_physics_parameter(orbit_device + '/COH10', 'ORBITBUMP', orbit_device)
coh11_parameter = lh.define_physics_parameter(orbit_device + '/COH11', 'ORBITBUMP', orbit_device)
coh12_parameter = lh.define_physics_parameter(orbit_device + '/COH12', 'ORBITBUMP', orbit_device)
cov01_parameter = lh.define_physics_parameter(orbit_device + '/COV01', 'ORBITBUMP', orbit_device)
cov02_parameter = lh.define_physics_parameter(orbit_device + '/COV02', 'ORBITBUMP', orbit_device)
cov03_parameter = lh.define_physics_parameter(orbit_device + '/COV03', 'ORBITBUMP', orbit_device)
cov04_parameter = lh.define_physics_parameter(orbit_device + '/COV04', 'ORBITBUMP', orbit_device)
cov05_parameter = lh.define_physics_parameter(orbit_device + '/COV05', 'ORBITBUMP', orbit_device)
cov06_parameter = lh.define_physics_parameter(orbit_device + '/COV06', 'ORBITBUMP', orbit_device)
cov07_parameter = lh.define_physics_parameter(orbit_device + '/COV07', 'ORBITBUMP', orbit_device)
cov08_parameter = lh.define_physics_parameter(orbit_device + '/COV08', 'ORBITBUMP', orbit_device)
cov09_parameter = lh.define_physics_parameter(orbit_device + '/COV09', 'ORBITBUMP', orbit_device)
cov10_parameter = lh.define_physics_parameter(orbit_device + '/COV10', 'ORBITBUMP', orbit_device)
cov11_parameter = lh.define_physics_parameter(orbit_device + '/COV11', 'ORBITBUMP', orbit_device)
cov12_parameter = lh.define_physics_parameter(orbit_device + '/COH12', 'ORBITBUMP', orbit_device)
extesep_parameter = lh.define_physics_parameter(orbit_device + '/EXTESEP', 'FLATBUMP', orbit_device)
extmsep_parameter = lh.define_physics_parameter(orbit_device + '/EXTMSEP', 'FLATBUMP', orbit_device)

coh_list = [coh01_parameter, coh02_parameter, coh03_parameter, coh04_parameter, coh05_parameter, coh06_parameter, coh07_parameter, coh08_parameter, coh09_parameter, coh10_parameter, coh11_parameter, coh12_parameter]

cov_list = [cov01_parameter, cov02_parameter, cov03_parameter, cov04_parameter, cov05_parameter, cov06_parameter, cov07_parameter, cov08_parameter, cov09_parameter, cov10_parameter, cov11_parameter, cov12_parameter]

## Timeparam parameters
bdot_parameter = lh.define_physics_parameter(timeparam_device + '/BDOT', 'SCALAR_BDOT', timeparam_device)
bp_length_parameter = lh.define_physics_parameter(timeparam_device + '/BP_LENGTH', 'SCALAR_BP_LENGTH', timeparam_device)
incorpip_parameter = lh.define_physics_parameter(timeparam_device + '/INCORPIP', 'INCORPIP', timeparam_device)
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

## Bumper parameters
curvature_parameter = lh.define_physics_parameter(bumper_device + '/CURVATURE', 'SCALAR_BUMPER_CURVATURE', bumper_device)
bumper_knob_parameter = lh.define_physics_parameter(bumper_device + '/KNOB', 'SCALAR_BUMPER_KNOB', bumper_device)
tfall_parameter = lh.define_physics_parameter(bumper_device + '/TFALL', 'SCALAR_TFALL', bumper_device)


for device in all_dipoles:
    lh.define_physics_parameter(device + '/KL', 'K0L', device)
    lh.define_physics_parameter(device + '/BL', 'B0L', device)

for device in all_quadrupoles:
    lh.define_physics_parameter(device + '/KL', 'K1L', device)
    lh.define_physics_parameter(device + '/BL', 'B1L', device)

for device in all_sextupoles:
    lh.define_physics_parameter(device + '/KLDELTA', 'DELTA_K2L', device) ## KLDELTA soll nicht fuer S02KM5SS und S08KM5SS angelegt werden, hier muss noch eine extra gruppe / hierarchie erstellt werden
    lh.define_physics_parameter(device + '/KL', 'K2L', device)
    lh.define_physics_parameter(device + '/BL', 'B2L', device)

for device in all_octupoles:
    lh.define_physics_parameter(device + '/KL', 'K3L', device)
    lh.define_physics_parameter(device + '/BL', 'B3L', device)

for device in kicker:
    lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
    lh.define_physics_parameter(device + '/BL', 'SCALAR_B0L', device)
    lh.define_physics_parameter(device + '/UKICK', 'SCALAR_UKICK', device)
    if device == 'S05MK2E': # Skip these parameters for the seconds kicker in SIS18
        continue
    lh.define_hardware_parameter(device, 'TIMDELRF', 'time')
    lh.define_hardware_parameter(device, 'TIMDELTG', 'time')
    lh.define_hardware_parameter(device, 'TIMFTRF', 'time')
    lh.define_hardware_parameter(device, 'TIMFTTG', 'time')
    lh.define_hardware_parameter(device, 'VOLTRFS', 'voltages')
    lh.define_hardware_parameter(device, 'VOLTRIS', 'voltages')
    lh.define_hardware_parameter(device, 'VOLTTGS', 'voltages')


for device in bumper:
    lh.define_physics_parameter(device + '/KL', 'SCALAR_K0L', device)
    lh.define_physics_parameter(device + '/BL', 'SCALAR_B0L', device)
    lh.define_physics_parameter(device + '/I', 'SCALAR_I', device)
    lh.define_hardware_parameter(device, 'CURRENTS', 'currents')
    lh.define_hardware_parameter(device, 'FTIMES', 'ftimes')
    lh.define_hardware_parameter(device, 'PARA', 'reference_parameters')


for device in extraction_bump_correction_coils:
    lh.define_physics_parameter(device + '/KL', 'FLAT_K0L', device)

for device in horizontal_orbit_correction_coils:
    lh.define_physics_parameter(device + '/KL', 'K0L', device)

for device in horizontal_correction_coils:
    lh.define_physics_parameter(device + '/BLCORR', 'CORR_B0L', device)   
    lh.define_physics_parameter(device + '/ICORR', 'ICORR', device)
    lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

for device in extra_correction_coils:
    lh.define_physics_parameter(device + '/ICORRDOT', 'ICORRDOT', device)
    lh.define_physics_parameter(device + '/UCORR', 'UCORR', device)

for device in all_magnets:
    lh.define_physics_parameter(device + '/I', 'I', device)
    lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

for device in main_magnets:
    lh.define_physics_parameter(device + '/IDOT', 'IDOT', device)
    lh.define_physics_parameter(device + '/UEDDY', 'UEDDY', device)
    lh.define_physics_parameter(device + '/U', 'U', device)

for device in sis18_bypass:
    lh.define_physics_parameter(device + '/KLBYP', 'SCALAR_KLBYP', device)
    lh.define_physics_parameter(device + '/BLBYP', 'SCALAR_BLBYP', device)
    lh.define_physics_parameter(device + '/IBYP', 'IBYP', device)
    lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

for device in sis18_ko_exiter:
    lh.define_physics_parameter(device + '/DQH', 'SCALAR_DQHKO', device)
    lh.define_physics_parameter(device + '/QHFR', 'SCALAR_QHFRKO', device)
    lh.define_physics_parameter(device + '/START_TAU', 'SCALAR_START_TAUKO', device)
    lh.define_physics_parameter(device + '/END_TAU', 'SCALAR_END_TAUKO', device)
    lh.define_physics_parameter(device + '/START_AMPL', 'SCALAR_START_AMPLKO', device)
    lh.define_physics_parameter(device + '/END_AMPL', 'SCALAR_END_AMPLKO', device)
    lh.define_physics_parameter(device + '/UPP', 'UPPKO', device) 
    lh.define_physics_parameter(device + '/UCTRL', 'UCTRLKO', device)
    lh.define_hardware_parameter(device, 'RAMPVALS', 'data')

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
create_child_node(inj_emil_parameter, [ dp_over_p_parameter, e_parameter, h_parameter ])
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
create_child_node(opticsip_parameter, [ sigma_parameter, tau_parameter, incorpip_parameter ])
create_child_node(sigma_parameter, [ brho_start_end_parameter, ext_sigma_parameter, bp_length_parameter, t_wait_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])
create_child_node(tau_parameter, [ tau_nlp_parameter, tau_start_end_parameter, bp_length_parameter, t_wait_parameter, brho_start_end_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])

## Orbit Parameters
create_child_node(coh01_parameter, incorpip_parameter )
create_child_node(coh02_parameter, incorpip_parameter )
create_child_node(coh03_parameter, incorpip_parameter )
create_child_node(coh04_parameter, incorpip_parameter )
create_child_node(coh05_parameter, incorpip_parameter )
create_child_node(coh06_parameter, incorpip_parameter )
create_child_node(coh07_parameter, incorpip_parameter )
create_child_node(coh08_parameter, incorpip_parameter )
create_child_node(coh09_parameter, incorpip_parameter )
create_child_node(coh10_parameter, incorpip_parameter )
create_child_node(coh11_parameter, incorpip_parameter )
create_child_node(coh12_parameter, incorpip_parameter )
create_child_node(cov01_parameter, incorpip_parameter )
create_child_node(cov02_parameter, incorpip_parameter )
create_child_node(cov03_parameter, incorpip_parameter )
create_child_node(cov04_parameter, incorpip_parameter )
create_child_node(cov05_parameter, incorpip_parameter )
create_child_node(cov06_parameter, incorpip_parameter )
create_child_node(cov07_parameter, incorpip_parameter )
create_child_node(cov08_parameter, incorpip_parameter )
create_child_node(cov09_parameter, incorpip_parameter )
create_child_node(cov10_parameter, incorpip_parameter )
create_child_node(cov11_parameter, incorpip_parameter )
create_child_node(cov12_parameter, incorpip_parameter )
create_child_node(extesep_parameter, incorpip_parameter )
create_child_node(extmsep_parameter, incorpip_parameter )

## Timeparam Parameters
create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, ext_sigma_parameter, tau_start_end_parameter, tround_parameter, bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
create_child_node(incorpip_parameter, bp_length_parameter )

## Kicker Parameters
create_child_node(thigh1_parameter, [ nbunch1_parameter, tbunch_parameter, h_parameter ])
create_child_node(thigh2_parameter, [ tbunch_parameter, h_parameter, nbunch1_parameter ])
create_child_node(toffset2_parameter, [ toffset1_parameter, thigh1_parameter ])

## Hardware rf system parameters
create_child_node(hardware_fs_rampvals_parameter, frev_parameter)

create_child_node(mhbpar_damp1_parameter, h_parameter )
create_child_node(mhbpar_damp2_parameter, h_parameter )
create_child_node(mhbpar_delay_parameter, h_parameter )
create_child_node(mhbpar_harm1_parameter, h_parameter )
create_child_node(mhbpar_harm2_parameter, h_parameter )
create_child_node(syncmode_hfssync_parameter, h_parameter )
create_child_node(workmode_workmode_parameter, h_parameter )

create_child_node(delay_trgdelay_parameter, [ tbunch_parameter, h_parameter, start_parameter ])
create_child_node(harmonic_harmonic_parameter, h_parameter )
create_child_node(mode_kickmode_parameter, [ kicker_mode_parameter, nbunch1_parameter, h_parameter ])
create_child_node(rftrig_rftrig_parameter, h_parameter )

create_child_node(chansequ_chancount_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter, kicker_mode_parameter ])
create_child_node(chansequ_chansequ_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter, kicker_mode_parameter ])
create_child_node(evtarray_chanarray_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter, kicker_mode_parameter ])

## Horizontal_orbit_correction_coils
horizontal_orbit_correction_coils.sort()
for device in horizontal_orbit_correction_coils:
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', lh.get_parameters())
    sector = int(device[1:3])
    index = sector - 1
    if (sector == 5) :
        create_child_node(kl_parameter, [ extesep_parameter, opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
    elif (sector == 7) :
        create_child_node(kl_parameter, [ extmsep_parameter, opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
    else:
        create_child_node(kl_parameter, [ opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])

## Extraction_bump_correction_coils
for device in extraction_bump_correction_coils:
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', lh.get_parameters())
    sector = int(device[1:3])
    if ((sector == 10) | (sector == 11) | (sector == 12)) :
        create_child_node(kl_parameter, opticsip_parameter)
    elif ((sector == 4) | (sector == 5)) :
        create_child_node(kl_parameter, [ opticsip_parameter, extesep_parameter ])
    else:
        create_child_node(kl_parameter, [ opticsip_parameter, extmsep_parameter ])

## Magnets
for device in all_magnets:
    bl_parameter = find_unique_string(device + '/B[0-3]?L$', lh.get_parameters())
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', lh.get_parameters())
    create_child_node(bl_parameter, [ brho_parameter, kl_parameter, incorpip_parameter])

for device in all_dipoles:
    bl_parameter = find_unique_string(device + '/B[0-3]?L$', lh.get_parameters())
    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    create_child_node(i_parameter, bl_parameter)

for device in main_dipoles:
    kl_parameter = find_unique_string(device + '/K0?L$', lh.get_parameters())
    create_child_node(kl_parameter, opticsip_parameter )

for device in main_quadrupoles:
    kl_parameter = find_unique_string(device + '/K1?L$', lh.get_parameters())
    create_child_node(kl_parameter, [ qh_parameter, qv_parameter, opticsip_parameter ])

for device in main_sextupoles:
    kldelta_parameter = find_unique_string(device + '/KLDELTA$', lh.get_parameters())
    create_child_node(kldelta_parameter, [ incorpip_parameter, kl_harm_parameter, kl_phase_parameter, kl_ampl_parameter, kl_offset_parameter ])

    kl_parameter = find_unique_string(device + '/K2?L$', lh.get_parameters())    
    create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter, kldelta_parameter ]) 

    bl_parameter = find_unique_string(device + '/B[0-3]?L$', lh.get_parameters())
    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    create_child_node(i_parameter, bl_parameter)

    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, i_parameter ) 

for device in correction_quadrupoles:
    kl_parameter = find_unique_string(device + '/K2?L$', lh.get_parameters())
    create_child_node(kl_parameter, opticsip_parameter )

    bl_parameter = find_unique_string(device + '/B[1]?L$', lh.get_parameters())
    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    create_child_node(i_parameter, bl_parameter)

    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, i_parameter)

for device in chromaticity_sextupoles:
    kl_parameter = find_unique_string(device + '/K2?L$', lh.get_parameters())
    create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter ])

for device in main_magnets:
    bl_parameter = find_unique_string(device + '/B[0-3]?L$', lh.get_parameters())
    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    create_child_node(i_parameter, bl_parameter)

    idot_parameter = find_unique_string(device + '/IDOT$', lh.get_parameters())
    create_child_node(idot_parameter, i_parameter)

    ueddy_parameter = find_unique_string(device + '/UEDDY$', lh.get_parameters())
    u_parameter = find_unique_string(device + '/U$', lh.get_parameters())
    create_child_node(ueddy_parameter, idot_parameter )   
    create_child_node(u_parameter, [ ueddy_parameter, idot_parameter ])

    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, [ u_parameter, i_parameter ])

for device in vertical_correctors:
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', lh.get_parameters())
    sector = int(device[1:3])
    index = sector - 1
    create_child_node(kl_parameter, [ opticsip_parameter, cov_list[index], coh_list[index - 1], coh_list[index + 1 - len(cov_list)] ])

    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, i_parameter)

for device in horizontal_correction_coils:
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', lh.get_parameters())
    blcorr_parameter = find_unique_string(device + '/B[0-3]?LCORR$', lh.get_parameters())
    icorr_parameter = find_unique_string(device + '/ICORR$', lh.get_parameters())
    create_child_node(blcorr_parameter, [ brho_parameter, kl_parameter, incorpip_parameter ])

    for dipol_device in main_dipoles:
        i_parameter = find_unique_string(dipol_device + '/I$', lh.get_parameters())
        bl_parameter = find_unique_string(dipol_device + '/B[0-3]?L$', lh.get_parameters())
        create_child_node(icorr_parameter, [ i_parameter, blcorr_parameter, bl_parameter ])

for device in extra_correction_coils:
    icorr_parameter = find_unique_string(device + '/ICORR$', lh.get_parameters())
    icorrdot_parameter = find_unique_string(device + '/ICORRDOT$', lh.get_parameters())
    ucorr_parameter = find_unique_string(device + '/UCORR$', lh.get_parameters())
    create_child_node(icorrdot_parameter, icorr_parameter )

    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, [ icorr_parameter, ucorr_parameter ])
    
    for dipol_device in main_dipoles:
        idot_parameter = find_unique_string(dipol_device + '/IDOT$', lh.get_parameters())
        create_child_node(ucorr_parameter, [ icorrdot_parameter, idot_parameter ])

for device in list(set(horizontal_correction_coils) - set(extra_correction_coils)):
    icorr_parameter = find_unique_string(device + '/ICORR$', lh.get_parameters())
    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, icorr_parameter)

for device in correction_sextupoles:
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', lh.get_parameters())
    create_child_node(kl_parameter, opticsip_parameter)

    bl_parameter = find_unique_string(device + '/B[0-3]?L$', lh.get_parameters())
    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    create_child_node(i_parameter, bl_parameter)

    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, i_parameter)

for device in resonance_sextupoles:
    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, i_parameter)


## Cavities
for device in cavities:
    urf_parameter = find_unique_string(device + '/URF$', lh.get_parameters())
    create_child_node(urf_parameter, [ h_parameter, incorpip_parameter, urfring_parameter, rf_mode_parameter ])

    frf_parameter = find_unique_string(device + '/FRF$', lh.get_parameters())
    create_child_node(frf_parameter, [ h_parameter, incorpip_parameter, frfring_parameter, rf_mode_parameter ])

    prf_parameter = find_unique_string(device + '/PRF$', lh.get_parameters())
    create_child_node(prf_parameter, [ h_parameter, incorpip_parameter, prfring_parameter, rf_mode_parameter ])

for device in sis18_cavities_ampl:
    urf_parameter = find_unique_string(device[:-1] + 'A/URF$', lh.get_parameters())
    create_child_node(urf_parameter, [ h_parameter, incorpip_parameter, urfring_parameter, rf_mode_parameter ])
    rampvals_a_parameter = find_unique_string(device[:-1] + 'A/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_a_parameter, urf_parameter )

    frf_parameter = find_unique_string(device[:-1] + 'FS/FRF$', lh.get_parameters())
    create_child_node(frf_parameter, [ h_parameter, incorpip_parameter, frfring_parameter, rf_mode_parameter ])
    rampvals_fs_parameter = find_unique_string(device[:-1] + 'FS/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_fs_parameter, urf_parameter )

    prf_parameter = find_unique_string(device[:-1] + 'P/PRF$', lh.get_parameters())
    create_child_node(prf_parameter, [ h_parameter, incorpip_parameter, prfring_parameter, rf_mode_parameter ])
    rampvals_p_parameter = find_unique_string(device[:-1] + 'P/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_p_parameter, urf_parameter )

    brotampl_parameter = find_unique_string(device[:-1] + 'A/BROTAMPL#highValue$', lh.get_parameters())
    create_child_node(brotampl_parameter, urf_parameter )

kicker_ukick_parameters = []
for device in kicker:
    ukick_parameter = find_unique_string(device + '/UKICK$', lh.get_parameters())
    kicker_ukick_parameters.append(ukick_parameter)


## Kicker
kicker.sort()
for device in kicker:
    kl_parameter = find_unique_string(device + '/KL$', lh.get_parameters())
    create_child_node(kl_parameter, kicker_knob_parameter )

    bl_parameter = find_unique_string(device + '/BL$', lh.get_parameters())
    create_child_node(bl_parameter, kl_parameter )

    ukick_parameter = find_unique_string(device + '/UKICK$', lh.get_parameters())
    create_child_node(ukick_parameter, bl_parameter )

    if (device == kicker[0]):
        timdelrf_time_parameter = find_unique_string(device + '/TIMDELRF#time$', lh.get_parameters())
        create_child_node(timdelrf_time_parameter, toffset1_parameter)
        
        timdeltg_time_parameter = find_unique_string(device + '/TIMDELTG#time$', lh.get_parameters())
        create_child_node(timdeltg_time_parameter, toffset2_parameter)
        
        timftrf_time_parameter = find_unique_string(device + '/TIMFTRF#time$', lh.get_parameters())
        create_child_node(timftrf_time_parameter, [ toffset1_parameter, thigh1_parameter ])
        
        timfttg_time_parameter = find_unique_string(device + '/TIMFTTG#time$', lh.get_parameters())
        create_child_node(timfttg_time_parameter, [ toffset2_parameter, thigh2_parameter ])
        
        voltrfs_voltages_parameter = find_unique_string(device + '/VOLTRFS#voltages$', lh.get_parameters())
        create_child_node(voltrfs_voltages_parameter, kicker_ukick_parameters)
        
        voltris_voltages_parameter = find_unique_string(device + '/VOLTRIS#voltages$', lh.get_parameters())
        create_child_node(voltris_voltages_parameter, kicker_ukick_parameters)
        
        volttgs_voltages_parameter = find_unique_string(device + '/VOLTTGS#voltages$', lh.get_parameters())
        create_child_node(volttgs_voltages_parameter, kicker_ukick_parameters)

## Bumper
for device in bumper:
    kl_parameter = find_unique_string(device + '/KL$', lh.get_parameters())
    create_child_node(kl_parameter, [ opticsip_parameter, bumper_knob_parameter ])

    bl_parameter = find_unique_string(device + '/BL$', lh.get_parameters())
    create_child_node(bl_parameter, [ brho_parameter, kl_parameter ])

    i_parameter = find_unique_string(device + '/I$', lh.get_parameters())
    create_child_node(i_parameter, bl_parameter )

    currents_currents_parameter = find_unique_string(device + '/CURRENTS#currents$', lh.get_parameters())
    create_child_node(currents_currents_parameter, i_parameter )

    ftimes_ftimes_parameter = find_unique_string(device + '/FTIMES#ftimes$', lh.get_parameters())
    create_child_node(ftimes_ftimes_parameter, tfall_parameter )

    para_reference_parameter = find_unique_string(device + '/PARA#reference_parameters$', lh.get_parameters())
    create_child_node(para_reference_parameter, curvature_parameter )

## SIS18 Bypass
for device in sis18_bypass:
    kl_parameter = find_unique_string(device + '/KLBYP$', lh.get_parameters())
    create_child_node(kl_parameter, opticsip_parameter )

    bl_parameter = find_unique_string(device + '/BLBYP$', lh.get_parameters())
    create_child_node(bl_parameter, kl_parameter )

    i_parameter = find_unique_string(device + '/IBYP$', lh.get_parameters())
    create_child_node(i_parameter, bl_parameter )

    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, i_parameter )

## SIS18 KO
for device in sis18_ko_exiter:
    start_tau_parameter = find_unique_string(device + '/START_TAU$', lh.get_parameters())
    end_tau_parameter = find_unique_string(device + '/END_TAU$', lh.get_parameters())
    start_ampl_parameter = find_unique_string(device + '/START_AMPL$', lh.get_parameters())
    end_ampl_parameter = find_unique_string(device + '/END_AMPL$', lh.get_parameters())
    upp_parameter = find_unique_string(device + '/UPP$', lh.get_parameters())
    create_child_node(upp_parameter, [ start_tau_parameter, end_tau_parameter, start_ampl_parameter, end_ampl_parameter, erho_parameter, tgrid_parameter, bp_length_parameter ])

    uctrl_parameter = find_unique_string(device + '/UCTRL$', lh.get_parameters())
    create_child_node(uctrl_parameter, [ upp_parameter, incorpip_parameter ])

    dqh_parameter = find_unique_string(device + '/DQH$', lh.get_parameters())
    qhfr_parameter = find_unique_string(device + '/QHFR$', lh.get_parameters())
    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', lh.get_parameters())
    create_child_node(rampvals_parameter, [ h_parameter, frev_parameter, dqh_parameter, uctrl_parameter, qhfr_parameter ])

#print ('Parameters that are created: %s\n' % lh.get_parameters());

#keylist = _relations.keys()
#keylist.sort()
#for key in keylist:
#    print (key, _relations[key])


#print ('Relations that are created: %s\n' % _relations);


lh.export()

