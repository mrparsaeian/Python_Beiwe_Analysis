import read_single_data
import pandas as pd
from os import listdir
from os.path import join, exists
import configparser
read_single_data.read_accelerometer("sample_root_dir")
read_single_data.read_gps("sample_root_dir")
config = configparser.ConfigParser()
config.read(".config.cfg")
data_dir = config["DEFAULT"]["root_dir"]
print(data_dir)


def read_all_data(data_dir):
    print(data_dir)


class beiwe:
    def __init__(self):
        self.bewei_data = pd.DataFrame()

    def read_participants(self):
        sample_participant = participant()


class participant:
    def __init__(self, init_root_dir):

        self.participant_names = self.read_participant_names(init_root_dir)
        # self.beiwe_data = self.read_data(init_root_dir)

    def read_participant_names(self, root):
        if exists(root):
            participants_names_df = pd.DataFrame()
            for participant_name, index in zip(listdir(root), range(len(listdir(root)))):
                print(f'Processing participants: {participant_name}')
                participants_names_df.loc[index,
                                          "id"] = participant_name
            return participants_names_df
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


participant01 = participant(data_dir)

print(participant01.participant_names)
