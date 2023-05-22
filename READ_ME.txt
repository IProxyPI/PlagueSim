Usage and configuration instructions, as well as general notes

Lets try and keep this updated with all relevant information

// DEPENDANCIES

Many modules import eachother. To avoid circular dependancies, intentional or
accidental, the flow of imports will be listed here:

Driver: Locations - Agent - Events - Testing_Module - Parameters - Resources
Agent:  Parameters - Resources
Events: Locations - Agent - Parameters
Locations: Agent - Parameters - Resources
Testing_Module: Location Agents - Events - Parameters - Resources
Parameters: None
Resources: None