import time
import praw
already_done = []

def is_comment(submission):
        answered = 0
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        if len(flat_comments)<= 0:
                return False
        else:
                for comment in flat_comments:
                        if comment.author.name <> submission.author.name:
                                answered = 1
        elif answered <> 1:
                return False

                        
f = open('posts.txt', 'r')
for line in f:
        already_done.append(line)
f.close()
r = praw.Reddit('Shadow ban scraper'
                'https://www.github.com/thebombadier/shadowban')

r.login('username','password')
print 'Logged in'


while True:
        sub = r.get_subreddit('shadowbanned')
        for submission in sub.get_new(limit=10):
                done = submission.id +'\n'
                if done not in already_done:
                        speak = 'You are not shadow banned -  still not convinced click [here](http://shadowbancheck.appspot.com/)'
                        try:
                                if is_comment(submission) == False:
                                        submission.add_comment(speak)
                                        print 'Replied to submision by ' + submission.author.name
                                        id = submission.id
                                        already_done.append(id)
                                        with open('posts.txt', 'a') as file:
                                                file.write(id + '\n')
                                        f.close()
                                        print id + ' added to posts.txt'
                                        time.sleep(300)
                                else:
                                        print "Post has already been answered"
                                
                        except praw.errors.RateLimitExceeded as error:
                                print '\tRatelimit exceeded, Sleeping for %d seconds' % errors.sleep_time
                                time.sleep(errors.sleep_time)
                else:
                        print submission.id + " - This post has already been commented on"
                        

                        
        print 'Resting..'
        time.sleep(1800)
        print 'Starting again'
