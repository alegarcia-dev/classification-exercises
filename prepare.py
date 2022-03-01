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