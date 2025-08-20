---
title: "Remote robotic-data farms"
subtitle: "Industry labs power up their robot learning research with parallelization!"
date: 2021-08-09
type: newsletter
audience: everyone
visibility: public
post_id: 39451282.remote-robot-data-farms
email_sent_at: 2021-08-09T13:31:22.821Z
---
Most robotics researchers start with some level of love for the hardware side of the work. The next big thing happening in robotics infrastructure is going to make it so us researchers no longer need to worry about all the hardware details --- it is *a series of technological developments* allowing **hardware papers to be written without going into the office**. After a Ph.D. of on and off hardware development, I am sure most of my desire to work hands-on with hardware is a graduate-student-special version of [Stockholm syndrome](https://en.wikipedia.org/wiki/Stockholm_syndrome).

I have heard of multiple researchers at big technology companies that have published robotic learning work without physically going into the office. The technology that allows remote operation also gets most of the way towards robots that can run extra experiments on their own to collect more data for future tasks that may not yet be known. This may seem somewhat backwards: what is the extra data going to be used for? To date, most robotic learning research has a very tight link between a paper and a set of experiments, but *breaking that one-to-one mapping is key to the field leveraging other advancements commercializing deep learning* (mostly bigger data).

As most people who work in tech know **remote work** is the future, this can become a major perk that some companies leverage to keep talent. Anyways, I am okay with saying \"hello\" to the robots executing our experiments when we have our on-site workshops with our team - the rest of the time we\'ll be doing long-distance.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

A fundamental axis to this is the fixed cost of operating hardware and how to amortize it. In reality, even just one robot that is able to operate without supervision is a large win in increasing the ratio of intellectual time to debugging time of a researcher. Robotics research has a substantial fixed cost of debugging that is rarely acknowledged in the literature (here is a fun paper related to it: *[Is Bang-bang control All You Need?](https://drive.google.com/file/d/1pzlVVsQeAJDOxRHp9p6HVknzQTiCtwNT/view)*). A huge benefit kicks in when these robots are combined to create a **parallel** workforce of learning robots - lower average fixed costs per agent by averaging over more.

There is one company that I know closely of, [Covariant](https://covariant.ai) (that I openly talk about a lot), that seems to be leveraging the potential of remote robot farms - to send out lots of robots, have them work autonomously across the globe, and all improve each other from **collective experience** (sounds a lot like how human society develops...). It is important to note a key difference between research labs and Covariant though, which also points to why they are likely not deploying reinforcement learning agents yet: *most of the data Covariant uses is from robots that are expected to perform at a high standard, therefore there is little room for exploration in the classical sense of RL*. There is still a weak notion of RL, where the agent can try again if it makes a mistake, or at least label the logged data as high priority.

The remote-operation and robust-control aspects of this article will slot into [Horizontal Modularity](https://robotic.substack.com/p/robotics-take-two), and make it more practical: *robotics companies should re-use data from similar applications on multiple platforms to compound their available data for learning-based control.* This article is focused on two interweaved time horizons: how research can be accelerated by making better platforms and how companies can build a data-moat. Having better infrastructure and data means that when upstarts apply potentially better, novel methods, it may not be a challenge. The data-moat allows companies to become dominant and entrenched in their best tasks (across multiple robotic platforms, ideally).

There are a few key technologies that will be developed as more people realize the power of this data-farming. In this post, I discuss the following (ordered by what seems like most-blocking of progress to most-futuristic):

-   **teleoperation**: low-latency tech for operation a robot virtually,

-   **safe learning**: a hilariously understudied area for not breaking things (and making them less scary in the real world!),

-   **self-supervised learning**: machine-learning algorithms that do not need human supervision,

-   **parallel execution**: developing algorithms with the knowledge that multiple agents will be running them.

I want to see labs where the robots continue running when no one has queued specific experiments, so they continue to collect more data and design their own curriculum (AGI w00t). This article discussed breakthroughs that should at least enable the former.

<div>

------------------------------------------------------------------------

</div>

## Telerobotics

[Telerobotics](https://en.wikipedia.org/wiki/Telerobotics) is an interesting area - it conjures a lot of different feelings across people based on their priors. Personally, when I hear it, I think of someone taking over in the room for a robot that got stuck in the course of a reinforcement learning experiment, but the technology has already been applied to much more practical scenarios like space exploration. On [Wikipedia](https://en.wikipedia.org/wiki/Telerobotics), telerobotics is...

> the area of robotics concerned with the control of semi-autonomous robots from a distance, chiefly using Wireless network (like Wi-Fi, Bluetooth, the Deep Space Network, and similar) or tethered connections. It is a combination of two major subfields, teleoperation and telepresence.

In my career, I have heard more about and focused on **teleoperation**, which is the infrastructure for controlling the robot, which in theory can be run without telepresence, but alone it won\'t enable robots to act any smoother than someone trying to order groceries on a wet iPhone screen. **Telepresence** is the feedback aspect that\'ll empower the users of these robots.

This is crucial for one short reason: humans are really good at most of the puzzles we are trying to have robots learn. If the robot is stuck, an engineer can call in and reset it most of the time (broken robots aside, more on that later). Only being looped in when needed is such a huge time-saver. it would re-write the paradigm of robotics research and development, where currently a ton of time is used to build an intuition of your system. Now, that time would be more data-driven, sampled (from a large replay of data), and quantitative.

Without proper teleoperation and telepresence, there is no hope of having robotics researchers remote from the lab, so this is step one.

*Note: a good blog post on telerobotics is [here](https://benjaminreinhardt.com/telerobotics-bottlenecks) from Ben Reinhardt.*

## Safety

Most algorithms and platforms used in robotic learning to date only optimize for *safety as a proxy*. This works because maximization of reward stops when the robot breaks, so there are weak gradients pointing systems to not break. This "weakly safe" behavior in my first research project was my quadrotor flying straight up fast because it knows that it is less unstable when flying at full thrust, but coincidentally to always crashed into the ceiling.

In reality, **robots break a lot**. Papers that showcase the most impressive results generally only work a low percentage of the time --- the best example of this is OpenAI's Rubik's Cube solving hand only worked 60% of the time (R.I.P. to their robotics team). 

Personally, I think [model-based RL](https://robotic.substack.com/p/mbrl) will be a useful candidate to sync safe and interpretable methods with open-ended learning. The ultimate solution to guaranteeing safety in data-driven autonomous systems would be to **translate** **control-theoretic** notions of **[stability](https://en.wikipedia.org/wiki/Stability_theory)** to learned models, but that seems like it can only take the form of a North Star for research rather than a practical goal. 

Safety will allow robots to attempt and learn more tasks, which will add layers to the autonomous and adventurous system of robot farms. Once safety exists in a lab, then companies can try it on real-world problems. No one would ever try and learn to control vehicles before making a lot of progress in a lab, [right](https://www.thedrive.com/tech/40794/tesla-removes-radar-sensors-from-model-3-and-model-y-so-autopilot-will-use-cameras-only)?

Waymo seems to be the company doing the most [safety-oriented research](https://waymo.com/safety/) (I discussed their approach in my [article illustrating the tradeoff](https://robotic.substack.com/p/clarifying-rl) between modular and end-to-end approaches in deep RL). Some people and conferences I happily follow to keep up with the safe learning literature all are entities I discovered from following [Claire Tomlin's](https://people.eecs.berkeley.edu/~tomlin/) lab at Berkeley (suggested reading, [Jaime Fisac](https://ece.princeton.edu/people/jaime-fernandez-fisac), or the [Conference on Learning for Decision and Control](https://l4dc.ethz.ch)).

## Self-supervised learning 

The technologies humans rely on the most (logistics, internet, etc.) operate at a scale by which humans-in-the-loop will be a bottleneck. For example: Sadly, Facebook cannot moderate all the content on the platform, so over 99% of the potentially harmful content is pre-flagged by an AI. Think about how great a (physical) mailing system would be that never needed to have humans in the loop and could further optimize its routing at the level of door carriers and freight jets? These are all things (with a little imagination) that are enabled by further **self-supervision**.

The famous researcher, Yann LeCun, says that self-supervised learning is "the bulk of the cake" of learning systems (see slide below). 

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/73b32d9e-6213-4cf5-803a-16e50b071555_2208x1244.png)

Self-supervised learning seems compelling to me, much like reinforcement learning is. If we want to have truly intelligent systems, there should be ways for them to make sense of data when given enough time and compute --- to compute and distill to **feature-rich manifolds** entirely on their own. Self-supervised learning is a much younger topic in robotics, but I clearly see it as a crucial aspect of the long-term future.

Us organizers for the [4th Robot Learning Workshop](http://www.robot-learning.ml/2021/) at the Neural Information Processing Conference have self-supervised learning as a core concept for this year! Fun fact, model-based RL is a form of self-supervised learning (dynamics data is annotated), but a lot of times algorithms violate this by giving the learner the underlying reward function (rather than just the samples!)

*Note: for those interested in the difference between self-supervised learning and unsupervised learning, continue reading this paragraph. Self-supervised learning has become [the more popular term](https://ai.facebook.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/), where algorithms learn from data in a way that populates their own labels --- you supervise the system in a way that it learns mappings across inputs (rather than input-output pairs). In this [podcast](https://thegradientpub.substack.com/p/yann-lecun-on-his-start-in-research?token=eyJ1c2VyX2lkIjoxMDQ3MjkwOSwicG9zdF9pZCI6Mzk2NTA3MTAsIl8iOiJ3OFdJdCIsImlhdCI6MTYyODE4NDMxOSwiZXhwIjoxNjI4MTg3OTE5LCJpc3MiOiJwdWItMjY1NDI0Iiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.6DmYrXkUTWNynwtyUiEeNgh2RshGcXjV4XqS4ECxpg8&utm_source=substack&utm_medium=email#play), Yann LeCun discusses the difference (about 18 minutes in). Unsupervised learning is a more general approach including methods that do not necessarily attempt to create labels or use other advances in supervised learning.*

## Parallel execution

Deep RL agents are designed to operate serially in almost the entire literature. The clearest case of this I have thought about recently is exploration methods --- most RL exploration equates to a sort of a random walk to find a goal. If you have multiple agents executing a random walk, there will be a lot of similar data. The goal should be to have each agent explore a targeted area independently! 

The culmination of any autonomous system is the compounding effects that kick in once the system is deployed at scale.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} Otherwise, I think I have covered why parallel execution is so important in the preceding of this article --- **redundancy**.

Now that people have seen this happen with many digital platforms, some big names in AI are suggesting moving the field from algorithm-centric to data-centric research, such as Andrew Ng: [3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

:::::::: {#youtube2-06-AZXmwHjo .youtube-wrap attrs="{\"videoId\":\"06-AZXmwHjo\",\"startTime\":\"1048\",\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=06-AZXmwHjo){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

<div>

------------------------------------------------------------------------

</div>

## Examples

I think places like Amazon are best positioned to already be benefiting from this framing (and Apple, depending on what your definition of robot is), though, they are some of the least likely to share. Thankfully, some recent examples highlighting these approaches (and the source of the thumbnail for this post) are coming from Google's various research organizations --- maybe because they do not have a hope of products physically embodied in customers' lives like these other two. The first paper from Google attempting to use a parallel setup was [QT-Opt](https://arxiv.org/abs/1806.10293), and now they have continued to utilize it, with another paper [MT-Opt](https://arxiv.org/abs/2104.08212) (and [video](https://www.youtube.com/watch?v=i3uUGSko2zY) from an author). [4](#footnote-4){#footnote-anchor-4 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/f4a51a6a-a855-4191-ada6-e5999474af9a_400x300.gif)

DeepMind does not have as clear examples publicly posted (research driving parallelization), but the teleoperation and self-operation of these robots are enabling their teams to continue to publish through COVID.[5](#footnote-5){#footnote-anchor-5 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

In reality, the vast majority of research is not framed nor optimized in a manner pointing towards parallelization. In academia, this could be more due to feasibility than interests. Scaling up laboratories for parallel execution costs multiple full-time employees (and they won't end up with Ph. D.s for their contributions). For example, current methods in RL are primarily designed around the question of \"how does one agent learn to act in the world," and this framing is elegant but less likely to tap into compounding (practical) benefits of these **remote robot-farms**.

There are a couple of industrial examples I have found and it seems like they are the tip of the iceberg of people trying to utilize this (but please send me links if there is anything I have missed)! There is a company [Phantom](https://phantom.auto/?utm_term=telerobotics) with a specific branch for telerobotics, but even with some [press](https://www.nytimes.com/2021/07/14/business/germany-autonomous-driving-new-law.html?utm_content=172984599&utm_medium=social&utm_source=facebook&hss_channel=fbp-1878240999162153) coverage, I cannot pinpoint their direction as well as some others. Another, [AMP Robotics](https://www.amprobotics.com) seems to be doing some cools things with re-using data across sites (faster to solve a new task now that they have a wider prior, describe in a [podcast](https://www.youtube.com/watch?v=fNq9oCH0h58), [press](https://www.youtube.com/watch?v=DKOf6yFepHA)). Finally, there is [Covariant](https://covariant.ai) in Berkeley that I can't confirm is taking the parallel approach, but they're trying to use deep learning as a core technology, so in parallel is the best way to get data! This is one of the bets I am willing to place some of my job-search decisions on (Amazon is building a new lab in Cambridge, MA 👀). There are likely other companies exploiting this in dark mode, so being able to do publish research on it would be too cool. Maybe I should write about literal robotic farms because automating agriculture is actually a huge area I have crossed paths with a few times but never taken the time to research. Thoughts?

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Yes, there are still staff that go into these labs, but this often is also for improvements and expansion. Given a decade, these labs will become even more reliable.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
These at scale effects bring increased risk with increased power. Consider the first company that creates an autonomous car --- they will effectively rewrite the rules of the road. 
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
This is an open debate in Robotics, to the point where we are considering running a debate on it at the next iteration of the [Robot Learning Workshop](http://www.robot-learning.ml/2021/).
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[4](#footnote-anchor-4){#footnote-4 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
The first paper was using one robot to solve a single task, the second is multiple robots for multiple tasks (as I have hinted at in the paper).
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[5](#footnote-anchor-5){#footnote-5 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Avoiding the cool details due to NDA and not being able to find them publicly explained.
:::
::::
