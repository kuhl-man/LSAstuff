from beamdiagnostic_device_groups import BeamdiagnosticDeviceGroups
from init_generic_devices import INIT_GENERIC_DEVICES

class INIT_BEAMDIAGNOSTIC_DEVICES(INIT_GENERIC_DEVICES,BeamdiagnosticDeviceGroups):
    
    def __init__(self):
      INIT_GENERIC_DEVICES.__init__(self)

      self._faraday_cups = []
      self._septa = []
                  
    def buildalldevices(self):
        self._alldevices = self.main_dipoles + self.main_quadrupoles + self.vertical_correctors + self.horizontal_correctors + self.extraction_quadrupoles + self.correction_quadrupoles + self.main_sextupoles + self.chromaticity_sextupoles + self.resonance_sextupoles + self.correction_sextupoles + self.cavities + self.inj_kicker + self.ext_kicker + self.q_kicker + self.septa + self.faraday_cups

        
    def buildsystemmap(self):
        INIT_GENERIC_DEVICES.buildsystemmap(self)
        self._devicesytemmap.update(dict((x, 'FARADAY_CUP') for x in self.faraday_cups))
        self._devicesytemmap.update(dict((x, 'SEPTA') for x in self.septa))

    def buildlinkrulemap(self):
        self._devicelinkrulemap = dict((x, 'DEFAULTLR') for x in self.main_dipoles)
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.main_quadrupoles))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.vertical_correctors))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.septa))

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

        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.faraday_cups))


    ## generic properties
    @property
    def faraday_cups(self):
      return self._faraday_cups

    @property
    def septa(self):
      return self._septa

      
if __name__ == '__main__':

  h = INIT_SIS18ESRCRYRING_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities
  print h.faraday_cups
  print h.septa

