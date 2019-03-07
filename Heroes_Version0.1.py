'''2018.7.3'''
#_*_ coding:utf-8 _*_
#this is code
#print("please input your heron name:")
# print("welcome to Heron world!")
# print("-------------------------------------------")
# print("|the map is #######,'a'is left,'b'is right|")
#
# print("-------------------------------------------")
# name=input("your heron name is:")
# hp=100
# if not name:
#     name='player'
# usermsg=[name,hp]
# print("your hero name is:",usermsg[0],"\nhp is:",usermsg[1])
# print("now you ere here *######")
# userinput=input()
# if userinput == 'a':
#     print("now you sre here #*######")
# if userinput == 'b':
#     print("now you are here *#######")



#hero_ver_0.2

# print("welcome to hero world!")
# print("the hero world is like ####, a is left, d is right")
# name = input("your hero name is:")
# if not name:
#     name = "zach"
# hp = 100;
# usermsg = [name, hp]
# userinput = input("please input which direction you choose:")
# if userinput is "a":
#     print("now you are here *###")
# elif userinput is "d":
#     print("now you are here #*##")
# else:
#     print("you are inut error!")







#hero_ver_0.3
# welcome = "welcome to hero world"
# # magsg = "#######"
# instruction = '''
# |'a' is left|'d' is right|'''
#
# print(welcome)
# map = ['#', '#', '#', '#', '#', '#', '#']
# print(map, instruction)
#
# name = input("please input your hero name:")
# if not name:
#     name = "zach"
# hp = 100
#
# usermsg = {"name": name, "hp": hp}
#
# print("your hero name:", usermsg['name'], "hp:",usermsg['hp'])
# point = 0
# while 1:
#     map[point] = '*'
#     print("you are here:", "".join(map))
#     userinput = input("go or quit:")
#
#     if userinput is 'a' and point<6:
#         map[point] = '#'
#         point += 1
#     elif userinput is 'd' and point >0:
#         map[point] = '#'
#         point -= 1
#     elif userinput is "quit":
#         print("--bybe--")
#         break
#     else:
#         print(instruction)


#该段code已经被锁住，需要找到lock.log文件删除即可
# import os    #os该模块可以创建文件夹，寻找文件等
# i = 0
# welcome = "welcome to hero world"
# while True:
#     if os.path.isfile('lock.log'):
#         print("locked")
#         break
#     username = input("input hero name:")
#     passwd = input("input passwd:")
#
#     i += 1
#     if username == "zach" and passwd == "123":
#         print(welcome)
#         break
#     else:
#         if i == 3:
#             open('lock.log', 'w').writable(username)
#             print("username:%s is locked" %username)
#             break
#         continue
#     # print(welcome)


# welcome = "welcome to hero world"
# # magsg = "#######"
# instruction = '''
# |'a' is left|'d' is right|'''
#
# print(welcome)
# map = ['#', '#', '#', '#', '#', '#', '#']
# print(map, instruction)
#
# name = input("please input your hero name:")
# if not name:
#     name = "zach"
# hp = 100
#
# usermsg = {"name": name, "hp": hp}
#
# print("your hero name:", usermsg['name'], "hp:",usermsg['hp'])
# point = 0
# while 1:
#     map[point] = '*'
#     print("you are here:", "".join(map))
#     userinput = input("go or quit:")
#
#     if userinput is 'd' and point<6:
#         map[point] = '#'
#         point += 1
#     elif userinput is 'a' and point >0:
#         map[point] = '#'
#         point -= 1
#     elif userinput is "quit":
#         print("--bybe--")
#         break
#     else:
#         print(instruction)

# ***************************************
# class hero:
#     def __init__(self,name,hp,act):
#         self.name = name
#         self.hp = hp
#         self.act = act
#         print("%s init complete!"%self.name)
#
#     def hit(self, name):
#         name.hp -= self.act
#
#
# class element:
#     def __init__(self, name, hp, act):
#         self.name = name
#         self.hp = hp
#         self.act = act
#         print("%s init complete!"%self.name)
#
# if __name__ == "__main__":
#     zach = hero("zach", 100,10)
#     element = element("boss", 200,20)







