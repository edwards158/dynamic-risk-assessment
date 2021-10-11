import numpy as np
import os
import json
import shutil

# Load config.json and correct path variable
with open('config.json', 'r') as f:
    config = json.load(f)

prod_deployment_path = os.path.join(config['prod_deployment_path'])
model_path = os.path.join(config['output_model_path'])
output_folder_path = config['output_folder_path']


def store_model_into_pickle():
    # copy the latest pickle file, the latestscore.txt value, and the ingestfiles.txt file
    # into the deployment directory

    model_file = os.path.join(model_path, 'trainedmodel.pkl')
    results_file = os.path.join(model_path, 'latestscore.txt')
    file_hist_file = os.path.join(output_folder_path, 'ingestedfiles.txt')

    shutil.copy(model_file, prod_deployment_path)
    shutil.copy(results_file, prod_deployment_path)
    shutil.copy(file_hist_file, prod_deployment_path)


if __name__ == "__main__":
    store_model_into_pickle()
