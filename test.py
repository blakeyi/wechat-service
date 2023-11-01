from wesdk import Bot
import logging

def on_msg(msg):
    logging.info("hi")

# connect to hook service
bot = Bot(ip='127.0.0.1', port=5555)
bot.register("on_open", lambda ws: logging.info("hi"))
bot.register("on_close", lambda ws: logging.info("bye"))
bot.register("recv_txt_msg", lambda msg: logging.info("msg"))
# run event loop
bot.run()