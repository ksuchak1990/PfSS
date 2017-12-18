# Agent-Based Model - Programming for Social Scientists '17
This repo contains code written for the 1-week intesive module on Programming for Social Scientists at the end of September 2017.
The aim of the module was to become familiar with programming, in particular, in the context of the Python programming language.

The code contained herein aims to introduce a simple agent-based model, which simulates the behaviour of agents as they move around the virtual environment that has been provided as a csv file (see `in.txt`).
Their behaviours include movement around the environment, eating/grazing, sharing with other nearby agents, and being sick.

This is achieved by implementing the agents through an object-oriented approach, by which an `Agent` class has been designed which defines the behaviours of all instances of the `Agent`.
This `Agent` class is defined in `agentframework.py`.

A branch labelled `experimental` has been set up to further develop the code.
This currently involves the construction of a `Wolf` class and a `Sheep` class, both of which will be subclasses of the `Agent` class.
As a consequence the these classes will inherit all of the methods from `Agent`.
The aim is to override the `eat` and `move` methods in each of the subclasses such that wolves move much faster than sheep, and are able to feed on sheep, thus killing the sheep (sorry if this sounds a bit morbid).

## Running the code
The original intention is that this code be run from the command-line/terminal by running

```python model.py [arg1=10] [arg2=100] [arg3=20]```

where the arguments are optional and defined as follows:
* `arg1`: number of agents
* `arg2`: number of iterations
* `arg3`: neighbourhood in terms of cartesian distance from agent
In the case when arguments are not provided, default values will be used.

Please note that the code was written under Python 3.6, and so it is crucial that the code is run using some version of Python 3 (this may need to be specified at the command-line).

### Inputs and Outputs
The code will read in the environment from the csv file named `in.txt` (see in repo above).
Alternative environments can be provided (assuming they are are provided with the same filename) - the code simply assumes that the environment 2-dimensional, and takes the shape of a rectangle.

Upon completion, the code will write out two files: `out.txt` and `stores.txt`.
`out.txt` is a csv file in the same form as `in.txt`; it provides a copy of the environment at the end of the simulation, and as such it is overwriten upon completion.
`store.txt` is a csv file that keeps a record of the stores of each of the agents at the end of the simulation; a new line is appended to the end of the file with a record from the completed simulation.

The program also outputs two figures to the screen over the course of running.
The first figure is a visualisation of the environment before it is populated with agents.
The second figure is a visualisation of the environment after the simulation has been run (whereby agents have 'eaten' and removed some of the store from some of the cells in the environment).
In both cases, the colour-scale represents the store values in each cell of the environment.
Please note that colour-scales may vary between machines with different versions of Python and Matplotlib.

## Conventions
For those interested in the code, the programmer has assumed the reader's awareness of the following conventions:
* CamelCase naming convention,
* '`get`' and '`set`' function naming for accessor and modifier methods respectively.

Please also note, the programmer has undertaken a somewhat minimal approach to commenting based on two motivations:
* A basic understanding of programming logic is assumed, i.e. the usage of data structures such as `dict` and `list`, and flow control such as `for` loops and `if` statements,
* Functions and variables have been named in such a way that their names should lend clarity to their purposes.
