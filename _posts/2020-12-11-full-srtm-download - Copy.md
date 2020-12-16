---
layout: post
title:  "Download all SRTM 30m tiles"
date:   2020-12-11 20:00:51 +0200
categories: Technical
tags: [Remote Sensing]
---

There is a great site for the visualization of downloadable [SRTM 30m tiles](https://dwtkns.com/srtm30m/).

With a bit of F12 debug in chrome I found a [JSON file with all available SRTM data files](https://dwtkns.com/srtm30m/srtm30m_bounding_boxes.json)

Then it was just a matter of a simple Python script to download them all. (This is not a particular interest of mine but there might be a chance that I will use it sometime in the future)

I'm not sure why it isn't straight forward from the python requests module but I couldn't figure out both the Oauth and the basic http authentication. (I tried the scripts from the [official site](https://ladsweb.modaps.eosdis.nasa.gov/tools-and-services/data-download-scripts/) but they also didn't work, they are probably for downloading other standard products)

With Wget it just works.

{% highlight python %}
import requests
import json
import os.path
import os

data_path = r'path/to/data'
srtm_url = 'http://e4ftl01.cr.usgs.gov/MEASURES/SRTMGL1.003/2000.02.11/'
srtm30json_url = 'https://dwtkns.com/srtm30m/srtm30m_bounding_boxes.json'

ret = requests.get(srtm30json_url)
j = json.loads(ret.text)
srtm_tiles = [x['properties']['dataFile'] for x in j['features']]

print('downloading', len(srtm_tiles), 'SRTM files')
for i, srtm_tile in enumerate(srtm_tiles):
    if os.path.exists(os.path.join(data_path, srtm_tile)):
        continue
    print('download', i, '/', len(srtm_tiles), srtm_tile)
    os.system('wget --user <user> --password <password> ' + srtm_url + srtm_tile)
{% endhighlight %}
