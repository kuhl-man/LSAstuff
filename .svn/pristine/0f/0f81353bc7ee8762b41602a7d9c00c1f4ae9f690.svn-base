#!/bin/env python2.6

from lh_builder import LHBuilder

from lh_builder_utils import LHBuilderUtils

from generic_parameters import GenericParameters

###
# Actual definitions
###   
accelerator = 'SIS18'
particle_transfer = 'SIS18_RING'
hierarchy = 'DEFAULT'
version = '1.0.0'

csv_filename = 'sis18_devices.csv'


lh_builder = LHBuilder(accelerator + 'TEST', particle_transfer, version)

# lege generischen Teil der Parameter an

generic_parameters = GenericParameters(lh_builder, csv_filename)

all_devices = generic_parameters.getdevices()

## Standard device groups
main_dipoles = LHBuilderUtils().find_strings('S11MU2$', all_devices)
horizontal_correctors = [] # none for SIS18
vertical_correctors = LHBuilderUtils().find_strings('S[01][0-9]KM2DV$', all_devices)

main_quadrupoles = LHBuilderUtils().find_strings('S((01)|(12))QS((1F)|(2D)|(3T))$', all_devices)
extraction_quadrupoles = LHBuilderUtils().find_strings('S02KQ1E', all_devices)
correction_quadrupoles = LHBuilderUtils().find_strings('(S[01][0-9]KM[0-9]Q[SN])|(S[01][0-9]KQ[0-9])|(S[01][0-9]KQ[0-9]E)$', all_devices)

main_sextupoles = LHBuilderUtils().find_strings('S[01][0-9]KS[13]C$', all_devices)
chromaticity_sextupoles = main_sextupoles[:] # python's shallow copy for lists
resonance_sextupoles = LHBuilderUtils().find_strings('S[01][0-9]KS1C$', main_sextupoles)
correction_sextupoles = LHBuilderUtils().find_strings('S[01][0-9]KM[0-9]S[SN]$', all_devices)

correction_octupoles = LHBuilderUtils().find_strings('S[01][0-9]KM[0-9]O[SN]$', all_devices) # none for SIS18

horizontal_correction_coils = LHBuilderUtils().find_strings('S[01][0-9]MU[12]A$', all_devices)
extraction_bump_correction_coils = LHBuilderUtils().find_strings('(S((04)|(06))MU1A)|(S((05)|(07)|(10)|(11)|(12))MU2A)', horizontal_correction_coils)
extra_correction_coils = LHBuilderUtils().find_strings('(S((02)|(07)|(08))MU1A)|(S04MU2A)', horizontal_correction_coils)
horizontal_orbit_correction_coils = list(set(horizontal_correction_coils)-set(extraction_bump_correction_coils))

cavities = LHBuilderUtils().find_strings('S07BE[1-3]$', all_devices)

sis18_cavities_ampl = LHBuilderUtils().find_strings('S0[28]BE[12]A$', all_devices)
sis18_cavities_freq = LHBuilderUtils().find_strings('S0[28]BE[12]FS$', all_devices)
sis18_cavities_phase = LHBuilderUtils().find_strings('S0[28]BE[12]P$', all_devices)

bumper = LHBuilderUtils().find_strings('S[01][1-3]MB[1-4]$', all_devices)

kicker = LHBuilderUtils().find_strings('S0[45]MK[12]E$', all_devices)

sis18_bypass = LHBuilderUtils().find_strings('S06MU4$', all_devices)

sis18_ko_exiter = LHBuilderUtils().find_strings('S07BO1E$', all_devices)

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

from specialSIS18_parameters import SpecialSIS18Parameters

specialSIS18_parameters = SpecialSIS18Parameters(lh_builder, csv_filename)

## Hardware
hardware_fs_system =  LHBuilderUtils().find_unique_string('S00BE_FS', all_devices)
hardware_rf_system = LHBuilderUtils().find_unique_string('S00BE_PS', all_devices)
tgx_system = LHBuilderUtils().find_unique_string('S00ZGT', all_devices)
timing_device = LHBuilderUtils().find_unique_string('S00ZZ', all_devices)

# set special devices
specialSIS18_parameters.sethardware_fs_system(hardware_fs_system)
specialSIS18_parameters.sethardware_rf_system(hardware_rf_system)
specialSIS18_parameters.settgx_system(tgx_system)
specialSIS18_parameters.settiming_device(timing_device)

specialSIS18_parameters.setmaindipole(main_dipoles)

specialSIS18_parameters.sethorizontal_correctors(horizontal_correctors)
specialSIS18_parameters.setvertical_correctors(vertical_correctors)

specialSIS18_parameters.setmain_sextupoles(main_sextupoles)

specialSIS18_parameters.sethorizontal_correction_coils(horizontal_correction_coils)
specialSIS18_parameters.setextraction_bump_correction_coils(extraction_bump_correction_coils)
specialSIS18_parameters.setextra_correction_coils(extra_correction_coils)
specialSIS18_parameters.sethorizontal_orbit_correction_coils(horizontal_orbit_correction_coils)


specialSIS18_parameters.setsis18_cavities_ampl(sis18_cavities_ampl)
specialSIS18_parameters.setsis18_cavities_freq(sis18_cavities_freq)
specialSIS18_parameters.setsis18_cavities_phase(sis18_cavities_phase)

specialSIS18_parameters.setkicker(kicker)
specialSIS18_parameters.setbumper(bumper)

specialSIS18_parameters.setsis18_bypass(sis18_bypass)
specialSIS18_parameters.setsis18_ko_exiter(sis18_ko_exiter)

# build special part of hierarchy

lh_builder = specialSIS18_parameters.build(particle_transfer)

# TESTING

#lh_builder.create_child_node("TEST1", "TEST2")

lh_builder.export()
