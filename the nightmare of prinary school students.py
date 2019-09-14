# -*- coding: UTF-8 -*-
import random
ques_answer='1.txt'
ques_no_answer='2.txt'

f1 =open(ques_answer,'w')
f2 =open(ques_no_answer,'w')

for row in range(20):
    for col in range(5):
        a=random.randint(1,99)
        b=random.randint(1,99)
        op=(random.randint(1,10000))% 4
        if op ==0:
            c = a + b
            op_str='+'
        elif op ==1:
            c=a - b
            op_str='-'
        elif op ==2:
            c=a * b
            op_str='X'
        elif op ==3:
            c=a / b
            op_str='/'
        problem= '%d %s %2d=\t\t\t\t\t' % (a,op_str,b)
        answer='%d %s %2d=%0.2f\t\t\t\t\t' % (a,op_str,b,c)
        f1.write(answer)
        f2.write(problem)

    f1.write('\n')
    f2.write('\n')

f1.close()
f2.close()
