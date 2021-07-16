#!/bin/env python

def permu(xs):
    # submitted to python cookbook
    # http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496819
    if len(xs)<2: yield xs
    else:
        h = []
        for x in xs:
            h.append(x)
            if x in h[:-1]: continue
            ts = xs[:]; ts.remove(x)
            for ps in permu(ts):
                yield [x]+ps

def bags(xs):
    lx = len(xs)
    if lx<2: yield [xs]
    for i in range(1,lx):
        yield [xs[:i],xs[i:]]
    
def calrec(list):
    if len(list)==1: return [[list[0],str(list[0])]]
    r = []
    for li in bags(list):
        for o in ['+','-','*','/']:
            for a in calrec(li[0]):
                for b in calrec(li[1]):
                    if o=='+': 
                        t = a[0]+b[0]
                        x = "%s+%s"%(a[1],b[1])
                    elif o=='-' and a[0]>=b[0]: 
                        t = a[0]-b[0]
                        x = "%s-%s"%(a[1],b[1])
                    elif o=='*': 
                        t = a[0]*b[0]
                        x = "%s*%s"%(a[1],b[1])
                    elif o=='/' and b[0]!=0 and a[0]%b[0]==0: 
                        t = a[0]/b[0]
                        x = "%s/%s"%(a[1],b[1])
                    else: continue
                    
                    x = '(%s)'%x
                    r.append([t,x])
    return r
    

def calc(e,d):
    for p in permu(d):
        for i in calrec(p):
            if i[0]==e: return i[1][1:-1]
    return ''

if __name__ == '__main__':
    import time, sys
    start = time.time()

    argv = sys.argv
    if len(argv)>1 and argv[1].startswith('c'):
        try: what = int(argv[1][1:])
        except:
            print("What?")
            sys.exit()	
        argv = argv[1:] 
    else: what = 24

    la = len(argv)

    if la<2:
        p,s,r = 0,0,14 # change r to 14 for J=11,Q=12,K=13 instead of 1
        for i in range(1,r):
            for j in range(i,r):
                for k in range(j,r):
                    for l in range(k,r):
                        d = [i,j,k,l]
                        a = calc(what, d)
                        p+=1
                        if a: s+=1; print("%s: %s"%(d,a))
                        else: print("%s: no solution!"%d)
        print("total %d, solvable %d"%(p,s))
    elif la<3:
        print("missing numbers?")
        sys.exit()
    else:
        try: d = map(int,argv[1:])
        except:
            print("wrong format")
            sys.exit()
        print(calc(what,d))

    #print time.time()-start
