# AutoRead

This software displays winch position and status from TAIT (formerly Stage Technologies) eChameleon entertainment automation systems, built upon the Siemens Simotion architecture.

## About this project
This project was developed as part of my graduation project at the Guildhall School of Music and Drama, where we have a TAIT PI (Permanent Install). I was fortunate enough to spend a month at TAIT, and learnt a lot about the way their automation systems are set up.

I've been planning and working on this project for a long while.

This project was originally based upon a "bodgy" way that the school used previously when integrating automation position with other entertainment control systems, primarily D3 media integrations, to map projected content to a moving piece of scenery.

## Origins and aims of this project
This software is based upon a single line of code from the old code used, which was only taking specific bytes of the data packets. This project aims to be scalable to multiple installations of eChameleon and Simotion, regardless of how many axes are in use. And instead of being limited to position data, hopes also to give a larger picture to the system, including now axisSpeed, axisStatus and timeLeft.

This project hopes to be able to act as a network bridge, and output the information to the show network, as OSC data, to be interpreted (for example) by OSCRouter.
