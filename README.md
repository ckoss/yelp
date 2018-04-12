# yelp

* Datensatz kann nun eingeladen werden mit:
```
from lib.data import load_df
df = load_df("path_to_yelp")

oder 

from lib import data
df = data.load_df("path_to_yelp")
```
Falls man sich in einem anderen Verzeichnis befindet, kann man den path zu data/race_by_postalcode.csv als kwarg anpassen: