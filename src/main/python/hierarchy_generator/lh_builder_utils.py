#!/bin/env python2.6
'''
Created on September 18, 2012

@author: rmueller
@author: dondreka
@author: hlieberm
'''

import csv
import re # Regular expressions


class LHBuilderUtils:

    def find_strings(self, reg_exp, in_list):
    # Filtering lists with regular expressions. Note that the pattern
    # matching is wrapped as a lambda expression (i.e. an anonymous
    # function). If the function evaluates to 'None' on an element of the
    # list to be filtered, this element is discarded, else it is retained.
        filtered_list = filter(lambda d: re.search(reg_exp, d), in_list)
        return filtered_list

    def find_unique_string(self, reg_exp, in_list):
        filtered_list = self.find_strings(reg_exp, in_list)
        if not filtered_list: # python's way of testing for empty lists
            raise RuntimeError('List did not contain string value matching regular expression ' + reg_exp)
        elif len(filtered_list) > 1:
            raise RuntimeError('More than one string value found matching regular expression ' + reg_exp)
        else:
            return filtered_list[0]

