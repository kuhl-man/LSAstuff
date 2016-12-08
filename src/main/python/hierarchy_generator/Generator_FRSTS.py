from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from FRS_device_groups import FRSDeviceGroups
from init_lh_builder import INIT_LH_BUILDER
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy
from FRSTS_properties import FRSTS_PROPERTIES

from FRSTS_devices import FRSTS_DEVICES

from devicedata_xml_parser import XMLParser

class GENERATOR_FRSTS(GenericTransferlineHierarchy,FRSGeneralTargetHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        self.standalone_acczone = False
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            FRSTS_properties = FRSTS_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, FRSTS_properties)
        
        FRSTS_device_groups = FRSTS_DEVICES()
        GenericTransferlineHierarchy.__init__(self, FRSTS_device_groups)
        FRSGeneralTargetHierarchy.__init__(self,FRSTS_device_groups)
        self.frsts_bp = True

    def __buildSpecial(self):
        # build special part of hierarchy for FRSS1
         
         self.lh_builder.create_child_node('TS1ET5G/E_IN','FRSTS_BEAM/E')
         self.lh_builder.create_child_node('TS1ET5G/E_OUT',['FRSTS_BEAM/ELEMENT','FRSTS_BEAM/ISOTOPE','FRSTS_BEAM/Q'])
         #self.lh_builder.create_child_node('TS1ET5G/Q_OUT','FRSTS_BEAM/Q')
         
         self.lh_builder.create_child_node('TS2ET1G/E_IN','TS1ET5G/E_OUT')
         self.lh_builder.create_child_node('TS2ET1G/E_OUT',['FRSTS_BEAM/ELEMENT','FRSTS_BEAM/ISOTOPE','FRSTS_BEAM/Q'])
         #self.lh_builder.create_child_node('TS2ET1G/Q_OUT','TS1ET5G/Q_OUT')
         
         self.lh_builder.create_child_node('TS2ET2G/E_IN','TS2ET1G/E_OUT')
         self.lh_builder.create_child_node('TS2ET2G/E_OUT',['FRSTS_BEAM/ELEMENT','FRSTS_BEAM/ISOTOPE','FRSTS_BEAM/Q'])
         #self.lh_builder.create_child_node('TS2ET2G/Q_OUT','TS2ET1G/Q_OUT')
         self.lh_builder.lh.add_parameter_to_system('FRSTS_BEAM/E', 'generation')
        
         for device in self.devices.main_dipoles + self.devices.main_quadrupoles +self.devices.vertical_correctors:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
 
            #y_prec_I = self.y_prec_parser.findYPrec(device, 'I', 1)
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device,y_prec=5)
 
            self.lh_builder.create_child_node(i_parameter, bl_parameter)
           
            system = self.devices.devicesystemmap.get(device)
           
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)
   
    def build(self):
        
        # build generic part of hierarchy
        GenericTransferlineHierarchy.build(self)
        FRSGeneralTargetHierarchy.build(self)
        
        # build special part of hierarchy
        self.__buildSpecial()
        FRSGeneralTargetHierarchy.generate_linkrules(self)
        GenericTransferlineHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
    
    h2 = GENERATOR_FRSTS()
    h2.build()
    h2.generate()