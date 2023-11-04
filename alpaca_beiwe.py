
from preprocessing import participants
import os
import configparser

config = configparser.ConfigParser()
config.read(".config.cfg")
data_dir = config["DEFAULT"]["root_dir"]
print(data_dir)
participants01 = participants(data_dir)

# for group in participants01.traversals:
group = participants01.traversals[0]
print(participants01.dictionary[group])
