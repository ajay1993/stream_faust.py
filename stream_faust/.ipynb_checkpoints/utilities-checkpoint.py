
import pandas as pd
from fuzzywuzzy import fuzz
import faust, datetime

def stream_data(topic_name, brocker_url,serializer_name):
    
    app = faust.App(
    topic_name,
    broker=brocker_url,
    value_serializer=serializer_name,)
    
    test3_topic = app.topic(topic_name)
    #print(test3_topic)
    @app.agent(test3_topic)
    async def test(test3):
        async for x in test3:
            print('1')
            print(x)
            value = []
            value = x
            print("do what ever u want")
    
    
    return(value)

def raw_data(path,encoder_name):
    
    value = pd.read_csv(path, index_col=None, header=0,encoding=encoder_name)
    
    return(value)


