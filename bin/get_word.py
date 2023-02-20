import pandas as pd
import random
import re
import os

pre = os.path.dirname(os.path.realpath(__file__))  # put project directory path in pre
file_name = 'data/irregular.xlsx'  # file name
path = os.path.join(pre, file_name)  # create full path

#  This function opens excel file then reads data from it and return one string
def get_rand():

    data = pd.read_excel(path)  # Open and read data from excel
    rows = data.shape[0]  # get data in rows format       ru -- en1 -- en2 -- en3
    random_row = random.randint(1, rows - 1)  # get random row from rows
    words = {'0': f'{data.iloc[random_row][0]}', '1': f'{data.iloc[random_row][1]}', '2': f'{data.iloc[random_row][2]}'}  # formating row
    output_row = f'{words["0"], words["1"], words["2"]}'  # make dict like ru -- en1 -- en2 -- en3

    output_row = re.sub(r"[\(\)]", '', output_row)  # remove all '(' and ')' from row

    return output_row