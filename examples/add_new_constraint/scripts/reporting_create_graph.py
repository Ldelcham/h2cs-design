from oemof import solph
from oemof.network.graph import create_nx_graph
from oemof.solph.processing import results
from vppopt.utils import draw_graph
from loguru import logger
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def main(esys, om, **kwargs):

    workflowObj = kwargs.get("workflowObj")

    print(om.integral_limit_emission_factor())

    results = solph.processing.results(om)
    data = solph.views.node(results, "bel")["sequences"]
    print(data.index)

    
    graph_data = []
    for col in data.columns:
        graph_data.append(go.Scatter(x=data.index, y=data[col],name=str(col)))
    
    fig = go.Figure(graph_data)
    fig.write_html("graph.html")

    
    logger.info("Create graph of energy system")
    graph_name = kwargs.get("graph_name")
    if not graph_name:
        graph_name = "esys.graphml"

    graph = create_nx_graph(esys,filename=graph_name)

    if os.path.isfile(graph_name):
        print("Graph created at {}".format(os.path.abspath(graph_name)))
    else:
        print("Graph is not found at {}".format(os.path.abspath(graph_name)))

    
    draw_graph(
        grph=graph,
        plot=True,
        node_size=1000,
        node_color={
            "bel":"yellow",
            "bh2":"green",
            "bheat":"red"
        }
    )