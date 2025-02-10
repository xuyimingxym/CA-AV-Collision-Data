import pymupdf
import pandas as pd
import numpy as py
import os

def pdf2df(doc):
    widget_dict = {}
    for page in doc:
            for widget in page.widgets():
                    field_name = widget.field_name.title()
                    field_value = widget.field_value
                    widget_dict[field_name] = field_value
    df = pd.DataFrame.from_dict(widget_dict,orient='index',columns=[0])
    if df.shape[0] not in [266,268]:
          print('Failed...')
          return
    info_index = [0, 2] + list(range(9,31)) + list(range(40,75)) + list(range(77,89)) + list(range(144,147)) + list(range(148,262))
    output = df.iloc[info_index,:].T.replace([' ','Off'], ['Yes',''])
    output.loc[0, 'Address_2.1.0.1'] = output['Address_2.1.0.1'][0].replace("\r", " ")
    output.rename(columns={"Am":"AM","Pm":"PM",
               "Section 2  Accident Information.0":"Address Of Accident",
               "Section 2  Accident Information.1.0":"City", 
               "Section 2  Accident Information.1.1.0":"County", 
               "Section 2  Accident Information.1.1.1.0":"State",
               "Section 2  Accident Information.1.1.1.1":"Zip Code", 
               "Pedestrian":"Pedestrian Involved",
               "Bicyclist":"Bicyclist Involved",
               "Unknown":"Damage: Unknown",
               "None":"Damage: None",
               "Minor":"Damage: Minor",
               "Moderate":"Damage: Moderate",
               "Major":"Damage: Major",
               "Address_2.1.0.1":"Accident Detail Description",},
               inplace=True)
    return output

folder = "./AV Collision Reports/2019"
res = pd.DataFrame()
for file in os.listdir(folder):
    if file[-4:] == '.pdf':
        doc = pymupdf.open(os.path.join(folder,file))
        print(file)
        res = pd.concat([res,pdf2df(doc)])
res.to_csv('./Results.csv')