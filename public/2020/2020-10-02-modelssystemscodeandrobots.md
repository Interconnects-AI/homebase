---
title: "Models, Systems, Code; and Robots"
subtitle: "EE v ME v CS in complex systems. Do we view things differently?"
date: 2020-10-02
type: newsletter
audience: everyone
visibility: public
post_id: 6011441.models-systems-code-and-robots
email_sent_at: 2020-10-02T14:00:54.704Z
---
The best teams for robotics are not all computer scientists --- they have electrical & mechanical engineers, computer scientists, robots, and more to fill the cracks. This post is an exploration of how different ways of thinking contribute to robotics --- and by extension to many software engineering projects.

> How would you summarize the overarching conceptual theme of your undergraduate major? One sentence.

(*You can reply below, or in this email, do it! See how your answer compares.*)

<div>

------------------------------------------------------------------------

</div>

## Seeing models

I don't characterize EE primarily by circuit design nor nano-fabrication. It took me a long time to figure out what was different between my degree in electrical engineering (EE) and a similar computer science degree. So many of my classmates get software engineer (SWE) jobs regardless, are we really different? I know the courses are different, but there's a chance that the courses teach the same concepts in a different curriculum and timeline.

So, one asks, how are EEs different? They learn to see the world in models. All of the different tasks we engage in have a different set of assumptions and tools. We need to be careful with and understand where the model we are using is true and where we may be hurting performance (in the form of uncertainty). Circuit design has a model in the form of a Cadence library for a specific fabrication run, microelectromechanical systems have models normally grounded in physics (but many other things effect the final device), signal processing uses models to determine what information they see and send, and more.

The mathematics of the major, such as Fourier transforms, wavelets, electromagnetism, and more are different sets of models. These analyses require a large underpinning of mathematics to teach (linear algebra, multivariable calculus, and probability) when compared to deep learning (\`import Keras\`). The rigor of learning these contained systems makes EEs view machine learning models with their limitations in scope.

This way of seeing the world in models is becoming even more valuable as every company tries to throw machine learning ***models*** at new problems. My lab group is almost entirely EE-type people, and the scientific, constrained way of thinking will help in way more systems than traditional EE design spaces.

Maybe send this to a friend who did EE and you had no idea what that meant?

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/194a2178-8875-449a-be65-db2878fb97d3_2544x1324.png)

## Thinking in systems

Along with seeing the world in models, most things that are made today are a cog in an incredibly complex series of interconnections. In reality, most engineers work on one piece that has many downstream effects (consider, for example, how [recommender systems affect way more than just the user](https://democraticrobots.substack.com/p/recommendations-are-a-game-a-dangerous)). This is a complex form of unmodeled ***dynamics*** (or a disturbance, some fields would say).

The mechanical engineers I know today have intuitions of the parts of the systems they have no control over. Making a piece of hardware? They think about what it will be touching and how that informs design. It's kind of the way of thinking where nothing you make lives in a bubble.

I don't have a full grasp here, as I wasn't a mechanical engineer, so I am curious what people can help me fill in. I have a hunch that thermodynamics, control theory, statics, etc have overlapping themes from above in EE, but my impression was that *how mech-e's are trained to think and approach things was a little different*. This difference in approach is where the value of adding both a mech-e and EE falls.

It's almost as if covering the same type of subject matter with a different frame of reference helps with redundancy. I would also loop chemical engineering into a lot of themes discussed in this section. Ultimately, it's pointing towards a discussion of computer science vs engineering, that we will be having more in the next decade.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/8ad0faa1-6cf5-4f8a-8c1f-6fe58b340878_4000x1400.jpeg)

## The sky is the limit

The best thing I have found when working with full-on computer scientists is their optimism. Software is changing the world (or, call it magic), and there are people who believe they can build anything. The culture of optimism and hacking does have it's merits.

I think computer science also builds strong themes of ***abstraction.*** Whether it's software abstraction (the common way) or system hierarchies, there are some really elegant solutions in the area of computer science. I would say that I am bearish on the rate of development of things like set theory, fundamental algorithms, compilers, etc when compared to the general trend of the growth in CS and broadly in artificial intelligence. This divergence from theoretically grounded areas and instruction in structure formulation of thoughts towards implementations and making things (in the formal period of education --- which has huge value), will define the future of computer science. I want to keep an eye on how smaller liberal arts schools teach computer science when compared to the corporate money grab of schools like Berkeley and Stanford.

Schools that made their own computer science department will be happy they did going forward. Due to the prevalence of the tools in society, the enrollment numbers are going to keep rising. That's the first layer point. Next, by separating the schools people will better realize that there is a different way of thinking in these groups. Computer scientists deserve to be able to [move fast and break things](https://en.wikipedia.org/wiki/Facebook,_Inc.#History), but the things that are being broken cannot be the fabric of our society.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/485e6a1a-dd71-4d12-bc51-b300b1046cf9_5760x2648.jpeg)

## Intangibles

Building anything at scale needs people not just trained in engineering. Maybe someone who is self-taught will fill some cracks in "what practically works" or (engineer superiority-complex trigger warning) people who were not trained as engineers still have valid input when engineering products.

A lot of the benefits of intangibles will play out over years. A take I like is, what if someone designed a recommender system that wants to try and make the user feel good about themselves. This is not the short term revenue play (conflicts with VC model), but I think a company that started this 5 years ago would be help on a golden platter by all tech journalism now and would be financially invincible (stock market game).

<div>

------------------------------------------------------------------------

</div>

# Putting it together

Robotics is a weird field. The variance of what people actually do is so high. It is a more obvious case of where we need a diverse way of thinking, but the same trends end up applying.

As a researcher, I spent my first "productive" months chasing after a drone, so when it hits the ceiling, detects a collision, and turns off I can catch it so it does not crash into the ground and make me re-assemble and start from ground zero.

-   Or, I have a friend that was trying to attach electric motors to the stem of a bicycle and make autonomous bikes (got swallowed into the micro-mobility crowd). 

-   Or, you have researchers at Amazon that manage their warehouses with many "simple" robots and, I am kidding, [raised injury rates.](https://www.theverge.com/2020/9/29/21493752/amazon-warehouses-robots-higher-injury-rates-report-reveal)

-   Or, you work in a laboratory focused on deep reinforcement learning and the metric of success is beating a baseline on a computational task.

These are all valid answers, but I am trying to disambiguate what it means to be a roboticist. I am trying to make sure people see that we need a huge variety of people to solve these problems.

The leap of faith is to see that we need more than just computer scientists to build products (even if they're not physically embodied). What starts as a software-only project is going to grow if it's successful, and with that growth will be a likely ill-prepared team if there is no diversity of thought in how it's made. I'm not going to point out the ethical and implementation failures of recent ML systems, but they are prevalent. Cross-pollination of thought helps these malicious angles be snuffed out.

<div>

------------------------------------------------------------------------

</div>

Hopefully, you find some of this interesting and fun. You can find more about the author [here](https://people.eecs.berkeley.edu/~nol/). Tweet at me [\@natolambert](https://twitter.com/natolambert), reply here. I write to learn and converse. Forwarded this? Subscribe [here](https://democraticrobots.substack.com/).
