n_gram = lambda str: {str[i:i + 2] for i in range(len(str) - 1)}

x = n_gram('paraparaparadise')
y = n_gram('paragraph')

print(x | y, x & y, x - y, 'se' in x, 'se' in y)