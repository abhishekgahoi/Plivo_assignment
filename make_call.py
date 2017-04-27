import plivo, plivoxml,time, json, requests, subprocess, string

""" script to make call, hang up and generate cdr"""
auth_id = "MAZDMXNDM0MTMWYTJKNJ"
auth_token = "ZDVhYTQ5YTViZmQ4ZTBmYWIyYTMzZDJiNWY2NTQ1"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'to': 'sip:abhishekgahoi170422055353@phone.plivo.com',    # The phone numer to which the call will be placed
    'from' : '1234567890', # The phone number to be used as the caller id
    'answer_url' : "https://s3.amazonaws.com/plivosamplexml/play_url.xml",
    'answer_method' : "GET", # The method used to call the answer_url
}

# Make an outbound call and print the response
code,response = p.make_call(params)

#print "about to print uuid"
print(str(response))

data = response

print data['message']
print data['request_uuid']
str2= data['request_uuid']


### call hang up #
time.sleep(5)
params = {'call_uuid': str2}

code,response = p.hangup_call(params)
print(str(response))

###generating CDR####
time.sleep(10)
params = {
    'call_uuid': str2 # The ID of the call
}

code,response = p.get_cdr(params)

print str(response)


