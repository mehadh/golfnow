# golfnow
GolfNow Giftcard Cracker

This checker was written in November of 2020. At the time, it was painfully easy to bruteforce giftcards from this website. Unlike my first publicly available checker, this one revealed far too much PII alongside the giftcards. Not only was the balance easily checked, but information that shouldn't be easily accessible, like email addresses, names, etc, were all easily exposed by the API. Due to this, I decided I would not upload this checker until the vulnerability was fixed. 

As of July 2021, it appears that the security loopholes have been mostly patched. It took the team quite a while, but kudos to them for resolving the issues. The API link has moved from the one mentioned in the main file to /api/check-balance and it now required a reCaptcha v2 to be filled out prior to submitting a request. Furthermore, the response given by the checker contains much less information now. 

Due to this, I am finally free to release this piece of code. Please bear in mind that it was only a proof of concept and not a finished product on the best way to create a checker. Additionally, as stated above, this tool is no longer able to crack GolfNow giftcards. The range number has also been stripped from the file. 
