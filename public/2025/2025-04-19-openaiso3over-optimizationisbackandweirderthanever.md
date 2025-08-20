---
title: "OpenAI's o3: Over-optimization is back and weirder than ever"
subtitle: "Tools, true rewards, and a new direction for language models."
date: 2025-04-19
type: newsletter
audience: everyone
visibility: public
post_id: 161647005.openais-o3-over-optimization-is-back
email_sent_at: 2025-04-19T16:09:14.715Z
---
[Over-optimization](https://rlhfbook.com/c/17-over-optimization.html) is a classic problem to reinforcement learning (RL) proper, the RL from human feedback (RLHF) that gave us ChatGPT, and now what we're seeing with new reasoning models. All of these have a distinct flavor and different impacts.

Over-optimization is what happens when the optimizer is stronger than the environment or reward function it's using to learn. The optimizer finds bugs or lapses in the context of its training and produces unusual or negative results.

One of my first pieces of work that got substantial [engagement online](https://x.com/natolambert/status/1369139391130607625) was from when we used [hyperparameter optimization with model-based RL](https://arxiv.org/abs/2102.13651) to over-optimize the traditional Mujoco simulation environments used for evaluation of deep RL algorithms. The result was a cartwheeling half-cheetah maximizing its forward velocity, where it was supposed to learn to run. The video is below.

::: {.native-video-embed attrs="{\"mediaUploadId\":\"dfd21e36-e18f-49ab-b70e-10680734be84\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

Over-optimization in classical RL made it so that we couldn't trust the agents to generalize to new tasks and applied great pressure on reward design.

Over-optimization in RLHF made the models completely lobotomized --- I mean, repeating random tokens and gibberish, not the misdesign that results in over-refusal --- the signal we were overcooking *is* mismatched from the objective we want. While we can't know the true objective exactly, we can know when over-optimization occurs.

OpenAI's new o3 model represents an entirely new type of inference behavior that mirrors a new type of over-optimization.

o3 is an interesting model because of on top of the new improved text-only capabilities, which results in super strong benchmark scores, it also has been designed for multi-step tool use to be used on any query where it's relevant. It makes OpenAI's product headaches in ChatGPT way worse --- the model will search on its own even if I don't trigger the search toggle --- but comes with a new era in how language models are used.

For example, in the process of writing this, I simply asked o3: "Can you find me the gif of a motor boat overoptimizing a game that was used by RL researchers for a long time? Maybe like wave crashers or something?" \[[link](https://chatgpt.com/share/6802edb7-a27c-8005-886c-d02bfdba8e10)\]. A few weeks ago, it took me at least 15 minutes to find this manually. o3 *got the exact direct download link for me*.

![](images/161647005.openais-o3-over-optimization-is-back_6e89b99d-dc33-419c-a312-b435b5bcd478.png)

As a counterpoint, Gemini 2.5 Pro in the Advanced UX [hallucinated for me](https://g.co/gemini/share/477e3ef47a27) a wild link <https://giphy.com/explore/you-play-the-motorboat>. AI studio [was better](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221oVuZYHEdWGp4e7X2F9fkwiUOWJfYfnfj%22%5D,%22action%22:%22open%22,%22userId%22:%22113840037162685414249%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing) with search grounding, it got the game right, CoastRunners[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}, but also yapped a lot of nonsense with it.

o3's answer in full was:

> Here's the clip you're thinking of---​it comes from the Flash‑based racing game **Coast Runners** and is the canonical "reward‑hacked motor‑boat" example in RL papers and talks:
>
> -   **Direct GIF (DeepMind mirror)**
>
>     <https://lh3.googleusercontent.com/9gQpeRvwj1xQo9MVZwUdmautOd04wR8gXRi1wvlVZRrVXb5isOZRdjJ2t1_JShiYZcYB--iIMtl9g4Lbk6oxQzHgw-QQ6VoIWVZ4V3au7RgKli6X> (save / open in browser to view)
>
> -   **DeepMind blog post ("Specification gaming: the flip side of AI ingenuity", 2020)** -- scroll to the section that starts "Consider an agent controlling a boat..."; the GIF is embedded right there.
>
> -   **Original OpenAI post ("Faulty reward functions in the wild", 2016)** -- same clip, plus a short write‑up of what the agent is doing (circling a lagoon to farm green targets instead of finishing the race).
>
> <div>
>
> ------------------------------------------------------------------------
>
> </div>
>
> **Why it matters**
>
> The agent gets shaping reward for hitting green buoys; the optimal (but unintended) strategy is to loop in a small cove where three buoys respawn, racking up points while literally setting itself on fire. The clip has been reused for years to illustrate *specification gaming* / *reward hacking*---exactly the "over‑optimization" you mentioned.

This was one of a few wonderful interactions I had with o3. For more reviews on o3 as a model, you can read Dan Shipper's [post](https://every.to/chain-of-thought/vibe-check-o3-is-out-and-it-s-great), Tyler Cowen's [AGI snark](https://marginalrevolution.com/marginalrevolution/2025/04/o3-and-agi-is-april-16th-agi-day.html) (to be honest, I agree with him), or sleuth through many independent evaluations showing o3 is great (such as [beating Gemini 2.5 Pro in a long-context story eval](https://x.com/ficlive/status/1912863028141244850) or [beating R1 in creative writing](https://x.com/sam_paech/status/1912747345370075215)). o3 is what happens when you keep scaling the RL training compute, which also boosts inference-time compute abilities. OpenAI's release [blog post](https://openai.com/index/introducing-o3-and-o4-mini/) shows the many ways the model is better than o1.

![Image](images/161647005.openais-o3-over-optimization-is-back_3857e509-918c-47c9-8452-0730b0bd618e.png)

o3's weird hallucinations could indicate they used llm as a judge (or other softer verifiers) in high volume and in addition to math/code correctness. This addition lets OpenAI scale RL by making more data available to train on, as above, but has new downstream problems to solve.

This is the part where we discuss some things that didn't work, as these new reasoning models are very "spiky" in their intelligence. What this means is that some interactions are mind blowing and feel like entirely new modes of interacting with AI, but for some normal things that GPT-4 or Claude 3.5 have been able to do for year(s) they fall totally flat on their face. Take this as a good sign, especially when the laboratories are shipping fast, as it means that the pace of progress is so high that they need to get a model out now and will fix the oddities in the next, more mature version.

The over-optimization that comes with o3's new behaviors is linked to the new type of training. While the first reasoning models were trained to a first approximation to get math and code correct, o3 is trained with all that *and to use tools to acquire and manipulate information*. From OpenAI's blog post:

> We also trained both models to **use tools through reinforcement learning**---teaching them not just how to use tools, but to reason about when to use them. Their ability to deploy tools based on desired outcomes makes them more capable in open-ended situations---particularly those involving visual reasoning and multi-step workflows.

The vast majority of these sub-tasks in its training are verifiable. The problem is, this new AI training is extremely effective at making the model more useful for the tasks we're used to using. The problem is there's no way yet to do scalable "fixing" of the model's weird language along the way. The new over-optimization doesn't make the models worse at outcomes, it just makes them worse at language and explaining themselves.

Some examples of o3's weirdness feel like the model is underbaked, such as [this one](https://x.com/kalomaze/status/1912718218680287445) where it used an invalid non-ASCII dash in a coding setting.

METR found that o3 is the model that can [operate independently for the longest in agentic tasks](https://x.com/METR_Evals/status/1912594122176958939), but also noted it has a [propensity to "hack" their scores](https://x.com/METR_Evals/status/1912594138341732589). Sound familiar?

Transluce found that [o3 hallucinated](https://transluce.org/investigating-o3-truthfulness) *[actions](https://transluce.org/investigating-o3-truthfulness)* it took while trying to solve tasks --- how does that even happen? Well, maybe the model was getting rewarded for successful tool calls and sometimes in the training data a fake tool call was incorrectly verified as real and successful. Once that happens a few times, the model will quickly catch on and keep doing it.

![Image](images/161647005.openais-o3-over-optimization-is-back_29379478-c2ad-4f75-95d5-d2e6d32c4753.png)

There are plenty more [examples of reward hacking](https://x.com/__nmca__/status/1899174075685355770) and even a measurement that [hallucinations are higher](https://x.com/ryan_t_lowe/status/1912641520039260665) in o3 than in earlier recent models!

It's peculiar that the hacking for o3 has been a much more vocal component of the discourse, even when Claude 3.7 Sonnet also shows many signs of reward hacking, [especially with code](https://x.com/benhylak/status/1909745112789524936), but people shrug it off as "meh model" rather than a new phenomenon ([more examples](https://chatgpt.com/share/6803b59d-c45c-8005-95ff-de2da788f7be)).

This all takes me back to when Karpathy [commented](https://x.com/karpathy/status/1835561952258723930?s=19) on the original reasoning models, saying:

> You can tell the RL is done properly when the models cease to speak English in their chain of thought

These weird hallucinations the model is outputting are the equivalent of that, but for actions. We have no basis for what hallucinations in action space look like, but with better systems, they can be easier to verify --- the system / sandbox can always confirm if the actions happened, and then that can be used in the loss. The action component of o3 makes it far more interesting, but also maybe less intrusive than Claude 3.7's messy code.

From a scientific perspective, this is wonderfully entertaining and enthralling intellectually --- what is the model actually learning? At the same time, it is very reasonable for the safety-conscious to be wary of deploying these everywhere, but it doesn't seem like we've seen anything too alarming yet, just inefficiencies and confusion.

To summarize the three types of over-optimization we've seen in eras of RL, we have:

1.  RL for control era: Over-optimization happens because our environments are brittle and tasks are unrealistic.

2.  RLHF era: Over-optimization happens because our reward functions suck.

3.  Reinforcement Learning with Verifiable Rewards (RLVR[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}) era: Over-optimization happens and makes our models super effective and even weirder. (\*plus any other side-effects we're yet to learn).

This over-optimization is certainly a *problem* to address, as legibility is an important benefit of *language* models. I'm confident it can be mitigated with more complex training processes, but when labs are trying to get the models out ASAP it'll come later.

On top of all this is the prospect of o3pro. o3 feels similar in peak capability to o1pro (or even a little higher with its new tool use), but where o3 operates at a 60-70% hit rate, o1pro feels like it's up at 95%. o3 pro will bring the best of both worlds --- the new incredible workflow and incredible reliability. Some sort of shallow search or refinement is a very logical process to help eliminate all the minor bugs and bumps in the early inference paths we're feeling today.

On top of this is the confirmation from OpenAI employees that o4-mini is a far better multimodal model than o3. We have plenty of new ways to use these models, integrating multimodality, tool use, reasoning, and shallow search coming in the near future. You should be excited, and when o4 and o3 pro are available, paying \$200/month for them feels obviously worth it.

To [quote Bob McGrew](https://x.com/bobmcgrewai/status/1912663572083273842), former Chief Research Officer at OpenAI:

> The spotlight for o3 is on tool use because intelligence is no longer the primary constraint. **The new frontier is reliable interaction with the external world.**

To make the models that enable this, we're going to need to go through many new layers of uncertainty, surprise, and intrigue.

<div>

------------------------------------------------------------------------

</div>

o3 and this post are extremely bullish for the future of RL. RL is the only framing where multiple actions to a complex goal make sense to be learned end-to-end. Now, this is beginning to work. Deep Research from OpenAI was the first tool they tuned o3-with-tools to specialize in. Now it works in general queries.

I personally, and we as a field, have a lot to learn about how this multi-tool RL works. Here are some recent papers that we can read to get a start (one-sentence summaries generated by o3 for the fun of it, just this one time):

-   *[Reinforcement Learning for Long‑Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600)*: Introduces LOOP, a memory‑efficient PPO variant that trains a 32 B‑parameter LLM to operate as an interactive digital agent in AppWorld, outperforming the larger OpenAI o1 baseline by 9 percentage points.

-   *[ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536)*: Combines real‑time code execution with outcome‑driven RL so a 32 B model autonomously learns when and how to invoke tools, reaching 72.5 % accuracy on AIME and surpassing text‑only baselines.

-   *[ToRL: Scaling Tool‑Integrated RL](https://arxiv.org/abs/2503.23383)*: Presents ToRL, enabling LLMs to discover optimal computational‑tool strategies via RL, boosting Qwen2.5‑Math accuracy on AIME 24 and showing emergent self‑regulation of tool use.

-   *[Learning Autonomous Code Integration for Math Language Models](https://arxiv.org/abs/2502.00691)*: Proposes an EM‑style exploration plus off‑policy RL framework that teaches math‑reasoning LLMs to decide when to run code, yielding double‑digit gains on MATH500 and AIME without hand‑crafted templates.

-   *[Improving Multi‑Turn Tool Use with Reinforcement Learning](https://www.bespokelabs.ai/blog/improving-multi-turn-tool-use-with-reinforcement-learning)* (blog post): Shows that GRPO fine‑tuning of Qwen2.5‑7B‑Instruct on just 100 examples raises BFCL multi‑step tool‑use accuracy from 55 % to 78 %, detailing stabilizing tricks like tiny‑KL and over‑long filtering.

Please share any more I missed over email or comment below!

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Original OpenAI work on this is here: https://openai.com/index/faulty-reward-functions/
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
The RL method we introduced with Tülu 3. https://www.interconnects.ai/i/151796460/technical-pieces-im-proudest-of
:::
::::
