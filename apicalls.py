import os
import subprocess
import json


with open('config.json', 'r') as f:
    config = json.load(f)

# curl -X POST http://0.0.0.0:8000/prediction?inputdata=hello

# Call each API endpoint and store the responses
response1 = subprocess.run(
    ['curl', '127.0.0.1:8000/prediction'], capture_output=True).stdout
# print(response1.decode("utf-8"))
response2 = subprocess.run(
    ['curl', '127.0.0.1:8000/scoring'], capture_output=True).stdout
# print(response2.decode("utf-8"))
response3 = subprocess.run(
    ['curl', '127.0.0.1:8000/summarystats'], capture_output=True).stdout
# print(response3.decode("utf-8"))
response4 = subprocess.run(
    ['curl', '127.0.0.1:8000/diagnostics'], capture_output=True).stdout
# print(response4.decode("utf-8"))

# combine all API responses
responses = [response1.decode("utf-8"), response2.decode("utf-8"),
             response3.decode("utf-8"), response4.decode("utf-8")]

# write the responses to your workspace
filename = os.path.join(config['output_model_path'], 'apireturns.txt')

with open(filename, "w") as f:
    f.write(str(responses))
