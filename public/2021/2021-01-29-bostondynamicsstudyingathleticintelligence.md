---
title: "Boston Dynamics 🤖🐈: Studying Athletic Intelligence "
subtitle: "The acrobatic dance videos are flashy, but what are the actual technical breakthroughs? What is happening to the Korean robotics industry?"
date: 2021-01-29
type: newsletter
audience: everyone
visibility: public
post_id: 31894313.boston-dynamics
email_sent_at: 2021-01-29T13:52:31.991Z
---
The robotics company that has a knack for viral technology videos showcasing [little things robots can do](https://www.youtube.com/watch?v=VRm7oRCTkjE), [parkour](https://www.youtube.com/watch?v=_sBBaNYex3E),[ bullying](https://www.youtube.com/watch?v=aFuA50H9uek) [robots](https://www.youtube.com/watch?v=aFuA50H9uek), and [more](https://www.youtube.com/channel/UC7vVhkEfw4nOGp8TyDk7RcQ). A central tenet of Boston Dynamics is the idea of **athletic intelligence** --- movement patterns that are robust, flexible, and maybe even human. These videos and technologies have gotten to the point where the most [popular technology entertainer got a copy and reviewed it](https://www.youtube.com/watch?v=s6_azdBnAlU), they are for sale, and accessible. The most recent video was trying to showcase a new *human* style of movement (below). 

Their focus on athletic intelligence really helped me understand the company, where it fits in with their videos, and why the owners don't stick around. Boston Dynamics uses machine learning and artificial intelligence as a tool in an engineering stack, rather than throwing it at every sub-problem they encounter.

In this issue we:

-   *clear up the history of Boston Dynamics (it isn't a government contractor)*,

-   *showcase the breakthroughs in their so-called **Athletic Intelligence***,

-   and *discuss what is next for the Hyundai subsidiary*.

:::::::: {#youtube2-fn3KWM1kuAw .youtube-wrap attrs="{\"videoId\":\"fn3KWM1kuAw\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=fn3KWM1kuAw){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

<div>

------------------------------------------------------------------------

</div>

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/e011eff4-1982-4ca1-8941-c8a46582f92a_442x114.png)

## What is Boston Dynamics

Boston Dynamics ditched all DARPA contracts in 2014 (they were started with DARPA seed funding, but tons of [technology we use was](https://www.darpa.mil/about-us/advancing-national-security-through-fundamental-research)!) They have a somewhat convoluted history of buyers and sellers including Google, Softbank, and now Hyundai--- I think this is mostly a disconnect between their long-term goals and the shorter-term values of markets. The long term goal of Boston Dynamics is to create a demonstration of athletic intelligence and sell that to people who can solve other cognitive problems (planning, logistics, interaction). 

Athletic intelligence is the goal of making the combo of robustness and velocity possible in robotics. If this does not seem impressive to you, check out some [historical examples](https://www.youtube.com/watch?v=g0TaYhjpOfo) of the best robotics teams in competition.

Something I hear a lot (and I have perpetuated part of this idea) is that their technologies are partially funded by and fully designed for military applications. While their robots seem robust in their own environment, they do not fill many trends of what 21st contrary warfare will look like: remote, stealth, and robust when damaged (their robots are loud --- those big hydraulic actuators are not sneaking up on you!). For a full history, see [Wikipedia](https://en.wikipedia.org/wiki/Boston_Dynamics), [their about page](https://www.bostondynamics.com/about#Q2), another [longer history](https://techstory.in/the-boston-dynamics-story/) write up, or some more personal comments from [Raibert](https://www.boston.com/news/technology/2021/01/21/boston-dynamics-dancing-robots-video) in a Boston paper. 

All in all, they have stayed focused on their goal of pushing the limits of legged locomotion by jointly developing hardware and software capabilities. They have struggled with how to monetize this advancement.

![A very cool rendering from their talk overlaying the perception and planning algorithms.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/47263398-5245-496e-906d-f92c6fa67cb0_2780x1550.png)

<div>

------------------------------------------------------------------------

</div>

## Athletic Intelligence with Machine Intelligence

In this section, I highlight how their magic happens. The hardware development they have done is top-notch, but the machine intelligence in the part that is [potentially scalable to many, many more platforms](https://democraticrobots.substack.com/p/robotics-take-two), so I focus on it. In short, their learning and control infrastructure is not revolutionary compared to the state of robotics research, but it is well-developed and highly-functional. Let's hope for Boston Dynamics' future that their control methodology is not too linked to their hardware platform and that they can repeat the control engineering.

Broadly, athletic intelligence entails developing low-level control and agility in locomotion above all else. This agile robotic motion **is the core of the companies value**. They study how mechanical pieces like hydraulics should be optimized to improve the control performance. They integrate precisely the sensors they need (LiDAR, motor encoders, IMUs, etc.) to solve the task and a many different computations. 

At the NeurIPs 2020 [Real-world RL workshop](https://sites.google.com/view/neurips2020rwrl), they presented the high level of their approach (video [here](https://bostondynamics1.app.box.com/s/w4tpxw3rb0jx7co9lyn9clxz42rtx028)). The slide on control methodology summarizes their toolset: model-based, precomputation, and careful engineering (the piece that research labs miss).

![The three pillars of their control approach: model-based, compute offline, and be rigorous.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/5c6efa92-1391-4df6-bf3b-64007e7b6097_3360x2100.png)

#### Model-based

*All models are wrong, but some are useful* is the gist of their slide here. 

In reality, there is an interesting interplay because they can model some aspects of their robotics (e.g. one type of hydraulic actuator) in great detail, but as they start to put pieces together the cumulative model has gaps --- and it is impossible to know exactly where. 

The model is also a great tool where humans are going to be in the loop (can interpret results), but there are no laws that say model-based methods are more effective. They're using it closely with the second point on the slide.

#### Precomputation

With model-based is the pairing, precomputation, that together make the tool of simulation. Simulation is the future of robotics (infinitely cheaper than running hardware experiments, especially in pandemics), and they seem to have leveraged it to great effect. 

The conversations at the real-world RL workshop highlighted the extent to which they leverage model predictive control (MPC), which is known as being one of the most computationally heavy approaches to control these days. Though, recent work has been shifting for MPC to be solved offline, and then run a simpler version online (they did not confirm this, but the answers point to at least something conceptually similar). In practice, this becomes: collect a lot of states from real robot trials, then solve for an optimal action at every possible state offline and run the controller reading those actions (really fast).

#### Rigorous logging

They use data-driven to mean a different thing here, "the data doesn't lie," which is actually much more common in EE and ME circles (pre deep learning hype, Choo Choo).

Something I think a lot of areas of RL could learn more from is analyzing exactly what happened in every trial. It is one thing to know that the agent was wrong, but figuring out why it was wrong and how the errors propagate over time is very important. Boston Dynamics is first and foremost not a machine learning company, and this is matched in their approach. 

### Making the new robot dance move

It's worth illustrating how they used motion capture, imitation learning, and rich simulations to made their recent video. To elaborate in more detail to what is in the figure below, they have human actors create movement primitives in recording environments (or specify movements in a physics simulator, which doesn't seem very athletic), use techniques from imitation learning to generate a policy to match the motion, and then have the simulators set up correctly so the new policy transfers to the robot easily.

![A slide from their real world RL workshop talk on data-driven MPC and general robotic agility.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/95c279b1-06e2-4ec5-9532-13bf05eb35c0_3360x2100.png)

From [IEEE Spectrum](https://spectrum.ieee.org/automaton/robotics/humanoids/how-boston-dynamics-taught-its-robots-to-dance):

> eventually we were able to use that toolchain to create one of Atlas' ballet moves in just one day, the day before we filmed, and it worked. So it's not hand-scripted or hand-coded, it's about having a pipeline that lets you take a diverse set of motions, that you can describe through a variety of different inputs, and push them through and onto the robot.

I only have one idea for what the bigger picture could be: pre-programming motions that a customer wants for a specific industry engagement. You want your Spot-with-arm fleet to be able to pick up packages of a certain dimension --- let us see if we can **validate** that motion and update your robot. Having a framework where the designers are confident enough in the output that they can ship it via software update would sound a lot like why so many people love their Teslas (software updates on hardware don't really exist).

They put a lot of engineering time into these movements. It's worth thinking more about what bigger picture motivation is here (it cannot just be videos). If they are trying to sell the robot in any human-interactive format, a richer set of movements could be very valuable, but nothing to date points to this. The human-style dance was likely pushing the limits of a package, maybe the new one they are announcing on February 2nd.

#### Artistic Emphasis and the Uncanny Valley

Making robots look human is something to be wary of. Of course, human movement is dynamic, elegant, and extremely efficient, but it does not mean that it is ever optimal with different actuators. Human **style** also would carry immense cultural baggage and unintended effects. 

This is not to say that I am against robots with human **function** --- society is structured around beings with our legs and height navigating buildings and solving routine tasks easily. What I propose and hope for is robots that take modules of human movement (such as using two legs or having arms with a hand and wrist-like entity), but do not target total emulation. 

If you're curious about this, read my [piece on the uncanny valley](https://democraticrobots.substack.com/p/the-uncanny-world-of-at-home-robots).

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/4991da12-7b5f-4095-9a96-b4e369dff73b_5184x3456.jpeg)

### Leveraging more learning

The slide with opportunities for learning is on point. Continual learning, model accuracy improvement, learning-based hardware optimization, and engineering assistance are all in the set of problems that learning can be helpful with today. 

1.  Continual learning fits very nicely with model-free RL --- it is a system designed to learn from sparse rewards with no goal of transfer to other tasks.

2.  Model accuracy in the real world comes down to fitting data to a disturbance, or the delta between the dynamics models they already optimized to get the initial agility and the observations from the onboard sensors. Simulation and physics to get the initial model, data, and machine learning to update it to match recent reality.

3.  Hardware optimization with ML: humans are really bad at fitting multi-objective functions. When you are making physical devices the cost increases via materials and time, let machines do this for you (see [something I am working on](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fnatolambert%2FJNRgSdmxXP.pdf?alt=media&token=da95c4f0-ccf6-4d80-bf76-7d84dd11a71f).

4.  Engineering descent. I love their term, I think this is just *filling in the cracks* so to say, and a nod that learning **can** be useful, even for a company so grounded in real deliverables. 

![The company seems to have a healthy relationship with learning. Healthy enough to present two out of many slides on machine learning at a machine learning conference.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/5d2502b7-1d26-4012-bfd6-1f04004f044e_1654x932.png)

<div>

------------------------------------------------------------------------

</div>

## What's next for Boston (Hyundai) Dynamics?

South Korea has a set of [cultural values](http://www.bbc.com/travel/story/20171205-why-south-korea-is-an-ideal-breeding-ground-for-robots) making it ripe for the proliferation of robotic agents in multiple spheres of society. An [analysis of a report](https://internetofbusiness.com/south-korea-automated-nation-earth-says-report-uk-nowhere-robotics/#:~:text=South%20Korea%20has%20by%20far,eight%20times%20the%20global%20average.&text=The%20US%20has%20189%20robots%20per%2010%2C000%20employees%2C%20placing%20it%20seventh.) (I know, double reference, painful, but so is doing industry research on robotics --- it's all hidden) from the [International Federation on Robotics](https://ifr.org/) concluded:

> South Korea is the most automated nation on earth.

### Korean Spirituality & Robots

More interestingly, as a Korean engineer [claim](http://www.bbc.com/travel/story/20171205-why-south-korea-is-an-ideal-breeding-ground-for-robots)s:

> Any kind of non-human being might have a spiritual or super power beyond human capacity.

This is just one view, but history points to a set of values that are more open and optimistic of other beings. This feeling is definitely grounded in animals, but a small portion translating to robots can substantially restructure the society.

The story of [Dangun](https://en.wikipedia.org/wiki/Dangun), the first king of modern South Korea, and Korea's affinity for animals and potentially spiritual non-human creatures is fantastic:

> A tiger and a bear prayed to Hwanung that they might become human. Upon hearing their prayers, Hwanung gave them twenty cloves of garlic and a bundle of mugwort, ordering them to eat only this sacred food and remain out of the sunlight for 100 days. The tiger gave up after about twenty days and left the cave. However, the bear persevered and was transformed into a woman. The bear and the tiger are said to represent two tribes that sought the favor of the heavenly prince.
>
> The bear-woman (Ungnyeo; 웅녀/ Hanja: 熊女) was grateful and made offerings to Hwanung. However, she lacked a husband, and soon became sad and prayed beneath a \"divine birch\" tree (Korean: 신단수; Hanja: 神檀樹; RR: shindansu) to be blessed with a child. Hwanung, moved by her prayers, took her for his wife and soon she gave birth to a son named Dangun Wanggeom.

From this, Korea has more openness to non-human creatures and the values they can bring. What a great change --- Americans can't get away from the quagmire of social media regulation and thinking their speakers are listening. 

### Korean Practicality & Robots

[Hyuandai recently acquired Boston Dynamics](https://www.therobotreport.com/hyundai-acquires-boston-dynamics-for-921m/) (and from [The Verge](https://www.theverge.com/2020/12/11/22167835/hyundai-boston-dynamics-aquisition-consumer-robotics)) and [Bloomberg shows the company is not consistently profitable](https://www.bloomberg.com/news/articles/2020-11-17/boston-dynamics-needs-to-start-making-money-off-its-robots#lazy-img-366074900:~:text=It%E2%80%99s%20had%20bouts%20of%20profitability%20over,it%20did%20its%20previous%20owner%2C%20Google.). Repeated sales and low profitability is not a good sign for a company (and maybe being in [Softbank's fund](https://techcrunch.com/2020/04/13/softbank-expects-24-billion-in-losses-from-vision-fund-wework-and-oneweb-investments/) is a bad sign for companies), so *what's next*? 

So why did Hyundai buy them? To use the robots for manufacturing. This is a big shift that I think most people didn't see coming (flashy, agile robots are at a first glance a best fit for high-end consumer and niche products). [Hyundai Heavy Machinery entered the market for selling many classes of robots in 2020](https://control.com/news/a-look-into-hyundai-robotics-latest-efforts-in-automation/) and they claim to be [Korea\'s number 1 robot manufacturer](http://www.hyundai-holdings.com/hhiholdings). Some important context is that Korea already has a high concentration of industrial robots per their population (see this [background on Korea\'s Robotics Industry](https://roboticsandautomationnews.com/2020/02/03/south-korea-reaches-new-record-of-300000-industrial-robots-in-operation/29454/)). 

The locomotion primitives Boston Dynamics has made in Spot and Atlas really are things people can build on. Athletic intelligence in manufacturing translates into robustness, which is extremely valuable. It is just less publicly-exciting than agility.

### New products

There is a new [product line announcement for February 2nd](https://www.youtube.com/watch?v=WvTdNwyADZc) expanding Spot's offerings. I expect this to be variants on hardware (think different arm attachments than just the single-arm showcased in videos) and different software packages that can solve tasks like exploration or more complicated locomotion challenges.

In interviews and in product, Boston Dynamics really seems like more of a research lab pushing the limits of synergized hardware-software design for legged locomotion. I like this from what they do for the field, but in reality, I expect more monetization for a few years and maybe less publicity as they become an industry research lab.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/6b34c1e9-d0e2-4174-9ebc-41773d825cb7_4032x1808.jpeg)

## Wrap

Boston Dynamics is an important company driving excitement and investment in robotics. I would not invest in them, though, and that is okay. As an athlete, I am drawn to their ideals around athletic intelligence, but as a researcher, I am really more interested in practical intelligence. It doesn't matter if a robot can do parkour if it cannot pick up a new object or make coffee. Hopefully, Hyundai adds a translational arm to their shiny new research organization.

I'm also thinking about re-branding this blog into something snappier. The themes won't change, but it could help with growth. Let me know if you have any comments.

<div>

------------------------------------------------------------------------

</div>

I made a [new website](www.natolambert.com) where you can learn about learning, robotics, and me.

If you want to support this: like, comment, or [reach out](https://twitter.com/natolambert)!
