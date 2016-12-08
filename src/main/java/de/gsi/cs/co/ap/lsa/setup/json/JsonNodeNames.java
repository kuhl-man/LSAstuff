package de.gsi.cs.co.ap.lsa.setup.json;

/**
 * Constant string identifiers used in JSON import files are centrally stored in this class.
 * 
 * @author hhuether
 */
public final class JsonNodeNames {

    // Node names used for all import artifacts
    public static final String ACCELERATOR = "ACCELERATOR";
    public static final String HIERARCHY_DETAILS = "HIERARCHY_DETAILS";
    public static final String PARTICLE_TRANSFER = "PARTICLE_TRANSFER";

    // Node names used for several import artifacts
    public static final String DEVICE_NAME = "DEVICE_NAME";
    /**
     * Although what was formerly called "system group" is now called "parameter group", the old name is still used in
     * the JSON file to avoid changes on the user's side.
     */
    public static final String SYSTEM_CONFIGS = "SYSTEM_CONFIGS";

    // Node names used for parameters
    public static final String BELONGS_TO_FUNCTION_BPROC = "BELONGS_TO_FUNCTION_BPROC";
    public static final String DEFAULT_HIERARCHY = "DEFAULT_HIERARCHY";
    public static final String FIELD_NAME = "FIELD_NAME";
    public static final String IS_RESERVED_FOR_OP_EXPERTS = "IS_RESERVED_FOR_OP_EXPERTS";
    public static final String MAX_DELTA = "MAX_DELTA";
    public static final String PARAMETER_NAME = "PARAMETER_NAME";
    public static final String PARAMETER_TYPE_NAME = "PARAMETER_TYPE_NAME";
    public static final String PARAMETERS_HARDWARE = "PARAMETERS_HARDWARE";
    public static final String PARAMETERS_PHYSICS = "PARAMETERS_PHYSICS";
    public static final String PROPERTY_NAME = "PROPERTY_NAME";
    public static final String TRIMABLE = "TRIMABLE";
    public static final String USERGROUP = "USERGROUP";
    public static final String X_PREC = "X_PREC";
    public static final String Y_PREC = "Y_PREC";

    // Node names used for devices
    public static final String DEVICES = "DEVICES";
    public static final String ACCELERATOR_ZONE = "ACCELERATOR_ZONE";
    public static final String DESCRIPTION = "DESCRIPTION";
    public static final String DEVICE_ALIAS = "DEVICE_ALIAS";
    public static final String DEVICE_TYPE = "DEVICE_TYPE";
    public static final String IS_MULTIPLEXED = "IS_MULTIPLEXED";

    // Node names used for parameter relations
    public static final String CHILD_NAME = "CHILD_NAME";
    public static final String HIERARCHY_NAME = "HIERARCHY_NAME";
    public static final String PARAMETER_RELATIONS = "PARAMETER_RELATIONS";
    public static final String POSITION = "POSITION";
    
    // Node names used for link rule configurations
    public static final String LINKRULES_CONFIGS = "LINKRULES_CONFIGS";
    public static final String TRIM_LINKRULE = "TRIM_LINKRULE";
}
