def sorting(list):
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    print(list)
    return list


def swap(a,b):
    print(a)
    print(b)
    temp = a
    a = b
    b = temp
    print(a)
    print(b)


def reverseNumber(num):
    strNum = str(num)
    outNum = ""
    for i in range(len(strNum)-1, -1, -1):
        outNum = outNum + (strNum[i])
    print(outNum)


sorting([2,5,1,7,8,3,0,3,10,4])
swap(3,4)
reverseNumber(111333444)