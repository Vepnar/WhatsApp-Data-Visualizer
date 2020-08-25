"""
Exploration data analysis
https://en.wikipedia.org/wiki/Exploratory_data_analysis

Here we will extract all import variables from the dataset and leave the useless variables behind.
We also try to identiy outliners, missing values or human errors.
Ultimatly;  maximizing the insights of the dataset and minimizing the potential error that may occur in later processes.

Author: Arjan de Haan (Vepnar)
Date: 25 Aug 2020

Content:
	- parse_lines: Cleaning and converting variables

"""

from datetime import datetime


def parse_lines(line: str) -> tuple:
    """Data cleaning

    This part of the code does the essential cleaning and converting of usefull variables.
    Useless variables & human errors will be removed.

    "Rubbish in; Rubbish out."
    https://en.wikipedia.org/wiki/Garbage_in,_garbage_out

    TODO: Add argument and return description


    """

    if ' -  ' in line:
        return
    date, _ = line.split(' - ', 1)
    date = datetime.strptime(date, '%d-%m-%Y %H:%M')
