#coding:utf-8
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #seek(0) 的左右是重新返回文件的起始位置。参数表示返回的位置。单位是byte。如果是1,2，测试程序看看结果。在这之前，read()已经读完，在文件位置的最后，如果不rewind 接下来readline() 读不出任何东西。  如果文档开头是中文，用参数1,2,3,4测试可得，在python utf-8 中，一个汉字占3个bytes。另外，ASCII编码 一个英文字母（不分大小写，也就字符，c++中常用到）占一个字节的空间，一个中文汉字占两个字节的空间。GB 2312/GBK 编码中，一个汉字字符存储需要2个字节。

def print_a_line(line_count, f):
    print line_count, f.readline(),  #如果不加,号 readline() 包含文件本身的\n print 自带\n 所以有两个换行符。去掉看看效果

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print"Now let's rewind, kind of like a tape."

rewind(current_file) 

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1  #用+= 运算符，这样更简便。
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
