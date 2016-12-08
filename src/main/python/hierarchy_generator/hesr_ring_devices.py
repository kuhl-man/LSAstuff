from init_sis18esr_devices import INIT_SIS18ESR_DEVICES
#from init_generic_devices import INIT_GENERIC_DEVICES --- had to be changed for horizontal corretion coils

class HESR_RING_DEVICES(INIT_SIS18ESR_DEVICES):
#class CRYRING_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
        INIT_SIS18ESR_DEVICES.__init__(self)
#        INIT_GENERIC_DEVICES.__init__(self)
        
        self._rigidity = 50.
        self._accelerator_zone = "HESR_RING"

        self._main_dipoles = [ "HR08MH01.GN" , "HR18MH23.GN" ]
        self._main_quadrupoles = [ "HR03QTA3D.GN" , "HR03QTA3F.GN" , "HR05QTA4D.GN" , "HR05QTA4F.GN" , "HR08QSA0D.GN" , "HR08QSA1D.GN" ,
				   "HR08QSA1F.GN" , "HR09QSA2D.GN" , "HR09QSA2F.GN" , "HR09QSA3D.GN" , "HR09QSA3F.GN" , "HR12QTA5D.GN" ,
				   "HR12QTA5F.GN" , "HR14QTA6D.GN" , "HR14QTA6F.GN" , "HR18QSA4D.GN" , "HR18QSA5D.GN" , "HR18QSA5F.GN" ,
				   "HR19QSA6D.GN" , "HR19QSA6F.GN" , "HR19QSA7D.GN" , "HR19QSA7F.GN" , "HR22QTA1D.GN" , "HR22QTA1F.GN" , "HR22QTA2F.GN" ]

#	correction, resonance, and chromaticity sextupoles are run differently; when the operation mode is clear, the type of sextupoles can be decided 
#       self._chromaticity_sextupoles = []
#       self._main_sextupoles = self._chromaticity_sextupoles
#       self._resonance_sextupoles = []
#       self._main_sextupoles = self._resonance_sextupoles
        self._correction_sextupoles = [ "HR01KS01.GN" , "HR03KS02.GN" , "HR03KS03.GN" , "HR05KS04.GN" , "HR05KS05.GN" , "HR07KS06.GN" , "HR08KSA1H.GN" ,
					"HR08KSA1V.GN" , "HR09KSA2H.GN" , "HR09KSA2V.GN" , "HR10KSA3H.GN" , "HR10KSA3V.GN" , "HR10KSA4H.GN" , "HR11KSA4V.GN" ,
					"HR12KS07.GN" , "HR14KS08.GN" , "HR14KS09.GN" , "HR17KS10.GN" , "HR17KS11.GN" , "HR18KS12.GN" , "HR18KSA5H.GN" ,
					"HR18KSA5V.GN" , "HR19KSA6H.GN" , "HR19KSA6V.GN" , "HR20KSA7H.GN" , "HR20KSA7V.GN" , "HR20KSA8H.GN" , "HR21KSA8V.GN" ]
        self._main_sextupoles = self._correction_sextupoles
        
