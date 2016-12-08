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

# This part will be externalized in a python module and resides here only during prototyping
import json # JSON export
import cx_Oracle
import os

_data = {} # empty dicts
_data ['parameter_types'] = {}
_data ['parameters'] = {}
_data ['parameter_relations'] = {}

def find_devices_by_accelerator(accelerator_name): 
    device_names = []
    
    # open the database to execute the import procedure
    os.environ['NLS_LANG'] = 'German_Germany.UTF8'
    
    # use correct user/name password here
    dbAccDbU = cx_Oracle.connect('LSA_PUB/READONLY@AccDbU')
    dbAccDbUCursor = dbAccDbU.cursor()
    
    dbAccDbUCursor.execute('''SELECT DEVICE_NAME FROM LSA.DEVICES d
        join LSA.ACCELERATOR_ZONES az on (d.ACCELERATOR_ZONE = az.ACCELERATOR_ZONE_ID)
        where az.ACCELERATOR = :accel ''', accel = accelerator_name)
    row_set = dbAccDbUCursor.fetchall()
    if row_set:
        for row in row_set:
            device_names.append(row[0]);
    
    dbAccDbUCursor.close()
    dbAccDbU.close()
    return device_names

def find_devices_by_particle_transfer(particle_transfer_name): 
    device_names = []
    
    # open the database to execute the import procedure
    os.environ['NLS_LANG'] = 'German_Germany.UTF8'
    
    # use correct user/name password here
    dbAccDbU = cx_Oracle.connect('LSA_PUB/READONLY@AccDbU')
    dbAccDbUCursor = dbAccDbU.cursor()
    
    dbAccDbUCursor.execute('''SELECT DEVICE_NAME FROM LSA.DEVICES d
        join LSA.ACCELERATOR_ZONES az on (d.ACCELERATOR_ZONE = az.ACCELERATOR_ZONE_ID)
        join LSA.PART_TRANS_ACC_ZONES ptaz on (az.ACCELERATOR_ZONE_ID = ptaz.ACCELERATOR_ZONE_ID)
        join LSA.PARTICLE_TRANSFERS pt on (pt.PARTICLE_TRANSFER_ID = ptaz.PARTICLE_TRANSFER_ID)
        where pt.PARTICLE_TRANSFER_NAME = :ptn ''', ptn = particle_transfer_name)
    row_set = dbAccDbUCursor.fetchall()
    if row_set:
        for row in row_set:
            device_names.append(row[0]);
    
    dbAccDbUCursor.close()
    dbAccDbU.close()
    return device_names
    
def create_parameter_type(parameter_type_name, value_type, type_category, type_group, display_name=None, unit=None, external=False, hardware=False, expert=False, description='',
                          x_prec=None, y_prec=None, min_value=None, max_value=None, multiplexed=True, function_bproc=True, restorable=True):
    print ('Created parameter type %s' % parameter_type_name)
    parameter_type_attributes = { 'display_name':display_name, 'unit': unit, 'value_type': value_type,
                              'is_external': external, 'is_hardware':hardware, 'is_expert':expert,
                              'description':description, 'parameter_type_category': type_category,
                              'x_prec':x_prec, 'y_prec':y_prec, 'min_value':min_value, 'max_value':max_value,
                              'parameter_type_group_name':type_group, 'is_multiplexed':multiplexed,
                              'belongs_to_function_bproc':function_bproc, 'is_restorable':restorable }
    _data ['parameter_types'] [ parameter_type_name ] = parameter_type_attributes
    
def create_parameter(parameter_name, parameter_type, trimable=True, min_value=None, max_value=None):
    print ('Created parameter %s' % parameter_name)
    parameter_attributes = { 'parameter_type_name' : parameter_type, 'is_trimable' : trimable, 'min_value' : min_value, 'max_value' : max_value }
    _data ['parameters'] [ parameter_name ] = parameter_attributes
    
def create_parameter_relations(parameter_name, parent_parameter_names):
    print ('Parameter %s connected to parents %s' % (parameter_name, parent_parameter_names))
    try:
        _data ['parameter_relations'][ parameter_name ].extend(parent_parameter_names)
    except KeyError:
        _data ['parameter_relations'][ parameter_name ] = parent_parameter_names
        
def create_parameter_from_type(device, parameter_type):
    parameter = device + "/" + parameter_type
    create_parameter(parameter, parameter_type)
    return parameter

# ------------------------ Old methods that should not be used anymore

def create_parameter_by_type(parameter_name, parameter_attributes):
    print ('Created parameter %s with attributes %s\n' %(parameter_name, parameter_attributes))
    create_parameter(parameter_name, parameter_attributes['type'])
    return parameter_name

def create_child_node(parameter_name, parameter_parent_names):
    if (parameter_name == None) or (parameter_parent_names is None):
        return
    if (type(parameter_parent_names) is str):
        create_parameter_relations(parameter_name, [ parameter_parent_names ] )
    else:
        create_parameter_relations(parameter_name, parameter_parent_names )

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


###
# Actual definitions
###   
accelerator = 'SIS100'
particle_transfer = 'SIS100_RING'
hierarchy = 'DEFAULT'
version = '1.0.0'

### Instantiate devices and device groups

# For now, the list of all devices is read from a file. The file used
# here has been created by exporting an SQL query for device names for
# the given particle transfer.
# For the future, it is conceivable that this list could be read
# directly from the data base.
all_devices =  find_devices_by_particle_transfer(particle_transfer)

## Standard beam and logical devices
beam_device = find_unique_string(particle_transfer.replace('_RING', 'BEAM'), all_devices)
optics_device = find_unique_string(particle_transfer.replace('_RING','OPTICS'), all_devices)
orbit_device = find_unique_string(particle_transfer.replace('_RING','ORBIT'), all_devices)
rf_device = find_unique_string(particle_transfer.replace('_RING','RF'), all_devices)
timeparam_device = find_unique_string(particle_transfer.replace('_RING','TIMEPARAM'), all_devices)
kicker_device = find_unique_string(particle_transfer.replace('_RING','KICKER'), all_devices)
#bumper_device = find_unique_string(particle_transfer.replace('_RING','BUMPER'), all_devices)

