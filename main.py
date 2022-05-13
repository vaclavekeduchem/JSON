import json

from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes


def vypis_napovedu():
    print("1) Vypiš žáky\t 2) Přidat žáka\t 3) Vypiš žáka")


def nacist_json(soubor: str):
    s = open(soubor, "r", encoding="utf-8")
    data = json.load(s)
    s.close()
    return data


def vypis_tabulku(zaci: list):
    tabulka = ColorTable(theme=Themes.OCEAN)
    tabulka.field_names = ["ID", "Jméno", "Příjmení", "Třída"]

    for zak in zaci:
        tabulka.add_row([zak["id"], zak["jmeno"], zak["prijmeni"], zak["trida"]])

    print(tabulka.get_string())


def upravit_json(hodnoty: dict, zaci: list, soubor: str):
    zaci.append(hodnoty)
    s = open(soubor, "w", encoding="utf-8")
    json.dump(zaci, s, ensure_ascii=False, indent=4)
    s.close()


def vypis_zaka(zaci: list, id: int):
    print(zaci)



if __name__ == "__main__":
    zaci = nacist_json("zaci.json")
    while True:
        vypis_napovedu()
        match int(input("Vyberte jednu z možností: ")):
            case 1:
                vypis_tabulku(zaci["zaci"])
            case 2:
                upravit_json({"jmeno": input("Jméno: "), "prijmeni": input("Příjmení: "), "trida": input("Třída: ")},
                             zaci["zaci"], "zaci.json")
            case 3:
                vypis_zaka(zaci["zaci"], 1)
