l = ['nomad', 'normal', 'nonstop', 'nooba']

def common_prefix(lst):
    for s in zip(*lst):
        if len(set(s)) == 1:
            yield s[0]
        else:
            return

result = ''.join(common_prefix(l))
print(result)