## Hardware
#hardware_fs_system = find_strings('S00BE_FS$', all_devices)
#hardware_rf_system = find_strings('S00BE_PS$', all_devices)
#tgx_system = find_strings('S00ZGT$', all_devices)
#timing_device = find_strings('S00ZZ$', all_devices)

## Standard device groups
main_dipoles = find_strings('1S00MH$', all_devices)
horizontal_correctors = find_strings('1S[1-6][1-E]KH1$', all_devices)
vertical_correctors = find_strings('1S[1-6][1-E]KV1$', all_devices)

main_quadrupoles = find_strings('1S00QD[12][DF]$', all_devices)
extraction_quadrupoles = find_strings('1S13QS1E$', all_devices)
correction_quadrupoles = find_strings('1S[1-6][1-E]KM1QN$', all_devices)

main_sextupoles = find_strings('(1S00KS[1-3]C[VH]|1S[1-6][1-E]KS1E)$', all_devices)
chromaticity_sextupoles = main_sextupoles[:] # python's shallow copy for lists
resonance_sextupoles = find_strings('1S[1-6][1-E]KS1E$', main_sextupoles)
correction_sextupoles = find_strings('1S[1-6][1-E]KM1SN$', all_devices)

correction_octupoles = find_strings('1S[1-6][1-E]KM1ON$', all_devices) # none for SIS18

#horizontal_correction_coils = find_strings('S[01][0-9]MU[12]A$', all_devices)
#extraction_bump_correction_coils = find_strings('(S((04)|(06))MU1A)|(S((05)|(07)|(10)|(11)|(12))MU2A)', horizontal_correction_coils)
#extra_correction_coils = find_strings('(S((02)|(07)|(08))MU1A)|(S04MU2A)', horizontal_correction_coils)
#horizontal_orbit_correction_coils = list(set(horizontal_correction_coils)-set(extraction_bump_correction_coils))

cavities = find_strings('1S[1-6][1-4]BE[1-2]$', all_devices)

#sis18_cavities_ampl = find_strings('S0[28]BE[12]A$', all_devices)
#sis18_cavities_freq = find_strings('S0[28]BE[12]FS$', all_devices)
#sis18_cavities_phase = find_strings('S0[28]BE[12]P$', all_devices)

#bumper = find_strings('S[01][1-3]MB[1-4]$', all_devices)

kicker = find_strings('1S5[1-3]MK[1-3]E$', all_devices)

q_kicker = find_strings('1S13MK[1-2]Q$', all_devices)

#sis18_bypass = find_strings('S06MU4$', all_devices)

#sis18_ko_exiter = find_strings('S07BO1E$', all_devices)

## Magnet groups according to multipole
all_dipoles = main_dipoles + horizontal_correctors + vertical_correctors
all_quadrupoles = main_quadrupoles + extraction_quadrupoles + correction_quadrupoles
all_sextupoles = main_sextupoles + correction_sextupoles
all_octupoles = correction_octupoles

all_correctors = horizontal_correctors + vertical_correctors

all_multipol_correctors = correction_quadrupoles + correction_sextupoles + correction_octupoles

all_magnets = all_dipoles + all_quadrupoles + all_sextupoles + all_octupoles
main_magnets = main_dipoles + main_quadrupoles

all_kicker = kicker + q_kicker

### Creation of parameters

## Hardware rf system parameters
#for device in hardware_fs_system:
#    hardware_fs_rampvals_parameter = create_parameter_from_type(device, 'RAMPVALS#data')

#for device in hardware_rf_system:
#    mhbpar_damp1_parameter = create_parameter_from_type(device, 'MHBPAR#DAmp1')
#    mhbpar_damp2_parameter = create_parameter_from_type(device, 'MHBPAR#DAmp2')
#    mhbpar_delay_parameter = create_parameter_from_type(device, 'MHBPAR#Delay')
#    mhbpar_harm1_parameter = create_parameter_from_type(device, 'MHBPAR#Harm1')
#    mhbpar_harm2_parameter = create_parameter_from_type(device, 'MHBPAR#Harm2')
#    syncmode_hfssync_parameter = create_parameter_from_type(device, 'SYNCMODE#hfssync')
#    workmode_workmode_parameter = create_parameter_from_type(device, 'WORKMODE#workmode')

#for device in tgx_system:
#    delay_trgdelay_parameter = create_parameter_from_type(device, 'DELAY')
#    harmonic_harmonic_parameter = create_parameter_from_type(device, 'HARMONIC')
#    mode_kickmode_parameter = create_parameter_from_type(device, 'MODE')
#    rftrig_rftrig_parameter = create_parameter_from_type(device, 'RFTRIG')

#for device in timing_device:
#    chansequ_chancount_parameter = create_parameter_from_type(device, 'CHANSEQU#chanCount')
#    chansequ_chansequ_parameter = create_parameter_from_type(device, 'CHANSEQU#chanSequ')
#    evtarray_chanarray_parameter = create_parameter_from_type(device, 'EVTARRAY#chanArray')
#    timeout_unilac_parameter = create_parameter(device + '/TIMEOUT_UNILAC', {'type' : 'SCALAR_TIMEOUT_UNILAC'})
#    tmeasure_parameter = create_parameter(device + '/TMEASURE', {'type' : 'SCALAR_TMEASURE'})
#    toffset_unilac_parameter = create_parameter(device + '/TOFFSET_UNILAC', {'type' : 'SCALAR_TOFFSET_UNILAC'})


