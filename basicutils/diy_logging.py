# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午9:03
# @Author  : Felix Wang

import logging
import traceback


def my_log(logfile, partName, level):
    """
    :param logfile: 日志文件名
    :param partName: 项目名称，模块名称或者其他日志使用者
    :param level: 日志等级
    :return: logger object

    # CRITICAL = 50
    # FATAL = CRITICAL
    # ERROR = 40
    # WARNING = 30
    # WARN = WARNING
    # INFO = 20
    # DEBUG = 10
    # NOTSET = 0

    """
    # 多文件日志处理
    # 创建⼀个操作⽇志的对象logger（依赖FileHandler）
    file_handler = logging.FileHandler(logfile, 'a', encoding='utf-8')
    # 设置日志文件内容的格式
    file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s: %(message)s"))
    logger = logging.Logger(partName, level=level)
    logger.addHandler(file_handler)
    return logger


# 记录日志
# # 写日志
# # logger.critical("我是critical")
# # logger.error("我是error")
# # logger.warning("我是警告")
# # logger.info("我是基本信息")
# # logger.debug("我是调试")
# # logger.log(2, "我是自定义")

if __name__ == '__main__':

    logger = my_log('my.log', 'felix', logging.WARNING)

    for i in range(20):
        try:
            if i % 3 == 0:
                raise FileNotFoundError("我是FileNotFountException")
            elif i % 3 == 1:
                raise StopIteration()
            elif i % 3 == 2:
                raise KeyError()

        except FileNotFoundError as e:
            val = traceback.format_exc()
            logger.warning(val)
        except StopIteration as e:
            val = traceback.format_exc()
            logger.error(val)
        except KeyError as e:
            val = traceback.format_exc()
            logger.info(val)
        except Exception as e:
            val = traceback.format_exc()
            logger.critical(val)
