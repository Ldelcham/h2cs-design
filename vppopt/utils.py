
from oemof.solph import options
import networkx as nx
from loguru import logger
from pyomo.core.base import label
import matplotlib.pyplot as plt

def draw_graph(
    grph,
    edge_labels=True,
    node_color="#AFAFAF",
    edge_color="#CFCFCF",
    plot=True,
    node_size=2000,
    with_labels=True,
    arrows=True,
    layout="neato",
    **kwargs
):
    """
    Parameters
    ----------
    grph: networkxGraph
        graph object to be drawn
    edge_labels : boolean
        Use nominal values of flow as edge label
    node_color : dict or string
        Hex color code oder matplotlib color for each node. If string, all
        colors are the same.

    edge_color : string
        Hex color code oder matplotlib color for edge color.

    plot : boolean
        Show matplotlib plot.

    node_size : integer
        Size of nodes.

    with_labels : boolean
        Draw node labels.

    arrows : boolean
        Draw arrows on directed edges. Works only if an optimization_model has
        been passed.
    layout : string
        networkx graph layout, one of: neato, dot, twopi, circo, fdp, sfdp.
    """
    if isinstance(node_color,dict):
        node_color = [node_color.get(g,"#AFAFAF") for g in grph.nodes()]
    # set drawing options
    options = {
        "with_labels": with_labels,
        "node_color": node_color,
        "edge_color": edge_color,
        "node_size": node_size,
        "arrows": arrows
    }
    # Try to use pygraphviz for graph layout
    try:
        import pygraphviz
        pos = nx.drawing.nx_agraph.graphviz_layout(grph, prog=layout)
    except ImportError:
        logger.error("Module pygraphviz is not found, the graph will not be plotted")
        return
    
    # draw graph
    nx.draw(grph,pos=pos,**options)

    # add edge labels for all edges
    if edge_labels:
        labels = nx.get_edge_attributes(grph,"weight")
        nx.draw_networkx_edge_labels(grph,pos=pos,edge_labels=labels)
    if plot:
        plt.show()


def run_external_script(
    workflow=None,
    energy_system=None,
    om = None,
    script_type = "",
    **kwargs
):
    
    import sys
    import importlib

    pass