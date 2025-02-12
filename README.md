# CA_AV_Collision_Data
## Introduction
The rapid advancement of autonomous vehicles (AVs) and the emergence of robotaxi services have the potential to transform urban mobility. However, public concerns regarding AV safety remain a significant barrier to widespread adoption. While extensive AV testing has been conducted in controlled environments, real-world accident data is crucial for understanding safety risks and enhancing public trust. This study addresses the gap in AV-specific accident datasets by presenting a comprehensive synthetic dataset of AV collisions in California, covering all reported AV-involved accidents from January 1, 2019, to December 31, 2024. The dataset integrates information from California DMV accident reports, geographical data derived using Geographic Information System (GIS) tools, and semantic information extracted via Large Language Models (LLMs). The resulting tabular dataset supports a wide range of applications, including AV crash pattern analysis, contributing factor identification, risk assessment, safety algorithm refinement, regulatory policy development, and urban infrastructure planning. 

## Data
The data encompasses all reported AV-involved accidents in California from January 1, 2019, to December 31, 2024, comprising a total of 646 records. It integrates report data, geographical coordinates, and semantic information into a single tabular dataset in CSV (comma-separated values) format. See **CA_AV_Collision_2019-2024.csv**.
### Data Records
| Variable                        | Type        | Description                                                                                      |
|----------------------------------|------------|--------------------------------------------------------------------------------------------------|
| Manufacturers                   | Text       | Manufacturers name and business name                                                             |
| Date Of Accident                | Date       | Date of accident                                                                                 |
| Time Of Accident                | Time       | Time of accident                                                                                 |
| Vehicle Info                    | Text       | Vehicle year, make, model, license, VIN, register state                                         |
| Address Of Accident             | Text       | Accident address                                                                                 |
| Vehicle Motion                  | Text       | Vehicle was moving or stopped in traffic                                                        |
| Involved in Accident            | Text       | If pedestrian/bicyclist/other involved                                                          |
| Num Of Vehicles Involved        | Int        | Number of vehicles involved                                                                     |
| Vehicle Damage                  | Categorical | Unknown, None, Minor, Moderate, Major                                                           |
| Damage Area                     | Categorical | Areas of damage                                                                                 |
| Other Vehicle's Info            | Text       | Vehicle year, make, model, license, VIN, register state                                         |
| Other Vehicle's Motion          | Text       | Vehicle was moving or stopped in traffic                                                        |
| Conventional Mode               | Binary     | If vehicle was in conventional mode                                                             |
| Autonomous Mode                 | Binary     | If vehicle was in autonomous mode                                                               |
| Accident Detail Description     | Text       | Accident detail description                                                                     |
| Weather                         | Categorical | Clear, Cloudy, Raining, Snowing, Fog, Other, Wind                                               |
| Lighting                        | Categorical | Daylight, Dark-Dawn, Dark-Street lights, Dark-No street lights, Dark-Street lights not functioning |
| Road Surface                    | Categorical | Dry, Wet, Snowy-Icy, Slippery                                                                   |
| Roadway Conditions              | Categorical | Roadway conditions                                                                              |
| Movement Preceding Collision    | Categorical | Movement of vehicles preceding collision                                                        |
| Type of Collision               | Categorical | Head-on, Side swipe, Rear end, Broadside, Hit object, Overturned, Vehicle/pedestrian, Other    |
| Latitude                        | Float      | Latitude of accident location                                                                  |
| Longitude                       | Float      | Longitude of accident location                                                                 |
| Narrow Roadway                  | Binary     | If accident occurred on narrow roadway                                                         |
| Parked Vehicles                 | Binary     | If street-parked vehicles existed                                                              |
| Intersection                    | Binary     | If accident occurred at or near an intersection                                                |
| Struck by Others                | Binary     | If the AV was struck by others                                                                 |
| Other Party                     | Categorical | 1 for passenger car, 2 for truck, 3 for motorcycle, 4 for bicycle/e-scooter, 5 for pedestrian, 0 for other |

## Code
### Required library:
- pymupdf
- pandas
- numpy

### Run: 
In terminal, run
```
cd YOUR_REPORT_FOLDER
python pdf2py.py
```
The results will be saved as 'Results.csv' in the YOUR_REPORT_FOLDER directory.
