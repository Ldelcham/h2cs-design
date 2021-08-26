# VPPopt - Virtual Power Plant Optimization Platform

## The platform is current under development

## Introduction

__to be improved/adapted/modified__

VPPopt platform is developed within the framework of [H2 CoopStorage](https://h2coopstorage.eu) project (WP3). The objective of this WP is to develop a tool for (optimally) sizing a Community-based Virtual Power Plant with a hybrid solution of energy storage using electric batteries and hydrogen production.

VPPopt will be developed to *optimize planning of generation, storage to maximize the value of integrated distributed energy system for a virtural power plant.*

*Formulated as a **mixed integer linear program (MILP)**, VPPopt recommends an optimally sized mix of **renewable energy**, and **energy storage technologies**; provides a **dispatch strategy** for operating the technology mix at **maximum economic efficiency**; and estimates the **net present value** of implementing those technologies*

## VPPopt (expected) Capabilities

VPPopt is expected to offer a range of features and capabilities to help users with planning and optimizing renewable energy (PV, Wind and geothermal) and energy storage systems including h2 storage and electric battery technology within a virtual power plant.

The following table describes the full breadth of VPPopt capabilities, including data inputs and variables, and the platform’s outputs and recommendations.

vppopt using [oemof.solph] to created a pyomo model which is a LP or a MILP optimization problem. The latter is then solved by a LP or MILP solver such as CBC, GLPK, Cplex, Gurobi

### Data Inputs

|Type |Name| Description|
|-------|-----------|-----------|
|Drivers|Energy cost|Utility energy and demand charges, and market participation revenues|
|Drivers|Economic factors|Technology costs, incentives, and financial parameters|
|Drivers|Resilience and environmental goals, including:|Minimizing life cycle cost of energy, providing resilience to sustain critical loads during outages, and meeting emissions reduction or percent renewable energy targets|

To be completed ...

### Outputs

To be completed ...

## Installation

python 3 is required, [miniconda](https://docs.conda.io/en/latest/miniconda.html) is recommended

```bash
git clone https://github.com/cenaero-enb/h2cs-design.git
cd h2cs-design
python setup.py install
pip install -r requirements.txt
```

### Extras

- [pygraphviz](https://github.com/pygraphviz/pygraphviz/blob/main/INSTALL.txt)

## Installing a solver

Various commercial and open-source solvers are available and can be used with vppopt, e.g. Cplex, Gurobi, CBC, GLPK, IPOPT, etc. As recommanded from oemof.solph, it worths sometime comparing the result of different solvers. More information about solvers supported by pyomo could be found [here](https://pyomo.readthedocs.io/en/stable/solving_pyomo_models.html#supported-solvers)

## Usage

To be completed ...

??? Evaluating only PV and Battery requires a linear program solver???

??? Adding a generator and/or multiple outages makes the problem mix-integer linear, and thus requires a MILP solver.

???VPPopt will be tested with Cbc and IPOPT???

Ask ULB for testing with CPLEX

## Examples

Several examples for using vppopt could be found [here](examples)

## Main developers

|Name|Affiliation|Email|
|-----|-----|-----|
|Van long Lê|Cenaero|vanlong.le@cenaero.be|

## supported solvers

|Solver|License|Supports|
|------|-----|------|
||||
