def searchPrefix(a):
    prefix = ""
    count = 0
    while count < len(a):
        count2 = 0
        while count2 < len(a[count]):
            print(f"count: {count}")
            print(f"count2: {count2}")
            if a[count][count2] == a[count+1][count2]:
                prefix += a[count][count2]
                print(prefix)
            else:
                break
            count2 += 1
        count += 1
    return prefix

def searchPrefix2(a):
    prefix = ""
    min = 0
    count = 0
    subindex = 0
    for i in a:
        lenn = len(i)
        if min == 0:
            min = lenn
        if min != 0 and lenn < min:
            min = lenn
    while count < len(a):
        count2 = 0
        while count2 < len(a[count]) and count < min:
            chast_prefixa = False
            print(f"count: {count}")
            print(f"count2: {count2}")
            if a[count][count2] == a[count+1][count2]:
                prefix += a[count][count2]
                print(prefix)
            else:
                count2 += 1
                break
            count2 += 1
        count += 1
    print(min)
    return prefix


def searchMin(a):
    min = 0
    for i in a:
        lenn = len(i)
        if min == 0:
            min = lenn
        if min != 0 and lenn < min:
            min = lenn
    return min

def searchPrefix4(step, a, min):
    lenn = len(a) #посчитаем заранее, так как будем использовать неоднократно (типо микро-оптимизация :D)
    count = 0
    tmp = a[0][step]
    prefix = ''
    while count <= lenn-1 and step <= min:
        if tmp == a[count][step]:
            #print(a[count][step])
            success = True
            if count == lenn-1:
                prefix += tmp
                step += 1
                break
        count += 1
    return prefix

a = ["Ваня", "Вася", "Вальгххалла", "Ваза"]
min = searchMin(a)
step = 0
prefix = ''
while step < min:
    prefix += searchPrefix4(step, a, min)
    step += 1
print(prefix)
