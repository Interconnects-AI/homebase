---
title: "The Ubiquity and Future of Model-based Reinforcement Learning"
subtitle: "Making a case for why you want to learn about models and why my research matters."
date: 2020-12-18
type: newsletter
audience: everyone
visibility: public
post_id: 25992199.mbrl
email_sent_at: 2020-12-18T12:42:47.246Z
---
This post is not talking about the technical details and recent work in model-based reinforcement learning (MBRL), but rather why I am bullish on it for the future. Beyond the prospects of how well it can perform (it's much younger than most of deep RL), having discussions with AI Safety and Ethical AI experts makes it clear that it's more structured learning-setup is pointing towards systems that humans can better understand. *Some level* of understanding how the system makes decisions is likely a prerequisite for many companies to start using it, else they cannot do real [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) and analysis.

I will start by showing you the rich set of parallels MBRL has in biological processes, and then show the features making it more suitable for safe deployment in society-facing systems ([see why this matters here](https://democraticrobots.substack.com/p/recommendations-are-a-game-a-dangerous)). After discussing its foundation in our biology, I discuss how it can lead to interpretable and generalizable systems. As many of you know, I am doing [my PhD centered around](https://natolambert.me/quals_trim.pdf) model-based reinforcement learning.

### Review of Model-based RL

Model-based reinforcement learning only differs from it's model-free counterpart in the learning of a dynamics model, but that has substantial downstream effects on how the decisions are made. Here are some *definition* statements.

#### Simple version: 

Model-based reinforcement learning (MBRL) is an iterative framework for solving tasks in a partially understood environment. There is an agent that repeatedly tries to solve a problem, accumulating state and action data. With that data, the agent creates a structured learning tool \-- a dynamics model \-- to reason about the world. With the dynamics model, the agent decides how to act by predicting into the future. With those actions, the agent collects more data, improves said model, and hopefully improves future actions.

#### Academic version: 

Model-based reinforcement learning (MBRL) follows the framework of an agent interacting in an environment, learning a model of said environment, and then leveraging the model for control. Specifically, the agent acts in a Markov Decision Process (MDP) governed by a transition function xt+1 = f (xt , ut) and returns a reward at each step r(xt, ut). With a collected dataset D :={ xi, ui, xi+1, ri}, the agent learns a model, xt+1 = fθ (xt , ut) to minimize the negative log-likelihood of the transitions. We employ sample-based model-predictive control (MPC) using the learned dynamics model, which optimizes the expected reward over a finite, recursively predicted horizon, τ, from a set of actions sampled from a uniform distribution U(a), (see [paper](https://arxiv.org/pdf/2002.04523) or [paper](https://arxiv.org/pdf/2012.09156.pdf) or [paper](https://arxiv.org/pdf/2009.01221.pdf)).

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/828e52e1-e458-4aac-918b-8e01736aff93_1047x816.png)

<div>

------------------------------------------------------------------------

</div>

### The Ubiquity of Model-based Reinforcement Learning

This section is based of the (suitably named) [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3513648/) from neuroscience making a case that model-based learning is more prevalent in biology than it's model-free counterpart. This section is also very well-placed for someone who was trained in reinforcement learning broadly from the optimal control side of things (Bellman updates) and wants to know how the neuroscience communities frames the iterative learning problems. 

Now, the paper on the origins of model-based thinking.

> This distinction is operationalized with tasks that use revaluation probes, such as training an animal to lever-press for food when hungry, then testing performance when full. Revaluation interrogates whether choice of an action (lever-pressing) is affected by consideration of its outcome (the food, now worthless) or merely determined by previous reinforcement (which occurred when hungry). If behavior instantly adjusts to reflect the new value of the outcome that the action would obtain, this demonstrates that the choice is 'goal-directed', that is, derived from a representation of the action's specific consequences, or in RL terms, model-based. Insensitivity to revaluation instead indicates 'habits', choices made without regard for any representation of outcome identity but instead selected based on previously realized value, as with model-free RL.

The reward prediction error (RPE) hypothesis of dopamine suggests that rewards are received **when they are predicted** ([paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4826767/#:~:text=Reward%20prediction%20errors%20in%20dopamine%20neurons&text=The%20response%20to%20the%20reward,less%20than%20predicted%2C%20reward%20occurs.)). This seems a little backwards, but it means biologically reward hormones are released when a brain predicts, with high certainty, an valued outcome. The RPE gets its name by the update function --- the brain's circuits rewire themselves based on the difference between the perceived and the experienced reward.

Some works hint that this formulates the **model-free** version of reinforcement learning, derived from understanding that the learner doesn\'t need to model the reward, just to predict it. There has been some pushback to this theory, summarized snarkily in the paper:

> However, it is easier to demonstrate that the brain is smart than it is to understand how it manages this sophistication.

Coming from engineering disciplines (likely optimal control), recent theories suggest control, planning, virtual rollouts, etc can better match biological processes. The paper discusses in a few examples how a brain can run through multiple "sequential contingencies of events and actions.\" I love the totally fresh phrasing on something that I regularly deploy in my research --- computational planning. From the computer science side of things, such a planning technique would be something like [Model Predictive Control](https://en.wikipedia.org/wiki/Model_predictive_control) --- the idea of, either via samples or convex optimization, to iteratively optimize an action sequence to achieve a desired trajectory through a state space.

Specifically, the paper highlights a series of experiments in the ventromedial prefrontal cortex and orbitofrontal cortex (or the rat prelimbic cortex) for goal-direct behavior (planning in values). Additional experiments have been teasing at **where the modeling occurs** (fMRI is a magical tool) and are finding recordings in hoppocampal regions (which has spacial mapping capabilities). The gist I got was that these regions of the brain are often associated with different types of planning --- we have a vision for our day versus we subconsciously plan how to pick up a mug. This ***hierarchy***also being present in the brain is very compelling from a control design perspective --- having one controller fine tune all the problems on your robot is unlikely. This sort of hierarchical control also lends itself to an elegant version of model-based and model-free learning coming together. Consider the described difference in the paper:

> The model-based versus model-free dichotomy was proposed to capture a longstanding distinction in psychology between two classes of instrumental behavior known as goal-directed and habitual.

In the hierarchical systems I have discussed with colleagues, the model-free control would be used for quick-thinking and simple tasks like getting the mug, but we want our agents to be able to reason into the future in structured ways, so we give them a model.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/18e6cdfa-9d88-44ed-84ee-cd2afacd07b8_2482x1596.png)

<div>

------------------------------------------------------------------------

</div>

### Interpretability and RL

One of my favorite ideas from NeurIPs this year is a set of experiments to try and make the RL systems I work with interpretable. What does interpretability mean in machine learning? The ability for a user to understand how a model came to a decision (I intentionally say user here because in some cases the company responsible may be able to understand the decisions sooner, but I like to look forward to a world when these insights are required to be passed onto the user \-- without disclosing the secret algorithm sauce, of course because capitalism). 

Why is the vanilla model-free RL loop not interpretable? The current favorite function approximator of the machine learning community, *neural networks, gives no insight into how a computation is made* (for example, compare to a random forest of decision trees where the decision features are recorded). This computational black-box is very limiting from a debugging perspective. It can make for fun research as it frequently either works or it doesn't, but that doesn't scale well when there are more real contingencies involved.

Model-based RL can gain some level of interpretability through the planning with **reward ensembles**. Normally in RL, we are only trying to optimize one reward function. If through careful design or inverse-RL (or by having multiple objectives), we can consider our plans in the presence of a reward ensemble. A general failure more of model-based learning is that actions exploit inaccuracies in the model. The goal is that by using multiple reward functions we can optimize the worst case (which reward function looks the worst). Instead of taking the maximum of one reward, we hope that this will also give more stable performance. The best way to convince people to use ML systems that are more open and comprehensible is to make them work better, right?

For those who want more on interpretability, I have heard a lot about [this report from Microsoft Research](https://arxiv.org/abs/1802.07810) discussing interpretable models. I look forward to learning more from it.

### Generalization with Models

We want our learning systems to be able to solve multiple related tasks (or at least improve at them) as we accumulate more data from the environment of those tasks. Better yet, we want our robots to be able to solve **totally new tasks** in the same environment from past data. This is the goal of generalization. The crux of this argument comes down to the potential benefit of learning in a structured way \-- through the dynamics model \-- to allow our agents to reason about different scenarios.

Why is the vanilla model-free RL loop not generalizable? The optimization that tunes the neural network policy is heavily conditioned on the reward function / task being optimized. This fine tuning, and again the lack of an ability for humans to manipulate these networks by hand and understand it, leaves the *policy useful for literally only that task*.

Model-based RL hopes to alleviate that by leveraging the dynamics model repeatedly. This is strong assumption because the model still suffers from distribution shift and other problems. For example, an accurate model is not a guarantee to get strong performance (a problem we coined [Objective Mismatch](https://arxiv.org/abs/2002.04523)). But given what we have learned about how biology works and the increasing availability of compute, it is logical to use the big computers we have to reason about a model we collected from data. For a good talk on how generalization could work with models, see [this talk from Anusha Nagabandi at the NeurIPs Deep RL Workshop](https://slideslive.com/38938089/modelbased-deep-reinforcement-learning-for-robotic-systems?ref=account-folder-62083-folders) this year.

<div>

------------------------------------------------------------------------

</div>

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/66321089-a6f5-423b-ae2b-723ec1f13acf_4032x2276.jpeg)

In conclusion, I also think model-based learning lends itself to a bright young area of reinforcement learning, offline RL. Offline RL is the idea of taking previously logged data and creating a policy with it, which could dramatically increase the scope of problems that RL can address. If this is interesting to you, [check out this workshop on offline RL](https://offline-rl-neurips.github.io/).

What a wild world we live in. This is likely the last issue of the year! Talk soon.

Hopefully, you find some of this interesting and fun. You can find more about the author [here](https://people.eecs.berkeley.edu/~nol/). Tweet at me [\@natolambert](https://twitter.com/natolambert) or follow the blog [\@demrobots](https://twitter.com/demrobots), reply here. I write to learn and converse. Forwarded this? Subscribe [here](https://democraticrobots.substack.com/).
