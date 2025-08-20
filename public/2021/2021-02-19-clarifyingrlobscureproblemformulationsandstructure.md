---
title: "Clarifying RL: Obscure problem formulations and structure tradeoffs"
subtitle: "Some debates that will be settled en route to RL being used in all corners of the modern world."
date: 2021-02-19
type: newsletter
audience: everyone
visibility: public
post_id: 32649615.clarifying-rl
email_sent_at: 2021-02-19T13:07:20.677Z
---
Reinforcement Learning (RL) is really popular. It's intriguing to see a **framework** be the attention of so many blogs, undergrads, conference talks, and seemingly everything the internet algorithms feed me. The prevalence is due to the many directions to get hooked into RL: optimal control, search, neuroscience, robotics, and likely more I haven't heard of.

RL is a framework for trying to solve problems where the engineer **does not have direct access to the environment**. Most learning systems, have the loss directly as a metric in training (like accuracy) and are studying a closed system (like input-output pairs). RL is observation based.

**Why does it need clarifying?** Mechanisms and phenomena that are part of RL by design are going to emerge in many of the learning-based systems growing to dominate our economy.

RL needs clarifying because it is a broad framework being used in a ton of different ways. The framework of act, learn, repeat is actually a reduction of any iterated machine learning solution (like companies that update their models for language processing, news feeds, or anything). We seen how connecting everyone to the internet can cause problems, but **the internet manipulating those users concurrently is a bigger realm of risk**.

*In this post, I go deeper into RL to show you what is missing from deploying RL in the real world and what there is a lot of debate on among researchers:*

1.  *reminder why RL is so obscure and hard to define,*

2.  *discuss tradeoffs between end-to-end learning, modularity, and exploration,*

3.  *some of my thoughts on the direction of RL.*

## Obscurity of RL...

