from init_generic_ring_devices import INIT_GENERIC_RING_DEVICES

_number_of_sections = 6
_number_of_cells = 14

class SIS100_DEVICES(INIT_GENERIC_RING_DEVICES):
    
    def __init__(self):
        INIT_GENERIC_RING_DEVICES.__init__(self)
        
        self._rigidity = 100
        self._accelerator_zone = "SIS100_RING"
        self._main_dipoles = [ "1S00MH" ]
        self._main_quadrupoles = [ "1S00QD1D", "1S00QD1F", "1S00QD2F", "1S52QD11", "1S52QD12" ]
        
        self._vertical_correctors = list(set([ "1S%d%XKV1" % (period1, period2) for period1 in range(1, _number_of_sections + 1) for period2 in range(1, _number_of_cells + 1)]) - set(["1S52KV1"]))
        self._horizontal_correctors = list(set([ "1S%d%XKH1" % (period1, period2) for period1 in range(1, _number_of_sections + 1) for period2 in range(1, _number_of_cells + 1)]) - set(["1S52KH1"]))

        self._extraction_quadrupoles = [ "1S13QS1E" ]
        self._correction_quadrupoles = [ "1S%d%XKM1Q" % (period1, period2) for period1 in range(1, _number_of_sections + 1) for period2 in [4,14]]

        self._chromaticity_sextupoles = [ "1S00KS%dC%s" % (period1,period2) for period1 in range(1, 4) for period2 in ["H","V"]] +  ["1S00KS4CH"]
        self._resonance_sextupoles = [ "1S%d4KS1E"  % period1 for period1 in range(1, _number_of_sections + 1)  ]
        self._main_sextupoles = self._resonance_sextupoles + self._chromaticity_sextupoles
        self._correction_sextupoles = [ "1S%d%XKM1S"  % (period1,period2) for period1 in range(1, _number_of_sections + 1) for period2 in [4,14] ]

        self._correction_octupoles = [ "1S%d%XKM1O"  % (period1,period2) for period1 in range(1, _number_of_sections + 1) for period2 in [4,14] ]

        self._cavities = [ "1S%d%dBE%d"  % (period1,period2,period3) for period1 in [2, 3] for period2 in range (1,5) for period3 in range(1,3) ] + [ "1S6%dBE%d"  % (period4,period5) for period4 in range (3,5) for period5 in range(1,3) ]

        #self._kicker = [ "1S51MK%dE"  % period1 for period1 in range (1, 4) ] + [  "1S52MK%dE"  % period1 for period1 in range (4, 6) ] + [  "1S53MK%dE"  % period1 for period1 in range (6, 9) ]
        self._ext_kicker = list(set([ "1S5%dMK%dE"  % (period1,period2) for period1 in range(1, 4) for period2 in range (1, 4) ]) - set(["1S52MK3E"]))
        self._q_kicker = [ "1S13MK1Q" , "1S13MK2Q" ]

        INIT_GENERIC_RING_DEVICES.buildalldevices(self)
        
        INIT_GENERIC_RING_DEVICES.buildsystemmap(self)
        INIT_GENERIC_RING_DEVICES.buildlinkrulemap(self)
        
        # SIS100 special
        self._t_kicker = []
        
        self._alldevices = self.alldevices + self._t_kicker
        
        self._devicesytemmap.update(dict((x, 'KICKER') for x in self.t_kicker))

    # SIS100 special
    @property
    def t_kicker(self):
      return self._t_kicker

if __name__ == '__main__':

  h = SIS100_DEVICES()

  print h.main_dipoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.correction_quadrupoles
  print h.main_sextupoles
  print h.cavities
