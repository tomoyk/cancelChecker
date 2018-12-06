# cancelChcker

学内サイトの休講情報をスクレイピングしてTwitterに投げる。

## 使い方

パッケージを導入する。

```
$ pip3 install lxml twitter bs requests
$ pip3 install --upgrade google-api-python-client oauth2client
```

走らせる。

    $ python3 main.py

Cronに登録する場合は以下のようなスクリプトを作成する。
```
#!/bin/bash
cd /you-path/
python3 main.py
exit 0
```

## 概要

1. bs4で学内サイトをスクレピング
1. 取得したデータを解析して過去のデータと比較
1. 新たなデータのみを取り出してTwitterに投稿

## Note

Googleカレンダの扱い: 
https://gist.github.com/tomoyk/a46b2e181ff76a82fddf45566d68a9f0
