#!/bin/env python2.6

from lh_builder import LHBuilder

from lh_builder_utils import LHBuilderUtils

from generic_parameters import GenericParameters


###
# Actual definitions
###   
accelerator = 'SIS100'
particle_transfer = 'SIS100_RING'
hierarchy = 'DEFAULT'
version = '1.0.0'

csv_filename = 'sis100_devices.csv'


lh_builder = LHBuilder(accelerator + 'TEST', particle_transfer, version)

# lege generischen Teil der Parameter an

generic_parameters = GenericParameters(lh_builder, csv_filename)

all_devices = generic_parameters.getdevices()

## Standard device groups
main_dipoles = LHBuilderUtils().find_strings('1S00MH$', all_devices)
horizontal_correctors = LHBuilderUtils().find_strings('1S[1-6][1-E]KH1$', all_devices)
vertical_correctors = LHBuilderUtils().find_strings('1S[1-6][1-E]KV1$', all_devices)

main_quadrupoles = LHBuilderUtils().find_strings('1S00QD[12][DF]$', all_devices)
extraction_quadrupoles = LHBuilderUtils().find_strings('1S13QS1E$', all_devices)
correction_quadrupoles = LHBuilderUtils().find_strings('1S[1-6][1-E]KM1QN$', all_devices)

main_sextupoles = LHBuilderUtils().find_strings('(1S00KS[1-3]C[VH]|1S[1-6][1-E]KS1E)$', all_devices)
chromaticity_sextupoles = main_sextupoles[:] # python's shallow copy for lists
resonance_sextupoles = LHBuilderUtils().find_strings('1S[1-6][1-E]KS1E$', main_sextupoles)
correction_sextupoles = LHBuilderUtils().find_strings('1S[1-6][1-E]KM1SN$', all_devices)

correction_octupoles = LHBuilderUtils().find_strings('1S[1-6][1-E]KM1ON$', all_devices) # none for SIS18

#horizontal_correction_coils = LHBuilderUtils().find_strings('S[01][0-9]MU[12]A$', all_devices)
#extraction_bump_correction_coils = LHBuilderUtils().find_strings('(S((04)|(06))MU1A)|(S((05)|(07)|(10)|(11)|(12))MU2A)', horizontal_correction_coils)
#extra_correction_coils = LHBuilderUtils().find_strings('(S((02)|(07)|(08))MU1A)|(S04MU2A)', horizontal_correction_coils)
#horizontal_orbit_correction_coils = list(set(horizontal_correction_coils)-set(extraction_bump_correction_coils))

cavities = LHBuilderUtils().find_strings('1S[1-6][1-4]BE[1-2]$', all_devices)

#sis18_cavities_ampl = LHBuilderUtils().find_strings('S0[28]BE[12]A$', all_devices)
#sis18_cavities_freq = LHBuilderUtils().find_strings('S0[28]BE[12]FS$', all_devices)
#sis18_cavities_phase = LHBuilderUtils().find_strings('S0[28]BE[12]P$', all_devices)

#bumper = LHBuilderUtils().find_strings('S[01][1-3]MB[1-4]$', all_devices)

kicker = LHBuilderUtils().find_strings('1S5[1-3]MK[1-3]E$', all_devices)

q_kicker = LHBuilderUtils().find_strings('1S13MK[1-2]Q$', all_devices)

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

generic_parameters.setkicker(kicker + q_kicker)

# build generic part of hierarchy

lh_builder = generic_parameters.build(particle_transfer)

# lege speziellen Teil der Parameter an

from specialSIS100_parameters import SpecialSIS100Parameters

specialSIS100_parameters = SpecialSIS100Parameters(lh_builder, csv_filename)

# set special devices

specialSIS100_parameters.setkicker(kicker)
specialSIS100_parameters.setq_kicker(q_kicker)

# build special part of hierarchy

lh_builder = specialSIS100_parameters.build(particle_transfer)

# TESTING

#lh_builder.create_child_node("TEST1", "TEST2")

lh_builder.export()
