# AutoRead

This software displays winch position and status from TAIT (formerly Stage Technologies) eChameleon entertainment automation systems, built upon the Siemens Simotion architecture.

## About this project
This project was developed as part of my graduation project at the Guildhall School of Music and Drama, where we have a TAIT PI (Permanent Install). I was fortunate enough to spend a month at TAIT, and learnt a lot about the way their automation systems are set up.

This project was originally based upon a bodged way that the school used previously when integrating automation position with other entertainment control systems, primarily D3 media integrations, to map projected content to a moving piece of scenery.

## Origins and aims of this project
This software is based upon a single line of code from the old code used, which was only taking specific bytes of the data packets. This project aims to be scalable to multiple installations of eChameleon and Simotion, regardless of how many axes are in use. And instead of being limited to position data, hopes also to give a larger picture to the system, including now axisSpeed, axisStatus and timeLeft.

This project hopes to be able to act as a network bridge, and output the information to the show network, as OSC data, to be interpreted (for example) by OSCRouter.

## Development environment
This project was developed on a Raspberry Pi 3B+, running Python 3.7, at present, it requires only a CLI, however the aim is to have this working with a Tkinter GUI in the near future.

### Network integration within eChameleon systems
This device connects to the eChameleon Desk Network, which talks to the eCham desks (G6, Illusionist, Nomad).
The ip range on our install is 172.16.1.0/24

There is a Profinet/Profibus network which exists within the MCC's, likely using the same network switches, on a different subnet.

DHCP is not used, and your Raspberry Pi should be given a static IP in the desk network, that is not in use by Automation system, this can be determined using Wireshark or eCham Maintenance.

# Professional programming
I'm not a professional programmer, however I would like to think that my code will be documented well, and follow fairly good industry practice.
Last studying Python 3 years ago, I know my way around, but not how the industry would like code laid out - naming conventions, etc.
Constructive feedback is always welcome! (I'm also new to GitHub, feel free to comment on my code if that's possible!)