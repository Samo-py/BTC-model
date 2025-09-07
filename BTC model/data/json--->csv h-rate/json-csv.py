import pandas as pd
import json

with open('path') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df.to_csv('path', index=False)
