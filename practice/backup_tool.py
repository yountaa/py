import os
import logging
import argparse
import shutil
import sys
##utility##
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


parser = argparse.ArgumentParser(description="[--source],[--dest]")
parser.add_argument("--source",required=True, help="Откуда бекапить")
parser.add_argument("--dest",required=True, help="Куда складывать")
args = parser.parse_args()

##ENV##
source = args.source
dest = args.dest
exception_suffix = [".yaml", ".yml", ".json", ".conf"]
count_copy_file = 0



##MAIN CODE##
if os.path.isdir(source):
  pass
else:
  logging.error(f"{source} не является папкой")
  sys.exit(1)


os.makedirs(dest, exist_ok=True)


logging.info(f"Начинаю бекап файлов из -> {source}")
content = os.listdir(source)
for file in content:
  file_name, suffix = os.path.splitext(file)
  if suffix in exception_suffix:
    shutil.copy2(os.path.join(source, file), os.path.join(dest, file + ".back"))
    count_copy_file += 1
logging.info(f"Конец бекапа данных -> {dest}")
logging.info(f"Файлов перемещено  -> {count_copy_file}")
