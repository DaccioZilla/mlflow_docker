import requests
import pandas as pd

url = 'http://localhost:5050/invocations'

data = {
    'dataframe_split': {
        "columns": ['tamanho', 'ano', 'garagem'],
        'data':[
            [159.0,2010,2]
        ]
    }
}

header = {
    'Content-Type': 'application/json'
}

res = requests.post(
    url= url,
    headers= header,
    json= data
)

print(res.status_code, res.text)