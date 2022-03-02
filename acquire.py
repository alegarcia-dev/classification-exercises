####################
#
#   acquire.py
#   ----------
#   
#   Description:
#       Provides functions for acquiring and cacheing commonly used
#       datasets.
#
#   Fields:
#       _titanic_file
#       _titanic_db
#       _iris_file
#       _iris_db
#       _telco_file
#       _telco_db
#
#   Functions:
#       _get_titanic_sql()
#       get_titanic_data(use_cache = True)
#       _get_iris_sql()
#       get_iris_data(use_cache = True)
#       _get_telco_sql()
#       get_telco_data(use_cache = True)
#
####################

import pandas as pd
import os

from env import get_db_url


# File names and database names for each dataset acquired through the 
# following functions.

_titanic_file = 'titanic.csv'
_titanic_db = 'titanic_db'

_iris_file = 'iris.csv'
_iris_db = 'iris_db'

_telco_file = 'telco.csv'
_telco_db = 'telco_churn'

##########

def _get_titanic_sql() -> str:
    '''
    Returns the SQL code required to retrieve the titanic dataset
    from the MySQL database.
    '''

    return '''
        SELECT * FROM passengers;
    '''

def get_titanic_data(use_cache: bool = True) -> pd.core.frame.DataFrame:
    '''
    Return a dataframe containing data from the titanic dataset.

    If a titanic.csv file containing the data does not already
    exist the data will be cached in that file inside the current
    working directory. Otherwise, the data will be read from the
    .csv file.

    Parameters
    ----------
    use_cache : bool, default True
        If True the dataset will be retrieved from a csv file if one
        exists, otherwise, it will be retrieved from the MySQL database. 
        If False the dataset will be retrieved from the MySQL database
        even if the csv file exists.

    Returns
    -------
    DataFrame : A Pandas DataFrame containing the data from the titanic
        dataset is returned.
    '''

    if os.path.exists(_titanic_file) and use_cache:
        return pd.read_csv(_titanic_file)
    else:
        df = pd.read_sql(_get_titanic_sql(), get_db_url(_titanic_db))
        df.to_csv(_titanic_file, index = False)
        return df

def _get_iris_sql() -> str:
    '''
    Returns the SQL code required to retrieve the iris dataset
    from the MySQL database.
    '''

    return '''
        SELECT *
        FROM measurements
        JOIN species USING (species_id);
    '''

def get_iris_data(use_cache: bool = True) -> pd.core.frame.DataFrame:
    '''
    Return a dataframe containing data from the iris dataset.

    If a iris.csv file containing the data does not already
    exist the data will be cached in that file inside the current
    working directory. Otherwise, the data will be read from the
    .csv file.

    Parameters
    ----------
    use_cache: bool, default True
        If True the dataset will be retrieved from a csv file if one
        exists, otherwise, it will be retrieved from the MySQL database. 
        If False the dataset will be retrieved from the MySQL database
        even if the csv file exists.

    Returns
    -------
    DataFrame : A Pandas DataFrame containing the data from the iris
        dataset is returned.
    '''

    if os.path.exists(_iris_file) and use_cache:
        return pd.read_csv(_iris_file)
    else:
        df = pd.read_sql(_get_iris_sql(), get_db_url_(iris_db))
        df.to_csv(_iris_file, index = False)
        return df

def _get_telco_sql() -> str:
    '''
    Returns the SQL code required to retrieve the telco dataset
    from the MySQL database.
    '''

    return '''
        SELECT *
        FROM customers
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN contract_types USING (contract_type_id);
    '''

def get_telco_data(use_cache: bool = True) -> pd.core.frame.DataFrame:
    '''
    Return a dataframe containing data from the telco dataset.

    If a telco.csv file containing the data does not already
    exist the data will be cached in that file inside the current
    working directory. Otherwise, the data will be read from the
    .csv file.

    Parameters
    ----------
    use_cache: bool, default True
        If True the dataset will be retrieved from a csv file if one
        exists, otherwise, it will be retrieved from the MySQL database. 
        If False the dataset will be retrieved from the MySQL database
        even if the csv file exists.

    Returns
    -------
    DataFrame : A Pandas DataFrame containing the data from the telco
        dataset is returned.
    '''

    if os.path.exists(_telco_file) and use_cache:
        return pd.read_csv(_telco_file)
    else:
        df = pd.read_sql(_get_telco_sql(), get_db_url(_telco_db))
        df.to_csv(_telco_file, index = False)
        return df