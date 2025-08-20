---
title: "The RLHF battle lines are drawn"
subtitle: "Tales of the open and closed sides, how these two dynamics will dictate progress and public perception."
date: 2023-02-27
type: newsletter
audience: everyone
visibility: public
post_id: 105456579.rlhf-battle-lines-2023
email_sent_at: 2023-02-27T19:31:27.401Z
---
It\'s been a couple of months since I [last shared my thoughts](https://robotic.substack.com/p/rlhf-chatgpt-data-moats) on the space of reinforcement learning from human feedback (RLHF), so I\'m due to go a little deeper. Ultimately, the known players for the next couple of years seem to have settled into plans. Half the companies will do everything to protect their IP and advantage and we\'ll see artifacts from the open others trickle, then flow, then amass by later this year. The open-source coalition is probably starting about 1.5 years behind in technological capacity. This is based on the hypothesis that the [OPT](https://arxiv.org/abs/2205.01068) models from Facebook follow GPT3 and [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/) follows [Chinchilla](https://www.deepmind.com/publications/an-empirical-analysis-of-compute-optimal-large-language-model-training). Both claims are a little stretched, but they\'re the leading beacons of what can be done on the open-source side of things.

On the other hand, we have seen the initial proposals from Microsoft & Google and OpenAI & Anthropic. If any other big companies had a card they were going to play, they probably would have. The missing component of these discussions is how these bets evolve from here. The only company sharing their \"plans\" is OpenAI with their lukewarm take on [planning for AGI](https://openai.com/blog/planning-for-agi-and-beyond/). The real discussions are around access to the compute resources and the talent needed to create these systems. The resurgence of generative AI is creating a crest in GPU usage, to the point where demand is and will exceed supply. For the cutting-edge GPUs, this demand is almost all enterprise customers too. Therefore, it takes even more clout and investment to close a cloud deal.

