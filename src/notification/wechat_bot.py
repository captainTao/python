from src.util.https import Https


class WechatBot:

    def __init__(self, key):
        self.wechat_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key
        pass

    def send_text(self, description):
        data = {
            "msgtype": "text",
            "text": {
                "content": description
            }
        }
        self.__send_msm(data)

    def send_markdown(self, description):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": description
            }
        }
        self.__send_msm(data)

    def send_picture(self, picbase64, picmd5):
        data = {
            "msgtype": "image",
            "image": {
                "base64": picbase64,
                "md5": picmd5
            }
        }
        self.__send_msm(data)

    def send_pic_text(self, title, description, url, picurl):
        data = {
            "msgtype": "news",
            "news": {
                "articles": [{
                    "title": title,
                    "description": description,
                    "url": url,
                    "picurl": picurl
                }]
            }
        }
        self.__send_msm(data)

    def __send_msm(self, data):
        header = {
            'Content-Type': 'application/json'
        }
        Https.post(self.wechat_url, '', data, header)


if __name__ == '__main__':
    wechatBot = WechatBot()
    wechatBot.send_text("你好...我是机器人此消息")
