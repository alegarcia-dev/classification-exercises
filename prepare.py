####################
#
#   prepare.py
#   ----------
#   
#   Description:
#       Provides functions for preparing and splitting raw datasets for 
#       exploratory analysis.
#
#   Fields:
#       None
#
#   Functions:
#       prep_iris_data(df)
#       prep_titanic_data(df)
#       prep_telco_data(df)
#       split_data(df, stratify, random_seed = 24)
#
####################

import pandas as pd

##########


def prep_iris_data(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the iris dataset and performs transformations to prepare the data 
        for exploratory analysis.

        Parameters
        ----------
        df : DataFrame
            The expected argument is a Pandas DataFrame containing the iris
            dataset.

        Returns
        -------
        DataFrame : A Pandas DataFrame containing the iris dataset with transformations.
            The resultant dataframe has the species_id and measurement_id columns
            removed, the species_name column renamed to species, and an encoded variable
            for the categorical column species.
    '''

    df = df.drop_duplicates()

    df = df.drop(columns = ['species_id', 'measurement_id'])
    df = df.rename(columns = {'species_name' : 'species'})

    dummy_df = pd.get_dummies(df[['species']], dummy_na = False, drop_first = ['True'])
    df = pd.concat([df, dummy_df], axis = 1)

    return df

def prep_titanic_data(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the titanic dataset and performs transformations to prepare the data
        for exploratory analysis.

        Parameters
        ----------
        df : DataFrame
            The expected argument is a Pandas DataFrame containing the titanic
            dataset.

        Returns
        -------
        DataFrame : A Pandas DataFrame containing the titanic dataset with transformations.
            The resultant dataframe has the deck, embarked, class, and age columns removed,
            null values in the embark_town column filled with the value 'Southampton', and
            encoded variables for the categorical columns sex and embark_town.
    '''

    df = df.drop_duplicates()

    cols_to_drop = ['deck', 'embarked', 'class', 'age']
    df = df.drop(columns=cols_to_drop)

    df['embark_town'] = df.embark_town.fillna(value='Southampton')

    dummy_df = pd.get_dummies(df[['sex','embark_town']], dummy_na=False, drop_first=[True, True])
    df = pd.concat([df, dummy_df], axis=1)

    return df

def prep_telco_data(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
        Accepts the telco dataset and performs transformations to prepare the data
        for exploratory analysis.

        Parameters
        ----------
        df : DataFrame
            The expected argument is a Pandas DataFrame containing the telco
            dataset.

        Returns
        -------
        DataFrame : A Pandas DataFrame containing the telco dataset with transformations.
            The resultant dataframe has the customer_id, contract_type_id, 
            internet_service_type_id, and payment_type_id columns removed, and encoded
            variables for all categorical columns (all non-numeric columns except customer_id
            and total_charges). Rows with customers of 0 tenure are also removed.
    '''

    df = df.drop_duplicates()

    cols_to_drop = [
        'customer_id',
        'contract_type_id',
        'internet_service_type_id',
        'payment_type_id'
    ]
    df = df.drop(columns = cols_to_drop)

    telco.total_charges = telco.total_charges.str.strip()
    telco = telco[telco.total_charges != '']

    categorical_cols = df.dtypes[df.dtypes == 'object'].index
    categorical_cols = categorical_cols.drop(labels = ['customer_id', 'total_charges'])

    dummy_df = pd.get_dummies(df[categorical_cols], dummy_na = False, drop_first = True)
    df = pd.concat([df, dummy_df], axis = 1)

    return df

def split_data(df: pd.core.frame.DataFrame, stratify: str, random_seed: int = 24) -> tuple[
    pd.core.frame.DataFrame,
    pd.core.frame.DataFrame,
    pd.core.frame.DataFrame
]:
    '''
        Accepts a DataFrame and returns train, validate, and test DataFrames.
        Splits are performed randomly.

        Proportion of original dataframe that each return dataframe comprises.
        ---------------
        Train:      56% (70% of 80%)
        Validate:   24% (30% of 80%)
        Test:       20%

        Parameters
        ----------
        df : DataFrame
            A Pandas DataFrame containing prepared data. It is expected that
            the input to this function will already have been prepared and
            tidied so that it will be ready for exploratory analysis.

        stratify : str
            A string value containing the name of the column to be stratified
            in the sklearn train_test_split function. This parameter should
            be the name of a column in the df dataframe.

        random_seed : int, default 24
            An integer value to be used as the random number seed. This parameter
            is passed to the random_state argument in the sklearn train_test_split
            function.

        Returns
        -------
        tuple : A tuple containing three Pandas DataFrames for train, validate
            and test datasets.    
    '''
    train_test_split = 0.2
    train_validate_split = 0.3

    train_validate, test = train_test_split(
        df,
        test_size = train_test_split,
        random_state = random_seed,
        stratify = df[stratify]
    )
    train, validate = train_test_split(
        train_validate,
        test_size = train_validate_split,
        random_state = random_seed,
        stratify = train_validate[stratify]
    )
    return train, validate, test