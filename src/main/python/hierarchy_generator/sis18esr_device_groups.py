from abc import ABCMeta, abstractproperty

from generic_device_groups import GenericDeviceGroups

class SIS18ESRDeviceGroups(GenericDeviceGroups):
  __metaclass__ = ABCMeta

    
  def __init__(self):
    pass

  @abstractproperty
  def old_cavities_ampl(self):
    pass

  @abstractproperty
  def old_cavities_freq(self):
    pass

  @abstractproperty
  def old_cavities_phase(self):
    pass

  @abstractproperty
  def horizontal_correction_coils(self):
    pass

  @abstractproperty
  def extraction_bump_correction_coils(self):
    pass
