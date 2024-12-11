import logging


def Clear_logfile():
    with open("app.log", "w") as f:
        pass  # 清空文件内容
def setup_logging():
    Clear_logfile()
    logging.basicConfig(level=logging.DEBUG, 
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("app.log"),
                            logging.StreamHandler()
                        ])


def log_message(message, level=logging.INFO):
    if level == logging.INFO:
        logging.info(message)
    elif level == logging.WARNING:
        logging.warning(message)
    elif level == logging.ERROR:
        logging.error(message)
    else:
        logging.debug(message)
def Rtn_logmessage():
    # 打开并读取文件内容
    with open("app.log", 'r') as file:   
        content = file.read()
        return content