import pandas as pd
import os

from utils import importFileLocal, exportFileLocal
print('drugclean:', os.path.abspath(os.curdir))


def test_drug_clean_transform(df):
    try:
        assert len(df['pk'].unique()) == len(df)
        assert None not in list(df['drug'])
        print('[INFO] Checks of the function drug_clean succeed')
    except:
        print('[FAIL] Checks of the function drug_clean failed')


def drug_clean_transform(df):
    df = df[df['drug'].notna()]
    df['pk'] = df['drug']
    return df


def drugs_clean():
    # IMPORT
    df = importFileLocal('datasource/drugs.csv')
    # TRANSFORMATION
    df = drug_clean_transform(df)
    # CHECK
    test_drug_clean_transform(df)
    # EXPORT
    exportFileLocal(df, 'clean/drugs_clean.csv')
    print('[INFO] End of the function drugs_clean')
