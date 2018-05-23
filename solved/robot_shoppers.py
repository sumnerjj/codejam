from collections import deque
def bits_for_cashier_in_time_t(cashier, t):
    m, s, p = cashier
    remaining_time = max(0, t - p)
    bits = min(m, remaining_time/s)
    # print 'bits for cashier %s bits %s' % (bits, cashier)
    return bits

def total_bits_for_time(cashiers, bot_count, t):
    cashier_totals = [bits_for_cashier_in_time_t(c, t) for c in cashiers]
    cashier_totals.sort(reverse=True)
    bits = sum(cashier_totals[:bot_count])
    # print 'total bits cashier totals %s bot_count %s bits %s' % (cashier_totals, bot_count, bits)
    return bits

def bin_recurse(lower, upper, best, cashiers, bot_count, bit_count, debug_counter):
    # print debug_counter
    mid_time = (lower + upper)/2
    if mid_time == lower:
        return best
    total_for_mid = total_bits_for_time(cashiers, bot_count, mid_time)
    if total_for_mid >= bit_count:
        return bin_recurse(lower, mid_time, mid_time, cashiers, bot_count, bit_count, debug_counter+1)
    else:
        return bin_recurse(mid_time, upper, best, cashiers, bot_count, bit_count, debug_counter+1)


def robots(r, b, c, cashiers):
    return bin_recurse(0, 10**19, 10**19, cashiers, r, b, 0)


t = int(raw_input())

for i in range(1, t + 1):
    n, p = [int(x) for x in raw_input().split()]
    cookies = []
    for j in range(n):
        # m, s, p = [int(x) for x in raw_input().split()]
        cookies.append([int(x) for x in raw_input().split()])
    print 'Case #%s: %s' % (i, robots(r, b, c, cashiers))
