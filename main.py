import json

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes


def vypis_napovedu():
    print(f"1) Vypis žáku\t 2) Přidat žáka")


def nacist_json(soubor: str):
    s = open(soubor, "r", encoding="utf-8")
    data = json.load(s)
    s.close()
    return data


def vypis_tabulku():
    zaci = nacist_json("zaci.json")

    tabulka = ColorTable(theme=Themes.OCEAN)
    tabulka.field_names = ["Jméno", "Příjmení", "Třída"]

    for zak in zaci["zaci"]:
        tabulka.add_row([zak["jmeno"], zak["prijmeni"], zak["trida"]])

    print(tabulka.get_string())


if __name__ == "__main__":
    vypis_tabulku()
