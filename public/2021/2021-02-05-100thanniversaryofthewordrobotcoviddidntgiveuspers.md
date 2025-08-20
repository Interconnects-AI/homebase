---
title: "100th anniversary of the word robot: COVID didn’t give us personal robots, it gave us Woebot"
subtitle: "Yes COVID accelerated automated manufacturing and logistics, but robots have not been helping out en masse anywhere else. "
date: 2021-02-05
type: newsletter
audience: everyone
visibility: public
post_id: 32099849.covid-robots-and-woebot
email_sent_at: 2021-02-05T12:30:28.994Z
---
This is my second article focusing on COVID and robotics (the [first one](https://robotic.substack.com/p/10-years-of-automation-in-1-year) kickstarted this blog), and there is a clearer picture now. This article summarizes what has happened to the robotics industry in the first year of the COVID19 pandemic. 

The mainstream news collectively *hurrah'd* all aspects of the robotics and automation industry when the pandemic hit. This is not the case. In reality, robotic adoption following [everyone's favorite graph type](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fnatolambert%2FvL_ZOgDlv1.png?alt=media&token=8d254bbf-2e08-4b79-b93a-efad6131e0df) of 2020, but only in specific areas where there was already a base level of adoption.

For the rest of people's dreams with robots --- the home, the office, toys, etc. --- any uptake could be doing more harm than good. This could be the state of robotic reality further separating from everyone's sci-fi ideals. There is definitely a ton more to learn and explore in this space, and I plan to revisit more fundamentals of machine learning in autonomous systems soon, but in summary:

-   Robot sales in areas that were already used are rocketing up (e.g. manufacturing, some logistics),

-   Consumer-facing robots are still pretty atrocious, such as a mental-health bot called [WoeBot](https://www.cnbc.com/2020/11/11/people-with-depression-anxiety-want-to-reveal-pain-to-a-robot.html) (okay app, horrid name),

-   There has been an acceleration of investment that will play out in the next 2-5 years for more pervasive robots.

![Just a good boy.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/fb72579b-9d0b-46b0-b393-23eb1873fdac_6000x4000.jpeg)

<div>

------------------------------------------------------------------------

</div>

## R. U. R.

As a required aside, the 100th anniversary of the word robot passed us last week on January 25th. Anyone who is interested in robotics should know about [Karel Čapek](https://en.wikipedia.org/wiki/Karel_%C4%8Capek)'s play [Rossumovi Univerzální Roboti](https://en.wikipedia.org/wiki/R.U.R) (Rossum\'s Universal Robots), which was the origin of the word robot. 

The word robot was born and raised in sci-fi culture. As robots become mainstream, we could see the first major cultural redefinition of what it means to be an embodied intelligent agent.

*(More reading from [WSJ](https://www.wsj.com/articles/on-the-100th-anniversary-of-robot-theyre-finally-taking-over-11611378002%0A))*

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/f88ca0aa-9629-4bd1-a473-a7e5ca088e00_6000x4000.jpeg)

<div>

------------------------------------------------------------------------

</div>

## The news slew

Doing multiple news-roundups on keywords including `covid, robot, automation, ai, etc.` really shows anyone how little real development there is in this space from covid. For a general summary, you can read this [WSJ article](https://www.wsj.com/articles/remote-work-isnt-just-for-white-collar-jobs-anymore-11603371826?mod=article%5C_inline%0A) on how robots are aiding remote work in blue-collar jobs. 

#### Health & COVID

I had to start with the topic none of us can get away from. The articles being championed as massive successes for health administration or tools are hilarious.

First, the [class reporting from CNBC](https://www.cnbc.com/2020/11/11/people-with-depression-anxiety-want-to-reveal-pain-to-a-robot.html) gave us the title for this post and Woebot. Woebot is actually an app (sorry to mislead slightly, but their awful pun gives me permission to double down) that is an automated mental health companion. You can find more on the [app's homepage](https://woebothealth.com/), where it describes an offering of mindfulness techniques, cognitive and dialectal behavioral therapy, and more. They really needed a better name.

I am very skeptical of the long-term viability of automated therapy, but this app seems to be taking a reasonable approach: scaling up techniques and lessons of individual therapists. My criticism can best be summarized around the lens of out-of-distribution-data and the [GPT3 medical chatbot](https://artificialintelligence-news.com/2020/10/28/medical-chatbot-openai-gpt3-patient-kill-themselves/) that told a patient they should probably kill themselves.

COVID did not give us physical aids, it accelerated technology that was already accessible, such as specialized chatbots!

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/61266b1b-ea25-414c-8588-49a01b98e590_1224x524.png)

[Singapore debuted a robot](https://www.healthcareitnews.com/news/asia-pacific/clinicians-singapore-develop-robot-faster-covid-19-nasal-swabbing) for faster nasal swabbing during covid that *empowered the user by letting them terminate the process* (above). Who in their right mind is going to do that? It is almost as absurd that anyone wrote a news story praising this, let alone let a robot swab them. 

For a bit of *reasonable* robotics applications in healthcare, both [India](https://www.cnn.com/2020/11/11/tech/robots-india-covid-spc-intl/index.html) and [Rwanda](https://www.reuters.com/article/us-health-coronavirus-rwanda-robots/rwandan-medical-workers-deploy-robots-to-minimize-coronavirus-risk-idUSKBN2360EW) deployed basic robots (essentially teleconference robots) for patient check-in. 

#### The industry spike

The International Federation of Robotics released [their report for 2020](https://ifr.org/downloads/press2018/Presentation_WR_2020.pdf) with predictions on the robotic industry looking ahead at 2023. They break the report into industrial robots and service robots, which mirrors the dichotomy I am covering. They make it very clear from the start that these two modalities have "different customers, pricing, machinery, distribution, channels, and suppliers" --- they are different tracks of technological development.

Personal (service) robots year over year growth from 2019 into 2020 dropped from 34% to 15%. It seems to be a case of the technology is not ready for mainstream adoption and fell behind. There is no way to skip the hard engineering problems that have not been solved in human-robot interaction (HRI), which is crucial for at-home robots to be well received. There were clear paths taken to scale up the adoption of robots that already work. Eventually, these paths should converge.

#### Office cleaning

A surprising category because all the offices I know are closed. Doubly interesting because people do not know the ways that the virus really spreads (best guesses now are on airborne, which cleaning robots do not touch). 

The Verge covered some of the more formal coverage. The company [Breezy One](https://fetchrobotics.com/breezyone/) claims:

> This robot's going to be able to clean 200,000 square feet of office and conference rooms in two, maybe two and a half hours.

Does this check out? What is clean? What does HEPA filters alone do?

Additionally, [Bloomberg covered airport cleaning ](https://www.bloomberg.com/news/articles/2020-12-14/butler-on-wheels-robot-cutting-salad-how-covid-sped-automation)(only part of the article) and the [Office of Navy Research](https://www.radio.com/connectingvets/articles/military/robot-enters-fight-against-covid-19) decontamination robot gets the "at least you tried award."

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/9d035d07-1f32-4cc4-bf97-85cc8baf25ef_1648x896.png)

#### Miscellaneous

[Boston Dynamics's](https://robotic.substack.com/p/boston-dynamics) made a flashy appearance in [Singapore early in COVID enforcing social distancing rules](https://www.bbc.com/news/av/technology-52619568) (or in [video](https://www.youtube.com/watch?v=2DJmIjKtVkA)). 

[1,000,000 deliveries](%20https://medium.com/starshiptechnologies%0A) have been made on the automated delivery platform Starship. Something like this --- many small, slow, safe robots --- for last-mile delivery is what I want (say no to delivery drones, more on the [new FAA regulations](https://www.faa.gov/uas/advanced_operations/package_delivery_drone/) soon). Here is their [homepage](https://www.starship.xyz/).

![Me, wondering if I will ever get a robot to make me waffles.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/7b9ce59b-88e5-41f0-a01c-13d3c5242c3d_3482x3487.jpeg)

<div>

------------------------------------------------------------------------

</div>

## Snacks

I've paused the *Tangentially Related* newsletters, so I will include the best mentions at the bottom of each article whenever something recent warrants brief discussion.

### Thoughts

Things I have done related to Democratizing Automation.

-   I tweeted a robotic kitchen video, and some interesting conversation came about. Seems like these robots may be close to useful for fast food, but labor is still cheap.

::::::::: {.tweet attrs="{\"url\":\"https://twitter.com/natolambert/status/1355547870649348098\",\"full_text\":\"All the robotic kitchen startups are hilarious. This experience costs more than hiring a chef:\\n\\nI too like to do the most time consuming part of cooking (chopping) and then hand it off to something that is only partially competent to burn my dinner.\\n\\n\",\"username\":\"natolambert\",\"name\":\"Nathan Lambert\",\"date\":\"Sat Jan 30 16:06:11 +0000 2021\",\"photos\":[],\"quoted_tweet\":{},\"retweet_count\":2,\"like_count\":12,\"expanded_url\":{\"url\":\"https://www.youtube.com/watch?v=PvxrM0-qhlQ\",\"image\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/87f90cf5-066e-429e-961e-50fa3464d948_480x360.jpeg\",\"title\":\"The Moley Robotic Kitchen has arrived!\",\"description\":\"Visit http://www.moley.com/ to find out more about this innovative new domestic and commercial kitchen. The Future is Served. Thanks to the motion-capture sy...\",\"domain\":\"youtube.com\"},\"video_url\":null,\"belowTheFold\":true}" component-name="Twitter2ToDOM"}
[](https://twitter.com/natolambert/status/1355547870649348098){.tweet-link-top target="_blank"}

:::: tweet-header
![Twitter avatar for \@natolambert](https://substackcdn.com/image/twitter_name/w_96/natolambert.jpg){.tweet-header-avatar loading="lazy"}

::: tweet-header-text
[Nathan Lambert ]{.tweet-author-name}[\@natolambert]{.tweet-author-handle}
:::
::::

::: tweet-text
All the robotic kitchen startups are hilarious. This experience costs more than hiring a chef: I too like to do the most time consuming part of cooking (chopping) and then hand it off to something that is only partially competent to burn my dinner.
:::

[![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/87f90cf5-066e-429e-961e-50fa3464d948_480x360.jpeg){.expanded-link-img loading="lazy"}](https://www.youtube.com/watch?v=PvxrM0-qhlQ){.expanded-link target="_blank"}

::: expanded-link-bottom
[youtube.com]{.expanded-link-domain}[The Moley Robotic Kitchen has arrived!]{.expanded-link-title}[Visit http://www.moley.com/ to find out more about this innovative new domestic and commercial kitchen. The Future is Served. Thanks to the motion-capture sy\...]{.expanded-link-description}
:::

[](https://twitter.com/natolambert/status/1355547870649348098){.tweet-link-bottom target="_blank"}

:::: tweet-footer
[4:06 PM ∙ Jan 30, 2021]{.tweet-date}

------------------------------------------------------------------------

::: tweet-ufi
[[12]{.like-count}Likes]{.likes href="https://twitter.com/natolambert/status/1355547870649348098/likes"}[[2]{.rt-count}Retweets]{.retweets href="https://twitter.com/natolambert/status/1355547870649348098/retweets"}
:::
::::
:::::::::

-   I added a [page to my website](https://www.natolambert.com/mental-health) being open about the mental challenges of graduate school. I hope this is a resource for young students, and plan on building it out to include more tips for applications and making sense of competition in research.

-   Blog post: [Exploitation Exploration (in MBRL)](https://www.natolambert.com/writing/exploitation-exploration): I talk about how the exploration that makes model-based RL algorithms function is predicated on exploiting a learned model. This seems a little backward and deserves to be characterized further.

### Reads

-   I enjoyed [learning about online prediction markets](https://astralcodexten.substack.com/p/metaculus-monday) and their takes on different COVID likelihoods.

-   I am excited to check out Ryan Calo's next project --- T[elling Stories: On Culturally Responsive Artificial Intelligence](%5Bhttp://techpolicylab.uw.edu/telling-stories/%5D).

<div>

------------------------------------------------------------------------

</div>

I made a [new website](https://www.natolambert.com). You can learn about machine learning, robotics, and me.

If you want to support this: like, comment, or [reach out](https://twitter.com/natolambert)!

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/418a9471-ad70-40a8-bc2c-ba52e0cdbda0_4032x1861.jpeg)
