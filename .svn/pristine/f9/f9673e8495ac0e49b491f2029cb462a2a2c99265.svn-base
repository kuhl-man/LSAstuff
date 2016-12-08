package de.gsi.cs.co.ap.lsa.setup.spi;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import cern.accsoft.commons.util.Nameds;
import cern.lsa.client.ParameterService;
import cern.lsa.client.ServiceLocator;
import cern.lsa.domain.settings.Parameter;
import cern.lsa.domain.settings.ParameterTreeNode;
import cern.lsa.domain.settings.factory.ParameterTreesRequestBuilder;
import cern.lsa.domain.settings.spi.ParameterImpl;
import cern.lsa.domain.settings.spi.ParameterTreeNodeImpl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;

import de.gsi.cs.co.ap.lsa.setup.data.ParameterTreeNodeWithPositions;
import de.gsi.cs.co.ap.lsa.setup.json.JsonNodeNames;

/**
 * @author rmueller
 * @author hhuether
 */
public class ParameterRelationImportImpl extends ImportBaseImpl {

    private static final Log LOGGER = LogFactory.getLog(ParameterRelationImportImpl.class);

    // LSA services
    private final ParameterService parameterService;

    private JsonNode parameterRelationsNode;
    private final List<ParameterTreeNodeWithPositions> parameterRelationsToKeep = new LinkedList<>();
    private final List<ParameterTreeNodeWithPositions> parameterRelationsToUpdate = new LinkedList<>();

    public ParameterRelationImportImpl(JsonNode root) {
        super(root);

        this.parameterRelationsNode = root.get(JsonNodeNames.PARAMETER_RELATIONS);

        parameterService = ServiceLocator.getService(ParameterService.class);
    }

    private boolean equalsForImport(ParameterTreeNodeWithPositions ptnwp1, ParameterTreeNodeWithPositions ptnwp2) {
        // The name of the hierarchy that the parameter relations belong to is stored in the child's defaultHierarchy
        // attribute
        if (ptnwp1.getParameterTreeNodeImpl().getParameter().getDefaultHierarchy() != ptnwp2.getParameterTreeNodeImpl()
                .getParameter().getDefaultHierarchy()) {
            return false;
        }

        if (ptnwp1.getParameterTreeNodeImpl().getParents().size() != ptnwp2.getParameterTreeNodeImpl().getParents()
                .size()) {
            return false;
        }

        // For all parents of the child at hand
        for (ParameterTreeNode parentParameterTreeNode1 : ptnwp1.getParameterTreeNodeImpl().getParents()) {

            ParameterTreeNode parentParameterTreeNode2 = Nameds.findByName(ptnwp2.getParameterTreeNodeImpl()
                    .getParents(), parentParameterTreeNode1.getName());
            if (parentParameterTreeNode2 == null) {
                return false;
            }

            if (ptnwp1.getPosition(parentParameterTreeNode1.getName()) != ptnwp2.getPosition(parentParameterTreeNode2
                    .getName())) {
                return false;
            }
        }

        return true;
    }

