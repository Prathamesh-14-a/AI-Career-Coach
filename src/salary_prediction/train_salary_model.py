import pandas as pd 
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (

    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from xgboost import XGBRegressor


# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
BASE_PATH = Path("d:/Startup/Project/ai-career-coach")

DATA_PATH = BASE_PATH / 'data' / 'Salary Prediction Data'

SALARY_DATA_FILE = DATA_PATH / 'salary_feature_data.csv'


#------------------------------------------------------
# LOAD DATA
# -----------------------------------------------------
def load_data():
    try:
        df = pd.read_csv(SALARY_DATA_FILE)
        print("Data Loaded Successfully")
        print(df.shape)

        return df

    except FileNotFoundError:
        print('File Not Found')

    except Exception as e:
        print(f'File Loading Eroor : {e}')

        return None
    
# -------------------------------------------------------
# SPLIT X and y
# -------------------------------------------------------
def split_features_target(df):

    X = df.drop(columns =["Salary", "Skills"] )

    y = df['Salary']

    print(f'Feature matrix shape : {X.shape}')
    print(f'Target Shape: {y.shape}')
    print(f'Dtypes:{X.dtypes} , {y.dtypes}')

    return X , y


# ---------------------------------------------------------
# TRAIN TEST SPLIT 
# ---------------------------------------------------------
def train_test_split_data(X , y):
    X_train , X_test , y_train , y_test = train_test_split(
        X ,
        y ,
        test_size= 0.2 , 
        random_state= 42
    )

    print(f'Train Size : {X_train.shape}')
    print(f'Test_Size : {X_test.shape}')

    return X_train , X_test , y_train , y_test


# -----------------------------------------------------------
# TRAIN LINEAR REGRESSION
# -----------------------------------------------------------
def train_linear_regression(X_train , y_train):
    model = LinearRegression()

    model.fit(X_train , y_train)
    print("\nLinear Regression Trained")

    return model


#-------------------------------------------------------------
# MAKE PREDICTIONS
#-------------------------------------------------------------
def make_predictions(model , X_test):
    predictions = model.predict(X_test)

    print("\nPredictions Made")

    return predictions


#------------------------------------------------------------
# EVALUATE MODEL 
# -----------------------------------------------------------
def evaluate_model(y_test, predictions):

    mae = mean_absolute_error(y_test, predictions)

    rmse = np.sqrt(
        mean_squared_error(y_test, predictions)
    )

    r2 = r2_score(y_test, predictions)

    print("\nMODEL PERFORMANCE")
    print("-" * 30)

    print(f"MAE  : {mae:,.2f}")
    print(f"RMSE : {rmse:,.2f}")
    print(f"R²   : {r2:.4f}")

#-----------------------------------------------------------
# TRAIN RANDOM FOREST
#-----------------------------------------------------------
def train_random_forest(X_train, y_train):
    print("\nTraining Random Forest...")

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=15,
        min_samples_split=10,
        min_samples_leaf=4,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    return model

#---------------------------------------------------------------
# TRAINING XGBOOST
#--------------------------------------------------------------
def train_gradient_boosting(X_train, y_train):
    print("\nTraining Gradient Boosting...")

    model = GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def train_extra_trees(X_train, y_train):
    print("\nTraining Extra Trees...")

    model = ExtraTreesRegressor(
        n_estimators=300,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    return model

def train_xgboost(X_train ,y_train ):
   model =  XGBRegressor(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
    )
   
   model.fit(X_train, y_train)
   return model


def main():

    df = load_data()

    if df is None:
        return

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = \
        train_test_split_data(X, y)

    # Linear Regression
    lr_model = train_linear_regression(
        X_train,
        y_train
    )

    lr_predictions = make_predictions(
        lr_model,
        X_test
    )

    print("\nLinear Regression Results")

    evaluate_model(y_test, lr_predictions)

    # Random Forest
    rf_model = train_random_forest(
        X_train,
        y_train
    )

    rf_predictions = make_predictions(
        rf_model,
        X_test
    )

    print("\nRandom Forest Results")

    evaluate_model(y_test, rf_predictions)

    #Gradient Boosing Regressor
    gb_model = train_gradient_boosting(
        X_train,
        y_train
    )

    gb_predictions = make_predictions(
        gb_model,
        X_test
    )

    print("\nGradient Boosing Regressor")

    evaluate_model(y_test, gb_predictions)


    #Gradient Boosing Regressor
    et_model = train_extra_trees(
        X_train,
        y_train
    )

    et_predictions = make_predictions(
        et_model,
        X_test
    )

    print("\nExtra Trees Regressor")

    evaluate_model(y_test, et_predictions)


      #Gradient Boosing Regressor
    xgb_model = train_xgboost(
        X_train,
        y_train
    )

    xgb_predictions = make_predictions(
        xgb_model,
        X_test
    )

    print("\nXGBoost Regressor")

    evaluate_model(y_test, xgb_predictions)


    


#-------------------------------------------------------
# ENTRY POINT 
#------------------------------------------------------A
if __name__ == '__main__':
    main()


    
