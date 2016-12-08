from init_generic_transfer_devices import INIT_GENERIC_TRANSFER_DEVICES
#from init_generic_devices import INIT_GENERIC_DEVICES --- had to be changed for horizontal corretion coils

class FRSTEST_TH_HHT_DEVICES(INIT_GENERIC_TRANSFER_DEVICES):
#class CRYRING_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
        INIT_GENERIC_TRANSFER_DEVICES.__init__(self)
#        INIT_GENERIC_DEVICES.__init__(self)
        
        self._accelerator = "SIS18"
        self._rigidity = 18.0
        self._particle_transfer = "FRSTEST"
        self._version = "1.0.0"

        self._main_dipoles = [ "TESTFRSD" ]
        self._main_quadrupoles = [ "TESTFRSD" ]

#	correction, resonance, and chromaticity sextupoles are run differently; when the operation mode is clear, the type of sextupoles can be decided 
#       self._chromaticity_sextupoles = []
#       self._main_sextupoles = self._chromaticity_sextupoles
#       self._resonance_sextupoles = []
#       self._main_sextupoles = self._resonance_sextupoles
        #self._correction_sextupoles = [  "YR02KS1",  "YR02KS2", "YR04KS1", "YR04KS2", "YR06KS1", "YR06KS2", "YR08KS1", "YR08KS2", "YR10KS1", "YR10KS2", "YR12KS1", "YR12KS2" ]
        #self._main_sextupoles = self._correction_sextupoles

     #   self._septum = [ "GS04ME1E"]
        
      #  self._vertical_correctors   = [ "GTE1KY1", "GTH1KY1" ]
       # self._horizontal_correctors = [ "GTE2KX1", "GTH1KX1" ]

#	injection and extraction kicker magnets, will only be used once FESA interface is available (extraction), for transfer of ESR beam (injection)
        #self._inj_kicker = [ "YR02MK1" ]
#       self._ext_kicker = [ "YR06MK1E" ]
#
        #self._cavities = [ "YR05BE" ]
#
        #self._horizontal_correction_coils =  [ "YR02KD" ] # corrects distortions caused by e-cooler
        
#	treat septa like main dipoles, if electrostatic, use special septum makerule!
#	move to extraction line?
#       self._main_dipoles = [ "YR06LP1E", "YR07MP1E" ]


        INIT_GENERIC_TRANSFER_DEVICES.buildalldevices(self)

        INIT_GENERIC_TRANSFER_DEVICES.buildsystemmap(self)
        INIT_GENERIC_TRANSFER_DEVICES.buildlinkrulemap(self)       



#        INIT_GENERIC_DEVICES.buildsystemmap(self)


if __name__ == '__main__':

  h = FRSTEST_TH_HHT_DEVICES()

  print h.main_dipoles
  print h.main_quadrupoles
  print h.vertical_correctors
  print h.horizontal_correctors
