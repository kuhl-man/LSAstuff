from init_sis18esr_devices import INIT_SIS18ESR_DEVICES

_number_of_periods = 12

class SIS18_DEVICES(INIT_SIS18ESR_DEVICES):
    
    def __init__(self):
        INIT_SIS18ESR_DEVICES.__init__(self)
        
        self._rigidity = 18
        self._accelerator_zone = "SIS18_RING"

        self._main_dipoles = [ "GS11MU2" ]
        self._main_quadrupoles = [ "GS01QS1F", "GS12QS1F", "GS01QS2D", "GS12QS2D", "GS12QS3T" ]
        self._vertical_correctors = [ "GS%02dKM2DV" % period for period in range(1, _number_of_periods + 1) ]
        self._horizontal_correctors = []

        self._extraction_quadrupoles = [ "GS02KQ1E" ]
        self._correction_quadrupoles = [ "GS02KQ4" , "GS04KQ4" , "GS08KQ4", "GS10KQ4" , "GS01KM3QS" , "GS02KM3QS", "GS04KM3QS" , "GS06KM3QS" , "GS07KM3QS", "GS08KM3QS" , "GS10KM3QS", "GS12KM3QS"]

        #self._main_sextupoles = [ "S%02dKS%1dC" % (period1,period2) for period1 in range(1, _number_of_periods + 1 , 2) for period2 in range(1, 4, 2)]
        self._chromaticity_sextupoles = [ "GS%02dKS%1dC" % (period1,period2) for period1 in range(1, _number_of_periods + 1 , 2) for period2 in range(1, 4, 2)]
        #self._resonance_sextupoles = [ "S%02dKS1C" % period for period in range(1, _number_of_periods + 1 , 2) ]
        self._correction_sextupoles = [ "GS02KM5SS" , "GS08KM5SS" ]

        self._correction_octupoles = []

        self._cavities = []#[ "S07BE%d" % period for period in range(1, 4) ]

        self._ext_kicker = [ "GS04MK1E" , "S05MK2E" ]

        # SIS18/ESR special
        self._old_cavities_ampl = [ "GS02BE1A" , "GS08BE2A" , "GS07BE3A" , "GS07BE4A" , "GS07BE5A" ]
        self._old_cavities_freq = [ "GS02BE1F" , "GS08BE2F" , "GS07BE3F" , "GS07BE4F" , "GS07BE5F" ]
        self._old_cavities_phase = [ "GS02BE1P" , "GS08BE2P" , "GS07BE3P" , "GS07BE4P" , "GS07BE5P" ]

        self._horizontal_correction_coils =  [ "GS%02dMU1A" % period for period in range(1, _number_of_periods + 1) ] + [ "GS%02dMU2A" % period for period in range(4, 8) ] + [ "GS%02dMU2A" % period for period in range(10, _number_of_periods + 1) ]
        self._extraction_bump_correction_coils = [ "GS%02dMU1A" % period for period in range(4, 7, 2) ] + [ "GS%02dMU2A" % period for period in range(5, 8, 2) ] + [ "GS%02dMU2A" % period for period in range(10, _number_of_periods + 1) ]

        INIT_SIS18ESR_DEVICES.buildalldevices(self)

        INIT_SIS18ESR_DEVICES.buildsystemmap(self)
        INIT_SIS18ESR_DEVICES.buildlinkrulemap(self)       
      
        # SIS18 special
        self._extra_correction_coils = list(set([ "GS%02dMU1A" % period for period in range(1, 4) ] + ["GS05MU1A"] + [ "GS%02dMU1A" % period for period in range(7, 10) ] + [ "GS12MU1A"] + [ "GS04MU2A"] + ["GS06MU2A"]).intersection(set(self._horizontal_correction_coils)))

        self._bumper = [ "GS01MB3" , "GS03MB4" , "GS11MB1" , "GS12MB2" ]

        self._sis18_bypass = [ "GS06MU4" ]
        self._sis18_ko_exiter = [ "GS01BO1EH" ]
        
        self._sis18_bunch_compressor_cavity = [ "GS02BB1F" ]
        
        self._alldevices = self.alldevices + self._extra_correction_coils + self._bumper + self._sis18_bypass + self._sis18_ko_exiter + self._sis18_bunch_compressor_cavity
        
        self._devicesytemmap.update(dict((x, 'CORRH') for x in self.extra_correction_coils))
        self._devicesytemmap.update(dict((x, 'BUMPER') for x in self.bumper))
        self._devicesytemmap.update(dict((x, 'BYPASS') for x in self.sis18_bypass))
        self._devicesytemmap.update(dict((x, 'KO') for x in self.sis18_ko_exiter))

        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.extra_correction_coils))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.bumper))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.sis18_bypass))
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.sis18_ko_exiter))
        
        self._devicelinkrulemap.update(dict((x, 'RAMPLR') for x in self.sis18_bunch_compressor_cavity))

    @property
    def extra_correction_coils(self):
      return self._extra_correction_coils

    @property
    def bumper(self):
      return self._bumper

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
    def sis18_bypass(self):
      return self._sis18_bypass

    @property
    def sis18_ko_exiter(self):
      return self._sis18_ko_exiter
  
    @property
    def sis18_bunch_compressor_cavity(self):
      return self._sis18_bunch_compressor_cavity


if __name__ == '__main__':

  h = SIS18_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities
