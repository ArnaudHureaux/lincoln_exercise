import pandas as pd
from utils import importFileLocal, exportFileLocal, importFileLocalJson


def test_pubmed_clean_transform(df):
    try:
        assert len(df[df.duplicated()]) == 0
        assert len(df['pk'].unique()) == len(df)
        assert list(df.columns) == ['id', 'title', 'date', 'journal', 'pk']
        print('[INFO] Checks of the function pubmed_clean succeed')
    except:
        print('[FAIL] Checks of the function pubmed_clean failed')


def pubmed_clean_transform(df1, dicte):
    df2 = pd.DataFrame(dicte['data'])
    df = pd.concat((df1, df2)).reset_index(drop=True)
    df = df.drop_duplicates()
    df['pk'] = df['title']+'_'+df['journal']
    return df


def pubmed_clean():
    # IMPORT
    df1 = importFileLocal('datasource/pubmed.csv')
    dicte = importFileLocalJson('datasource/pubmed.json')
    # TRANSFORMATION
    df = pubmed_clean_transform(df1, dicte)
    # CHECK
    test_pubmed_clean_transform(df)
    # EXPORT
    exportFileLocal(df, 'clean/pubmed_clean.csv')
    print('[INFO] End of the function pubmed_clean')
