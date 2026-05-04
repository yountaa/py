import subprocess

hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.254", "10.0.0.1"]
count_up = 0
count_down = 0
count_all = len(hosts)

for host in hosts:
    result = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        count_up += 1
        print(f"{host:<15} -> UP")
    else:
        count_down += 1
        print(f"{host:<15} -> DOWN")

print(f"Всего: {count_all} | UP: {count_up} | DOWN: {count_down}")
