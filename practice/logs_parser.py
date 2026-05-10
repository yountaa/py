import re

status_bad = 0

with open(file="/home/swaga/py/logs/logs_parser.log") as file:
  for line in file:
    match = re.search(r"ERROR|CRITICAL", line)
    if match :
      result = re.search(r"\d+\.\d+\.\d+\.\d+", line)
#      end_line = re.search(r"(ERROR|CRITICAL) (.+)", line)
      status_bad += 1
#      print(f"{ip_take:<10} - {end_line.group()}")
      print(f"{result.group():<15} — {match.group()} {line.strip()}")
print(f"Общее колличество ошибок в логе {status_bad}")
