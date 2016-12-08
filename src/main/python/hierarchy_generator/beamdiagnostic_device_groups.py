from abc import ABCMeta, abstractproperty

from generic_device_groups import GenericDeviceGroups

class BeamdiagnosticDeviceGroups(GenericDeviceGroups):
  __metaclass__ = ABCMeta

  def __init__(self):
    pass

  @abstractproperty
  def faraday_cups(self):
    pass

  @abstractproperty
  def septa(self):
    pass
