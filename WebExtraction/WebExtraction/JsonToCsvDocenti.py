import pandas as pd

class jsonToCsvDocenti(object):

    df = pd.read_json ('dettagliDocentiBocconi.json')
    df.to_csv ('dettagliDocentiBocconi.csv', index = None)