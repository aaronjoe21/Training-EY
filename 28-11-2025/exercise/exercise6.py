import datetime
def log_error(message):
    return (f"""ERROR -Log Date&Time: {datetime.datetime.now().strftime('%H:%M:%S')}
ERROR: {message}\n""")
with open("errorlog.txt", "a") as log:
    log.write(log_error("File not found"))
    log.write(log_error("Invalid User Input"))
    log.write(log_error("Timeout occurred"))
    log.write(log_error("Permission denied"))
    log.write(log_error("Database Error"))

