from sis18esr_device_groups import SIS18ESRDeviceGroups
from init_generic_ring_devices import INIT_GENERIC_RING_DEVICES

class INIT_SIS18ESR_DEVICES(INIT_GENERIC_RING_DEVICES,SIS18ESRDeviceGroups):
    
    def __init__(self):
      INIT_GENERIC_RING_DEVICES.__init__(self)

      # ESR/SIS18 special
      self._old_cavities_ampl = []
      self._old_cavities_freq = []
      self._old_cavities_phase = []

      self._horizontal_correction_coils =  []
      self._extraction_bump_correction_coils = []


    def buildalldevices(self):
        INIT_GENERIC_RING_DEVICES.buildalldevices(self)
        self._alldevices = self.alldevices + self.old_cavities_ampl + self.old_cavities_freq + self.old_cavities_phase + self.horizontal_correction_coils + self.extraction_bump_correction_coils

    def buildsystemmap(self):
        INIT_GENERIC_RING_DEVICES.buildsystemmap(self)
        self._devicesytemmap.update(dict((x, 'RF') for x in self.old_cavities_ampl))
        self._devicesytemmap.update(dict((x, 'RF') for x in self.old_cavities_freq))
        self._devicesytemmap.update(dict((x, 'RF') for x in self.old_cavities_phase))
        self._devicesytemmap.update(dict((x, 'CORRH') for x in self.horizontal_correction_coils))
        self._devicesytemmap.update(dict((x, 'CORRH') for x in self.extraction_bump_correction_coils))

    def buildlinkrulemap(self):
        INIT_GENERIC_RING_DEVICES.buildlinkrulemap(self)
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.old_cavities_ampl))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.old_cavities_freq))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.old_cavities_phase))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.horizontal_correction_coils))
        self._devicelinkrulemap.update(dict((x, 'ZEROLR') for x in self.extraction_bump_correction_coils))

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

      
if __name__ == '__main__':

  h = INIT_SIS18ESR_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities

