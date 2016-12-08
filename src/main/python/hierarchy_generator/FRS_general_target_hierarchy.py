from init_lh_builder import INIT_LH_BUILDER
from lh_builder import LHBuilder
from lh_builder_utils import LHBuilderUtils
#from _xmlplus.xpath.XPathParser import SELF
from FRS_device_groups import FRSDeviceGroups


class FRSGeneralTargetHierarchy():

    
  def __init__(self, devices):
     self.devices = devices
     self.reader = LHBuilderUtils()
     
  def generate_linkrules(self):
        
        print ('LinkRules:')
        for device in self.devices.alldevices:
            
            ##print (self.devices._devicelinkrulemap)
            if device in self.devices.devicelinkrulemap:
                linkrule = self.devices.devicelinkrulemap.get(device)
                
                self.lh_builder.lh.add_linkrule_for_device(device,linkrule)
                print (device , linkrule)

  def build(self):
      
     for device in self.devices.targetladders:
            system = self.devices.devicesystemmap.get(device)
            ein_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_IN','SCALAR_TARGET_EIN',device)
            inbeam_parameter = self.lh_builder.lh.define_physics_parameter(device + '/INBEAM','BOOLEAN_TARGET_INBEAM',device)
            material_parameter = self.lh_builder.lh.define_physics_parameter(device + '/MATERIAL','STRING_TARGET_MATERIAL',device)
            thickness_parameter = self.lh_builder.lh.define_physics_parameter(device + '/THICKNESS','SCALAR_TARGET_THICKNESS',device)
            areadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/AREADENSITY','SCALAR_TARGET_AREADENSITY',device)
            effectiveareadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/EFF_AREADENSITY','SCALAR_TARGET_EFFAREADENSITY',device)
            eout_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_OUT','SCALAR_TARGET_EOUT',device)
            index_parameter = self.lh_builder.lh.define_physics_parameter(device + '/INDEX','SCALAR_TARGET_INDEX',device)
            xpos_parameter = self.lh_builder.lh.define_physics_parameter(device + '/XPOS','SCALAR_TARGET_XPOS',device)
            ypos_parameter = self.lh_builder.lh.define_physics_parameter(device + '/YPOS','SCALAR_TARGET_YPOS',device)
           
           # brho_parameter = self.lh_builder.lh.define_physics_parameter(device + '/BRHO','SCALAR_BRHO',device)
            self.lh_builder.create_child_node(xpos_parameter, index_parameter)
            self.lh_builder.create_child_node(ypos_parameter, index_parameter)
            self.lh_builder.create_child_node(material_parameter, index_parameter)
            self.lh_builder.create_child_node(thickness_parameter, index_parameter)
            self.lh_builder.create_child_node(areadensity_parameter, index_parameter)

            self.lh_builder.create_child_node(eout_parameter, [material_parameter,ein_parameter,areadensity_parameter,effectiveareadensity_parameter,inbeam_parameter])   
            
            self.lh_builder.lh.add_parameter_to_system(index_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(xpos_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(ypos_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(ein_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(inbeam_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(material_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(thickness_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(areadensity_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(effectiveareadensity_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(eout_parameter, system) 
            
            
     for device in self.devices.targets:
            ein_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_IN','SCALAR_TARGET_EIN',device)
            inbeam_parameter = self.lh_builder.lh.define_physics_parameter(device + '/INBEAM','BOOLEAN_TARGET_INBEAM',device)
            material_parameter = self.lh_builder.lh.define_physics_parameter(device + '/MATERIAL','STRING_TARGET_MATERIAL',device)
            thickness_parameter = self.lh_builder.lh.define_physics_parameter(device + '/THICKNESS','SCALAR_TARGET_THICKNESS',device)
            areadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/AREADENSITY','SCALAR_TARGET_AREADENSITY',device)
            effectiveareadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/EFF_AREADENSITY','SCALAR_TARGET_EFFAREADENSITY',device)
            eout_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_OUT','SCALAR_TARGET_EOUT',device)
            self.lh_builder.create_child_node(eout_parameter, [material_parameter,ein_parameter,areadensity_parameter,effectiveareadensity_parameter,inbeam_parameter])   
            
            system = self.devices.devicesystemmap.get(device)
            self.lh_builder.lh.add_parameter_to_system(ein_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(inbeam_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(material_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(thickness_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(areadensity_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(effectiveareadensity_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(eout_parameter, system) 

            
     for device in self.devices.degraders:
            rotangle_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ROTANGLE','SCALAR_DEGRADER_ROTANGLE',device)
            ein_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_IN','SCALAR_TARGET_EIN',device)
            inbeam_parameter = self.lh_builder.lh.define_physics_parameter(device + '/INBEAM','BOOLEAN_TARGET_INBEAM',device)
            material_parameter = self.lh_builder.lh.define_physics_parameter(device + '/MATERIAL','STRING_TARGET_MATERIAL',device)
            eout_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_OUT','SCALAR_TARGET_EOUT',device)
            xpos_parameter = self.lh_builder.lh.define_physics_parameter(device + '/XPOS','SCALAR_TARGET_XPOS',device)
            angle_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ANGLE','SCALAR_TARGET_ANGLE',device)
            areadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/AREADENSITY','SCALAR_TARGET_AREADENSITY',device)
            effectiveareadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/EFF_AREADENSITY','SCALAR_TARGET_EFFAREADENSITY',device)
            self.lh_builder.create_child_node(effectiveareadensity_parameter, [xpos_parameter,angle_parameter,rotangle_parameter,areadensity_parameter])
            self.lh_builder.create_child_node(eout_parameter, [material_parameter,ein_parameter,areadensity_parameter,effectiveareadensity_parameter,inbeam_parameter])   
            
            system = self.devices.devicesystemmap.get(device)
            self.lh_builder.lh.add_parameter_to_system(areadensity_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(ein_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(inbeam_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(material_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(eout_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(xpos_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(rotangle_parameter,'generation')
            self.lh_builder.lh.add_parameter_to_system(angle_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(effectiveareadensity_parameter, system)
            
     for device in self.devices.degrader_disks:
            system = self.devices.devicesystemmap.get(device)
            ein_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_IN','SCALAR_TARGET_EIN',device)
            inbeam_parameter = self.lh_builder.lh.define_physics_parameter(device + '/INBEAM','BOOLEAN_TARGET_INBEAM',device)
            material_parameter = self.lh_builder.lh.define_physics_parameter(device + '/MATERIAL','STRING_TARGET_MATERIAL',device)
            eout_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_OUT','SCALAR_TARGET_EOUT',device)
            rotangle_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ROTANGLE','SCALAR_DEGRADER_ROTANGLE',device)
            xpos_parameter = self.lh_builder.lh.define_physics_parameter(device + '/XPOS','SCALAR_TARGET_XPOS',device)
            angle_parameter = self.lh_builder.lh.define_physics_parameter(device + '/ANGLE','SCALAR_TARGET_ANGLE',device)
            areadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/AREADENSITY','SCALAR_TARGET_AREADENSITY',device)
            effectiveareadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/EFF_AREADENSITY','SCALAR_TARGET_EFFAREADENSITY',device)
            self.lh_builder.create_child_node(effectiveareadensity_parameter, [xpos_parameter,angle_parameter,rotangle_parameter,areadensity_parameter])
            self.lh_builder.create_child_node(eout_parameter, [material_parameter,ein_parameter,areadensity_parameter,effectiveareadensity_parameter,inbeam_parameter])   
           
            system = self.devices.devicesystemmap.get(device)
            self.lh_builder.lh.add_parameter_to_system(areadensity_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(ein_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(inbeam_parameter, 'generation') 
            self.lh_builder.lh.add_parameter_to_system(material_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(eout_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(rotangle_parameter,'generation')
            self.lh_builder.lh.add_parameter_to_system(xpos_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(angle_parameter, 'generation')
            self.lh_builder.lh.add_parameter_to_system(effectiveareadensity_parameter, system)

            
  def buildTarget(self): 
            ein_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_IN','SCALAR_TARGET_EIN',device)
            inbeam_parameter = self.lh_builder.lh.define_physics_parameter(device + '/INBEAM','BOOLEAN_TARGET_INBEAM',device)
            material_parameter = self.lh_builder.lh.define_physics_parameter(device + '/MATERIAL','STRING_TARGET_MATERIAL',device)
            thickness_parameter = self.lh_builder.lh.define_physics_parameter(device + '/THICKNESS','SCALAR_TARGET_THICKNESS',device)
            areadensity_parameter = self.lh_builder.lh.define_physics_parameter(device + '/AREADENSITY','SCALAR_TARGET_AREADENSITY',device)
            eout_parameter = self.lh_builder.lh.define_physics_parameter(device + '/E_OUT','SCALAR_TARGET_EOUT',device)
            self.lh_builder.create_child_node(eout_parameter, [material_parameter,ein_parameter,areadensity_parameter,inbeam_parameter])   
            
            system = self.devices.devicesystemmap.get(device)
            self.lh_builder.lh.add_parameter_to_system(ein_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(inbeam_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(material_parameter, system)
            self.lh_builder.lh.add_parameter_to_system(thickness_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(areadensity_parameter, system) 
            self.lh_builder.lh.add_parameter_to_system(eout_parameter, system) 