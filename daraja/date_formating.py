from datetime import datetime

def formatDateTime():
    unformated_currentTime = datetime.now()
    formated_currentTime =  unformated_currentTime.strftime('%Y%m%d%H%M%S')

    return formated_currentTime