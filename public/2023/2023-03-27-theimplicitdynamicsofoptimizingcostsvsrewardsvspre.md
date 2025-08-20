---
title: "The implicit dynamics of optimizing costs vs. rewards vs. preferences"
subtitle: "With the emergence of reinforcement learning from human feedback, we've been applying old techniques with a new guiding function (🤫 RLHF)."
date: 2023-03-27
type: newsletter
audience: everyone
visibility: public
post_id: 110914092.costs-v-rewards-v-preferences
email_sent_at: 2023-03-27T14:45:00.239Z
---
We don't have any guarantees that preference models even remotely match our actual preferences.

If you follow the scientific history of reinforcement learning (RL) back to [Bellman updates](https://en.wikipedia.org/wiki/Bellman_equation) and optimal control, the progression has been from costs to rewards to preferences. Cost functions have their origins as closed-form expressions selected by engineers to elicit behaviors in control systems, reward functions are more loosely defined as signals from an environment or game directly (not that that is always the case), and preferences are represented in functions to approximate previously measured data. This trilogy of topics gives an important baseline in understanding where reinforcement learning agents, and most other automated systems, originated and where they are going today.

The last time I talked about something related to this was in the context of DeepMind\'s *[Reward is Enough](https://www.deepmind.com/publications/reward-is-enough)* proclamation \-- where [I reminded everyone that that is abundantly not true](https://robotic.substack.com/p/reward-is-not-enough). Now, the lifelong-only-use-RL folks are feeling the pressure from language models, accepting that there may be other pieces to the puzzle. The need for preference models showcases why the reward wasn\'t going to work on its own and the challenges in preference modeling showcase why it was so hilarious that *Reward is Enough* came about.

The goal of grappling with these topics is to understand the added levels of uncertainty that we have added to the system at each step, and the underlying techniques that are intended to help solve the new problem specifications. In reality, as the problem specifications have become looser, the final agents we have are less of solutions and more of best-attempts. Compared to the behaviors generated in optimal control coursework, the modern ML-first world has drifted a long way. In some ways, it\'s remarkable that machine-learning-driven decisions ever work.

Back to cost functions. Cost functions seem like they are normally closely tied to a value function (at least an easy cost to optimize). There\'s more nuance in this, where you can start talking about terminal costs, running costs, LQR solutions, etc., but that\'s not the goal of this article (please bear with me if you are a roboticist, and leave a comment!). The quintessential examples are things like distance functions or energy functions --- quadratic bowls. When you take one of these cost functions, RL algorithms work really well. Consider Q-learning, the original algorithm is designed to recursively pass information about costs \-- this works really well if you have smooth information about your world. If you\'ve never seen any reward, these algorithms are useless.

With a simple trick (actually used by many grad. students), we can switch a cost to a reward simply by multiplying by a negative one. Take a cost function like distance of time alive, and RL algorithms will do really well at it. This is a reason why cartpole-balance is so easy for RL agents (the task is to stay alive) and cartpole-swing-up is not (the task is to get within a certain region, sparse reward). There are plenty of tasks that simply will not work if you transition from a continuous to a discrete version of the reward; a central challenge behind modern RL methods.

Modern RL methods are designed to optimize discrete rewards returned from the environment. The agent and designer a priori are expected to have no intuition about the reward function, which means an agent must explore and find a signal. This dynamic, conceptually, lends itself nicely to a sparse notion (while all the functions I mentioned as costs are generally continuous signals). Rewards are how the goals of modern exploration algorithms came about.

Importantly, rewards and costs are both expected to be deterministic functions. If the agent is in a specific state-action pair, it will see a certain value. As we move into preferences, this is no longer the case. Preference models are attempting to map from the text on the screen to a scalar signal, but in reality, dynamics not captured in the problem specification influence the true decision. The human user who labeled or generated the text has dynamic preferences, so every preference measurement has an error to it. The error can be present immediately or emerge downstream. There are some really simple and well-documented ways this can happen.

Quoting from [a paper on preference models in recommendation systems](https://arxiv.org/abs/2208.01534), here are some ways preferences can be challenging to accurately measure and model:

> Mere-Exposure or the familiarity effect says that humans tend to like more what they are exposed to more often;
>
> Operant Conditioning is the effect that beings tend to engage more in activities that are associated with positive stimuli (positive reinforcement) and avoid activities associated with negative stimuli (negative reinforcement); 
>
> Hedonic Adaptation is the effect that after some time, any change in happiness fades, and humans return to a baseline level.

In short, capturing preferences can be greatly affected by all of these. They are simple ways that even a well-instructed crowd worker will shift over time. When modeling preferences, the system is always behind. Reckoning with these errors is something more people should be doing.

Reward models themselves have been used in RL for a long time. For example, model-based RL algorithms that use planning often cheated at evaluation (by evaluating the reward in the environment corresponding to a calculated state), so reward models were used that mapped from a state-action pair to a predicted reward. They worked acceptably, but preferences have a lot more structural challenges to model correctly (as rewards are usually at least comparable!).

Modeling preferences as a scalar is like training a function from a state-action pair to a scalar for a multi-reward environment with no labels on which reward function is active.

![DALL·E 2023-03-26 21.23.53 - The dynamics of human preferences and how they change through a digital life, art.png](images/110914092.costs-v-rewards-v-preferences_3b1ebf48-4652-4a2c-95e8-9ca288110f49.png)

## Preference modeling: the great unknown

One of my biggest takeaways in working in RLHF is the lack of literature on what these relative preference models will capture and cause. As a quick primer, the preference models are trained on pairs of text (by comparing scalar values from two elements in a batch in a single loss function) in order to consistently assign a scalar \"reward\" to each entry. Therefore the models are entirely relative, with the only grounding being the generative pretraining used across all large language models (LLMs) today. I don\'t think this is a grounding a lot of societally-conscious engineers will be happy with (glances at my Reddit tab). Language is definitely flexible, but training on pairwise combinations leaves a lot unaddressed (and potentially impossible to fix).

Many different areas of cognitive science, psychology, and human-computer interaction have studied techniques related to human preferences. For example, there\'s substantial literature on learning preferences in the context of recommendation systems ([example one](https://arxiv.org/abs/2205.13026) and [example two](https://arxiv.org/abs/2208.01534)), which are fairly interdisciplinary in nature. As a starting point, we need a review paper connecting this literature.

Modern work on RLHF coming from large industrial labs generally reports preference learning as a pipeline without commenting on the power dynamics it is manipulating for its users. At a basic level, evaluation is really limited \-- the preference model is deemed good when it is good for the downstream task, not when it is accurate at modeling the environment it is trained on (matching a classic problem from my Ph.D. area of model-based reinforcement learning: [Objective Mismatch](https://arxiv.org/abs/2002.04523)). This is in the context where the model is *[known to be exploited](https://arxiv.org/abs/2210.10760)*, so an added constraint on policy drift is added to most reinforcement learning from human feedback (RLHF) systems.

If we\'re going to rely on these models trained with RLHF for everyday tasks and widespread consumer use (especially with sensitive topics such as general mental well-being), measuring preferences is a crucial sociotechnical problem. Anthropic may not talk about it because it is not a long-term safety problem and OpenAI doesn\'t because they don\'t write technical papers anymore, so we need two things to happen: 1) a moderately sized lab releases a generally capable preference model (e.g. across many dialogue and functional tasks) so that 2) academics can evaluate and measure the system. I suspect a lot of issues are found in the current best practices.

Once we know a little more about the preference models, we can easily start researching what makes a \"good\" preference model in the sociotechnical sense: a model that has uncertainty, specific transfer properties, user-tunability, interpretability, etc. A lot of these techniques are well known as things that could be tried but have been omitted due to their lack of end-goal signal (see John Schulman\'s talk RL podcast on RLHF, he says they tried some things that didn\'t help).

Having a better preference model could lower the system\'s performance on benchmarks and simultaneously reduce harm to historically underrepresented groups. It is a common occurrence for ML systems with multiple models that are measured collectively to create sub-optimal constituent components that function well together. Manipulating the representations of our preferences with gradients and capitalism should be frowned upon.

An additional challenge to assessing and commenting on these potential harms and potential benefits for society is that once a company officially documents or acknowledges its efforts to improve them, the public can hold them accountable for reporting and improving more. Following public pressure comes regulation. In the early stage of technical progress, the *take-off phase*, there is a huge incentive to share nothing that is politically sensitive. This could be one of the reasons that OpenAI engages so heavily in technical progress and policy progress, but not sociotechnical work. Technical work is crucial and policy work lets them get ahead of future problems by cultivating soft power, but sociotechnical work can lead to short-term struggles.

Largely, I expect this conversation around engaging with the great unknown of preference models to fall on the back of academics, who can still do interesting experiments. This dynamic could well continue to unfold. Industry research is in a high flux phase. People who were hired in the 2016-2020 influx to big tech research are now being gagged when it comes to papers and forced to work on products. An initial reduction in papers will create a vacuum that hopefully the academics can fill (with increased government funding and compute credits).

As things at HuggingFace stabilize from an engineering perspective, pushing on training valuable and understood preference models is at the top of my list. All the rage is saying you built a good chatbot, but I think reward models are the thing that could be most likely to be used broadly if done right. In GPT4\'s system card, OpenAI showed the world what day0 patches you need to release a safe system, but someone else can showcase how to train a model that matches our needs on preference learning.

<div>

------------------------------------------------------------------------

</div>

*Are you a researcher on preference models?*

*Email me if you want advice or are addressing any of the issues I commented on. I would love to learn more.*

<div>

------------------------------------------------------------------------

</div>

![DALL·E 2023-03-26 21.24.00 - The dynamics of human preferences and how they change through a digital life, art.png](images/110914092.costs-v-rewards-v-preferences_8f8a39eb-7c62-4f36-b028-cd59b5d6a10a.png)

## Endnote: preferences in other modalities

The primary reason that I am extremely optimistic about RLHF on non-text systems is that preferences seem a lot more intuitive for a lot of visual concepts. It\'s much easier to look at two photos and know which feels right when compared to two paragraphs. I\'m excited for my Stable Diffusion to be tuned to what I like (images at the border of photorealism and some classical styles of painting). With that, feedback data should be more plentiful, accurate, and not restricted to English-speaking workers.

Maybe in a few years, we\'ll have a GPT4 equivalent preference model (text and image inputs), I certainly wouldn\'t be surprised.
