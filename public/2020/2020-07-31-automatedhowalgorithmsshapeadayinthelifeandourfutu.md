---
title: "Automated: how algorithms shape a day in the life and our future"
subtitle: "The goal of the algorithm is not to give users content they like, but to make the users more predictable. Brief added comment on online courses."
date: 2020-07-31
type: newsletter
audience: everyone
visibility: public
post_id: 787586.automated-how-algorithms-shape-a
email_sent_at: 2020-07-31T13:00:55.124Z
---
I figured the logical followup on my analysis of recommender systems from last week ([it's worth a read](https://democraticrobots.substack.com/p/recommendations-are-a-game-a-dangerous)) would be a walkthrough of what I can learn about the algorithms that affect you and me, ***at a low level***. This is a survey with some specific metrics companies use and a high-level analysis of themes I found. Mostly, else it turn into a full length research paper, this article is a distillation of articles I found into digestible bites, with the links to read more if you're interested in a particular player.

Upon doing this research, there are way more points of algorithmic interaction then I expected --- I mean that algorithms can touch us and interact in more ways than we expect. Someone should study the *game-theory of algorithmic competition* within human brains. How does TikTok's algorithm help it hold onto users that Youtube may pull? Hopefully this is a starting point if people want to figure out how an app works.

*If you want to get the most value out of this post, click a couple links.*

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/fb77ad5d-f874-496c-afac-37cc256bc1e3_7443x4500.png)

A **general theme** of recommender systems and these platforms is: *if we can predict what the user wants to do, then we can make that feature into our system.*

The **general problem** formulation is: *how compounding interactions change how we act and can harm our well-being.*

# The core players

Facebook, Apple, Amazon, Netflix, and Google (FAANG) are often the most coveted companies to work for, and they have an outsized effect on the population of the world. This article does not go into all the geopolitical and ethical issues of the companies, it just tries to show how they work, a bit.

#### Facebook

The algorithm is designed to show individuals things in their circles, and get them to engage with it. This considers the contents' sources, the geographic location of the user, the social position of the user, the history of user engagements, paid advertisements, and more. The algorithm has been studied well enough to realize it has a dramatic effect, but conditioning on any one input is impossible, hence common references as a dangerous **black box**. A second-order effect of this is that the algorithms end up predicting which circle you are in, and guiding you to the middle of it (sometimes called polarization if your circle was a moderate, to begin with).

*I use Instagram off and on, and the biggest effect is likely to drive me to try and glamorize my life, but thankfully I consider the effects minor.*

\[Sources: [WSJ](https://www.wsj.com/articles/how-facebooks-master-algorithm-powers-the-social-network-1508673600), [WSJ2](https://www.wsj.com/articles/facebook-knows-it-encourages-division-top-executives-nixed-solutions-11590507499), [Verge](https://www.theverge.com/2020/5/26/21270659/facebook-division-news-feed-algorithms), [Facebook AI](https://www.facebook.com/business/news/good-questions-real-answers-how-does-facebook-use-machine-learning-to-deliver-ads/)\]

#### Twitter

The algorithm is like Facebook's, but more prone to vitality --- especially for users that start with a large audience. From Twitter itself, it considers the following features:

> The Tweet itself: its recency, presence of media cards (image or video), total interactions (e.g. number of Retweets or likes)
>
> The Tweet's author: your past interactions with this author, the strength of your connection to them, the origin of your relationship
>
> You: Tweets you found engaging in the past, how often and how heavily you use Twitter

Honestly, this doesn't say much. Given Twitter's quirks, I could see them having an obscure end-to-end optimizer and not many controls.

*I am definitely addicted to the knowledge vitality and access to other intellectuals on Twitter. These blue notification bubbles get me.*

\[Sources: [Sprout Social](https://sproutsocial.com/insights/twitter-algorithm/), [Twitter Blog](https://blog.twitter.com/engineering/en_us/topics/insights/2017/using-deep-learning-at-scale-in-twitters-timelines.html), [Hootsuite](https://blog.hootsuite.com/twitter-algorithm/) - a social media marketing company\]

#### YouTube

A mysterious entertainment platform upon closer inspection. While governed by a public American company, there have been multiple studies showing recommendations tracking pathways to radicalization (See NYT below) and even showing children troubling material (NYT2). The wealth of content available makes series' of recommendations incredibly depth and impactful. I would like to see more public insight, now that the [company is competing with TikTok](https://www.theverge.com/2020/4/1/21203451/youtube-tiktok-competitor-shorts-music-google-report).

*I consume a lot of my casual content on Youtube. I think that watching Joe Rogan clips has gotten me some Trump ads (Yes dramatically more for Biden), but it makes me think about how the videos I am watching can drift.*

\[Source: [NYT](https://www.nytimes.com/interactive/2019/06/08/technology/youtube-radical.html), [NYT2](https://www.nytimes.com/2017/11/04/business/media/youtube-kids-paw-patrol.html), [Shopify](https://www.shopify.com/blog/youtube-algorithm) - yes they analyze the Youtube algorithm?\]

#### Google

As the first widely useful search engine, everyone uses Google. Google uses a variety of tools to index webpages (see [PageRank](https://en.wikipedia.org/wiki/PageRank) as the origin) including text, links to other pages, history of readers on the site, and more. Its hand in the dissemination of information is crucial, and I worry that it has biases that are impossible to track.

Their position is now more precarious in the context of [anti-trust hearings](https://www.nytimes.com/2020/07/28/technology/amazon-apple-facebook-google-antitrust-hearing.html) and competitors. In recent years, Google shifted its results to include many more ads and self-referencing results (especially in profitable searches like travel and shopping). This self-referencing is what I see as a competitive angle against Google.

*Google controls how I find other academic papers, blogs, news, and more. I don't know how to measure the effects beyond big.*

\[Source: [WSJ](https://www.wsj.com/articles/how-google-interferes-with-its-search-algorithms-and-changes-your-results-11573823753), [The Mark Up](https://themarkup.org/google-the-giant/2020/07/28/google-search-results-prioritize-google-products-over-competitors), [Search Engine Journal](https://www.searchenginejournal.com/google-algorithm-history/)\]

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/61bbdc4c-ad81-4358-841a-d14afbce25fe_2647x1231.png)

# The coming players

These are areas where I see algorithms coming into play in new ways, and particularly in ways that may disadvantage some and or have deleterious effects.

#### News

Classical media shifting online (New York Times, Wall Street Journal, etc.) and new online-only publications (Medium, etc.) will corral our political and global world views. Clickbait has shifted into reading time, but that changes from a clickbait title to a clickbait title + a readbait introductory paragraph. I saw the effects of this in my own Medium articles - my writing was being tuned to the algorithm (and it worked - tutorials, code examples, and lists get more views than in-depth analysis). The reading population of the world is re-emerging on Substack (and other platforms - such as [context is recent events](https://nymag.com/intelligencer/2020/07/andrew-sullivan-see-you-next-friday.html)).

Beyond clickbait, the New York times is beginning to use research engagement algorithms on the news platform(specifically, something called contextual bandits - [context in research](http://proceedings.mlr.press/v32/agarwalb14.pdf)). To be blunt, when I read the news I want to read the events with minor added opinions. I do not want control over how I receive national and global news, but it is an expected development.

*Medium drove me away from clickbait to Substack (here). I am subscribing to more newsletters and could see myself unsubscribing from NYT and WSJ if trends continue too far. The picture of America being ruined solely by Trump is too narrow-minded from me and not giving me a broad enough education.*

\[Sources: [NYT](https://open.nytimes.com/how-the-new-york-times-is-experimenting-with-recommendation-algorithms-562f78624d26)\]

#### Shopping

Amazon wants to be the go-to search engine for shopping. They are expanding into many different areas of shopping (e.g. groceries, retail, and more soon) to get a bigger picture of individuals needs. When you ask Alexa to remind you of something, that could be recorded too. These form a multi-modal recommender system for ads and sales.

Facebook created a new marketplace to try and fight Amazon's rule. Facebook wants to be a middle man with Shopify (Shopify isn't an Amazon competitor without other companies) and vendors to create a platform where people can buy anything. With differing incentives (financials), it will be interesting to see how this plays out.

*I have taken steps to use Amazon much less. Its recommendations are weird, is filled with duplicate content, but is still incredibly convenient. The prospect of the Facebook marketplace makes me think of a more automated customer-vendor connection.*

\[Sources: [Recipe](https://www.repricerexpress.com/amazons-algorithm-a9/) [Express](https://www.repricerexpress.com/amazon-a10-algorithm-updates/), [Axios](https://www.axios.com/facebook-shops-online-marketplace-569242f4-da58-4f9b-8036-c21dca03a66b.html), [Sellics](https://sellics.com/blog-amazon-seo/)\]

#### Services

New applications are coming to offer value across many areas: including financial market access, customer analysis, ride-sharing, and more. These services will have less public oversight, to begin with, but time will show that multiple of them will have extremely harmful algorithmic effects. I include services in the coming players because the timescale from adoption to problem will be very short (apps can explode in usership, [see the example of Zoom](https://www.theverge.com/2020/4/23/21232401/zoom-300-million-users-growth-coronavirus-pandemic-security-privacy-concerns-response)). The negative metrics usually lag behind adoption, except in the example of the [least thought through service maybe ever](https://twitter.com/_alialkhatib/status/1288179135211114497).

\[Sources: [UC Berkeley on Fintech](https://faculty.haas.berkeley.edu/morse/research/papers/discrim.pdf), [Genderfying AI Fail](https://twitter.com/_alialkhatib/status/1288179135211114497), [GIG Economies](https://www.newscientist.com/article/2246202-uber-and-lyft-pricing-algorithms-charge-more-in-non-white-areas/#:~:text=The%20algorithms%20that%20ride%2Dhailing,to%20create%20a%20racial%20bias.&text=%E2%80%9CBasically%2C%20if%20you're,your%20ride%2C%E2%80%9D%20says%20Caliskan.)\]

# Second order effects

These are current applications that are undiscussed and deserve to be questioned on possible side effects (of initially positive applications).

#### Consumer devices

Apple watches attempting to detect atrial fibrillation for their users opens a huge problem of false-positives (see StatNews below). Technology companies will without a doubt attempt to add more features to their devices, and with a market penetration of millions of users, the inevitable false positive rate will have potential medical and financial implications. The compounding effect of these devices and misleading datapoints is left to be observed in the 2020s - with the uninformed most at risk.

\[Sources: [Apple](https://machinelearning.apple.com/research/learning-with-privacy-at-scale), [StatNews](https://www.statnews.com/2019/01/08/apple-watch-iffy-atrial-fibrillation-detector/#:~:text=In%20people%20younger%20than%2055,79.4%20percent%20of%20the%20time.), [Oura](https://ouraring.com/wvu-rockefeller-neuroscience-institute-and-oura-health-unveil-study-to-predict-the-outbreak-of-covid-19-in-healthcare-professionals)\]

#### Public medical / health tools

There are many new companies in the health space, such as Strive.ai that'll analyze workouts and Bloodsmart.ai that'll analyze blood tests to give you a health score (based on normalized, age-adjusted risk of death). This is preliminary, but gamifying one's health is coming. Only a few steps after Apple's "fill the rings" watch campaign is health-dashboards telling users how their habits may be numerically shortening their life.

*I don't use that many trackers now, but simply having a readout of estimated calories on my watch caused me to be self-conscious of eating too much when not working out in a day. This problem would be compounded with noisy readings on blood-markers or emotional well-being.*

\[Sources: [Strive](https://strive.ai/2020/03/keep-up-with-strive-ai/), [Bloodsmart](https://bloodsmart.ai/)\]

<div>

------------------------------------------------------------------------

</div>

# Isn't this a robotics blog?

Everything we have said in the last two iterations of Democratizing Automation regarding recommenders and algorithms will apply to robotic systems in the next decade. I forecast a dramatic increase in the penetration of robotic-human interaction with the incentives of the robots governed (for the most part) by big technology companies (informed by [some research](https://democraticrobots.substack.com/p/10-years-of-automation-in-1-year)).

The few smaller companies making personal robots may seem more exciting (e.g. [Hello Robotics](https://hello-robot.com/)), but that market share will be relatively small to start with (high-cost) while many companies can afford to replace the human cashier and salesperson with an embodied autonomous agent.

[I made a resource](https://github.com/natolambert/robot-ethics-books) tracking when these algorithms go wrong and some philosophical background.

<div>

------------------------------------------------------------------------

</div>

# Hop on or Fizzle out (in education)

Universities are going to quickly fall behind with online courses if they don't innovate. Translating university courses in their current form online will not be sustainable. After teaching a section the other day with 13 participants that took 15minutes to speak up in a form other than the Zoom chat box, I realized things have to change. For reference, I say 1.5 students were conversing with me for the rest of the section. It was pretty much an open room tutoring session that was recorded for people to watch later. Bizarre. This extends to lecture, but becomes an even more challenging question: Should lectures have variable lengths based on content? Some long form and some short form? *Please chime in if you have ideas.*

Engagement with no socialization will be the death of how colleges used to operate. I have some more solutions to offer:

1.  Compulsive attendance-based grading metrics. In my piece *[online courses, automating education, and digitalizing degrees](https://democraticrobots.substack.com/p/online-courses-automating-education),* I talked about the s**ynchronicity vs coverage problem** and how universities will try to accomodate global students --- this won't work without an outlay of resources. Students need to be given set times where they can engage in small groups.

2.  Less time teaching, more time making. In a traditional class, there are 3-9 staff members that teach roughly the same material every week. In an online only course, this number should reduce to 1-2 teaching staff and the rest creating engaging content. I propose having people spend 2-3 weeks creating an instructive lab material ([Jupyter notebook](https://jupyter.org/) or something similar) and having most students continue to watch the recordings.

[](https://substackcdn.com/image/fetch/$s_!WXx2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22339704-6f61-4cdb-9998-5eb0f7590a9c_768x1024.jpeg){.image-link .image2 .is-viewable-img component-name="Image2ToDOM" target="_blank"}

::::::: image2-inset
![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/22339704-6f61-4cdb-9998-5eb0f7590a9c_768x1024.jpeg){.sizing-normal attrs="{\"src\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/22339704-6f61-4cdb-9998-5eb0f7590a9c_768x1024.jpeg\",\"srcNoWatermark\":null,\"fullscreen\":null,\"imageSize\":null,\"height\":1024,\"width\":768,\"resizeWidth\":null,\"bytes\":161700,\"alt\":null,\"title\":null,\"type\":\"image/jpeg\",\"href\":null,\"belowTheFold\":true,\"topImage\":false,\"internalRedirect\":null,\"isProcessing\":false,\"align\":null,\"offset\":false}" height="1024" loading="lazy" sizes="100vw" srcset="https://substackcdn.com/image/fetch/$s_!WXx2!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22339704-6f61-4cdb-9998-5eb0f7590a9c_768x1024.jpeg 424w, https://substackcdn.com/image/fetch/$s_!WXx2!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22339704-6f61-4cdb-9998-5eb0f7590a9c_768x1024.jpeg 848w, https://substackcdn.com/image/fetch/$s_!WXx2!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22339704-6f61-4cdb-9998-5eb0f7590a9c_768x1024.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!WXx2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22339704-6f61-4cdb-9998-5eb0f7590a9c_768x1024.jpeg 1456w" width="768"}

:::::: image-link-expand
::::: {.pencraft .pc-display-flex .pc-gap-8 .pc-reset}
::: {.pencraft .pc-reset .icon-container .restack-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1yZWZyZXNoLWN3IiBmaWxsPSJub25lIiBoZWlnaHQ9IjIwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zIDEyYTkgOSAwIDAgMSA5LTkgOS43NSA5Ljc1IDAgMCAxIDYuNzQgMi43NEwyMSA4IiAvPjxwYXRoIGQ9Ik0yMSAzdjVoLTUiIC8+PHBhdGggZD0iTTIxIDEyYTkgOSAwIDAgMS05IDkgOS43NSA5Ljc1IDAgMCAxLTYuNzQtMi43NEwzIDE2IiAvPjxwYXRoIGQ9Ik04IDE2SDN2NSIgLz48L3N2Zz4=){.lucide .lucide-refresh-cw}
:::

::: {.pencraft .pc-reset .icon-container .view-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1tYXhpbWl6ZTIiIGZpbGw9Im5vbmUiIGhlaWdodD0iMjAiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgdmlld2JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBvbHlsaW5lIHBvaW50cz0iMTUgMyAyMSAzIDIxIDkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIHBvaW50cz0iOSAyMSAzIDIxIDMgMTUiPjwvcG9seWxpbmU+PGxpbmUgeDE9IjIxIiB4Mj0iMTQiIHkxPSIzIiB5Mj0iMTAiPjwvbGluZT48bGluZSB4MT0iMyIgeDI9IjEwIiB5MT0iMjEiIHkyPSIxNCI+PC9saW5lPjwvc3ZnPg==){.lucide .lucide-maximize2}
:::
:::::
::::::
:::::::

### **The tangentially related**

I am reading (newsletters/blogs):

-   [A brief history of deep learning's rocket trajectory into commonplace](https://dennybritz.com/blog/deep-learning-most-important-ideas/).

-   [How neural networks can cheat if you give them shortcuts in the data.](https://thegradient.pub/shortcuts-neural-networks-love-to-cheat/)

-   [Random Americans getting unmarked seeds from China.](https://www.wsj.com/articles/federal-officials-testing-mystery-seeds-mailed-to-u-s-residents-11595978122?mod=hp_lead_pos12) Uhm, please don't plant these. Crazy to follow, though.

Books:

-   *White Fragility -* Robin DiAngelo. It's not about you feeling bad for saying something they interpreted as racist, it's about you changing and understanding you are part of the system. Try to be better every day.

I am listening to / watching:

-   [The Drive - Peter Attia with Azra Raza](https://peterattiamd.com/azraraza/), "Why we're losing the war on cancer." Treatments for metastatic cancer have not improved life expectancy since the 1930s. We have improved early detection and prevention, but once people have serious cancer, research has not solved that (even with over \$250Billion spent on research). We need to rethink how cancer research is done.

<div>

------------------------------------------------------------------------

</div>

Hopefully you find some of this interesting and fun. You can find more about the author [here](http://www.natolambert.me/). Tweet at me [\@natolambert](https://twitter.com/natolambert), email [democraticrobots@gmail.com](mailto:%20democraticrobots@gmail.com). I write to learn and converse. Forwarded this? [Subscribe here](https://democraticrobots.substack.com/).
