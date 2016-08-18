#coding:utf-8
tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

flat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''  # 这里单引号双引号没什么区别，但是如果字符串里有单引号 外部就用双引号，里面有双引号，外部就用单引号。

print tabby_cat
print persian_cat
print backslash_cat
print flat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i  #\r 回车符  \n换行符  \n的距离更大
