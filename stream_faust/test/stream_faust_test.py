
from unittest import TestCase
from stream_faust import utilities
import pandas as pd

path = 'stream_faust/data/iris.csv'
encoder_name = 'utf8'

topic_name = 'test3'
brocker_url = 'kafka://localhost:9092'
value_serializer = 'raw'

def test_stream_data():
    stream_data(topic_name, brocker_url,serializer_name)
    #print(value)
    
def test_raw_data():
    raw_data(path,encoder_name)
    #print(value)