## Beam parameters
a_parameter = create_parameter_by_type(beam_device + '/A', {'type' : 'SCALAR_A'})
alphac_parameter = create_parameter_from_type(beam_device, 'ALPHAC')
aoq_parameter = create_parameter_by_type(beam_device + '/AOQ', {'type' : 'SCALAR_AOQ'})
brho_parameter = create_parameter_from_type(beam_device, 'BRHO')
brhodot_parameter = create_parameter_from_type(beam_device, 'BRHODOT')
brho_start_end_parameter = create_parameter_by_type(beam_device + '/BRHO_START_END', {'type' : 'SCALAR_BRHO'})
bucketfill_parameter = create_parameter_by_type(beam_device + '/BUCKETFILL', {'type' : 'SCALAR_BUCKETFILL'})
bunchfactor_parameter = create_parameter_from_type(beam_device, 'BUNCHFACTOR')
bunchpattern_parameter = create_parameter_by_type(beam_device + '/BUNCHPATTERN', {'type' : 'SCALAR_BUNCHPATTERN'})
ch_parameter = create_parameter_from_type(beam_device, 'CH')
cv_parameter = create_parameter_from_type(beam_device, 'CV')
deltar_parameter = create_parameter_from_type(beam_device, 'DELTAR')
#dp_over_p_parameter = create_parameter(beam_device + '/DP_OVER_P', {'type' : 'SCALAR_DP_OVER_P'})
e_parameter = create_parameter_by_type(beam_device + '/E', {'type' : 'SCALAR_E'})
element_parameter = create_parameter_by_type(beam_device + '/ELEMENT', {'type' : 'SCALAR_ELEMENT'})
erho_parameter = create_parameter_from_type(beam_device, 'ERHO')
eta_parameter = create_parameter_from_type(beam_device, 'ETA')
frev_parameter = create_parameter_from_type(beam_device, 'FREV')
gamma_parameter = create_parameter_from_type(beam_device, 'GAMMA')
geofact_parameter = create_parameter_from_type(beam_device, 'GEOFACT')
h_parameter = create_parameter_by_type(beam_device + '/H', {'type' : 'SCALAR_H'})
inj_emih_parameter = create_parameter_by_type(beam_device + '/INJ_EMIH', {'type' : 'SCALAR_INJ_EMIH'})
inj_emil_parameter = create_parameter_by_type(beam_device + '/INJ_EMIL', {'type' : 'SCALAR_INJ_EMIL'})
inj_emiv_parameter = create_parameter_by_type(beam_device + '/INJ_EMIV', {'type' : 'SCALAR_INJ_EMIV'})
isotope_parameter = create_parameter_by_type(beam_device + '/ISOTOPE', {'type' : 'SCALAR_ISOTOPE'})
kl_ampl_parameter = create_parameter_by_type(beam_device + '/KL_AMPL', {'type' : 'SCALAR_KL_AMPL'})
kl_harm_parameter = create_parameter_by_type(beam_device + '/KL_HARM', {'type' : 'SCALAR_KL_HARM'})
kl_offset_parameter = create_parameter_by_type(beam_device + '/KL_OFFSET', {'type' : 'SCALAR_KL_OFFSET'})
kl_phase_parameter = create_parameter_by_type(beam_device + '/KL_PHASE', {'type' : 'SCALAR_KL_PHASE'})
maxrh_parameter = create_parameter_from_type(beam_device, 'MAXRH')
maxrv_parameter = create_parameter_from_type(beam_device, 'MAXRV')
nparticles_parameter = create_parameter_by_type(beam_device + '/NPARTICLES', {'type' : 'SCALAR_NPARTICLES'})
nperbunch_parameter = create_parameter_by_type(beam_device + '/NPERBUNCH', {'type' : 'SCALAR_NPERBUNCH'})
phis_parameter = create_parameter_from_type(beam_device, 'PHIS')
q_parameter = create_parameter_by_type(beam_device + '/Q', {'type' : 'SCALAR_Q'})
qh_parameter = create_parameter_from_type(beam_device, 'QH')
qv_parameter = create_parameter_from_type(beam_device, 'QV')
tbunch_parameter = create_parameter_by_type(beam_device + '/TBUNCH', {'type' : 'SCALAR_TBUNCH'})
trev_parameter = create_parameter_from_type(beam_device, 'TREV')

## RF parameters
abkt_parameter = create_parameter_from_type(rf_device, 'ABKT')
dualh_parameter = create_parameter_by_type(rf_device + '/DUALH', {'type' : 'SCALAR_DUALH'})
dualhip_parameter = create_parameter_from_type(rf_device, 'DUALHIP')
frfring_parameter = create_parameter_from_type(rf_device, 'FRFRING')
rf_mode_parameter = create_parameter_by_type(rf_device + '/MODE', {'type' : 'SCALAR_CAVITY_MODE'})
prfring_parameter = create_parameter_from_type(rf_device, 'PRFRING')
urfring_parameter = create_parameter_from_type(rf_device, 'URFRING')
urfsc_parameter = create_parameter_from_type(rf_device, 'URFSC')

for device in cavities:
    create_parameter_by_type(device + '/URF',    {'type' : 'URF'})
    create_parameter_by_type(device + '/FRF',    {'type' : 'FRF'})
    create_parameter_by_type(device + '/PRF',    {'type' : 'PRF'})

#for device in sis18_cavities_ampl:
#    create_parameter(device + '/URF',    {'type' : 'URF'})
#    create_parameter(device + '/RAMPVALS#data',    {'type' : 'RAMPVALS#data'})
#    create_parameter(device + '/BROTAMPL#highValue',    {'type' : 'BROTAMPL#highValue'})


#for device in sis18_cavities_freq:
#    create_parameter(device + '/FRF',    {'type' : 'FRF'})
#    create_parameter(device + '/RAMPVALS#data',    {'type' : 'RAMPVALS#data'})

#for device in sis18_cavities_phase:
#    create_parameter(device + '/PRF',    {'type' : 'PRF'})
#    create_parameter(device + '/RAMPVALS#data',    {'type' : 'RAMPVALS#data'})

## Optics parameters
#ext_sigma_parameter = create_parameter(optics_device + '/EXT_SIGMA', {'type' : 'SCALAR_EXT_SIGMA'})
opticsip_parameter = create_parameter_from_type(optics_device, 'OPTICSIP')
#sigma_parameter = create_parameter_from_type(optics_device, 'SIGMA')
#tau_parameter = create_parameter_from_type(optics_device, 'TAU')
#tau_endpoint_parameter = create_parameter(optics_device + '/TAU_ENDPOINT', {'type' : 'SCALAR_TAU_ENDPOINT'})
#tau_nlp_parameter = create_parameter(optics_device + '/TAU_NLP', {'type' : 'SCALAR_TAU_NLP'})
tau_start_end_parameter = create_parameter_by_type(optics_device + '/TAU_START_END', {'type' : 'SCALAR_TAU'})

