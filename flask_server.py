# -*- coding: utf-8 -*-
import os
import sys
from readmdict import MDX
from flask import Flask, request, render_template
from glob import glob
import shutil

# 加载.mdx文件,修改此处，可以更换不同的mdx；
# 注意： 路径下必须同时包含mdx和css文件。
dict_dir = 'Vocabulary/新东方英语词根词缀'
dict_dir = 'Vocabulary/etymology'

mdx_name = glob(os.path.join(dict_dir,'*.mdx'))[0]
css_name = glob(os.path.join(dict_dir,'*.css'))[0]

print('mdx_name = ', mdx_name)
print('css_name = ', css_name)
shutil.copy(css_name, 'static/css/')
css_name = os.path.basename(css_name)

mdx = MDX(mdx_name)
headwords = [*mdx]       # 单词名列表
items = [*mdx.items()]   # 释义html源码列表
n = len(headwords)
m = len(items)
if n == m:
    print(f'{mdx_name} 加载成功：共{n}条')
else:
    print(f'ERROR:加载失败 {n}!={m}')
    sys.exit(1)
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("index.html")
 
@app.route('/trans', methods=['POST'])
def trans():
    result = ''
    if request.method == 'POST':
        try:
            txt = request.form['txt']
        except:
            return '1: get txt error'
        if len(txt.strip()) ==0:
            return 'text is null'
        print(txt)
        if not txt.isascii():
            return 'Maybe text is not english'
        word = txt.encode()
        word1 = txt.capitalize().encode() 
        global headwords, items
        try: 
            if word in headwords:
                wordIndex = headwords.index(word)
            else:
                wordIndex = headwords.index(word1)
            word,html = items[wordIndex]
            print('********Search: ', wordIndex,word, html)
            result = html.decode()
            result = result.replace(css_name,os.path.join('static/css',css_name))
            print('Final Result: \n', result)
        except:
            result = f"<h3>{txt} is not in word_list.</h3>"
            print('Exception:', result)
            print('Error : Cannot  Find the Word!!!')
    return result

@app.route('/incrementAndSubmit', methods=['POST'])
def incrementAndSubmit():
    result = ''
    # 获取前端发送的 JSON 数据
    data = request.get_json()
    # 从 JSON 数据中获取递增的 ID
    increment_id = data.get('id')
    # 在实际应用中，这里可以进行相应的处理，例如保存到数据库等
    print(f'Received ID from frontend: {increment_id}')
    global headwords, items
    try: # 查词，返回单词和html文件
        wordIndex  = increment_id
        word,html = items[wordIndex]
        #print('********Search: ', wordIndex,word, html)
        result = html.decode()
        result = result.replace(css_name,os.path.join('static/css',css_name))
        #print('Final Result: \n', result)
    except:
        result = f"<h3>{increment_id} is not in word_list.</h3>"
        print('Exception:', result)
        print('Error : Cannot  Find the Word!!!')
    return result

   
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8899, debug=True)


