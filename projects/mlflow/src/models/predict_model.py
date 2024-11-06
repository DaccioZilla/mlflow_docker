import mlflow
logged_model = 'runs:/3dae27d3872f49c7adc303952d219f92/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
import os
os.chdir('/opt/projects/mlflow')
data = pd.read_csv('./data/processed/casas_X.csv')

data['predicted'] = loaded_model.predict(pd.DataFrame(data))
data.to_csv('./data/processed/precos.csv', index= False)