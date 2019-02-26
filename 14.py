# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
print(''.join([l for i, l in zip(range(int(__import__('sys').argv[1])), open('hightemp.txt').readlines())]))