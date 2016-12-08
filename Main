"""
This bot is meant to search /r/YasuoMains or Matchup thread in that subreddit
for the champion the user typed in then print the comment(or link it?). In the
future it will be able to search a site (try op.gg) and display the runes,
masteries, or builds if asked with the highest win rate. Maybe later have an
option to search the subreddit for tips or op.gg for builds and things so the
bot doesn't do both if the user only wants one of the two.
"""

import praw

reddit = praw.Reddit(user_agent = 'Yasuo Tips Comment Scraper 1.0 for YasuoMains. Contact me at /u/Dfree35 or ',
                client_id='', client_secret='',
                username='', password='')


submission = reddit.submission(id='5c9wti') #get reddit thread


#for top_level_comment in submission.comments.list(): #only get the top comment of the thread so needs to change!!!!!!!!!
#    #In comment body try to find what the user inputs, make the input lowercase, and start at the beginning of the comment i.e. "> -1"
#    if top_level_comment.body.find(input("Who do you need help with?")): ###if input('dw?).lower()' in comment.body
#        print(str(top_level_comment.body)) #print the comment that is matched as a string???


#This is suppossed to search the thread and find what the user input then print the comment with the word the user inputted.
#Right now I think it just prints a random comment, I cant remember and can't check until tonight.
champ = input("Who do you need help with?")
for comment in submission.comments.list():
    if comment.body.find(champ):
        try:
            print(comment.body)
        except AttributeError:
            pass

