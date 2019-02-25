print((lambda str, n: [str[i:i+n] for i in range(len(str) - n + 1)])('I am an NLPer', 2))
print((lambda str, n: [str[i:i+n] for i in range(len(str) - n + 1)])('I am an NLPer'.split(), 2))