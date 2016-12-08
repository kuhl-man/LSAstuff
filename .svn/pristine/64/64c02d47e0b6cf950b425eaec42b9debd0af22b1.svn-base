package de.gsi.cs.co.ap.lsa.setup.data;

import java.util.HashMap;

import cern.lsa.domain.settings.spi.ParameterTreeNodeImpl;

/*
 * TODO HH: This class is not needed anymore since position values have been removed from the database. 
 * Some refactoring should be done to remove it and a warning printed if a JSON file still contains position values.
 */
public class ParameterTreeNodeWithPositions {

	private ParameterTreeNodeImpl parameterTreeNodeImpl;
	private HashMap<String, Integer> positions = new HashMap<>();

	public ParameterTreeNodeWithPositions(
			ParameterTreeNodeImpl parameterTreeNodeImpl) {
		this.parameterTreeNodeImpl = parameterTreeNodeImpl;
	}

	public ParameterTreeNodeImpl getParameterTreeNodeImpl() {
		return this.parameterTreeNodeImpl;
	}

	public void putPosition(String parentParameterName, Integer position) {
		this.positions.put(parentParameterName, position);
	}

	public Integer getPosition(String parentParameterName) {
		return this.positions.get(parentParameterName);
	}
}