    public void evaluate() throws JsonProcessingException {
        if (parameterRelationsNode != null) {

            ArrayList<Parameter> processedParameters = new ArrayList<>();

            // Iterate through hierarchies
            Iterator<String> hierarchyNames = parameterRelationsNode.fieldNames();
            while (hierarchyNames.hasNext()) {
                String hierarchyName = hierarchyNames.next();

                // Inject the hierarchy into the deserialization context. This is needed since we cannot access the
                // parent node within the deserializer.
                this.addValueToInjectIntoDeserializer(JsonNodeNames.HIERARCHY_NAME, hierarchyName);

                // Iterate through child parameters
                Iterator<String> childParameterNames = parameterRelationsNode.get(hierarchyName).fieldNames();
                while (childParameterNames.hasNext()) {
                    String childParameterName = childParameterNames.next();

                    // Inject the child parameter name into the deserialization context. This is needed since we cannot
                    // access the parent node within the deserializer.
                    this.addValueToInjectIntoDeserializer(JsonNodeNames.CHILD_NAME, childParameterName);

                    // Deserialize
                    ParameterTreeNodeWithPositions parameterTreeNodeWithPositionsFromJson = this.getObjectMapper()
                            .treeToValue(parameterRelationsNode.get(hierarchyName).get(childParameterName),
                                    ParameterTreeNodeWithPositions.class);
                    ParameterImpl childParameter = (ParameterImpl) parameterTreeNodeWithPositionsFromJson
                            .getParameterTreeNodeImpl().getParameter();

                    if (processedParameters.contains(childParameter)) {
                        for (Parameter processedParameter : processedParameters) {
                            if ((processedParameter.getName().equals(childParameter.getName()))
                                    && (processedParameter.getDefaultHierarchy().equals(childParameter
                                            .getDefaultHierarchy()))) {
                                // Relations will become inconsistent if they are defined in two or
                                // more different nodes for the same child parameter.
                                throw new RuntimeException(String.format(
                                        ImportMessages.ERROR_DATA_ENTRY_RELATIONS_FOR_PARAMETER_SPECIFIED_TWICE,
                                        childParameter.getName()));
                            }
                        }
                    }
                    processedParameters.add(childParameter);

                    // Get child tree node with parents from database
                    Collection<ParameterTreeNode> parameterTreeNodesFromDatabase = parameterService
                            .findParameterTrees(ParameterTreesRequestBuilder.byParameterAndHierarchyFindSourceTrees(
                                    childParameterName, hierarchyName));

                    ParameterTreeNode parameterTreeNodeFromDatabase = Nameds.findByName(parameterTreeNodesFromDatabase,
                            childParameter.getName());

                    // Put child tree node from database into wrapper with positions
                    ParameterTreeNodeWithPositions parameterTreeNodeWithPositionsFromDatabase = new ParameterTreeNodeWithPositions(
                            (ParameterTreeNodeImpl) parameterTreeNodeFromDatabase);

                    if (equalsForImport(parameterTreeNodeWithPositionsFromDatabase,
                            parameterTreeNodeWithPositionsFromJson)) {
                        parameterRelationsToKeep.add(parameterTreeNodeWithPositionsFromJson);
                    } else {
                        parameterRelationsToUpdate.add(parameterTreeNodeWithPositionsFromJson);
                    }
                }
            }
        }
    }

    public String retrieveChanges(Boolean printArtifactsToBeKept) throws JsonProcessingException {
        Map<String, Map<String, ParameterTreeNodeWithPositions>> all = new HashMap<String, Map<String, ParameterTreeNodeWithPositions>>();

        if (printArtifactsToBeKept) {
            all.put("KEEP", new HashMap<String, ParameterTreeNodeWithPositions>());
            for (ParameterTreeNodeWithPositions childParameterNode : parameterRelationsToKeep) {
                all.get("KEEP").put(childParameterNode.getParameterTreeNodeImpl().getParameter().getName(),
                        childParameterNode);
            }
        }

        all.put("UPDATE", new HashMap<String, ParameterTreeNodeWithPositions>());
        for (ParameterTreeNodeWithPositions childParameterNode : parameterRelationsToUpdate) {
            all.get("UPDATE").put(childParameterNode.getParameterTreeNodeImpl().getParameter().getName(),
                    childParameterNode);
        }

        return "\"PARAMETER_RELATIONS\":"
                + this.getObjectMapper().writer().withDefaultPrettyPrinter().writeValueAsString(all);

    }

