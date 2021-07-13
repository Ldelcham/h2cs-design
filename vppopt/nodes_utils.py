# -*- coding: utf-8 -*-
"""
General description
-------------------
Collection of functions for handling with oemof.solph nodes
"""

import os
from oemof import solph
from oemof.network.network import Outputs
from oemof.solph.network.flow import Flow
import pandas as pd
from pyomo.core.base import label

def nodes_data_excel(excel_path,**kwargs):
    """
    Return a dictionary of pandas series from Excel sheet

    Parameters
    ----------
    excel_path : :obj:`str`
        Path to excel file
    
    Possible keyword arguments
    --------------------------
    engine: :obj: `str`
        Engine for parsing excel file using pandas, by default engine='xlrd'

    Returns
    -------
    :obj:`dict`
        Imported nodes data
    """
    engine = kwargs.get("engine","xlrd")

    # does Excel file exist?
    if not excel_path or not os.path.isfile(excel_path):
        raise FileNotFoundError(
            "Excel data file {} not found.".format(excel_path)
        )

    xls = pd.ExcelFile(excel_path,engine=engine)

    try:
        nodes_data = {
            "buses": xls.parse("buses"),
            "commodity_sources": xls.parse("commodity_sources"),
            "transformers": xls.parse("transformers"),
            "renewables": xls.parse("renewables"),
            "demand": xls.parse("demand"),
            "storages": xls.parse("storages"),
            "powerlines": xls.parse("powerlines"),
            "timeseries": xls.parse("time_series"),
            # "financial":xls.parse("financial")
        }
    except KeyError:
        err_msg = "Excel file must contains: [buses, commodity_sources, transformers, renewables, demand, storages, powerlines and timeseries].\n\
        The following sheets are found: {}".format(xls.sheet_names)
        raise Exception(err_msg)

    # set datetime index
    nodes_data["timeseries"].set_index("timestamp", inplace=True)
    nodes_data["timeseries"].index = pd.to_datetime(
        nodes_data["timeseries"].index
    )

    print("Data from Excel file {} imported.".format(excel_path))

    return nodes_data
#====================================#
def nodes_from_dict(nd=None,**kwargs):
    """
    Return nodes (oemof objects) from node dict
    Parameters
    ----------
    nd : :obj:`dict`
        Nodes data

    Returns
    -------
    nodes : `obj`:dict of :class:`nodes <oemof.network.Node>`
    """

    if not nd:
        err_msg = "ERROR: No nodes data provided"
        print(err_msg)
        return 1
    nodes = []
    #==============================#
    #Create BUS objects from buses table
    busd = {}

    for i, b in nd["buses"].iterrows():
        if b["active"] and not pd.isnull(b["active"]):
            bus = solph.Bus(label=b["label"])
            nodes.append(bus)

            busd[b["label"]] = bus
            if b["excess"]:
                # Automatically add Sink for curtailment
                nodes.append(
                    solph.Sink(
                        label=b["label"] + "_excess",
                        inputs={
                            busd[b["label"]]:solph.Flow(
                                variable_costs = b["excess costs"]
                            )
                        },
                    )
                )
            
            if b["shortage"]:
                nodes.append(
                    solph.Source(
                        label = b["label"] + "_shortage",
                        outputs={
                            busd[b["label"]]:solph.Flow(
                                variable_costs=b["shortage costs"]
                            )
                        },
                    )
                )
    
    # Create Source objects from table 'commodity sources'
    for i, cs in nd["commodity_sources"].iterrows():
        if cs["active"] and not pd.isnull(cs["active"]):
            nodes.append(
                solph.Source(
                    label=cs["label"],
                    outputs={
                        busd[cs["to"]]: solph.Flow(
                            variable_costs = cs["variable costs"]
                        )
                    },
                )
            )
    # Create Source objects with fixed time series from 'renewables' table
    for i, re in nd["renewables"].iterrows():
        if re["active"] and not pd.isnull(re["active"]):
            # set static outflow values
            outflow_args = {
                "nominal_value":re["capacity"]
            }
            # get time series for node and parameter
            for col in nd["timeseries"].columns.values:
                if col.split(".")[0] == re["label"]:
                    outflow_args[col.split(".")[1]]=nd["timeseries"][col]
            
            # TODO add investment, NON-CONVEX to outflow_args
            if re["capex"] and not pd.isnull(re["capex"]):
                pass
            
            # create
            nodes.append(
                solph.Source(
                    label=re["label"],
                    outputs = {
                        busd[re["to"]]:solph.Flow(**outflow_args)
                    }
                )
            ),
    
    # Create Sink objects with fixed time series from 'demand' table
    for i, de in nd["demand"].iterrows():
        if de["active"] and not pd.isnull(de["active"]):
            # set static inflow values
            inflow_args = {
                "nominal_value":de["nominal value"]
            }
            # get time series for node and parameter
            for col in nd["timeseries"].columns.values:
                if col.split(".")[0]==de["label"]:
                    inflow_args[col.split(".")[1]]=nd["timeseries"][col]
            
            # Create Sink object and append to nodes
            nodes.append(
                solph.Sink(
                    label=de["label"],
                    inputs={
                        busd[de["from"]]:solph.Flow(**inflow_args)
                    }
                )
            )
    
    # Create Link objects 
    for i, p in nd["powerlines"].iterrows():
        if p["active"]:
            bus1 = busd[p["bus_1"]]
            bus2 = busd[p["bus_2"]]
            nodes.append(
                solph.custom.Link(
                    label = "powerline" + "_" + p["bus_1"] + "_" + p["bus_2"],
                    inputs = {
                        bus1:solph.Flow(),
                        bus2:solph.Flow
                    },
                    outputs = {
                        bus1: solph.Flow(nominal_value = p["capacity"]),
                        bus2: solph.Flow(nominal_value=p["capacity"]),
                    },
                    conversion_factors={
                        (bus1,bus2):p["efficiency"],
                        (bus2,bus1):p["efficiency"]
                    }

                )
            )


    
    return nodes
