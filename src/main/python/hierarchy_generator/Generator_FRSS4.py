from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy

from init_lh_builder import INIT_LH_BUILDER

from FRSS4_properties import FRSS4_PROPERTIES

from FRSS4_devices import FRSS4_DEVICES

from devicedata_xml_parser import XMLParser

class GENERATOR_FRSS4(GenericTransferlineHierarchy,FRSGeneralTargetHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        self.standalone_acczone = False
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            FRSS4_properties = FRSS4_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, FRSS4_properties)
        
        FRSS4_device_groups = FRSS4_DEVICES()
        GenericTransferlineHierarchy.__init__(self, FRSS4_device_groups)
        FRSGeneralTargetHierarchy.__init__(self,FRSS4_device_groups)

        self.FRSS4_bp = True

    def __buildSpecial(self):
        # build special part of hierarchy for FRSS4
         FRSGeneralTargetHierarchy.build(self)
         #self.lh_builder.create_child_node('TS3ED2V1G/Q_OUT','FRSS4_BEAM/Q')
         self.lh_builder.create_child_node('HFSED3VOG/E_IN','FRSS4_BEAM/E')
         self.lh_builder.create_child_node('HFSED3VOG/E_OUT',['FRSS4_BEAM/ELEMENT','FRSS4_BEAM/ISOTOPE','FRSS4_BEAM/Q'])
         
         self.lh_builder.create_child_node('HFSED4SG/E_IN','HFSED3VOG/E_OUT')
         self.lh_builder.create_child_node('HFSED4SG/E_OUT',['FRSS4_BEAM/ELEMENT','FRSS4_BEAM/ISOTOPE','FRSS4_BEAM/Q'])
         
         self.lh_builder.create_child_node('HFSED5SG/E_IN','HFSED4SG/E_OUT')
         self.lh_builder.create_child_node('HFSED5SG/E_OUT',['FRSS4_BEAM/ELEMENT','FRSS4_BEAM/ISOTOPE','FRSS4_BEAM/Q'])
         
         #self.lh_builder.create_child_node('TS3ED2O2G/Q_OUT','TS3ED2V1G/Q_OUT')
         self.lh_builder.create_child_node('HFSET3SG/E_IN','HFSED5SG/E_OUT')
         self.lh_builder.create_child_node('HFSET3SG/E_OUT',['FRSS4_BEAM/ELEMENT','FRSS4_BEAM/ISOTOPE','FRSS4_BEAM/Q'])
         
         self.lh_builder.create_child_node('HFSET4SG/E_IN','HFSET3SG/E_OUT')
         self.lh_builder.create_child_node('HFSET4SG/E_OUT',['FRSS4_BEAM/ELEMENT','FRSS4_BEAM/ISOTOPE','FRSS4_BEAM/Q'])
        
        
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
    
    h2 = GENERATOR_FRSS4()
    h2.build()
    h2.generate()
