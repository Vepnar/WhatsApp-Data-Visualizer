#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Create a chatbot based on the dataset with continuous-time markov chain

Author: Arjan de Haan (Vepnar)
Created: 1 January 2021
"""
import re
import numpy as np

# Markov chain stored as adjacency list.
LEXICON = {}

# Length of the 
WORD_LENGTH = 2

LINE_END_REGEX = re.compile(r'(\.|\!|\?|\n)')

def is_ending(line : str) -> bool:
    """Detect if the current line is ending.

    Args:
        line (str): Line that should be checked.

    Returns:
        bool: True when it is ending and false when it isn't ending.
    """
    return len(LINE_END_REGEX.findall(line)) > 0
