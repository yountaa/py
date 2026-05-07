from pathlib import Path

path = Path(__file__).parent
archive = path / "archive"
list_suffux = []
mv_list = []

archive.mkdir(parents=True, exist_ok=True)
for file in path.iterdir():
  size = file.stat().st_size / 1024
  name = file.name
  suffix = file.suffix
  if suffix == ".log":
    list_suffux.append(f"{name:<10} - {size:.2f} kb")
    if size > 1:
      file.rename(archive/name)
      mv_list.append(f"{name:<5}")


result = "\n".join(list_suffux)
print(result)
result = ",".join(mv_list)
print(result)
