SimpleChat
==========

A very basic no-frills web chat system built to enable conversing with users on basic mobile phones.

SimpleChat should work perfectly on just about any device with a "web browser". I very purposely do not use any javascript or cumbersome styling.

Yes, there are no push notifications, that's up to you to sort out. Poll the JSON URL to see if the remote user (party "b") has not  yet seen your latest message (See `seen_by_other_party`) and then send them a reminder via SMS, smoke signal etc.

If you create the chat you are Party A. Party A and B have different URLS. Party A is the host and knows both URLS. Party B sees a simplified version of the interface and does not know the Party A URL.  

* Hit /json/new/ to create a new chat with JSON feedback. 
* POST to `party_a_url` with a form parameter called `lines` with the message you wish to send. You'll get back a JSON response with the full chat log.

You can see a demo at http://www.underground.co.za/sc/

Feel free to send feedback to arbitraryuser@gmail.com