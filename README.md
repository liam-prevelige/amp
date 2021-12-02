# Intelligent and Decentralized Multi-Robot Patrol System
> Liam Prevelige - Eren Aldemir\
> Dartmouth College

This ROS package contains the code for final project.

## Requirements
- ROS -- tested on Melodic, but other versions may work.
- Stage (ROS) must be installed within the catkin workspace to be able to launch the experiments.

## Build
Once cloned in a ROS workspace, e.g., `ros_workspace/src/`, run the following command to build it:

	catkin_make
	
## Usage
There are 3 different setups for each of the two approaches (baseline, and learned): 2 overseer, 3 overseer, and 5 overseer. To launch the experiment, simply `roslaunch` the respective `.launch` file.

Example:

	roslaunch patrollers learned_3.launch

## Attribution & Licensing
The code is authored by Eren Aldemir and Liam Prevelige unless otherwise noted. The A* search and grid class is adapted from [grid-pathfinding](https://github.com/mlyean/grid-pathfinding) repository of GitHub user [mlyean](https://github.com/mlyean/). Random weighted selection function is taken from [this](https://stackoverflow.com/a/3679747) StackOverflow answer.
