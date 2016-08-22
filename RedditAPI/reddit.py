import praw
r = praw.Reddit(user_agent='simacna')
submissions = r.get_subreddit('bicycling').get_hot(limit=5)
print ([str(x) for x in submissions])

