def pan(s, k):
    in_st = s.replace('-','1').replace('+','0')
    bits = int(in_st, 2)
    kflip = 2**k-1
    kmin = 2**(k-1)
    total = 0
    while True:
        while bits % 2 == 0:
            bits = bits / 2
            if bits == 0:
                return str(total)
        if bits < kmin:
            return 'IMPOSSIBLE'
        bits = bits ^ kflip
        total += 1

import sys
lines = sys.stdin.readlines()
for i, line in enumerate(lines[1:]):
    s, k = line.split()
    k = int(k)
    print 'Case #%s: %s' % (i+1, pan(s, k))

'''
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
  m, n = [int(s) for s in raw_input().split()]
  primes(m, n)
  print '\r'
'''
# pancake https://code.google.com/codejam/contest/3264486/dashboard
