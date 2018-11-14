import requests
import json

def tweet(text):

	requests.post('https://hooks.slack.com/services/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', data = json.dumps({
	    'text': text, # 投稿するテキスト
	    'username': u'cancelChecker', # 投稿のユーザー名
	    'icon_emoji': u':sunglasses:', # 投稿のプロフィール画像に入れる絵文字
	    'link_names': 1, # メンションを有効にする
	}))

if __name__ == '__main__':
	tweet('hello')
