# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
[[open('hightemp{}.txt'.format(i - int(i / int(__import__('sys').argv[1]) * (int(__import__('sys').argv[1]) - 1))), 'a').write(l) for l in open('hightemp.txt').readlines()[i:i + int(__import__('sys').argv[1])]] for i in range(0, len(open('hightemp.txt').readlines()) - 1, int(__import__('sys').argv[1]))]