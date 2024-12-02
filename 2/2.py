
def issafe(list):
    if (sorted(list) != list and sorted(list, reverse = True) != list):
            # print("fail")
            return False

    for i, v in enumerate(list):
        if i == 0:
            mem = v
            continue
        diff = abs(v -mem)
        if diff >= 1 and diff <= 3:
            if i == len(list) -1:
                # print("diff")
                return True
            mem = v
        else:
            return False

with open('in', 'r') as file:
    res1 = 0
    res2 = 0
    for line in file:
        values = list(map(int, line.split()))
        # print (values)      

        if issafe(values):
            res1 += 1
            res2 += 1
        else:
            #pt 2
            for i in range(len(values)):
                damped = values.copy()
                del damped[i]
                if issafe(damped):
                    res2 += 1;
                    break

    print("Sum1: " + str(res1))
    print("Sum2: " + str(res2))


        

# [7 6 4 2 1]
# [1 2 7 8 9] 
# [9 7 6 2 1]
# [1 3 2 4 5] <--
# [8 6 4 4 1]
# [1 3 6 7 9]