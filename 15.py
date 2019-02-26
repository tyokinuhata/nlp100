# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
print(''.join(reversed([l for i, l in zip(range(int(__import__('sys').argv[1])), reversed(open('hightemp.txt').readlines()))])))