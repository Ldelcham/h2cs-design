import os
import pandas as pd

from oemof.solph import processing, views
from oemof import solph

# om is the optimization model which has been solved

def om_result_to_excel(om, excel_path,**kwargs):
    if not isinstance(om, solph.Model):
        err_msg = "om must be solph Model object non {}".format(type(om))
        raise Exception(err_msg)
    
    result_data = processing.results(om)
    result_data = views.convert_keys_to_strings(result_data)
    writer = pd.ExcelWriter(excel_path,engine='xlsxwriter')
    # add regular optimization results
    nodes = sorted(
        set(
            [
                item for tup in result_data.keys() for item in tup
            ]
        )
    )
    for n in nodes:
        node_data = views.node(result_data,n)
        n = n[:15] # trim string length to allowed charts for a worksheet < 31 characters
        if 'scalars' in node_data:
            node_data["scalars"].to_excel(writer, sheet_name=n+'_scalars')
        if 'sequences' in node_data:
            # for key in keys:
            #     if key in data['sequences']:
            #         node_data["sequences"][key] = data["sequences"][key]
            node_data['sequences'].to_excel(writer, sheet_name=n+'_sequences')
    writer.save()
    if os.path.isfile(excel_path):
        print("Excel file created at {}".format(excel_path))
    else:
        print("Excel file not found at {}".format(excel_path))

