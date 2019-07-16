# swedishBot
A reddit bot that answers "haha aah" and simular in a swedish subreddit

### What you need:
* Python3
* Praw
* A reddit account
  
### Startup:
1. Log in to the reddit account that the bot will post from.
2. Create a reddit app [here](https://www.reddit.com/prefs/apps/)
3. 
    * **Name** = swedishbot
    * **Type** = script
    * **redirect uri** = http://localhost:8080
4. Insert all data in the "logindetails.py" file.
    * clientSecret and clientID is found in the reddit app page [here](https://www.reddit.com/prefs/apps/)
5. *>python3 swedishbot.py*
