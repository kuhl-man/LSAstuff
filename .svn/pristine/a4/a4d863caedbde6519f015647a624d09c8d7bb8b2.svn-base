#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller
@author: dondreka
@author: hlieberm
'''

import csv
from lsa.setup.hierarchy import LsaHierarchy

class LHBuilder:
    
    def __init__(self, accelerator, particle_transfer, version):
        self.lh = LsaHierarchy(accelerator, particle_transfer, version)

    def create_child_node(self, parameter_name, parameter_parent_names):
        if (parameter_name == None) or (parameter_parent_names is None):
            return
        if (type(parameter_parent_names) is str):
            self.lh.add_parameter_relations(parameter_name, [ parameter_parent_names ] )
        else:
            self.lh.add_parameter_relations(parameter_name, parameter_parent_names )

    def _read_devices(file_name):
        _devices = []
        with open(file_name, 'rb') as in_file:
            reader = csv.reader(in_file)
            reader.next() # ignore header line
            for row in reader:
                _devices=_devices + row
        in_file.close()
        return _devices

    def export(self):
        self.lh.export()

