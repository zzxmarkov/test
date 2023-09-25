# 2021-04-24  16:25
"""import os

#print(os.getcwd())
#os.system('notepad.exe')
#print(os.listdir('..\\chap14'))
#os.mkdir('22')
#os.makedirs('A/B/C')
os.chdir('..\\chap13')
print(os.getcwd())"""


"""import os.path as a
print(a.abspath('OS模块'))
print(a.exists('C:\\Users\\小角色\\Desktop\\python练习\\chap14\\OS模块.py'))
print(a.join('C:\\Users\\小角色\\Desktop\\python练习', 'OS模块'))
print(a.split('C:\\Users\\小角色\\Desktop\\python练习\\OS模块.py'))
print(a.isdir('C:\\Users\\小角色\\Desktop\\python练习'))
print(a.basename('C:\\Users\\小角色\\Desktop\\python练习\\OS模块.py'))
print(a.dirname('C:\\Users\\小角色\\Desktop\\python练习\\OS模块.py'))"""


"""import os

lis = os.listdir()
for filename in lis:
    filename.endswith('.py')
    print(filename)"""


"""import os

path = os.getcwd()
m = os.walk(path)
for filepath, dirname, name in m:
    print(filepath)
    print(dirname)
    print(name)"""


"""for i in range(3):
    print('哈哈哈')
    for j in range(4):
        print('好好')"""


i = 0
while i < 10:
    b = i + 1
    print("11")
    i = b

print('hello')

