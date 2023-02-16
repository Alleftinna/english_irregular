import pandas as pd
import random
import re
import os

pre = os.path.dirname(os.path.realpath(__file__))
file_name = 'data/irregular.xlsx'
path = os.path.join(pre, file_name)


def get_rand():

    data = pd.read_excel(path)
    rows = data.shape[0]
    random_row = random.randint(1, rows - 1)
    words = {'0': f'{data.iloc[random_row][0]}', '1': f'{data.iloc[random_row][1]}', '2': f'{data.iloc[random_row][2]}'}
    st = f'{words["0"], words["1"], words["2"]}'

    st = re.sub(r"[\(\)]", '', st)
    # st = re.sub(r",", ', ', st)
    return st


def get_autoload():
    data = pd.read_excel(path)
    rows = data.shape[0]
    random_row = random.randint(1, rows - 1)
    words = {'0': f'{data.iloc[random_row][0]}', '1': f'{data.iloc[random_row][1]}', '2': f'{data.iloc[random_row][2]}'}

    return words
