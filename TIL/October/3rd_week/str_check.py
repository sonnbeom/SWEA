req = input()

temp_list = ['' for _ in range(9)]
for i in range(9):
    temp_list[i] = req[i]
req_v2 = list(req)
print(req_v2)
print(temp_list)
print(len(temp_list))
print(type(req))
print(req)
req = req.split()
print(type(req))
print(req)