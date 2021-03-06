# Scripts
All the code to be deployed to the Raspberry Pi goes in this folder, and set up to run at boot, with GUI support.

## Files:
- axis_list.txt - generated by axis_list_generator.py, it just creates a flat file to read some dummy data from.
- axis_list_generator.py - see above.
- demo_static.py - displays static information for general publicity. Defines CLI output for ../read.py

## Filename convention
Files are assigned to projects by prefixing the project code to the file.
For example:
- AR_file.py = AutoRead project
- ART_file.py = AutoRead Track project
- ARC_file.py = AutoRead Control project
- COM_file.py = Common code used in multiple projects (EG. GPIO)
- DIAG_file.py = Diagnostics file, used for testing.

The reason the project is structured  this way relates to how python handles sharing code between files.
It's easier to put it all in one folder, than have each project separated.
