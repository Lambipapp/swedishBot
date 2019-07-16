import logindetails
import praw
import os
import random
import time

def login():
    print("Account login")
    rInstance = praw.Reddit(
        username = logindetails.handle, 
        password = logindetails.pw,
        client_id = logindetails.cId,
        client_secret = logindetails.cSecret,
        user_agent = "bot v0.1"
    )
    return rInstance

def findPosts(rInstance, sub, prevPosts, commentTexts):
    print("searching posts")

    for post in sub.new(limit = 10):
        if "bekanta" in post.title and "fredag" in post.title and post.id not in prevPosts:
            reply = random.choice(commentTexts)
            print("replies: \"" + reply + "\" to post id: " + post.id)
            post.reply(reply)

            prevPosts.append(post.id)
            with open("prevPosts.txt", "a") as postFile:
                postFile.write(post.id + "\n")

def findComments(rInstance, sub, prevComments, commentTexts):
    print("searching comments")

    for com in sub.comments(limit=1000):
        if "aa" in com.body and "haha" in com.body and com.author != rInstance.user.me() and com.id not in prevComments:
            reply = random.choice(commentTexts)
            print("replies: \"" + reply + "\" to comment id: " + com.id)
            com.reply(reply)

            prevComments.append(com.id)
            with open("prevComments.txt", "a") as commentFile:
                commentFile.write(com.id + "\n")


def run(rInstance, prevComments, prevPosts, commentTexts):
    sweddit = rInstance.subreddit('sweden')
    findPosts(rInstance, sweddit, prevPosts, commentTexts)
    findComments(rInstance, sweddit, prevComments, commentTexts)
   

    print("search done")
    time.sleep(10)
    

def getPrevComments():
    if not os.path.isfile("prevComments.txt"):
        prevComments = []
        print("commentFile not found")
    else:
        print("commentFile found")
        with open("prevComments.txt", "r") as commentFile:
            prevComments = commentFile.read()
            prevComments = prevComments.split("\n")
            #prevComments = filter(None, prevComments)
    return prevComments

def getPrevPosts():
    if not os.path.isfile("prevPosts.txt"):
        prevPosts = []
        print("postFile not found")
    else:
        print("postFile found")
        with open("prevPosts.txt", "r") as postFile:
            prevPosts = postFile.read()
            prevPosts = prevPosts.split("\n")
            #prevPosts = filter(None, prevPosts)
    return prevPosts

commentTexts = ["aah, haha", "aah haha", "haha, aah", "haha aah", "haha ja", "ja haha", "ja, haha", "haha, ja"]
rInstance = login()
print("logged in to user: " + str(rInstance.user.me()))
prevComments = getPrevComments()
prevPosts = getPrevPosts()


while True:
    run(rInstance, prevComments, prevPosts, commentTexts)
