def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

def cookie_weight(cookie):
    return 2*min(cookie[0], cookie[1])

def cookie_value(cookie):
    a, b = cookie
    return 2*((a**2 + b**2)**(1.0/2))

def optimal_cuts(n, p, cookies):
    starting_perim = sum(2*(x[0] + x[1]) for x in cookies)
    target = p - starting_perim
    if target == 0:
        return p
    weights = [cookie_weight(c) for c in cookies]
    values = [cookie_value(c) for c in cookies]
    maxx = knapSack(target, weights, values, n) + starting_perim
    return min(maxx, p)


t = int(raw_input())

for i in range(1, t + 1):
    n, p = [int(x) for x in raw_input().split()]
    cookies = []
    for j in range(n):
        cookies.append([int(x) for x in raw_input().split()])
    print 'Case #%s: %s' % (i, optimal_cuts(n, p, cookies))
