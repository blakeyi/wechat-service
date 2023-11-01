from wesdk import *
# connect to hook service
bot = Bot(ip='127.0.0.1', port=5555)
bot.register("on_open", lambda ws: logging("hi"))
bot.register("recv_txt_msg", lambda msg: logging(msg))
# run event loop
bot.run()