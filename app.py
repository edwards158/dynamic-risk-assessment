from flask import Flask
import json
import os
import diagnostics
import scoring as score
from flask import Flask, session, jsonify, request

# Set up variables for use in our script
app = Flask(__name__)
app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'

with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
test_data_path = os.path.join(config['test_data_path'])

prediction_model = None


@app.route("/prediction", methods=['POST', 'OPTIONS'])
def predict():
    dataset_path = request.json.get('dataset_path')
    predictions = diagnostics.model_predictions(dataset_path)
    return str(predictions)


@app.route("/scoring", methods=['GET', 'OPTIONS'])
def scoring():
    f1_score = score.score_model()
    return str(f1_score)


@app.route("/summarystats", methods=['GET', 'OPTIONS'])
def stats():
    result = diagnostics.dataframe_summary()
    return str(result)


@app.route("/diagnostics", methods=['GET', 'OPTIONS'])
def diag():
    execution_time = (diagnostics.execution_time())
    missing_values = (diagnostics.missing_data_summary())
    package_data = (diagnostics.outdated_packages_list())
    return str("execution_time:" + execution_time + "\n" + "missing_values"
               + missing_values + "\n" + "package_data" + "\n" + package_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
