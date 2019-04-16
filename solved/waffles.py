'''
https://codingcompetitions.withgoogle.com/codejam/round/0000000000007883/000000000003005a

Problem
The diners at the Infinite House of Pancakes have gotten tired of circular pancakes, so the chefs are about to offer a new menu option: waffles! As a publicity stunt, they have made one large waffle that is a grid of square cells with R rows and C columns. Each cell of the waffle is either empty, or contains a single chocolate chip.

Now it is time for the chefs to divide up the waffle among their hungry diners. A horizontal cut runs along the entire gridline between two of the rows; a vertical cut runs along the entire gridline between two of the columns. For efficiency's sake, one chef will make exactly H different horizontal cuts and another chef will make exactly V different vertical cuts. This will conveniently create one piece for each of the (H + 1) × (V + 1) diners. The pieces will not necessarily all be of equal sizes, but that is fine; market research has shown that the diners do not care about that.

What the diners do care about is the number of chocolate chips they get, so each piece must have exactly the same number of chocolate chips. Can you determine whether the chefs can accomplish this goal using the given numbers of horizontal and vertical cuts?

Input
The first line of the input gives the number of test cases, T; T test cases follow. Each begins with one line containing four integers R, C, H, and V: the number of rows and columns in the waffle, and the exact numbers of horizontal and vertical cuts that the chefs must make. Then, there are R more lines of C characters each; the j-th character in the i-th of these lines represents the cell in the i-th row and the j-th column of the waffle. Each character is either @, which means the cell has a chocolate chip, or ., which means the cell is empty.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is POSSIBLE if the chefs can accomplish the goal as described above, or IMPOSSIBLE if they cannot.

Limits
1 ≤ T ≤ 100.
Time limit: 6 seconds per test set.
Memory limit: 1GB.

Test set 1 (Visible)
2 ≤ R ≤ 10.
2 ≤ C ≤ 10.
H = 1.
V = 1.

Test set 2 (Hidden)
2 ≤ R ≤ 100.
2 ≤ C ≤ 100.
1 ≤ H < R.
1 ≤ V < C.
'''

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

