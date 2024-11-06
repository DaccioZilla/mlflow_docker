import os
from sklearn.model_selection import train_test_split
import pandas as pd
import xgboost 
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import argparse

os.chdir('/opt/projects/mlflow')

def parse_args():
    parser = argparse.ArgumentParser(description='House Parse ML')
    parser.add_argument(
        '--learning_rate', 
        type=float, 
        default= 0.3, 
        help = 'tamanho de passo na descida do gradiente'
    )
    parser.add_argument(
        '--max_depth', 
        type=int, 
        default= 6, 
        help = 'profundidade maxima das arvores'
    )

    return parser.parse_args()


df = pd.read_csv('./data/processed/casas.csv')

X = df.drop(columns=['preco'])
y = df['preco'].copy()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state= 42)

dTrain = xgboost.DMatrix(X_train, label = y_train)
dTest = xgboost.DMatrix(X_test, label = y_test)

mlflow.set_experiment('house_price-eda')

def main():
    args = parse_args()
    xgb_params = {
        'learning_rate': args.learning_rate,
        'max_depth': args.max_depth,
        'seed': 42
    }

    with mlflow.start_run():
        mlflow.xgboost.autolog()

        model = xgboost.train(xgb_params, dTrain, evals =[(dTrain, 'train')])

        model_pred = model.predict(dTest)

        mse = mean_squared_error(y_test, model_pred)
        rmse = mse ** 0.5
        r2 = r2_score(y_test, model_pred)

        mlflow.log_metrics({'MSE': mse, 'RMSE': rmse, 'R2': r2})

if __name__ == '__main__':
    main()