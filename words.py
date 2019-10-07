"""
Dictionary object for spelling bee
"""
import random
import pandas as pd
import boto3


class BeeWords:
    def __init__(self, fn: str):
        self.words = [{'english': 'mum', 'estonian': 'ema'},
                      {'english': 'cat', 'estonian': 'kass'}]
        df = pd.read_csv(fn, delimiter=",")
        self.words = df.to_dict('records')
        self.polly = boto3.Session(region_name="us-east-1").client("polly")

    def get_word(self):
        return random.choice(self.words)

    def say_english(self, w):
        response = self.polly.synthesize_speech(VoiceId='Joanna',
                                                TextType="ssml",
                                                OutputFormat="mp3",
                                                Text='<prosody rate="65%">' +
                                                     w + '</prosody>')
        return response["AudioStream"].read()
