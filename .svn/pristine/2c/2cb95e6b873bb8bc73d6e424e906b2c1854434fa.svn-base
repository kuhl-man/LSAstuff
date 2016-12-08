from sis18esrcryring_device_groups import SIS18ESRCRYRINGDeviceGroups
from init_beamdiagnostic_devices import INIT_BEAMDIAGNOSTIC_DEVICES
#from init_generic_transfer_devices import INIT_GENERIC_TRANSFER_DEVICES

class INIT_SIS18ESRCRYRING_DEVICES(INIT_BEAMDIAGNOSTIC_DEVICES,SIS18ESRCRYRINGDeviceGroups):
#class INIT_SIS18ESRCRYRING_DEVICES(INIT_GENERIC_TRANSFER_DEVICES,SIS18ESRCRYRINGDeviceGroups):
    
    def __init__(self):
      INIT_BEAMDIAGNOSTIC_DEVICES.__init__(self)
#      INIT_GENERIC_TRANSFER_DEVICES.__init__(self)

      # ESR/SIS18 special
      self._old_cavities_ampl = []
      self._old_cavities_freq = []
      self._old_cavities_phase = []

      self._horizontal_correction_coils =  []
      self._extraction_bump_correction_coils = []

      self._electrostatic_quadrupole = []
      self._chopper = []

    def buildalldevices(self):
        self._alldevices = self.main_dipoles + self.main_quadrupoles + self.vertical_correctors + self.horizontal_correctors + self.extraction_quadrupoles + self.correction_quadrupoles + self.main_sextupoles + self.chromaticity_sextupoles + self.resonance_sextupoles + self.correction_sextupoles + self.cavities + self.inj_kicker + self.ext_kicker + self.q_kicker + self.septum + self.electrostatic_quadrupole + self.chopper + self.faraday_cups

    def buildsystemmap(self):
        INIT_BEAMDIAGNOSTIC_DEVICES.buildsystemmap(self)
#        INIT_GENERIC_TRANSFER_DEVICES.buildsystemmap(self)
        self._devicesytemmap.update(dict((x, 'RF') for x in self.old_cavities_ampl))
        self._devicesytemmap.update(dict((x, 'RF') for x in self.old_cavities_freq))
        self._devicesytemmap.update(dict((x, 'RF') for x in self.old_cavities_phase))
        self._devicesytemmap.update(dict((x, 'CORRH') for x in self.horizontal_correction_coils))
        self._devicesytemmap.update(dict((x, 'CORRH') for x in self.extraction_bump_correction_coils))
        self._devicesytemmap.update(dict((x, 'QUADCORR') for x in self.electrostatic_quadrupole))
        self._devicesytemmap.update(dict((x, 'CORRH') for x in self.chopper))

    def buildlinkrulemap(self):
        self._devicelinkrulemap = dict((x, 'DEFAULTLR') for x in self.main_dipoles)
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.main_quadrupoles))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.vertical_correctors))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.horizontal_correctors))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.extraction_quadrupoles))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.correction_quadrupoles))

        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.chromaticity_sextupoles))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.resonance_sextupoles))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.main_sextupoles))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.correction_sextupoles))

        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.correction_octupoles))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.cavities))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.inj_kicker))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.ext_kicker))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.q_kicker))

        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.electrostatic_quadrupole))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.chopper))


    ## ESR/SIS18 special properties
    @property
    def old_cavities_ampl(self):
      return self._old_cavities_ampl

    @property
    def old_cavities_freq(self):
      return self._old_cavities_freq

    @property
    def old_cavities_phase(self):
      return self._old_cavities_phase

    @property
    def horizontal_correction_coils(self):
      return self._horizontal_correction_coils

    @property
    def extraction_bump_correction_coils(self):
      return self._extraction_bump_correction_coils

    @property
    def electrostatic_quadrupole(self):
      return self._electrostatic_quadrupole

    @property
    def chopper(self):
      return self._chopper

      
if __name__ == '__main__':

  h = INIT_SIS18ESRCRYRING_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities
  print h.electrostatic_quadrupoles
  print h.chopper
  print h.faraday_cups

