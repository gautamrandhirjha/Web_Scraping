import requests  # for fetching data
import re  # for string operations
import pandas as pd  # for creating excel

r = requests.get('https://dating.lovetoknow.com/dating-resources/new-relationship-quotes').text
r = r.split('<li>')
quotes = []
for i in r[1:]:
    quote = re.search('(.*?)<', i, re.S)  # returns an object
    if quote:
        quote = quote.group(1).replace('–', '').strip()
    if not re.search('[a-zA-Z]', quote):
        continue
    quotes.append(quote)
df = pd.DataFrame({'Val_Quotes': quotes})
df.to_excel('val_quotes2.xlsx', index=False)
df
