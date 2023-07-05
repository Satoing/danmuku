import asyncio
from bilibili_api import video, Credential, Danmaku
import time

# 从cookie中获取
SESSDATA = ""
BILI_JCT = ""
BUVID3 = ""
# 视频的bvid（从url中获取）
bid  = "BVxxxx"
# 弹幕的文字内容
content = ""

async def main():
    # 实例化 Credential 类
    credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUVID3)
    # 实例化 Video 类
    v = video.Video(bvid=bid, credential=credential)
    count = 0
    while count <= 3000:
        try:
            # 获取视频信息
            info = await v.get_info()
            count += 1
            # 打印视频弹幕数
            print(f"当前弹幕数：{info['stat']['danmaku']}")
            # 发弹幕
            d = Danmaku(text=content)
            await v.send_danmaku(0, d)
            if count%6 == 0:
                print("暂停30s")
                time.sleep(30)
            time.sleep(6)
        except:
            print("发送太快，暂停5min")
            time.sleep(300)

if __name__ == '__main__':
    # 主入口
    asyncio.get_event_loop().run_until_complete(main())