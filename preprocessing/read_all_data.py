import pandas as pd
from os import listdir
from os.path import join, exists, basename, normpath
import pickle
from sys import getsizeof


class participants:
    '''
        This class reads Beiwe data files recursively based on
        the root_dir config files variable defined in .config.cfg
        file and writes the data into pickle files for further analysis.
    '''

    def __init__(self, init_root_dir):
        self.traversals = ["group", "participants",
                           "sensors", "metrics", "surveys"]
        self.dictionary = {}
        """
         The init_root_dir variable contains the value from the config file is a single string but 
         read_traversals() function gets a 
         array in order to read all the other directories specific  to each values from self.traversals
        """
        init_root_dir = [init_root_dir]
        self.dictionary = self.read_traversals(
            init_root_dir, 0, self.dictionary)

    def read_traversals(self, dirs, current_traversal_index, dictionary):
        current_directories = []
        if current_traversal_index < 4:
            # if current_traversal_index < 5 or basename(normpath(root)) not in ['survey_answers', 'survey_timings']:
            for root in dirs:
                print(f'Current dir: {root}')
                # print(f'current_traversal_index:{current_traversal_index}')
                dictionary[self.traversals[current_traversal_index]
                           ] = pd.DataFrame()
                if self.traversals[current_traversal_index] == 'metrics':
                    # if self.traversals[current_traversal_index] == 'metrics' and basename(normpath(root)) not in ['survey_answers', 'survey_timings']:
                    print(f'Metrics dir:{root}')
                    for data_file_name, index in zip(listdir(root), range(len(listdir(root)))):
                        print(
                            f'Processing data files: {data_file_name}', '\n'
                            f'Processing data files: {dictionary[self.traversals[current_traversal_index]]}')
                        if basename(normpath(root)) == 'app_log':
                            """
                            the third column in app_log.csv contains commas.
                            The argument of usecols=range(3) is passed conditionally to it to bypass the error from ps.read_csv 
                            """
                            dictionary[self.traversals[current_traversal_index]] = pd.concat(
                                [dictionary[self.traversals[current_traversal_index]], pd.read_csv(join(root, data_file_name), usecols=range(3))])
                        else:
                            dictionary[self.traversals[current_traversal_index]] = pd.concat(
                                [dictionary[self.traversals[current_traversal_index]], pd.read_csv(join(root, data_file_name))])
                        # print(
                        #     dictionary[self.traversals[current_traversal_index]])
                else:
                    for traversal_name, index in zip(listdir(root), range(len(listdir(root)))):
                        print(f'Processing: {traversal_name}')
                        dictionary[self.traversals[current_traversal_index]].loc[index,
                                                                                 f'{self.traversals[current_traversal_index]}_id'] = traversal_name
                        current_directories.append(join(root, traversal_name))
                    # print(dictionary[self.traversals[current_traversal_index]])
                with open(f'{basename(normpath(root))}.pickle', 'wb') as handle:
                    pickle.dump(dictionary, handle,
                                protocol=pickle.HIGHEST_PROTOCOL)

            print(f'Current directories:{current_directories}')
            return self.read_traversals(
                current_directories, current_traversal_index+1, dictionary)
        else:
            return dictionary
