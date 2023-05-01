"""
The motivation for creating prediction and ranking tasks for EIE datasets was to extend the dataset ecosystem available for algorithmic fairness research in two directions: the education domain and the dataset from Eastern Europe (Ukraine). We obtained the data from publicly available Open Data resource https://zno.testportal.com.ua/opendata.

The tasks were created by Dr. Julia Stoyanovich and Andrew Bell from the Center for Responsible AI, New York University, and Tetiana Zakharchenko, Nazarii Drushchak, Oleksandra Konopatska, and Olha Liuba from Ukrainian Catholic University.

The creation of the dataset was funded by the Center for Responsible AI, New York University.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset

def load_datasets(years):
    """
    We will load and work with datasets from 2018 to 2021 since they have a comparable structure.
    We downloaded original datasets from Open Data Resource and uploaded to HuggingFace for easiness of usage.
    """
    base_file_nams = "OpenData{year}.csv"
    dataset_id = "DSRL/zno"

    # load datasets
    datasets = []
    for year in years:
        print(f"ZNO {year} Loading...")
        hf_dataset = load_dataset(dataset_id, data_files=base_file_nams.format(year=year),keep_default_na=False, use_auth_token=True)
        datasets.append(pd.DataFrame(hf_dataset['train']))

    return datasets


def finalize_datasets(datasets, years):
    """
    Names of all features are the same across all years,
    but can have some difference with capital and lower cases.
    That's why we lower all of them. Also, we add a new column – a corresponding year.
    Finally, we can concatenate all datasets and save and return the result.
    """
    for year, dataset in zip(years, datasets):
        dataset.columns = [col.lower() for col in dataset.columns]
        dataset['year'] = year

    df_all = pd.concat(datasets)
    df_all.to_csv('zno_all.csv',index=False)
    return df_all


def encode_tertypename(x):
    if x['tername'].startswith('м.'):
        return 'місто'
    elif x['tername'].startswith('смт'):
        return 'селище міського типу'
    elif x['tername'].startswith('с.'):
        return 'селище, село'
    elif x['tername'].startswith('с-ще'):
         return 'селище, село'
    elif x['areaname'].startswith('м.'):
        return 'місто'
    return None

def encode_regtypename(x):
    regtypename_dict = {
    'Випускник української школи поточного року': ['Випускник загальноосвітнього навчального закладу 2016 року','Випускник загальноосвітнього навчального закладу 2017 року',
                         'Випускник загальноосвітнього навчального закладу 2021 року', 'Випускник закладу загальної середньої освіти 2018 року',
                         'Випускник закладу загальної середньої освіти 2019 року', 'випускник закладу загальної середньої освіти 2020 року'],
    'Випускник іноземної школи': ['Випускник, який здобуде в 2016 році повну загальну середню освіту в навчальному закладі іншої держави', 'Випускник, який здобуде в 2017 році повну загальну середню освіту в навчальному закладі іншої держави',
                                  'Випускник, який здобуде в 2018 році повну загальну середню освіту в навчальному закладі іншої держави', 'Випускник, який здобуде в 2019 році повну загальну середню освіту в закордонному закладі освіти',
                                  'Випускник, який здобуде в 2020 році повну загальну середню освіту в закордонному закладі освіти', 'Випускник, який здобуде в 2021 році повну загальну середню освіту в навчальному закладі іншої держави'],
    'Випускник коледжу': ['Учень (слухач) закладу професійної (професійно-технічної) освіти', 'Учень (слухач, студент) професійно-технічного, вищого навчального закладу'],
    'Студент закладу вищої освіти': ['Студент закладу вищої освіти'],
    'Випускник минулих років': ['Випускник минулих років']
    }
    for type, possible_types in regtypename_dict.items():
        if x in possible_types:
            return type
    return None


def unify_features(df_all):
    """
    Since in 2021 'tertypename' has 3 territory types: city (місто), town (селище міського типу) and village (селище, село),
    and before we had only 2: city (місто) and village (селище, село), we reconstruct the correct type for 2018-2020 period.

    Also we remove year-specific information from regtypename.
    """
    df_all['tertypename'] = df_all.apply(encode_tertypename,axis=1)
    df_all.regtypename = df_all.regtypename.map(encode_regtypename)
    return df_all

def drop_experiental_tests(df_all):
    """
    Drop Math Standard test and UkrsubTest.
    It was new experiment in 2021, that failed since due to COVID, it was cancelled.
    """
    df_all = df_all.drop(columns=['mathsttest', 'mathstlang', 'mathstteststatus', 'mathstball12', 
                              'mathstball','mathstptname','mathstptregname', 'mathstptareaname', 'mathstpttername', 'mathdpalevel'])
    df_all = df_all.drop(columns=['ukrsubtest'])
    return df_all


def prep_ukr_uml(x, name):
    if x['year']<2021:
        return x[name]
    return x[name.replace('ukr','uml')]

def change_uml_2021(df_all):
    """
    In 2021 Ukrtest was renamed to UMLtest
    """
    for name in [col for col in df_all.columns if col.startswith('ukr')]:
        df_all[name] = df_all.apply(prep_ukr_uml,axis=1,args=[name])
    df_all = df_all.drop(columns=[col for col in df_all.columns if col.startswith('uml')])
    return df_all


def drop_ball12_ball100(df_all):
    """
    They are ranking scores for different scales.
    """
    df_all = df_all.drop(columns=[col for col in df_all.columns if '12' in col or '100' in col])
    return df_all

def create_dataset():
    years = [2018,2019,2020,2021]
    datasets = load_datasets(years)
    df_all = finalize_datasets(datasets, years)
    df_all = unify_features(df_all)
    df_all = drop_experiental_tests(df_all)
    df_all = change_uml_2021(df_all)
    df_all = drop_ball12_ball100(df_all)
    df_all.to_csv('zno_preprocessed.csv', index=False)

if __name__ == "__main__":
    create_dataset()
