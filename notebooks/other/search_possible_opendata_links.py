import time
import pandas as pd
from tqdm import tqdm
from duckpy import Client

def search_opendatabot(school_name: str, max_retry: int=20) -> dict:
    """
    Search for school in opendatabot.ua
    """
    client = Client()
    opendatabot_url = ''
    retry = 0
    while not opendatabot_url and retry < max_retry:
        try:
            results = client.search(school_name.replace('"','').replace("'","")+ ' ЄДРПОУ', limit=20)
        except:
            time.sleep(20)
            continue
        for site in results:
            if site['url'].startswith('https://opendatabot.ua/c/'):
                opendatabot_url = site['url']
                break
        retry += 1
    return {'eoname': school_name, "url": opendatabot_url}

if __name__ == '__main__':
    # Load data
    unmatched_link = pd.read_csv('data/schools_bot.csv', dtype=str)
    unmatched_link = unmatched_link[unmatched_link['EDRPOU'].isna()]

    # Search for opendatabot links
    opendatabot_links_new = []
    for eoname in tqdm(unmatched_link['eoname']):
        opendatabot_links_new.append(search_opendatabot(eoname))
    
    # Save results
    opendatabot_df_new = pd.DataFrame(opendatabot_links_new)
    opendatabot_df_new[opendatabot_df_new.url!=''].to_csv('data/unmatched_link.csv', index=False)  