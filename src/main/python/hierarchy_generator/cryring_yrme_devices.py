from init_sis18esrcryring_devices import INIT_SIS18ESRCRYRING_DEVICES
# from init_beamdiagnostic_devices import INIT_BEAMDIAGNOSTIC_DEVICES --- had to be changed for electrostatic quadrupoles

class CRYRING_YRME_DEVICES(INIT_SIS18ESRCRYRING_DEVICES):
    
    def __init__(self):
        INIT_SIS18ESRCRYRING_DEVICES.__init__(self)
        
        self._rigidity = 0.079
        self._accelerator_zone = "YRME"

#        self._main_dipoles = [ ]
        self._main_quadrupoles = [ "YRT1QD61", "YRT1QD62", "YRT1QD71", "YRT1QD72" ]
       
        self._vertical_correctors   = [ "YRT1KV2" ]
        self._horizontal_correctors = [ "YRT1KH2" ]

        self._cavities = [ "YRT1BR1" ]

        self._electrostatic_quadrupole =  [ "YRT1LD51", "YRT1LD52" ];

        self._faraday_cups = [ "YRT1DC6", "YRT1DF6", "YRT1DC7", "YRT1DF7" ]; # moved to YRLE for timing reasons

        INIT_SIS18ESRCRYRING_DEVICES.buildalldevices(self)
        INIT_SIS18ESRCRYRING_DEVICES.buildsystemmap(self)
        INIT_SIS18ESRCRYRING_DEVICES.buildlinkrulemap(self)       

        # CRYRING special

if __name__ == '__main__':

  h = CRYRING_YRME_DEVICES()

#  print h.main_dipoles
  print h.main_quadrupoles
  print h.vertical_correctors
  print h.horizontal_correctors
  print h.cavities
  print h.electrostatic_quadrupole
  print h.faraday_cups

