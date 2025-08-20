---
title: "How all machine learning becomes reinforcement learning"
subtitle: "I make the case why people iteratively training any model should learn some core concerns of reinforcement learning."
date: 2021-06-14
type: newsletter
audience: everyone
visibility: public
post_id: 37397613.ml-becomes-rl
email_sent_at: 2021-06-14T18:55:27.358Z
---
*Edit 14 June 2021, 16:00 EST: I added another example of early A/B testing thanks to Victor L.*

#### Thought exercise

Consider these examples of an ML problem that has ***across-time** effects on its models*. This time-dependent function of reinforcement learning is where most of the "**core pieces**"(below) will emerge.

Consider a system that is trying to reduce the **churn** (ended subscriptions) of a paid online membership. Such a company could train a model to reduce churn on the current batch of most vulnerable subscribers (e.g. those who do not click frequently in the algorithm's replay buffer - more later), but this can come at the cost of churn of unintended users before the next model is re-trained.

More precisely, this *action* could take the form of new parameters that tune text in email subjects to individuals on an email list. This *policy* (the model that determines actions) could change the text across each registered email address, targeting a variety of email preferences, e.g. those who like emojis (many people do). As there is no free lunch in any optimization, adding emoji's would not be every user's favorite, which could be represented by the *reward* the engineer sees after this new model is deployed.This tuning could be done automatically. Though, this change could have unintended behavior of those who were currently the most loyal customers becoming annoyed --- a **[positive feedback loop](https://en.wikipedia.org/wiki/Positive_feedback)** of churn so to say.

Another example would be with **recommendations**. I am someone who watches a lot of YouTube and have seen my interests shift over time on the broader web, in the real world, and with YouTube specifically. The YouTube algorithm already shows reinforcement-like behavior (aside from the debate of how prevalent [their RL algorithm](https://dl.acm.org/doi/pdf/10.1145/3289600.3290999?casa_token=MJrmS7SMrecAAAAA:D6DrDx_MrVGy98Ct9_YCCN_5LfYdfC_1pSBr50BY9_2JzjXG5ROeBRP5x-M6FSHngTlP1GEALKdtSQ) for tuning content selections is). The simple behavior is I click on a topic I have not viewed in months or years, and the next day the amount of my feed around that topic will grow substantially. I suspect Google's model either has a heavily-weighted history term, or it allows the parameters of its recommendation engine to change rapidly. This feedback is independant of the evolution of my interests external to YouTube, so it is something that should be considered more deeply. Do you want algorithms defining who you are?

The recommendation and churn algorithm here shows a clear notion of feedback, which is an effect where your future state and dynamics evolve over time and depending on your current (and recent) state and actions.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} **Reinforcement Learning** (RL) is the field of machine learning that is formulated around an unknown world where our only signal on how to improve on a task is noisy information fed back to us from the world. This representation is normally through a *reward function*, but can be generalized to many of the signals propagating back to applications we use on a regular basis to inform them on how they are **tuning** **our behavior.**

I am not trying to say that knowing RL would easily mitigate any noticeable shifts in user-behavior in and out of the application. I am saying it may be easier to diagnose possible long-term / time-varying effects of human-facing ML tools by studying RL. Supervised learning is framed as a tool for one instance, so with the ever-changing real world, all models are outdated --- the question is how much?

<div>

------------------------------------------------------------------------

</div>

## Broader context

Large technology companies are **repeatedly** deploying large *models*, collecting *new data* from the world, and *re-training* their solutions. In the ideals of an engineer, said models would improve from new data as soon as the environment action happens (usually via a user). This sounds a lot like **reinforcement learning** (RL), where there would be a set metric that the model would seek to improve. It may not sound like reinforcement learning if the engineer doesn't let the model fully control its actions (more on this later), but the **feedback loop** core to RL is there, and the signal it provides will impact the system. These signals can compound and bias systems over longer timescales.

There are many places where the ideal conception of RL falls short. Consider this framing that is common to conceptual RL instruction (like [Introduction to AI](https://inst.eecs.berkeley.edu/~cs188/sp20/) at UC Berkeley): *an agent interacts with the world, gathers more data, and updates its policy before its next rollout*. This works for young researchers playing with toy physics problems on their computers, but not for the systems that constitute a large portion of internet traffic. These sites have a different paradigm: *a deployed model serves one task for tons of users, new data is collected, and hours to days to weeks later a new model is trained and deployed*. Model training steps in this loop can take incredible amounts of computation because there are computed on datasets easily above a million samples.

A good example of a system that could use RL in the applied setting is any form of **recommendation system**. Think of a news feed of some sort deciding which pieces of content it should serve you. This easily takes the form of a policy translating from the current user state (time, location, recent clicks) to actions (content). 

Deep learning models do many other tasks online too, including ad delivery, text analysis, image recognition, etc. Any of these models that heavily impact the user experience will then alter the resulting dataset they and their peer models are trained on in the future. For example, by deploying a more useful model for text analysis, a phone's search engine may get better, resulting in less time spent reading results and fewer loaded targeted advertisements. All of these models are constantly feeding back signals as to what the cumulative system prioritizes: *these* *signals are what determines what the next iteration of models will prioritize slightly more*. 

Zooming out, it's all one big mess of a loosely defined, multi-agent reinforcement learning system. Many policies are deployed and they're nowhere close to independent.

## The core pieces of RL's structure 

Even if the framing of RL changes there are some pieces of its structure that remain. Those key pieces mean certain core concepts and concerns of RL research will appear in these applied loops. To what extent they appear is up for debate and discovery. Given the fact that RL has been used to solve some of the world's hardest games and is prone to unintended behaviors, we should have people who have studied it monitoring these systems. **At-scale RL can be immensely impactful, so its potential for risk grows proportionally.**

Some core aspects of RL to understand include:

-   **Policy fragility** (forgetting and instability): the performance over the number of trials of RL algorithms is known to be wildly unstable --- an agent that solves the task at one iteration may do nothing intelligent at the next iteration, where it is now only a few data points and gradient steps different.

-   **Policy exploitation**: due to the narrowness of how reward functions are defined, RL often [demonstrates unintended behaviors](https://robotic.substack.com/p/rl-exploitation).

-   **Feedback** and **reward** signals: RL is conceived around the interactions of an agent or system that are fed back into the learning system. It is designed to be **trial and error** learning.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   **Mysteriousness**: RL is known to be very hard to debug and subject to numerical issues. This poses a risk for companies (but maybe less of a case in the pseudo-RL systems I am describing). 

Most of these features coalesce in my formulation because RL acts over time, where many of the other ML systems we used are trained and used in static scenarios.

A lot of people view RL as a black box algorithm thrown at toy simulated problems. This is what the research often looks like, but the lessons learned there apply to any iterative learning task where new data feeds back in an iterative manner. In this case, applied ML becomes RL in the broader sense, where we train a new model without a complete understanding of how it'll perform at test time. Those tests give us valuable new data to use at the next iteration. 

## RL out of the classroom

Two key assumptions break down when RL is taken out of a totally conceptually controlled environment. This section is addressing the idea: ***if*** most applied ML systems take on characteristics of RL, ***then*** where may the biggest differences be apparent?

The first difference between the commonly studied RL loop and what happens at these companies: **time-scale shifting**. As most model deployment infrastructure varies wildly (without even considering how most technical problems differ in scope, importance, and solution) there are different shades of how far from the common conceptualization of reinforcement learning these applications shift. Smaller companies may have relatively little data, so they can train every hour. Plenty of companies may *want* to train every hour, but they may lack the tooling to do it. The stack of taking a dataset, generating and model from it, and sending it to be user-facing is quite complex.

The two core components that impact time-scale shifting are 1) data magnitude and 2) model infrastructure. Both of these can affect the feedback of new data in the same ways: longer model update delays (assuming all the same data gets used) gives the current model more time to influence the overall training set for the next model. Time scales can be interpreted even further down the stack to the rate at which your model chooses a new action[3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}.

Next, a core difference between the study of RL in a lab to the real world: **distribution shift**. In research, distribution shift takes at most a minor role. Most tasks assume independent and identically distributed (iid) data, but in the real world, the distribution moves over time. New data will always come in, and the best solution to the task at hand can easily change over time. 

A core piece of RL systems is the notion of a replay-buffer, which is a first-in first-out (FIFO) buffer that stores recent transitions in the world. The TL;DR on a replay buffer is a data-structure used to store recent transitions --- RL agents use the samples in their replay buffer for computation. For more on replay buffers, this [paper](https://arxiv.org/pdf/2007.06700.pdf) is a modern perspective on how they impact RL.

Using the correct sized replay buffer is crucial to stable behavior (a buffer that is too small forgets needed data too fast, but a buffer that is too large prioritizes data that is no longer relevant). I suspect that the models in these systems, especially given their strong roots in supervised learning, do not have the same "learn from scratch" nature that defines RL baselines, such as those in robotics. This leads to a much more open question as to how the system handles data shift.

The core idea here is that the real world does change. It is not a simulator. There may be effects that are similar to refreshing a replay buffer in simulation, but the data from the simulation was in fact always from the same system, it was just not optimal to solve a given task. Having data that no longer represents what is true in your world is likely to corrupt a learning system in a far more detrimental way. [4](#footnote-4){#footnote-anchor-4 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

Something that is hard to pin down as the difference between RL's conceptualization and its usage in practice is the scale of the action spaces. Content recommendation or models for engagement are well more complex than a robotic task. The application of RL should transitions across domains without loss of generality if one maintains a certain baseline of faith in deep learning. The rule of thumb I have heard is that with RL a certain model or policy's data needs scale with the number of inputs or actions squared (with other factors)... so these applied systems would need all of the big data they generate. 

<div>

------------------------------------------------------------------------

</div>

## Industrial ML Loop

What companies actually deploy and how varies dramatically across the technology landscape. For example, big players like Google and Facebook have built their own model training, deployment, and monitoring stack. Meanwhile, there are many, many startups trying to build tools to improve pieces of the model deployment stack, such as model deploying, updating, efficiency, etc. (not my area of most understanding).

These large tools do not act in a black box. They impact our individual and societal behaviors greatly. This impact causes the underlying data the companies train on to change. *How long companies wait to update the model can make a certain error in model behavior become more prevalent in data used for the next training loop* --- **reinforcement**. 

It is also crucial to remember that the scale at which Google and Facebook operate is so beyond what is mentally tractable. It is impossible for humans to sift through, annotate, or understand all the data they receive. Without a doubt, there are many unintended behaviors that occur every second. Large datasets also need more time to train policies, so updating with every sample is practically impossible. Even with this scale, there is a huge push to move fast because user attention is highly competitive across digital services.

I've heard of two examples of industrial bloopers in model training and deployment, and there are surely more (note: accuracy of these may not be perfect, I could not find blog posts clearly describing them after conversations with others in the applied-ML space). These are not from RL deployments, but it is cool to think about how such issues can translate to an RL paradigm:

1.  *Early[ A/B test](https://en.wikipedia.org/wiki/A/B_testing) stopping at* **Facebook** (also see this [post](https://multithreaded.stitchfix.com/blog/2020/08/05/bandits/) from Stich Fix --- they have a great data blog and likely team): A/B tests are used to determine which feature change is best. In the case of ML, a company can use two models and determine which one is the best. These tests operate for a set amount of time to help avoid numerical difficulties (like a P-value), but Facebook's engineering culture had a habit of stopping tests early when they seemed obvious. This served to reinforce both the engineer's biases and more importantly to this article, the models they perceived as being "better." Depending on how long this proceeded and under what time-scaled they fed back the results into new models, different RL properties could emerge.

2.  *Losing model training sets at* **NextDoor**: I heard that there was a period of time where the NextDoor engineers did not know which model resulted in which data. Practically, this means that they did not store model training properties in enough detail, which can relate to a bunch of wild potential framings. For example, this could be akin to RL without policy checkpointing (saving what the parameters are at each training step, and what replay buffer resulted in it). Anyone who works in RL knows that this would be suicidal for any challenging problem. \
    \
    It's like re-training a policy and throwing away all the past ones, or keeping one training dataset that could get corrupted by the new policy(without easily knowing when). Either of these options is dire from an RL engineer's perspective who wants to keep track of peak behavior, so they can go back and re-fork the policy from there. Without doing so, there is a huge potential for bias and model exploitation as unintended behaviors can get reinforced in the underlying dataset before the engineer notices. 

The thing is, NextDoor cannot be the only one making these *doh* errors. Plenty of engineers cut corners, and knowing the patterns at play in your system will make it easier to return to the desired operation. 

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/7c95fa11-8be8-4610-8835-2e59f119cca9_3823x1500.jpeg)

<div>

------------------------------------------------------------------------

</div>

The RL paradigms we discussed:

1.  **Coursework RL**: *an agent interacts with the world, gathers more data, and updates its policy before its next rollout*. 

2.  **Applied ML Reduction to RL**: *a deployed model serves one task for tons of users, new data is collected, and hours to days to weeks later a new model is trained and deployed*.

Let me know if you have seen anything that may have looked like this, where it may fall short, or anything. This is an idea I have been trying to work out, but it seems inevitable that it will play out to some extent. If not, then we will have to just make RL so good that everyone uses and acknowledges it directly. 

Important to making RL work in situations like this is the growing field of batch RL that is designed to operate in a slower update frequency manner of the applications I have discussed. It takes all task data to date and extracts a new policy --- such policy extraction can happen whenever the deployment engineer wants.

*Acknowledgements: thank you to Vikram Sreekanti for helping me formulate this post and fixing some typos.*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
An additional feature that makes me think Google may be using RL here is that there seems to be random videos that come and go on my feed with no pretext, which seems like the algorithm exploring to find what I like.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
I am very interested in the relation of **feedback**, mostly from a control theory perspective, to modern learning systems. I think there is a lot to learn there, so if you have ideas, [let's talk](https://www.natolambert.com/contact)!
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Interestingly for me, time-scale shifting takes another key form in robotics research: *setting the control frequency of your robot*. While most simulated RL tasks are disconnected from the true time it takes to compute your action (often called wall-time), performance on real-world tasks is intimately related to the rate by which new actions are computed for the robot to execute. This affects the system in two ways: 

1.  First, a slower control frequency can change the dynamics of your system, often making them more unstable (barring a discussion on Eigenvalue placement, state feedback, and more).

2.  The control frequency you set, especially when viewed in terms of the period, determines how long the agent has to compute its next action. Especially with expensive controllers like Model Predictive Control (MPC), this is core to the question of it the task at hand **can** be solved.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[4](#footnote-anchor-4){#footnote-4 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
For example, in robotics research, I have been recommended to try and collect all of my data in one sitting to avoid this. I would guess that deployed robot-learning solutions are designed for one industrial application that should not change in the lifetime of the model.
:::
::::
