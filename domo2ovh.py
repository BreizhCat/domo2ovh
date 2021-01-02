import json
import ovh
import argparse

__FULL_PATH__ = './' # To be updated according to your needs

parser = argparse.ArgumentParser(prog="domo2ovh")
group = parser.add_argument_group(title="Basics Arguments")
group.add_argument("-i", "--ip",  help = "IP à mettre à jour", default=None, required = True)

args = parser.parse_args()

if args.ip:
    client = ovh.Client()

    with open(__FULL_PATH__ + 'conf.json') as param_data:
        data = json.load(param_data)

    result = client.get('/domain/zone/'+data['zone']+'/record', fieldType='A')
    if result[0]:

        result = client.put('/domain/zone/'+data['zone']+'/record/'+ str(result[0]), 
            target=args.ip,
        )