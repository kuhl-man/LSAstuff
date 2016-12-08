#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller
@author: dondreka
@author: hlieberm
'''

import csv
from lsa.setup.hierarchy import LsaHierarchy

_DEFAULT_HIERARCHY_NAME = 'DEFAULT'

class LHBuilder:
    
    def __init__(self, accelerator, particle_transfer, version):
        self.lh = LsaHierarchy(accelerator, particle_transfer, version)

    def create_child_node(self, parameter_name, parameter_parent_names, parent_parameter_order={}):
        if (parameter_name == None) or (parameter_parent_names is None):
            return
        if (type(parameter_parent_names) is str):
            self.lh.add_parameter_relations(parameter_name, [ parameter_parent_names ], parent_parameter_order )
        else:
            self.lh.add_parameter_relations(parameter_name, parameter_parent_names, parent_parameter_order )
            
    def remove_child_node(self, child_parameter_name, parent_parameter_names):
        for parent_parameter_name in parent_parameter_names:
            if parent_parameter_name in self.lh.data['PARAMETER_RELATIONS'][_DEFAULT_HIERARCHY_NAME][child_parameter_name]:
                 del self.lh.data['PARAMETER_RELATIONS'][_DEFAULT_HIERARCHY_NAME][child_parameter_name][parent_parameter_name]
                 if len(self.lh.data['PARAMETER_RELATIONS'][_DEFAULT_HIERARCHY_NAME][child_parameter_name]) == 0:
                     del self.lh.data['PARAMETER_RELATIONS'][_DEFAULT_HIERARCHY_NAME][child_parameter_name]
                     
    def remove_system(self, parameter_name, system_name):
        if system_name in self.lh.data['SYSTEM_CONFIGS'][parameter_name]:
            del self.lh.data['SYSTEM_CONFIGS'][parameter_name][system_name]
                     
        
    def export(self):
        self.lh.export()

