"""
Exploration data analysis
https://en.wikipedia.org/wiki/Exploratory_data_analysis

Here we will extract all import variables from the dataset and leave the useless variables behind.
We also try to identiy outliners, missing values or human errors.
Ultimatly;  maximizing the insights of the dataset and minimizing the potential error that may occur in later processes.

Author: Arjan de Haan (Vepnar)
Date: 25 Aug 2020

Content:
    - parse_lines: Cleaning and converting variables.
    - de_emojify: Cutout emojis from text messages.

TODO: Add argument and return description
"""

import re
import time
from datetime import datetime

# Note: My system language is dutch. update these strings to fit your language.
EXTERNAL_MEDIA = '<Media weggelaten>'
MESSAGE_DELETED = 'U hebt dit bericht verwijderd'

# Regular exptression to discard all emojis
# Source: https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b#gistcomment-3360005
EMOJI_PATTERN = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", flags=re.UNICODE)


def emoji_filter(line):
    """Cut out all emoticons with a regular expression"""
    return EMOJI_PATTERN.sub(r'', line)


def parse_lines(line: str, remove_media=True, remove_deleted=True, remove_emojis=True, minimum_length=3) -> tuple:
    """Data cleaning

    This part of the code does the essential cleaning and converting of usefull variables.
    Useless variables & human errors will be removed.

    "Rubbish in; Rubbish out."
    https://en.wikipedia.org/wiki/Garbage_in,_garbage_out
    """
    try:

        # Remove and parse the date
        date, message = line.split(' - ', 1)
        date = datetime.strptime(date, '%d-%m-%Y %H:%M')

        # Remove and parse the author of the message.
        sender, message = message.split(': ', 1)

        # Remove external media when this is enabled.
        if remove_media and EXTERNAL_MEDIA in message:
            return

        # Remove deleted messages when this is enabled.
        if remove_deleted and MESSAGE_DELETED in message:
            return

        # Remove emoticons when this is enabled.
        if remove_emojis:
            message = emoji_filter(message)

        # Remove messages below the given thresholdv
        if minimum_length > len(message):
            return

        return date, sender, message

    except:
        pass
