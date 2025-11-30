from datetime import datetime

class WorkInMondeyError(Exception):
    pass

now = datetime.now()
weekday = now.weekday()
if weekday == 0:
    raise WorkInMondeyError("Not work in monday")


