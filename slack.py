#!/usr/bin/env python


def slack(message):
    requests.post('https://hooks.slack.com/services/', data = json.dumps({
        'text': message, # 投稿するテキスト
        'username': u'feedChecker', # 投稿のユーザー名
        'icon_emoji': u':robot_face:', # 投稿のプロフィール画像に入れる絵文字
        'link_names': 1, # メンションを有効にする
    }))

if __name__ == '__main__':
    slack('hello world')
