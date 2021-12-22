# CPSC 571 Project - Disease Spread Simulator

This project is a Python and Jupyter Notebook program that simulates disease spread based on input parameters and Alberta census data.

## Installation

To run the Jupyter Visualization program, Jupyter needs to be installed either as an IDE package, or locally with JupyterHub.

https://jupyter.org/install

The program runs with Python 3.9 and also requires sklearn to be installed. 

```
pip install jupyterlab
pip install sklearn
```

## Usage

Option 1:

Run the Jupyter Notebook in JupyterHub. Run each cell in sequence to see the final visuals. 

Option 2:

Run the simulation in Python and manually view the sim_out.csv data. Thise data is what is used to construct the Jupyter visuals.

```
python3 simulator.py
```

For  both options, input the number of days to run, the percentage of the population infected at day 0, and the number of days the disease lasts for.


