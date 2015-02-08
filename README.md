# bgw-scraper
Quick and dirty script to scrape post data from /r/bikesgonewild on reddit using praw [python reddit api wrapper].

This is my first reddit scraper and I have had a lot of fun with it so far.

This little project was motivated by the question of what brands are best represented in the motorcycle subreddit /r/bikesgonewild where users show off their motorcycles. Having heard of the praw package, I set out to write a python script to get the data.

Since this is my first experience using praw, I think I have run into a couple issues with it and just interesting data analysis issues.
  - Clearly, my keywords are not exhaustive and my parsing method is simplistic. TODO: improve this. Also improving the list of nicknames and model names could be a good way to improve the proportion of posts counted in a brand category.
  - Ideally, I would like to get data from **ALL** of the posts from the sub, but it seems the limit is around 1000 per request.
  - Due to this limit on the sample size and time period (i.e. recent) I believe that I caught a "Yamaha" day that strongly biased my results toward Yamaha. These happen periodically and spontaneously on this sub. TODO: figure solution where can pull all posts from each month (say) iteratively (with multiple praw requests) to get larger sample.
  - I'd like to put together an IPython notebook with some visualizations soon.
