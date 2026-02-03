from datetime import datetime, timedelta


def next_30_days() -> list:
    today = datetime.today()
    return [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)]

print(next_30_days())