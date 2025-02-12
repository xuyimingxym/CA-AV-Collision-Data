# CA_AV_Collision_Data
## Introduction
The rapid advancement of autonomous vehicles (AVs) and the emergence of robotaxi services have the potential to transform urban mobility. However, public concerns regarding AV safety remain a significant barrier to widespread adoption. While extensive AV testing has been conducted in controlled environments, real-world accident data is crucial for understanding safety risks and enhancing public trust. This study addresses the gap in AV-specific accident datasets by presenting a comprehensive synthetic dataset of AV collisions in California, covering all reported AV-involved accidents from January 1, 2019, to December 31, 2024. The dataset integrates information from California DMV accident reports, geographical data derived using Geographic Information System (GIS) tools, and semantic information extracted via Large Language Models (LLMs). The resulting tabular dataset supports a wide range of applications, including AV crash pattern analysis, contributing factor identification, risk assessment, safety algorithm refinement, regulatory policy development, and urban infrastructure planning. 

## Data
The data encompasses all reported AV-involved accidents in California from January 1, 2019, to December 31, 2024, comprising a total of 646 records. It integrates report data, geographical coordinates, and semantic information into a single tabular dataset in CSV (comma-separated values) format. See **CA_AV_Collision_2019-2024.csv**.
### Data Records

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
