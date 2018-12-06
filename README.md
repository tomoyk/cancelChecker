# cancelChcker

学内サイトの休講情報をスクレイピングしてTwitterに投げる。

## 使い方

### パッケージを導入

```
$ pip3 install lxml twitter bs requests feedparser
$ pip3 install --upgrade google-api-python-client oauth2client
```

### クレデンシャルの取得

GoogleカレンダーAPIのcredentialを取得する。

https://console.developers.google.com/apis/credentials

プロジェクトの選択→クライアントIDを選択→JSONをダウンロード→ `credential.json` として保存

### 認証の取得

```
$ python3 calAdd.py --noauth_local_webserver
```

ブラウザに表示された認証コードをターミナルに貼り付ける。

### 実行

走らせる。

    $ python3 main.py

Cronに登録する場合は以下のようにCronを登録する。
```
$ crontab -e
*/5 * * * *  /usr/bin/cd /home/foo/cancelChecker && /usr/bin/python3 /home/foo/cancelChecker/main.py
```

## 概要

1. bs4で学内サイトをスクレピング
1. 取得したデータを解析して過去のデータと比較
1. 新たなデータのみを取り出してTwitterに投稿

## Note

Googleカレンダの扱い: 
https://gist.github.com/tomoyk/a46b2e181ff76a82fddf45566d68a9f0
