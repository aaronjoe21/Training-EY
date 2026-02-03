from datetime import datetime


def sort_dates(date_list: list) -> list:
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in date_list]
    dates.sort()
    return [d.strftime("%Y-%m-%d") for d in dates]


print(sort_dates(["2025-12-10", "2025-11-30", "2025-12-05"]))