This clout is likely going to be *supported by personnel more than anything else*. The population of engineers that can manage the large distributed systems needed to train these models is so small (jokes on Twitter say it's [200 people](https://twitter.com/ericjang11/status/1627818245406461952)). Most companies are left to choose from the engineers that OpenAI et al. passed on hiring or have a strong moral conviction that they want to be doing their own thing / joining a new entrant. With the amount these people are paid, I\'m guessing most of these moral convictions are rare.

This leaves the vast majority of the talent behind the walls of a few companies that want to maintain their advantage.

While there is a huge need for oversight of these models, this advantage is unlikely to be broken up by legislation anytime soon. Instead of sharing publicly about the advances, as papers have become less frequent and less informative on these topics, the advances will likely go through a closed auditing organization. It seems likely that a couple of these non-profit language model auditing organizations pop up soon from the effective altruism / other rich folk circles. The narrative around this will be that the models cannot be released for safety reasons, again. Instead, we get an in-group, out-group dance.

The missing point of these arguments is that **not releasing models has its own set of harms**. The values the companies imbue into the models are way less traceable and the questions ultimately hover around *why should I trust this company*. This often goes unasked when the products are new and exciting, but becomes more difficult to ask when the company is entrenched. This dynamic is by design. For example, there will be some internal bias to model design based on the planned product and potential commercial processes (profits). OpenAI etc. try to tell us their internal tools are safe, but we can never know! If we cannot use their models, they should disclose the processes they use to reduce harm. Part of the motivation for my work on [Reward Reports](https://rewardreports.github.io/) was to create another potential documentation tool in these circumstances.

On the other side of things is the growing pressure on the open-source movement to catch up. The pressure is due to the fact that the open-source models could be left behind and all of the market opportunities will collapse (and become entrenched with) the closed counterparts. The leading open models are from Meta these days, and they\'re all released with **non-commercial** licenses. To avoid a long rant on the legal side of things, an organization \"just\" needs to recreate and continue on the LLaMA recipe and unlock that value.

The question of who that\'ll be is really up in the air. [OpenAssistant](https://github.com/LAION-AI/Open-Assistant) is already training good models, previewed under the moniker Joi, without RLHF (can chat with it [here](https://huggingface.co/spaces/HuggingFaceH4/chatty-lms); warning: it is a little slow and not tuned / with safety filters). EluetherAI is on a similar path to HuggingFace (maybe even ahead on training models), CarperAI is deep into a project for code models, and the same is very likely with many more machine learning startups. These trends will sound similar until the models appear.

Unfortunately, I suspect a couple of these efforts get nipped by the growing computing costs. As the efforts draw on, who foots the growing bill or what is the business incentive for releasing everything? There are a lot of reasons, but make sure it is discussed.

My predictions about having decent starting models and datasets within 3-6 months seem to really be taking shape. Other places like Allen Institute for AI are going to play in this space (e.g with their [RL4LMs](https://github.com/allenai/RL4LMs) library), but leave the training to others. The timeline for truly useful datasets seems more uncertain. Plenty of organizations want to release them, but the specifics of licenses and contents are to be determined. Ultimately, a lot of challenges come when releasing incremental progress because you get overloaded with community interest.

Finally, a race with kickstarting training and products is leaving behind interesting research questions (like Jan Leike sharing on [Twitter](https://twitter.com/janleike/status/1627023973040136192)). One of my deeper to-do\'s for the year is to figure out how to engage academics in the problem area of RLHF and ChatBots. Ultimately, we need the deep thinking and unbiased assessments that they would bring to the space. The entry point I see is studying one specific module of the system (e.g. reward model changes to the preference ranking system) within compute-tractable ranges. The missing component is a deep understanding of which scaling laws translate.

The open organization closest to releasing models right now, OpenAssistant actually has a team for safety engineering and all that, but I expect them to get criticized for releasing the model regardless. To address the challenges of these super-powerful models being in the open, we should need more powerful communications around gating techniques.

Sharing progress in the open has such a huge potential to reduce the hype and misinformation in the AI space while bringing in broad stakeholders (e.g. governments).

**As models become more important to a functioning society, effective access and information sharing between the open and closed alternatives should converge.** The information would be shared with different processes (e.g. papers vs. audits), but ultimately it should be a trade-off between slightly more information and more access vs. a closed model with maybe more performance. The power dynamics pushing these release strategies in other directions, to the extremes, are communication, policy, and strategy failures. The AI community needs to fix this rift pronto (as [I discussed with the term "AI alignment"](https://robotic.substack.com/p/ai-alignment)).

In some ways, the most popular models will have more societal pressure to be safe now that they\'re consumer-facing (not just researchers), which is almost a reasonable feedback loop. You create something powerful, you\'re on the hook with the media if you don\'t make it user-friendly. It\'ll be interesting to see if the more open organizations can keep up with this pressure, even when they (e.g. HuggingFace) actually care so much about harms and proper model access.

That mostly summarizes the RLHF / chatbot dance:

-   big companies are ahead, see the huge economic value, and will quietly set up processes to maintain that.

-   open source companies likely have flipped the acceleration of progress (behind by a lot, likely falling further behind now, but at a decreasing rate) and sometimes are duplicating each-others efforts.

-   corporate communications around safety are annoying and laden with strategic, not human, value.

![](images/105456579.rlhf-battle-lines-2023_262dd8b1-019d-492c-98d9-21abd8679848.png)

<div>

------------------------------------------------------------------------

</div>

#### Elsewhere from me

-   My team at 🤗 published a [blog post](https://huggingface.co/blog/red-teaming) introducing the concept of red-teaming for large language models, check it out!

#### From the rumor mill

-   Anthropic is raising more money ([NYTimes](https://www.nytimes.com/2023/01/27/technology/anthropic-ai-funding.html)),

-   Elon is likely to re-enter the open-source AI space this year (see his angry Tweets),

-   Sort of collusion agreement from all the big LM companies to not publish papers on it (Anthropic\'s papers are only on AI Safety it seems when you really dig into them),

-   Human feedback + learning on diffusion models is [here](https://arxiv.org/abs/2302.12192), expect more of this soon (especially from Stability). It\'s going to work really well (feedback labeling is faster, more intuitive, and more fun than text).

-   People under-appreciate fine-tuning alone compared to RLHF: lots of papers are coming out (mostly academic) showing how far you can get with instruction tuning and no RL. RL is still really really hard to do.
