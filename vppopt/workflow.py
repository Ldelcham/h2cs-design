
import json
import python_jsonschema_objects as pjs
from vppopt.schemas import WORKFLOW_SCHEMA

class WorkFlow(object):
    """
    VPPOPT workflow class
    """
    def __init__(self) -> None:
        super().__init__()

        builder = pjs.ObjectBuilder(WORKFLOW_SCHEMA)
        ns = builder.build_classes()
        self.workflow = ns.VppoptWorkflowSchema()
        self.filepath = None
    
    @property
    def workflow_for_json(self):
        """
        workflow object to json
        """
        return self.workflow.for_json()
    
    def load_workflow(self,jsonWorkflow):
        """
        docstring
        """
        try:
            with open(jsonWorkflow,"r") as jsonFile:
                currentWF = json.load(jsonFile)
        except:
            try:
                currentWF = json.loads(jsonWorkflow)
            except:
                err_msg="ERROR: json workflow must be json file or string not {}".format(type(jsonWorkflow))
                raise Exception(err_msg)
        for key, val in currentWF.items():
            self.workflow[key] = val
    
    def saveAs(self,filepath):
        """
        save workflow as a json file
        ----------------------------
        filepath: string, file path including file name and extension
        """
        with open(filepath,'w') as jsonFile:
            json.dump(self.workflow.for_json(),jsonFile,indent=4)
        self.filepath = filepath
    
    def save(self):
        """
        docstring
        """
        if not self.filepath:
            err_msg = "ERROR: filepath attribute of JsonWorkflow instance is not set, saveAs function should be use"
            raise Exception(err_msg)
        
        with open(self.filepath,'w') as jsonFile:
            json.dump(self.workflow.for_json(),jsonFile,indent=4)

        #self.saveAs(self.filepath)     

        