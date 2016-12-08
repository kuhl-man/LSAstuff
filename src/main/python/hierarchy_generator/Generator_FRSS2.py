from generic_transferline_hierarchy_generator import GenericTransferlineHierarchy
from FRS_general_target_hierarchy import FRSGeneralTargetHierarchy

from init_lh_builder import INIT_LH_BUILDER

from FRSS2_properties import FRSS2_PROPERTIES

from FRSS2_devices import FRSS2_DEVICES

from devicedata_xml_parser import XMLParser

class GENERATOR_FRSS2(GenericTransferlineHierarchy,FRSGeneralTargetHierarchy, INIT_LH_BUILDER):
    
    def __init__(self):

        self.standalone_acczone = False
        if not hasattr(self, 'lh_builder'):
            self.standalone_acczone = True
            FRSS2_properties = FRSS2_PROPERTIES()
            INIT_LH_BUILDER.__init__(self, FRSS2_properties)
        
        FRSS2_device_groups = FRSS2_DEVICES()
        GenericTransferlineHierarchy.__init__(self, FRSS2_device_groups)
        FRSGeneralTargetHierarchy.__init__(self,FRSS2_device_groups)

        self.frss2_bp = True

    def __buildSpecial(self):
        # build special part of hierarchy for FRSS1
         FRSGeneralTargetHierarchy.build(self)
         self.lh_builder.create_child_node('DetSC21/E_IN','FRSS2_BEAM/E')         
         self.lh_builder.create_child_node('TS3ED7DPG/E_IN','DetSC21/E_OUT')         
         self.lh_builder.create_child_node('TS3ED7DSG/E_IN','TS3ED7DPG/E_OUT')        
         self.lh_builder.create_child_node('TS3ED7LSG/E_IN','TS3ED7DSG/E_OUT')        
         self.lh_builder.create_child_node('TS3ED7OUG/E_IN','TS3ED7LSG/E_OUT')        
         self.lh_builder.create_child_node('TS3ED7VOG/E_IN','TS3ED7OUG/E_OUT')         
         self.lh_builder.create_child_node('TS3ET7GSG/E_IN','TS3ED7VOG/E_OUT')        
         self.lh_builder.create_child_node('TS3DB7LG/E_IN','TS3ET7GSG/E_OUT')         
         self.lh_builder.create_child_node('TS3ET7RSG/E_IN','TS3DB7LG/E_OUT')         
         self.lh_builder.create_child_node('TS3ET7LSG/E_IN','TS3ET7RSG/E_OUT')        
         self.lh_builder.create_child_node('TS3ET7USG/E_IN','TS3ET7LSG/E_OUT')
         self.lh_builder.create_child_node('DetSC22/E_IN','TS3ET7USG/E_OUT')
         self.lh_builder.create_child_node('DetTPC21/E_IN','DetSC22/E_OUT')
         self.lh_builder.create_child_node('DetTPC22/E_IN','DetTPC21/E_OUT')
         
         
         for device in self.devices.targetladders + self.devices.targets + self.devices.degraders + self.devices.degrader_disks:
            self.lh_builder.create_child_node(device + '/E_OUT', ['FRSS2_BEAM/ELEMENT','FRSS2_BEAM/ISOTOPE','FRSS2_BEAM/Q'])
 
         for device in self.devices.main_dipoles + self.devices.main_quadrupoles + self.devices.main_sextupoles + self.devices.vertical_correctors:
            bl_parameter = self.reader.find_unique_string(device + '/B[0-3]?L$', self.lh_builder.lh.get_parameters())
 
           # y_prec_I = self.y_prec_parser.findYPrec(device, 'I', 1)
            i_parameter = self.lh_builder.lh.define_physics_parameter(device + '/I', 'I', device,y_prec=5)
 
            self.lh_builder.create_child_node(i_parameter, bl_parameter)
           
            system = self.devices.devicesystemmap.get(device)
           
            self.lh_builder.lh.add_parameter_to_system(i_parameter, system)

    ### special parameters ----------------------------------------------------------------------------------------------------------

        
        ## as chopper use either electrostatic bender or one plate of first quadrupole
#       
 
        ## as chopper use either electrostatic bender or bottom plate of first quadrupole
###     
    ### special relations ----------------------------------------------------------------------------------------------------------
        ### Creation of relations

        ## electrostatic quadrupole
      
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
    
    h2 = GENERATOR_FRSS2()
    h2.build()
    h2.generate()