
import logging
from vppopt.workflow import WorkFlow
from loguru import logger
from oemof import solph
import pandas as pd
import datetime
import os


def run_external_script(
    workflowObj,
    esys=None,
    om = None,
    script_type="reporting"
    ):

    """
    run external python script for run_vppopt and vppopt run 
    ===========================
    """
    workflow_for_json = workflowObj.workflow_for_json
    if not workflow_for_json:
        err_msg = "ERROR: vppopt json workflow not found"
        logger.error(err_msg)
        return 1
    
    # script type must be either 'inputgen' or 'energyplus' or 'reporting'
    if not script_type or not any(script_type==el for el in ["inputgen", "model","reporting"]):
        err_msg = "ERROR: script_type is missed or not equal to either 'inputgen', 'mode' or 'reporting'"
        logger.error(err_msg)
        return 1
    
    import sys
    import importlib
    externalScript = workflow_for_json["ExternalScript"]
    scriptDir = str(externalScript["script_dir"])
    if not os.path.exists(scriptDir):
        err_msg = "ERROR: No such file or directory {}".format(scriptDir)
        logger.error(err_msg)
        return 1
    
    # should check if path already exisist
    if not os.path.dirname(scriptDir) in sys.path:
        sys.path.append(os.path.dirname(scriptDir))
    
    script_count = 0
    for script in externalScript["scripts"]:
        if (not script["tag"]) or (not script["name"]):
            script_count+=1
            print(
                "WARNING: script name and tag must be specified for all external python script. Name and/or tag of script [{}] is/are missed".format(script_count)
                )
        if str(script["tag"]).lower()==script_type.lower():
            importedModule = importlib.import_module("scripts.{}".format(script["name"]))
            kwargs = script["arguments"]
            kwargs["workflowObj"] = workflowObj

            # for key_name in script["additional_arguments"]:
            #     if key_name in kwargs.keys():
            #         err_msg = "ERROR: key name conflict between script principal arguments and additional one {}".format(key_name)
            #         raise Exception(err_msg)

            #     if not key_name in additional_args.keys():
            #         err_msg = "ERROR: {} is not found in function keyword additional arguments {}".format(key_name,additional_args.keys())
            #         raise Exception(err_msg)

            #     kwargs[key_name] = additional_args[key_name]

            eval("importedModule.main(esys, om,**kwargs)")

def run_vppopt(nodes,**kwargs):
    """
    :param model - pyomo abstract model
    """
    workflowObj = kwargs.get("workflowObj")
    # TODO: timeindex could be gotten from vppopt.json, timeseries data
    # simulation settings
    timeindex = kwargs.get('timeindex',None)
    periods = kwargs.get('periods',8760)

    # optimizer setting
    # solver could be gotten from vppopt also
    solver = kwargs.get('solver','cbc')
    solver_io = kwargs.get('solver_io',"lp")
    executable = kwargs.get('executable',"")
    solve_kwargs = kwargs.get('solve_kwargs',{})
    solver_cmd_options = kwargs.get("cmdline_options",{})


    if not timeindex:
        logger.info("No timeindex is specified, only 24 hours will be considered as simulation time")
        start_date = datetime.datetime(datetime.datetime.now().year,1,1)
        timeindex = pd.date_range(start=start_date,periods=periods,freq='H')    

    # model creation and solving
    logger.info("Starting optimization")

    # initilisation of the energy system
    energy_system = solph.EnergySystem(timeindex=timeindex)

    # add nodes and flows to energy system
    energy_system.add(*nodes)

    print("*********************************************************")
    print("The following objects have been added to energy system object:")
    for n in energy_system.nodes:
        oobj = str(type(n)).replace("<class 'oemof.solph.", "").replace("'>", "")
        print(oobj + ":", n.label)
    print("*********************************************************")

    #####################################
    # Optimize the energy system
    #####################################
    om = solph.Model(energy_system)

    # TODO: Do not understand what is it for?
    om.receive_duals()

    # solving the linear problem using the given solver
    om.solve(
        solver=solver,
        solver_io=solver_io,
        executable=executable,
        solve_kwargs=solve_kwargs,
        cmdline_options = solver_cmd_options        
        )

    return energy_system, om