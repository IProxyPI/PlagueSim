Usage and configuration instructions, as well as general notes

Lets try and keep this updated with all relevant information

// DEPENDANCIES

Many modules import eachother. To avoid circular dependancies, intentional or
accidental, the flow of imports will be listed here:

Driver: Locations - Agent - Events - Testing_Module - Parameters - Resources - Sim_Tools - Visuals
Agent:  Parameters - Resources - Sim_Tools
Events: Locations - Agent - Parameters
Locations: Agent - Parameters - Resources - Sim_Tools
Testing_Module: Location Agents - Events - Parameters - Resources - Sim_Tools - Visuals
Visuals: Locations - Agent - Parameters
Parameters: None
Resources: None
