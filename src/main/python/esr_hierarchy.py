#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller
'''

from __future__ import print_function # Python 3.x style print function
import re # Regular expressions

# This part will be externalized in a python module and resides here only during prototyping
import json # JSON export
import cx_Oracle
import os

_data = {} # empty dicts
_data ['parameter_types'] = {}
_data ['parameters'] = {}
_data ['relations'] = {}

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
        _data ['relations'][ parameter_name ].extend(parent_parameter_names)
    except KeyError:
        _data ['relations'][ parameter_name ] = parent_parameter_names
    
###
# The script starts here
###   
accelerator = 'ESR'
particle_transfer = 'ESR_RING'
hierarchy = 'DEFAULT'
version = '1.0.0'

device_names = find_devices_by_particle_transfer(particle_transfer);
for device_name in device_names:
    print (device_name);
    
beam_device         = accelerator + 'BEAM';
kicker_device       = accelerator + 'KICKER';
optics_device       = accelerator + 'OPTICS';
rf_device           = accelerator + 'RF';
timeparam_device    = accelerator + 'TIMEPARAM';
orbit_device        = accelerator + 'ORBIT';

create_parameter(beam_device  + '/A','SCALAR_A','Y');
create_parameter(beam_device  + '/ALPHAC','ALPHAC','N');
create_parameter(beam_device  + '/AOQ','SCALAR_AOQ','N');
create_parameter(beam_device  + '/BRHO','BRHO','N');
create_parameter(beam_device  + '/BRHODOT','BRHODOT','N');
create_parameter(beam_device  + '/BRHO_START_END','SCALAR_BRHO','N');
create_parameter(beam_device  + '/BUCKETFILL','SCALAR_BUCKETFILL','Y');
create_parameter(beam_device  + '/BUNCHFACTOR','BUNCHFACTOR','Y');
create_parameter(beam_device  + '/BUNCHPATTERN','SCALAR_BUNCHPATTERN','Y');
create_parameter(beam_device  + '/CH','CHROMATICITY','Y');
create_parameter(beam_device  + '/CV','CHROMATICITY','Y');
create_parameter(beam_device  + '/DELTAR','DELTAR','Y');
create_parameter(beam_device  + '/E','SCALAR_E','Y');
create_parameter(beam_device  + '/ELEMENT','SCALAR_ELEMENT','Y');
create_parameter(beam_device  + '/ERHO','ERHO','N');
create_parameter(beam_device  + '/ETA','ETA','N');
create_parameter(beam_device  + '/FREV','FREV','N');
create_parameter(beam_device  + '/GAMMA','GAMMA','N');
create_parameter(beam_device  + '/GEOFACT','GEOFACT','Y');
create_parameter(beam_device  + '/H','SCALAR_H','Y');
create_parameter(beam_device  + '/INJ_EMIH','SCALAR_INJ_EMIH','Y');
create_parameter(beam_device  + '/INJ_EMIL','SCALAR_INJ_EMIL','Y');
create_parameter(beam_device  + '/INJ_EMIV','SCALAR_INJ_EMIV','Y');
create_parameter(beam_device  + '/ISOTOPE','SCALAR_ISOTOPE','Y');
create_parameter(beam_device  + '/KAMPL','SCALAR_KAMPL','Y');
create_parameter(beam_device  + '/KHARM','SCALAR_KHARM','Y');
create_parameter(beam_device  + '/KOFFSET','SCALAR_KOFFSET','Y');
create_parameter(beam_device  + '/KPHASE','SCALAR_KPHASE','Y');
create_parameter(beam_device  + '/MAXRH','MAXRH','N');
create_parameter(beam_device  + '/MAXRV','MAXRV','N');
create_parameter(beam_device  + '/NPARTICLES','SCALAR_NPARTICLES','Y');
create_parameter(beam_device  + '/NPERBUNCH','SCALAR_NPERBUNCH','N');
create_parameter(beam_device  + '/PHIS','PHIS','N');
create_parameter(beam_device  + '/Q','SCALAR_Q','Y');
create_parameter(beam_device  + '/QH','TUNE','Y');
create_parameter(beam_device  + '/QV','TUNE','Y');
create_parameter(beam_device  + '/TBUNCH','SCALAR_TBUNCH','N');
create_parameter(beam_device  + '/TREV','TREV','N');
create_parameter(kicker_device  + '/MODE','SCALAR_KICKER_MODE','Y');
create_parameter(kicker_device  + '/NBUNCH1','SCALAR_NBUNCH1','Y');
create_parameter(kicker_device  + '/START','SCALAR_KICKER_START','Y');
create_parameter(kicker_device  + '/THIGH1','SCALAR_KICKER_THIGH1','Y');
create_parameter(kicker_device  + '/THIGH2','SCALAR_KICKER_THIGH2','Y');
create_parameter(kicker_device  + '/TOFFSET1','SCALAR_KICKER_TOFFSET1','Y');
create_parameter(kicker_device  + '/TOFFSET2','SCALAR_KICKER_TOFFSET2','Y');
create_parameter(optics_device  + '/TAU_START_END','SCALAR_TAU','Y');
create_parameter(optics_device  + '/OPTICSIP','OPTICSIP','Y');
create_parameter(rf_device  + '/ABKT','ABKT','Y');
create_parameter(rf_device  + '/DUALH','SCALAR_DUALH','Y');
create_parameter(rf_device  + '/DUALHIP','DUALHIP','Y');
create_parameter(rf_device  + '/FRFRING','FRFRING','Y');
create_parameter(rf_device  + '/MODE','SCALAR_CAVITY_MODE','Y');
create_parameter(rf_device  + '/PRFRING','PRFRING','N');
create_parameter(rf_device  + '/URFRING','URFRING','N');
create_parameter(rf_device  + '/URFSC','URFSC','N');
create_parameter(timeparam_device  + '/BDOT','SCALAR_BDOT','Y');
create_parameter(timeparam_device  + '/BP_LENGTH','SCALAR_BP_LENGTH','N');
create_parameter(timeparam_device  + '/INCORPIP','INCORPIP','N');
create_parameter(timeparam_device  + '/TGRID','SCALAR_TGRID','Y');
create_parameter(timeparam_device  + '/TROUND','SCALAR_TROUND','Y');
create_parameter(timeparam_device  + '/T_BP_LENGTH','SCALAR_T_BP_LENGTH','Y');
create_parameter(timeparam_device  + '/T_WAIT','SCALAR_T_WAIT','Y');


create_parameter_relations(beam_device + '/A', [ beam_device + '/AOQ']);
create_parameter_relations(beam_device + '/ALPHAC', [ beam_device + '/ETA']);
create_parameter_relations(beam_device + '/AOQ', [ beam_device + '/ERHO']);
create_parameter_relations(beam_device + '/AOQ', [ beam_device + '/BRHO_START_END']);
create_parameter_relations(beam_device + '/AOQ', [ beam_device + '/GAMMA']);
create_parameter_relations(beam_device + '/AOQ', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/BRHO', [ beam_device + '/ERHO']);
create_parameter_relations(beam_device + '/BRHO', [ beam_device + '/GAMMA']);
create_parameter_relations(beam_device + '/BRHO', [ beam_device + '/GEOFACT']);
create_parameter_relations(beam_device + '/BRHO', [ beam_device + '/MAXRH']);
create_parameter_relations(beam_device + '/BRHO', [ beam_device + '/MAXRV']);
create_parameter_relations(beam_device + '/BRHODOT', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/BRHO_START_END', [ beam_device + '/GEOFACT']);
create_parameter_relations(beam_device + '/BRHO_START_END', [ beam_device + '/MAXRH']);
create_parameter_relations(beam_device + '/BRHO_START_END', [ beam_device + '/MAXRV']);
create_parameter_relations(beam_device + '/BRHO_START_END', [ timeparam_device + '/BP_LENGTH']);
create_parameter_relations(beam_device + '/BUCKETFILL', [ rf_device + '/ABKT']);
create_parameter_relations(beam_device + '/BUNCHPATTERN', [ beam_device + '/NPERBUNCH']);
create_parameter_relations(beam_device + '/E', [ beam_device + '/BRHO_START_END']);
create_parameter_relations(beam_device + '/E', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/ELEMENT', [ beam_device + '/A']);
create_parameter_relations(beam_device + '/ETA', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/EXT_BRHO', [ timeparam_device + '/BP_LENGTH']);
create_parameter_relations(beam_device + '/FREV', [ rf_device + '/FRFRING']);
create_parameter_relations(beam_device + '/FREV', [ beam_device + '/TREV']);
create_parameter_relations(beam_device + '/GAMMA', [ beam_device + '/ETA']);
create_parameter_relations(beam_device + '/GAMMA', [ beam_device + '/FREV']);
create_parameter_relations(beam_device + '/GAMMA', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/GEOFACT', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/H', [ beam_device + '/NPERBUNCH']);
create_parameter_relations(beam_device + '/H', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/H', [ beam_device + '/TBUNCH']);
create_parameter_relations(beam_device + '/H', [ kicker_device + '/THIGH1']);
create_parameter_relations(beam_device + '/H', [ kicker_device + '/THIGH2']);
create_parameter_relations(beam_device + '/H', [ rf_device + '/FRFRING']);
create_parameter_relations(beam_device + '/INJ_EMIH', [ beam_device + '/GEOFACT']);
create_parameter_relations(beam_device + '/INJ_EMIH', [ beam_device + '/MAXRH']);
create_parameter_relations(beam_device + '/INJ_EMIH', [ beam_device + '/MAXRV']);
create_parameter_relations(beam_device + '/INJ_EMIL', [ rf_device + '/ABKT']);
create_parameter_relations(beam_device + '/INJ_EMIL', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/INJ_EMIV', [ beam_device + '/GEOFACT']);
create_parameter_relations(beam_device + '/INJ_EMIV', [ beam_device + '/MAXRH']);
create_parameter_relations(beam_device + '/INJ_EMIV', [ beam_device + '/MAXRV']);
create_parameter_relations(beam_device + '/ISOTOPE', [ beam_device + '/A']);
create_parameter_relations(beam_device + '/NPARTICLES', [ beam_device + '/NPERBUNCH']);
create_parameter_relations(beam_device + '/NPERBUNCH', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/PHIS', [ beam_device + '/BUNCHFACTOR']);
create_parameter_relations(beam_device + '/PHIS', [ rf_device + '/PRFRING']);
create_parameter_relations(beam_device + '/PHIS', [ rf_device + '/URFRING']);
create_parameter_relations(beam_device + '/PHIS', [ rf_device + '/URFSC']);
create_parameter_relations(beam_device + '/Q', [ beam_device + '/AOQ']);
create_parameter_relations(beam_device + '/Q', [ beam_device + '/PHIS']);
create_parameter_relations(beam_device + '/TBUNCH', [ kicker_device + '/THIGH1']);
create_parameter_relations(beam_device + '/TBUNCH', [ kicker_device + '/THIGH2']);
create_parameter_relations(beam_device + '/TREV', [ beam_device + '/TBUNCH']);

create_parameter_relations(kicker_device + '/NBUNCH1', [ kicker_device + '/THIGH1']);
create_parameter_relations(kicker_device + '/NBUNCH1', [ kicker_device + '/THIGH2']);
create_parameter_relations(kicker_device + '/THIGH1', [ kicker_device + '/TOFFSET2']);
create_parameter_relations(kicker_device + '/TOFFSET1', [ kicker_device + '/TOFFSET2']);

create_parameter_relations(optics_device + '/TAU_START_END', [ timeparam_device + '/BP_LENGTH']);
create_parameter_relations(optics_device + '/TAU_START_END', [ optics_device + '/OPTICSIP']);
create_parameter_relations(optics_device + '/OPTICSIP', [ beam_device + '/ALPHAC']);
create_parameter_relations(optics_device + '/OPTICSIP', [ beam_device + '/CH']);
create_parameter_relations(optics_device + '/OPTICSIP', [ beam_device + '/CV']);
create_parameter_relations(optics_device + '/OPTICSIP', [ beam_device + '/MAXRH']);
create_parameter_relations(optics_device + '/OPTICSIP', [ beam_device + '/MAXRV']);
create_parameter_relations(optics_device + '/OPTICSIP', [ beam_device + '/QH']);
create_parameter_relations(optics_device + '/OPTICSIP', [ beam_device + '/QV']);

create_parameter_relations(rf_device + '/ABKT', [ beam_device + '/PHIS']);
create_parameter_relations(rf_device + '/DUALH', [ rf_device + '/DUALHIP']);    
create_parameter_relations(rf_device + '/DUALHIP', [ beam_device + '/PHIS']);

create_parameter_relations(timeparam_device + '/BDOT', [ timeparam_device + '/BP_LENGTH']);
create_parameter_relations(timeparam_device + '/BP_LENGTH', [ beam_device + '/BRHO']);
create_parameter_relations(timeparam_device + '/BP_LENGTH', [ beam_device + '/BRHODOT']);
create_parameter_relations(timeparam_device + '/BP_LENGTH', [ beam_device + '/DELTAR']);
create_parameter_relations(timeparam_device + '/BP_LENGTH', [ rf_device + '/ABKT']);
create_parameter_relations(timeparam_device + '/BP_LENGTH', [ rf_device + '/DUALHIP']);
create_parameter_relations(timeparam_device + '/BP_LENGTH', [ timeparam_device + '/INCORPIP']);
create_parameter_relations(timeparam_device + '/INCORPIP', [ optics_device + '/OPTICSIP']);
create_parameter_relations(timeparam_device + '/TGRID', [ rf_device + '/ABKT']);
create_parameter_relations(timeparam_device + '/TGRID', [ timeparam_device + '/BP_LENGTH']);
create_parameter_relations(timeparam_device + '/TROUND', [ timeparam_device + '/BP_LENGTH']);
create_parameter_relations(timeparam_device + '/T_BP_LENGTH', [ timeparam_device + '/BP_LENGTH']);
create_parameter_relations(timeparam_device + '/T_WAIT', [ timeparam_device + '/BP_LENGTH']);


# Create optics parameter



































quadrupole_devices = [ 'S01QS1F', 'S12QS1F', 'S01QS2D', 'S12QS2D', 'S12QS3T' ]

create_parameter_type('K1L', display_name=None, unit='1/m', value_type='FUNCTION',
                              external=False, hardware=False, expert=False,
                              description='Generic normalized quadrupole strength', type_category='HW MAGNITUDE',
                              x_prec=3, y_prec=3, min_value=None, max_value=None,
                              type_group='KL', multiplexed=True,
                              function_bproc=True, restorable=True)
create_parameter_type('B1L', display_name=None, unit='T', value_type='FUNCTION',
                              hardware=True, type_category='HW SETTINGS', type_group='BL',
                              description='Generic integral quadrupole field')
create_parameter_type('I', 'VALUE_TYPE', 'TYPE_CATEGORY', 'TYPE_GROUP')
create_parameter_type('IDOT', 'VALUE_TYPE', 'TYPE_CATEGORY', 'TYPE_GROUP')
create_parameter_type('UEDDY', 'VALUE_TYPE', 'TYPE_CATEGORY', 'TYPE_GROUP')
create_parameter_type('U', 'VALUE_TYPE', 'TYPE_CATEGORY', 'TYPE_GROUP')
create_parameter_type('QH', 'VALUE_TYPE', 'TYPE_CATEGORY', 'TYPE_GROUP')
create_parameter_type('QV', 'VALUE_TYPE', 'TYPE_CATEGORY', 'TYPE_GROUP')
create_parameter_type('BRHO', 'VALUE_TYPE', 'TYPE_CATEGORY', 'TYPE_GROUP')

# Hier ein Beispiel fuer einen Listenfilters mit regex. Zur Erklaerung:
# lambda Ausdruecke sind quasi Funktionen: f(x)=x*x waere lambda x=x*x
# Ist das Ergebnis der Funktionsauswertung 'None' wird der Eintrag gefiltered, sonst wird er uebernommen.
s01_quadrupoles = filter(lambda device: re.search('S[0 | 1][0 | 1]QS.*', device), quadrupole_devices)
print ('Quadrupoles starting with S01: %s' % s01_quadrupoles)

beam_device = particle_transfer.replace('_RING', 'BEAM')

for device in quadrupole_devices:
    create_parameter(device + '/KL', 'K1L')
    create_parameter(device + '/BL', 'B1L')
    create_parameter(device + '/I', 'I')
    create_parameter(device + '/IDOT', 'IDOT')
    create_parameter(device + '/UEDDY', 'UEDDY')
    create_parameter(device + '/U', 'U')
    
#    create_dependencies(device + '/KL', [ beam_device + '/QH', beam_device + '/QV'])

bl_parameters = filter(lambda parameter: re.search('.*/BL', parameter) , _data['parameters'])
kl_parameters = filter(lambda parameter: re.search('.*/KL', parameter) , _data['parameters'])

#for parameter in bl_parameters:
#    create_dependencies(parameter, [ beam_device + '/BRHO' ] + kl_parameters)

print ()
print ('Items that are created:')
print (json.dumps(_data, sort_keys=True, indent=4))

