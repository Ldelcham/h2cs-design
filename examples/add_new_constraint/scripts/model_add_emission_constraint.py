import pandas as pd
from oemof import solph
from oemof.solph import constraints

def script_description():
    desc = """"
    This script aims at adding an emission constraint in a model


    """
    return desc
def main(esys,om, **kwargs):
    # Add the emission constraint

    constraints.emission_limit(om, limit=100)

    # print out the emission constraint
    om.integral_limit_emission_factor_constraint.pprint()
    om.integral_limit_emission_factor.pprint()
    
