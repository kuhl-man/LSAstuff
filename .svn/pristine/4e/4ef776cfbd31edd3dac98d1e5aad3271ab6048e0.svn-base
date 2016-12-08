from init_sis18esr_devices import INIT_SIS18ESR_DEVICES

class ESR_DEVICES(INIT_SIS18ESR_DEVICES):
    
    def __init__(self):
        INIT_SIS18ESR_DEVICES.__init__(self)
        
        self._rigidity = 18
        self._accelerator_zone = "ESR_RING"

        self._main_dipoles = [ "GE01MU1" ]
        self._main_quadrupoles = [ "GE01QS0D", "GE01QS1F", "GE01QS2F" , "GE01QS3D" , "GE01QS4F" , "GE01QS5F" , "GE01QS6D" , "GE01QS7F" , "GE01QS8F" , "GE01QS9D" ]
        self._vertical_correctors = [ "GE0%dKY%d" % (period1, period2) for period1 in range(1, 3) for period2 in range(1, 5)]

        self._main_sextupoles = [ "GE0%dKS%d" % (period1, period2) for period1 in range(1, 3) for period2 in range(1, 5)]
        self._chromaticity_sextupoles = self._main_sextupoles

        # ESR/SIS18 special
        self._old_cavities_ampl = [ "GE02BE1A" ]
        self._old_cavities_freq = [ "GE02BE1FS" ]
        self._old_cavities_phase = [ "GE02BE1PD"]

        self._horizontal_correction_coils =  [ "GE0%dKX%d" % (period1, period2) for period1 in range(1, 3) for period2 in range(1, 7)]
        
        INIT_SIS18ESR_DEVICES.buildalldevices(self)

        INIT_SIS18ESR_DEVICES.buildsystemmap(self)
        INIT_SIS18ESR_DEVICES.buildlinkrulemap(self)       
        
        # ESR special
        self._polefacewindings = [ "GE01KP%02d" % period for period in range(2, 11) ] + [ "GE01KP%02d" % period for period in range(17, 25) ]

        self._alldevices = self.alldevices + self._polefacewindings

        self._devicesytemmap.update(dict((x, 'NOSYSTEM') for x in self.polefacewindings))

    @property
    def polefacewindings(self):
      return self._polefacewindings


        
if __name__ == '__main__':

  h = ESR_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities
  print h.polefacewindings
