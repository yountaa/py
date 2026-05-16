import argparse
import yaml
import requests
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s | %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

def load_config(path):
  try:
    with open(path) as f:
        file_yaml = yaml.safe_load(f)
        return file_yaml["services"]
  except FileNotFoundError as e:
      logging.error(f"Файл не найден. {e}")
  except PermissionError as e:
      logging.error(f"Недостаточно прав для доступа к файлу. {e}")
  except OSError as e:
      logging.error(f"Ошибка файловой системы: {e}")



def check_service( url, name="service", timeout=5):
  list_new = []
  count_up = 0
  try:
    response = requests.get(url=url)
    response.raise_for_status()
    count_up += 1
    list_new.append({"name": name, "url": url, "status": "UP"})
    return count_up , list_new
  except requests.exceptions.RequestException :
    list_new.append({"name": name, "url": url, "status": "DOWN"})
    return count_up , list_new

def check_all_service(services, timeout=5):
  count_up = 0
  list_new = []
  for service in services:
    total_up, all_results = check_service(url=service["url"],name=service["name"])
    count_up += total_up
    list_new += all_results
  return count_up, list_new



def main():
  logging.info("запуск скрипта")
  parser = argparse.ArgumentParser(description='Чекер сервисов')
  parser.add_argument("--path",required=True, help="path to file")
  args = parser.parse_args()
  path_main = Path(args.path)

  if path_main.is_file() and path_main.suffix in (".yaml", ".yml"):
      file = load_config(path_main)
      count_up, list_new = check_all_service(file)
      print("--summary--")
      for result in list_new:
        print(f"{result['name']} — {result['status']}")
      print(f"Общее колличество рабочих сервисов : {count_up}")
      logging.info("окончание скрипта")
  else:
      logging.error(f"Введен не путь к файлу или файл не .yml")

if __name__ == "__main__":
    main()