    public void applyDelete(Boolean printQuantities) {
        Integer numberOfRemovedRelations = 0;

        // For all child nodes
        for (ParameterTreeNodeWithPositions childParameterTreeNodeWithPositionsFromJSON : parameterRelationsToUpdate) {

            // Get child with parents from database
            ParameterTreeNode childParameterTreeNodeFromDatabase = Nameds.findByName(parameterService
                    .findParameterTrees(ParameterTreesRequestBuilder.byParameterAndHierarchyFindSourceTrees(
                            childParameterTreeNodeWithPositionsFromJSON.getParameterTreeNodeImpl().getParameter()
                                    .getName(), childParameterTreeNodeWithPositionsFromJSON.getParameterTreeNodeImpl()
                                    .getParameter().getDefaultHierarchy())),
                    childParameterTreeNodeWithPositionsFromJSON.getParameterTreeNodeImpl().getParameter().getName());

            if (childParameterTreeNodeFromDatabase.getParents().size() == childParameterTreeNodeWithPositionsFromJSON
                    .getParameterTreeNodeImpl().getParents().size()) {
                // Child node from database and the one to be imported have the same number of parents, so nothing to
                // delete here.
                continue;
            }

            // For all parent nodes of the child from the database
            for (ParameterTreeNode parentParameterTreeNodeFromDatabase : childParameterTreeNodeFromDatabase
                    .getParents()) {

                // if the child node from JSON does not contain the parent at hand, it has to be removed from the
                // database
                if (Nameds.findByName(childParameterTreeNodeWithPositionsFromJSON.getParameterTreeNodeImpl()
                        .getParents(), parentParameterTreeNodeFromDatabase.getName()) == null) {

                    LOGGER.debug("Removing relation between parameters '"
                            + childParameterTreeNodeWithPositionsFromJSON.getParameterTreeNodeImpl().getParameter()
                                    .getName() + "' (child) and '"
                            + parentParameterTreeNodeFromDatabase.getParameter().getName() + "' (parent).");

                    // The relation to this parent is to be removed from the database. Because creation and deletion of
                    // relations works from parent to children, the children for this parent have to be found first, and
                    // then the child concerned can be removed.
                    Collection<ParameterTreeNode> childrenForParentParameterTreeNode = Nameds.findByName(
                            parameterService.findParameterTrees(ParameterTreesRequestBuilder
                                    .byParameterAndHierarchyFindDependentTrees(parentParameterTreeNodeFromDatabase
                                            .getParameter().getName(), childParameterTreeNodeWithPositionsFromJSON
                                            .getParameterTreeNodeImpl().getParameter().getDefaultHierarchy())),
                            parentParameterTreeNodeFromDatabase.getParameter().getName()).getChildren();

                    // Because deleting a parameter relation works by saving all relations except the one to
                    // delete, a list of all relations not to be deleted has to be built.
                    ArrayList<Parameter> allChildrenForParent = new ArrayList<>();
                    for (ParameterTreeNode childForParentParameterTreeNode : childrenForParentParameterTreeNode) {
                        // All children get added to the list, except the one to be removed
                        if (!childForParentParameterTreeNode
                                .getParameter()
                                .getName()
                                .equals(childParameterTreeNodeWithPositionsFromJSON.getParameterTreeNodeImpl()
                                        .getParameter().getName())) {
                            allChildrenForParent.add(childForParentParameterTreeNode.getParameter());
                        }
                    }

                    // Finally save the set of relations excluding the one to be removed.
                    HashMap<Parameter, List<Parameter>> newHierarchy = new HashMap<Parameter, List<Parameter>>();
                    newHierarchy.put(parentParameterTreeNodeFromDatabase.getParameter(), allChildrenForParent);
                    parameterService.saveParameterRelations(newHierarchy, childParameterTreeNodeWithPositionsFromJSON
                            .getParameterTreeNodeImpl().getParameter().getDefaultHierarchy());

                    numberOfRemovedRelations++;
                }
            }
        }

        if (printQuantities) {
            System.out.println("    Removing " + numberOfRemovedRelations
                    + " parameter relation sets (table PARAMETER_RELATIONS)");
        }
    }

