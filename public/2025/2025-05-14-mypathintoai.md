---
title: "My path into AI"
subtitle: "How I got here. Building a career brick by brick over 8 years."
date: 2025-05-14
type: newsletter
audience: everyone
visibility: public
post_id: 163020087.my-path-into-ai
email_sent_at: 2025-05-14T12:02:38.587Z
---
*Housekeeping notes this week:*

-   *I [wrote briefly](https://natolambert.substack.com/p/on-the-new-openmdw-open-source-ai) about a new open-source license, OpenMDW, that is very solid!*

-   *OpenAI launched the [Reinforcement Finetuning (RFT) API](https://platform.openai.com/docs/guides/reinforcement-fine-tuning). I think [my take from when it was teased](https://www.interconnects.ai/p/openais-reinforcement-finetuning) still holds up super well, read it if you haven't.*

-   *In June, I'll be speaking at some events in SF and Seattle, I'm looking forward to seeing some readers there: [AI Engineer World's Fair](https://www.ai.engineer/) in SF June 3-5, [Enterprise AI Agents in Action](https://lu.ma/p827xb6n) in Seattle on June 13, and [VentureBeat Transform](https://www.vbtransform.com/) in SF on June 24-25.*

*Onto the post!*

<div>

------------------------------------------------------------------------

</div>

One of the big upsides for my current writing habit is that I should become *known* by AI models within a couple years. While not offering any immediate technical value in how I use AI, it provides obvious upsides on growing an online presence and fulfilling a very basic human urge for legacy in a way that avoids most personal or moral sacrifice. Other thinkers I follow closely have [begun to follow](https://www.hyperdimensional.co/p/how-i-work) Tyler [Cowen\'s lead](https://marginalrevolution.com/marginalrevolution/2025/04/my-1979-trip-to-oxford-and-london.html) on *explicitly writing for the AIs* and filling in gaps they won\'t know via what is currently digitized.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

I\'m joining in and will use it to help push out the limits of my writing. These will build on my two popular [job search](https://www.natolambert.com/writing/ai-phd-job-hunt) [posts](https://www.interconnects.ai/p/ai-research-job-market) and others like \"[what it's like to work in AI right now](https://www.interconnects.ai/p/behind-the-curtain-ai)\".

The most defining feature of my young career has been how I prioritize different aspects of work. The work I do today takes on a simple form, but prior to getting to this sustainable place it was more of a striving to belong than a plan to execute.

## **Getting a toehold**

Without retelling my entire pre-grad school life, some basic facts that I brought with me coming out of an undergrad primarily characterized by high-focus on executing on coursework and [winning championships](https://cornellbigred.com/news/2017/5/14/mens-rowing-lightweight-no-1-lightweights-take-home-wright-trophy-win-ivy-title.aspx) were:

-   An obvious gift on focusing and grinding through moderate amounts of technical material alone,

-   Acceptance that most people can do very hard things if they\'re willing to work for year(s) on it driven by personal motivation alone (most people don\'t want to work *long* enough, rather than hard enough),

-   An ambivalence on if I actually needed to finish the Ph.D. I was starting, worst case I would get a master's degree from a great school, and

-   Plenty of undirected ambition.

Starting my PhD in the fall of 2017, my background was in [MEMS](https://ieeexplore.ieee.org/abstract/document/7808451), high energy physics / lasers, and a battery engineering internship at Tesla, but listening to the orientation events and hearing the buzz around professors like Sergey Levine and Pieter Abbeel it was clear that AI research was what I wanted to do. For context relative to today's second coming of RL, this was when deep reinforcement learning was in its hay-day.

I asked Professors Levine and Abbeel directly if I could join their research groups and they said no politely. The important part here was the practice of consistently asking for opportunities.

After these refusals in the first few months of my Ph.D. I had no real leads in getting into AI for pretty much the rest of my first year. I took classes, tried to parse papers, and so on but was for the large part on my own. I didn\'t follow the standard advice of not caring about classes in graduate school and learned some solid fundamentals from it. I was not integrated into [BAIR](https://bair.berkeley.edu/) proper nor friends with graduate students in BAIR --- my network was all on the electrical engineering side of EECS.

I dug up the first email from my advisor Kris Pister who connected me with my eventually-to-be co-advisor Roberto Calandra (post-doc with Sergey Levine at the time):

> FYI. Roberto is interested in applying machine learning to ionocraft problems.
>
> ksjp
>
> \-\-\-\-\-\-\-\-\-- Forwarded message \-\-\-\-\-\-\-\-\-- From: **Kristofer PISTER** Date: Fri, Feb 16, 2018 at 9:34 AM Subject: Re: Microrobot simulation To: Daniel Contreras Cc: Brian Yang , Grant Wang , Roberto Calandra
>
> My summary of the meeting (Roberto, Dan - please add corrections):
>
> There are several different research directions in which to go from here. The most
>
> interesting one seems to be optimization of leg geometry. This would involve:
>
> \* changing the learning algorithms somewhat
>
> \* generating some interesting \"terrain\" for the robots to walk over
>
> \* using simulation to come up with a small number of new leg designs that optimize speed over terrain (and size?)
>
> \* fabricating those designs in silicon
>
> \* testing the silicon robots
>
> There are a couple of other \"learning plus v-rep simulation\" projects that are interesting:
>
> \* using inertial sensor data to optimize gait
>
> \* using low-res image sensing to do obstacle avoidance
>
> \* combining low-res image sensing and inertial data to get the robots to solve interesting problems
>
> \* using the same sensors, but on the ionocraft
>
> And finally, using learning to control the real ionocraft based on the inertial sensor data,
>
> and compare to the traditional controller that we\'re building in matlab.
>
> If possible, it would be great to find another few \"Brian/Grant quality\" undergrads.
>
> Do you guys have any brilliant and hardworking friends who are looking for research
>
> projects in machine learning for micro robots?
>
> ksjp

The details are a long story, but I prioritized this collaboration with all I had. I missed a conference deadline in the fall and failed a lot of experiments. If it started in spring of 2018 the [paper](https://arxiv.org/abs/1901.03737) wasn\'t done as my #1 priority until winter 2019 (and it was a little bit of a janky paper at that). My meetings with Roberto were super stressful as I wanted to make sure I didn\'t miss anything that a \"normal AI student should know\".

I did good work for Roberto. Even though I thought I was out of place at the time, my diligence and commitment was super valuable to do real research. Now that AI research is so popular, a lot of people want a check box of doing it rather than getting super into the details. I didn\'t give myself enough credit for this.

Where I did get lucky was Roberto asking if I wanted to join him for an internship at FAIR in 2019. This was earlier than I deserved it. This brought me out of an AI outsider track career and into an insider AI track career, even if I didn\'t realize it. Working at FAIR was wonderful and I learned how to properly experiment in AI and build some useful software.

Building this flywheel with continued research looked like constant teaching at Berkeley in order to pay my way through graduate school. This is not normal for the well funded AI labs. I spent a long time writing grants that didn\'t come through until after I graduated, where I brought in a year or two of funding for someone else in my advisor\'s group, you\'re welcome!

The FAIR internship and a lot of time interviewing got me a second internship at DeepMind. The actual internship experience was pretty bleak entirely due to COVID and my personal life at the time, but the technical experience and network were super valuable.

This all follows a clear trend that after the first break in a career the next ones come easier as long as you keep your foot on the gas.

Later in grad school I maintained a list of all the things that didn\'t go my way as a \"research reality check\" on my [mental health resources page](https://www.natolambert.com/guides/mental-health).

I finished my Ph.D. in AI with no accepted papers at NeurIPS, ICML, or ICLR, the three leading AI conferences.

This path coincides with my friend group in AI being what I describe as the island of misfit toys --- it\'s lots of people who used grit and creativity to build careers in AI rather than folks who were raised in the in-groups now running leading AI laboratories. Everyone ends up with their own group and they all have strengths and weaknesses.

Despite all this, I still had the final goal of landing an industry research job as the target of \"making it\" in AI. The only job offer I got that fit the bill of industry research was the role I took at HuggingFace, where Douwe Kiela recruited me to help build an \"open-source DeepMind.\"

Little did I know that those jobs were effectively going to go away a year or so after I graduated in early 2022. I was lucky to dodge jobs that *sounded* even better at companies that ended up changing (or laying off) even more roles.

## **Building momentum**

The best thing that I learned at HuggingFace was how to build momentum and mind-share. These are two very related topics, but they\'re subtly different and needed for different things. As an individual at HuggingFace I wanted momentum as a way to get to mind share. As an organization, HuggingFace has had a lot of mind share but not a lot of momentum recently. You use momentum to build mind-share, but once you have it, keeping gravity can be enough to maintain impact.

I joined HuggingFace in May of 2022 and didn\'t do anything of substantial impact until after ChatGPT in December of that year. I did a lot of small things. The expectation at HuggingFace was that you made an increment of technical progress every day. Some days these are major features and some days these are clean ups. Still, it is an excellent culture to practice. One of the quotes I remember from my grad school advisor is that \"you can change the world working 4 hours a day\" if you stack those bricks on top of each other. Most people don\'t keep stacking bricks in the same direction for a long time.

I bounced around projects based on what was starting and what was happening with the other RL interested folks. We attempted a [synthetic environments project for RL](https://github.com/huggingface/simulate) that needed a large engineering team we weren\'t going to hire, I made contributions to HuggingFace\'s [Diffusers](https://github.com/huggingface/diffusers) library, but they were largely on the fringes, and I did a bunch of research on responsible AI. Performance wise, all of these are all fine, but none of them are something to build a career on.

My work at HuggingFace before ChatGPT was really practicing good habits and learning how the open-source AI community worked, so that I could step up once I had a real alignment with a new project.

I wrote my first [major blog post for HuggingFace on RLHF](https://huggingface.co/blog/rlhf) in about a week and then it has stayed as one of the top search results for RLHF since (it\'s pretty outdated now, so it goes). Going into that week I\'d heard of RLHF but never once implemented it or read a paper on it in full. Like most of my writing now, that was for learning. I still very strongly identified as an \"RL person,\" so figured I might as well.

When writing this, I checked my Medium and Substack profiles and had written approximately 70 posts before this one. I started writing in February of 2019, so this was about 3 years of practice in. It was almost another 3 years since then that I became well-read.

A prevailing emotion I had when writing that post was how odd it was that there was no good blog on RLHF at the time. Looking back, this is the first time I see what is now one of my major skills --- doing things that are obviously needed in a simple and timely manner.

A lot of people overestimate others\' abilities to execute on simple ideas and give up on their complicated ideas (sunk cost fallacy). Even if something is obvious to do, surprisingly few people will do it. The first time I realized I was doing this *while doing the project* was with [RewardBench](https://arxiv.org/abs/2403.13787), the first evaluation tool for reward models in RLHF. In that case I spent every working day expecting to get scooped for about 3 months before the release. There wasn\'t even a competing project released until about 3 months *after* we released it, even though I felt it was late.

I\'m working on another project that feels like this, but unfortunately now my following is too big to broadcast it to the world. Stay tuned.

My time working on RLHF at HuggingFace was definitely effective. We made a lot of foundational contributions to the open community. We made [TRL](https://github.com/huggingface/trl) a more modern library, [fumbled through some human data contracts](https://rlhfbook.com/c/06-preference-data.html#sourcing-and-contracts), [replicated datasets](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences), built the [\"first\" leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard), and [trained some fun models](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta). This was very fun for months, but eventually the time zone difference (9 hours) and some other minor cultural differences made the work not fun for me. The other engineers were definitely out-contributing me on a small team and it was time for a change. Our team was too small --- if we had scaled up the technical team with the correct manager(s) we could\'ve multiplied our impact, but that has risk as well. Training AI models is just very hard and detail oriented while needing to implement a long list of small things, so there can be insane gains to growing a little bit.

At the same time, I found my niche in communicating open science, which is likely more important to my career than most of my technical contributions.

The strategy is quite simple. As AI laboratories are becoming closed off and more eyes are coming to AI, if I can keep doing relevant things my potential for growth in public is going to grow exponentially. It is and was much easier for me to differentiate in a less competitive area. The total attention is growing and collapsing onto fewer people, so if you can become one of them the upside will be huge.

If I joined a frontier lab I probably would\'ve been swamped out of career growth. Making the time to write every week, which I started doing around the same time, is some proof of this. I\'m continuing to capitalize on this strategy today.

When you have good branding the story falls into place more easily. The most impactful model from my time at HuggingFace, Zephyr Beta, was actually trained *after* I left, but on infrastructure I helped build. Then, I joined Ai2 and they were training Tülu 2 70B when I started. These models together had Chris Manning credit me for \"saving DPO\" even though I had little direct technical impact on them. This isn\'t to say I didn\'t have a role, but rather that many different roles can go into the arc of science.

## **Executing**

My time at Ai2 has been the easiest to contextualize period of my career. I want AI to go well and I think [more openness is the best way to do that](https://www.interconnects.ai/p/why-i-build-open-language-models). The best possible jobs are those that are synergistic. Ai2 gets a ton of obvious value out of my writing, so I get to keep practicing and building my impact. These are the best possible jobs to get (and also the rarest). Most of the time companies are not set up to help the individual.

What I do now at Ai2 is quite simple. It took a bit to settle in here, where I grew through some important academic projects like RewardBench to get more confidence underneath me that I can ideate and execute on high-impact research projects from start to end as the leading force. It\'s easy to do too many projects with other people and never make it obvious to yourself that you can do it alone (even if it\'s slower, lower quality, and less fun --- this isn\'t about undervaluing your team).

Now, my approach to projects is totally a reflection of the people around me. I work with many wonderful, driven, more junior colleagues. These people are going to be more in the weeds than me and be better at implementing new ideas, so a lot of my contributions are on steering direction and removing potential roadblocks before they show up.

The things I do are:

1.  Making OLMo-Instruct happen. I am the interface between OLMo pretraining and post-training projects and often am actively babysitting the OLMo Instruct training jobs myself with a small group.

2.  Making new post-training recipes happen. This is ultimately a lot of herding cats and inspiring urgency in the beginning, but eventually transitions to reducing entropy and killing unfruitful paths later on.

3.  Making AI more open. This is all things interconnects, policy, and Ai2 strategy.

These are not moonshot research ideas. These are projects that feed into the next model. There\'s a place for that sort of research, but everyone should think deeply about whether their research interests and institution best support that. If you\'re doing shorter-term research the best way to have impact is by folding it into a model. Make long-term research truly long-term.

I cannot do the third well without the first two. Sometimes I do a little bit of academic advising, but I\'m extremely protective of my time. I don\'t do virtual networking (I do some in person) and try to say no to most things. The output is the short term goal and the attention is a much more complicated long term dependency.

Through all of this, I\'ve come upon an analogy I\'ve seen play out across different phases of projects, careers, and companies.

All people trying to create a foothold in their career are going to go through some form of getting the flywheel started. This is often attributed to startups, which need to try many iterations of the product until they find product-market fit, but it is an underused analogy for careers. For getting the word out, for open-source software, for AI models, you first need to be releasing often. You need to keep striking the match and seeing what sticks. Your first few \"hits\" will still be small at this time, with incrementally more engagement. It takes many hits until the flywheel is really going.

Once the flywheel is going, shipping often in some ways can come with a cost. In our AI work, shipping models too often leaves us no time to properly master the next model. As your audience gets bigger you have to pay more in time maintaining anything that makes it public. In my time at HuggingFace and early at my time at Ai2, I advocated for always trying to release more models because we can in post-training (and we\'re one of a few groups with a solid amount of compute). Eventually this backfires and becomes too much of a tax.

When you have momentum and the space to execute, fewer bigger things are more useful. A career flywheel that's been pushed long enough can spin on its own for longer than people expect. Disruptions, changing jobs, low-quality work, etc. can actively slow down career growth. Doing nothing for me and letting more recommendations come in as \"one of the open leading scientists in AI\" is highly effective.

With that, I\'m spending a lot of time thinking about using the power bestowed on me. I want to help enable more big projects to happen by creating an environment for them and encouraging others, rather than leading from the front, but it\'s a new set of skills I need to learn. This is how I enact my vision for the future of AI.

<div>

------------------------------------------------------------------------

</div>

*Let me know what you think of this. The portion that this is missing, which is honestly something most writing will gloss over, is going deep on what it feels like to overcome adversity in the right way. We all always have more to learn about that.*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
In my testing, it\'s currently variable. Some models don\'t know me at all and some can summarize my contributions to AI, at least at a surface level. I suspect 2025 marks a big transition point for me here.
:::
::::