## Orbit parameters
#coh01_parameter = create_parameter(orbit_device + '/COH01', {'type' : 'ORBITBUMP'})
#coh02_parameter = create_parameter(orbit_device + '/COH02', {'type' : 'ORBITBUMP'})
#coh03_parameter = create_parameter(orbit_device + '/COH03', {'type' : 'ORBITBUMP'})
#coh04_parameter = create_parameter(orbit_device + '/COH04', {'type' : 'ORBITBUMP'})
#coh05_parameter = create_parameter(orbit_device + '/COH05', {'type' : 'ORBITBUMP'})
#coh06_parameter = create_parameter(orbit_device + '/COH06', {'type' : 'ORBITBUMP'})
#coh07_parameter = create_parameter(orbit_device + '/COH07', {'type' : 'ORBITBUMP'})
#coh08_parameter = create_parameter(orbit_device + '/COH08', {'type' : 'ORBITBUMP'})
#coh09_parameter = create_parameter(orbit_device + '/COH09', {'type' : 'ORBITBUMP'})
#coh10_parameter = create_parameter(orbit_device + '/COH10', {'type' : 'ORBITBUMP'})
#coh11_parameter = create_parameter(orbit_device + '/COH11', {'type' : 'ORBITBUMP'})
#coh12_parameter = create_parameter(orbit_device + '/COH12', {'type' : 'ORBITBUMP'})
#cov01_parameter = create_parameter(orbit_device + '/COV01', {'type' : 'ORBITBUMP'})
#cov02_parameter = create_parameter(orbit_device + '/COV02', {'type' : 'ORBITBUMP'})
#cov03_parameter = create_parameter(orbit_device + '/COV03', {'type' : 'ORBITBUMP'})
#cov04_parameter = create_parameter(orbit_device + '/COV04', {'type' : 'ORBITBUMP'})
#cov05_parameter = create_parameter(orbit_device + '/COV05', {'type' : 'ORBITBUMP'})
#cov06_parameter = create_parameter(orbit_device + '/COV06', {'type' : 'ORBITBUMP'})
#cov07_parameter = create_parameter(orbit_device + '/COV07', {'type' : 'ORBITBUMP'})
#cov08_parameter = create_parameter(orbit_device + '/COV08', {'type' : 'ORBITBUMP'})
#cov09_parameter = create_parameter(orbit_device + '/COV09', {'type' : 'ORBITBUMP'})
#cov10_parameter = create_parameter(orbit_device + '/COV10', {'type' : 'ORBITBUMP'})
#cov11_parameter = create_parameter(orbit_device + '/COV11', {'type' : 'ORBITBUMP'})
#cov12_parameter = create_parameter(orbit_device + '/COV12', {'type' : 'ORBITBUMP'})
#extesep_parameter = create_parameter(orbit_device + '/EXTESEP', {'type' : 'FLATBUMP'})
#extmsep_parameter = create_parameter(orbit_device + '/EXTMSEP', {'type' : 'FLATBUMP'})

#coh_list = [coh01_parameter, coh02_parameter, coh03_parameter, coh04_parameter, coh05_parameter, coh06_parameter, coh07_parameter, coh08_parameter, coh09_parameter, coh10_parameter, coh11_parameter, coh12_parameter]

#cov_list = [cov01_parameter, cov02_parameter, cov03_parameter, cov04_parameter, cov05_parameter, cov06_parameter, cov07_parameter, cov08_parameter, cov09_parameter, cov10_parameter, cov11_parameter, cov12_parameter]

## Timeparam parameters
bdot_parameter = create_parameter_by_type(timeparam_device + '/BDOT', {'type' : 'SCALAR_BDOT'})
bp_length_parameter = create_parameter_by_type(timeparam_device + '/BP_LENGTH', {'type' : 'SCALAR_BP_LENGTH'})
incorpip_parameter = create_parameter_from_type(timeparam_device, 'INCORPIP')
tgrid_parameter = create_parameter_by_type(timeparam_device + '/TGRID', {'type' : 'SCALAR_TGRID'})
tround_parameter = create_parameter_by_type(timeparam_device + '/TROUND', {'type' : 'SCALAR_TROUND'})
t_bp_length_parameter = create_parameter_by_type(timeparam_device + '/T_BP_LENGTH', {'type' : 'SCALAR_T_BP_LENGTH'})
t_wait_parameter = create_parameter_by_type(timeparam_device + '/T_WAIT', {'type' : 'SCALAR_T_WAIT'})


## Kicker parameters
kicker_knob_parameter = create_parameter_by_type(kicker_device + '/KNOB', {'type' : 'SCALAR_KICKER_KNOB'})
kicker_mode_parameter = create_parameter_by_type(kicker_device + '/MODE', {'type' : 'SCALAR_KICKER_MODE'})
nbunch1_parameter = create_parameter_by_type(kicker_device + '/NBUNCH1', {'type' : 'SCALAR_NBUNCH1'})
start_parameter = create_parameter_by_type(kicker_device + '/START', {'type' : 'SCALAR_KICKER_START'})
thigh1_parameter = create_parameter_by_type(kicker_device + '/THIGH1', {'type' : 'SCALAR_KICKER_THIGH1'})
thigh2_parameter = create_parameter_by_type(kicker_device + '/THIGH2', {'type' : 'SCALAR_KICKER_THIGH2'})
toffset1_parameter = create_parameter_by_type(kicker_device + '/TOFFSET1', {'type' : 'SCALAR_KICKER_TOFFSET1'})
toffset2_parameter = create_parameter_by_type(kicker_device + '/TOFFSET2', {'type' : 'SCALAR_KICKER_TOFFSET2'})

kicker_ext_kick_parameter = create_parameter_by_type(kicker_device + '/EXT_KICK', {'type' : 'SCALAR_EXT_KICK'})
kicker_qh_kick_parameter = create_parameter_by_type(kicker_device + '/QH_KICK', {'type' : 'SCALAR_Q_KICK'})
kicker_qv_kick_parameter = create_parameter_by_type(kicker_device + '/QV_KICK', {'type' : 'SCALAR_Q_KICK'})

## Bumper parameters
#curvature_parameter = create_parameter(bumper_device + '/CURVATURE', {'type' : 'SCALAR_BUMPER_CURVATURE'})
#bumper_knob_parameter = create_parameter(bumper_device + '/KNOB', {'type' : 'SCALAR_BUMPER_KNOB'})
#tfall_parameter = create_parameter(bumper_device + '/TFALL', {'type' : 'SCALAR_TFALL'})


