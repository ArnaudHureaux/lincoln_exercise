import pandas as pd
import os
import json

from utils import importFileLocal, exportFileLocalJson


def test_drugs_json_extraction_transform(drug, dicte):
    try:
        assert len(dicte.keys()) == len(drug)
        assert list(dicte[list(dicte.keys())[0]].keys()) == [
            'pubmed', 'clinical_trial']
        assert len(dicte[list(dicte.keys())[0]]['pubmed'][0]) == 3
        print('[INFO] Checks of the function drugs_json_extraction succeed')
    except:
        print('[INFO] Checks of the function drugs_json_extraction failed')


def drugs_json_extraction_transform(drug, pubmed, clin):
    drugs = drug['drug'].unique()
    sources = ['pubmed', 'clinical_trial']
    sources_df = {sources[0]: pubmed, sources[1]: clin}
    dicte = {}
    for drug in drugs:
        dicte[drug] = {}
        for source in sources:
            dicte[drug][source] = {}
            df = sources_df[source]
            df['drug_in_title'] = df['title'].apply(
                lambda x: drug.upper() in x.upper())
            df_filter = df[df['drug_in_title']][['title', 'date', 'journal']]
            list_for_dicte = df_filter.values.tolist()
            for k in range(len(list_for_dicte)):
                dicte[drug][source][k] = list_for_dicte[k]
    return dicte


def drugs_json_extraction():
    # IMPORT
    drug = importFileLocal('clean/drugs_clean.csv')
    pubmed = importFileLocal('clean/pubmed_clean.csv')
    clin = importFileLocal('clean/clinical_trials_clean.csv')
    # TRANSFORM
    dicte = drugs_json_extraction_transform(drug, pubmed, clin)
    # CHECK
    test_drugs_json_extraction_transform(drug, dicte)
    # EXPORT
    exportFileLocalJson(dicte, 'aggregate/drugs_journal_link_graph.json')
    print('[INFO] End of the function drugs_json_extraction')