Defining the reward function for an experiment is the clearest source of uncertainty in RL. A popular theory underpinning rewards and RL is the [reward hypothesis](http://incompleteideas.net/rlai.cs.ualberta.ca/RLAI/rewardhypothesis.html):

> That all of what we mean by goals and purposes can be well thought of as maximization of the expected value of the cumulative sum of a received scalar signal (reward).

I find this to be very innately wrong, but impractical is likely a better way of thinking about it. In concept, every human could have different weights that encompass their peers' rewards, but it is not practical. Traditionally, RL often hinges on the **designer translating from an imagined reward behavior** (latent space of planning) to a **scalar reward signal** (latent space of observations, which may not encompass a behavior).

This translation is especially burdensome with multi-objective optimization. RL agents generally assume the reward function as a ground truth, but I am becoming aligned with the AI Safety partitioners here: all **reward functions should be assumed to be slightly incorrect interpretations of the desired behavior**, with infinite ability for fine-tuning of reward signals (here is [a paper](https://arxiv.org/pdf/2006.13900.pdf) from a Berkeley colleague Michael Dennis, who speaks very eloquently about re-designing how RL thinks about reward functions).

Defining the agent and the environment can seem more straightforward, but the ease falls out when moving from robotics and games to broad interpretation of iterative tasks (newsfeeds, health optimization, routing, etc.). My favorite example is to consider deploying RL on social media curation algorithms --- at first glance, the agent is the algorithm (what is shown to a user), but that makes the environment the human and the humans in a network, which will always be changing (RL is assumed to operate in *stationary distributions* normally). Alternatively, the application can be viewed as an environment where the user interacts with it and achieves some reward. This turns into an agent/environment [duality](https://en.wikipedia.org/wiki/Duality_(optimization)) in optimization, which could likely help stabilize performance, but is deeply weird. 

This quickly turns RL into a framework where every instantiation of a problem is inherently a slightly incorrect model of reality. It's not to say it cannot still solve tasks (some models are still useful), but it is much harder to have strict bounds on performance (crucial for safety-oriented systems).

![From a Talk from A.G. Barto on the History of RL.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/fddc9322-eaa7-46e2-9ea2-1deb70631dcb_1842x1262.jpeg)

*(A good place to start learning reinforcement learning is [The RL book](http://incompleteideas.net/book/the-book.html).)*

## ... and where we shouldn't try RL

RL is uncertain in ways that make it very scary to real-world applications. This section follows very closely onto the article [I wrote on RL (legal) policy](https://robotic.substack.com/p/rl-policy) that covered three main axes of consideration. We should likely ban using RL in an online setting if one of the following axes tends too extreme:

> 1.  Ability to model targeted dynamics,
>
> 2.  Closed/openness of abstraction of targeted dynamics,
>
> 3.  Existing regulation on targeted dynamics.

That is to say, "how much do we know?" and "is not knowing risky?". Drawing red lines around applications that are not worth the risk of trying to deploy a new technology is crucial to the beneficial deployment of the next generations of AI.

In academia, I think the incentives are really weird around ethical risk. It is much harder to publish a paper saying "we should not do this research because it may cause harm," than it is to say "whoops, we did it again."

*As a point of self-reflection, I am proud of myself and my readers for making time to consider where technology can cause harm regularly. This blog is trying to tread the line between "shiny new robot" and "impactful discourse." I appreciate the support and am open to suggestions to improve the model.*

![Autonomous vehicle routing is one of the most championed testbeds for practical RL: a problem at scale with well-defined constraints.](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/6499bde0-1994-49fc-89bc-f3942302aedb_3992x2000.jpeg)

<div>

------------------------------------------------------------------------

</div>

## Some structural tradeoffs

When discussing the future of my work in model-based RL and the future of RL as a tool, many tradeoffs come up repeatedly. They tend to trade between interpretability (and therefore some safety) and ease of use or theoretical functionality. 

### Model-based vs. end-to-end

For self-driving, model-based approaches are characterized by the Waymo approach, *optimize each module of autonomy*, and end-to-end learning by the Tesla approach, *one model to rule them all*. 

End-to-end learning is how our brain works for vision (high level): go from input observations directly to actions with one learned model. End-to-end learning is proven to be able to work and quickly solve many tasks. End-to-end learning is very theoretically elegant and conceptually able to use less data by solving for the **minimum latent representations of the model**. 

Model-based learning is centered around the idea that we can learn a function to approximate some domain dynamics, and then use that for control. We can learn functions at multiple levels of the stack, such as perception and dynamics separately. The main benefit of model-based approaches is the ability to **run diagnostics on the system outside of online experimentation**.

Model-based approaches currently are more data-efficient (likely because the structure is closer to the ideal arrangement than current large end-to-end models), but end-to-end approaches conceptually can be more data-efficient because they can reduce learning to the minimum number of intermediate representations. Model-based RL, though, is also characterized by weaker peak performance. These two trends will converge in interesting ways: model-based methods likely cannot get much more sample efficient, but they can perform much better. End-to-end approaches will get more sample efficient *and more effective* over time. The intersection of the [Pareto fronts](https://en.wikipedia.org/wiki/Pareto_efficiency#Pareto_frontier) will likely show which one wins because most companies will only use the interpretability of models as a tiebreak.

*For more on model-based RL, see [my article](https://robotic.substack.com/p/mbrl) or [my research page](https://www.natolambert.com/research/model-learning). Here is a cool review on the [Limits of End-to-end Learning](http://proceedings.mlr.press/v77/glasmachers17a/glasmachers17a.pdf), which I have much more to learn about.*

### Explorative vs. offline

Online learning systems are characterized by a fundamental tradeoff (can also be viewed as a chicken-egg problem): **You need data to be able to solve a task, but the data is risky / expensive / impossible to get**. I first came to this as a hypothesis for why more robots are not in homes: *no one wants shitty at-home robots, but until they are in homes regularly they will likely be shitty*.

A new subfield of RL is **Offline RL**, quoting from [a past post](https://robotic.substack.com/p/mbrl):

> Offline RL is the idea of taking previously logged data and creating a policy with it, which could dramatically increase the scope of problems that RL can address

Offline RL makes a lot of sense in terms of **what can we do with xyz data**, but it does not answer the question of how do we get the best data for our solution. The last breakthrough algorithm in model-free RL, [Soft Actor-Critic](http://proceedings.mlr.press/v80/haarnoja18b/haarnoja18b.pdf), came by adding an entropy-based exploration mechanism to the learning process. Model-based RL has few analogous mechanisms for exploration and actually explores by leveraging model uncertainty in a very [exploitative manner](https://www.natolambert.com/writing/exploitation-exploration).

The question in my mind is: how does the offline learning process change when shifting the data distribution it is trained on. Is the shift in performance smooth regarding changes in the data distribution? Or, is the performance very noisy with respect to changing the data distribution for offline RL (not an expert here, please chime in if you know more!). 

Ultimately, offline RL is a very young field. I think it will progress very rapidly until it maxes out the current benchmark datasets we have, and then it will become closely tied to exploration: **how can we rapidly collect the minimum data to solve this problem**? Then, in the real world, it progresses to *how can we **safely** collect the minimum data to solve this problem*?

### Things that don't work

These are not tradeoffs but rather debates on things that simply need to be fixed.

1.  **High computation burden**: running some simulated results (famously half cheetah) in RL can take up to 3 days to learn in wall time with a GPU. This benchmark is not useful for translating to reality because most tasks happen well under this timescale, and devices cannot run for 3 days autonomously. Wall time cannot be avoided and needs to be reduced.

2.  **Walled gardens**: the state-of-the-art in RL algorithms are now evaluated on simulation environments that are both buggy and cost thousands of dollars are a year to license. A second generation of benchmarks will come out and reinvigorate research and progress.\
    *Edit 19 Feb. 2022* --- *Note: at the time of writing, Mujoco was a very challenging simulator to work with. Since, [DeepMind has acquired it](https://venturebeat.com/2021/10/18/deepmind-acquires-and-open-sources-robotics-simulator-mujoco/amp/), hopefully leveling access for researchers. I am also excited by recent moves by companies like [HuggingFace](https://huggingface.co/spaces/ThomasSimonini/SnowballFight) and [Unity](https://github.com/Unity-Technologies/ml-agents).*

3.  **Irregularity of implementations**: most results are hard to reproduce. The field knows this, but little work is done. If RL wants to be adopted by the industry, more rigorous standards are needed. Or, it is more likely that the industry adopts some RL and trickles down some better practices to use fickle researchers. 

<div>

------------------------------------------------------------------------

</div>

RL is very elegant, and I am still bullish on its future. I am just pretty sure it won't be used in the application spaces it is being developed. Embodied intelligence is such a fruitful place for the study of AI because of how close to reality it is: we know solutions exist because we are the existence proof for rapid skill acquisition. **What do you think will be the next breakthrough in RL?**

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/74664676-e448-492d-9c69-0ae1523f7130_4288x2094.jpeg)

<div>

------------------------------------------------------------------------

</div>

## Snacks

### Thoughts

-   I have been reading, watching, and thinking about the neuroscience between RL a lot recently. Writing on this topic is likely coming soon, but I wanted to share this [history of RL video](https://www.youtube.com/watch?v=ul6B2oFPNDM) I found from AG Barto (about 20 minutes).

### Reads

-   The New Yorker released [a great piece](https://www.newyorker.com/tech/annals-of-technology/who-should-stop-unethical-ai) covering the conversation I and many people in the AI field are having around ethics, and what we can and cannot prevent in the future of malignant technology.

-   I am reading [Artemis](https://en.wikipedia.org/wiki/Artemis_(novel)) (the same author as the Martian), and it seems quite fun. A good escape book for engineers.

I made a [new website](https://www.natolambert.com) --- learn about machine learning, robotics, and me.

If you want to support this: like, comment, or [reach out](https://twitter.com/natolambert)!
