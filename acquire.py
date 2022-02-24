import pandas as pd
import os

from env import get_db_url


# File names and database names for each dataset acquired through the 
# following functions.

titanic_file = 'titanic.csv'
titanic_db = 'titanic_db'

iris_file = 'iris.csv'
iris_db = 'iris_db'

telco_file = 'telco.csv'
telco_db = 'telco_churn'



def _get_titanic_sql() -> str:
    return '''
        SELECT * FROM passengers;
    '''

def get_titanic_data() -> pd.core.frame.DataFrame:
    '''
    Return a dataframe containing data from the titanic dataset.

    If a titanic.csv file containing the data does not already
    exist the data will be cached in that file inside the current
    working directory. Otherwise, the data will be read from the
    .csv file.
    '''

    if os.path.exists(titanic_file):
        return pd.read_csv(titanic_file)
    else:
        df = pd.read_sql(_get_titanic_sql(), get_db_url(titanic_db))
        df.to_csv(titanic_file)
        return df

def _get_iris_sql() -> str:
    return '''
        SELECT *
        FROM measurements
        JOIN species USING (species_id);
    '''

def get_iris_data() -> pd.core.frame.DataFrame:
    '''
    Return a dataframe containing data from the iris dataset.

    If a iris.csv file containing the data does not already
    exist the data will be cached in that file inside the current
    working directory. Otherwise, the data will be read from the
    .csv file.
    '''

    if os.path.exists(iris_file):
        return pd.read_csv(iris_file)
    else:
        df = pd.read_sql(_get_iris_sql(), get_db_url(iris_db))
        df.to_csv(iris_file)
        return df

def _get_telco_sql() -> str:
    return '''
        SELECT *
        FROM customers
        JOIN payment_types USING (payment_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN contract_types USING (contract_type_id);
    '''

def get_telco_data() -> pd.core.frame.DataFrame:
    '''
    Return a dataframe containing data from the telco dataset.

    If a telco.csv file containing the data does not already
    exist the data will be cached in that file inside the current
    working directory. Otherwise, the data will be read from the
    .csv file.
    '''

    if os.path.exists(telco_file):
        return pd.read_csv(telco_file)
    else:
        df = pd.read_sql(_get_telco_sql(), get_db_url(telco_db))
        df.to_csv(telco_file)
        return df