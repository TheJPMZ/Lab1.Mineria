import pandas as pd


def codify_bind(original_dataframe: pd.DataFrame, variables: list) -> pd.DataFrame:
    
    for variable in variables:
        dummies = pd.get_dummies(original_dataframe[[variable]])
        new_dataframe = pd.concat([original_dataframe, dummies], axis=1)
        new_dataframe = new_dataframe.drop([variable], axis=1)
        original_dataframe = new_dataframe
    
    return original_dataframe



    
