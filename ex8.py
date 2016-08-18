#coding:utf-8
formatter = "%r %r %r %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
     "I have this thing.",
     "That you should type up right.",
     "But it didn't sing.",
     "中文。So I said goodnight" #包含中文，这里输出就会是乱码，要讲最后一个r修改成s
)
