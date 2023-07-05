# bilibili弹幕

简简单单刷bilibili视频弹幕。

配置：
1. python3.8以上
2. pip install bilibili-api
3. 代码中的配置：
```python
# 从cookie中获取（f12打开控制台，选择网络，找到一个请求的cookie，从中获得相应字段即可）
SESSDATA = ""
BILI_JCT = ""
BUVID3 = ""
# 视频的bvid（从url中获取）
bid  = "BVxxxx"
```