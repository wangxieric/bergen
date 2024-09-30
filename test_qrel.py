import json
from utils import get_qrel_ranking_filename
qrels_folder = 'qrels'
query_dataset_name = 'kilt_nq'
split = 'dev'
debug = False
qrels_file = get_qrel_ranking_filename(qrels_folder, query_dataset_name, split, debug)
qrel = json.load(open(qrels_file))
doc_dataset_name = "kilt-100w"

if "doc_dataset_name" in qrel:
    qrel.pop("doc_dataset_name")

doc_ids = list(qrel.keys())
print(qrel[doc_ids[0]])
for doc_id in doc_ids:
    if qrel[doc_id].values == 0:
        print(doc_id)