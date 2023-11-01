from wesdk import *
from bigmodel.xfspark.xfspark import getAnswer as getXunFeiAnswer
from bigmodel.baidu.ERNIE import getAnswer as getBaiduAnswer

# connect to hook service
def on_msg(msg):
    logging(msg)
    ans = getXunFeiAnswer(str(msg["content"]).replace("@masteryi", ""))
    if msg["roomid"]:
        nickname = bot.get_chatroom_member_nick(msg["roomid"], msg['senderid'])
        print("nickname", nickname)
        bot.send_msg(ans, msg['senderid'], msg["roomid"], "总想")
    else:
        bot.send_msg(ans, msg['wxid'])

bot = Bot(ip='127.0.0.1', port=5555)
bot.register("on_open", lambda ws: logging("hi"))
bot.register("recv_txt_msg", lambda msg: on_msg(msg))
# run event loop
bot.run()