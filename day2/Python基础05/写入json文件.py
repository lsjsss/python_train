import json
a = {"name":"zouwuqi","age":20,"weight":150,"height":180}
with open("zwq.json","w",encoding="utf-8") as f:
    f.write(json.dumps(a,indent=2,sort_keys=False))

with open("zwq.txt","a",encoding="utf-8") as f:
    f.write("hello")