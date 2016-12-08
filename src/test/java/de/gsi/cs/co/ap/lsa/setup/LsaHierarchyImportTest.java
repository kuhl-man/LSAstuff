package de.gsi.cs.co.ap.lsa.setup;

import java.io.IOException;
import java.net.URISyntaxException;

import org.junit.Assert;
import org.junit.Test;

import com.fasterxml.jackson.core.JsonProcessingException;

import de.gsi.cs.co.ap.lsa.setup.LsaHierarchyImport.OperationMode;

/**
 * Test class for {@link LsaHierarchyImport}.
 * 
 * @author hhuether
 */
public class LsaHierarchyImportTest {

	private static final String JSON_TO_IMPORT_1 = "lh-CRYRING-CRYRING_RING-1.0.0.json";
	private static final String JSON_TO_IMPORT_2 = "lh-SIS18-SIS18_TH_HHT-1.0.0.json";

	/**
	 * Very basic test that simply executes the importer in apply mode using a
	 * JSON file from resources. Even though that's quite primitive, it's still
	 * useful, since if any obvious errors occur that lead to an exception, the
	 * test case will fail.
	 * @throws JsonProcessingException Not expected.
	 * @throws URISyntaxException Not expected.
	 * @throws IOException Not expected.
	 */
	@Test
	public void testApply() throws JsonProcessingException, URISyntaxException,
			IOException {
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.APPLY, true, JSON_TO_IMPORT_1));
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.APPLY, false, JSON_TO_IMPORT_1));
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.APPLY, true, JSON_TO_IMPORT_2));
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.APPLY, false, JSON_TO_IMPORT_2));
		// TODO HH: Does not fail if encapsulating transaction is marked as
		// "RollbackOnly"
	}

	/**
	 * Very basic test that simply executes the importer in evaluation mode
	 * using a JSON file from resources. Even though that's quite primitive,
	 * it's still useful, since if any obvious errors occur that lead to an
	 * exception, the test case will fail.
	 * @throws JsonProcessingException Not expected.
	 * @throws URISyntaxException Not expected.
	 * @throws IOException Not expected.
	 */
	@Test
	public void testEvaluate() throws JsonProcessingException,
			URISyntaxException, IOException {
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.EVALUATE, true, JSON_TO_IMPORT_1));
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.EVALUATE, false, JSON_TO_IMPORT_1));
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.EVALUATE, true, JSON_TO_IMPORT_2));
		Assert.assertTrue(LsaHierarchyImport.importFromJson(
				OperationMode.EVALUATE, false, JSON_TO_IMPORT_2));
		// TODO HH: Does not fail if encapsulating transaction is marked as
		// "RollbackOnly"
	}
}