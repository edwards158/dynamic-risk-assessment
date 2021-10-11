import pandas as pd
import numpy as np
import timeit
import os
import json
import pickle
import common_functions

# Load config.json and get environment variables
with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
test_data_path = os.path.join(config['test_data_path'])
prod_deployment_path = os.path.join(config['prod_deployment_path'])


def model_predictions():
    # read the deployed model and a test dataset, calculate predictions
    filename = os.path.join(prod_deployment_path, 'trainedmodel.pkl')

    with open(filename, 'rb') as file:
        model = pickle.load(file)

    df = pd.read_csv(os.path.join(test_data_path, 'testdata.csv'))

    X_data, y_data = common_functions.get_columns()

    X = df[X_data].values
    y = df[y_data].values.ravel()

    predicted = model.predict(X)

    # return value should be a list containing all predictions
    return predicted


def dataframe_summary():
    # calculate summary statistics here

    df = pd.read_csv(os.path.join(dataset_csv_path, 'finaldata.csv'))

    summary_list = []
    X_data, _ = common_functions.get_columns()

    summary_dict = dict.fromkeys(X_data)
    stats_dict = {}

    for feature in X_data:
        stats_dict['mean'] = round(np.mean(df[feature]), 2)
        stats_dict['median'] = round(np.median(df[feature]), 2)
        stats_dict['std'] = round(np.std(df[feature]), 2)
        stats_dict_copy = stats_dict.copy()
        summary_dict[feature] = stats_dict_copy

    summary_list.append(summary_dict)

    return summary_list


def missing_data_summary():
    # calculate summary statistics here
    df = pd.read_csv(os.path.join(dataset_csv_path, 'finaldata.csv'))

    X_data, _ = common_functions.get_columns()
    summary_dict = dict.fromkeys(X_data)
    summary_list = []
    for feature in X_data:
        summary_dict[feature] = pd.isna(df[feature].sum())/len(df)*100

    summary_list.append(summary_dict)

    # return value should be a list containing all summary statistics
    return summary_list


def execution_time():
    # calculate timing of training.py and ingestion.py
    timing_dict = {'ingestion_time_secs': 0, 'training_time_secs': 0}
    timning_output = []

    starttime = timeit.default_timer()
    os.system('python3 ingestion.py')
    timing = timeit.default_timer() - starttime
    timing_dict['ingestion_time_secs'] = round(timing, 2)

    starttime = timeit.default_timer()
    os.system('python3 training.py')
    timing = timeit.default_timer() - starttime
    timing_dict['training_time_secs'] = round(timing, 2)

    timning_output.append(timing_dict)

    # return a list of 2 timing values in seconds
    return timning_output


def outdated_packages_list():
    os.system('python -m pip list  -o --format columns')


if __name__ == '__main__':
    model_predictions()
    dataframe_summary()
    missing_data_summary()
    execution_time()
    outdated_packages_list()
