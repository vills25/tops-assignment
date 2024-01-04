from datetime import datetime

def log_file(Details):
    DateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open('log.txt','a')
    file.write(f"{DateTime}:{Details}\n")