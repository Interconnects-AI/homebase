---
title: "Reward is not enough"
subtitle: "Multi-agent scenarios make reward maximization a risk. Discussing when, rather than if, we should believe in the Reward Hypothesis."
date: 2021-06-21
type: newsletter
audience: everyone
visibility: public
post_id: 37004859.reward-is-not-enough
email_sent_at: 2021-06-21T15:08:24.597Z
---
**[Dopamine](https://en.wikipedia.org/wiki/Dopamine)** (below) is central to human experience. It is known to be involved in feeling a current pleasure --- that is something you are experiencing and enjoying. Dopamine also plays a crucial role in predicting a future please --- that is done in planning by releasing the same feeling of enjoyment when you are planning to do something that you will like. The human body has a super complex infrastructure around enjoyment, pleasure, goal-setting, reproduction, and more that all involve this molecule. 

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/92604532-4ead-4b74-a4da-812ba994c136_2828x2000.png)

Trying to model dopamine's effects could be a path toward understanding how humans learn. This one signal is the center of my personal review of how reinforcement learning ties to neuroscience and biochemical systems (blog TBD). The goal of claiming we can understand human intent by "solving" dopamine is much akin to if we can optimize any complex system from one measured signal (and [Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law) results from human nature). 

The idea that we can encapsulate all the metrics we need in a single reward function is endemic to the current technology applications of deep learning. Particularly in reinforcement learning, there is a theory that any agent can learn to solve any task in its reachable space with a suitable scalar reward function. This ***reward hypothesis*** ([link](http://incompleteideas.net/rlai.cs.ualberta.ca/RLAI/rewardhypothesis.html)) is saying that we can reduce multi-objective optimization to that of scalar optimization for any reinforcement learning agent (often viewed as an individual). The reward hypothesis, or The Hypothesis in this article, is put forth by some of the "founders" or RL, so it carries weight.

It is stated originally on [Rich Sutton's blog](http://incompleteideas.net/rlai.cs.ualberta.ca/RLAI/rewardhypothesis.html):

> That all of what we mean by goals and purposes can be well thought of as maximization of the expected value of the cumulative sum of a received scalar signal (reward).

In applying this methodology to more complex internet systems, all the actions that can be taken (across many users) are included under the same agent, which is extending the scope of the original idea, and causing its validity to be up for debate. This post is designed to go through some key ideas behind the [reward hypothesis](http://incompleteideas.net/rlai.cs.ualberta.ca/RLAI/rewardhypothesis.html) and figure out where we should draw the line at the applicability of this hypothesis.

What are the limits in understanding behavior that can be reasonably defined by a scalar reward function? There likely is an exact function that describes human intent at any scale, but it is likely too sensitive to perturbations that trying to find it will cause more harm than good.

## The Hypothesis

The reward hypothesis is on a decent footing because of the infinity of real numbers and expressions. Proponents of the theory say that for one agent there is necessarily one highly precise function that fits its needs. I do not refute the existence of such functions, but rather if we should bother looking for them.

Two critiques at the low level of the hypothesis (i.e. if it is a reasonable claim in any setting) follow. First, we should consider if these scalar reward functions may **never be static**, so, if they exist, the one that we find will always be wrong after the fact. Additionally, as there are infinite possible reward functions, it may also be **infinitely hard to find an agent's reward specification**. *What is the point of being able to encapsulate every possible reward in a scalar function if we know we are unlikely to ever find the correct representation? *

For scenarios like games where a score and leaderboard are provided, the reward function is intuitive: maximize score. For agents with multiple priorities, e.g. being healthy and having a career, finding a reward function becomes more challenging via **relational** optimization. I posit that for individuals it is still more reasonable to do, but not worth it, as we can expand the state-action space to easily account for multi-modal behavior. This is to say that humans could be taking very different actions when reading or working out, and they could contribute to a reward function in relatable ways (the reward function is generally defined as a function of the current state and action).

The true challenges of the reward hypothesis fall around much more existential questions:

1.  **Does this work for relational reward**: Can scalar functions represent how different people may value different things, especially when these people interact or systems must decide that one person wants it more?

2.  **Control and political economy**: Is having a company or some machine understand, dictate, and act on specifically-tuned rewards, worth it? With all of the above considered, it is a strong statement to say things like for-profit corporations are benefiting you by trying to learn and act on both your reward preferences and the preferences of your closest friends.

Learning someone else's values is not necessarily an impingement of some form of our societal goals. *Knowing that such an approximation is by setup going to have errors, and acting as if the learned rewards are true anyways likely is*. When companies move past click-based metrics, understanding user goals is a logical next step for engagement and value maximization. 

A recent [paper](https://www.sciencedirect.com/science/article/pii/S0004370221000862), *Reward is Enough*, by David Silver, Satinder Singh, Doina Precup, and Richard S.Sutton carries substantial weight in the field via the positions of David Silver (led many of DeepMind's RL for games efforts; some of the highest-profile successes of ML to date) and Richard Sutton (an originator of the field of RL in the 80s). In my opinion, people working on these systems need to have a more diverse discourse on what it means for **RL to be used at scale**. Yes, reward maximization is likely useful in all of these applications, but people need to be thinking about boundaries, redlines, final goals, worthiness, etc. 

Many of the claims in the paper are reasonable, but the claims that reward-maximization is the only lens needed to model and understand "social intelligence, language, generalisation" are harder to support. Following through on these claims of reward maximization and optimization frameworks being useful for designing such relational systems is a strong statement of what structures should be in control of our lives. 

## (bio)logical agents and scalar maximization

The hypothesis that dopamine played a central role in the subjective experience of humans was coined the [Anhedonia Hypothesis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3155128/) (1982):

> The anhedonia hypothesis -- that brain dopamine plays a critical role in the subjective pleasure associated with positive rewards -- was intended to draw the attention of psychiatrists to the growing evidence that dopamine plays a critical role in the objective reinforcement and incentive motivation associated with food and water, brain stimulation reward, and psychomotor stimulant and opiate reward. 

Dopamine is a bit better known now:

> Brain dopamine plays a very important role in reinforcement of response habits, conditioned preferences, and synaptic plasticity in cellular models of learning and memory. The notion that dopamine plays a dominant role in reinforcement is fundamental to the psychomotor stimulant theory of addiction, to most neuroadaptation theories of addiction, and to current theories of conditioned reinforcement and reward prediction. Properly understood, it is also fundamental to recent theories of *incentive motivation*.

Such **incentive motivation** is imbued in many learning agents as a distillation of expected reward into parameters that govern action:

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/d35a2437-1967-44eb-bf5e-f4b8ddee26a5_1218x342.png)

A strong argument can be made that individuals do act as if life is a finely tuned reward system prioritizing reproduction. One's genetics and environment determine a certain condition that re-weights different priorities in their dopamine circuit. 

Our brains would likely adapt to the changes it is facing in social media pretty rapidly where possible within its known behavior and unimaginably slowly through evolution. If social media was in a bubble, and our interactions with it did not affect each other, that may be okay. The principles of dopamine prediction and scalar optimization of an agent break down when we are studying it at the scale of society and trying to compare motivation across groups. 

## Applying optimization to real-world decisions

Where this post really started was thinking about, more realistically hoping for, the end of the era of attention-based metric maximization. Attention-based metric optimization is: how technology companies use a handful of simple metrics to drive engagement up (in the short term, and consistently) on their platforms. **The goal is in considering how the systems could better balance and jointly optimize the long-term interests of their users.**

Through meetings at Berkeley around the future implications of AI, I have heard multiple first-hand accounts on how it is unlikely that a massive overhaul of the user-metric tracking occurs anytime soon.

What is highly profitable for these companies will still work for the time being, at least until any regulation is passed. Eventually, I suspect the large social media companies will want to transition to a model that matches their platform's behavior with the goals of the users.

Most people who are cognizant of the fact that they, or those they are close to, are addicted to their phones dislike it, therefore a change in optimization is due. No more clickthrough, hesitation time, like counting, etc.! Though, the likely outcome is companies transitioning the current approach to a different reward function optimizing a long-term plan, but the optimization may be ill-posed if the reward function for social media apps is designed to incentivize certain types of lifestyle.

Looking past short-term metrics makes these algorithms a balance between on-screen behavior (counting seconds, minutes, hours) and lifestyle structure (days, weeks, years). The field of [multi-objective optimization](https://en.wikipedia.org/wiki/Multi-objective_optimization) says so clearly why this is hard to do:

> For a [nontrivial](https://en.wikipedia.org/wiki/Nontrivial) multi-objective optimization problem, no single solution exists that simultaneously optimizes each objective. In that case, the objective functions are said to be conflicting, and there exists a (possibly infinite) number of Pareto optimal solutions. A solution is called [nondominated](https://en.wikipedia.org/wiki/Maxima_of_a_point_set), Pareto optimal, [Pareto efficient](https://en.wikipedia.org/wiki/Pareto_efficient) or noninferior, if none of the objective functions can be improved in value without degrading some of the other objective values. Without additional [subjective](https://en.wikipedia.org/wiki/Subjectivity) preference information, all Pareto optimal solutions are considered equally good\... The goal may be to find a representative set of Pareto optimal solutions, and/or quantify the trade-offs in satisfying the different objectives, and/or finding a single solution that satisfies the subjective preferences of a human decision maker (DM).

There is an infinite number of solutions. Pareto optimality does not seem like something humans can actually pursue. ***Choosing between the Pareto solutions is not something I want my apps to be doing. ***

Any user should have the ability to state what their goals are and have the algorithms tune their behavior to match this. With any amount of reflection, the fact that companies regularly change the optimization problem behind the scenes of our lives without telling us is paternalistic and undesirable.

With profitability in question, the user's choices will likely be constrained. At the scale of these systems, anyone user may look more akin to noise than the true signal the companies are optimizing for. It is the interaction between users plural, and the enumerated applications that they frequent that will heavily determine the trajectory of these systems.

## Societies and systems as a multi-objective optimization

Any attempt to define a reward function in society will impinge on what we view as unalienable rights. Human societies as a new emergent behavior of evolution are not well-studied in their stability. Soon, will be applying more test-cases to our most important evolved skill.

Comparing motivation, as discussed above, will translate into prioritizing certain users based on the weights at hand. Consider a foreboding scenario where certain applications can accurately predict our dopamine levels and use that to tailor the actions of the individual and their closest friends. **Will the person that has higher peak dopamine levels be prioritized over one with a lower baseline?** Refuting this argument can open up many more shortcomings, like social media never knowing your past and not knowing someone's peak happiness that is blocked by some form of trauma.

It may make sense for a reward-hypothesis-like system to run large systems if all of the individual agents were in agreement on the goal, but this is not the case. In the case of at-scale recommendation (e.g. YouTube, Facebook, \...) there are so many ways to view the problem from an engineering point of view. Each of these system designs is reasonable at the high-level, but will have substantially different downstream effects: 

-   Deploy one global policy (cumulative recommender is the agent with a huge action space that grows with the number of users), human is the environment.

-   Change the reward mechanism such that humans acting on the environment that includes recommendations (maybe a sort of inverse RL).

-   Stick with one-to-one optimization where a user queries a set of weights and has their experience closed off to other user's digital choices (interactions still exist in the real world, outside of the intended abstraction of this approach).

The many views and few compelling answers that center on human alignment, especially from the individual perspective, worry me. More integrated and advanced data-driven systems are moving us in that direction, it is not clear when we will reach a **breaking point** for some important societal structure by **re-wiring our preferences and goals**.

These situations where *reward is not enough* may not have a tool that can solve them optimally. There are some problems that may be better left un-optimized.

*Acknowledgements: thank you to Thomas Gilbert for helping me add more useful content and fix some typos.*
