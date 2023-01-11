## TITLE: UCL_RC3_RobotControl

## Description:
This project prodives a number of pipelines to control Dynamixel AX servo motors:
Pipeline #1 Cabled Python Control via USB
Pipeline #2 Wireless Python Control via Raspberry Pi
Pipeline #3 Wireless Unity Control via Raspberry Pi

## Setup:
Before using any of the pipelines, beyond basic development software, it is recommended to install Dynamixel Wizard from http://www.dynamixel.com/
Pipeline #1 requires: (1+) Dynamixel AX servo motor, (1) U2D2 Power Hub, (1) U2D2, (1) computer.
Pipeline #2 requires: (1+) Dynamixel AX servo motor, (1) U2D2 Power Hub, (1) U2D2, (1) computer, (1) Raspberry Pi.
Pipeline #3 requires: (1+) Dynamixel AX servo motor, (1) U2D2 Power Hub, (1) U2D2, (1) computer, (1) Raspberry Pi, and Unity3D (software installation)
Check http://www.dynamixel.com/ or https://robotis.co.uk/dynamixel to learn the proper way to setup the Dynamixel circuit.

## Usage A:
Pipeline #1 is enabled by running the 'dxl_a12_usb_control_1-generic.py' script.
Pipeline #2 is enabled by running the 'dxl_control_osc' script.
Pipeline #3 is enabled by running a Unity app constructed around the scripts provided. 
Check https://unitylist.com/p/spm/DXL-AX-12-A for more info on Justin Moon's Unity >> Raspberry Pi >> Dynamixel servo control pipeline via udp protoco

## Usage B:
The scripts are meant to be duplicated and edited to generate project-specific control apps (particularly for robotic projects)
The repository provides an example of this, 'dxl_a12_usb_control_1-generic.py' was duplicated and adapted into 'dxl_a12_usb_control_2-DH.py' 
for the Diffusive Habitats project, which also required a custom method library 'DH_project_specific_methods'. 

## Contributions:
This project is based on the Dynamixel framework and Justin Moon's Unity >> Raspberry Pi >> Dynamixel servo control pipeline via udp protocol
It was developed by Research Cluster 3 of the Bartlett School of Architecture at UCL, with contributions from Valentina Soana, Ziming He, and Sergio Mutis.

## Resources:
For more info about Research Cluster 3 at UCL Bartlett, visit https://www.livingarchitecturelab.com/
For more info about the Dynamixel framework, visit http://www.dynamixel.com/
For more info about the Unity-RaspberryPi-Dynamixel pipeline, visit https://unitylist.com/p/spm/DXL-AX-12-A
For more info about Diffusive Habitats, visit https://bpro2022.bartlettarchucl.com/rc3-living-architecture-lab-22/diffusive-habitats

## Licensing:
The project is subject to licensing and copyright by Robotis Dynamixel, The Living Architecture Lab, and others as specified.
