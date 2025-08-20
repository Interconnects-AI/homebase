---
title: "Can robots be autonomous and unintelligent?"
subtitle: "Re-thinking robot design part 2: don’t restrict your robot worldview to robot (a) does task (b)."
date: 2020-08-28
type: newsletter
audience: everyone
visibility: public
post_id: 812606.autonomy-vs-intelligence-with-humans
email_sent_at: 2020-08-28T14:03:18.590Z
---
This is part two of a series on re-thinking robot design, you can find the first part here on the decisions behind [what a robot should look and act like](https://democraticrobots.substack.com/p/the-uncanny-world-of-at-home-robots). *Please subscribe to get the rest of the series (which is evolving) and happenings on robotics and automation (ie the fun parts of tech.). *

<div>

------------------------------------------------------------------------

</div>

In this post, I address two questions:

1.  Is automation equal to intelligence --- is one a prerequisite for another?

2.  How do we train agents to act in ways that align with human goals --- what limits are there on automation with the ***standard model*** (direct optimization of a singular reward).

### Hardware-Task Relationship:

To start, consider this video. In it, you'll see an agent accomplishing a task: swimming upstream (the water is flowing from left to right).

:::::: {#vimeo-44887922 .vimeo-wrap attrs="{\"videoId\":\"44887922\",\"videoKey\":\"\",\"belowTheFold\":false}" component-name="VimeoToDOM"}
::::: vimeo-inner
:::: iframe
[](https://player.vimeo.com/video/44887922)

::: {#crawler_player}
Play

![Vimeo](https://f.vimeocdn.com/p/images/crawler_logo.png){.logo}
:::
::::
:::::
::::::

Now, I know some of you didn't click the link and that's okay, but the catch is that it is a **dead fish** swimming upstream. Nature has figured some things out about design that humans creating products may never get to tap into: **passive design**. Passive design is great because it normally accomplishes the goal with very little effort, but it means that your design is normally locked into a task.

**My hypothesis:** *the most successful robotics companies of the future will be **platforms** that enable both users and other companies to enable new tasks rapidly and reliably.* These companies will figure out a couple tricks of design, and how to better act at the boundary of autonomy and intelligence.

Today, robots are designed with a task in mind, and this task can limit them. In this post, **I start with hardware because the structure a robot is on defines what it can do**. I like to think about [passive robot walkers](https://www.youtube.com/watch?v=rhu2xNIpgDE) (usually bipedal, like humans): they are designed to passively walk with a mass distribution, joint ranges, and more. Then, when you add motors and a controller to it, what can you do? Normally not much more because the design constraints the movement.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c3d79ec6-320b-4d60-a8bf-b6175b3a92d6_5331x3001.jpeg)

<div>

------------------------------------------------------------------------

</div>

## Automation is not always intelligence

One of the leaders in at-home robotics recently made a big shift from hardware-based development to software-based application development: [iRobot (king of the Roomba)](https://www.irobot.com/). This is an interesting shift, that in many ways co-aligns thematically in what I am writing about (and [it happened just when I was writing about it](https://spectrum.ieee.org/automaton/robotics/home-robots/irobot-home-autonomy-update)). The TL;DR is that iRobot moved two-thirds of their engineering base to software and human-robot interaction development, but the quotes from the CEO are very telling for anyone either a) interested in making at-home robots for a career or b) wondering by the at-home robot market seems so bizarrely empty and shifty. 

### Design a robot vs design for users

The Roomba company is shifting from a robust autonomy approach, ie *how to make the vacuum that'll get the highest percentage of particles in any space with the most [9's of reliability](https://en.wikipedia.org/wiki/High_availability#Percentage_calculation)*, to that of *how do we create happy customers that interact with their vacuum*. When reflecting on what users want, the CEO of iRobot, Anges says the company needs a new direction to keep users engaged:

> Autonomy is not intelligence. We need to do something more.

This dichotomy comes into play with many other companies, and I will take a little liberty when I make these comparisons. A similar difference in self-driving cars is that Waymo is making an autonomy-stack and Tesla is making a product people want to use. This could also be seen in a difference between more of a hardware-focused company that famously went by a motto of "[do what the customer needs before they want it](https://www.goodreads.com/quotes/988332-some-people-say-give-the-customers-what-they-want-but)," versus a company [that copies the trend in technology to stay afloat](https://www.digitaltrends.com/android/samsung-copied-apple-who-cares/). 

The former stance --- make what is right --- is very hard in robotics. No one knows the answer, and what is right likely is not technologically feasible yet. 

### Robots are inherently hard and limited

Thinking about this above, I think a lot of people will reflect that they want to make agents that are intelligent, reflective of their environment, and interactive, but that's really damn hard. Getting any single new task to work on a robot is a huge success. Moving parts, changing worlds, and anything physical is doubly hard to sell when it is so easy to print money on the digital marketplace --- but it's rewarding.

Think about what needs to be in place before a robot can even maybe reason about how to better serve **you** in your home. Again, from Anges:

> Until the robot proves that it knows enough about your home and about the way that you want your home cleaned, you can't move forward."

And more succinctly:

> a robot can't be responsive if it's incompetent.

How iRobot is making this transition is very reminiscent of how [I have done research](https://arxiv.org/abs/2004.13194): go around lab taking photos of low lying objects and see how the model we create can capture them. 

> This is done through machine learning using a library of images of common household objects from a floor perspective that iRobot had to develop from scratch. 

*For the curious*: we are working towards autonomous microrobots, and want to have them navigate the world. In our image-based navigation dataset, cubicles look like the giant, looming walls of a maze. iRobot is trying to re-create a navigation dataset for homes. This reminds me of how [Covariant](https://covariant.ai/) is equipping robots for pick-and-place in logistics: really, really robust data.

I leave you with a tangent that summarizes well the current state of personal electronics --- what if my Roomba is stolen, will they know what kind of slippers I wear?

> Worst case, if all the data iRobot has about your home gets somehow stolen, the hacker would only know that (for example) your dining room has a table in it and the approximate size and location of that table, because the map iRobot has of your place only stores symbolic representations rather than images.

<div>

------------------------------------------------------------------------

</div>

## The standard model

How do we make it easier for robots to bridge the gap from autonomy to intelligence? Change how the tasks are modeled.

Let's take a step back, all the way back. Humans are called *homo sapiens* which can roughly be translated as "wise man." Is more intelligence always the answer? Consider this in the above example --- is a Roomba that continues to learn more about you and always gain more abilities always the answer? Surely not --- surely there is a peak with how much reasoning you want your vacuum to have.

### Machines are intelligent to the extent by which they can achieve their outcomes

Is this true? Do we want this to be how our robots are defined?

This is the definition of the standard model. All across robotics and machine learning, the measure the success of an agent by its performance on baselines --- a small set of tasks (that are [very troubling in my field](https://towardsdatascience.com/the-state-of-baselines-in-reinforcement-learning-research-160e463003d9)). This results in a *standard model* shown below --- computers are optimizing reward functions we have given them. (*Credit to Stuart Russell on this naming convention*). 

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/aca02b89-2fed-4673-810e-528d7b9b0718_1366x192.png)

### Humans in the loop

What we want is (from *Human Compatible*):

> machines that are beneficial to the extent that their actions can be expected to achieve our outcomes.

There is a big caveat on this that we by no means know how to model human rewards, but that should be the new assumption: uncertainty and exploration. What this translates to in the model above: 

-   assuming the previous set of parameters you chose is always imperfect because your model of humans is imperfect, 

-   any model you use for one human cannot translate because of each human being different,

-   weighing objectives that affect multiple people is near impossible (can't compare relative views),

-   and finally: all humans operate on a distribution of rewards. Encoding it into a single function is always sub-optimal.

The point of this point is to get to the point where we a) see that there is a different path forward and b) have a direction to point at. By no means do I expect anyone to solve this overnight, but it is a set of goalposts for us to aim at while we keep automating the world.

I recommend Stuart's recent book *[Human Compatible](https://bookshop.org/books/human-compatible-artificial-intelligence-and-the-problem-of-control/9780525558613)* if you would like to read more.

I am intentionally avoiding a couple of hot topics in reinforcement learning that pertains to generalization / task transfer (such as [meta-learning](https://escholarship.org/content/qt0987d4n3/qt0987d4n3.pdf) or [other generalizable methods](https://bair.berkeley.edu/blog/2019/03/18/rl-generalization/)). I think that most generalization to date is proportional to data-distribution coverage of multiple tasks --- not the ability for the same hyperparameters to solve numerically distinct tasks.

The good news: I think ***expanding our robot worldview can lead to robots that can generalize and help humans all the same.***

<div>

------------------------------------------------------------------------

</div>

Last week, I wrote about [The uncanny world of robots at home](https://democraticrobots.substack.com/p/the-uncanny-world-of-at-home-robots) and *how social support robots diving us into the uncanny valley. We don\'t need robots to look like humans.*

More recent writing from the author:

-   a [30-minute conceptual intro to reinforcement learning](https://natolambert.me/writing/2020/0826_rl.html).

-   [my writing workflow](https://natolambert.me/writing/2020/0822_writingregularly.html) and why I write as a scientist.

-   some thoughts on [meditation & a meditation journal](https://natolambert.me/writing/2020/0819_meditation.html).

Hopefully, you find some of this interesting and fun. You can find more about the author [here](https://natolambert.me). Tweet at me [\@natolambert](https://twitter.com/natolambert), reply here. I write to learn and converse. Forwarded this? Subscribe [here](https://democraticrobots.substack.com/).
