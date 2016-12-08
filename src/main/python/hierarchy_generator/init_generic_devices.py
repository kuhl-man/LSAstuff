from generic_device_groups import GenericDeviceGroups

class INIT_GENERIC_DEVICES(GenericDeviceGroups):
    
    def __init__(self):
      self._rigidity = 1
      self._accelerator_zone = ""
      self._main_dipoles = []
      self._main_quadrupoles = []
      self._vertical_correctors = []
      self._horizontal_correctors = []

      self._extraction_quadrupoles = []
      self._correction_quadrupoles = []

      self._main_sextupoles = []
      self._chromaticity_sextupoles = []
      self._resonance_sextupoles = []
      self._correction_sextupoles = []

      self._correction_octupoles = []

      self._cavities = []

      self._inj_kicker = []
      self._ext_kicker = []
      self._q_kicker = []
      
      self._septum = []
      
      self._alldevices = []
      
      self._devicesytemmap = {}
      self._devicelinkrulemap = {}
      
    def buildalldevices(self):
        self._alldevices = self.main_dipoles + self.main_quadrupoles + self.vertical_correctors + self.horizontal_correctors + self.extraction_quadrupoles + self.correction_quadrupoles + self.main_sextupoles + self.chromaticity_sextupoles + self.resonance_sextupoles + self.correction_sextupoles + self.cavities + self.inj_kicker + self.ext_kicker + self.q_kicker + self.septum
        
    def buildsystemmap(self):
        self._devicesytemmap = dict((x, 'DIPOLE') for x in self.main_dipoles)
        self._devicesytemmap.update(dict((x, 'QUADRUPOLE') for x in self.main_quadrupoles))
        self._devicesytemmap.update(dict((x, 'CORRV') for x in self.vertical_correctors))
        self._devicesytemmap.update(dict((x, 'CORRH') for x in self.horizontal_correctors))
        self._devicesytemmap.update(dict((x, 'QUADRUPOLE') for x in self.extraction_quadrupoles))
        self._devicesytemmap.update(dict((x, 'QUADCORR') for x in self.correction_quadrupoles))

        self._devicesytemmap.update(dict((x, 'SEXTUPOLE') for x in self.chromaticity_sextupoles))
        self._devicesytemmap.update(dict((x, 'SEXTUPOLE') for x in self.resonance_sextupoles))
        self._devicesytemmap.update(dict((x, 'SEXTUPOLE') for x in self.main_sextupoles))
        self._devicesytemmap.update(dict((x, 'SEXTUPOLE') for x in self.correction_sextupoles))

        self._devicesytemmap.update(dict((x, 'OCTUPOLE') for x in self.correction_octupoles))
        self._devicesytemmap.update(dict((x, 'RF') for x in self.cavities))
        self._devicesytemmap.update(dict((x, 'KICKER') for x in self.inj_kicker))
        self._devicesytemmap.update(dict((x, 'KICKER') for x in self.ext_kicker))
        self._devicesytemmap.update(dict((x, 'KICKER') for x in self.q_kicker))
        
        self._devicesytemmap.update(dict((x, 'SEPTUM') for x in self.septum))

    ## generic properties
    @property
    def rigidity(self):
      return self._rigidity

    @property
    def accelerator_zone(self):
      return self._accelerator_zone
    
    @property
    def main_dipoles(self):
      return self._main_dipoles

    @property
    def main_quadrupoles(self):
      return self._main_quadrupoles

    @property
    def horizontal_correctors(self):
      return self._horizontal_correctors

    @property
    def vertical_correctors(self):
      return self._vertical_correctors

    @property
    def extraction_quadrupoles(self):
      return self._extraction_quadrupoles

    @property
    def correction_quadrupoles(self):
      return self._correction_quadrupoles

    @property
    def main_sextupoles(self):
      return self._main_sextupoles

    @property
    def chromaticity_sextupoles(self):
      return self._chromaticity_sextupoles

    @property
    def resonance_sextupoles(self):
      return self._resonance_sextupoles

    @property
    def correction_sextupoles(self):
      return self._correction_sextupoles

    @property
    def correction_octupoles(self):
      return self._correction_octupoles

    @property
    def cavities(self):
      return self._cavities

    @property
    def inj_kicker(self):
      return self._inj_kicker

    @property
    def ext_kicker(self):
      return self._ext_kicker

    @property
    def q_kicker(self):
      return self._q_kicker
  
    @property
    def septum(self):
      return self._septum

    @property
    def alldevices(self):
      return self._alldevices

    @property
    def devicesystemmap(self):
      return self._devicesytemmap

    @property
    def devicelinkrulemap(self):
      return self._devicelinkrulemap
