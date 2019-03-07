# a caculator
x = int(input("x = "))
o = input("operation :")
y = int(input("y = "))

operation = {
         '+': x+y,
         '-': x-y,
         '*': x*y,
         '/': x/y,}

#result = operation[o]  #这种只能输入字典里对应的 键
result = operation.get(o,"please input:+ - * /")
                        #这种可以在输入错误时给个提示
print("result is:",result)