for device in all_dipoles:
    create_parameter_by_type(device + '/KL',    {'type' : 'K0L'})
    create_parameter_by_type(device + '/BL',    {'type' : 'B0L'})

for device in all_quadrupoles:
    create_parameter_by_type(device + '/KL',    {'type' : 'K1L'})
    create_parameter_by_type(device + '/BL',    {'type' : 'B1L'})

for device in all_sextupoles:
    create_parameter_by_type(device + '/KLDELTA', {'type' : 'DELTA_K2L'})
    create_parameter_by_type(device + '/KL',    {'type' : 'K2L'})
    create_parameter_by_type(device + '/BL',    {'type' : 'B2L'})

for device in all_octupoles:
    create_parameter_by_type(device + '/KL',    {'type' : 'K3L'})
    create_parameter_by_type(device + '/BL',    {'type' : 'B3L'})

for device in all_kicker:
    create_parameter_by_type(device + '/KL',    {'type' : 'SCALAR_K0L'})
    create_parameter_by_type(device + '/BL',    {'type' : 'SCALAR_B0L'})
    create_parameter_by_type(device + '/UKICK',    {'type' : 'SCALAR_UKICK'})
#    create_parameter(device + '/TIMDELRF#time',    {'type' : 'TIMDELRF#time'})
#    create_parameter(device + '/TIMDELTG#time',    {'type' : 'TIMDELTG#time'})
#    create_parameter(device + '/TIMFTRF#time',    {'type' : 'TIMFTRF#time'})
#    create_parameter(device + '/TIMFTTG#time',    {'type' : 'TIMFTTG#time'})
#    create_parameter(device + '/VOLTRFS#voltages',    {'type' : 'VOLTRFS#voltages'})
#    create_parameter(device + '/VOLTRIS#voltages',    {'type' : 'VOLTRIS#voltages'})
#    create_parameter(device + '/VOLTTGS#voltages',    {'type' : 'VOLTTGS#voltages'})


#for device in bumper:
#    create_parameter(device + '/KL',    {'type' : 'SCALAR_K0L'})
#    create_parameter(device + '/BL',    {'type' : 'SCALAR_B0L'})
#    create_parameter(device + '/I',    {'type' : 'SCALAR_I'})
#    create_parameter(device + '/CURRENTS#currents',    {'type' : 'CURRENTS#currents'})
#    create_parameter(device + '/FTIMES#ftimes',    {'type' : 'FTIMES#ftimes'})
#    create_parameter(device + '/PARA#reference_parameters',    {'type' : 'PARA#reference_parameters'})


#for device in extraction_bump_correction_coils:
#    create_parameter(device + '/KL',    {'type' : 'FLAT_K0L'})

#for device in horizontal_orbit_correction_coils:
#    create_parameter(device + '/KL',    {'type' : 'K0L'})

#for device in horizontal_correction_coils:
#    create_parameter(device + '/BLCORR',    {'type' : 'CORR_B0L'})    
#    create_parameter(device + '/ICORR',    {'type' : 'ICORR'})    
#    create_parameter(device + '/RAMPVALS#data', {'type' : 'RAMPVALS#data'})

#for device in extra_correction_coils:
#    create_parameter(device + '/ICORRDOT',    {'type' : 'ICORRDOT'})
#    create_parameter(device + '/UCORR',    {'type' : 'UCORR'})

for device in all_magnets:
    create_parameter_from_type(device, 'I')
    create_parameter_from_type(device, 'RAMPVALS#data')

for device in main_magnets:
    create_parameter_from_type(device, 'IDOT')
    create_parameter_from_type(device, 'UEDDY')
    create_parameter_from_type(device, 'U')

#for device in sis18_bypass:
#    create_parameter_from_type(device, 'KLBYP')
#    create_parameter_from_type(device, 'BLBYP')
#    create_parameter_from_type(device, 'IBYP')
#    create_parameter_from_type(device, 'RAMPVALS#data')

#for device in sis18_ko_exiter:
#    create_parameter(device + '/DQH',    {'type' : 'SCALAR_DQHKO'})
#    create_parameter(device + '/QHFR',    {'type' : 'SCALAR_QHFRKO'})
#    create_parameter(device + '/START_TAU',    {'type' : 'SCALAR_START_TAUKO'})
#    create_parameter(device + '/END_TAU',    {'type' : 'SCALAR_END_TAUKO'})
#    create_parameter(device + '/START_AMPL',    {'type' : 'SCALAR_START_AMPLKO'})
#    create_parameter(device + '/END_AMPL',    {'type' : 'SCALAR_END_AMPLKO'})
#    create_parameter_from_type(device, 'UPP')
#    create_parameter_from_type(device, 'UCTRL')
#    create_parameter_from_type(device, 'RAMPVALS#data')

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
#SIS18
#create_child_node(inj_emil_parameter, [ dp_over_p_parameter, e_parameter, h_parameter ])
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
#SIS18
#create_child_node(opticsip_parameter, [ sigma_parameter, tau_parameter, incorpip_parameter ])
#create_child_node(sigma_parameter, [ brho_start_end_parameter, ext_sigma_parameter, bp_length_parameter, t_wait_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])
#create_child_node(tau_parameter, [ tau_nlp_parameter, tau_start_end_parameter, bp_length_parameter, t_wait_parameter, brho_start_end_parameter, tround_parameter, tgrid_parameter, tau_endpoint_parameter ])

#SIS100
create_child_node(opticsip_parameter, [ tau_start_end_parameter, incorpip_parameter, tgrid_parameter, tround_parameter, t_wait_parameter, gamma_parameter ])

