#!/bin/env python2.6

from lh_builder import LHBuilder

from lh_builder_utils import LHBuilderUtils

from generic_parameters import GenericParameters


###
# Actual definitions
###   
accelerator = 'ESR'
particle_transfer = 'ESR_RING'
hierarchy = 'DEFAULT'
version = '1.0.0'

csv_filename = 'esr_devices.csv'


lh_builder = LHBuilder(accelerator + 'TEST', particle_transfer, version)

# lege generischen Teil der Parameter an

generic_parameters = GenericParameters(lh_builder, csv_filename)

all_devices = generic_parameters.getdevices()

## Standard device groups
main_dipoles = LHBuilderUtils().find_strings('E01MU1$', all_devices)
horizontal_correctors = []
vertical_correctors = LHBuilderUtils().find_strings('E0[1-2]KY[1-4]$', all_devices)

main_quadrupoles = LHBuilderUtils().find_strings('E01QS[0-9][DF]$', all_devices)
extraction_quadrupoles = [] #LHBuilderUtils().find_strings('1S13QS1E$', all_devices)
correction_quadrupoles = [] #LHBuilderUtils().find_strings('1S[1-6][1-E]KM1QN$', all_devices)

main_sextupoles = LHBuilderUtils().find_strings('E0[1-2]KS[1-4]$', all_devices)
chromaticity_sextupoles = main_sextupoles[:] # python's shallow copy for lists
resonance_sextupoles = [] #LHBuilderUtils().find_strings('1S[1-6][1-E]KS1E$', main_sextupoles)
correction_sextupoles = [] #LHBuilderUtils().find_strings('1S[1-6][1-E]KM1SN$', all_devices)

correction_octupoles = [] #LHBuilderUtils().find_strings('1S[1-6][1-E]KM1ON$', all_devices) # none for SIS18

horizontal_correction_coils = LHBuilderUtils().find_strings('E0[1-2]KX[1-6]$', all_devices)
#extraction_bump_correction_coils = LHBuilderUtils().find_strings('(S((04)|(06))MU1A)|(S((05)|(07)|(10)|(11)|(12))MU2A)', horizontal_correction_coils)
#extra_correction_coils = LHBuilderUtils().find_strings('(S((02)|(07)|(08))MU1A)|(S04MU2A)', horizontal_correction_coils)
#horizontal_orbit_correction_coils = list(set(horizontal_correction_coils)-set(extraction_bump_correction_coils))

cavities = [] #LHBuilderUtils().find_strings('1S[1-6][1-4]BE[1-2]$', all_devices)

#sis18_cavities_ampl = LHBuilderUtils().find_strings('S0[28]BE[12]A$', all_devices)
#sis18_cavities_freq = LHBuilderUtils().find_strings('S0[28]BE[12]FS$', all_devices)
#sis18_cavities_phase = LHBuilderUtils().find_strings('S0[28]BE[12]P$', all_devices)

esr_cavities_ampl = LHBuilderUtils().find_strings('E02BE1A$', all_devices)
esr_cavities_freq = LHBuilderUtils().find_strings('E02BE1FS$', all_devices)

polefacewindings = LHBuilderUtils().find_strings('E01KP[0-2][0-9]$', all_devices)

#bumper = LHBuilderUtils().find_strings('S[01][1-3]MB[1-4]$', all_devices)

kicker = [] #LHBuilderUtils().find_strings('1S5[1-3]MK[1-3]E$', all_devices)

q_kicker = [] #LHBuilderUtils().find_strings('1S13MK[1-2]Q$', all_devices)

#sis18_bypass = LHBuilderUtils().find_strings('S06MU4$', all_devices)

#sis18_ko_exiter = LHBuilderUtils().find_strings('S07BO1E$', all_devices)

# set devices
generic_parameters.setmaindipole(main_dipoles)
generic_parameters.sethorizontal_correctors(horizontal_correctors)
generic_parameters.setvertical_correctors(vertical_correctors)

generic_parameters.setmain_quadrupoles(main_quadrupoles)
generic_parameters.setextraction_quadrupoles(extraction_quadrupoles)
generic_parameters.setcorrection_quadrupoles(correction_quadrupoles)

generic_parameters.setmain_sextupoles(main_sextupoles)
generic_parameters.setchromaticity_sextupoles(chromaticity_sextupoles)
generic_parameters.setresonance_sextupoles(resonance_sextupoles)
generic_parameters.setcorrection_sextupoles(correction_sextupoles)

generic_parameters.setcorrection_octupoles(correction_octupoles)

generic_parameters.setcavities(cavities)

generic_parameters.setkicker(kicker)

# build generic part of hierarchy

lh_builder = generic_parameters.build(particle_transfer)

# lege speziellen Teil der Parameter an

from specialESR_parameters import SpecialESRParameters

specialESR_parameters = SpecialESRParameters(lh_builder, csv_filename)

# set special devices
specialESR_parameters.setmaindipole(main_dipoles)

specialESR_parameters.sethorizontal_correction_coils(horizontal_correction_coils)

specialESR_parameters.setesr_cavities_ampl(esr_cavities_ampl)
specialESR_parameters.setesr_cavities_freq(esr_cavities_freq)

specialESR_parameters.setpolefacewindings(polefacewindings)

# build special part of hierarchy

lh_builder = specialESR_parameters.build(particle_transfer)

# TESTING

#lh_builder.create_child_node("TEST1", "TEST2")

lh_builder.export()
