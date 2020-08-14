import json
from datetime import datetime

now = datetime.now().replace(microsecond=0)
timestamp = now.timestamp()
filename = f"{str(timestamp).split('.')[0]}.json"

x = {'datetime': str(now), 'timestamp': str(timestamp)}

with open(f'data/{filename}', mode='w', encoding='utf-8') as fp:
    json.dump(x, fp)

print(f'Results written to file: data/{filename}')
