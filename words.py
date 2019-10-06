"""
Dictionary object for spelling bee
"""
import random
import pandas as pd


class BeeWords:
    def __init__(self, fn: str):
        self.words = [{'english': 'mum', 'estonian': 'ema'},
                      {'english': 'cat', 'estonian': 'kass'}]
        df = pd.read_csv(fn, delimiter=",")
        self.words = df.to_dict('records')

    def get_word(self):
        return random.choice(self.words)
