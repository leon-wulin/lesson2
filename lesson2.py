# -*- coding: UTF-8 -*-

filename = "test,txt"

f = open(filename, 'w')

for i in range(10):

    data = "row no.=%2d Hello Word\n" % (i+1
)
    f.write(data)

f.close()
