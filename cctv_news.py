import News as news
import News_all as allnews
import pandas as pd
import time, random
from datetime import date, timedelta

df = pd.DataFrame()
start_date = date(2022, 5, 23)
end_date = date(2022, 12, 31)

for i in range((end_date - start_date).days + 1):
    i = start_date + timedelta(days=i)
    i = i.strftime('%Y%m%d')
    try:
        dfi = allnews.find_title(i) #news是只取标题
        df = pd.concat([df, dfi])
        time.sleep(random.randint(0, 3))
        print(i)
    except Exception as e:
        print(f"Error occurred at date {i}: {e}")
        df.to_csv('news3.csv')
        break
df.to_csv('news_2022.csv')