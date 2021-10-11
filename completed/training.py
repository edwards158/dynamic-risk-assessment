import pandas as pd
import pickle
import os
import json
from sklearn.linear_model import LogisticRegression
import common_functions


# Load config.json and get path variables
with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
model_path = os.path.join(config['output_model_path'])


# Function for training the model
def train_model():

    # use this logistic regression for training
    model = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                               intercept_scaling=1, l1_ratio=None, max_iter=100,
                               multi_class='ovr', n_jobs=None, penalty='l2',
                               random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                               warm_start=False)

    filename = os.path.join(dataset_csv_path, 'finaldata.csv')

    df = pd.read_csv(filename)

    X_data, y_data = common_functions.get_columns()

    X = df[X_data].values
    y = df[y_data].values.ravel()

    # fit the logistic regression to your data
    model.fit(X, y)

    filename = os.path.join(model_path, 'trainedmodel.pkl')

    # write the trained model to your workspace in a file called trainedmodel.pkl
    pickle.dump(model, open(filename, 'wb'))


if __name__ == "__main__":
    train_model()
