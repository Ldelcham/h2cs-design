# Tutorial for using VPPopt

Inspired from

- vpplib
- micro-grids
- Reoptlite

## Inputs

Input tot `h2cs_run` can be provided in one of three format:

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

## Examples

To run `h2cs` an optimization solver is needed.

- Linear Program solvers
- Mixed Integer Linear Program solver

### Basic

```python
import h2cs

m = Model(solver=IOPT)
results = h2cs_run(m,senario)
```

### Advanced

#### Manipulating Inputs

A senario.json goes through two conversion steps before the data is passed to the Pyomo model

1. Conversion to a python object? (julia struct)
2. conversion to a h2csInputs