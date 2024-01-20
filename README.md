解析MDX/MDD文件，在浏览器显示

需要安装的包：
pip install flask
pip install python-lzo
pip install readmdict
等等

用法：
   
    python flask_server.py

    等服务器启动后 ，访问地址：http://127.0.0.1:8899

    默认为新东方词根词缀词典，
    点击 ‘按索引查询’按钮，即为按索引顺序依次显示mdx字典内容
    在文本框输入“词根”（如：ab-），点击 “查询” 按钮 ，即可显示匹配到的字典内容。‘

仅为测试，后续需要寻找合适的mdx，根据项目转换为合适的数据结构。