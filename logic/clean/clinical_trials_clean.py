import pandas as pd
from utils import importFileLocal, exportFileLocal


def test_clinical_trials_clean_transform(df):
    try:
        assert len(df[df.duplicated()]) == 0
        assert len(df['pk'].unique() == len(df))
        assert None not in df['title'].unique()
        assert '' not in df['title'].apply(lambda x: x.replace(' ', ''))
        print('[INFO] Checks of the function clinical_trials_clean succeed')
    except:
        print('[FAIL] Checks of the function clinical_trials_clean failed')


def clinical_trials_clean_transform(df):
    df = df[(df['scientific_title'].notna()) & (
        df['scientific_title'].apply(lambda x: x.replace(' ', '')) != '')]
    df = df[df['journal'].notna()]
    df['journal'] = df['journal'].apply(lambda x: x.replace('\xc3\x28', ''))
    df = df.rename(columns={'scientific_title': 'title'})
    df['pk'] = df['title']+'_'+df['journal']
    return df


def clinical_trials_clean():
    # IMPORT
    df = importFileLocal('datasource/clinical_trials.csv')
    # TRANSFORMATION
    df = clinical_trials_clean_transform(df)
    # CHECK
    test_clinical_trials_clean_transform(df)
    # EXPORT
    exportFileLocal(df, 'clean/clinical_trials_clean.csv')
    print('[INFO] End of the function clinical_trials_clean')
