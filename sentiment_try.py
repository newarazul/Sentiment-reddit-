import praw
from praw.models import MoreComments
from DateTime import DateTime
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt


reddit=praw.Reddit(
        client_id="ZY6pSfL-s1JT8g",
        client_secret="jhcaVn4-hD9sTOwcsQhLA6VFCsqERw",
        user_agent="sentiment_analysis"
)






#top_level_comments=list(submission.comments)

words=[]
bull=0
bear=0
ratio=0
for submission in reddit.subreddit("wallstreetbets").hot(limit=1):
    print(submission.num_comments)
    print(submission.title)
#url="https://www.reddit.com/r/wallstreetbets/comments/kumvk6/what_are_your_moves_tomorrow_january_8_2021/"
#submission=reddit.submission(url=url)
#print(submission.num_comments)
    number=submission.num_comments
    submission.comment_sort="best"
    submission.comments.replace_more(limit=10)
    for comment in submission.comments.list():
        print(comment.body)
        words=comment.body.split(" ")
        for i in words:
            if i == "call" or i=="calls" or i=="moon" or i=="rise" or i=="up" or i=="buy" or i=="buying" or "long":
                print(i)
                bull+=1
            if i == "put" or i== "puts" or i=="drill" or i=="fall" or i=="down" or i=="sell" or i=="selling" or "short":
                print(i)
                bear+=1


print(bear)
print(bull)
ratio=bull/bear
#with open ("dump.dat", "w") as outfile:
#    outfile.write(bull+bear+ratio)


#make_pie_chart(bull,bear)


print("ratio", ratio)



#today=date.today()
#print(today)

#if you get an error after executing the code, try adding below. pd.core.common.is_list_like = pd.api.types.is_list_like
#start = datetime.datetime(2010, 1, 1)
#end = datetime.datetime(2020, 1, 27)
#SP500 = web.DataReader(['sp500'], 'fred', today, today)


#def print_to_file(name)
    

#f.write(number, ratio, "tuesday 12. January")
#f.close

#def make_pie_chart(bull,bear):
labels='Bull','Bear'
sizes=[bull/(bull+bear),bear/(bull+bear)]
    
fig, ax1=plt.subplots()
ax1.pie(sizes,labels=labels,shadow=True,startangle=90)
ax1.axis("equal")
plt.show()

