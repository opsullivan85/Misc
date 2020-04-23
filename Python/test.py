def f(p1,p2):
    return f"({p1}(1-t)+{p2}t)"

a='a'
b='b'
c='c'
d='d'

print(f(f(f(a,b),f(b,c)),f(f(b,c),f(c,d))))
