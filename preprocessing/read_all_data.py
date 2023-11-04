import pandas as pd
from os import listdir
from os.path import join, exists


class participants:
    def __init__(self, init_root_dir):
        self.traversals = ["group", "participants", "sensors", "metrics"]
        self.dictionary = {}
        self.dictionary = self.read_traversals(
            init_root_dir, 0, self.dictionary)

    def read_traversals(self, root, current_traversal_index, dictionary):
        if exists(root):
            print(f'current_traversal_index:{current_traversal_index}')
            dictionary[self.traversals[current_traversal_index]
                       ] = pd.DataFrame()
            if self.traversals[current_traversal_index] == 'metrics':
                print(f'Metrics dir:{root}')
                for data_file_name, index in zip(listdir(root), range(len(listdir(root)))):
                    print(
                        f'Processing data files: {data_file_name}', '\n'
                        f'Processing data files: {dictionary[self.traversals[current_traversal_index]]}')
                    dictionary[self.traversals[current_traversal_index]] = pd.concat(
                        [dictionary[self.traversals[current_traversal_index]], pd.read_csv(join(root, data_file_name))])
            else:
                for traversal_name, index in zip(listdir(root), range(len(listdir(root)))):
                    print(f'Processing: {traversal_name}')
                    dictionary[self.traversals[current_traversal_index]].loc[index,
                                                                             f'{self.traversals[current_traversal_index]}_id'] = traversal_name
                    print(dictionary[self.traversals[current_traversal_index]])
                return self.read_traversals(
                    join(root, traversal_name), current_traversal_index+1, dictionary)
        else:
            return None

    def read_data(self, participant_df):
        if exists(participant_dir):
            participant_df = pd.DataFrame()
            for sensor_file_name in listdir(participant_dir):
                print(f'Processing sensor: {sensor_file_name}')
                participant_df.loc[sensor_file_name,] = self.read_sensor(
                    join(participant_dir, sensor_file_name))
            return participant_df
        else:
            return None

    def read_sensor(self, sensor_dir):
        if exists(sensor_dir):
            sensor_df = pd.DataFrame()
            print(listdir(sensor_dir))
            print(f'sensor_dir is {sensor_dir}')
            for data_file_name in listdir(sensor_dir):
                print(
                    f'Processing data file: {join(sensor_dir, data_file_name)}')
                sensor_df = pd.concat([sensor_df,
                                       pd.read_csv(join(sensor_dir, data_file_name))])
            return data_type_frame
        else:
            return None
