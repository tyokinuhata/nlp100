# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

n_gram = lambda str: {str[i:i + 2] for i in range(len(str) - 1)}

x = n_gram('paraparaparadise')
y = n_gram('paragraph')

# 和集合, 積集合, 差集合, xに"se"が含まれるか, yに"se"が含まれるか
print(x | y, x & y, x - y, 'se' in x, 'se' in y)