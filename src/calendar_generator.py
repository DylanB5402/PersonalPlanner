from notion.client import NotionClient
from notion.collection import NotionDate
import datetime
import tokens

client = NotionClient(token_v2=tokens.token_v2)
cv = client.get_collection_view(tokens.url)
# print(cv.collection.get_rows())
for row in cv.collection.get_rows():
    print(row.Date)
for x in range(5):
    new = cv.collection.add_row()
    new.Class = str(x)
    new.Date = NotionDate(start=datetime.datetime(year=2020, month=9, day=12, hour=2, minute=0), end =datetime.datetime(year=2020, month=9, day=12, hour=16, minute=0) )