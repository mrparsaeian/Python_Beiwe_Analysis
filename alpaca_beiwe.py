
from preprocessing import participants
import os
import configparser
import pickle


config = configparser.ConfigParser()
config.read(".config.cfg")
data_dir = config["DEFAULT"]["root_dir"]
print(data_dir)
# participants01 = participants(data_dir)

# for group in participants01.traversals:
# group = participants01.traversals[0]

with open('filename.pickle', 'rb') as handle:
    dict = pickle.load(handle)
# with open('filename.pickle', 'wb') as handle:
#     pickle.dump(participants01.dictionary, handle,
#                 protocol=pickle.HIGHEST_PROTOCOL)
print(dict)
