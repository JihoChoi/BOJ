room_num = list(map(int, input()))
num_dict = {i: 0 for i in range(10)}
# num_set = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in room_num:
    if i == 9:
        num_dict[6] += 1
    else:
        num_dict[i] += 1

count = 0
FLAG = True
while FLAG:
    count += 1
    for i in range(10):
        if i == 9:
            num_dict[6] -= 1
        else:
            num_dict[i] -= 1
    
    for key, value in num_dict.items():
        if value > 0:
            FLAG = True
            break;
        FLAG = False

print(count)

# TODO: Without FLAG