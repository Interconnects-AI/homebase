---
title: "on the Horizon of applied RL"
subtitle: "How RL is starting to be used by industry and how RL is heading to a framing more suited for industrial scales."
date: 2021-08-02
type: newsletter
audience: everyone
visibility: public
post_id: 37413686.applied-rl-horizon
email_sent_at: 2021-08-02T18:46:01.396Z
---
Reinforcement learning (RL) --- the computing realization of trial and error learning --- is touted because it can be framed to solve problems that humans do not know how to start. It is the current leading candidate to lead towards general intelligence (especially according to DeepMind). Transitioning RL from toy robotics problems to real-world niches to at-scale integrations is one of the technical challenges I will be following most closely in the next decade. There are signs that people are moving in these directions, where methods are either designed for or mirror assumptions needed to operate reliably at scale. 

The leading player in RL research these days is Google, which applies this to small projects in their research lab, in [public](https://ai.googleblog.com/2020/04/chip-design-with-deep-reinforcement.html)-[relation](https://deepmind.com/blog/article/deepmind-ai-reduces-google-data-centre-cooling-bill-40) [efforts](https://www.nature.com/articles/s41586-020-2939-8) in their parent company, Alphabet, and in their RL-moonshot lab, DeepMind. The most detailed, and non-hype-oriented report I came across regarding applied RL came from the company constantly nipping at Google Research's heels: Facebook.

## Facebook's applied RL

A couple of years ago, Facebook released a platform for Applied RL: [Horizon](https://arxiv.org/pdf/1811.00260.pdf), and they have been continuing to update the paper. The content of the paper has not changed substantially, but given that it is on its fifth version, its statements can be regarded as more precise. What companies like Facebook intend to do with emerging, novel technologies matters for the field and drives substantial investment (regardless of academia). [1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/3a2a8633-11ce-46fa-8ac2-953c37001cf5_5041x3364.jpeg)

As with any paper, when reading the details of the methods, most of the content goes somewhat over my head. Sporadically it seems like those sections are as much there for impressing readers from adjacent fields as much as conferring information to reviewers and the field. In particular, this paper discusses features that are useful for at-scale system integration but are not components researchers would often focus on. These details are insightful for what it takes to use RL in the real world (the paper was originally presented at a real-world RL workshop, for that matter).

The abstract points to what is covered, but it is also directly related to a problem I highlight in my, **[How all machine learning becomes reinforcement learning](https://robotic.substack.com/p/ml-becomes-rl)**. Recall:

> The first difference between the commonly studied RL loop and what happens at these companies: time-scale shifting. As most model deployment infrastructure varies wildly, there are different shades of how far from the common conceptualization of reinforcement learning these applications shift. Smaller companies may have relatively little data, so they can train every hour. Plenty of companies may want to train every hour, but they may lack the tooling to do it. The stack of taking a dataset, generating and model from it, and sending it to be user-facing is quite complex.\
> \
> The two core components that impact time-scale shifting are 1) data magnitude and 2) model infrastructure. Both of these can affect the feedback of new data in the same ways: longer model update delays give the current model more time to influence the overall training set for the next model. Time scales can be interpreted even further down the stack to the rate at which your model chooses a new action.

The authors' state: 

> Horizon is an end-to-end platform designed to solve industry applied RL problems where datasets are large (millions to billions of observations), the feedback loop is slow (vs. a simulator), and experiments must be done with care because they don't run in a simulator.

The first two lines match up very closely with my ideas on time-scale shifting caused by many engineering differences. The end of the sentence is a gentle nod to *how ethically gray the idea of applying RL in the wild is*, due to the concept of [exploitation](https://robotic.substack.com/p/rl-exploitation).

The authors go into very specific details of what they identify as core features of applied RL libraries: Data Preprocessing & Feature Normalization, Distributed Training, Counterfactual Policy Evaluation, and Amazon EC2 Integration. These features are primarily concerned with how RL is deployed --- *often, I am more interested in how RL affects the larger systems it is a part of*. All of these items except **counterfactual policy evaluation** seem generic to machine learning, and less interesting to examine (though they did have to build this system and I am sure they learned where these systems conflict with the goals of RL, such as the rate of parameter updates in RL). Counterfactual policy evaluation is a key feature in the framing of RL I have been building on this publication.

## Moderating RL

Counterfactual policy evaluation, and many other phrases in this paper, relate to the crucial question of **how do we actually get the reinforcement learning systems to do exactly what we want**? The following quotes are from the [paper](https://arxiv.org/abs/1811.00260):

> Unlike in pure research settings where simulators offer safe ways to test models and time to collect new samples is very short, in applied settings it is usually rare to have access to a simulator. 

It is interesting to note that applying RL to digital domains will likely have very different challenges than most RL research that is positioned in the real of simulated or real-world rigid body dynamics (robotics). A controller in a digital regime could move much, much faster than one with physical time constraints, but simulating a social network is even harder than physical motion. 

> This makes offline model evaluation important as new models affect the real world and time to collect new observations and retrain models may be days or weeks. Horizon scores trained models offline using several well known counterfactual policy evaluation (CPE) methods. The step-wise importance sampling estimator, step-wise direct sampling estimator, step-wise doubly-robust estimator (Dudık et al., 2011), sequential doubly-robust estimator (Jiang & Li, 2016), and MAGIC estimator (Thomas & Brunskill, 2016) are all run as part of Horizon's end-to-end training workflow.

This is an ensemble of mechanisms to predict policy performance offline. Given a trained policy and a replay buffer, these numerical tools estimate the downstream reward. This is a mitigation technique of the sim-to-real transfer from replay buffer data (the ultimate model of the world lies in the data) to the real-world application. To my knowledge, they do not have any way to make these bounds true with distribution shift (a constant problem in the real world).

A key missing point is where or not the reward that is intended to be optimized is ill-formed or not. Something I am formulating is the idea that RL practitioners should study something akin to "reward responses for reward specification" (think [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) or [Datasheets for Datasets](https://arxiv.org/abs/1803.09010)). 

### A few more interesting points 

I found a few more sections of this paper interesting to think about when deploying RL. For example, the authors included details regarding another trick they use to reduce the sensitivity of RL:

> As an implementation trick, we use a proportional integral derivative (PID) controller to tune the threshold used in the RL policy. This helps to keep the RL policy's action distribution inline with the previous production policy's action distribution.

Essentially this is avoiding doing precise low-level control with RL because RL may cause too much exploitation. When you see a simple addition like this it is because the simplest attempt did not work or was actively harmful --- in this case, end-to-end learning where RL directly determines the actions.

Next, the authors glean some details into how they actually train these RL models. There is no way to know what the baseline will be for model-update-frequency when RL starts to get used for more in the industry.

> The model was incrementally retrained daily on data from people exposed to the model with some action exploration introduced during serving. The model is updated with batches of tens of millions of state transitions. We observed this to help online usage metrics as we are doing off-policy batch learning.

To me, this sounds like they threw RL on top of their existing content delivery AI that was re-trained every day, but maybe the change in problem formulation helped them eke out more performance:

> We observed a significant improvement in activity and meaningful interactions by deploying an RL based policy for certain types of notifications, replacing the previous system based on supervised learning.

It is interesting to think about these small deployments of RL (there is also a [paper](https://dl.acm.org/doi/pdf/10.1145/3289600.3290999?casa%5C_token=RbKbt-uYqJsAAAAA%3ATayeHpEk-gMvpz7eqNx9CHE9yLJ1WE-Jk6lZpyoHd5JzX8%5C_BFpOBKf%5C_KzpIx4TgJ3REPnXx754%5C_M1A) on high-dimensional policy gradient at Google). To me, this is becoming a question: *Given that gradient-based optimization empowers the largest deep learning success, is that indicative that RL agents can scale further, or the optimization's success a function of the data format?*

<div>

------------------------------------------------------------------------

</div>

## ML Operations: moving infrastructure to real-time

So it turns out machine learning operations --- the processes that deploy and maintain models on our devices and services --- are turning into a bit of a meme with #MLOps filling many bios on Twitter. It is a huge field that is entirely warranted in its interest, but it seems like it is somewhat laughed at (from people I know *in the field* because of its inconsistency). 

Consider, this [fun piece](https://marksaroufim.substack.com/p/wild-west-ml-ops) that will take you on a journey through its pitfalls. I include this because everything will get worse when companies intentionally deploy RL at scale. Infrastructure will go from that which is designed to easily and efficiently deploy models (and update them sometimes) to systems that need to be regularly updating models all of the time. For example, websites will update certain models (like user churn estimates) every day. Many current RL algorithms are designed to update their models and resulting policy after every trial or episode (which is not easy to define in industrial settings).

A certain new variety of RL research does lend itself to being a useful step for translating state-of-the-art RL to existing ML infrastructure: batch RL. It moves toward the direction of expensive policy updates on every step to policy updates when needed.

## Batch RL: moving RL to match current infrastructure

Batch reinforcement learning, also re-coined as offline reinforcement learning, is the hot field of how to generate the best possible policy from a large dataset of world interactions. Think of it as the question of *if I am given a large dataset of transitions from one or many agents solving a task, how do I extract the best policy*? This tends to happen after some learning or data collection process, but this idea of policy extraction, or **collect and infer**, has some serious potential.

Batch RL keeps the open-ended trial and error learning framing that is so intriguing but aligns it more closely with existing ML operations.

A couple of other intuitions and framings for batch RL come as follows (hopefully one of them gives you an, *aha, I see how that could be useful for industry* moment:

-   Reduction of "normal" RL without more data collection: our agent happens to be stuck and can't update its policy in normal ways, what is the new policy we should use? This was the framing I was stuck on until I saw its potential.

-   If we have collected a lot of data in the past for this situation, why not use it? To date, many RL algorithms do not use past data in a reasonable way (at-scale RL framing, part 1). 

-   Also, collecting one sample and then re-training seems like a potentially burdensome task. Can we just send out a bunch of agents with a policy and train a new version when needed (at-scale RL framing, part 2)?

-   The "best policy" framing I introduced it with, above.

Model learning with the aim of driving interaction seems very akin to batch RL. I want to recommend the best content for a user? It is taking data to build a model that either directly acts as a policy or heavily impacts the resulting policy (depends on your RL framing). 

<div>

------------------------------------------------------------------------

</div>

## Ending 

This is just a reminder of how challenging it is to frame and understand how RL systems could work in industry.

We are at the beginning of a long journey, where many applications of RL will pop up in the areas where we least expect it. Hopefully, this writing helps you and me understand how these systems will play out.

Reinforcement learning is not the darling of the technology industry like deep learning is --- well, at least not yet. Personally, I think that industry is much less risk-tolerant, and until better methods for verifying and interpreting RL are developed, it\'ll be more on the sidelines. There are some examples of applied RL at Facebook and Google, though!

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/45e965b9-df15-4400-9613-b1fe251ff802_800x534.png)

*Endnote: we need to consider the broader effects of these systems, and there is a new venue to do so: The [Political Economy of Reinforcement Learning (PERLS) Workshop](https://perls-workshop.github.io) at NeurIPs 2021. I'm excited to share more work on this topic with some of the organizers later this summer!*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Companies like Google or Facebook buy startups to build core teams around ideas like this (included because starting an RL startup is on my radar in the next 12 months).
:::
::::
