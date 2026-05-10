import subprocess

disk_used = subprocess.run(
            ["df","-h"],
            capture_output=True,
            text=True,
            )

lines = disk_used.stdout.splitlines()
warned = False
for line in lines[1:]:
  parts = line.split()
  num_int = int(parts[4].strip("%"))
  if num_int > 80:
    warned = True
    print(f"[WARN] {parts[5]:<5} - {parts[4]:<5} (использует {parts[2]:<5} из {parts[1]:<5})")
  else:
    print(f"[OK] {parts[5]:<15} — {parts[4]}")

if not warned:
    print("[OK] Disk usage is normal")
