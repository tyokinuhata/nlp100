# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

print(' '.join(s if len(s) <= 4 else s[0] + ''.join(__import__('random').sample(s[1:-1], len(s) - 2)) + s[-1] for s in "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split()))