from datetime import datetime

with open("logfile.txt", "a") as f:
    f.write(f"Log entry at {datetime.now()}\n")
