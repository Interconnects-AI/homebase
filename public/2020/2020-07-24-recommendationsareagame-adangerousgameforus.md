---
title: "Recommendations are a game - a dangerous game (for us)."
subtitle: "Machine-recommendation system ethics, models of human reward, reinforcement learning framing; followup on GPT-3."
date: 2020-07-24
type: newsletter
audience: everyone
visibility: public
post_id: 551941.recommendations-are-a-game-a-dangerous
email_sent_at: 2020-07-24T11:18:59.331Z
---
This week we are discussing recommender systems. What began with an essay titled "On the ethics of recommendation systems" now encompasses a brief intro to recommendation systems online, ethics of such systems, ways we can formulate human reward, and views of human recommendations as a slowly updated batch reinforcement learning problem (the *game*, where our reward is not even in the loop).

#### A brief overview of recommender systems

The news feed systems, so to say. The recommender systems ([Wikipedia had the most to the point summary for me](https://en.wikipedia.org/wiki/Recommender_system)) decide what content to give us, which is a function of our profile data and our past interactions. The interactions can include many things depending on the interface (mobile vs desktop) and platform (app, operative system, webpage). Netflix, often touted as making the most advancements to the technology, has a webpage describing [some of their research in the area](https://research.netflix.com/research-area/recommendations).

What kind of machine learning do these systems use? [A survey from 2015](https://arxiv.org/pdf/1511.05263.pdf) found that many applications used [decision trees](https://en.wikipedia.org/wiki/Decision_tree) and [Bayesian methods](https://en.wikipedia.org/wiki/Bayesian_inference#:~:text=Bayesian%20inference%20is%20a%20method,and%20especially%20in%20mathematical%20statistics.) (because they give you interpretability). Only 2 years later there was a [survey on exclusively deep learning](https://arxiv.org/pdf/1707.07435.pdf) approaches. I think many companies are using neural networks and are okay with the tradeoff of dramatically improved performance at the cost of interpretability - *it's not like they would tell the customer why they're seeing certain content, would they?*

I drew up a fun diagram that is your baseline, and it'll be expanded throughout the article. It's a sort of incomplete reinforcement learning framework of the agent takes action *a* -\> environment moves to state *s* -\> returns reward *r*.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/6a8d38d1-9f07-44d1-8a1b-7019ea6bb1a2_2006x1253.png)

#### Clickthrough led to clickbait

Clickthrough (a heuristic of engagement, reward) was an early metric used to create recommendations. The clickbait problem (open link, close it immediately) led to a dwell time metrics on pages. I have been satisfactory burnt out of clickbait sites, so I started this direct-to-reader blog. That's just the surface level effect for me, and I am sure there's more. At one point, Facebook's go-to metric for a while was the usage of the click to share button - okay, you get the point, on to the paper.

I found a [paper](https://participatoryml.github.io/papers/2020/42.pdf) from a [workshop](https://participatoryml.github.io/) on **Participatory Approaches to Machine Learning (*****when you look closer, there are many great papers to draw on, I will likely revisit)*** at the International Conference on Machine Learning last week. When you see block quotes, they are from *[What are you optimizing for? Aligning Recommender Systems with Human Values](https://participatoryml.github.io/papers/2020/42.pdf)*, Stray et. al, 2020. There's some great context on how the systems are used and deployed.

> Most large production systems today (including Flipboard (Cora, 2017) and Facebook (Peysakhovich & Hendrix, 2016)) instead train classifiers on human-labelled clickbait and use them to measure and decrease the prevalence of clickbait within the system.

Human labeled content is a bottleneck when generated content outpaces labeling capacity. Also, labeling a classifier will be outdated immediately at deployment (constantly moving test set). [There are also companies that won't describe how they operate](https://www.wired.com/story/tiktok-finally-explains-for-you-algorithm-works/). Another point regarding industry usage I found interesting is:

> Spotify is notable for elaborating on the fairness and diversity issues faced by a music platform. Their recommendation system is essentially a two-sided market, since artists must be matched with users in a way that satisfies both, or neither will stay on the platform.

And, obvious comment below, but requisite.

> Especially when filtering social media and news content, recommenders are key mediators in public discussion. Twitter has attempted to create "healthy conversation" metrics with the goal to "provide positive incentives for encouraging more constructive conversation" (Wagner, 2019).

My impression of the learned models is: **If the big companies do it, it's because it works.** Again, don't assume malintent, assume profits. Now that we have covered how the companies are using their platforms to addict us to their advertisements, here is a small update to our model - a feedback loop and bidirectional arrows.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/ee545177-9ab1-439d-a5c6-99b490fde69c_2006x1250.png)

# Ethics of Recommender Systems

Our computers are deciding what to put in front of us, primarily so that the companies retain us as reliable customers. What could go wrong? What are you okay with robots recommending for you? Your social media content - okay. How I decide my career path - I don't know.

I don't blame companies for making these tools and putting them in front of us - they want to make money after all. These issues will come to the forefront as the negative effects compound over the next few years. Here are a few points where I don't think companies are held to high enough standards:

-   [Financial Technology (Fintech) Companies](https://www.nytimes.com/2020/07/08/technology/robinhood-risky-trading.html): manipulate your brain into engaging with financial products in different ways, which has had more dramatic effects on people without certain financial stability.

-   [High-traffic Media Platforms](https://www.wsj.com/articles/facebook-criticized-in-india-over-free-limited-internet-1453398493): Beyond the simple point of the hours you spend online each day, or how Google dictates everything you see, technology companies have tried to "*be the internet*" in developing nations. Click the link to see what happened when Facebook tried to be the internet in India (they were nice enough to include Wikipedia, though!).

-   [News Sources](https://open.nytimes.com/how-the-new-york-times-is-experimenting-with-recommendation-algorithms-562f78624d26): Mainstream newsrooms (and definitely fringe sites, and everything in between) use automated methods to tune what news is given to you. I see a future where they tune the writing style to better match your views, too. Conformism is not progressive.

I want to start with what has been called the **Value Alignment Problem** in at-scale, human-facing AI (example paper on legal contracts, AI, and value alignment [Hadfield-Menell & Hadfield, 2019](https://dl.acm.org/doi/pdf/10.1145/3306618.3314250?casa_token=nGByQyqI-vAAAAAA%3AwFL1xCEWvZSBgUUS9ylzqq5x1lUmn3d_bv5rSY0wxsjK8VGCuJS5LqUmI6SgIJ2rsf4WizUGzosZ6g)).

#### Low-level ethics of working with human subjects

I define the ethical problem here as short term results (highlighted below) and long term mental-rewiring of humans whose lives are run by algorithms.

> Concerns about recommender systems include the promotion of disinformation ([Stocker, 2019](https://link.springer.com/chapter/10.1007/978-3-030-39627-5_11)), discriminatory or otherwise unfair results ([Barocas et al., 2019](https://fairmlbook.org/)), addictive behavior ([Hasan et al., 2018](https://www.sciencedirect.com/science/article/pii/S0747563217306581))([Andreassen, 2015)](https://link.springer.com/article/10.1007/s40429-015-0056-9), insufficient diversity of content ([Castells et al., 2015](https://link.springer.com/chapter/10.1007/978-1-4899-7637-6_26)), and the balkanization of public discourse and resulting political polarization ([Benkler et al., 2018](https://books.google.com/books?hl=en&lr=&id=MVRuDwAAQBAJ&oi=fnd&pg=PP1&dq=Benkler,+Y.,+Faris,+R.,+and+Roberts,+H.+Network+propaganda:+Manipulation,+disinformation,+and+radicalization+in+American+politics.+Oxford+University+Press,+2018.&ots=W7mpAkGznh&sig=z9hR7vzs8oaLujF-MP2JCSW-tMg#v=onepage&q&f=false)).

Stray et. al, 2020 continue and introduce the **Recommender Alignment Problem**. It is a specific version of the value alignment problem that could have increased emergence because of the prevalence of the technologies in our lives. If at this point you aren't thinking about how they affect you, have you been reading closely? Finally, a three-phase approach to alignment:

> We observe a common three phase approach to alignment: 1) relevant categories of content (e.g., clickbait) are identified; 2) these categories are operationalized as evolving labeled datasets; and 3) models trained off this data are used to adjust the system recommendations

This can be summarized as identification (of content and issues), operalization (of models and data), adjustment of deployment. This sounds relatively close to how machine learning models are deployed to start with, but it is detailed below.

#### High-level, recommender system adjustments:

The high-level ideas again are from the paper, but the comments are my own.

1.  Useful definitions and measures of alignment - companies need to create research on internet metrics that better match user expectations and accumulated harm (or uplifting!)

2.  Participatory recommenders - having humans in the loop for content will enable much better matching of human reward to modeled reward, which long term will pay off.

3.  **Interactive value learning -** this is the most important issue and it can encompass all others. Ultimately, assume the reward function is a distribution and extreme exploitation dramatically decreases (more below)

4.  Design around informed, deliberative judgment - this seems obvious to me, but please no fake news.

Let's continue with point three.

#### Modeling human reward

The interaction between what the ***optimization problem is defined as*** and what the ***optimization problem really is*** is the long term battle of applying machine learning systems in safe interactions with humans.

The model used by most machine learning tools now is to optimize a reward function given to the computer by a human. The **Standard Model** ([Russell -](https://books.google.com/books?hl=en&lr=&id=M1eFDwAAQBAJ&oi=fnd&pg=PT6&dq=human+compatible+book&ots=k_Vqa9Ac13&sig=iD5t7xb-HH1NovGRij2AI--2nt8#v=onepage&q=human%20compatible%20book&f=false) *[Human Compatible](https://books.google.com/books?hl=en&lr=&id=M1eFDwAAQBAJ&oi=fnd&pg=PT6&dq=human+compatible+book&ots=k_Vqa9Ac13&sig=iD5t7xb-HH1NovGRij2AI--2nt8#v=onepage&q=human%20compatible%20book&f=false)*[, 2019](https://books.google.com/books?hl=en&lr=&id=M1eFDwAAQBAJ&oi=fnd&pg=PT6&dq=human+compatible+book&ots=k_Vqa9Ac13&sig=iD5t7xb-HH1NovGRij2AI--2nt8#v=onepage&q=human%20compatible%20book&f=false)) is nothing more than an [optimization problem](https://en.wikipedia.org/wiki/Optimization_problem#:~:text=In%20mathematics%2C%20computer%20science%20and,solution%20from%20all%20feasible%20solutions.&text=A%20problem%20with%20continuous%20variables,continuous%20function%20must%20be%20found.) where the outcomes will improve when the metric on a certain reward function is improved. This falls flat on its face when we consider comparing weighing reward of multiple humans (magnitude and direction), that AIs will exploit unmentioned avenues for action (I tell the robot I want coffee, but the nearest coffee shop is \$12, that's not an outcome I wanted, but it "did it"), and more deleterious unmodeled effects.

What is a better way to do this? The better way is again, **interactive value learning**. Value learning is a framework that would allow the AIs we make to never assume they have a full model for what humans want. If an AI only thinks that it will have a 80% chance of acting correctly, it will be much timider in its actions to maintain high expected utility (I think about the 20% chance including some very negative outcomes). Recommender systems need to account for this as well, otherwise, we will be spiraling in a game that we have little control over.

# Reinforcement Learning with Humans and Computers in the Loop

Reinforcement learning is an iterative framework where an agent interacts with an environment via actions to maximize reward. [Reinforcement learning (RL) has had a lot of success with confined games.](https://deepmind.com/blog/article/deep-reinforcement-learning) In this case, there are two 'game' framings.

1.  The application is the agent, and the human is part of the state space (actually fits with the problem formulation better)

2.  The human is the agent, the computer, and the world is the environment, and the reward is hard to model. This one is much more compelling, so on I go. This is **the game** I refer to in my title.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/61bbdc4c-ad81-4358-841a-d14afbce25fe_2647x1231.png)

Ultimately, the FAANG companies are going to be logging all of the traffic data (including heuristics towards true human reward that we talked about earlier) and trying to learn how your device should interact with you. It's a complicated system that has the downstream effect of **everyone else you interact with**in the feedback loop. As an RL researcher, I know the algorithms are fragile, and I do not want that applied to me (but I struggle to remove myself, frequently). The diagram above is most of the point - there is no way that a single entity can design an optimization to "solve" that net.

Let's talk about the data and modeling. To my knowledge, FAANG is not using RL yet, but they are acquiring a large dataset to potentially do so. The process of going from a large dataset of states, actions, and rewards to a new policy is called **batch reinforcement learning** (or offline RL). It tries to distill a history of unordered behavior into an optimal policy. *My view of the technology companies' applications is that they are already playing this game, but an RL agent doesn't determine updates to the recommender system, a team of engineers do*. The only case that could be made is that maybe TikTok's black box has shifted towards an RL algorithm prioritizing viewership. If recommendation systems are going to become a reinforcement learning problem, the ethic solutions need to come ASAP.

Here are resources for readers interested in [batch RL course material](https://web.stanford.edu/class/cs234/CS234Win2018/slides/cs234_2018_l13.pdf), [offline RL research](https://arxiv.org/pdf/2005.13239.pdf), and [broad challenges of real-world RL](https://arxiv.org/pdf/1904.12901.pdf).

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/9c760a17-6b2d-4fa6-aa46-eb7d991cde1b_1258x625.jpeg)

<div>

------------------------------------------------------------------------

</div>

# Follow Up on GPT-3

This is a follow up from my article last week: [Automating Code, Twitter\'s hack(s), a robot named Stretch](https://democraticrobots.substack.com/p/automating-code-twitters-hacks-a?r=68gy5&utm_campaign=post&utm_medium=web&utm_source=copy) on the recent [OpenAI model GPT3](https://openai.com/blog/openai-api/). I wanted to include a couple of points that I have heard repeated for why this is not an economic powerhouse, yet.

1.  From the venture capital perspective, no business that is leveraging this is extremely interesting because **there is no competitive advantage**. Your advantage would be being the first one to use the tool. It's not to say people won't make money off of it, but it is more of a reward for people who are quick on their feet. **You don't own the model** - this means that anyone using it is liable to OpenAI clogging their pipe, sorry!

2.  From a practical perspective, a 175Billion parameter model is huge. This is not something that everyone can run 1000s of queries a second on without notable cost (electricity reflected in API costs). **There is visible lag** in the video demos already (*last week I shared [this link](https://twitter.com/sharifshameem/status/1284095222939451393?s=20) of a video showing GPT-3 write code*). Not only does it imply cost, it implies a barrier to entry. Engineers may turn away from a tool that is inconsistent and difficult to use in favor of consistent progress. Heard the saying that no internet is better than slow internet?

You can read OpenAI's commitment to making this a safe tool below (clickable link embeds as an image). If you want more material, I suggest you [search on Twitter](https://twitter.com/search?q=gpt3&src=typed_query) (bizarre that it is all on that platform)

::::::::::: {.tweet attrs="{\"url\":\"https://twitter.com/OpenAI/status/1286393813817151488\",\"full_text\":\"Last month we released an API for developers to build on top of our latest technology: . There’s been a lot of enthusiasm, but a great deal needs to be figured out as we scale up access. Here's how we're thinking about it. 1/8\",\"username\":\"OpenAI\",\"name\":\"OpenAI\",\"date\":\"Thu Jul 23 20:12:39 +0000 2020\",\"photos\":[],\"quoted_tweet\":{\"full_text\":\"We're releasing an API for accessing new AI models developed by OpenAI. You can \\\"program\\\" the API in natural language with just a few examples of your task. See how companies are using the API today, or join our waitlist: https://t.co/SvTgaFuTzN https://t.co/uoeeuqpDWR\",\"username\":\"OpenAI\",\"name\":\"OpenAI\"},\"retweet_count\":100,\"like_count\":462,\"expanded_url\":{},\"video_url\":null,\"belowTheFold\":true}" component-name="Twitter2ToDOM"}
[](https://twitter.com/OpenAI/status/1286393813817151488){.tweet-link-top target="_blank"}

:::: tweet-header
![Twitter avatar for \@OpenAI](https://substackcdn.com/image/twitter_name/w_96/OpenAI.jpg){.tweet-header-avatar loading="lazy"}

::: tweet-header-text
[OpenAI ]{.tweet-author-name}[\@OpenAI]{.tweet-author-handle}
:::
::::

::: tweet-text
Last month we released an API for developers to build on top of our latest technology: . There's been a lot of enthusiasm, but a great deal needs to be figured out as we scale up access. Here\'s how we\'re thinking about it. 1/8
:::

::::: quote-tweet
:::: quote-tweet-header
![Twitter avatar for \@OpenAI](https://substackcdn.com/image/twitter_name/w_40/OpenAI.jpg){.quote-tweet-header-avatar loading="lazy"}

::: quote-tweet-header-text
[OpenAI ]{.quote-tweet-name}[\@OpenAI]{.quote-tweet-username}
:::
::::

We\'re releasing an API for accessing new AI models developed by OpenAI. You can \"program\" the API in natural language with just a few examples of your task. See how companies are using the API today, or join our waitlist: https://t.co/SvTgaFuTzN https://t.co/uoeeuqpDWR
:::::

[](https://twitter.com/OpenAI/status/1286393813817151488){.tweet-link-bottom target="_blank"}

:::: tweet-footer
[8:12 PM ∙ Jul 23, 2020]{.tweet-date}

------------------------------------------------------------------------

::: tweet-ufi
[[462]{.like-count}Likes]{.likes href="https://twitter.com/OpenAI/status/1286393813817151488/likes"}[[100]{.rt-count}Retweets]{.retweets href="https://twitter.com/OpenAI/status/1286393813817151488/retweets"}
:::
::::
:::::::::::

<div>

------------------------------------------------------------------------

</div>

### **The tangentially related**

*The best of what I have found and been forwarded this week. Mostly forward-looking, sometimes current events, always good value per time.*

#### Online reading:

-   [A follow-up on](https://thegradient.pub/pulse-lessons/) interaction in the machine learning twitter community on fairness, data-bias, and if there is algorithm bias (yes there is).

-   [A research-lab "capable" robot](https://www.theverge.com/21317052/mobile-autonomous-robot-lab-assistant-research-speed) from [Kuka](https://www.kuka.com/en-us) (a big robotics supplier, at least in research). Let's be honest, it looks awesome and probably will work in 5 labs, but in 5 years I want one.

-   [A product that lets you record a preset amount of video of yourself and use deepfakes to produce more](https://www.synthesia.io/about). I think there are interesting applications in education, where you can have a tutor read any script they want. Very individualized, and the instructor only has to write out content, not speak.

-   [All of Garmin's apps, production, and website were (maybe still are) from a ransomware attack.](https://www.zdnet.com/article/garmin-services-and-production-go-down-after-ransomware-attack/) Not a good look that you can't sync your run to your phone without external servers.

#### Books:

-   *Superintelligence* - Nick Bostrom. Thinking about the potential types of superintelligence is fun. **Machine intelligence** is the starter, but there's also **biological emulation** (simulated brains), **network superintelligence** (if there were 10x humans?), **brain-machine superintelligence**, and more. Many paths lead to dangerous ground.

#### Listen or watch:

-   *[The Portal](https://art19.com/shows/the-portal/episodes/afb2330a-850e-488e-b729-dadc0c5e58bf)* [- Eric Weinstein](https://art19.com/shows/the-portal/episodes/afb2330a-850e-488e-b729-dadc0c5e58bf) with [Andrew Marantz](https://www.newyorker.com/contributors/andrew-marantz) **(**writer, New Yorker**),** on internet culture, wokeness, privilege, and more.

-   *[Making Sense](https://samharris.org/podcasts/211-the-nature-of-human-nature/)* [- Sam Harris](https://samharris.org/podcasts/211-the-nature-of-human-nature/) with [Robert Plomin](https://www.kcl.ac.uk/people/robert-plomin). On genetics and their effect on us as individual genetics. The more I learn about genetics, the more I realize what we have is mostly luck. I love listening, but think in a couple of years when we have polygenetic scores I will need to remove myself from most of the conversation (like discussions on free will, life in a simulation).

<div>

------------------------------------------------------------------------

</div>

Hopefully, you find some of this interesting and fun. You can find more about the author [here](http://www.natolambert.me/). Forwarded this? [Subscribe here](https://democraticrobots.substack.com/). It helps me a lot to forward this to interested parties, are Tweet at me [\@natolambert](https://twitter.com/natolambert). I write to learn and converse.
