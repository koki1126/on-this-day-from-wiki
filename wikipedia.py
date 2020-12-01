'''
https://qiita.com/seradaihyo/items/006c5f1c86314a3b7a38
pythonでwikipediaをスクレイピングする
'''
#
# import requests,bs4
#
# # urlの取得
#
#
# url = 'https://ja.wikipedia.org/wiki/Python'
# res = requests.get(url)
#
# # htmlの取得
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
# # 選択した要素を取得
# index = soup.select('#toc')
#
# # 出力する
# for i in index:
#     print(i.getText())


'''
先にコメントアウトでコードの処理を考えていく方法
'''

'''
スクレイピングに必要な流れ
htmlのソースコードを取得
クラス、文字列などから必要なものを取得する
for文で回して出力する(必要に応じて)
'''

# 必要なライブラリの取得
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup


# htmlのソースを取得する
# url = 'https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8'
# html = requests.get(url)
# soup = BeautifulSoup(html.content, 'html.parser')
#
# # テスト
# # print('htmlのソース')
# # print('soupのみ')
# print(soup)
# print('soup.prettify')
# print(soup.prettify)


# 文字を取り出す 文字以外の要素を削除
# for script in soup(['script', 'style']):
#     script.decompose()


# テキストのみを取得　タグは全部取る
# text = soup.get_text()


# テキストを改行ごとにリストに入れて、リスト内の要素の前後の空白を削除
# line=[]
# for line in text.splitlines():
#     lines.append(line.strip)
#
#
# text = '\n'.join(line for line in lines if line)



'''
amazonprimevideoでその映画が無料で見られるかを確認するプログラム
'''

'''
wikipediaの「今日は何の日」から一日一回取得する
'''

'''
※練習
日経ビジネスから
新着記事の見出しとURLを取得する
'''

# import requests
# from bs4 import BeautifulSoup
# import re
#
# urlName = 'https://business.nikkei.com/'
# url = requests.get(urlName)
# soup = BeautifulSoup(url.content, 'html.parser')
#
# elems = soup.find_all('span')
# for elem in elems:
#     try:
#         string = elem.get('class').pop(0) #spanから'class'を取り出す
#         if string in 'category': #in→その文字列が含まれているかを判定してくれる
#             print(elem.string)
#             title = elem.find_next_sibling('h3') #兄弟要素を取得する
#             print(title.text.replace('\n',''))
#             r = elem.find_previous('a')
#             print(urlName + r.get('href'), '\n')
#         except:
#             print('エラーです')




# 取得したいクラス名 mainpage-content-text


# 日経ビジネス電子版から新着記事の見出しとURLを取得する。https://business.nikkei.com/

# import requests
# from bs4 import BeautifulSoup
# import re
#
# #urlとhtmlのコンテンツを取得する
# urlName = 'https://business.nikkei.com/'
# url = requests.get(urlName)
# soup = BeautifulSoup(url.content, 'html.parser')
#
#
# # beautifulsoupでhtmlの解析をする
#
# elems = soup.find_all('span') #span要素をすべてelemsに格納
#
# for elem in elems:
#     try:
#         string = elem.get("class").pop(0) #elemからclassを取り出す
#         if string in 'category': #文字列の中に'カテゴリ'があった場合
#             print(elem.string) #テキスト名を抜き出す
#             title = elem.find_next_sibling('h3') #find_next_sibling()で同じ深さのh3を検索する
#             print(title.text.replace('\n', '')) #タイトルをプリントする
#             r = elem.find_previous('a') #find_previous()でaタグを探す。
#             print(urlName + r.get('href'), '\n')
#     except:
#         pass



import requests
from bs4 import BeautifulSoup
import re
import datetime

today = datetime.date.today() #今日の日付を出力する

urlName = 'https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8'

url = requests.get(urlName)
soup = BeautifulSoup(url.content, 'html.parser')

elems = soup.select('.mainpage-onthisday',)


print(today)
print('本日のできごと')


for elem in elems:
    result = []
    print(elem.text)
    result.append(elem.text)
    # /nのところで改行をしてリスト形式にする
    # printをするまえに上記を行えば更にきれいになる？

# 結果を出力したい
# with open('result.html', 'a', encoding='utf-8,') as f:
#   print(result, file=f)
