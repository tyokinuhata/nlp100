# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
[open('merge.txt', 'a').write(col1[0] + col2[0] + '\n') for col1, col2 in zip(open('col1.txt').readlines(), open('col2.txt').readlines())]