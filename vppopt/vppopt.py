
import logging
from oemof.tools import logger
from oemof import solph
import pandas as pd
import datetime

def run_vppopt(nodes,**kwargs):
    """
    :param model - pyomo abstract model
    """
    timeindex = kwargs.get('timeindex',None)
    periods = kwargs.get('periods',8760)

    solver = kwargs.get('solver','cbc')
    solver_io = kwargs.get('solver_io',"lp")
    executable = kwargs.get('executable',"")
    solve_kwargs = kwargs.get('solve_kwargs',{})
    solver_cmd_options = kwargs.get("cmdline_options",{})

    logger.define_logging()

    if not timeindex:
        logging.info("No timeindex is specified, only 24 hours will be considered as simulation time")
        start_date = datetime.datetime(datetime.datetime.now().year,1,1)
        timeindex = pd.date_range(start=start_date,periods=periods,freq='H')    

    # model creation and solving
    logging.info("Starting optimization")

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