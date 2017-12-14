# Agent-Based Model - Programming for Social Scientists '17
This repo contains code written for the intesive module on Programming for Social Scientists at the end of September 2017.
The aim of the module was to become familiar with programming, in particular, in the context of the Python programming language.

The code contained herein aims to introduce a simple agent-based model, which simulates the behaviour of agents (tentatively called sheep) as they move around the virtual environment that has been provided.
Their behaviours include movement around the environment, eating/grazing, sharing with other nearby agents, and being sick.

This is achieved by implementing the agents through an object-oriented approach, by which a agent class has been designed which defines the behaviours of all instances of the agent.

The original intention is that this code be run from the command-line/terminal by running
	python model.py [arg1=10] [arg2=100] [arg3=20]
where the arguments are optional and defined as follows:
* arg1: number of agents
* arg2: number of iterations
* arg3: neighbourhood in terms of cartesian distance from agent
In the case when arguments are not provided, default values will be used.
