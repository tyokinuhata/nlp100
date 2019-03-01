# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

print([__import__('json').loads(l)['text'] for l in __import__('gzip').open('jawiki-country.json.gz', 'rt') if __import__('json').loads(l)['title'] == 'イギリス'])