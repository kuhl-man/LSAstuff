#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller

'''

from __future__ import print_function # Python 3.x style print function
import json

class LsaHierarchy:
    _default_hierarchy_name = 'DEFAULT'
    _default_usergroup = 'OP'
    
    def __init__(self, accelerator_name, particle_transfer_name, hierarchy_version_number):
        self.data = {
                     'hierarchy_details' : {
                                            'accelerator' : accelerator_name,
                                            'particle_transfer' : particle_transfer_name,
                                            'version_number' : hierarchy_version_number,
                     },
                     'parameters_physics' : {},
                     'parameters_hardware' : {},
                     'parameter_relations' : { self._default_hierarchy_name : {} },
                     }
        
    def define_hardware_parameter(self, device_name, property_name, field_name, is_trimable=True, belongs_to_function_bproc=True, x_prec=None, y_prec=None):
        parameter_name = "%s/%s#%s" % (device_name, property_name, field_name)
        parameter_attributes = { 
                                'device_name' : device_name, 
                                'property_name' : property_name, 
                                'field_name' : field_name, 
                                'x_prec' : x_prec, 
                                'y_prec' : y_prec, 
                                'is_trimable' : is_trimable,
                                'belongs_to_function_bproc' : belongs_to_function_bproc, 
                                'usergroup' : self._default_usergroup, 
                                'default_hierarchy' : self._default_hierarchy_name,
                                }
        self.data ['parameters_hardware'] [ parameter_name ] = parameter_attributes
        return parameter_name

    def define_discrete_physics_parameter(self, parameter_name, parameter_type_name, device_name, is_trimable=True, belongs_to_function_bproc=False, x_prec=None, y_prec=None):
        self.define_generic_physics_parameter(parameter_name, parameter_type_name, device_name, is_trimable, belongs_to_function_bproc, x_prec, y_prec)
        return parameter_name

    def define_nontrimable_discrete_physics_parameter(self, parameter_name, parameter_type_name, device_name, is_trimable=False, belongs_to_function_bproc=False, x_prec=None, y_prec=None):
        self.define_generic_physics_parameter(parameter_name, parameter_type_name, device_name, is_trimable, belongs_to_function_bproc, x_prec, y_prec)
        return parameter_name

    def define_physics_parameter(self, parameter_name, parameter_type_name, device_name, is_trimable=True, belongs_to_function_bproc=True, x_prec=None, y_prec=None):
        self.define_generic_physics_parameter(parameter_name, parameter_type_name, device_name, is_trimable, belongs_to_function_bproc, x_prec, y_prec)
        return parameter_name

    def define_nontrimable_physics_parameter(self, parameter_name, parameter_type_name, device_name, is_trimable=False, belongs_to_function_bproc=True, x_prec=None, y_prec=None):
        self.define_generic_physics_parameter(parameter_name, parameter_type_name, device_name, is_trimable, belongs_to_function_bproc, x_prec, y_prec)
        return parameter_name

    def define_generic_physics_parameter(self, parameter_name, parameter_type_name, device_name, is_trimable, belongs_to_function_bproc, x_prec, y_prec):
        parameter_attributes = { 
                                'parameter_type_name' : parameter_type_name, 
                                'device_name' : device_name, 
                                'x_prec' : x_prec, 
                                'y_prec' : y_prec, 
                                'is_trimable' : is_trimable,
                                'belongs_to_function_bproc' : belongs_to_function_bproc, 
                                'usergroup' : self._default_usergroup, 
                                'default_hierarchy' : self._default_hierarchy_name,
                                }
        self.data ['parameters_physics'] [ parameter_name ] = parameter_attributes
        return parameter_name
        
    def add_parameter_relations(self, child_parameter_name, parent_parameter_names, parent_parameter_order={}):
        for parent_parameter_name in parent_parameter_names:
            order_number = None
            if parent_parameter_name in parent_parameter_order:
                order_number = parent_parameter_order[parent_parameter_name]
                
            if child_parameter_name not in self.data['parameter_relations'][self._default_hierarchy_name]:
                self.data['parameter_relations'][self._default_hierarchy_name][child_parameter_name] = {}
                
            if parent_parameter_name not in self.data['parameter_relations'][self._default_hierarchy_name][child_parameter_name]:
                self.data['parameter_relations'][self._default_hierarchy_name][child_parameter_name][parent_parameter_name] = {}
                
            self.data['parameter_relations'][self._default_hierarchy_name][child_parameter_name][parent_parameter_name]['position'] = order_number
                
    def get_parameters(self):
        parameter_names = self.data['parameters_physics'].keys() + self.data['parameters_hardware'].keys() 
        return parameter_names
    
    def get_data(self):
        return self.data
    
    def export(self):
        json_file_name = 'lh-%s-%s-%s.json' % (self.data['hierarchy_details']['accelerator'], self.data['hierarchy_details']['particle_transfer'], self.data['hierarchy_details']['version_number'] )
        json_file = open(json_file_name, 'wb')
        json_file.write(json.dumps(self.data, sort_keys=True, indent=2))
        json_file.close()
        
