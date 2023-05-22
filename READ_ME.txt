Usage and configuration instructions, as well as general notes

Lets try and keep this updated with all relevant information

// DEPENDANCIES

Many modules import eachother. To avoid circular dependancies, intentional or
accidental, the flow of imports will be listed here:

Driver: Locations - Agent - Events - Testing_Module - Parameters
Agent:  Parameters
Events: Locations - Agent - Parameters
Locations: Agent - Parameters
Testing_Module: Location Agents - Events - Parameters
Parameters: None