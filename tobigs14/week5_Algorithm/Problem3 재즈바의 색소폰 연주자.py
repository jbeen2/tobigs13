note = {
    'c' : [0,1,1,1,0,0,1,1,1,1],
    'd' : [0,1,1,1,0,0,1,1,1,0],
    'e' : [0,1,1,1,0,0,1,1,0,0],
    'f' : [0,1,1,1,0,0,1,0,0,0],
    'g' : [0,1,1,1,0,0,0,0,0,0],
    'a' : [0,1,1,0,0,0,0,0,0,0],
    'b' : [0,1,0,0,0,0,0,0,0,0],
    'C' : [0,0,1,0,0,0,0,0,0,0],
    'D' : [1,1,1,1,0,0,1,1,1,0],
    'E' : [1,1,1,1,0,0,1,1,0,0],
    'F' : [1,1,1,1,0,0,1,0,0,0],
    'G' : [1,1,1,1,0,0,0,0,0,0],
    'A' : [1,1,1,0,0,0,0,0,0,0],
    'B' : [1,1,0,0,0,0,0,0,0,0]
}

finger = [s for s in str(input())]

def solve(finger, note) :
    num = []
    num.extend(note[finger[0]])

    # 여기서 바로 num = note[finger[0]] 해버리면 note[C]값이 바뀜..황당
    # 복사된 지역변수인 note를 계속 참조하고, 이거로 선언해 버리기 때문에 값이 바뀌어버리는 느낌 ......

    check = note[finger[0]]

    for i in range(1, len(finger)) :
        for j in range(10) :
            if check[j] == 0 and note[finger[i]][j] == 1 :
                num[j] += 1
        check = note[finger[i]]

    return num


print(' '.join([str(n) for n in solve(finger, note)]))
