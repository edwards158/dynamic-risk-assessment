import os
import json
import pandas as pd

# Load config.json and get input and output paths
with open('config.json', 'r') as f:
    config = json.load(f)

input_folder_path = config['input_folder_path']
output_folder_path = config['output_folder_path']


def merge_multiple_dataframe():
    # check for datasets, compile them together, and write to an output file

    columns = ['corporation', 'lastmonth_activity',
               'lastyear_activity', 'number_of_employees', 'exited']
    final_dataframe = pd.DataFrame(columns=columns)

    filenames = os.listdir(input_folder_path)

    for each_filename in filenames:
        file_path = os.path.join(input_folder_path, each_filename)

        df = pd.read_csv(file_path)
        final_dataframe = final_dataframe.append(
            df).reset_index(drop=True)

    final_dataframe.drop_duplicates(inplace=True)

    final_dataframe.to_csv(os.path.join(
        output_folder_path, 'finaldata.csv'), index=False)

    output_location = os.path.join(output_folder_path, 'ingestedfiles.txt')

    myfile = open(output_location, 'w')
    for each_filename in filenames:
        myfile.write(each_filename + "\n")
    myfile.close()


if __name__ == '__main__':
    merge_multiple_dataframe()
