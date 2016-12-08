from init_generic_transfer_devices import INIT_GENERIC_TRANSFER_DEVICES
#from init_generic_devices import INIT_GENERIC_DEVICES --- had to be changed for horizontal corretion coils

class TS3MU1_TO_HHD_DEVICES(INIT_GENERIC_TRANSFER_DEVICES):
#class CRYRING_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
        INIT_GENERIC_TRANSFER_DEVICES.__init__(self)
#        INIT_GENERIC_DEVICES.__init__(self)
        
        self._rigidity = 18.0
        self._accelerator_zone = "TS3MU1_TO_HHD"

        #self._main_dipoles = [ "GTS1MU1", "GTS1MU2", "GTS3MU1" ]
        #self._main_quadrupoles = [ "GTE1QD11", "GTE1QD12", "GTS1QD11", "GTS1QD12", "GTS2QT11", "GTS2QT12", "GTS2QT13" ]

#	correction, resonance, and chromaticity sextupoles are run differently; when the operation mode is clear, the type of sextupoles can be decided 
#       self._chromaticity_sextupoles = []
#       self._main_sextupoles = self._chromaticity_sextupoles
#       self._resonance_sextupoles = []
#       self._main_sextupoles = self._resonance_sextupoles
        #self._correction_sextupoles = [  "YR02KS1",  "YR02KS2", "YR04KS1", "YR04KS2", "YR06KS1", "YR06KS2", "YR08KS1", "YR08KS2", "YR10KS1", "YR10KS2", "YR12KS1", "YR12KS2" ]
        #self._main_sextupoles = self._correction_sextupoles
        
        #self._main_sextupoles = [ "GTS2KS1"]
        
        #self._septum = [ "GS04ME1E"]
        
        self._vertical_correctors   = [ "GHHDKY1", "GHHDKY2" ]
        self._horizontal_correctors = [ "GHHDKX1", "GHHDKX2" ]

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

  h = TS3MU1_TO_HHT_DEVICES()

  #print h.main_dipoles
  #print h.main_quadrupoles
  print h.vertical_correctors
  print h.horizontal_correctors
