import argparse
import re
import logging
import json

##ENV##
logging_path = "/home/swaga/py/logs/analyzer.log"
logging_level_file = "DEBUG"
logging_level_console = "INFO"

##Аргументы для запуска cli##
parser = argparse.ArgumentParser(description=f"add'[--log_level],[--path]'")
parser.add_argument("--log_level",default="WARNING", help="level для выполнения скрипта , def=WARNING")
parser.add_argument("--path",required=True , help="укажи путь к файлу")
args = parser.parse_args()
logging_level_console = args.log_level
file_path = args.path

##Логирование##
logger = logging.getLogger("main")
logger.setLevel(level="DEBUG")
fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

console = logging.StreamHandler()
console.setLevel(level=f"{logging_level_console}")
console.setFormatter(fmt)

file = logging.FileHandler(filename=f"{logging_path}")
file.setLevel(level=f"{logging_level_file}")
file.setFormatter(fmt)

logger.addHandler(console)
logger.addHandler(file)




##MAIN CODE##

count_error = 0
hosts = []
details = []
reports = {}
logger.debug("Запуск скрипта")
logger.info("Пытаемся прочитать файл")

try:
  with open(file=file_path,mode="r") as f:
    for line in f:
      match = re.search(pattern=r"ERROR|CRITICAL", string=line)
      if match:
        parsed_log = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+?) (?:on|from|to) (\d+\.\d+\.\d+\.\d+)", line)
        count_error += 1
        hosts.append(parsed_log.group(4))
        details.append({
                      "ip": parsed_log.group(4),
                      "level": parsed_log.group(2),
                      "message": parsed_log.group(3)
                      })

  reports["total_errors"] = count_error
  reports["hosts"] = hosts
  reports["details"] = details

  try:
    with open("/home/swaga/py/utility/reports.json", "w") as f:
      json.dump(reports, f, indent=2, ensure_ascii=False)
      logger.info("Данные записаны в файл /home/swaga/py/utility/reports.json")

  except FileNotFoundError:
    logger.critical("Файл не найден для записи")

except FileNotFoundError:
  logger.critical("Файл не найден для чтения , введите правильный путь")

logger.debug("Конец работы")
