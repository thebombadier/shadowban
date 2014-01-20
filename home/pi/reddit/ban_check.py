praw.r.Reddit = ('Delete negative comments'
                 'url_goes_here'
                 )
      
def login(name,password):
  try:
    r.login(name,password)
  except:
    return "Couldn't Log in"
  
for comment in r.Redditor(user_name='godwin_finder').get_comments():
   