    /*
     * The "applyUpdate" method covers both creating and updating for this importer. The reason behind pulling those two
     * together is that it was more efficient to implement this way, amongst other reasons because of the way
     * CommonParameterService.saveParameterRelations works and the fact that a new class had to be created to store
     * position values which can more easily be handled if a child parameter and its relations are seen as one entity.
     */
    public void applyCreate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Keeping " + parameterRelationsToKeep.size()
                    + " parameter relation sets (table PARAMETER_RELATIONS)");
        }

        for (ParameterTreeNodeWithPositions childParameterTreeNode : parameterRelationsToKeep) {
            for (ParameterTreeNode parentParameterTreeNode : childParameterTreeNode.getParameterTreeNodeImpl()
                    .getParents()) {
                LOGGER.debug("Keeping " + childParameterTreeNode.getParameterTreeNodeImpl().getParameter().getName()
                        + " --parent--> " + parentParameterTreeNode.getParameter().getName());
            }
        }
    }

    /*
     * The "applyUpdate" method covers both creating and updating for this importer. The reason behind pulling those two
     * together is that it was more efficient to implement this way, amongst other reasons because of the way
     * CommonParameterService.saveParameterRelations works and the fact that a new class had to be created to store
     * position values which can more easily be handled if a child parameter and its relations are seen as one entity.
     */
    public void applyUpdate(Boolean printQuantities) {
        if (printQuantities) {
            System.out.println("    Updating " + parameterRelationsToUpdate.size()
                    + " parameter relation sets (table PARAMETER_RELATIONS)");
        }
        // For all child nodes to be updated
        for (ParameterTreeNodeWithPositions childParameterTreeNode : parameterRelationsToUpdate) {

            LOGGER.debug("Updating " + childParameterTreeNode.getParameterTreeNodeImpl().getParameter().getName());

            // For all parent nodes of the child at hand
            for (ParameterTreeNode parentParameterTreeNode : childParameterTreeNode.getParameterTreeNodeImpl()
                    .getParents()) {

                // The relation to this parent is to be created in the database. Because saving works from parent to
                // children, the children for this parent have to be found first, and then child concerned can be added.
                Collection<ParameterTreeNode> childrenForParentToBeCreated = parameterService
                        .findParameterTrees(ParameterTreesRequestBuilder.byParameterAndHierarchyFindDependentTrees(
                                parentParameterTreeNode.getParameter().getName(), childParameterTreeNode
                                        .getParameterTreeNodeImpl().getParameter().getDefaultHierarchy()));

                // The method findParameterTrees returns the specified parameters on the first level. Here there parents
                // are needed, though.
                childrenForParentToBeCreated = Nameds.findByName(childrenForParentToBeCreated,
                        parentParameterTreeNode.getParameter().getName()).getChildren();

                // Because deleting a parameter relation works by saving all relations except the one to
                // delete, a list of all relations not to be deleted has to be built.
                ArrayList<Parameter> allChildrenForParent = new ArrayList<>();
                for (ParameterTreeNode childForParentToBeCreated : childrenForParentToBeCreated) {
                    allChildrenForParent.add(childForParentToBeCreated.getParameter());
                }

                // Now the new relation is added
                if (!allChildrenForParent.contains(childParameterTreeNode.getParameterTreeNodeImpl().getParameter())) {
                    allChildrenForParent.add(childParameterTreeNode.getParameterTreeNodeImpl().getParameter());
                }

                // Finally save the complete set of relations including the new one.
                HashMap<Parameter, List<Parameter>> newHierarchy = new HashMap<Parameter, List<Parameter>>();
                newHierarchy.put(parentParameterTreeNode.getParameter(), allChildrenForParent);
                parameterService.saveParameterRelations(newHierarchy, childParameterTreeNode.getParameterTreeNodeImpl()
                        .getParameter().getDefaultHierarchy());
            }
        }
    }

    private void checkImportForChildParameterTreeNode(ParameterTreeNodeWithPositions childParameterTreeNode) {
        // Get parents for child
        Collection<ParameterTreeNode> parentParameterTreeNodesInDatabase = parameterService
                .findParameterTrees(ParameterTreesRequestBuilder.byParameterAndHierarchyFindSourceTrees(
                        childParameterTreeNode.getParameterTreeNodeImpl().getParameter().getName(),
                        childParameterTreeNode.getParameterTreeNodeImpl().getParameter().getDefaultHierarchy()));

        // The method findParameterTrees returns the specified parameters on the first level. Here there parents are
        // needed, though.
        ParameterTreeNode childParameterTreeNodeInDatabase = Nameds.findByName(parentParameterTreeNodesInDatabase,
                childParameterTreeNode.getParameterTreeNodeImpl().getParameter().getName());

        parentParameterTreeNodesInDatabase = childParameterTreeNodeInDatabase.getParents();

        // Check that child from database has the same number of parents as specified in JSON
        if (parentParameterTreeNodesInDatabase.size() != childParameterTreeNode.getParameterTreeNodeImpl().getParents()
                .size()) {
            throw new RuntimeException(String.format(
                    ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_RELATION_WRONG_NUMBER_OF_RELATIONS,
                    childParameterTreeNode.getParameterTreeNodeImpl().getParameter().getName(), childParameterTreeNode
                            .getParameterTreeNodeImpl().getParents().size(), parentParameterTreeNodesInDatabase.size()));
        }

        // For all parents
        for (ParameterTreeNode parentParameterTreeNodeFromJson : childParameterTreeNode.getParameterTreeNodeImpl()
                .getParents()) {

            // Check that parent exists
            ParameterTreeNode parentParameterTreeNodeInDatabase = Nameds.findByName(parentParameterTreeNodesInDatabase,
                    parentParameterTreeNodeFromJson.getParameter().getName());
            if (parentParameterTreeNodeInDatabase == null) {
                throw new RuntimeException(String.format(
                        ImportMessages.ERROR_NOT_IMPORTED_CORRECTLY_PARAMETER_RELATION_DOES_NOT_EXIST,
                        childParameterTreeNode.getParameterTreeNodeImpl().getParameter().getName(),
                        parentParameterTreeNodeFromJson.getParameter().getName()));
            }
        }
    }

    @Override
    public void checkImport() throws JsonProcessingException {
        System.out.println("    Checking import of relations between parameters...");

        // Check that relations that were to be kept are still present in the database
        for (ParameterTreeNodeWithPositions childParameterTreeNode : parameterRelationsToKeep) {
            checkImportForChildParameterTreeNode(childParameterTreeNode);
        }
        // Check that updates (covers creation and deletion) were successful
        for (ParameterTreeNodeWithPositions childParameterTreeNode : parameterRelationsToUpdate) {
            checkImportForChildParameterTreeNode(childParameterTreeNode);
        }

        System.out.println("    ...Relations between parameters were imported correctly.");
    }
}
