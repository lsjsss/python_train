import json
with open("zwq.json","r",encoding="utf-8") as f:
    data1 = json.loads(f.read())
    f.seek(0)
    data2 = json.load(f)
print(data1)
print(data2)