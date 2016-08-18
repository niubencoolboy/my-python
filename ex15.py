#coding:utf-8
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()


#其实下面的代码与上面的功能一样，都是读一个文件，一个是用argv 下面的用raw_input()
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
