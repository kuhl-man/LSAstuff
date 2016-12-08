from init_beamdiagnostic_devices import INIT_BEAMDIAGNOSTIC_DEVICES

class CRYRING_TYR1_DEVICES(INIT_BEAMDIAGNOSTIC_DEVICES):
    
    def __init__(self):
        INIT_BEAMDIAGNOSTIC_DEVICES.__init__(self)
        
        self._rigidity = 0.8
        self._accelerator_zone = "TYR1"

#	septa belong usually to injection / extraction line and are treated like main dipoles
#	use special septum makerule for electrostatic septa
        self._main_dipoles = [ "YRT1MH2", "YR01MP1" ]
        self._septa = [ "YR01LP1", "YR01LP2" ]
        self._main_quadrupoles = [ "GHTYQD41", "GHTYQD42" ]
        self._vertical_correctors   = [ "GHTYKV3"]

        self._faraday_cups = [ "GHTYDF3" ];

        INIT_BEAMDIAGNOSTIC_DEVICES.buildalldevices(self)
        INIT_BEAMDIAGNOSTIC_DEVICES.buildsystemmap(self)
        INIT_BEAMDIAGNOSTIC_DEVICES.buildlinkrulemap(self)       

        # CRYRING special

if __name__ == '__main__':

  h = CRYRING_TYR1_DEVICES()

  print h.main_dipoles
  print h.septa
  print h.main_quadrupoles
  print h.vertical_correctors
  print h.faraday_cups

