Dependencies for running GUI.py are:
-	Python 3, Tkinter, Being currently connected to the Automation Network

Known issues:
-	Data is updated only once, when the system starts. As we know, packets are sent every 50ms.
-	This would likely be a serviceable Readout GUI, by making it run in a loop something like a `while exit_state != True:` – for some reason I could never get this to work, despite the usual tutorials available online.
-	Current default output is a black screen with red border - until it gets a correct IP, and also receives the auto packets.
