from utils import importFileLocalJson
final_result = importFileLocalJson('aggregate/drugs_journal_link_graph.json')
def getTheJournalWithTheHighestDifferentDrugs():
    journals={}
    for med in list(final_result['data'].keys()):
        allready_mentioned=[]
        for _type in ['pubmed','clinical_trial']:
            dicte1=final_result['data'][med][_type]
            for k in range(len(dicte1.keys())):
                values_3=list(dicte1.values())[k]
                if values_3[2] not in allready_mentioned:
                    try:
                        journals[values_3[2]]=journals[values_3[2]]+1
                        allready_mentioned.append(values_3[2])
                    except:
                        journals[values_3[2]]=1
                        allready_mentioned.append(values_3[2])
    print(journals)
