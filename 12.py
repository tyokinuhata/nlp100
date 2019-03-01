# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

[open('col1.txt', 'a').write(line[0] + '\n') & open('col2.txt', 'a').write(line[1] + '\n') for line in open('hightemp.txt').readlines()]