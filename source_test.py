import config
import requests

Image_source_dict_new = config.Image_source_dict
for x in list(config.Image_source_dict.keys()):
    try:
        a = requests.get(config.Image_source_dict[x]+'/0/')
    except requests.RequestException:
        del Image_source_dict_new[x]
        continue
    if a.status_code != 200:
        del Image_source_dict_new[x]
