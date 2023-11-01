from wesdk import *
# connect to hook service
def on_msg(msg):
    logging(msg)

bot = Bot(ip='127.0.0.1', port=5555)
bot.register("on_open", lambda ws: logging("hi"))
bot.register("recv_txt_msg", lambda msg: on_msg(msg))
# run event loop
bot.run()