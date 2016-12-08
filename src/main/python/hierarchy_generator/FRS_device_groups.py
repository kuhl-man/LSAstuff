from abc import ABCMeta, abstractproperty

from generic_device_groups import GenericDeviceGroups

class FRSDeviceGroups(GenericDeviceGroups):
  __metaclass__ = ABCMeta

    
  def __init__(self):
    pass

  @abstractproperty
  def targetladders(self):
    pass

  @abstractproperty
  def targets(self):
    pass

  @abstractproperty
  def degraders(self):
    pass

  @abstractproperty
  def degrader_disks(self):
    pass
