import json
import pandas as pd
import pickle
import os
import common_functions
from sklearn.metrics import f1_score


# Load config.json and get path variables
with open('config.json', 'r') as f:
    config = json.load(f)

model_path = os.path.join(config['output_model_path'])
test_data_path = os.path.join(config['test_data_path'])
output_folder_path = config['output_folder_path']


# Function for model scoring
def score_model(production=True):
    # this function should take a trained model, load test data, and calculate an F1 score
    # for the model relative to the test data
    # it should write the result to the latestscore.txt file

    filename = os.path.join(model_path, 'trainedmodel.pkl')

    with open(filename, 'rb') as file:
        model = pickle.load(file)

    if production:
        df = pd.read_csv(os.path.join(output_folder_path, 'finaldata.csv'))
    else:
        df = pd.read_csv(os.path.join(test_data_path, 'testdata.csv'))

    X_data, y_data = common_functions.get_columns()

    X = df[X_data].values
    y = df[y_data].values.ravel()

    predicted = model.predict(X)
    score = f1_score(y, predicted)

    output_location = os.path.join(model_path, 'latestscore.txt')
    templ = '{0:.10f}\n'
    with open(output_location, 'w') as f:
        f.write(templ.format(score))

    return score


if __name__ == "__main__":
    score_model()
