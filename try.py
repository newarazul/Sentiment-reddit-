import praw
from praw.models import MoreComments



reddit=praw.Reddit(
        client_id="ZY6pSfL-s1JT8g",
        client_secret="jhcaVn4-hD9sTOwcsQhLA6VFCsqERw",
        user_agent="sentiment_analysis"
)



def print_5_comments(submission):
    #get the best comments
    submission.comment_sort="best"
    #Limit to 5 comments
    submission.comment_limit=5
    for top_level_comment in submission.comments:
        submission.comment.replace_more(limit=0)
        print(top_level_comment.body)





for submission in reddit.subreddit("wallstreetbets").hot(limit=1):
        print(submission.title)
        print_5_comments(submission)




#        for comment in submission.comments.list():
#            print(submission.comment.list()[0].body)
#            submission.comments.replace_more(limit=0)
#            for top_level_comment in submission.comments:
#                print(top_level_comment.list()[0].body)

#print(call_number)






#def getAll(r, submissionId, verbose=True):
#  submission = r.submission(submissionId)
#  comments = submission.comments
#  commentsList = []
#  for comment in comments:
#    getSubComments(comment, commentsList, verbose=verbose)
#  return commentsList
