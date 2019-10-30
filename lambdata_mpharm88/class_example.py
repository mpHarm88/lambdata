import numpy as np
import pandas as pd
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score


class Baseline:
    "creating minimum standards"
    def __init__(self, data, target, feat, col):
        pass

    def train_test(df, target, feat):
        """
        THIS FUNCTION DOES NOT DO TIME SERIES SPLITS
  
        This is a function to split your dataframe into you training, validation, test,
        and cross validations dataframes. This function returns 8 values
        so have 8 var names ready to capture all values outputted by the funcntion.
  
        Example (Using Titanic data set as example filler target/features):
        X_train, y_train, X_val, y_val, X_test, y_test, X_test_CV, y_test_CV =
        train_test(df, "survived", ["age", "fare", "class"])
  
        This inputs of the function are as follows:
        df = the dataframe to be split (cleaned or dirty)
        target = Your target (y)
        feat = Your features being used passed in as a list or a object pointing to a 
        list          
  
        This function will also display a labled list of the shape of each new
        dataframe that was created (8 dataframes in total) for quick fact checking
        """
        df = pd.DataFrame(data=df)
        df = df.copy()
        training, testing = train_test_split(df, random_state=42)
        train, val = train_test_split(training, random_state=42)
  
        y = target
        features = feat
  
        X_train = train[features]
        y_train = train[target]
  
        X_val = val[features]
        y_val = val[target]
  
        X_test = testing[features]
        y_test = testing[target]
  
        X_test_CV = df[features]
        y_test_CV = df[target]
        print(f"Original Data Frame Shape: {df.shape}")
        print()
        print(f"Target: {y}")
        print(f"Features: {features}")
        print()
        print(f"X Training Shape: {X_train.shape}")
        print(f"y Training Shape: {y_train.shape}")
        print()
        print(f"X Validation Shape: {X_val.shape}")
        print(f"y Validation Shape: {y_val.shape}")
        print()
        print(f"X Testing Shape: {X_test.shape}")
        print(f"y Testing Shape: {y_test.shape}")
        print()
        print(f"X Cross Validation Testing Shape: {X_test_CV.shape}")
        print(f"y Cross Validation Testing Shape: {y_test_CV.shape}")
        return (X_train,
                y_train,
                X_val,
                y_val,
                X_test,
                y_test,
                X_test_CV,
                y_test_CV)
    
    def date(df, col):
        """
        This is a function for turning a date column that includes month, day, and year
        into 5 separate columns that includes: Pandas date time, year, month, day, season.
        Seasons identified as: {3,4,5:spring, 6,7,8:summer, 9,10,11:autumn, 12,1,2:winter} 
        """
        df = df.copy()
        season = {1: 'winter',
                  2: 'winter',
                  3: 'spring',
                  4: 'spring',
                  5: 'spring',
                  6: 'summer',
                  7: 'summer',
                  8: 'summer',
                  9: 'autumn',
                  10: 'autumn',
                  11: 'autumn',
                  12: 'winter'}
        df = pd.DataFrame(data=df)
        df['pd_date_time'] = pd.to_datetime(df[col])
        df['day'] = df['pd_date_time'].dt.day
        df['month'] = df['pd_date_time'].dt.month
        df['year'] = df['pd_date_time'].dt.year
        df['season'] = df['month'].map(season)
        return df

    def xgb_reg(X_train, y_train, X_test, y_test):
        """
        Simple pipeline Baseline model for using XGB Regressor including a 
        ordinal encoder, standard scaler, simple imputer. This function returns 
        Mean baseline, R^2, and RMSE. If R^2 is negative this means mean 
        baseline is a more effective model
        """
        s1 = pd.Series(y_train)
        s2 = pd.Series(y_test)
        s3 = s1.append(s2)
        mean = np.mean(s3)

        model = make_pipeline(
             OrdinalEncoder(),
             StandardScaler(),
             SimpleImputer(strategy='median'),
             XGBRegressor(
                 n_estimators=100,
                 n_jobs=-1,
                 max_depth=10
             )
        )

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        print(f'Mean baseline of target = {mean}')
        print(f'Gradient Boosting R^2 = {r2}')
        print(f'Gradient Boosting RMSE = {rmse}') 
        return

    def xgb_class(X_train, y_train, X_test, y_test):
        """
        Baseline XGB Classifier that prints out ROC score for Train and Test 
        sets provided.
        """
        class_index = 1
        processor = make_pipeline(
            OrdinalEncoder(),
            SimpleImputer(strategy='median')
        )

        X_train_processed = processor.fit_transform(X_train)
        X_test_processed = processor.transform(X_test)

        eval_set = [(X_train_processed, y_train),
                    (X_test_processed, y_test)]
  
        model = XGBClassifier(
                n_estimators=100,
                n_jobs=-1,
                max_depth=10
            )
        
        model.fit(X_train_processed, y_train, eval_metric='auc')

        # Getting the predicted probabilities 
        y_pred = model.predict(X_test_processed)
        y_pred_proba_train = model.predict_proba(X_train_processed)[:, class_index]
        y_pred_proba_test = model.predict_proba(X_test_processed)[:, class_index]

        train_roc = roc_auc_score(y_train, y_pred_proba_train)
        test_roc = roc_auc_score(y_test, y_pred_proba_test)
        
        # Making a new Series for mean baseline print
        s1 = pd.Series(y_train)
        s2 = pd.Series(y_test)
        s3 = s1.append(s2)

        print('Mean Baseline of Target')
        print(s3.value_counts(normalize=True))
        print()
        print(f'Train ROC AUC for class: {train_roc} \n')
        print(f'Test ROC AUC for class: {test_roc}')

        return

