from init_generic_devices import INIT_GENERIC_DEVICES

class INIT_GENERIC_RING_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
      INIT_GENERIC_DEVICES.__init__(self)

    def buildalldevices(self):
        INIT_GENERIC_DEVICES.buildalldevices(self)

    def buildsystemmap(self):
        INIT_GENERIC_DEVICES.buildsystemmap(self)

    def buildlinkrulemap(self):
        self._devicelinkrulemap = dict((x, 'RAMPLR') for x in self.main_dipoles)
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.main_quadrupoles))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.vertical_correctors))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.horizontal_correctors))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.extraction_quadrupoles))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.correction_quadrupoles))

        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.chromaticity_sextupoles))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.resonance_sextupoles))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.main_sextupoles))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.correction_sextupoles))

        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.correction_octupoles))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.cavities))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.inj_kicker))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.ext_kicker))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.q_kicker))
      
if __name__ == '__main__':

  h = INIT_GENERIC_RING_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities

