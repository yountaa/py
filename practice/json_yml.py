import json
import yaml

def check_cfg (path):
    with open(path) as f:
        file_json = json.load(f)

    services = file_json.get("services", [])

    for line in services:
        if line.get("status", {}) == "down":
            restart = line.get("restart_count", 0)
            line["restart_count"] = restart + 1
            line["status"] = "restarting"

    with open("/home/swaga/repo/py/new_file.yaml", "w") as f:
        yaml.safe_dump(file_json, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    with open("/home/swaga/repo/py/new_file.json", "w") as f:
        json.dump(file_json, f, indent=2, ensure_ascii=False)

check_cfg("/home/swaga/repo/py/services.json")
