#this script calls the MailChimp API using the urllib2 python library
#parses out the subscriber count
#and outputs it to the terminal
#github @sugaroverflow

import urllib2
import json

url = 'YOUR MAIL CHIMP API CALL URL HERE'
#this is the API Call for the data for ALL of your account / including private stats and member names + emails
#the structure is something like: https://us11.api.mailchimp.com/3.0/lists/LISTID?apikey=APIKEYHERE for a particular list ID
#sometimes the us11 can be a different value (check your account)

response = urllib2.urlopen(url)
data = response.read()
json_data = json.loads(data)

subcount =  json_data['stats']['member_count'] #subscriber count variable

print "The subscriber count: " + str(subcount) #outputs to the terminal

#note the subcount is a int value
#you can return it in whatever form is meaningful to you
#for example if you just want the script to send you the integer value:
return subcount
