import praw

reddit = praw.Reddit(user_agent = 'Yasuo Tips',
                client_id='', client_secret='',
                username='', password='')


submission = reddit.submission(id='5c9wti') #get reddit thread




#This is suppossed to search the thread and find what the user input then print the comment with the word the user inputted.
champ = input("Who do you need help with?")
for comment in submission.comments.list():
    if comment.body.find(champ):
        try:
            print(comment.body)
        except AttributeError:
            pass

