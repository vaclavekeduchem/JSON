import json

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes


def vypis_napovedu():
    print("1) Vypiš žáky\t 2) Přidat žáka")


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


def upravit_json(hodnoty: dict, soubor: str):
    zaci = nacist_json(soubor)
    zaci["zaci"].append(hodnoty)

    s = open(soubor, "w", encoding="utf-8")
    json.dump(zaci, s, ensure_ascii=False, indent=4)
    s.close()


if __name__ == "__main__":
    while True:
        vypis_napovedu()
        match int(input("Vyberte jednu z možností: ")):
            case 1:
                vypis_tabulku()
            case 2:
                upravit_json({"jmeno": input("Jméno: "), "prijmeni": input("Příjmení: "), "trida": input("Třída: ")}, "zaci.json")
