import time
import json
from urllib.request import Request, urlopen


def get_art_uri(item):
    try:
        return item['image_uris']['art_crop']
    except:
        return item['card_faces'][0]['image_uris']['art_crop']


def main():
    # make the request
    req = Request(
        url='https://mtgjson.com/api/v5/AtomicCards.json', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    # download the json data
    cards = json.loads(urlopen(req).read())

    time.sleep(0.5)

    # req = Request(
    #     url="https://data.scryfall.io/oracle-cards/oracle-cards-20230128220300.json",
    #     headers={'User-Agent': 'Mozilla/5.0'}
    # )

    # scryfall_cards = json.loads(urlopen(req).read())
    
    time.sleep(0.5)

    req = Request(
        url="https://data.scryfall.io/unique-artwork/unique-artwork-20230128220408.json",
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    scryfall_images = json.loads(urlopen(req).read())
    image_map = {x['oracle_id']: get_art_uri(x) for x in scryfall_images if 'oracle_id' in x}


    # # filter to legal commanders
    commanders = list(filter(lambda x: x[1][0].get('leadershipSkills'), cards['data'].items()))
    
    # # get names and scryfall oracle ids
    savedata = list(filter(lambda x: x['image_uri'] is not None, map(lambda x: dict(name=x[0], image_uri=image_map.get(x[1][0]['identifiers']['scryfallOracleId'])), commanders)))

    # write the data we want to disk
    with open('src/lib/static/commanders.json', 'w') as f:
        json.dump(savedata, f)

    print(f"saved {len(savedata)} items")

if __name__ == "__main__":
    main()
