import json,sys
p=sys.argv[1] if len(sys.argv)>1 else "CORE_CASES.json"
d=json.load(open(p))
ids=[c["id"] for c in d["cases"]]
assert len(ids)==len(set(ids))
for c in d["cases"]:
    assert c["requirements"] and all(isinstance(n,int) and 1<=n<=97 for n in c["requirements"])
    assert isinstance(c["expected"],dict) and c["expected"]
for bad in ["done-without-result","unknown-finding-impact","reviewer-is-author","parallel-no-admission","old-gate-satisfaction"]:
    c=next(x for x in d["cases"] if x["id"]==bad)
    assert c["expected"].get("accepted",c["expected"].get("verdict_allowed",c["expected"].get("parallel_allowed",False))) is False
print(f"PASS {len(ids)} independent core cases")
