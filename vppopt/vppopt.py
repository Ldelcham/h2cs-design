
import logging
from sys import executable
from oemof.tools import logger
from oemof import solph
import pandas as pd
import datetime

def run_vppopt(model, senario,**kwargs):
    """
    :param model - pyomo abstract model
    """
    timeindex = kwargs.get('timeindex',None)
    periods = kwargs.get('periods',24)

    solver = kwargs.get('solver','cbc')
    solver_io = kwargs.get('solver_io','lp'),
    executable = kwargs.get('executable',"")
    solve_kwargs = kwargs.get('solve_kwargs',{})

    if not timeindex:
        start_date = datetime.datetime(1,1,datetime.datetime.now().year)
        timeindex = pd.date_range(start=start_date,periods=periods,freq='H')

    logger.define_logging()
    

    # model creation and solving
    logging.info("Starting optimization")

    # initilisation of the energy system
    energy_system = solph.EnergySystem(timeindex=timeindex)

    #####################################
    # Optimize the energy system
    #####################################
    om = solph.Model(energy_system)

    # solving the linear problem using the given solver
    om.solve(solver=solver,solver_io=solver_io,executable=executable,solve_kwargs=solve_kwargs)

    return