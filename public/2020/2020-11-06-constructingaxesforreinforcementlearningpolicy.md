---
title: "Constructing Axes for Reinforcement Learning Policy"
subtitle: "A small step into the research community’s most opaque framework."
date: 2020-11-06
type: newsletter
audience: everyone
visibility: public
post_id: 18075112.rl-policy
email_sent_at: 2020-11-06T16:09:51.925Z
---
Reinforcement learning (RL) --- the framework of interacting with an environment to learn a policy to act and achieve some objective --- is on the up in many domains. Some domains make sense, some will never work, and most are bound to fall somewhere in the middle. RL is so popular because of its elegance: ***we know that most creatures learn by interacting with their environment*** (but, we should note that evolution is really a strong prior to these behaviors that we don't know how to model). The problem is RL has deleterious effects on our society at individual and group levels (see my writing on [recommender systems](https://democraticrobots.substack.com/p/recommendations-are-a-game-a-dangerous)) --- this is not a piece to describe those problems, but teasing at how we may address them in a more precise manner. 

Recommender systems are, although, a great reminder of how difficult (and sometimes backward) it is to model society as a reinforcement learning problem. From the point of view of the engineer, recommender systems are an RL loop where the consumer (us) is the environment, the application is the agent, and money is the reward. It is troubling that technology companies are going to explore your inner workings as the environment for their research. The engineering problem ultimately turns into a *game between the designer/user and the agent* --- RL traditionally is very sensitive to tweaks and sudden, unexpected changes in behavior. After a couple of examples of real-world RL, I propose three initial axes to start a discussion on RL policy:

1.  Ability to model targeted dynamics,

2.  Closedness of abstraction of targeted dynamics,

3.  Existing regulation on targeted dynamics.

I've been in a reading group with Berkeley's Graduates for Engaged and Extended Scholarship in Computing and Engineering ([GEESE](https://geesegraduates.org/blog/)) and the Center for Long-Term Cybersecurity ([CLTC](https://cltc.berkeley.edu/)), hoping to culminate in a white paper on the topic (thanks and credit to collaborators). 

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/4e22d1e7-5561-4a4b-ba7e-fed8bfa3e4dc_5184x3456.jpeg)

<div>

------------------------------------------------------------------------

</div>

# Real-world RL: present and future

RL is being used in the real world in positive ways, and I am an optimist that it will work in more domains than initially expected. Here are a few examples to get the thoughts going:

### Example: power grid

Power systems have proven very tractable for study with reinforcement learning. It can be used to manage network load, plan production at different facilities, and more. Many of the papers leverage accurate simulation of the dynamics and fail-safes so that the learning process doesn't cause any weird behaviors. The history of studying power dynamics in electrical engineering provided clear bounds and fail-safes for the new learning-based technology. These themes behind the power grid is why some [big technology players have applied RL](https://deepmind.com/blog/article/deepmind-ai-reduces-google-data-centre-cooling-bill-40) to optimization of data-center operations. The system is closed in its abstractions, has accurate to-model dynamics, and reasonable to-model goals.

### Example: automatic trading

Automated trading may be the most logical problem space for RL --- the reward function is to make money and keep making money. The actions are to buy and sell, but how do you put a bounding box on the underlying environment --- it extends beyond just moving money to all the end-users' bank accounts. Another problem is that the action space is so diverse and hard to constrain (the constraints are set by mistakes humans have made in the past, and the [one flash crash](https://en.wikipedia.org/wiki/2010_flash_crash)), and the dynamics are very unknown. The uncertainty has not stopped people from making a ton of money in the area, but I don't think we are done with flash crashes and other periods where the stock market seems separated from reality. [Here is a good blog post in the area](https://dennybritz.com/blog/ai-trading). I think people will continue to make money in the area, we won't see much regulation unless something truly breaks, and the money-market to end-user dynamics will be impossible to capture (people don't always like to talk about where their money is).

### Example: medical treatment

RL for medical treatment could very well look like a computer figuring out how to make new drugs or administer previously unstudied combinations (sounds alright in an offline fashion), but it can also take many forms and is intentionally vague (highlights the challenge). Current medical policy could inform future data-driven medicine policy, but this may be too much optimism. Specifically, I bring up medical treatment because RL has a lot to learn from this area across applications beyond just medicine. Clinical trials in medicine compare any new method to the current standard of care. Implementing this standard in RL would be that the change from going to the current human-centric medical system (or another process) to a data-driven system would not decrease performance at an individual level (even if it's cheaper to send someone a computer). This performance comparison should be made irrespective of access (human doctors are more expensive because they are scarce) and would prevent too early adoption of computer-docs. If you're interested as to if data-medicine is ready, [this blog probed](https://www.nabla.com/blog/gpt-3/) the intuitions of the Reddit-corpus GPT3 on medical ideas, and it didn't perform great.

<div>

------------------------------------------------------------------------

</div>

# Axes for RL Policy

Here is my first pass at sketching RL policy. Such policy *should not* prohibit studying RL in systems in extreme areas of one of these axes, but it should require additional oversight or better data-practices. An exciting area for slowing the feedback loop for RL is limiting some areas of study to offline RL --- the process of distilling logged data to a policy and updating occasionally rather than consistently.

### Axis 1: Ability to model the targeted agent

Consider the difference from power systems to medical treatment: we know [Maxwell's equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations) and how they work in engineering systems, but we do not know the biology of the human body (relatively). Modeling the physics behind power systems lets the machine-learning engineer be bounded by physical realities --- we know when certain actions will turn the power off and they are removed from the action space (this does make the learning problem slightly harder, albeit). There are some constraints on biology, of course, but there are much fewer higher-order interactions in power systems.

This bound makes sure we don't cause harm at the low-level of the system we are controlling.

### Axis 2: Accuracy of abstraction at targeted endpoint

My biggest gripe for reinforcement learning in the real-world is when the targeted end-user, e.g. the news feed in a social network, clearly has ramifications beyond just the individual users. This axis seems very similar to the above, but I separate it intentionally. For example, the potential harm for a datacenter costing more to run versus the power grid is very different (we don't necessarily know how much harm Google going down, would actually cause though). This axis could be refined more, but I think some sense of scale is important. We can apply RL to our smart fridge, but maybe not to the food distribution infrastructure. 

This box lets us consider the scale for potential damage outside the bounds of the control algorithm. 

### Axis 3: Existing regulation for scaffolding

The medical example highlights the potential for existing normative behaviors and regulation helping to define a problem space. Power systems are in the middle on this: being a utility helps constrain some actions. Other examples are further off. RL policy, and other technology litigation, should lean on this existing scaffolding. Knowing that the Food and Drug Administration (FDA) and other government agencies were founded by patching over historical errors, I think this is a hard trend to be ahead on, but I am a proponent for founding a Data and Algorithms Administration.

This axis lets us remember that there is more potential harm in applying RL when the environment and agent are relatively free systems (cough, cough, social media).

### Example: transportation

Google Maps algorithms could probably be improved by RL (maybe they are? Let me know). Transportation and routing have nice abstractions, rewards, and dynamics. First, consider medicine versus transportation: medicine is a much more regulated, and more formal normative structure to be navigated. People are excited to apply RL to transportation - transportation is ripe for the extraction of reward functions and easier than things like medicine that have more normative content. Normative content is correlated with how badly people want to maintain the "humanness." Transportation is an example where at-scale RL could translate into complex multi-agent interactions and unintended problems (e.g. autonomous vehicles make normally non-traveled roads un-usable for pedestrians).

Transportation I would put safe on axis 1 (essentially traversing a graph), moderate on axis 2 (not sure how autonomous routing will go because it's such a massive system), and safe on axis 3 (we have a lot of rules for cars to follow already). 

# at-scale RL becomes multi-agent RL

Multi-agent RL (MARL) can be defined in many ways, but it is where at-scale reinforcement learning with individual fine-tuning is going. It is really relevant to discuss some documented key challenges of MARL (see [overview](https://arxiv.org/abs/1911.10635)):

1.  **Non-unique learning goals**: each agent has different goals, how do we optimize the whole picture?

2.  **Non-stationarity**: the data-distribution changes incredibly at each step because an individual agent no longer controls everything.

3.  **Scalability issues**: if agents consider the behaviors of each nearby agent the complexity scales exponentially.

4.  **Varying information structures**: agents and environmental data are heterogeneous across agents (I think this one is nearest to being solved).

I am interested in formulating my view of the social media world through the lens of cooperative vs competitive games (only some are zero-sum), sequential vs parallel MDP, centralized vs de-centralized control, and more. I have become increasingly interested in MARL from a research perspective because it is what most app-based algorithms are doing to us. The current consensus in MARL is that almost any complex reward function is intractable, so that's the experiment all the tech companies decided to run!

That last sentence was intentionally a lot, flipping the subject-object ordering for some drama. But, it seriously seems like it: tech companies determine more and more of our interactions each day, and, while they are optimizing for profits, each individual agent (us) has our reward functions. The downstream effects are playing out.

I'm sure I will touch on this more in the future, as I have in the past with the recommender systems post. This election season has more weight on my need to work in community and common-good building technology, maybe I should start with a mental-health improving and long-term oriented social network. 

My one comment for current events: we all need more positive energy and a bit more discursive engagement. Don't give up on individuals that have been unknowingly skewed by some apps on their phone.

<div>

------------------------------------------------------------------------

</div>

Hopefully, you find some of this interesting and fun. You can find more about the author [here](https://people.eecs.berkeley.edu/~nol/). Tweet at me [\@natolambert](https://twitter.com/natolambert), reply here, email me. I write to learn and converse. Forwarded this? Subscribe [here](https://democraticrobots.substack.com/).
