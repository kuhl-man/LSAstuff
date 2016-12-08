from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy

from init_lh_builder import INIT_LH_BUILDER

from FRSS6_properties import FRSS6_PROPERTIES

from FRSS6_devices import FRSS6_DEVICES

from devicedata_xml_parser import XMLParser

class GENERATOR_FRSS6(GenericTransferlineHierarchy,FRSGeneralTargetHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        self.standalone_acczone = False
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            FRSS6_properties = FRSS6_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, FRSS6_properties)
        
        FRSS6_device_groups = FRSS6_DEVICES()
        GenericTransferlineHierarchy.__init__(self, FRSS6_device_groups)
        #FRSGeneralTargetHierarchy.__init__(self,FRSS6_device_groups)

        self.FRSS6_bp = True

    def __buildSpecial(self):
        # build special part of hierarchy for FRSS6
         #FRSGeneralTargetHierarchy.build(self)
        
        
         for device in self.devices.main_dipoles + self.devices.main_quadrupoles + self.devices.chromaticity_sextupoles:
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
       # FRSGeneralTargetHierarchy.generate_linkrules(self)
        GenericTransferlineHierarchy.generate_linkrules(self)
        
    def generate(self):
        self.lh_builder.export()

        

if __name__ == '__main__':
    
    h2 = GENERATOR_FRSS6()
    h2.build()
    h2.generate()
