list2 = [{'a':1, 'b':2, 'c':{1:2, 2:{'a':5, 'b':7, "c":'harsha'}}}]
print(list2[0]['c'][2]["c"])
x = list2[0]['c'][2]["c"]
print({i:x.count(i) for i in x})