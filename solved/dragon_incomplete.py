def dragon(health_dragon, attack_dragon, health_knight, attack_knight, buff, debuff):
    print health_dragon, attack_dragon, health_knight, attack_knight, buff, debuff
    if buff > attack_dragon:
        attack_moves_required = attacks_required_with_buff(attack_dragon, buff, health_knight)
    else:
        attack_moves_required = attacks_required_no_buff(attack_dragon, health_knight)
    return attack_moves_required

def attacks_required_with_buff(attack, buff, health):
    count = 0
    delta = health - attack
    if delta > 0:
        count += attacks_required_no_buff(buff, delta)
    count += 1
    return count

def attacks_required_no_buff(attack, health):
    count = health/attack
    count = count if health%attack == 0 else count + 1
    count = max(count, 1)
    return count



t = int(raw_input())

for i in range(1, t + 1):
    hd, ad, hk, ak, b, d = [int(x) for x in raw_input().split()]
    print 'Case #%s: %s' % (i, dragon(hd, ad, hk, ak, b, d))