## Orbit Parameters
#create_child_node(coh01_parameter, incorpip_parameter )
#create_child_node(coh02_parameter, incorpip_parameter )
#create_child_node(coh03_parameter, incorpip_parameter )
#create_child_node(coh04_parameter, incorpip_parameter )
#create_child_node(coh05_parameter, incorpip_parameter )
#create_child_node(coh06_parameter, incorpip_parameter )
#create_child_node(coh07_parameter, incorpip_parameter )
#create_child_node(coh08_parameter, incorpip_parameter )
#create_child_node(coh09_parameter, incorpip_parameter )
#create_child_node(coh10_parameter, incorpip_parameter )
#create_child_node(coh11_parameter, incorpip_parameter )
#create_child_node(coh12_parameter, incorpip_parameter )
#create_child_node(cov01_parameter, incorpip_parameter )
#create_child_node(cov02_parameter, incorpip_parameter )
#create_child_node(cov03_parameter, incorpip_parameter )
#create_child_node(cov04_parameter, incorpip_parameter )
#create_child_node(cov05_parameter, incorpip_parameter )
#create_child_node(cov06_parameter, incorpip_parameter )
#create_child_node(cov07_parameter, incorpip_parameter )
#create_child_node(cov08_parameter, incorpip_parameter )
#create_child_node(cov09_parameter, incorpip_parameter )
#create_child_node(cov10_parameter, incorpip_parameter )
#create_child_node(cov11_parameter, incorpip_parameter )
#create_child_node(cov12_parameter, incorpip_parameter )
#create_child_node(extesep_parameter, incorpip_parameter )
#create_child_node(extmsep_parameter, incorpip_parameter )

## Timeparam Parameters
##SIS18
#create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, ext_sigma_parameter, tau_start_end_parameter, tround_parameter, bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
##SIS100
create_child_node(bp_length_parameter, [ t_bp_length_parameter, t_wait_parameter, tau_start_end_parameter, tround_parameter, bdot_parameter, brho_start_end_parameter, tgrid_parameter ])
create_child_node(incorpip_parameter, bp_length_parameter )

## Kicker Parameters
create_child_node(thigh1_parameter, [ nbunch1_parameter, tbunch_parameter, h_parameter ])
create_child_node(thigh2_parameter, [ tbunch_parameter, h_parameter, nbunch1_parameter ])
create_child_node(toffset2_parameter, [ toffset1_parameter, thigh1_parameter ])

## Hardware rf system parameters
#create_child_node(hardware_fs_rampvals_parameter, frev_parameter)

#create_child_node(mhbpar_damp1_parameter, h_parameter )
#create_child_node(mhbpar_damp2_parameter, h_parameter )
#create_child_node(mhbpar_delay_parameter, h_parameter )
#create_child_node(mhbpar_harm1_parameter, h_parameter )
#create_child_node(mhbpar_harm2_parameter, h_parameter )
#create_child_node(syncmode_hfssync_parameter, h_parameter )
#create_child_node(workmode_workmode_parameter, h_parameter )

#create_child_node(delay_trgdelay_parameter, [ tbunch_parameter, h_parameter, start_parameter ])
#create_child_node(harmonic_harmonic_parameter, h_parameter )
#create_child_node(mode_kickmode_parameter, [ kicker_mode_parameter, nbunch1_parameter, h_parameter ])
#create_child_node(rftrig_rftrig_parameter, h_parameter )

#create_child_node(chansequ_chancount_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter, kicker_mode_parameter ])
#create_child_node(chansequ_chansequ_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter, kicker_mode_parameter ])
#create_child_node(evtarray_chanarray_parameter, [timeout_unilac_parameter, tmeasure_parameter, toffset_unilac_parameter, bp_length_parameter, kicker_mode_parameter ])

## Horizontal_orbit_correction_coils
#horizontal_orbit_correction_coils.sort()
#for device in horizontal_orbit_correction_coils:
#    kl_parameter = find_unique_string(device + '/K[0-3]?L$', _data ['parameters'])
#    sector = int(device[1:3])
#    index = sector - 1
#    if (sector == 5) :
#       create_child_node(kl_parameter, [ extesep_parameter, opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
#    elif (sector == 7) :
#       create_child_node(kl_parameter, [ extmsep_parameter, opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])
#    else:
#       create_child_node(kl_parameter, [ opticsip_parameter, coh_list[index], coh_list[index - 1], coh_list[index - 2] ])

## Extraction_bump_correction_coils
#for device in extraction_bump_correction_coils:
#    kl_parameter = find_unique_string(device + '/K[0-3]?L$', _data ['parameters'])
#    sector = int(device[1:3])
#    if ((sector == 10) | (sector == 11) | (sector == 12)) :
#       create_child_node(kl_parameter, opticsip_parameter)
#    elif ((sector == 4) | (sector == 5)) :
#       create_child_node(kl_parameter, [ opticsip_parameter, extesep_parameter ])
#    else:
#       create_child_node(kl_parameter, [ opticsip_parameter, extmsep_parameter ])

## Magnets
for device in all_magnets:
    bl_parameter = find_unique_string(device + '/B[0-3]?L$', _data ['parameters'])
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', _data ['parameters'])
    create_child_node(bl_parameter, [ brho_parameter, kl_parameter, incorpip_parameter])

for device in all_dipoles:
    bl_parameter = find_unique_string(device + '/B[0-3]?L$', _data ['parameters'])
    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
    create_child_node(i_parameter, bl_parameter)

for device in main_dipoles:
    kl_parameter = find_unique_string(device + '/K0?L$', _data ['parameters'])
    create_child_node(kl_parameter, opticsip_parameter )

for device in extraction_quadrupoles:
    kl_parameter = find_unique_string(device + '/K0?L$', _data ['parameters'])
    create_child_node(kl_parameter, opticsip_parameter )

    bl_parameter = find_unique_string(device + '/B[0-3]?L$', _data ['parameters'])
    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
    create_child_node(i_parameter, bl_parameter)

for device in main_quadrupoles:
    kl_parameter = find_unique_string(device + '/K1?L$', _data ['parameters'])
    create_child_node(kl_parameter, [ qh_parameter, qv_parameter, opticsip_parameter ])

for device in main_sextupoles:
#    kldelta_parameter = find_unique_string(device + '/KLDELTA$', _data ['parameters'])
#    create_child_node(kldelta_parameter, [ incorpip_parameter, kl_harm_parameter, kl_phase_parameter, kl_ampl_parameter, kl_offset_parameter ])

#    kl_parameter = find_unique_string(device + '/K2?L$', _data ['parameters'])    
#    create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter, kldelta_parameter ]) 

    bl_parameter = find_unique_string(device + '/B[0-3]?L$', _data ['parameters'])
    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
    create_child_node(i_parameter, bl_parameter)

