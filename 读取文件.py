# 2021-04-23  15:43
"""file = open('C:\\Users\\小角色\\Desktop\\《三国演义》作者：罗贯中.txt', 'r')
print(file.readlines())
file.close()"""


"""file = open('C:\\Users\\小角色\\Desktop\\b.txt', 'a')
print(file.write('hello world'))
file.close()"""


"""file = open('C:\\Users\\小角色\\Desktop\\诊断证明.jpg', 'rb')
file1 = open('C:\\Users\\小角色\\Desktop\\诊断证明2.jpg', 'wb')
file1.write(file.read())
file.close()
file1.close()"""


file = open('C:\\Users\\小角色\\Desktop\\111.txt', 'w', encoding='utf-8')
print(file.write('ML'))
file.flush()
print(file.write('AI'))
file.close()





