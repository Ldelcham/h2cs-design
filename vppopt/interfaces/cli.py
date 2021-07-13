import logging
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import argparse
from vppopt.workflow import WorkFlow

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
    run_parser.add_argument('-wf','--workflow',type=str,help='[REQUIRED] vppopt JSON Workflow', required=True)
    
    #==========================#
    # excel_reader sub-command
    excel_reader_parser = subparsers.add_parser("excel_reader",help="run vppopt with scenario read from excel file")
    excel_reader_parser.add_argument(
        'excel_file',
        metavar='excel_file',
        type=str,
        help='[REQUIRED] Excel File for vppopt scenario')

    args = parser.parse_args()

    "========================="
    if args.subcmd=='init':        
        # Default vppopt json workflow
        jsonWorkflow = WorkFlow()
        workflow = jsonWorkflow.workflow

        if not args.proj_dir:
            # if project directory is not specified, a directory named 
            # 'NewProject' will be created in the current working directory
            projDir = os.path.join(os.getcwd(),"NewProject")
        else:
            projDir = os.path.abspath(args.proj_dir)
        
        # Verifying if the project directory is created
        if not os.path.exists(projDir):
            os.mkdir(projDir)
        workflow.ProjDir = projDir

        workflowName = os.path.split(args.scenario)[-1].split('.')[0]
        jsonWorkflow.saveAs(os.path.join(projDir,"{}.json".format(workflowName)))

        workflow.WorkflowFile = os.path.join(projDir,"{}.json".format(workflowName))
        workflow.Scenario.Site.logitude=10.6

        jsonWorkflow.save()
    
    #===========================#    
    if args.subcmd=='run':

        if not os.path.isfile(os.path.abspath(args.workflow)):
            err_msg = "ERROR: No such file or directory {}".format(os.path.abspath(args.workflow))
            print(err_msg)

            #raise Exception(err_msg)
        
        from oemof.tools import logger
        from oemof.tools import economics


        logger.define_logging()
        logging.info("Initialize the energy system")
        
        epc_wind = economics.annuity(capex=1000,n=20,wacc=0.05)
        print(epc_wind)

        bus_dict = {}

        logging.info('Create oemof objects')
        
    #===========================#    
    if args.subcmd=='excel_reader':
        if not os.path.isfile(os.path.abspath(args.excel_file)):
            err_msg = "ERROR: No such file or directory {}".format(os.path.abspath(args.excel_file))
            print(err_msg)
        pass


if __name__=='__main__':
    main()