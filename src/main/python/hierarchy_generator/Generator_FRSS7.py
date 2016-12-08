from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy

from init_lh_builder import INIT_LH_BUILDER

from FRSS7_properties import FRSS7_PROPERTIES

from FRSS7_devices import FRSS7_DEVICES

from devicedata_xml_parser import XMLParser

class GENERATOR_FRSS7(GenericTransferlineHierarchy,FRSGeneralTargetHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        self.standalone_acczone = False
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            FRSS7_properties = FRSS7_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, FRSS7_properties)
        
        FRSS7_device_groups = FRSS7_DEVICES()
        GenericTransferlineHierarchy.__init__(self, FRSS7_device_groups)
        FRSGeneralTargetHierarchy.__init__(self,FRSS7_device_groups)

        self.FRSS7_bp = True

    def __buildSpecial(self):
        # build special part of hierarchy for FRSS7
         FRSGeneralTargetHierarchy.build(self)
         #self.lh_builder.create_child_node('TS3ED2V1G/Q_OUT','FRSS7_BEAM/Q')
         self.lh_builder.create_child_node('TH4UFG/E_IN','FRSS7_BEAM/E')
         self.lh_builder.create_child_node('TH4UFG/E_OUT',['FRSS7_BEAM/ELEMENT','FRSS7_BEAM/ISOTOPE','FRSS7_BEAM/Q'])
        
        
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
    
    h2 = GENERATOR_FRSS7()
    h2.build()
    h2.generate()
