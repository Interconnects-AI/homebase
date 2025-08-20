---
title: "Flexible Centralization in Multi-agent Learning & Control"
subtitle: "A tour of control theory, multi-agent RL, and hierarchical learning."
date: 2022-01-21
type: newsletter
audience: everyone
visibility: public
post_id: 47493885.multi-agent
email_sent_at: 2022-01-21T16:21:47.091Z
---
Multi-agent control is naturally one of the most promising areas of study for learning about how ecologies, societies, and intelligence emerge from basic principles. Multiple bodies come together to make compounded effects that way surpass their mere sum. Substantial progress is being made computationally to push the limits of *understanding* these systems, which is wildly exciting to follow. Though, as is the case with many computing technologies that we hope to embody in the real world, the hardware interface is becoming the bottleneck. Translating this understanding into *behavior* and *application* is a point of major friction. The sources of resistance are major engineering problems.

This emerges as a challenge of having each agent communicate with each other or a tough scaling factor when one central governor plans all agents' actions.

Multi-agent control as a problem setting fits well as one of the final challenges for intelligent systems --- it's a high-dimensional, non-stationary optimization. Intuitively, including more than one agent increases the complexity of the underlying dynamics along with the dimensionality of the resulting representation. Machine learning seems like an obvious tool to mitigate these problems, so [success is guaranteed](https://www.cs.toronto.edu/~guerzhoy/411/lec/W12/success.pdf) once the systems hit a sufficiently complex dimension and tall data log? Not quite - *scaling over action dimension is much harder than scaling over features* (e.g. giving automated systems agency versus compressing pixels, words, etc.)

This article is a foray into multi-agency for me, highlighting challenges posed by current ideologies (centralized vs. decentralized), current solutions (control theoretic and learning-based), and how we may be able to get the *best of both worlds* approach for both trade-offs. I cannot help it, so of course, I will give my two cents on multi-agent RL (MARL) too.

A hypothesis I have gotten to with my Ph.D. advisor is that we can get a lot of the \"best of both worlds", but researchers often don\'t want to compromise with the mirrored intellectual ideology. We want to coin **flexible** **centralization**, which implies that we give agents the ability to make decisions based on their surroundings, but we also use a central planning entity to point behavior in the desired direction.

Throughout this article, I will use a motivating example of a group of drones cooperating to accomplish a singular task. Tasks can include emergent phenomena such as flocking and human-centric applications such as search and rescue. Drones are fast, capable of high payload ratios, and cheap, setting up a plethora of applications. Though, deploying them in large numbers in dynamic situations is near impossible --- something that public encounters with them do not portray well.

