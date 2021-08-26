import logging
import os
import sys
from oemof import solph

from oemof.solph.processing import meta_results, results
from vppopt.nodes_utils import nodes_data_excel_parser, create_nodes,nodes_from_dict
from vppopt.vppopt import run_vppopt, run_external_script
from vppopt.results import om_result_to_excel

import argparse
from vppopt.workflow import WorkFlow
from vppopt.schemas import excel_scenario_init
from loguru import logger

def main():
    parser = argparse.ArgumentParser(
        description='Script for initilazing vppopt scenario'
        )

    "Sub-commands arguments"
    subparsers = parser.add_subparsers(dest = "subcmd",help="sub-command help")

    #==========================#
    # init sub-command
    """
    cli init -pdir
    """
    init_parser = subparsers.add_parser("init",help="Initializing vppopt scenario and more")
    init_parser.add_argument('-pdir','--proj_dir',type=str,help='vppopt project directory')
    init_parser.add_argument('-s','--scenario',type=str,default="vppopt",help="name of vppopt scenario json file")
    
    #==========================#
    # run sub-command
    run_parser = subparsers.add_parser("run",help="run vppopt scenario and more")
    run_parser.add_argument(
        '-wf',
        '--workflow',
        type=str,
        help='[REQUIRED] vppopt JSON Workflow', 
        required=True
        )
    
    #==========================#
    # excel_reader sub-command
    excel_reader_parser = subparsers.add_parser("excel_reader",help="run vppopt with scenario read from excel file")
    excel_reader_parser.add_argument(
        'excel_file',
        metavar='excel_file',
        type=str,
        help='[REQUIRED] Excel File for vppopt scenario')
    
    excel_reader_parser.add_argument(
        '--graph',
        help="Path for saving energy system graph",
        type=str
    )
    excel_reader_parser.add_argument(
        '--result_excel',
        help="Path for saving energy system graph",
        type=str
    )

    args = parser.parse_args()

    "========================="
    if args.subcmd=='init':        
        # Default vppopt json workflow
        jsonWorkflow = WorkFlow()
        workflow = jsonWorkflow.workflow

        if not args.proj_dir:
            logger.info("No value is given for proj_dir argument, 'NewProject' directory will be created as project directory")
            projDir = os.path.join(os.getcwd(),"NewProject")
        else:
            projDir = os.path.abspath(args.proj_dir)
        
        # Verifying if the project directory is created
        if not os.path.exists(projDir):
            os.mkdir(projDir)
        workflow.ProjDir = projDir

        workflow.ExternalScript.script_dir = os.path.join(projDir,"scripts")
        scriptDir = str(workflow.ExternalScript.script_dir)
        if not os.path.exists(scriptDir):
            os.mkdir(scriptDir)
        
        # workflow name or senario name
        workflowName = os.path.split(args.scenario)[-1].split('.')[0]
        jsonWorkflow.saveAs(os.path.join(projDir,"{}.json".format(workflowName)))
        workflow.WorkflowFile = os.path.join(projDir,"{}.json".format(workflowName))

        # automatically generate excel input
        excel_path = os.path.join(projDir,"{}.xlsx".format(workflowName))
        excel_scenario_init(excel_path)
        workflow.NodesDataExcelFile = excel_path        
        
        # workflow.Scenario.Site.logitude=10.6 # TODO: addd restriction to json field

        jsonWorkflow.save()
    
    #===========================#    
    if args.subcmd=='run':

        if not os.path.isfile(os.path.abspath(args.workflow)):
            err_msg = "ERROR: No such file or directory {}".format(os.path.abspath(args.workflow))
            logger.error(err_msg)
            return 1
        
        workflowObj = WorkFlow()
        workflowObj.load_workflow(args.workflow)
        ################# Update Project dir#################
        # TODO: update project dir information in workflow file when move to another machine
        #####################################################
        # get nodes data excel file from workflow file
        nodesExcelFile = workflowObj.workflow_for_json["NodesDataExcelFile"]
        # read in nodes data from excel file into python dictionary
        nodes_data_dictionary = nodes_data_excel_parser(nodesExcelFile,engine='openpyxl')
        # create oemof nodes liste from nodes data dictionary
        nodes = nodes_from_dict(nd=nodes_data_dictionary)
        
        esys,om = run_vppopt(nodes)
        
        ############## Reporting external scripts would be run here############
        run_external_script(workflowObj,esys=esys,om=om, script_type="reporting")        
        
        # automatically store all 
        
    #===========================#    
    if args.subcmd=='excel_reader':
        if not os.path.isfile(os.path.abspath(args.excel_file)):
            err_msg = "ERROR: No such file or directory {}".format(os.path.abspath(args.excel_file))
            print(err_msg)
        
        # should try with xlrd first?
        nodes_data_dictionary = nodes_data_excel_parser(args.excel_file,engine='openpyxl')
        nodes = nodes_from_dict(nd=nodes_data_dictionary)
        esys,om = run_vppopt(nodes)

        ##############POST PROCESSING############
        # Energy System Graph
        if args.graph:
            from oemof.network.graph import create_nx_graph
            logger.info("Create graph of energy system")
            graph_name = args.graph
            graph = create_nx_graph(esys,filename=graph_name)
            if os.path.isfile(graph_name):
                print("Graph created at {}".format(os.path.abspath(graph_name)))
            else:
                print("Graph is not found at {}".format(os.path.abspath(graph_name)))
            
            from vppopt.utils import draw_graph
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
        ####################################################
        # Result excel file (could be automatically created)
        if args.result_excel:
            excel_path = args.result_excel
            om_result_to_excel(om, excel_path)
        
        meta_results = solph.processing.meta_results(om)
        import pprint as pp
        pp.pprint(meta_results)

        results = solph.processing.results(om)
        R1_bus_el_results = solph.views.node(results, "R1_bus_el")

if __name__=='__main__':
    main()