#coding:utf-8
print "How old are you?"
age = raw_input() # 不管用户输入什么 最后都会被转化成字符
print "How tall are you?"
height = raw_input()
print "How much do you weight?"
weight = raw_input()

hei_heavy =float(height) / float(weight)

print "So, you're %r old, %r tall, %r heavy and %f hei_heavy." % (age, height,weight,hei_heavy)
