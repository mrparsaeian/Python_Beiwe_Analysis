
from preprocessing import participant
import os
import configparser

config = configparser.ConfigParser()
config.read(".config.cfg")
data_dir = config["DEFAULT"]["root_dir"]
print(data_dir)
participant01 = participant(data_dir)

print(participant01.participant_names)
