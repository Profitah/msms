Dic = []
dic = {}
while True :
    key = int(input('키 입력 : '))
    val = input('밸류 입력 : ')
    dic[key] = val
    if key == 0:
        Dic.append(dic)
        print("그만", Dic)
        break