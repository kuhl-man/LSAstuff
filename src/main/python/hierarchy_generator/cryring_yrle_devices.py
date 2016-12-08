from init_sis18esrcryring_devices import INIT_SIS18ESRCRYRING_DEVICES
#from init_generic_devices import INIT_GENERIC_DEVICES --- had to be changed for electrostatic quadrupoles

class CRYRING_YRLE_DEVICES(INIT_SIS18ESRCRYRING_DEVICES):
#class CRYRING_DEVICES(INIT_GENERIC_DEVICES):
    
    def __init__(self):
        INIT_SIS18ESRCRYRING_DEVICES.__init__(self)
#       INIT_GENERIC_DEVICES.__init__(self)
        
        self._rigidity = 0.029
        self._accelerator_zone = "YRLE"

        self._main_dipoles = [ "YRT1MH1" ]
#        self._main_quadrupoles = [ ]
        
        self._vertical_correctors   = [ "YRT1KV1" ]
        self._horizontal_correctors = [ "YRT1KH1" ];

        self._electrostatic_quadrupole =  [# "YRT1LE1", Einzel lens is controled by ion-source application
					    "YRT1LD21", "YRT1LD22",
					    "YRT1LT31", "YRT1LT32", "YRT1LT33",
					    "YRT1LT41", "YRT1LT42", "YRT1LT43"
					  ]
        self._chopper = [ "YRT1LC1_V" ]; # , "YRT1LQ11", "YRT1LQ12", "YRT1LQ13", "YRT1LQ14" ]

        self._faraday_cups = [ "YRT1DC2", "YRT1DF2", "YRT1DC3", "YRT1DF3" ];
#       self._faraday_cups = [ "YRT1DC2", "YRT1DF2MV", "YRT1DC3", "YRT1DF3MV",
#			       "YRT1DC6", "YRT1DF6MV", "YRT1DC7", "YRT1DF7MV" ];


        INIT_SIS18ESRCRYRING_DEVICES.buildalldevices(self)
        INIT_SIS18ESRCRYRING_DEVICES.buildsystemmap(self)
        INIT_SIS18ESRCRYRING_DEVICES.buildlinkrulemap(self)       

        # CRYRING special

if __name__ == '__main__':

  h = CRYRING_YRLE_DEVICES()

  print h.main_dipoles
#  print h.main_quadrupoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.electrostatic_quadrupole
  print h.chopper
  print h.faraday_cups


