# Tutorial for using VPPopt

Inspired from

- [vpplib](https://github.com/Pyosch/vpplib)
- [micro-grids](https://github.com/MicroGridsPy/Micro-Grids)
- [Reoptlite](https://github.com/NREL/REoptLite)
- [OSeMOSYS](https://github.com/OSeMOSYS/OSeMOSYS) (Open-Source Energy Modelling System)
- [oemof](https://github.com/oemof)(Open Energy Modelling Framework)

## Inputs

Input to `run_vppopt` can be provided in one of three format:

1. a file path (string) to a JSON file
2. a Dict, or
3. using H2csInputs struct

The first option is perhaps the most straightforward one. For example, the minimum requirements for a JSON scenario file would look like:

```json
{
    "Site": {
        "longitude": -118.1164613,
        "latitude": 34.5794343
    },
    "ElectricLoad": {
        "doe_reference_name": "MidriseApartment",
        "annual_kwh": 1000000.0,
        "city": "Boulder"
    },
    "ElectricTariff": {
        "urdb_label": "5ed6c1a15457a3367add15ae"
    }
}
```

The order of the keys do not matter. Note that this scenario does not include any energy generation technologies and therefore the results can be used as a baseline for comparison to scenarios that result in cost-optimal generation technologies.

To add PV to the analysis simply add a PV key with an empty dictionary (to use default values):

```json
{
    "Site": {
        "longitude": -118.1164613,
        "latitude": 34.5794343
    },
    "ElectricLoad": {
        "doe_reference_name": "MidriseApartment",
        "annual_kwh": 1000000.0,
        "city": "Boulder"
    },
    "ElectricTariff": {
        "urdb_label": "5ed6c1a15457a3367add15ae"
    },
    "PV": {}
}
```

This scenario will consider the option 

## Examples

To run `vppopt` an optimization solver is needed. vppopt will be developed and test with opensource optimization solvers like IPOPT, CBC but it should work with other

- Linear Program solvers (for PV and Storage Scenarios)
- Mixed Integer Linear Program solver (for scenarios with outages and/or Generators)

### Basic

```python
import vppopt

m = Model(solver=IOPT)
results = run_vppopt(m,senario)
```

### Advanced

#### Manipulating Inputs

A senario.json goes through two conversion steps before the data is passed to the Pyomo model

1. Conversion to a python object? (julia struct)
2. conversion to a h2csInputs