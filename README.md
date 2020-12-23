# Elite Dangerous Modular Assistant
A highly modular and configurable helper tool for Elite Dangerous.



Installation:

 - Download and run the latest [`edma.exe`](https://github.com/RaVenInTheDark/edma/releases/)
 

Usage:

 - You can now run this through a means of your choice. Any event extensions must be in the same directory as the script, more below.
 
 - The config json is in `%appdata%/edma/config.json`, if you break something when editing it just delete the file. It may be necassary to create the `edma` directory manually.

 



Extending:


Note that this will be heavily improved in upcoming updates.

 - All `.py` files in the same directory as the tool will be checked. Note that the code in these files ***will*** be executed, if you want to prevent this check if `__name__` == `"__main__"` and only run code if this is True.
 
 - Currently, extensions can only respond to events, and an extension setting an event response will override any previous responses for that event. This will change in upcoming releases.
 
 - These extensions can contain and run any code they like, however any python modules not in the list of provided modules below are inaccessible through conventional `import` methods. There are strict rules for event responses to follow, once again below.
 
- **PROVIDED MODULES**: `os`, `keyboard`, `clipboard`, `json`, `csv`, `requests` and all of their requirements. Any present modules not in this list are not intended to be available, and may have side effects if used, although they can be useful.

- **RULES FOR EVENT RESPONSES**: 
 -- Event responses are defined as functions, and are passed a single dictionary. This contains the event type, but also all data the game provides for the event in question. 
 -- Events must return a singular string if text is to be displayed. This can contain newline characters. If you do not wish to update the overlay text, return `None`.
 -- Function names must be completely lowercase, and match a valid name. If an event is registered that doesn't match a valid name,
 -- Events are registered with a single list at the end of the extension file, containing all functions.
 -- A detailed guide to all valid event names, along with some examples, can be found [here](https://github.com/RaVenInTheDark/edma/blob/master/Journal_Manual_v28.pdf).
