def tidy(s):
    array = [int(c) for c in s][::-1]
    for i in range(len(array) - 1):
        if array[i] < array[i+1]:
            asd = [9]*(i+1) +[array[i+1] -1] + array[i+2:]
            array = asd
    qwe = [str(c) for c in array][::-1]
    r = ''.join(qwe)
    return str(int(r))



import sys
lines = sys.stdin.readlines()
for i, line in enumerate(lines[1:]):
    s = line.split()[0]
    print 'Case #%s: %s' % (i+1, tidy(s))

'''
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
  m, n = [int(s) for s in raw_input().split()]
  primes(m, n)
  print '\r'
'''
# tidy numbers https://code.google.com/codejam/contest/3264486/dashboard#s=p1
