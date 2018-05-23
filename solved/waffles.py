def chips_in_section(waffle, row_start, row_end, column_start, column_end):
    return sum([sum(row[column_start:column_end]) for row in waffle[row_start:row_end]])

def chipossible(r, c, h, v, waffle):
    row_sums = {i + 1: sum(waffle[i]) for i in range(r)}
    column_sums = {j + 1: sum([waffle[i][j] for i in range(r)]) for j in range(c)}
    total_chips = sum([row_sums[i] for i in range(1, r+1)])
    total_diners = (h+1)*(v+1)
    if total_chips == 0:
        return 'POSSIBLE'
    if total_chips%total_diners != 0:
        return 'IMPOSSIBLE'
    chips_per_diner = total_chips/total_diners
    running_chips = 0
    h_cuts = []
    for row in range(1, r + 1):
        running_chips += row_sums[row]
        if running_chips < (v+1)*chips_per_diner:
            continue
        elif running_chips > (v+1)*chips_per_diner:
            return'IMPOSSIBLE'
        elif running_chips == (v+1)*chips_per_diner:
            running_chips = 0
            h_cuts.append(row)
    if len(h_cuts) > h + 1:
        return'IMPOSSIBLE'

    running_chips = 0
    v_cuts = []
    for column in range(1, c + 1):
        running_chips += column_sums[column]
        if running_chips < (h+1)*chips_per_diner:
            continue
        elif running_chips > (h+1)*chips_per_diner:
            return'IMPOSSIBLE'
        elif running_chips == (h+1)*chips_per_diner:
            running_chips = 0
            v_cuts.append(column)
    if len(v_cuts) > v + 1:
        return'IMPOSSIBLE'

    last_hcut = 0
    last_vcut = 0
    for hcut in h_cuts:
        for vcut in v_cuts:
            if chips_in_section(waffle, last_hcut, hcut, last_vcut, vcut) != chips_per_diner:
                return'IMPOSSIBLE'
            else:
                last_vcut = vcut
        last_vcut = 0
        last_hcut = hcut

    return'POSSIBLE'


t = int(raw_input())
for i in xrange(1, t + 1):
    R, C, H, V = [int(x) for x in raw_input().split()]
    waffle = []
    for j in range(R):
        row = [1 if x=='@' else 0 for x in raw_input()]
        waffle.append(row)
    print 'Case #%s: %s' % (i, chipossible(R, C, H, V, waffle))

