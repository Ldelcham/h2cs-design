
# VPPopt changelog

## v2021.02

## v2021.01 Initial release

### Platform features

This package is currently under development. Following, some idea for package developement

- package will be developed using python 3 (3.6+)
- an (LP or MILP) optimization solver will be needed for solving the optimization problem
- package must be robust
- user friendly
- flexibility (modularity, scalability)

### Package structure

```txt
h2cs-design
|__CHANGELOG.md
|__README.md
|__LICENSE.md
|__requirements.txt
|__setup.py
|__vppopt
|       |__src
|       |__compoments
|       |__interfaces
|       |__solver
|__docs
|   |__source
|__test
|__examples
```

Think about using  json schema for creating model
    - PV
    - Battery
    - fuel cell
    - electrolyser
  
Potential python package

pypsa
pvlib
pysam

### Possible sytem combination

- pv
- pv + battery
- pv + battery + fuel cell
- pv + battery + wind + fuel cell
- pv + battery + wind + fuell cell + hydrogen storage
- geothermal + hydrogen storage + fuel cell
  
**To be adapted ...**