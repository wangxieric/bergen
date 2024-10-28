import json

qrels = dict()

with open('qrel.kilt_triviaqa.dev.txt') as f:
    for line in f:
        qid, _, doc_id, rel = line.strip().split()
        if qid not in qrels:
            qrels[qid] = dict()
        else:
            print(qid)
        qrels[qid][doc_id] = int(rel)

# check if a qid has more than 1 doc_id
for qid, docs in qrels.items():
    if len(docs) > 1:
        print(qid)