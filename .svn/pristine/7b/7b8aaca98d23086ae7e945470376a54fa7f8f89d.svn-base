package de.gsi.cs.co.ap.lsa.setup.spi;

import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

public class ImportMessages {

    // Required artifact was not found in database
    public static final String ERROR_NOT_FOUND_DEVICE = "Error while performing import: Device '%s' was not found in database.";
    public static final String ERROR_NOT_FOUND_PARAMETER = "Error while performing import: Parameter '%s' was not found in database.";
    public static final String ERROR_NOT_FOUND_PARAMETER_GROUP = "Error whild performing import: Parameter group '%s' was not found in database.";
    public static final String ERROR_NOT_FOUND_PARAMETER_TYPE = "Error while performing import: Parameter type '%s' was not found in database.";

    // No artifacts of certain kind found at all
    public static final String ERROR_NOT_FOUND_PARAMETER_TYPES_FOR_DEVICE_TYPE = "Error while performing import: There could not be any parameter types found in the database for device type '%s'.";
    public static final String ERROR_NOT_FOUND_PARAMETER_TYPES_FOR_DEVICE_TYPE_VERSION = "Error while performing import: There could not be any parameter types found in the database for version '%s' of device type '%s'.";

    // Required data field not specified in JSON file
    public static final String ERROR_NOT_SPECIFIED_PROPERTY_NAME = "Error while performing import: Property name has not been specified in JSON file for hardware parameter '%s'.";
    public static final String ERROR_NOT_SPECIFIED_FIELD_NAME = "Error while performing import: Field name has not been specified in JSON file for hardware parameter '%s'.";
    public static final String ERROR_NOT_SPECIFIED_PARAMETER_TYPE_NAME = "Error while performing import: Parameter type name has not been specified in JSON file for physics parameter '%s'.";

    // Data entry errors in JSON file
    public static final String ERROR_DATA_ENTRY_RELATIONS_FOR_PARAMETER_SPECIFIED_TWICE = "Error while performing import: Relations for parameter '%s' have been specified more than once within the JSON file. Please consolidate!";
    public static final String ERROR_DATA_ENTRY_LINK_RULE_NAME_NOT_SPECIFIED = "Error while performing import: Link rule name (Node '"
            + JsonNodeNames.TRIM_LINKRULE + "') was not specified for logical hardware '%s'.";

    // Deviation detected while checking import
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_DEVICE = "Error while checking import: Device '%s' was not imported correctly.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_LINKRULES_CONFIG = "Error while checking import: Link rule configuration for logical hardware '%s' was not imported correctly.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_LINKRULES_CONFIG_LOGICAL_HARDWARE_NOT_FOUND = "Error while checking import: Logical hardware '%s' was not found in the database.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_GROUP = "Error while checking import: Parameter group '%s' was not imported correctly.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_HARDWARE = "Error while checking import: Hardware parameter '%s' was not imported correctly.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_GROUP_PARAMETER_NOT_FOUND = "Error while checking import: Assignment of parameter '%s' to parameter group '%s' was not found.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_GROUP_PARAMETER_WRONG_NUMBER_OF_ASSIGNMENTS = "Error while checking import: Parameter '%s' should be assigned to %d parameter groups, but is assigned to %d parameter groups.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_PHYSICS = "Error while checking import: Physics parameter '%s' was not imported correctly.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_RELATION_DOES_NOT_EXIST = "Error while checking import: Relation between parameters '%s' (child) and '%s' (parent) does not exist.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_RELATION_INCORRECT_POSITION = "Error while checking import: Relation between parameters '%s' (child) and '%s' (parent) has incorrect 'position' value.";
    public static final String ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_RELATION_WRONG_NUMBER_OF_RELATIONS = "Error while checking import: Parameter '%s' (child) should have %d relations to parent parameters, but has %d relations.";

    // Unsupported fields in JSON file
    public static final String WARNING_UNSUPPORTED_USERGROUP = "Warning: The field 'USERGROUP' is not supported anymore due to changes in parameters table structure.";
    public static final String WARNING_UNSUPPORTED_POSITION = "Warning: The field 'POSITION' is not supported anymore.";
    public static final String WARNING_UNSUPPORTED_UNKNOWN_FIELD = "Warning: The field '%s' for artifact %s is not supported and has been ignored.";

    // Status messages
    public static final String STATUS_CHECK_IMPORT_PARAMETER_GROUP_NOTHING_TO_IMPORT = "    ...There were no parameter group assignments to be imported.";
    public static final String STATUS_CHECK_IMPORT_PARAMETER_GROUP_PARAMETER_STARTED = "    Checking import of parameter group assignments...";
    public static final String STATUS_CHECK_IMPORT_PARAMETER_GROUP_PARAMETER_SUCCESSFUL = "    ...Parameter group assignments were imported correctly.";
    public static final String STATUS_PARAMETER_GROUP_PARAMETER_CREATE_QUANTITY = "    Creating %d parameter group assignments (table PARAMETER_GROUP_PARAMETERS)";
    public static final String STATUS_PARAMETER_GROUP_PARAMETER_KEEP_QUANTITY = "    Keeping %d parameter group assignments (table PARAMETER_GROUP_PARAMETERS)";
    public static final String STATUS_PARAMETER_GROUP_PARAMETER_REMOVE_QUANTITY = "    Removing %d parameter group assignments (table PARAMETER_GROUP_PARAMETERS)";

    // Debug messages
    public static final String DEBUG_PARAMETER_GROUP_PARAMETER_CREATE = "Creating assignment of parameter '%s' to parameter group '%s'.";
    public static final String DEBUG_PARAMETER_GROUP_PARAMETER_KEEP = "Keeping assignment of parameter '%s' to parameter group '%s'.";
    public static final String DEBUG_PARAMETER_GROUP_PARAMETER_REMOVE = "Removing assignment of parameter '%s' to parameter group '%s'.";
}
