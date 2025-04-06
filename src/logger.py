import logging
import os

from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H,_%M_%S')}.log"                                  #How the log file will be created
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)                                              #Naming the File with path specified
os.makedirs(log_path, exist_ok= True)


LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,

)

