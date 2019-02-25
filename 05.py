# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# 単語bi-gram
print((lambda str, n: [str[i:i+n] for i in range(len(str) - n + 1)])('I am an NLPer'.split(), 2))

# 文字bi-gram
print((lambda str, n: [str[i:i+n] for i in range(len(str) - n + 1)])('I am an NLPer', 2))