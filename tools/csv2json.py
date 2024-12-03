import argparse

parser = argparse.ArgumentParser(description="Process a file.")
parser.add_argument("filename", help="The name of the file to process.")
args = parser.parse_args()
test_json = []
i = 0

with open('csv.json', 'w') as w:
    with open(args.filename, "r") as f:
        for line in f:
            if i > 0:
                details = line.split(',')
                card = {
                    "model": "bounty.card",
                    "pk": i,
                    "fields":{
                        "card_name": details[0],
                        "card_mp": details[1],
                        "card_rarity": details[2],
                        "card_desc": details[3],
                        "card_color": details[4],
                        "card_cost": details[5]
                    }
                }
                test_json.append(card)
            i += 1
    w.write(str(test_json).replace("'", '"'))