#	all steerers
#	"HR08KV1.GN" , "HR09KH1.GN" , "HR09KV2.GN" , "HR09KH2.GN" , "HR10KV1.GN" , "HR10KH1.GN" , "HR10KH2.GN" , "HR10KV2.GN" ,
#	"HR11KH1.GN" , "HR11KV1.GN" , "HR11KH2.GN" , "HR12KV1.GN" , "HR12KH1.GN" , "HR12KV2.GN" , "HR14KH1.GN" , "HR14KV1.GN" ,
#	"HR14KH2.GN" , "HR14KV2.GN" , "HR14KH3.GN" , "HR14KV3.GN" , "HR17KH1.GN" , "HR17KV1.GN" , "HR17KH1H.GN" , "HR17KH2.GN" ,
#	"HR17KV2.GN" , "HR17KH2H.GN" , "HR17KH3H.GN" , "HR17KH3.GN" , "HR17KV3.GN" , "HR17KH4H.GN" , "HR18KH1.GN" , "HR18KV1.GN" ,
#	"HR18KV2.GN" , "HR19KH1.GN" , "HR19KV1.GN" , "HR19KH2.GN" , "HR20KV1.GN" , "HR20KH1.GN" , "HR20KH2.GN" , "HR20KV2.GN" ,
#	"HR21KH1.GN" , "HR21KV1.GN" , "HR21KH2.GN" , "HR22KV1.GN" , "HR01KH1.GN" , "HR01KV1.GN" , "HR03KH1.GN" , "HR03KV1.GN" ,
#	"HR03KH2.GN" , "HR03KV2.GN" , "HR05KH1.GN" , "HR05KV1.GN" , "HR05KH2.GN" , "HR05KV2.GN" , "HR07KV1.GN" , "HR07KH1.GN" , "HR17KV3.GN"

        self._vertical_correctors   = [ "HR08KV1.GN" , "HR09KV2.GN" , "HR10KV1.GN" , "HR10KV2.GN" , "HR11KV1.GN" , "HR12KV1.GN" , "HR12KV2.GN" , "HR14KV1.GN" ,
					"HR14KV2.GN" , "HR14KV3.GN" , "HR17KV1.GN" , "HR17KV2.GN" , "HR17KV3.GN" , "HR18KV1.GN" , "HR18KV2.GN" , "HR19KV1.GN" ,
					"HR20KV1.GN" , "HR20KV2.GN" , "HR21KV1.GN" , "HR22KV1.GN" , "HR01KV1.GN" , "HR03KV1.GN" , "HR03KV2.GN" , "HR05KV1.GN" , 
					"HR05KV2.GN" , "HR07KV1.GN" , "HR17KV3.GN" ] 
        self._horizontal_correctors = [ "HR09KH1.GN" , "HR09KH2.GN" , "HR10KH1.GN" , "HR10KH2.GN" , "HR11KH1.GN" , "HR11KH2.GN" , "HR12KH1.GN" , "HR14KH1.GN" ,
					"HR14KH2.GN" , "HR14KH3.GN" , "HR17KH1.GN" , "HR17KH1H.GN" , "HR17KH2.GN" , "HR17KH2H.GN" , "HR17KH3H.GN" , "HR17KH3.GN" ,
					"HR17KH4H.GN" , "HR18KH1.GN" , "HR19KH1.GN" , "HR19KH2.GN" , "HR20KH1.GN" , "HR20KH2.GN" , "HR21KH1.GN" , "HR21KH2.GN" , 
					"HR01KH1.GN" , "HR03KH1.GN" , "HR03KH2.GN" , "HR05KH1.GN" , "HR05KH2.GN" , "HR07KH1.GN" ]

#	injection and extraction kicker magnets, will only be used once FESA interface is available (extraction), for transfer of ESR beam (injection)
#        self._inj_kicker = [ "YR02MK1" ]
#       self._ext_kicker = [ "YR06MK1E" ]
#
#        self._cavities = [ "YR05BE" ]
#
#        self._horizontal_correction_coils =  [ "YR02KD" ] # corrects distortions caused by e-cooler
        
#	treat septa like main dipoles, if electrostatic, use special septum makerule!
#	move to extraction line?
#       self._main_dipoles = [ "YR06LP1E", "YR07MP1E" ]


        INIT_SIS18ESR_DEVICES.buildsystemmap(self)
#        INIT_GENERIC_DEVICES.buildsystemmap(self)

        INIT_SIS18ESR_DEVICES.buildalldevices(self)
        
        INIT_SIS18ESR_DEVICES.buildlinkrulemap(self)


        # CRYRING special
#        self._bumper = [ "YR01LB" ] # for multi-turn injection
#
#        self._devicesytemmap.update(dict((x, 'BUMPER') for x in self.bumper))
# 
#    @property
#    def bumper(self):
#      return self._bumper


if __name__ == '__main__':

  h = HESR_RING_DEVICES()

  print h.main_dipoles
  print h.main_quadrupoles
  print h.main_sextupoles
  print h.vertical_correctors
  print h.horizontal_correctors
#  print h.cavities
#  print h.bumper
#  print h.horizontal_correction_coils
