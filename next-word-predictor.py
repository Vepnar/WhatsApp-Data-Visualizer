#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Predict the next word based on the dataset with markov chains.

Author: Arjan de Haan (Vepnar)
Created: 14 December 2020
"""
import numpy as np

# Markov chain stored as adjacency list.
lexicon = {}

def update_lexicon(current : str, next_word : str) -> None:
    """Add item to the lexicon.

    Args:
        current (str): Input word.
        next_word (str): Output word.
    """

    # Add the input word to the lexicon if it in there yet.
    if current not in lexicon:
        lexicon.update({current: {next_word: 1} })
        return

    # Recieve te probabilties of the input word.
    options = lexicon[current]

    # Check if the output word is in the propability list.
    if next_word not in options:
        options.update({next_word : 1})
    else:
        options.update({next_word : options[next_word] + 1})

    # Update the lexicon
    lexicon[current] = options

def ajust_probability() -> None:
    """Scale the probability to a 0-1 float"""
    for word, transition in lexicon.items():
        transition = dict((key, value / sum(transition.values())) for key, value in transition.items())
        lexicon[word] = transition

def parse_line(line : str) -> None:
    """Parse the given line and ajust the markov chain. 

    Args:
        line (string): Line of words
    """
    words = line.strip().split(' ')
    for i in range(len(words) - 1):
        update_lexicon(words[i], words[i+1])

def predict(word : str) -> str:
    """Attempt to predict the next word in the markov chain.

    Args:
        word (str): Last word in a line.

    Returns:
        str: Next word.
        None: current word is not in the markov chain.
    """
    if word not in lexicon:
        return None

    options = lexicon[word]
    return np.random.choice(list(options.keys()), p=list(options.values()))
    

def load_dataset():
    """Load the dataset from the file and update the markov chain"""
    with open('dataset.txt', 'r') as dataset:
        for raw_line in dataset:
            
            # Split the whatsapp data and only accept the language part
            line = raw_line.split(' ', 5)[-1].strip('\n')

            # Update markov chain.
            parse_line(line)
    ajust_probability()

def predict_loop():
    """Infinity loop of predictions"""
    while(1):
        
        # Recieve user input.
        line = input('> ')

        # Select the last word.
        word = line.strip().split(' ')[-1]
        word = predict(word)

        # Print a line if the word is found.
        if word is not None:
            print(line +' '+ word)


if __name__ == '__main__':
    load_dataset()
    try:
        predict_loop()
    except (KeyboardInterrupt, EOFError):
        pass