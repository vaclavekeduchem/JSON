import json

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

def load_json_file(filename):
    f = open(filename, "r", encoding="utf-8")
    data = json.load(f)
    f.close()
    return data


if __name__ == "__main__":
    zaci = load_json_file("zaci.json")

    tabulka = ColorTable(theme=Themes.OCEAN)
    tabulka.field_names = ["Jméno", "Příjmení", "Třída"]

    for zak in zaci["zaci"]:
        tabulka.add_row([zak["jmeno"], zak["prijmeni"], zak["trida"]])

    print(tabulka.get_string())
