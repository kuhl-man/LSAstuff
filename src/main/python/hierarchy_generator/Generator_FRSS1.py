from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy

from init_lh_builder import INIT_LH_BUILDER

from FRSS1_properties import FRSS1_PROPERTIES

from FRSS1_devices import FRSS1_DEVICES

from devicedata_xml_parser import XMLParser

class GENERATOR_FRSS1(GenericTransferlineHierarchy,FRSGeneralTargetHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        self.standalone_acczone = False
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            FRSS1_properties = FRSS1_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, FRSS1_properties)
        
        FRSS1_device_groups = FRSS1_DEVICES()
        GenericTransferlineHierarchy.__init__(self, FRSS1_device_groups)
        FRSGeneralTargetHierarchy.__init__(self,FRSS1_device_groups)

        self.frss1_bp = True

    def __buildSpecial(self):
        # build special part of hierarchy for FRSS1
         FRSGeneralTargetHierarchy.build(self)
         #self.lh_builder.create_child_node('TS3ED2V1G/Q_OUT','FRSS1_BEAM/Q')
         self.lh_builder.create_child_node('TS3ED2V1G/E_IN','FRSS1_BEAM/E')
         self.lh_builder.create_child_node('TS3ED2V1G/E_OUT',['FRSS1_BEAM/ELEMENT','FRSS1_BEAM/ISOTOPE','FRSS1_BEAM/Q'])
         
         #self.lh_builder.create_child_node('TS3ED2O2G/Q_OUT','TS3ED2V1G/Q_OUT')
         self.lh_builder.create_child_node('TS3ED2O2G/E_IN','TS3ED2V1G/E_OUT')
         self.lh_builder.create_child_node('TS3ED2O2G/E_OUT',['FRSS1_BEAM/ELEMENT','FRSS1_BEAM/ISOTOPE','FRSS1_BEAM/Q'])
        
        
         for device in self.devices.main_dipoles + self.devices.main_quadrupoles + self.devices.main_sextupoles:
  
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters()) 
            
            #y_prec_I = self.y_prec_parser.findYPrec(device, 'I', 1)
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device,y_prec=5)
 
            self.lh_builder.create_child_node(i_parameter, bl_parameter)
           
            system = self.devices.devicesystemmap.get(device)
           
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)
 

    def build(self):
        
        # build generic part of hierarchy
        GenericTransferlineHierarchy.build(self)
        
        # build special part of hierarchy
        self.__buildSpecial()
        FRSGeneralTargetHierarchy.generate_linkrules(self)
        GenericTransferlineHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
    
    h2 = GENERATOR_FRSS1()
    h2.build()
    h2.generate()
