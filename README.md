# Hi!

I'm Ola-Alt, and this is my attempt to create sort of a migration application for Blue Sky. I like following art, and
I also happen to be good at coding. So when I found it difficult to translate all the accounts I followed to Blue-Sky,
then I decided to use my skills to bridge that difficulty.

It resulted in something that honestly worked a little bit. However, around the same time I started disliking social
media as a whole and I kind of abandoned the project. It would be a shame to get rid of such a nifty account follower
though, so I am uploading it to GitHub in case anyone else wants to try their hand at improving it.

Right now, it supports loading accounts from an Instagram JSON file and a Twitter text file. The only real loader is the
Instagram JSON, as the Twitter text one is shabby. For context as to why, read my autistic ramblings in this Bsky
thread-

https://bsky.app/profile/ola-alt.bsky.social/post/3la2slwgt4f2b

And here as well, this is a part two to the above link-

https://bsky.app/profile/ola-alt.bsky.social/post/3la2wsk6e2w2k

But yeah. The one crucial thing that should really be fixed is the lack of input validation when entering the username
and password, but I have lost the interest to expand this project further. 

As a quick run through of the project:

* transfer_follows.py - the program the user would actually run to do the whole migration thing.
* Combine Followers.py - a test-ish file I made to combine copied Twitter accounts into one file to make it easier to
  pass to transfer_followers.py
* TopLevelUtils - a module with utilities used by the transfer script itself. What WAS supposed to be the entry point
  into more functionality, if I had bothered to build it.
* LoadingUtils - a module for specific loading methods. In this case, only JSON and TXT.
* Tests - a folder with tests for automated testing of specific functionality. If you have pytest you can run it on the 
  Tests folder to ensure everything works.

To try it, request your follower/following data from Twitter and Facebook and give it a whirl. Specifically for Twitter
though, don't do that and instead just copy directly off. To understand how to do that exactly, see the above links.

Alright, see you when I see you. :heart_emoji:
