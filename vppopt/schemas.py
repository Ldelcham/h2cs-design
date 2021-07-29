import json
import os
from collections import OrderedDict

import pandas as pd
#===========================================
with open(os.path.join(os.path.dirname(__file__),"vppopt_schema.json"),"r") as jsonfile:
    WORKFLOW_SCHEMA = json.load(jsonfile)
#===========================================
# scenario excel template
SCENARIO_EXCEL_TMPL=OrderedDict(
    {
        "INFO":OrderedDict(),
        "buses":OrderedDict(
            {
                "label":[],
                "active":[],
                "excess":[],
                "shortage":[],
                "shortage costs":[],
                "excess costs":[]
            }
        ),
        "commodity_sources": OrderedDict(
            {
                "label":[],         # label
                "active":[],        # 
                "to":[],            # to_bus
                "variable costs":[] # variable cost, e.g. price
            }
        ),
        "demand":OrderedDict(
            {
                "label":[],         # label
                "active":[],        # 1 is active otherwise deactive
                "from":[],          # from_bus
                "nominal value":[], # maximum value
                "fixed":[]
            }
        ),
        "powerlines":OrderedDict(
            {
                "label":[],
                "active":[],        # 1 is active otherwise deactive
                "bus_1":[],         # from_bus
                "bus_2":[],         # to_bus
                "efficiency":[],    # transmission efficiency between 0 and 1
                "capacity":[]       # capacity in kWh?
            }
        ),
        "renewables": OrderedDict(
            {
                "label":[],
                "active":[],
                "to":[],
                "capacity":[],
                "capex":[],
                "max":[],
                "min":[],
                "existing":[],
                "epc_invest":[]
            }
        ),
        "storages":OrderedDict(
            {
                "label":[],
                "active":[],
                "bus":[],
                "capacity inflow":[],
                "capacity outflow":[],
                "nominal capacity":[],
                "capacity loss":[],
                "efficiency inflow":[],
                "efficiency outflow":[],
                "initial capacity":[],
                "capacity min":[],
                "capacity max":[],
                "variable input costs":[],
                "variable output costs":[],
                "capex":[],
                "max":[],
                "min":[],
                "existing":[],
                "epc_invest":[]
            }
        ),
        "transformers":OrderedDict(
            {
                "label":[],
                "active":[],        # 1 is active otherwise deactive
                "from":[],         # from_bus
                "to":[],         # to_bus,
                "efficiency":[],
                "capacity":[],
                "variable input costs":[],
                "capex inflow":[],
                "max inflow":[],
                "min inflow":[],
                "existing inflow":[],
            }
        ),
        "transformers_chp":OrderedDict(
            {
                "label":[],
                "active":[],        # 1 is active otherwise deactive
                "from":[],         # from_bus
                "to_el":[],         # to_bus,
                "to_heat":[],         # to_bus,
                "efficiency_el":[],
                "efficiency_heat":[],
                "capacity_el":[],
                "capacity_heat":[],
                "variable input costs":[],
                "capex elec":[],
                "max elec":[],
                "min elec":[],
                "existing elec":[]
            }
        ),
        "time_series":OrderedDict(
            {
                "timestamp":[]
            }
        ),
        "financial":OrderedDict(
            {
                "lifespan":[],
                "wacc":[]
            }
        )
    }
)
#===========================================
def excel_scenario_init(excel_path,**kwargs):    
    """
    Create empty excel file containing nodes data for oemof EnergySystem class.
    Inspired from https://github.com/oemof/oemof-examples/tree/master/oemof_examples/oemof.solph/v0.4.x/excel_reader

    Parameters
    ----------
    excel_path: str, excel file path
    
    """
    
    sheet_dict = {}
    for key,val in SCENARIO_EXCEL_TMPL.items():
        try:
            sheet_dict[key] = pd.DataFrame.from_dict(val)
        except:
            err_msg = "ERROR occurs"
            print(err_msg)
            return 1
    
    with pd.ExcelWriter(excel_path) as writer:
        for key, val in sheet_dict.items():
            val.to_excel(
                writer, 
                sheet_name=key,
                index = False
            )
    
    if not os.path.isfile(excel_path):
        err_msg = "ERROR: Excel file is not found at {}".format(excel_path)
        raise Exception(err_msg)
    else:
        print("Excel file is created at {}".format(excel_path))
        return

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Script for generating vppopt excel scenario'
        )
    parser.add_argument('excel_path',type=str,help='excel path')

    args =parser.parse_args()

    excel_scenario_init(args.excel_path)