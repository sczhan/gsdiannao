f = open('2.txt', 'r+')
# print('欢迎使用Python',file=f)
# f.write('hello欢迎')
# f.writelines(['\naaaa','\nbbbb'])
# t=f.read(10)
# t=f.readline()
t = f.readlines()
print(type(t), t)
f.close()