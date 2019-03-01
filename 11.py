# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

open('hightemp2.txt', 'w').write((open('hightemp.txt').read()).replace('\t', ' '))