'''Read system.log and count:
number of ERROR lines
number of WARNING lines
#number of INFO lines
Write the summary into log_summary.txt .'''
count_error = 0
count_warning = 0
count_info = 0
try:
    with open("system.log", "r") as log_file:
        for line in log_file:
            if "ERROR" in line:
                count_error += 1
            if "WARNING" in line:
                count_warning += 1
            if "INFO" in line:
                count_info += 1
except FileNotFoundError:
    print("File NOT found.")
with open("log_summary.txt", "w") as log_file:
    log_file.write(f"System Log Summary\n")
    log_file.write(f"Number of ERROR lines: {str(count_error)}\n")
    log_file.write(f"Number of WARNING lines: {str(count_warning)}\n")
    log_file.write(f"Number of INFO lines: {str(count_info)}")
