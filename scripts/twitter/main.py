import twitter
import os
from lcd import *
# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=''
consumer_secret=''
# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=''
access_token_secret=''

# Connection to twitter
init(CONTRAST)
gotoxy(0,0)
#text("Conectando a twitter")
api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
cmd_ip = os.popen("ifconfig eth0 | grep 'inet addr' | awk -F: '{print $2}' | awk '{print $1}'")
cmd_hora = os.popen(" uptime |awk '{print$1}'")
ip = str(cmd_ip.readline())
hora = str(cmd_hora.readline())
cmd_ip.close()
cmd_hora.close()
# If the authentication was successful, you should
# see the name of the account print out
gotoxy(0,1)
status = api.GetReplies()

user = str(status[0].user.screen_name)
tweet = str(status[0].text[10:int(len(status[0].text))])
id = int(status[0].id)
print id
text("u:" + user)
print "u:" + user + "\n"
gotoxy(0,2)
text("c:" +tweet)
print "c:" + tweet + "\n"
gotoxy(0,3)
if tweet == "ip":
	text("a:" + ip)
	print("a:" + ip)
	api.PostUpdate("@"+ user + " tengo la ip local: " + ip)
if tweet == "hora":
	text("a:" + hora)
	print("a:" + hora)
	api.PostUpdate("@"+ user + " son las: " + hora).SetInReplyToStatusId(id)