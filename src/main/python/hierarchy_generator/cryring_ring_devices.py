from init_sis18esr_devices import INIT_SIS18ESR_DEVICES
#from init_generic_devices import INIT_GENERIC_DEVICES --- had to be changed for horizontal corretion coils

class CRYRING_RING_DEVICES(INIT_SIS18ESR_DEVICES):
#class CRYRING_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
        INIT_SIS18ESR_DEVICES.__init__(self)
#        INIT_GENERIC_DEVICES.__init__(self)
        
        self._accelerator = "CRYRING"
        self._rigidity = 1.44
        self._particle_transfer = "CRYRING_RING"
        self._accelerator_zone = "CRYRING_RING"
        self._version = "1.0.0"

        self._main_dipoles = [ "YR00MH" ]
        self._main_quadrupoles = [ "YR00QS1", "YR00QS2" ]

#	correction, resonance, and chromaticity sextupoles are run differently; when the operation mode is clear, the type of sextupoles can be decided 
        self._chromaticity_sextupoles = [ "YR02KS1",  "YR02KS2", "YR04KS1", "YR04KS2", "YR06KS1", "YR06KS2", "YR08KS1", "YR08KS2", "YR10KS1", "YR10KS2", "YR12KS1", "YR12KS2" ]
        self._main_sextupoles = self._chromaticity_sextupoles
#       self._resonance_sextupoles = []
#       self._main_sextupoles = self._resonance_sextupoles
#       self._correction_sextupoles = [ "YR02KS1",  "YR02KS2", "YR04KS1", "YR04KS2", "YR06KS1", "YR06KS2", "YR08KS1", "YR08KS2", "YR10KS1", "YR10KS2", "YR12KS1", "YR12KS2" ]
#       self._main_sextupoles = self._correction_sextupoles
        
        self._vertical_correctors   = [ "YR02KV", "YR04KV", "YR07KV", "YR08KV", "YR10KV", "YR12KV" ]
        self._horizontal_correctors = [ "YR02KH", "YR04KH", "YR06KH", "YR08KH", "YR10KH", "YR12KH" ]

#	injection and extraction kicker magnets, will only be used once FESA interface is available (extraction), for transfer of ESR beam (injection)
        self._inj_kicker = [ "YR02MK1" ]
#       self._ext_kicker = [ "YR06MK1E" ]
#
        self._cavities = [ "YR05BE" ]
#
        self._horizontal_correction_coils =  [ "YR02KD" ] # corrects distortions caused by e-cooler
        
#	treat septa like main dipoles, if electrostatic, use special septum makerule!
#	move to extraction line?
#       self._main_dipoles = [ "YR06LP1E", "YR07MP1E" ]


        INIT_SIS18ESR_DEVICES.buildsystemmap(self)
#        INIT_GENERIC_DEVICES.buildsystemmap(self)

        # CRYRING special
        self._bumper = [ "YR01LB1K", "YR01LB30K" ] # for multi-turn injection

        self._devicesytemmap.update(dict((x, 'BUMPER') for x in self.bumper))
 
    @property
    def bumper(self):
      return self._bumper


if __name__ == '__main__':

  h = CRYRING_RING_DEVICES()

  print h.main_dipoles
  print h.main_quadrupoles
  print h.main_sextupoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.cavities
  print h.bumper
  print h.horizontal_correction_coils
