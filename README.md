# Dynamic Risk Assessment

Create, deploy, and monitor a risk assessment ML model that will estimate the attrition risk of each of a company's 10,000 clients. If the model you create and deploy is accurate, it will enable the client managers to contact the clients with the highest risk and avoid losing clients and revenue.

## Project Steps Overview
Complete the project by proceeding through 5 steps:

- **Data ingestion** - Automatically check a database for new data that can be used for model training. Compile all training data to a training dataset and save it to persistent storage. Write metrics related to the completed data ingestion tasks to persistent storage.
- **Training, scoring, and deploying** - Write scripts that train an ML model that predicts attrition risk, and score the model. Write the model and the scoring metrics to persistent storage.
- **Diagnostic** - Determine and save summary statistics related to a dataset. Time the performance of model training and scoring scripts. Check for dependency changes and package updates.
- **Reporting** - Automatically generate plots and documents that report on model metrics. Provide an API endpoint that can return model predictions and metrics.
- **Process Automation** -  Create a script and cron job that automatically run all previous steps at regular intervals.

### Data Ingestion
- **ingestion.py** - Read data files into Python, and write them to an output file that will be your master dataset. Save a record of the files you've read

### Training, Scoring, and Deploying an ML Model
- **training.py, scoring.py, deployment.py** - training an ML model, generating scoring metrics for the model and deploying the trained model.
- 
### Model and Data Diagnostics
- **diagnostics.py** - script that performs diagnostic tests related to your model as well as your data.

### Model Reporting
- **reporting.py, app.py, apicalls.py** - scripts that create reports related to your ML model, its performance, and related diagnostics.

