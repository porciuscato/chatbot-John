import os

# print(os.listdir())
# os.rename('dog.py', 'hello.py')
# print(os.listdir())
os.chdir('report')

# 100번 반복하여 파일을 생성
# for i in range(100, 200):
#     os.system('touch report{}.txt'.format(i))

files = os.listdir()
print(files)

for name in files:
    os.rename(name, name.replace('samsung_', 'ssafy_'))

