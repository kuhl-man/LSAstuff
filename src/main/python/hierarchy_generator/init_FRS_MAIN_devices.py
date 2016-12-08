from init_generic_devices import INIT_GENERIC_DEVICES
from FRS_device_groups import FRSDeviceGroups

class INIT_FRS_MAIN_DEVICES(INIT_GENERIC_DEVICES, FRSDeviceGroups):
    
    def __init__(self):
      INIT_GENERIC_DEVICES.__init__(self)
      self._targetladders = []
      self._targets = []
      self._degraders = []
      self._degrader_disks = []

    def buildalldevices(self):
        self._alldevices = self.main_dipoles + self.main_quadrupoles + self.vertical_correctors + self.horizontal_correctors + self.extraction_quadrupoles + self.correction_quadrupoles + self.main_sextupoles + self.chromaticity_sextupoles + self.resonance_sextupoles + self.correction_sextupoles + self.cavities + self.inj_kicker + self.ext_kicker + self.q_kicker + self.septum + self.targetladders + self.targets + self.degraders + self.degrader_disks

    def buildsystemmap(self):
        INIT_GENERIC_DEVICES.buildsystemmap(self)
        self._devicesytemmap.update(dict((x, 'TARGETLADDER') for x in self.targetladders))
        self._devicesytemmap.update(dict((x, 'TARGET') for x in self.targets))
        self._devicesytemmap.update(dict((x, 'DEGRADER') for x in self.degraders))
        self._devicesytemmap.update(dict((x, 'DEGRADER_DISK') for x in self.degrader_disks))

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
        
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.targetladders))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.targets))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.degraders))
        self._devicelinkrulemap.update(dict((x, 'DEFAULTLR') for x in self.degrader_disks))
        
    @property
    def targetladders(self):
      return self._targetladders
  
    @property
    def targets(self):
      return self._targets
  
    @property
    def degraders(self):
      return self._degraders
  
    @property
    def degrader_disks(self):
      return self._degrader_disks
      
if __name__ == '__main__':

  h = INIT_GENERIC_TRANSFER_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities

