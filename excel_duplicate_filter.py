import pandas as pd  # pip install pandas
import os
import sys

#terminal_filename = sys.argv[1] # takes the filename entered in terminal

#file_name = terminal_filename  # assigns the name from terminal to a value.

file_name = 'new_FP.xlsx' # comment both lines above and uncomment this one if you want to change filename inside the script


"""try:
    directory_new = 'new'
    directory_old = 'old'
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory_new)
    os.mkdir(path)
    path = os.path.join(parent_dir, directory_old)
    os.mkdir(path)

except FileExistsError:
    print("directory 'new' and 'old' already present")
    pass"""


def remove_self_maps_and_dupes():
    data = pd.read_excel(file_name)
    no_dupes = data.drop_duplicates(subset=[data.columns.values[0]], keep="first")  # set keep to False if you don't
    # want to keep any values that would've been dupes
    # keep first keeps the 1st value and removes others
    self_maps = no_dupes[no_dupes.columns[0]] != no_dupes[no_dupes.columns[1]].str.upper()
    dataframe_final = no_dupes[self_maps]
    print(dataframe_final)
    dataframe_final.to_excel(os.getcwd() + "/"+ "filtered_"+ file_name )


remove_self_maps_and_dupes()
# uncomment line below to move original file to old folder
#os.rename(os.getcwd()+"/"+file_name, os.getcwd()+"/old/"+file_name)
