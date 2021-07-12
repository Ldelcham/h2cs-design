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

python 3 is required, [miniconda]() is recommended

```bash
git clone https://github.com/cenaero-enb/h2cs-design.git
cd h2cs-design
python setup.py install
```

To be completed ...

## Usage

To be completed ...

??? Evaluating only PV and Battery requires a linear program solver???

??? Adding a generator and/or multiple outages makes the problem mix-integer linear, and thus requires a MILP solver.

???VPPopt will be tested with Cbc and IPOPT???

Ask ULB for testing with CPLEX

## Example

```python
import vppopt
m = vppopt.Model(solver='IPOPT')
results = vppopt.run_vppopt(m,'path/to/senario.json')
```

## Contribution

For contributing to the project development, you will need a github account (free)

After creating a github acount you can loged in h2cs-design repository using your account.

On the web interface, press [Fork](https://github.com/cenaero-enb/h2cs-design) to fork the repository to your gittest account.

Clone the repository from your gittest account on your computer or your work station

```bash
git clone https://github.com/your-github-account/h2cs-design.git
cd h2cs-design
```

Add a remote upstream so that you can get changes from the `main` branch

```bash
git remote add upstream https://github.com/cenaero-enb/h2cs-design.git
```

Make changes (for ex. edit README file with vim vi README.md) and then commit your changes

```bash
vi README.md
commit -m "Made changes to README.md" README.md
```

Fetch upstream changes, without changing local files, and merge changes from the upstream master (the main repo) with your local files

More detail about forking projects could be found [HERE](https://guides.github.com/activities/forking/)

```bash
# Fetch all branches of remote upstream
git fetch upstream
git merge upstream/master
```

Push the changes to your repository

```bash
git push
```

Finally, on the web interface of your account, open a `Pull Request` so that the changes are merged to the `main` or `develop` branch. By using @mention system in your Pull Request message, you can ask for feedback from specific people or teams, whether they're down the hall or ten time zones away. Pull Requests provide a way to notify project maintainers about the changes you'd like them to consider.

## Main developers

|Name|Affiliation|Email|
|-----|-----|-----|
|Van long Lê|Cenaero|vanlong.le@cenaero.be|

## supported solvers

|Solver|License|Supports|
|------|-----|------|
||||
