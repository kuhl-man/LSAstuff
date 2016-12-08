from init_beamdiagnostic_devices import INIT_BEAMDIAGNOSTIC_DEVICES

class CRYRING_TEY1_DEVICES(INIT_BEAMDIAGNOSTIC_DEVICES):
    
    def __init__(self):
        INIT_BEAMDIAGNOSTIC_DEVICES.__init__(self)
        
        self._rigidity = 0.1
        self._accelerator_zone = "TEY1"

        self._main_dipoles = [ "GHTYMH2" ]
        self._main_quadrupoles = [ "GHTYQD21", "GHTYQD22", "GHTYQD31", "GHTYQD32" ]
       
        self._vertical_correctors   = [ "GHTYKV2" ]
        self._horizontal_correctors = [ "GHTYKH2" ]

        self._faraday_cups = [ "GHTYDC2", "GHTYDF2" ];

        INIT_BEAMDIAGNOSTIC_DEVICES.buildalldevices(self)
        INIT_BEAMDIAGNOSTIC_DEVICES.buildsystemmap(self)
        INIT_BEAMDIAGNOSTIC_DEVICES.buildlinkrulemap(self)       

        # CRYRING special

if __name__ == '__main__':

  h = CRYRING_TEY1_DEVICES()

  print h.main_dipoles
  print h.main_quadrupoles
  print h.vertical_correctors
  print h.horizontal_correctors
#  print h.cavities
  print h.faraday_cups

