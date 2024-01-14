d = {"shaswata": 98369, "ayusha":98310, "mayukh":12345, "sourin":54321}
print(d)
print(d["ayusha"])
d["sam"] = 11111
print(d)

# for key in d:
#     print("key:", key, "value:", d[key])

for k,v in d.items():
    print("key:", k, "value:", v)