The canonical example of drone coordination I have seen in the last years is the [large](https://www.youtube.com/watch?v=44KvHwRHb3A) \| [light](https://www.youtube.com/watch?v=BjRb6u_PQwQ) \| [shows](https://www.youtube.com/watch?v=zXoW2iHfVYA) at high-profile events. To be blunt, those agents are not intelligent and likely do not know there are neighbors. They are impressive, but not that interesting. The drones in these groups are likely tracking close GPS trajectories. The field can do much better, and I hope to be a part of that.

## Engineering Limitations of Multi-agent Control

Let's start with some review. There are two paradigms of multi-agent control that I will use throughout, and if I do nothing else right I would like you to take away that these exist and what their strengths are:

***Decentralized control*** is the solution where each agent makes decisions based only on the observations it picks up from its neighbors (major strength: emergent capability, low controller complexity). It's how we see animals working, but for modern systems, it is very challenging because it needs policies that are agnostic to the number of neighbors it observes (math limitation), and communicating with neighbors that come and go is very, very hard (hardware limitation).

***Centralized control*** has been the canonical approach of control engineers for decades, where they design control laws that adapt to the challenging environment with more actions (strength: acts like a scaled-up version of existing methods). These tend to need a big computer to find the optimal behavior and lose touch with the *elegance* of multi-agent interactions (needs to communicate with each agent, computation scales quadratically+ in the number of agents).

Both of these paradigms have clear strengths, though only one of them seems to acknowledge the practical limitations as much. I'll explain.

There is quite a large gap between the possible implementations of multi-agent control in hardware and the simulated experiments of machine learning conferences. Deploying more than one robot to work in synchrony with its mates is an exceedingly hard task due to scaling factors and plain probabilities of failure increasing linearly with more agents. It feels like a trend in my academic career to run with ideas until you realize there are not the right tools for evaluating your ideas. Deep RL is at the peak of this field-wide challenge right now.

While researchers are interested in what happens with thousands of learning-based teaming up, most hardware applications don't make it above 10 robots. There are a [couple](https://www.robotarium.gatech.edu/) \| [recent](https://project.inria.fr/dotbots/) tools for improving access to realistic experimentation, but they are not widely adopted nor the norm. The crucial limiting factors, with their general strategy, are:

-   communication with many mobile agents (limits decentralized control)

-   optimization techniques scale poorly with dimension, often quadratically (limits centralized control).

In one of my first projects to come out of mentoring undergrads, we tried to paint the picture of how hard scaling decentralized control is. We built a simulator called [BotNet](https://github.com/PisterLab/BotNet) and showed that even the most basic multi-agent control scenarios totally break down when agents are subject to a probabilistic communication likelihood (basic activities like flocking or forming shapes do not work). Communication is very, very hard and most control designers do not acknowledge it in their papers. The tool has a gym interface if you would like to see how quickly multi-agent reinforcement learning techniques break down when applied to moving radios.

## Partially Centralized Control

Bees have fellow bees tell them where to go. The hive is not fully decentralized, and it is by definition not centralized because the pollen-harvesters make independent decisions when out in the world. The hive tells them \"let's use the info that we have when we can." This is the idea of **flexible centralization** I hinted at before. There is an existence proof for this hierarchical approach (which I would also call partially centralized and partially decentralized control, but those together create confusion).

Full decentralization is an over-the-top solution to prove intelligent systems do not need a centralized governor. It is a valid research path, but not one that I would stake my bet on for the solution of the future for applied tools. Therefore, we know we want to pass some information from our decision-making node and that we want agents to make some of their own decisions. This is naturally parsing itself into a **hierarchy**.

This is where multi-agency connects to my intellectual priors --- my work in model-based RL has always bounced around the notion of hierarchy, and I've been selling my work on microrobots as the future beneficial "swarm". Hierarchical RL (HRL) promises to learn levels of centralization for agents akin to any learning problem. This could be a crucial tool for providing the flexibility I posit we need. Learning the intermediate representations obviously adds complexity, but in spirit, it is an automated way to take the best of both centralization and emergence. This moved our idea from partially centralized control to flexibly centralized control.

When all the agents are spread out and doing their own thing, we want the policies to be chosen by the central governor. How else can one get information? When the agents are covering the same territory, we want them to communicate with each other to eliminate collisions and wasted time. The challenge is how to translate this intuition into practice.

What interests me is using variable abstractions on the notion of time-horizon to allow agents to reason at different hierarchies. That, though is left to future work at my hopeful new job.

## Multi-agent RL & Looking Forward

A final note on multi-agent reinforcement learning should wrap this up. I think multi-agent RL falls for the trap where designers think that because RL is a good framework for solving the problem (trial and error learning, reward maximization, etc), the agents they are trying to model must functionally be doing the same (at the biological level). There is a deep difference between modeling a group of humans hunting an ancient creature and these humans taking these actions because they feel rewarded. I think hunger, cravings, impulses, etc. are *crafted by* dopamine, but there are other chemical circuits in humans that impact their behavior. RL researchers should focus on scenarios where reward maximization is a more logical frame, such as exploration if they want to force a specific solution architecture onto a problem specification.

This fallacy will become increasingly important as multi-agent systems interface with society. There is a framing where the large recommender engines *are multi-agent control systems.* The systems are designed to be fully centralized (one policy works for each user) to not try and model the complex interactions between humans. As human preferences are fed back into the control problem, there will be emergent properties.

As machine learning interfaces at such a large scale, it is a multi-agent experiment. We need to use this lens to understand its effects. It's wild that systems as powerful as AlphaGo/Fold are acting on all of us without the majority knowing. Multi-agency and feedback are how we start to understand the effects.
