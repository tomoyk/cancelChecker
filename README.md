# cancelChcker

学内サイトの休講情報をスクレイピングしてTwitterに投げる。

## 使い方

パッケージを導入する。

    $ pip3 install lxml twitter bs

走らせる。

    $ python3 main.py

Cronに登録する場合は以下のようなスクリプトを作成する。

    #!/bin/bash
    cd /you-path/
    python3 main.py
    exit 0

## 概要

1. bs4で学内サイトをスクレピング
1. 取得したデータを解析して過去のデータと比較
1. 新たなデータのみを取り出してTwitterに投稿
