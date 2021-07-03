boys = [
    {'n': 'b0', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'b1', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'b2', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'b3', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'b4', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
]
girls = [
    {'n': 'g0', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'g1', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'g2', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'g3', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
    {'n': 'g4', 'prefer': [0, 1, 2, 3, 4], 'pair': None},
]

marriage = set()

for step in range(len(boys)):
    loop = True
    b_pos = step
    print("----Step---- ")
    while loop:
        b = boys[b_pos]
        print(f'New loop step {step}', marriage, b)
        for b_prefer in b['prefer']:
            if girls[b_prefer]['pair'] == None:
                girls[b_prefer]['pair'] = b_pos
                pair = 'b%s_g%s' % (b_pos, b_prefer)
                marriage.add((pair,))
                print("no marr")
                loop = False
                break
            else:
                for g_prefer in girls[b_prefer]['prefer']:
                    if g_prefer == girls[b_prefer]['pair']:
                        loop = False
                        break
                    if g_prefer == b_pos:
                        rem_pair = 'b_%sg_%s' % (
                            girls[b_prefer]['pair'], b_prefer)
                        girls[b_prefer]['pair'] = b_pos
                        add_pair = 'b_%sg_%s' % (b_pos, b_prefer)
                        marriage.remove((rem_pair,))
                        marriage.add((add_pair,))
                        loop = True
                        break

print(marriage)
