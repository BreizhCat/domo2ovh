import json
import ovh
import argparse

parser = argparse.ArgumentParser(prog="domo2speak")
group = parser.add_argument_group(title="Basics Arguments")
group.add_argument("-i", "--ip",  help = "IP à mettre à jour", default=None, required = True)

args = parser.parse_args()

if args.ip:
    client = ovh.Client(
        endpoint='ovh-eu',               
        application_key='',   
        application_secret='', 
        consumer_key='',      
    )

    result = client.get('/domain/zone/breizhcat.fr/record', 
        fieldType='A'
    )

    if result[0]:
        result = client.put('/domain/zone/breizhcat.fr/record/'+ str(result[0]), 
            target='86.206.243.92',
        )