#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, i_parameter ) 

for device in all_multipol_correctors:
    kl_parameter = find_unique_string(device + '/K[1-3]?L$', _data ['parameters'])
    create_child_node(kl_parameter, opticsip_parameter )

    bl_parameter = find_unique_string(device + '/B[1-3]?L$', _data ['parameters'])
    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
    create_child_node(i_parameter, bl_parameter)

#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, i_parameter)

for device in chromaticity_sextupoles:
    kl_parameter = find_unique_string(device + '/K2?L$', _data ['parameters'])
    create_child_node(kl_parameter, [ ch_parameter, cv_parameter, opticsip_parameter ])

for device in main_magnets:
    bl_parameter = find_unique_string(device + '/B[0-3]?L$', _data ['parameters'])
    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
    create_child_node(i_parameter, bl_parameter)

    idot_parameter = find_unique_string(device + '/IDOT$', _data ['parameters'])
    create_child_node(idot_parameter, i_parameter)

    ueddy_parameter = find_unique_string(device + '/UEDDY$', _data ['parameters'])
    u_parameter = find_unique_string(device + '/U$', _data ['parameters'])
    create_child_node(ueddy_parameter, idot_parameter )   
    create_child_node(u_parameter, [ ueddy_parameter, idot_parameter ])

#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, [ u_parameter, i_parameter ])

for device in all_correctors:
    kl_parameter = find_unique_string(device + '/K[0-3]?L$', _data ['parameters'])
#    sector = int(device[1:3])
#    index = sector - 1
#    create_child_node(kl_parameter, [ opticsip_parameter, cov_list[index], coh_list[index - 1], coh_list[index + 1 - len(cov_list)] ])
    create_child_node(kl_parameter, opticsip_parameter )

#    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, i_parameter)

#for device in horizontal_correction_coils:
#    kl_parameter = find_unique_string(device + '/K[0-3]?L$', _data ['parameters'])
#    blcorr_parameter = find_unique_string(device + '/B[0-3]?LCORR$', _data ['parameters'])
#    icorr_parameter = find_unique_string(device + '/ICORR$', _data ['parameters'])
#    create_child_node(blcorr_parameter, [ brho_parameter, kl_parameter, incorpip_parameter ])

#    for dipol_device in main_dipoles:
#        i_parameter = find_unique_string(dipol_device + '/I$', _data ['parameters'])
#        bl_parameter = find_unique_string(dipol_device + '/B[0-3]?L$', _data ['parameters'])
#        create_child_node(icorr_parameter, [ i_parameter, blcorr_parameter, bl_parameter ])

#for device in extra_correction_coils:
#    icorr_parameter = find_unique_string(device + '/ICORR$', _data ['parameters'])
#    icorrdot_parameter = find_unique_string(device + '/ICORRDOT$', _data ['parameters'])
#    ucorr_parameter = find_unique_string(device + '/UCORR$', _data ['parameters'])
#    create_child_node(icorrdot_parameter, icorr_parameter )

#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, [ icorr_parameter, ucorr_parameter ])
    
#    for dipol_device in main_dipoles:
#        idot_parameter = find_unique_string(dipol_device + '/IDOT$', _data ['parameters'])
#        create_child_node(ucorr_parameter, [ icorrdot_parameter, idot_parameter ])

#for device in list(set(horizontal_correction_coils) - set(extra_correction_coils)):
#    icorr_parameter = find_unique_string(device + '/ICORR$', _data ['parameters'])
#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, icorr_parameter)

#for device in correction_sextupoles:
#    kl_parameter = find_unique_string(device + '/K[0-3]?L$', _data ['parameters'])
#    create_child_node(kl_parameter, opticsip_parameter)

#    bl_parameter = find_unique_string(device + '/B[0-3]?L$', _data ['parameters'])
#    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
#    create_child_node(i_parameter, bl_parameter)

#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, i_parameter)

for device in resonance_sextupoles:
    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, i_parameter)


## Cavities
for device in cavities:
    urf_parameter = find_unique_string(device + '/URF$', _data ['parameters'])
    create_child_node(urf_parameter, [ h_parameter, incorpip_parameter, urfring_parameter, rf_mode_parameter ])

    frf_parameter = find_unique_string(device + '/FRF$', _data ['parameters'])
    create_child_node(frf_parameter, [ h_parameter, incorpip_parameter, frfring_parameter, rf_mode_parameter ])

    prf_parameter = find_unique_string(device + '/PRF$', _data ['parameters'])
    create_child_node(prf_parameter, [ h_parameter, incorpip_parameter, prfring_parameter, rf_mode_parameter ])

#for device in sis18_cavities_ampl:
#    urf_parameter = find_unique_string(device[:-1] + 'A/URF$', _data ['parameters'])
#    create_child_node(urf_parameter, [ h_parameter, incorpip_parameter, urfring_parameter, rf_mode_parameter ])
#    rampvals_a_parameter = find_unique_string(device[:-1] + 'A/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_a_parameter, urf_parameter )

#    frf_parameter = find_unique_string(device[:-1] + 'FS/FRF$', _data ['parameters'])
#    create_child_node(frf_parameter, [ h_parameter, incorpip_parameter, frfring_parameter, rf_mode_parameter ])
#    rampvals_fs_parameter = find_unique_string(device[:-1] + 'FS/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_fs_parameter, urf_parameter )

#    prf_parameter = find_unique_string(device[:-1] + 'P/PRF$', _data ['parameters'])
#    create_child_node(prf_parameter, [ h_parameter, incorpip_parameter, prfring_parameter, rf_mode_parameter ])
#    rampvals_p_parameter = find_unique_string(device[:-1] + 'P/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_p_parameter, urf_parameter )

#    brotampl_parameter = find_unique_string(device[:-1] + 'A/BROTAMPL#highValue$', _data ['parameters'])
#    create_child_node(brotampl_parameter, urf_parameter )

#kicker_ukick_parameters = ('[')
#for device in kicker:
#    ukick_parameter = find_unique_string(device + '/UKICK$', _data ['parameters'])
#    kicker_ukick_parameters = kicker_ukick_parameters + '\'' + ukick_parameter + '\','

