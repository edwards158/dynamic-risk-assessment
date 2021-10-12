from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import diagnostics
import common_functions

# Load config.json and get path variables
with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
test_data_path = os.path.join(config['test_data_path'])
output_figure_path = os.path.join(config['output_model_path'])


def score_model():
    # calculate a confusion matrix using the test data and the deployed model
    # write the confusion matrix to the workspace
    predictions = diagnostics.model_predictions(None)
    df = pd.read_csv(os.path.join(test_data_path, 'testdata.csv'))

    _, y_data = common_functions.get_columns()
    y = df[y_data].values.ravel()

    figures = os.path.join(output_figure_path, 'confusionmatrix.png')
    cm = confusion_matrix(y, predictions)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.savefig(fname=figures)
    plt.close()


if __name__ == '__main__':
    score_model()
