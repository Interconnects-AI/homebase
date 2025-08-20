---
title: "SB 1047, AI regulation, and unlikely allies for open models"
subtitle: "The rallying of the open-source community against CA SB 1047 can represent a turning point for AI regulation."
date: 2024-07-17
type: newsletter
audience: everyone
visibility: public
post_id: 146686823.sb-1047-and-open-weights
email_sent_at: 2024-07-17T12:00:52.686Z
---
For my about quarterly update in the Interconnects universe, we have a few items:

1.  We now have a [basic merch store](https://interconnects.myshopify.com/), if you are so inclined.

2.  I've got a bunch of interesting guests lined up for interviews later this summer. Subscribe to the [podcast feed](https://podcast.interconnects.ai/subscribe) or [YouTube](https://www.youtube.com/channel/UCMhPRKnK8S_ruoGSt3vm1sQ) for native audio apps.

Please reach out if you have any feedback on this early endeavors. Comment below or reach out to `mail at interconnects.ai`. Onto today's article.

*Audio of this post is available [here](https://podcast.interconnects.ai/episodes/sb-1047-ai-regulation-and-unlikely-allies-for-open-models).*

<div>

------------------------------------------------------------------------

</div>

AI's future is going to be deeply tied to real efforts to regulate it. This was inevitable with the obvious power and dramatized narratives around the technology. Regulation is out of the gates.

Most unbiased technical experts on AI, who can be hard to find, will tell you it is difficult to create accurate and effective regulations on AI given how little we know about the technology. Some will go so far to say that AI *models* themselves are likely always going to be near impossible to regulate. Whatever the specifics of the matter, we're heading towards many conflicts over regulatory proposals and bills. CA SB 1047 is the starting line. Outside of California, there are many other regulatory bodies either taking action or commenting on the future prospects of AI.

Together, all of these efforts reflect common trends in efforts to regulate AI. I see two trends:

-   **Misunderstanding the stack from a rush to regulate**: From California regulating compute threshold of models to enforce safety (rather than considering the broader AI systems) to [France targeting Nvidia's integration of CUDA software on antitrust grounds](https://www.reuters.com/technology/french-antitrust-regulators-preparing-nvidia-charges-sources-say-2024-07-01/), we are far from the basic levels of education on the AI stack to make meaningful regulation. We're in an era of political wins for first movers, which incurs future costs in reduced growth.

-   **Antitrust attention from scaling AI:** The current regulatory climate, both in the US and in Europe, is anti-big-tech. One of few bipartisan issues. Companies scaling AI models with extreme capital expenditures, such as OpenAI and Anthropic, are getting sucked into the orbit of antitrust regulators given an already frothy environment. Without new laws, existing institutions can't do much to take down the biggest companies, but broad agreement can lead to measures that support open-leaning companies.

So long as open-source can avoid crippling regulation in the first camp, "open" broadly is positioned to win the cultural battle across many types of power, from the technical in SF to the political in Washington DC.

## SB 1047 and targeting regulation

*These are my views and not those of my employer.*

Let's start with CA SB 1047. The [California bill](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1047), which has passed the state Senate and is moving through committees, has been discussed at length online (such as on [Hyperdimensional](https://www.hyperdimensional.co/p/californias-effort-to-strangle-ai), [The Zvi](https://thezvi.substack.com/p/on-the-proposed-california-sb-1047), and [my own Interview series](https://www.interconnects.ai/p/interviewing-dean-ball-on-ai-policy)) and has clear clauses that can make life very awkward for open-source developers. I don't plan on covering the specifics here. Rather, I wanted to capture the cultural moment that is forming around the regulation of AI, and especially how it relates to the prospects of a healthy open-source ecosystem for large AI models in the near- and long-term future.

This legislation, while local to California, would effectively impact every language model. Any model operating in California would be subject, and most models are primarily developed in San Francisco and neighboring cities.

CA SB 1047 touches on many recurring themes of AI regulation: [Compute thresholds for classifying models](https://arxiv.org/abs/2407.05694v1), [committees for reviewing AI applications](https://www.hyperdimensional.co/p/the-political-economy-of-ai-regulation), whether [AI should be regulated at the system or model level](https://www.answer.ai/posts/2024-06-19-ai-defn.html), and more. On every side of these issues, the bill is on the wrong side of history. It would have a group of unelected officials decide which models being trained should be reported to them.

A large theme of the bill is to regulate developers for downstream harm of models. **We should only regulate developers for** ***known harms native to the model*****, otherwise, we should regulate systems deploying the model.**

There are two ways that people have criticized the potential impact of the bill on downstream open-source efforts.

1.  The simple one: Small developers won't be able to pay to comply with more regulatory oversight while bigger developers will. This is a common refrain against technology regulation in general, painting efforts as regulatory capture.

2.  The impactful one: Models released as open weights with compute above California's threshold will be in some manner held liable for harms caused by future derivates of the model. This would impact open-source AI by making organizations even more wary of releasing their weights.

What is really odd is how Senator Wiener, who introduced the bill, [said with respect to the blowback from this bill "I did not appreciate how toxic the division is."](https://archive.is/e5n9A#selection-979.1-979.47) AI is how the domain where the giants of technology are staking off their claims for the future, such dispute is the starting point. The list of supports for the bill, Geoffrey Hinton, Yoshua Bengio, and Dan Hendrycks, are all people that think very reasonably about *some* things, but I regularly think they're getting stuck in blind spots when this is their answer to "what should we regulate today?\" Even Anthropic has [stepped back from this ledge](https://archive.is/e5n9A#selection-1105.227-1108.0).

> Anthropic CEO Dario Amodei said during an interview on the In Good Company podcast in June that the regulation envisioned in SB-1047 is too early---that industry consensus around a "responsible scaling policy" should come first.

**On thresholds**: The general idea of a threshold is to set a target by which a model that is above it triggers regulatory practices. Thresholds became popular via the [Biden Executive Order on Safe, Secure, and Trustworthy Artificial Intelligence](https://www.whitehouse.gov/briefing-room/statements-releases/2023/10/30/fact-sheet-president-biden-issues-executive-order-on-safe-secure-and-trustworthy-artificial-intelligence/), where they included the threshold of 10\^26 FLOPs. There are a lot of questions on where that threshold came from, with [guesses being just above the GPT-4 level](https://arxiv.org/abs/2307.03718). The executive order was [written and influenced by many organizations, such as classic Washington think tanks like RAND](https://www.opensecrets.org/news/2024/01/federal-lobbying-on-artificial-intelligence-grows-as-legislative-efforts-stall/). CA SB 1047 started with this 10\^26 FLOPs number but [was modified to be 10\^26 FLOPs and \$ 100 million to train](https://thezvi.substack.com/i/145370669/the-big-flip). This is much more reasonable, but plenty of the problems with the bill remained.

While the big picture trend is likely to be that AI models are getting larger, thresholds are a messy process that very poorly captures the dynamics of model capabilities to a user. Even the core metric used in regulation, [floating point operations (FLOPs), is very hard to measure](https://epochai.org/blog/measure-FLOPs-empirically). There are theoretical FLOPs based on a data center capacity, but in reality, the actual utilization is far lower. Beyond this, we have new techniques like [distillation](https://www.interconnects.ai/i/145870222/are-gemini-flash-and-claude-haiku-distilled) that are making leading models smaller to meet high needs for inference.

If you mitigate the compute I can use for training, I'll spend more on inference.

If you mitigate the compute I can use for training, I'll spend more time training specific models that are networked together in a system.

If you mitigate the compute I can use for training, I'll develop better sparse and efficient training methods.

I trust technology companies, especially scrappy startups, to be much better at innovating in a fast-moving technology than I do to see a regulatory body nail a threshold correctly.

**On models vs. systems**: Regulating models specifically is bad for the open-source community. The open models community operates with just that, models. They take a model, fine-tune it, and or run it locally. Large companies, which don't actually trade models, do something far more complicated. The "model" in something like ChatGPT is the core computing engine. Around it are many more models. As mentioned above, if you regulate the model, companies serving complicated systems can distort the meaning of "a model" to still meet their needs. If you regulate this notion of model, the open source community would need to rebuild tools, compute infrastructure, and more in order to accommodate it.

I'd expect that most of the harm happening from language models to date is through closed AI systems. To have disproportionate exposure to regulation while being the minority participant in deploying the technology is tough.

**On the future of SB 1047:** Regardless, the process for clearing out this would-be law is flawed. [Dean Ball explained to me in June](https://www.interconnects.ai/p/interviewing-dean-ball-on-ai-policy) the process that state bills will often follow to potentially become law:

> **Dean W Ball** (00:18:31): Yeah, well, and I think also worth noting is that Scott Weiner, the state senator who authored the bill, is a very powerful figure in California politics. And I would guess that a lot of the senators who voted in favor of the bill really barely looked at it and aren\'t even necessarily thinking about their constituents. First and foremost, they\'re thinking more about, well, Scott\'s my ally. I need X, Y, Z thing from Scott. So I\'m going to vote yes on his bill. Um, and that dynamic will apply at the assembly too is, is very common. Uh, the, the California legislature has a history of, um, uh, sometimes even unanimously passing bills that the governor then vetoes. So the governor is often expected to be a little bit the adult in the room on this stuff.

The fragility of the situation is why so many leading figures in AI and related fields are [clearly stating their disapproval of the bill](https://x.com/AnjneyMidha/status/1811207378949607638).

This is a repeating cycle, earlier this year the [National Telecommunications and Information Administration (NTIA) solicited comments on open-weight models](https://www.ntia.gov/federal-register-notice/2024/ntia-receives-more-300-comments-open-weight-ai-models#:~:text=Home-,NTIA%20Receives%20More%20Than%20300%20Comments%20on%20Open%20Weight%20AI,benefits%20while%20mitigating%20the%20risks), and most of the comments warned of things that we are now debating in CA SB 1047.

## Unlikely allies of "open"

#### **Antitrust attention and opportunity**

While SB 1047 is the hot news, the real reason for revisiting AI regulation and open source is how obviously the cultural winds have been shifting in favor of open-source AI models. What other types of technology are ones that all of the [Federal Trade Commission (FTC)](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/07/open-weights-foundation-models), [China](https://www.wired.com/story/chinese-startup-01-ai-is-winning-the-open-source-ai-race/), [leading AI academics](https://info.deeplearning.ai/ais-cloudy-path-to-zero-emissions-amazons-agent-builders-claudes-ui-advance-training-on-consumer-gpus), and [Marc Andreessen's a16z](https://a16z.com/podcast/californias-senate-bill-1047-what-you-need-to-know/) will agree on? Open-weight models, relative to somewhat unclear "fully open-source AI," are becoming a consensus opinion.

This comes in the context of increased scrutiny of the AI angles of big tech. Two companies that don't even have their own models, Apple and Microsoft, have [backed out of OpenAI board observer seat roles](https://www.ft.com/content/ecfa69df-5d1c-4177-9b14-a3a73072db12) (or prospective roles in Apple's case). The bipartisan agreement that big tech companies are "bad" for Americans has many angles to play for open-source. It'll limit the ability of these companies, potentially soon to include Nvidia, to make deals that serve each other collectively.

I'm new to antitrust and regulation as an area of focus, but this level of early action in an area only seems to be prompted by a long-simmering discontent with the companies. None of these companies are really making money with AI, outside of boosting their valuations, but regulators are still eager to limit their mobility. Open-source AI is the most mobile and fluid way to build the technology, requiring new ways of building value. The big technology companies still have countless advantages over open-source, but culturally open-weight models seem to have legs.

I'm more optimistic now about the future of [truly open-source AI](https://www.interconnects.ai/p/an-open-source-llm) than I have been since ChatGPT. We have to keep building this momentum and ecosystem.

#### **China and national security**

Any inertia added to the U.S. open-source AI ecosystem will heavily favor China. While the leading AI models will likely be closed for every due to the benefits of integration and risks of sharing industry secrets, there will *also* be a flourishing open model ecosystem. People will always turn to some open-source alternative, even if the peak performance isn't as good --- we've been seeing this for decades in open-source software. Many of the reasons people [enjoy truly open-source software](https://www.interconnects.ai/p/an-open-source-llm) don't translate to open-weight models, especially if the lead proprietors are influenced by Chinese politics.

There are many major open-weight language models coming out of China. The names that come to mind are [01-ai's](https://huggingface.co/01-ai) Yi (startup), [Qwen](https://huggingface.co/Qwen) from Alibaba, and [DeepSeek](https://www.deepseek.com/) (startup), but there's a long list of minor players --- e.g. Baichuan AI and Zhipu AI just don't have as strong of marketing in the U.S. (Zhipu AI is behind GLM-4, a high scoring model on ChatBotArena). This steady flow of models is a mix of practical considerations such as [Nvidia largely avoiding the Chip Ban](https://www.businessinsider.com/nvidia-still-selling-chips-to-china-despite-us-trade-restrictions-2024-2), reliance on older computer clusters, and models needed in the open ecosystem being relatively small (7 to 70 billion parameters). At the same time, we should expect China to be clever and keep building its way through this. It will never be *impossible* for China to have similar compute stacks as the leading American companies --- it'll just take them working 2 to 4 times harder to get there.

The cloud shadowing this article, open-weight models, and the entire Western AI ecosystem is prospects of [nationalization for security concerns](https://www.youtube.com/watch?v=K0Pa5oudUp4). The threat of China taking over control of a stack as important as open source AI by a regulation\'s own goal looms bigger than any national security risks of China infiltrating national labs --- this could happen without any malicious action and statecraft. Anyone worried about China should be worried about this too. Don't just focus on the fancy top end of AI models, but also on who controls the long tail.

#### **Politicizing open source AI**

This is not a political blog nor will it become one. Putting aside the profound sadness of this weekend's events aside in the United States --- on Monday, Trump announced his running mate, J.D. Vance. Earlier this year, Vance [expressed some concerns over the potential concentration of power in the AI space](https://x.com/JDVance1/status/1764471399823847525) in [reaction to the Gemini saga](https://www.interconnects.ai/i/141929268/is-google-back-on-top-geminis-woes).

> There are undoubtedly risks related to AI. One of the biggest:
>
> A partisan group of crazy people use AI to infect every part of the information economy with left wing bias. Gemini can't produce accurate history. ChatGPT promotes genocidal concepts.
>
> The solution is open source

This is by no means a commitment to policy, but it shows how far AI has enmeshed itself with our current political environment. This goes hand in hand with concerns of antitrust, and is a view that open source is the alternative to big tech companies. This isn't universally true, given how much value is creation through aggregators that leverage the zero marginal cost of users, but is likely a narrative we hear again and again.

<div>

------------------------------------------------------------------------

</div>

## What would I regulate today?

The common refrain when you dunk on every attempt to regulate AI to date is "What would you regulate?" There are remarkably few people putting coherent worldviews out on this. Most of them are like Gary Marcus, [who posits that modern language models won't lead to any form of superintelligence, but we should over-threshold oversight like in CA SB 1047 and other policy proposals](https://garymarcus.substack.com/p/the-misguided-backlash-against-californias). Most reasonably drafted proposals are probably narrow and timid, making people feel like they aren't worth putting out there. One that I found was Andrew Ng's take on ["what he would regulate" in The Batch](https://info.deeplearning.ai/ais-cloudy-path-to-zero-emissions-amazons-agent-builders-claudes-ui-advance-training-on-consumer-gpus) (which also has a good commentary on CA SB 1047).

> I would welcome outlawing nonconsensual deepfake pornography, standardizing watermarking and fingerprinting to identify generated content, and investing more in red teaming and other safety research. Unfortunately, the proposed bill pursues a less beneficial and more harmful path.

This is a good start. I think Andrew can be a little more specific and advocate for more resources (which are dispersed and controlled in the same laws enforcing oversight. In summary, I think attempts to regulate the following are worthwhile:

-   **CSAM + nonconsensual deepfakes**. It is likely that AI tools will make it easier to generate and distribute child sexual abuse material, so we need to make major investments to counteract that. We've already seen [deepfakes be deployed in very malicious contexts](https://www.wired.com/story/florida-teens-arrested-deepfake-nudes-classmates/). These interventions will happen at multiple levels of the stack: models, data, and distribution (e.g. social media).

-   **Mitigating the impact of [slop](https://simonwillison.net/2024/May/8/slop/)**: Watermarking regimes *for human content* not for AI content. AI content will be so prevalent we cannot hope to watermark even a majority, let alone reliably.

-   **User privacy, PII, and right to be removed**. Given that AI is going to absorb all the data on the internet, legislation to mandate deletion and safe storage of data is very important. Without it, unprofessional models of the future likely can be search engines for sensitive data. Rather than waiting for problems, we could spend money on cleaning our house up. One example is [Clearview AI's data deletion requirement from California](https://www.clearview.ai/privacy-and-requests) (consider doing this if you're a resident).

-   **Infrastructure for future risks**. In order to keep up with new and emerging risks, we should invest in infrastructure for researchers to have [deliberate and non-random access to state-of-the-art AI models](https://sites.mit.edu/ai-safe-harbor/). We can't rely on the AI labs to determine who these people should be and how they should access it.

<div>

------------------------------------------------------------------------

</div>

**Housekeeping**

-   Audio of this post is available (soon) in [podcast](https://podcast.interconnects.ai/) form (and sometimes on [YouTube](https://www.youtube.com/@interconnects)).

-   My real podcast is at [retortai.com](http://retortai.com).

-   *Paid subscriber Discord access in email footer.*

-   Referrals → paid sub: Use the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   Student discounts in [About page](https://www.interconnects.ai/about).
