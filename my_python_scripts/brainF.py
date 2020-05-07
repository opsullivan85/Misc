import re

def brainF(string,debug=0):
    string=re.sub(r'[^><+-.,\[\]]','',string)
    pointer=0
    mem=[0]
    i=0
    braceSum=0
    while i<len(string):
        c=string[i]
        if(c=='>'):
            pointer+=1
            if(pointer>=len(mem)):
                mem.append(0)
        elif(c=='<'):
            if(pointer):
                pointer-=1
            else:
                raise Exception("Index out of Bounds")
        elif(c=='+'):
            mem[pointer]+=1
        elif(c=='-'):
            mem[pointer]-=1
        elif(c=='.'):
            print(str(chr(mem[pointer])), end='')
        elif(c==','):
            mem[pointer]=input("Input: ")
        elif(c=='['):
            try:
                if(not mem[pointer]):
                    braceSum=1
                    while braceSum:
                        i+=1
                        if string[i]==']':
                            braceSum-=1
                        elif string[i]=='[':
                            braceSum+=1
            except:
                raise Exception("Unmatched brackets")
        elif(c==']'):
            try:
                if(mem[pointer]):
                    braceSum=-1
                    while braceSum:
                        i-=1
                        if string[i]==']':
                            braceSum-=1
                        elif string[i]=='[':
                            braceSum+=1
            except:
                raise Exception("Unmatched brackets")
        i+=1
        if(debug):
            print(len(mem),pointer,i)
    return mem

pgrm='''
+[>+]
'''
#brainF(pgrm,1)












print(re.sub(r'[^><+-.,\[\]]','','''+++++ +++++             initialize counter (cell #0) to 10
[                       use loop to set 70/100/30/10
    > +++++ ++              add  7 to cell #1
    > +++++ +++++           add 10 to cell #2
    > +++                   add  3 to cell #3
    > +                     add  1 to cell #4
<<<< -                  decrement counter (cell #0)
]
> ++ .                  print 'H'
> + .                   print 'e'
+++++ ++ .              print 'l'
.                       print 'l'
+++ .                   print 'o'
> ++ .                  print ' '
<< +++++ +++++ +++++ .  print 'W'
> .                     print 'o'
+++ .                   print 'r'
----- - .               print 'l'
----- --- .             print 'd'
> + .                   print '!'
> .                     print '\n'
'''))











