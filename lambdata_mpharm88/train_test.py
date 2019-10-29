"""
This is a function for taking a df and splitting into 8 dataframes including:
    X_train,
    y_train,
    X_val,
    y_val,
    X_test,
    y_test,
    X_test_CV,
    y_test_CV

THIS FUNCTION DOES NOT DO TIME SERIES SPLITS
"""
import pandas as pd 
from sklearn.model_selection import train_test_split


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
     feat = Your features being used passed in as a list or a var pointing to a 
     list           
 
This function will also display a labled list of the shape of each new
dataframe that was created (8 dataframes in total) for quick fact checking
capabilities
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
