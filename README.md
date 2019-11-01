<div align="center">
  <img src="https://github.com/mpHarm88/lambdata/blob/master/lambdata.jpg.png"><br>
</div>

---

# lambdata 
A collection of Data Science helper functions. **Currently xgb_class and xgb_reg do not output as intended and are being investigated for potential issues.** 

## Download
https://test.pypi.org/project/lambdata-mpharm88/

## What is it?
lambdatas_mpharm88 is a **Python** package that lets you reach your model baseline as quickly as possible. This means that when you use lambdata_mpharm88 your delivering initial observations **faster** to interested parties. This package also helps you find out how hard it will be to **beat your mean baseline and provides functionality for preprocessing your data frame too.** Lambdata_mpharm88 seeks to deliver quick, meaningful results when time constraints don't allow for a full investigation into the data.

## Main Features
Here is a list of what lambdata_mpharm88 does well:
  
  - Changing a date column into **５ new columns** including:
      - Pandas date time column
      - Year column
      - Month column
      - Day column
      - **Season column**
  - Performing a **train/test split** using your original data frame, target (y), and features. This function will give you 8 
    separate dataframes including:
      - X training set
      - y training set
      - X validation set
      - y validation set
      - X testing set
      - y testing set
      - X cross validation set
      - y cross validation set
      - Shapes of all dataframes outputted
  - A simple **XGBClassifier** including an Ordinal Encoder and Simple Imputer that out puts:
      - Training **ROC/AUC** Score 
      - Testing **ROC/AUC** score
      - Mean baseline of majority class in target column
  - A simple **XGBRegressor** including an Ordinal Encoder and Simple Imputer
      - Training **RMSE**
      - Testing **RMSE**
      - Mean baseline of target column
      
## Dependencies
- [XGBoost](https://xgboost.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/)
- [Numpy](https://www.numpy.org)
- [Category Encoders](https://contrib.scikit-learn.org/categorical-encoding/)
- [Scikit Learn](https://scikit-learn.org/stable/documentation.html)

## License
[MIT License](https://opensource.org/licenses/MIT)

## Documentation
Currently, this read me is the only documentation available. If you would like to join the party and help build this package, feel free to create a pull request with your changes. All feedback is appreciated, and together we can turn lambdata_mpharm88 into a tool that's used by people all over the world.
