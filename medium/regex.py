import re

def matches_same_start_end(s):
    return bool(re.match(r'^(a[ab]*a|b[ab]*b|a|b)$', s))

# Test cases
test_strings = [ 'a', 'b', 'ab', 'ba', 'aba']

for s in test_strings:
    print(f"{s!r}: {matches_same_start_end(s)}")
