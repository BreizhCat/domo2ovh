# domo2ovh

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Update IP on OVH DNS when my IP change.
Please refer to [Github OVH](https://github.com/ovh/python-ovh).

Test with Python 3.8.2

## HOW TO
```shell
usage: domo2speak [-h] -i IP

optional arguments:
  -h, --help      show this help message and exit

Basics Arguments:
  -i IP, --ip IP  IP à mettre à jour
```

## Example
```shell
python domo2ovh.py -i '127.0.0.1'
```

Please also update Python code with the folder where the configuration is `__FULL_PATH__`
And finally configure the configuration file `conf.json` by renamming the file `conf.json.model`
To configure application please read [this chapter](https://github.com/ovh/python-ovh#2-configure-your-application). You need to fill the file `ovh.conf` as explained.
```json
{
    "zone":"your_domain"
}
```