#kicker_ukick_parameters = kicker_ukick_parameters[:-1] + ']'

## Kicker
kicker.sort()
for device in kicker:
    kl_parameter = find_unique_string(device + '/KL$', _data ['parameters'])
    create_child_node(kl_parameter, [ kicker_ext_kick_parameter, opticsip_parameter ])

    bl_parameter = find_unique_string(device + '/BL$', _data ['parameters'])
    create_child_node(bl_parameter, [ brho_parameter, kl_parameter ])

    ukick_parameter = find_unique_string(device + '/UKICK$', _data ['parameters'])
    create_child_node(ukick_parameter, bl_parameter )

#    if (device == kicker[0]):
#       timdelrf_time_parameter = find_unique_string(device + '/TIMDELRF#time$', _data ['parameters'])
#       create_child_node(timdelrf_time_parameter, toffset1_parameter )

#       timdeltg_time_parameter = find_unique_string(device + '/TIMDELTG#time$', _data ['parameters'])
#       create_child_node(timdeltg_time_parameter, toffset2_parameter )

#       timftrf_time_parameter = find_unique_string(device + '/TIMFTRF#time$', _data ['parameters'])
#       create_child_node(timftrf_time_parameter, [ toffset1_parameter, thigh1_parameter ])

#       timfttg_time_parameter = find_unique_string(device + '/TIMFTTG#time$', _data ['parameters'])
#       create_child_node(timfttg_time_parameter, [ toffset2_parameter, thigh2_parameter ])

#       voltrfs_voltages_parameter = find_unique_string(device + '/VOLTRFS#voltages$', _data ['parameters'])
#       create_child_node(voltrfs_voltages_parameter, kicker_ukick_data ['parameters'])

#       voltris_voltages_parameter = find_unique_string(device + '/VOLTRIS#voltages$', _data ['parameters'])
#       create_child_node(voltris_voltages_parameter, kicker_ukick_data ['parameters'])

#       volttgs_voltages_parameter = find_unique_string(device + '/VOLTTGS#voltages$', _data ['parameters'])
#       create_child_node(volttgs_voltages_parameter, kicker_ukick_data ['parameters'])

for device in q_kicker:
    kl_parameter = find_unique_string(device + '/KL$', _data ['parameters'])
    
    number = int(device[6:7])
    if(number == 1):
        create_child_node(kl_parameter, [ opticsip_parameter, kicker_qh_kick_parameter ])
    else:
        create_child_node(kl_parameter, [ opticsip_parameter, kicker_qv_kick_parameter ])

    bl_parameter = find_unique_string(device + '/BL$', _data ['parameters'])
    create_child_node(bl_parameter, [ brho_parameter, kl_parameter ])

    ukick_parameter = find_unique_string(device + '/UKICK$', _data ['parameters'])
    create_child_node(ukick_parameter, bl_parameter )
    
## Bumper
#for device in bumper:
#    kl_parameter = find_unique_string(device + '/KL$', _data ['parameters'])
#    create_child_node(kl_parameter, [ opticsip_parameter, bumper_knob_parameter ])

#    bl_parameter = find_unique_string(device + '/BL$', _data ['parameters'])
#    create_child_node(bl_parameter, [ brho_parameter, kl_parameter ])

#    i_parameter = find_unique_string(device + '/I$', _data ['parameters'])
#    create_child_node(i_parameter, bl_parameter )

#    currents_currents_parameter = find_unique_string(device + '/CURRENTS#currents$', _data ['parameters'])
#    create_child_node(currents_currents_parameter, i_parameter )

#    ftimes_ftimes_parameter = find_unique_string(device + '/FTIMES#ftimes$', _data ['parameters'])
#    create_child_node(ftimes_ftimes_parameter, tfall_parameter )

#    para_reference_parameter = find_unique_string(device + '/PARA#reference_parameters$', _data ['parameters'])
#    create_child_node(para_reference_parameter, curvature_parameter )

## SIS18 Bypass
#for device in sis18_bypass:
#    kl_parameter = find_unique_string(device + '/KLBYP$', _data ['parameters'])
#    create_child_node(kl_parameter, opticsip_parameter )

#    bl_parameter = find_unique_string(device + '/BLBYP$', _data ['parameters'])
#    create_child_node(bl_parameter, kl_parameter )

#    i_parameter = find_unique_string(device + '/IBYP$', _data ['parameters'])
#    create_child_node(i_parameter, bl_parameter )

#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, i_parameter )

## SIS18 KO
#for device in sis18_ko_exiter:
#    start_tau_parameter = find_unique_string(device + '/START_TAU$', _data ['parameters'])
#    end_tau_parameter = find_unique_string(device + '/END_TAU$', _data ['parameters'])
#    start_ampl_parameter = find_unique_string(device + '/START_AMPL$', _data ['parameters'])
#    end_ampl_parameter = find_unique_string(device + '/END_AMPL$', _data ['parameters'])
#    upp_parameter = find_unique_string(device + '/UPP$', _data ['parameters'])
#    create_child_node(upp_parameter, [ start_tau_parameter, end_tau_parameter, start_ampl_parameter, end_ampl_parameter, erho_parameter, tgrid_parameter, bp_length_parameter ])

#    uctrl_parameter = find_unique_string(device + '/UCTRL$', _data ['parameters'])
#    create_child_node(uctrl_parameter, [ upp_parameter, incorpip_parameter ])

#    dqh_parameter = find_unique_string(device + '/DQH$', _data ['parameters'])
#    qhfr_parameter = find_unique_string(device + '/QHFR$', _data ['parameters'])
#    rampvals_parameter = find_unique_string(device + '/RAMPVALS#data$', _data ['parameters'])
#    create_child_node(rampvals_parameter, [ h_parameter, frev_parameter, dqh_parameter, uctrl_parameter, qhfr_parameter ])

#print ('Parameters that are created: %s\n' % _data ['parameters']);

#keylist = _relations.keys()
#keylist.sort()
#for key in keylist:
#    print (key, _relations[key])


#print ('Relations that are created: %s\n' % _relations);

print ()
print ('Items that are created:')
print ('"data":')
print (json.dumps(_data, sort_keys=True, indent=4))
