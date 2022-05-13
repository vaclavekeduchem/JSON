from main import nacist_json
import json

if __name__ == "__main__":
    zaci = nacist_json("zaci.json")
    new_zaci = []
    for zak_id, zak in enumerate(zaci["zaci"]):
        new_zak = {"id": zak_id+1}
        new_zak.update(zak)
        new_zaci.append(new_zak)
    s = open("zaci.json", "w", encoding="utf-8")
    json.dump({"zaci": new_zaci}, s, ensure_ascii=False, indent=4)
    s.close()