names = {
    '강동주': '외판원',
    '정의진': '주조원'
}

nums = [1, 2, 3, 4]

# print('김민지' in names)
# print(5 in nums)

# names['양찬우'] = '프로그래머'
# print(type(names.keys()))

# babo = '정의진'
# you = '설현'

babos = {
    '강동주' : {
        '김지수': 55,
        '아이유' : 100
    },
    '정의진' : {
        '설현': 75
    }
}

# key, value를 같이 순회하는 방법
for k, v in babos.items():
    print(k, v)

# key만 뽑는 방법
print(list(babos.keys()))

# values만 뽑는 방법
print(list(babos.values()))
