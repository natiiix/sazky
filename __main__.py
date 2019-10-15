import sqlite3


def prompt(text):
    print(text + ": ", end="")
    value = input().strip()

    if not value:
        return None

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value.replace(",", "."))
    except ValueError:
        pass

    return value


if __name__ == "__main__":
    bets = []

    while True:
        name = prompt("Jméno")

        if not name:
            break

        bets.append((
            name,
            prompt("Kategorie"),
            prompt("Druh sázky"),
            prompt("Hodnota sázky"),
            prompt("Kurz"),
            prompt("Minimální kurz"),
            prompt("Výhra")
        ))

        print("--------------------------------")

    if not bets:
        exit()

    with sqlite3.connect("sazky.db") as conn:
        cur = conn.cursor()

        cur.executemany(
            'INSERT INTO sazky ("jmeno", "kategorie", "typ", "hodnota", "kurz", "min_kurz", "vyhra") VALUES (?, ?, ?, ?, ?, ?, ?);', bets)

        cur.close()
        conn.commit()

    print("OK; bye")
