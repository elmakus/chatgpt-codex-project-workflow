import json,sys
p=sys.argv[1] if len(sys.argv)>1 else "HOST_RECOVERY_CASES.json"
d=json.load(open(p)); cs=d["cases"]; ids=[c["id"] for c in cs]
assert len(ids)==len(set(ids))
assert {c["input"]["direction"] for c in cs if c["id"].startswith("handoff-")}=={"chatgpt->pi","pi->chatgpt","chatgpt->chatgpt","pi->pi"}
for c in cs:
 assert c["req"] and all(isinstance(n,int) and 1<=n<=97 for n in c["req"])
 assert c["expected"]
for x in ["mutant-trust-latest","mutant-wrong-provenance","mutant-local-only","mutant-duplicate-slot","mutant-clean-merge-semantic-mismatch"]:
 assert next(c for c in cs if c["id"]==x)["expected"]["accepted"] is False
assert next(c for c in cs if c["id"]=="mutant-archive-parent")["expected"]["all_closed"] is False
for x in ["legacy-v1","legacy-v20","legacy-v21"]:
 e=next(c for c in cs if c["id"]==x)["expected"]; assert e["accepted"] is False and e["bytes_unchanged"] and e["writes"]==0
assert {c["input"]["family"] for c in cs if c["kind"]=="r6"}=={"P0","P1","P2","P3","P4","P5","P6"}
print(f"PASS {len(cs)} host/recovery scenarios")
