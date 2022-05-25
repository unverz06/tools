# Utilities
# Installation des dépendances Python
```bash
pip install pandas
pip install ciso8601
pip install scikit-learn
pip install python-binance
...
```
Check that all packages are installed
# Installation de l'env local
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
```
source env/bin/activate
```

# Exemple d'arborescence
```bash
Local
├── data
│   ├── BTCUSDT_DATA_2022_INTERVAL_5m.json
│   └── ETHUSDT_DATA_2022_INTERVAL_5m.json
├── engine
│   ├── function.py
│   └── head.py
├── crawler_multi.py # -- By Unverz06 --
├── import_data_sample.py # -- By Unverz06 --
└── support_resistance.py # -- By Skeletozaure — https://gist.github.com/skeletozaure --

# Notes
Utilisation simple avec MacOS et VSCODE