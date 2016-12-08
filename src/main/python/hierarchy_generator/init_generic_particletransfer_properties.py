from generic_particletransfer_properties import GenericParticleTransferProperties

class INIT_GENERIC_PARTICLETRANSFER_PROPERTIES(GenericParticleTransferProperties):
    
    def __init__(self):
      self._accelerator = ""
      self._rigidity = 1
      self._particle_transfer = ""
      self._version = ""
      self._timing_device = ""

    ## generic properties
    @property
    def accelerator(self):
      return self._accelerator

    @property
    def particle_transfer(self):
      return self._particle_transfer

    @property
    def version(self):
      return self._version

    @property
    def timing_device(self):
      return self._timing_device
