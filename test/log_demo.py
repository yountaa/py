import logging
import argparse
import subprocess

#ПЕРЕМЕННЫЕ В КОДЕ log_level - чреез arg
##Вынесли ввод уровня логирования##
parser = argparse.ArgumentParser(description=f"{{Передай}}'[--log_level]'")
parser.add_argument("--log_level",default="INFO", help="log_level дял выполнения скрипта")
args = parser.parse_args()

##Логирование##
logger = logging.getLogger("check_host")
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

console = logging.StreamHandler()
console.setLevel(args.log_level.upper())
console.setFormatter(fmt)

file = logging.FileHandler(filename="access.log")
file.setLevel(logging.DEBUG)
file.setFormatter(fmt)

logger.addHandler(console)
logger.addHandler(file)







##Основной скрипт##
hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.254", "10.0.0.1"]
count_up = 0
count_down = 0

logger.debug("Запуск проверки хостов")

for host in hosts:
    result = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
#        timeout=5
    )
    if result.returncode == 0:
        logger.info(f"{host:<15} -> UP")
        count_up += 1
    else:
        logger.error(f"{host:<15} -> DOWN")
        count_down += 1

logger.debug("Конец проверки хостов")
logger.info(f"После проверки всех хостов из списка , выяснилось :")
logger.info(f"Хостов онлайн : {count_up}")
logger.info(f"Хостов оффлай : {count_down}")
