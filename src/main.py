from notion.client import NotionClient
from notion.collection import NotionDate
import datetime
import tokens

client = NotionClient(token_v2=tokens.token_v2)
cv = client.get_collection_view("https://www.notion.so/f8504b47212f4069b93f98d60009c5af?v=d151d277f22a45078c252e6e0ee30f99")
# print(cv.collection.get_rows())
for row in cv.collection.get_rows():
    print(row.Date)
new = cv.collection.add_row()
new.Class = "Math 20C"
new.Date = NotionDate(datetime.datetime(year=2020, month=9, day=12, hour=2, minute=0))


