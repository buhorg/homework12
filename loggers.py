import logging

def create_logger():
    logger = logging.getLogger('basic')
    logger.setLevel('DEBUG')
    console_Handler = logging.StreamHandler()
    file_Handler = logging.FileHandler('logs/basic.txt')
    logger.addHandler(console_Handler)
    logger.addHandler(file_Handler)
    formatter_one = logging.Formatter('%(asctime)s:%(message)s')
    console_Handler.setFormatter(formatter_one)
    file_Handler.setFormatter(formatter_one)
