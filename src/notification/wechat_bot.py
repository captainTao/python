from src.util.https import Https


class WechatBot:

    def __init__(self, key):
        self.wechat_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key
        pass

    def send_text(self, description):
        request = {
            "msgtype": "text",
            "text": {
                "content": description
            }
        }
        self.__send_msm(request)

    def send_markdown(self, description):
        request = {
            "msgtype": "markdown",
            "markdown": {
                "content": description
            }
        }
        self.__send_msm(request)

    def send_picture(self, picbase64, picmd5):
        request = {
            "msgtype": "image",
            "image": {
                "base64": picbase64,
                "md5": picmd5
            }
        }
        self.__send_msm(request)

    def send_pic_text(self, title, description, url, picurl):
        request = {
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
        self.__send_msm(request)

    def __send_msm(self, request):
        header = {
            'Content-Type': 'application/json'
        }
        Https.send_post_data(self.wechat_url, '', request, header)


if __name__ == '__main__':
    wechatBot = WechatBot()
    wechatBot.send_text("你好...我是机器人此消息")
