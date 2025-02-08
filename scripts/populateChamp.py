import requests
import time

headers = {"Authorization": "TOKEN xxx"}

if __name__ == "__main__":
    data = requests.get(
        "https://ddragon.leagueoflegends.com/cdn/15.3.1/data/en_US/champion.json"
    ).json()

    champs = data["data"]

    print("Starting to populate the database")

    for champ in champs.values():
        print(f"Processing {champ['name']}")

        id = champ["id"]
        name = champ["name"]
        key = champ["key"]
        image = champ["image"]["full"]
        sprite = champ["image"]["sprite"]
        title = champ["title"]

        tags = champ["tags"]
        par_type = champ["partype"] if champ["partype"] != "" else "None"

        fr_data = requests.get(
            "https://ddragon.leagueoflegends.com/cdn/15.3.1/data/fr_FR/champion/"
            + id
            + ".json"
        ).json()["data"][id]

        fr_name = fr_data["name"]
        fr_title = fr_data["title"]
        fr_lore = fr_data["lore"]

        fr_tags = fr_data["tags"]
        fr_par_type = fr_data["partype"]

        en_data = requests.get(
            "https://ddragon.leagueoflegends.com/cdn/15.3.1/data/en_US/champion/"
            + id
            + ".json"
        ).json()["data"][id]

        lore = en_data["lore"]

        for i, tag in enumerate(tags):
            req_t = requests.get(
                f"http://127.0.0.1:8000/game/api/tags/{tag}", headers=headers
            )
            if req_t.status_code == 404:
                req_test = requests.post(
                    "http://127.0.0.1:8000/game/api/tags/",
                    json={"name": tags[i], "fr_name": fr_tags[i]},
                    headers=headers,
                )

        req_p = requests.get(
            f"http://127.0.0.1:8000/game/api/partypes/{par_type}", headers=headers
        )
        if req_p.status_code == 404:
            req_test = requests.post(
                "http://127.0.0.1:8000/game/api/partypes/",
                json={"name": par_type, "fr_name": fr_par_type},
                headers=headers,
            )

        req = requests.post(
            "http://127.0.0.1:8000/game/api/champions/",
            json={
                "name": name,
                "fr_name": fr_name,
                "key": key,
                "image": image,
                "sprite": sprite,
                "title": title,
                "fr_title": fr_title,
                "lore": lore,
                "fr_lore": fr_lore,
                "tags": tags,
                "par_type": par_type,
            },
            headers=headers,
        )
        print(req.json())

        time.sleep(2)
