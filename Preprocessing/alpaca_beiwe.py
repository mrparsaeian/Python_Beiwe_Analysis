# from read_beiwe_data import read_all_data

from read_beiwe_data import read_all_data
import os
from m1 import f1
my_current_dir = "/media/D_Drive/PJ/git-projects/Beiwe-Analysis/Preprocessing/Python"
root_dir_control = '/media/D_Drive/PJ/git-projects/Beiwe-Analysis/data/data_17participants/control_group/'
os.chdir(my_current_dir)
read_all_data(root_dir_control)
f1()
