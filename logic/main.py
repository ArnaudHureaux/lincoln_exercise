from aggregate.drugs_json_extraction import drugs_json_extraction
from clean.clinical_trials_clean import clinical_trials_clean
from clean.drugs_clean import drugs_clean
from clean.pubmed_clean import pubmed_clean
from utils import importFileLocalJson
import os

print(os.path.abspath(os.curdir))
drugs_clean()
pubmed_clean()
clinical_trials_clean()

drugs_json_extraction()
final_result = importFileLocalJson('aggregate/drugs_journal_link_graph.json')
print('[END] The entire pipeline has been executed and the final result has been saved in data/aggregate/drugs_journal_link_graph.json')
first_element = list(final_result['data'].keys())[0]
first_data = final_result['data'][first_element]
print('[END] Below an extract of the Json file for the', first_element, ':')
print(first_data)
