#coding:utf-8
from sys import argv    #module

script, user_name,space = argv #自己加的第二个参数 argument 
prompt = '->'

print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few question."
print "Do you like me %s? " % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Do you want to go %s?" % space #自己加的第二个参数
ask = raw_input(prompt)

print """
Alright, so you said %r about likeing me.
You live in %r. Not sure where that is.
And you have a %r computer. You want go to %r. Nice.
""" % (likes,lives,computer,space)
