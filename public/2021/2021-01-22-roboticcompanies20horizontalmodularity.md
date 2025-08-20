---
title: "Robotic Companies 2.0: Horizontal Modularity"
subtitle: "How behaving as a platform rather than a manufacturer will be the sweet spot for the next generation of robotics companies. "
date: 2021-01-22
type: newsletter
audience: everyone
visibility: public
post_id: 31775456.robotics-take-two
email_sent_at: 2021-01-22T17:19:11.176Z
---
Data and deep learning have been changing the world for the last decade. Most robotics companies have not tapped into the *datavolution* and the mainstream vision for what robotics can be is still far from realized. The status quo for robotics companies will not achieve that dream of robots helping us with any task in any scenario (or at least trying to some degree of success), but it will create some expensive toys that are solving one problem (hint, we [have](https://www.bostondynamics.com/spot) [some](https://www.tesla.com/models) already).

The most popular robotics startups these days are the likes of Boston Dynamics, Tesla Motors, and maybe even SpaceX. All of these companies are vertically integrating a product with best-in-class autonomy to create extremely valuable products **years before their competition**. Eventually, the competition will catch up, and my interest is in the new companies that get 90 or 99% of the same ability on one task but solve a variety of similar ones all at once. The ability to solve other problems simultaneously appears from viewing problem statements that are heuristically the same (avoid crashing, locate an object) on platforms that are physically different.

The view I have for the next era of successful robotics companies is one of **horizontal modularity**, where the data sharing across systems enables to use of new sets of technologies and removes the need to solve the same classes of problems multiple times.

In this essay, I highlight how I *perceive* two of the big players in robotics development: [Boston Dynamics](https://www.bostondynamics.com/) and [Covariant.ai](https://covariant.ai/) (self-reporting bias as this is a Berkeley spinoff) and their future. There will be more examples to draw on in the coming years.

<div>

------------------------------------------------------------------------

</div>

First, a little background on the companies and their development processes before telling the story of how we get from vertical hardware optimization to horizontal modular robotics platforms.

#### Boston Dynamics

[Boston Dynamics](https://www.youtube.com/watch?v=fn3KWM1kuAw) produces amazing work at the narrow end of mobility by maximizing the performance of a **specific hardware assembly** (planning an article on them soon, and the systems they use), but it is not set up for generalization and scalability. They have engineers working on every sub-problem to get more nines of reliability. From an introductory reading, Boston Dynamics leverages very accurate simulators and models of their robot to compute the best actions with popular optimal control variants (such as [Model Predictive Control](https://en.wikipedia.org/wiki/Model_predictive_control)). This approach is hyper-focused on their platform, and there is no easy transfer of weights or modules to a new problem (some sources: [Boston Dynamics discussed their MPC at the Real World RL Workshop](https://sites.google.com/view/neurips2020rwrl) and a [decent summary from IEEE](https://spectrum.ieee.org/automaton/robotics/humanoids/how-boston-dynamics-taught-its-robots-to-dance)).

#### Covariant.ai

Meanwhile, Covariant is focusing on collecting the right data to solve a **class of problems**, such as robotic perception for pick and place. In an interview, the co-founder Pieter Abbeel pretty much said their development process is (recalling from memory):

> We are throwing everything we can come up with at the robots in the lab.

It sounds like corner case development from data rather than a control perspective. An example would be, how do we solve a robotic perception problem so that it can see and manipulate translucent objects. If the perception stack can see and identify where in space a translucent object is, that knowledge can be used for both manipulation and locomotion. Outside of the data-driven regimes of perception, Covariant does not try to reinvent the wheel and uses tried and true methods from control with the likes of PID, LQR, MPC, etc.

<div>

------------------------------------------------------------------------

</div>

## Rotating from Vertical to Horizontal Robotic Development

We start with how robots have been developed in the past. It could be best described as an **expertise dance** between hardware and software. The best roboticists had a renaissance-man vibe to them and in small teams, they would iterate and optimize the systems serially. The limiting factors here are time, expertise, and resources. 

![Robots are optimized iteratively and slowly.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c49a5e56-c406-4f6e-b6da-64c3e2074b9e_2400x1338.png)

To see how the industry can move past this approach, we need to understand that robotic systems are composed of overlapping sets of primitives.

#### Robotic primitives

There are certain skills that every robot needs to have to be able to exist as a product. Every robot needs to: interact with the world (manipulation, locomotion, etc) and see the world, often called perception. Locomotion and control can use many different blocks that include different actuators and different algorithms for deciding and planning. Perception uses many different modalities that are akin to different senses.

If we zoom in on where multiple of the robotic companies converge, they have a lot of different capabilities and almost always some overlap with related systems. Leveraging these horizontal connections in similar types of data and motion is where opportunities lay.

![A visualization of how some robotic systems could overlap in modules.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/0a7e26bd-57a3-429e-bb02-7a84f9783706_2400x1192.png)

Of course, I am not going to say this is easy to do: plugging data from another project into your own project and vice versa normally results in neither of them working. There is hope by leveraging hierarchies.

#### Hierarchy and modularity

[Hierarchical control](https://en.wikipedia.org/wiki/Hierarchical_control_system#:~:text=A%20hierarchical%20control%20system%20(HCS,form%20of%20networked%20control%20system.) and [hierarchical learning](https://thegradient.pub/the-promise-of-hierarchical-reinforcement-learning/) are fields that explicitly or automatically create abstractions in systems to improve their behavior. Having a dynamic hierarchy is crucial to the development of this vision. If parts of the system cannot be separated from each other, there is little hope for robots using solutions sourced from multiple best-in-class suppliers (luckily, computer scientists, who are becoming the next generation of roboticists, [are really the best at abstraction](https://democraticrobots.substack.com/p/models-systems-code-and-robots)).

The effect of the best hierarchy is robot-agnosticism, where some research has shown that data and methods can work on **separate robots with centralized training**. You can see these two papers to learn more (both of these papers were very well received and I have a strong inclination that this direction of research will continue): [Multi-Robot Deep Reinforcement Learning via Hierarchically Integrated Models](http://www.robot-learning.ml/2020/files/B4.pdf) or [Sim-to-(Multi)-Real: Transfer of Low-Level Robust Control Policies to Multiple Quadrotors](https://arxiv.org/pdf/1903.04628.pdf). As many roboticists are stuck away from their robots in lockdowns, the ability to share data is becoming pressing instead of just interesting.

#### Data and scaling

Looping back to the start, here is how I view the two companies I highlighted:

![Boston Dynamics and Covariant take different directions in their approach.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/28ced26a-9b56-4daf-b085-5dd8d4862a3b_2400x1525.png)

With a small variety of robots and a small number of robots streaming their data to the cloud, this is less impactful. Though there is a [clear trend of increasing the number of devices online](https://review42.com/internet-of-things-stats/#:~:text=20.4%20billion%20IoT%20devices%20will,self%2Ddriving%20fleet%20by%202035), and Covariant starts to look like a totally different proposition when there are many systems trying to solve many scenarios. Robotics seems set up to be the next field where the company with the best data delivers the best product (though, gathering and generating data in a physical world could be more of a creative and compelling task).

![The end game and key takeaway of horizontal modularity.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/3f4d9c36-dd7b-4d06-a426-6790ef638c79_2400x499.png)

This is not to say Covariant will solve all of the problems in the perception and control stack, but rather by being the best-in-class for one of the problems, their impact and value will aggregate. 

Doubling down, this approach can allow **new robotics companies to grow and deploy faster**. For example, a company with a new actuator and scenario to solve (there are always new applications for robots, just sometimes not enough creativity) can use pluggable pieces of a perception and control stack like APIs from other companies. The new player will not need to collect an abundant amount of data to use vision in their new environment, and it will serve to improve the player that they bought for any component. The company needs to solve the previously missing subcomponents, rather than building a whole new system from scratch.

The horizontal, modular companies will capture most of the value (as always happens with digital mediums), but the fast-moving, new vertical companies will deploy quickly and bring back the exciting future of robots: ***we can make anything to solve your problem***. 

<div>

------------------------------------------------------------------------

</div>

I have been spending a lot of time building a new website, which will be the home for a lot of my knowledge and thoughts on machine learning and life more broadly. [It is here.](https://www.natolambert.com/subscribe)

If you want to support this: like, comment, or [reach out](https://twitter.com/natolambert)!

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/2efd0dbd-4d23-4a05-acb5-5b8451073387_4032x2262.jpeg)
