#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller
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