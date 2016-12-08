from init_FRS_MAIN_devices import INIT_FRS_MAIN_DEVICES
from FRS_device_groups import FRSDeviceGroups
#from init_generic_devices import INIT_GENERIC_DEVICES --- had to be changed for horizontal corretion coils

class FRSS2_DEVICES(INIT_FRS_MAIN_DEVICES):
#class CRYRING_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
        INIT_FRS_MAIN_DEVICES.__init__(self)
#        INIT_GENERIC_DEVICES.__init__(self)
        
        self._accelerator = "SIS18"
        self._rigidity = 18.0
        self._accelerator_zone = "FRSS2"
        

        self._main_dipoles = [ "TS3MU2G" ]
        self._main_quadrupoles = [ "TS3QD21G", "TS3QD22G", "TS3QT31G", "TS3QT32G", "TS3QT33G" ]
        self._degraders = [ "TS3ED7VOG","TS3ED7OUG" ]
        self._degrader_disks = ["TS3ED7DSG","TS3ED7DPG"]
        self._targets = [ "TS3ET7GSG","TS3DB7LG","DetSC21","DetSC22","DetTPC21","DetTPC22" ]
        self._targetladders = ["TS3ET7RSG","TS3ET7LSG","TS3ET7USG","TS3ED7LSG"]

#	correction, resonance, and chromaticity sextupoles are run differently; when the operation mode is clear, the type of sextupoles can be decided 
        self._main_sextupoles = [ "TS3KS2G", "TS3KS3G" ]
#       self._main_sextupoles = self._chromaticity_sextupoles
#       self._resonance_sextupoles = []
#       self._main_sextupoles = self._resonance_sextupoles
        #self._correction_sextupoles = [  "YR02KS1",  "YR02KS2", "YR04KS1", "YR04KS2", "YR06KS1", "YR06KS2", "YR08KS1", "YR08KS2", "YR10KS1", "YR10KS2", "YR12KS1", "YR12KS2" ]
        #self._main_sextupoles = self._correction_sextupoles
        
       # self._main_sextupoles = [ "GTS2KS1"]
        
       # self._septum = [ "GS04ME1E"]
        
        self._vertical_correctors   = [ "TS3KY1G", "TS3KY2G" ]
       # self._horizontal_correctors = [ "GHHDKX1", "GHHDKX2" ]

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


        INIT_FRS_MAIN_DEVICES.buildalldevices(self)

        INIT_FRS_MAIN_DEVICES.buildsystemmap(self)
        INIT_FRS_MAIN_DEVICES.buildlinkrulemap(self)       



#        INIT_GENERIC_DEVICES.buildsystemmap(self)


if __name__ == '__main__':

  h = FRSS2_DEVICES()

  print h.main_dipoles
  print h.main_quadrupoles
  print h.vertical_correctors
  print h.chromaticity_sextupoles
