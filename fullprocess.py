import training
import scoring
import deployment
import diagnostics
import reporting
import ingestion
import os
import json
import pickle
import sys


with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
prod_deployment_path = os.path.join(config['prod_deployment_path'])
model_path = os.path.join(config['output_model_path'])
input_folder_path = config['input_folder_path']

# Check and read new data
# first, read ingestedfiles.txt

ingested_files = []
file_history_file = os.path.join(
    prod_deployment_path, 'ingestedfiles.txt')
with open(file_history_file, 'r') as f:
    lines = f.readlines()

ingested_files = [line.strip() for line in lines]

# second, determine whether the source data folder has files that
# aren't listed in ingestedfiles.txt
source_data_files = os.listdir(input_folder_path)

# Deciding whether to proceed, part 1
# if you found new data, you should proceed. otherwise, do end the process here

for file in ingested_files:
    if file not in source_data_files:
        print("New data found, ingesting data")
        ingestion.merge_multiple_dataframe()
        break
    else:
        print("No new data found, exiting program")
        sys.exit(0)


# Checking for model drift
# check whether the score from the deployed model is different from the score
# from the model that uses the newest ingested data
previous_score_file = os.path.join(
    prod_deployment_path, 'latestscore.txt')

with open(previous_score_file, 'r') as f:
    result = f.readline()
prod_score = float(result.strip())

new_score = scoring.score_model(production=True)

if new_score < prod_score:
    model_drift = True
if model_drift == False:
    print("No model drift detected, exiting")
    sys.exit()
# Deciding whether to proceed, part 2
# if you found model drift, you should proceed. otherwise, do end the process here
training.train_model()

# Re-deployment
# if you found evidence for model drift, re-run the deployment.py script
deployment.store_model_into_pickle()


##################Diagnostics and reporting
# run diagnostics.py and reporting.py for the re-deployed model
diagnostics.model_predictions(None)
diagnostics.execution_time()
diagnostics.dataframe_summary()
diagnostics.missing_data_summary()
diagnostics.outdated_packages_list()
reporting.score_model()
