---
title: "Interviewing OLMo 2 leads: Open secrets of training language models"
subtitle: "#12 What we have learned and are going to do next."
date: 2025-01-22
type: podcast
audience: everyone
visibility: public
post_id: 155126564.olmo-2-pod
email_sent_at: 2025-01-22T15:39:57.040Z
---
We\'re here to share the story of building our Open Language Models (OLMos) and what we improved to build the OLMo 2 7B/13B model that is competitive with the Llama 3.1 8B model. This is all about building an effective, small language modeling team that can share all it learns with the scientific community. Dirk, Luca, and Kyle are some of the people I learn the most from and have more knowledge (and entertainment) to share than we have time.

*Some questions were [pulled from Twitter](https://x.com/natolambert/status/1876309495472693741), but please comment or get in touch if you want us to cover anything in the future episode(s)!*

Main topics:

1.  Pretraining efficiency and our quest for stability after a not-so-secret failed 70B run early in 2024,

2.  What the role of OLMo is in the broader AI landscape and how that is, or is not, changing,

3.  Many little decisions that going into building language models and their teams (with a focus on NOT post-training, given I already talk about that a ton).

Play with the models we build here: [playground.allenai.org/](http://playground.allenai.org/)

For more history of open language models (OLMos) on Interconnects, see my [first post on OLMo](https://www.interconnects.ai/p/olmo?utm_source=publication-search), my coverage of [OLMoE](https://www.interconnects.ai/p/olmoe-and-building-better-llms?utm_source=publication-search), [OLMo 2](https://www.interconnects.ai/p/olmo-2-and-building-language-model-training?utm_source=publication-search), and [why I build open language models](https://www.interconnects.ai/p/why-i-build-open-language-models?utm_source=publication-search). If you have more questions or requests, please let us know (especially the researchers out there) and this can be one of N, rather than a one off celebration.

Listen on [Apple Podcasts](https://podcasts.apple.com/us/podcast/interconnects-audio/id1719552353), [Spotify](https://open.spotify.com/show/2UE6s7wZC4kiXYOnWRuxGv), [YouTube](https://www.youtube.com/@interconnects), and [where ever you get your podcasts](https://www.interconnects.ai/podcast). For other Interconnects interviews, [go here](https://www.interconnects.ai/t/interviews).

:::::::: {#youtube2-dS7QI99uJVc .youtube-wrap attrs="{\"videoId\":\"dS7QI99uJVc\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=dS7QI99uJVc){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

### Contacts

Dirk Groeneveld --- <https://x.com/mechanicaldirk> // <https://bsky.app/profile/mechanicaldirk.bsky.social>

Kyle Lo --- <https://x.com/kylelostat> // <https://bsky.app/profile/kylelo.bsky.social>

Luca Soldaini --- <https://twitter.com/soldni> // <https://bsky.app/profile/soldaini.net>

General OLMo contact --- <olmo@allenai.org>

### Papers / models / codebases discussed

-   [OLMo 2 paper](https://arxiv.org/abs/2501.00656)

-   [OLMo 1 paper](https://arxiv.org/abs/2402.00838)

-   [OPT](https://arxiv.org/abs/2205.01068) models and [talk](https://www.youtube.com/watch?v=p9IxoSkvZ-M) from Susan Zhang

-   [BLOOM](https://arxiv.org/abs/2211.05100)

-   [Red Pajama V1 Dataset](https://arxiv.org/abs/2411.12372)

-   [Falcon LLM](https://arxiv.org/abs/2311.16867)

-   [C4](https://arxiv.org/abs/2406.04594v1): *Boosting Large-scale Parallel Training Efficiency with C4: A Communication-Driven Approach*

-   [Maximal Update Parametrization](https://arxiv.org/abs/2203.03466) (muP) is from *Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer*

-   [Spike No More](https://arxiv.org/abs/2312.16903): Stabilizing the Pre-training of Large Language Models

-   [LLM360: Towards Fully Transparent Open-Source LLMs](https://arxiv.org/abs/2312.06550) --- [Amber model](https://huggingface.co/LLM360/Amber)

-   [EfficientNet](https://arxiv.org/abs/1905.11946)

-   [MegaBlocks](https://github.com/databricks/megablocks)

-   [A Pretrainer\'s Guide to Training Data](https://arxiv.org/abs/2305.13169): Measuring the Effects of Data Age, Domain Coverage, Quality, & Toxicity (Kyle said *Hitchhikers*)

-   [Fishing for Magikarp](https://arxiv.org/abs/2405.05417): Automatically Detecting Under-trained Tokens in Large Language Models

### Chapters

Chapters: Here is a list of major topics covered in the podcast, with timestamps for when the discussion starts:

-   \[00:00:00\] Introduction

-   \[00:02:45\] Early history of the OLMo project

-   \[00:15:27\] The journey to stability

-   \[00:25:00\] The evolving role of OLMo and pretraining research

-   \[00:29:00\] Pretraining Q&A (µP, scaling laws, MoE, etc.)

-   \[00:40:40\] How to think about pretraining data work

-   \[00:54:30\] Role of pre-training vs mid training vs post-training

-   \[01:02:19\] Release strategy and wrapping up

### Transcript

*This is generated by AI and lightly edited for clarity. Particularly, the attribution per-speaker was poor on this time around.*

**Nathan Lambert** \[00:00:07\]: Hey, welcome back to Interconnects. In this interview, we\'re bringing one that I\'ve hinted at for a while, which is interviewing some of the other leads on the OLMo team at AI2. So essentially, this covers the story of OLMo from its early days where we got our compute, kind of our path to stability and some failed runs along the way, the role of OLMo and the broader AI ecosystem, and really just a very long tale of technical details and decision making and considerations that you have when actually training language models that you\'re trying to have at the frontier of performance relative to peers like Llama, etc. This is a fun one. There\'s less post-training than normal because this is me interviewing some other co-leads at the Allen Institute for AI. So there\'s three people in addition to me, which is Dirk Groeneveld, who is the lead of training, handles most of engineering, Kyle Lo, and Luca Soldaini, who are the data leads. So we have a pre-training engineering lead and two data leads with me who has done a lot of the post-training. This is just a part of the team. And I hope you enjoy this one. We can do more of these and bear with the fact that I\'m still expanding my podcasting tech equipment. But I think the audio is definitely good enough and enjoy this episode with me, Kyle, Dirk, and Luca.

Hey, everyone. Welcome to the AI2 office. We\'re finally talking more about some of our OLMo things. Too much work to do to actually get all the\... the information we want to share out into the world. So I\'m here with Dirk, Kyle, and Luca. We can also talk so people identify your voices so people are not all on video. Hi, I\'m Dirk.

**Dirk Groeneveld** \[00:02:01\]: I am the lead of the pre-training part of OLMo.

**Kyle Lo**: Hi, I\'m Kyle. I work on data.

**Luca Soldaini** \[00:02:08\]: Hello, Luca. Also work on data with Kyle.

**Nathan Lambert** \[00:02:13\]: Okay, so we\'re kind of going to maybe go through some of the story of OLMo to start. And then just get into as many nerdy details until we get tired of OLMo 2. Which, in my state, this will probably be mostly about pre-training. You can ask me post-training questions as well. But I\'m not going to sit here and be like, ask myself questions that I\'m not going to answer. Because that is an absolutely ridiculous thing. You can ask me one question. Okay. One question. It\'s like, why shouldn\'t you post-training with all the compute?

**Nathan Lambert** \[00:02:45\]: But I wasn\'t here for when OLMo actually started. So I think it\'d be good to tell people, I mean, like, broadly what AI2 was like at the time, what language modeling was like at the time, what it may or may not have been risky.

**Kyle Lo** \[00:03:01\]: Yeah, you should probably get this.

**Dirk Groeneveld** \[00:03:03\]: Yeah, I think it all started in the fall of 2022.

**Dirk Groeneveld** \[00:03:10\]: We were talking to AMD at the time about some sort of collaboration. We\'re scoping out some stuff. And at the time, we wanted to take the Bloom model. And put 300 billion extra tokens in. And we wrote up a proposal and we sent it to AMD and it disappeared into a black hole. And we never heard from them again. And then ChatGPT came out a couple months after that. And suddenly everybody was very excited. And two, maybe one month after that, AMD came back to us and said, now let\'s do it. And that kicked off a very busy period for us. At least the three of us were involved at the time. Plus some of us. Some more people trying to scope out exactly what the project would be. Putting 300 billion tokens into Bloom wasn\'t that cool anymore. The field had moved on. So we needed to find something else that would work both for us and for AMD.

**Dirk Groeneveld** \[00:04:07\]: And that\'s exactly what we did. We figured it out. We figured out who would be on the team, how exactly to do it. We had to get the data from all of that stuff and then started working on it.

**Luca Soldaini** \[00:04:16\]: I think it was, let\'s look it up. And the official birthday of all of us. Almost is February 2nd, 2023. That\'s when we had like a big sort of half day. Summit workshop and a bunch of researchers self-organized a long discussion. I\'m foreseeing maybe like 40, 50 of us try to scope down a potential language model project at AI2.

**Kyle Lo** \[00:04:48\]: Yeah, it was also extremely bottom. Up because we were all like, nobody, it was not on anyone\'s radar. We were working on, everyone\'s working on different projects that we had promised for the end of the year. This was very much just like a side gig for us. We had no compute other than this mysterious AMD GPUs that just came. It was like, oh, it\'s possible. And everyone was just like, yeah, I\'ll work on this on the side. Let\'s just start hacking together some stuff.

**Nathan Lambert** \[00:05:14\]: How far along the line until you decided on 7B? Like, were these things obvious at the time?

**Luca Soldaini** \[00:05:20\]: I think the size of it. This is where Llama\'s size was. Yeah, we started with seven because seven was the smallest Llama size. This was Llama one. Yeah, Llama one was like first couple months of 2023. Yeah, we started, we started scoping before Llama one. And then when Llama one came out, it made sense to have a configuration that was just sort of close to what they were doing. So it\'s not too much reinventing. I think seven was.

**Dirk Groeneveld** \[00:05:52\]: Yeah, I mean, I think the original scope was recreate Llama one, which would be a 7B at 1.4 million tokens. What were we staring at? OPT.

**Kyle Lo** \[00:06:03\]: We were staring at OPT also, right? During around that time.

**Dirk Groeneveld** \[00:06:07\]: For inspiration. Yeah. And for what not to do in many cases. Was OPT even like in the many tokens regime or was that still like when people did the booms and booms?

**Luca Soldaini** \[00:06:18\]: I think OPT and booms were.

**Luca Soldaini** \[00:06:22\]: They were not, they were not over trained at the end were both a scope to Chinchilla that they both had extensive logs and so they were very useful because both of them have hundreds of pages of like, whatever can go wrong during pre-training. Yeah. I mean, OPT was amazing as a resource for figuring out, you know, we knew nothing, so we needed to know what\'s important. And yeah, I remember there\'s also avoidance and so on. There\'s that. It\'s like Susan has this talk.

**Dirk Groeneveld**: I\'ll come load parallels of training OPT and yeah, I think the original ones, I always feel it\'s kind of a shame because the OPT models are not very good, but, but they were first, like they figured all that stuff out for the first time. I have huge amounts of respect for that.

**Nathan Lambert** \[00:07:11\]: And what\'s the like open source angle thing at the time, or like, had you already identified that there was no open pre-trained data sets for these models?

**Kyle Lo** There definitely wasn\'t any open pre-trained data sets. I think we were basically looking at. The gopher paper that had most documentation and then Llama one had enough documentation about what data sources were using, where we were like, okay, let\'s try to reconstruct what it was. And I think roughly around the same time, Red Pajama V1 and then shortly after it was like Falcon, Falcon, the first Falcon, we were all kind of concurrent works at the time, but basically starting from, I don\'t know, Grab, Common Crawl, grab a bunch of sources to try our best.

**Luca Soldaini** \[00:07:50\]: The funny thing, like we had conversation of like. Like, uh, there was like, boy, it would be good if we didn\'t have to do the data. This would be one fewer thing to do, but at the time, like even when, uh, Falcon dropped, they released like a small preview that wouldn\'t match like the token budget that we wanted for a training run. So it was not even like, you know, it was good work and like, oh, maybe we just switched to this one. And then we quickly arise, not, not big enough for the two trillion. So I think it was like, maybe. Yeah. Yeah.

**Dirk Groeneveld** \[00:08:22\]: I mean, we did the C4 data set way before any of this. Um, and so my first idea for how to do data was to just run C4, but on all the Common Crawl, um, instead of just whatever the most recent one was at the time. And I actually started writing a repo for that, but then ended up not doing it. This is the C5 repo. Yeah.

**Nathan Lambert** This was C4\'s side of data cleaning practices.

**Dirk Groeneveld** Yes. That\'s exactly a re-implementation of C4. And, um, for it to touch it, we\'d run on slightly different hardware, um, with more dApps and that was, that was going to be the entire story until we found we could do better.

**Nathan Lambert** Yeah. And, um, for general timelining, I joined pretty much like almost 7B was, I think mostly done training or wrapping up pre-training and the like instruction tuning at the time was like basic SFT with a sprinkle of DPO. Yeah. So I think a lot of that story gets cut. Compressed. Like I\'m guessing the actual pre-training happened in like the second half of the year, mostly. So it\'s a lot of prep to get a language modeling system to exist. Yeah.

**Luca Soldaini** \[00:09:32\]: I think we handed off the one of Dolma. So the data set that we used for pre-training is like end of June, I think, 2023. Grab Common Crawl, end of March. Yeah. So all the source acquisition was March, April. Let\'s see March and then yeah, a few months. There.

**Nathan Lambert** \[00:09:52\]: Um, if someone wants to do the same thing today, which is like, we should train a language model, how much faster would it be to like, is OLMo actually making that much of like, would it be a week with OLMo stuff now, or would it still take a lot of time to set this up?

**Luca Soldaini** \[00:10:07\]: I think if, if you want to, um, if you want to train exactly on OLMo data, you know, data, it\'s much faster, um, training, I think it requires a little bit more finesse and dirt. Yeah.

**Dirk Groeneveld** \[00:10:23\]: If someone gives you a cluster to, to run on, just figuring out the mechanics of getting your thing to run, just so setting all the environment variables and having the drivers loaded and so on, it might take you a week or so if you\'re, if you\'ve done that kind of thing before. Um, so that\'s very different, but you can take a trainer that already works and just, just use it.

**Luca Soldaini** \[00:10:45\]: Um, it really depends like where, where you start. It\'s like, if, if you\'re spinning up your cluster from. Scratch, then you acquired a hardware, then that hardware has burning periods. So the first three months stuff will fail and that has nothing to do with the model itself. It\'s just, your hardware is also brand new.

**Dirk Groeneveld** \[00:11:06\]: Yeah. I mean, I am eternally grateful for AMD for giving us the compute to get started, but it was kind of difficult to run on.

**Nathan Lambert** What was the exact amount of compute? Like, I think when I arrived, that wasn\'t even what we\'re using where it\'s like Lumi discussions and the original amount.

**Dirk Groeneveld** Of compute was, uh, 2 million hours on Lumi.

**Nathan Lambert** So, so 2 million GPU hours.

**Dirk Groeneveld** \[00:11:29\]: Um, that\'s we\'re training way bigger now than that. Yeah. So I think I did the math recently. It\'s like the order of a million hours is if you do a thousand GPUs concurrently, like 20 days. Uh, I don\'t have that math in the top of my head, but, um, the first, the first end to end run for the 7B that we did took, uh, 35 days. We can now train that same. Model again in three days. So things have changed a lot since then. Yeah.

**Luca Soldaini** \[00:11:58\]: Well, some rough, rough stats for almost two anyways, seven and 13, just the final ones, um, was a little bit over 5 million GPU hours combined. And then we have roughly 5 million hours worth of experiments.

**Dirk Groeneveld** \[00:12:15\]: Um, these are, uh, A100, H100. Might be surprised. Oh, it\'s the case too high or too bad to do some, it\'s way too high.

**Luca Soldaini** \[00:12:33\]: Um, it\'s like, how do you encamber overhead then?

**Dirk Groeneveld** Oh, combined.

**Luca Soldaini** \[00:12:36\]: It\'s some of them plus the ultimate training. They\'re also not using the new one core quickly.

**Dirk Groeneveld** \[00:12:42\]: So, yeah, but I\'m just thinking if it\'s, let\'s say conservatively 7,000 tokens per second, four months on a thousand. Do you think it\'s less than that?

**Nathan Lambert** Like, okay, let\'s just go and track those number down. I think it\'s interesting. It\'s like, what percentage, what is the percentage of improvements still? Like how much of all the two being better is just by the compute being more stable just by doing more experiments. And that lets you test things like stability and just get the ducks in a row rather than like the data being so much better. It\'s an impossible question.

**Luca Soldaini** \[00:13:20\]: It\'s that it was like. And, you know, the trigger part with using that AMD hardware at the time, specifically that cluster, was that cluster was being brought up online at the same time as we were experimenting with it. So we were helping that cluster being set up. So it\'s because of that, there\'s a lot of things where we had to second guess ourselves, whether that was an issue on our side, the hardware side.

**Nathan Lambert** \[00:13:58\]: Isn\'t this always going to be an issue with new GPUs coming into the world? Does Microsoft plug in opening eyes GPUs and they just work?

**Luca Soldaini** \[00:14:06\]: I think it was, yeah, it\'s always tricky. It\'s a combination of like getting both new GPUs. At the time, AMD was a relatively new vendor, plus the cluster itself being new. So it\'s like stacking, you know, risky, risky things on top of each other in a way that it\'s like, oh, if you can, if your cluster is solid, that, you know, the GPUs are brand new. Well, the network is not going to cause issues, but if the cluster is new and the GPUs are new, who knows where the problem sits. Yeah.

**Nathan Lambert** \[00:14:44\]: We\'ll go down the\... Yeah. We\'ll go down the whole stability round the hole. Dirk, how close are you to a number?

**Dirk Groeneveld** Five trillion tokens at 7,000 tokens per second, which is what we get for the 7 billion, more or less, over the long run, is only about 200,000 hours on each one. So our first estimate was way off.

**Luca Soldaini** \[00:15:05\]: It was\... Check the top. I think maybe my memory was wrong. Maybe my thing was\... This is why I have this laptop here.

**Luca Soldaini** \[00:15:18\]: Oh, no, I was misremembering. Okay. My name is 500K. I remember flying\... 500K. Yeah, yeah, yeah.

**Nathan Lambert** \[00:15:27\]: So it\'s like from the first AMD grant of a few million GPU hours on AMD to what we have today. It\'s like it\'s gone from multiple million AMD hours to training a model over five times the tokens in half the GPU hours. That\'s right. Yeah. Like, where do we\...

**Dirk Groeneveld** I mean, the biggest one is that the MI250 that Lumi has on, like, the MI250 is the AMD GPU that Lumi has, is of the A100 era. It\'s comparable to an A100 in price and capacity. But now we train on H100s, and they\'re just\...

**Nathan Lambert** What percentage of tokens\... It\'s just a newer GPU. Yeah, what percentage of tokens in OLMo 1 code versus OLMo 2 code are lost at, like, a 7B, so a scale that we\'re reliable on? What percentage of tokens in OLMo 1 code versus OLMo 2 code are lost to spikes?

**Dirk Groeneveld** I think it was OLMo 1 losing a considerable amount against the spikes game. That\'s impossible to estimate, because there\'s so many other differences at the same time between OLMo 1 and OLMo 2.

**Nathan Lambert** Can you summarize the architecture differences? There\'s a list in the paper. We don\'t have to be exhaustive.

**Dirk Groeneveld** That\'s going to be a lot of stuff. The biggest difference is the init. So I guess now we\'re getting into what did we actually discover?

**Nathan Lambert** These are some audience questions. OLMo 1 and OLMo 2. Finbar, who you might know specifically, asked, like, how do you write an init N(0,0.02) to an init? I\'m like, I don\'t know.

**Dirk Groeneveld** That particular init is the default in Megatron. And the init that we had in all one was just trying to be too clever. We stole that init from OpenOLM, and they took it from somewhere else, actually. And I don\'t remember what the original source is.

**Nathan Lambert** What is the actual decision-making on an init that\'s too clever? You, like, think that you can get a better learning region by bundling with something?

**Dirk Groeneveld** We tried it. We ran it for, you know, 100 billion, 200 billion tokens, and we looked at which one is better. And scaled init is absolutely better for a long time. So scaled init is the original. It\'s the OLMo 1 init. Works better for a long time. You have to train for a really long time before you see it come apart. You have 2 trillion tokens for a 7Bmodel. And then things get a little bit dicey. So this is why, you know, this is why we used it for OLMo 1, because it looks quite good for a long time.

**Nathan Lambert** Which of our OLMo models did we figure out that the init was a change?

**Dirk Groeneveld** Because we did a few through the year. We tried that same init with a 7D model, and that did not work. That model stalled out around 1.3 trillion, 1.4 trillion, something like that,

**Dirk Groeneveld** \[00:18:12\]: which gets at the heart of the stability. So we started to think about the stability investigation. So I think that was one of the audience questions, right? And how do we even go about the stability investigation? starting from the point of we\'re training the 7DB and it\'s not working anymore, what did we do? The first step was to identify the issues that we see in the metrics and see them in a smaller model. And the two issues we saw were lots of spikes that we call them fast spikes. So the model recover. They recover quickly, but they just happen more and more the longer you keep training. And at some point, even the fast spikes kill you.

And the other thing was a growth in GradNorm. It seemed very much that the 7DB would always start blowing up once the GradNorm got to 0.4, regardless of what intervention we did, it would get a little bit further. And then as soon as we hit 0.4 GradNorm, it would blow up again.

**Nathan Lambert** So you lowered the learning rate and it was up again.

**Dirk Groeneveld** So fortunately, yeah. Yeah. So we would do things like that, increase the batch size, change the late decay, blah, blah, blah, but quickly it gets back to 0.4 and then blows up again. So fortunately, both of those phenomena also appear at the 7DB, even though the 7DB trains fine, it has both of those traits. So we decided to focus on those two because it\'s too expensive to try all these experiments at 7DB. But these are two things we could fix at 7DB and then see how it goes. So that was, that was the first step. But now. Now we have a metric where we can pretty quickly, within 12 hours or so, do a run, find out if our numbers are better and then change something and do it again. And the second component was we took another model that successfully trained that didn\'t show these issues, that didn\'t show the slow GradNorm growth and it didn\'t show the spikes either. And we ablated against that. So that was the LLM-360 Amber model. They\'re like all very open. So we could take their data. We could take their setup and look at it in great detail.

**Dirk Groeneveld** \[00:20:22\]: And we basically tried things one by one, sometimes two by two or so to not run too many operations. But we tried things until we got to a stable setup. There are some other insights at the time. I was really into the Spike No More paper, which is all about the magnitude of this. So we tried embeddings. So we tried some stuff there.

**Dirk Groeneveld** \[00:20:48\]: Pete Walsh on our team tried some other stuff involving Adam W settings that made things even better. And then we took a lot of inspiration from the Chameleon models because we were talking to that team on a semi-regular basis and they had a lot of stability issues. They found some solutions that we also tried and some of them worked for us and some of them didn\'t. And we took the ones that worked for us. So it\'s always ablating at the 70 scale until our numbers look super smooth and super nice.

**Nathan Lambert** How specific do you think these are to our setup? Are these all OLMo specific insights or is it just kind of a process you have to walk down? We\'ve heard some of these things before. It\'s like all these developments are you have to do the previous type of thing before you can go bigger, do a more complicated model. Do you think that\'s actually true or is there just best configurations at the time?

**Dirk Groeneveld** I really don\'t know the answer to that. It\'s hard. But something I want to know, something I want to do for OLMo three is walk back a few of these things and see in retrospect which ones are actually necessary. And in particular, I\'m hoping that some of those are not necessary and they\'re costing a bit of performance, you know, just to boost our own efficiency a little bit.

**Luca Soldaini** \[00:21:54\]: In general, I don\'t know, you can tell me if there\'s a useful summary, but it seems like the space of intervention you can take is so big. And other model, they\'re not going to translate perfectly, but the hit rate to like find a good solution is higher if you start from that model and you explore around it versus like try to explore like the full space of possible solutions. Yeah. And then some things will not pan out once you try to rerun them on your setup. And I don\'t think that\'s an indication of like necessary . Yeah. You know, we can mistakenly reimplement their thing, not in the way they\'re supposed to be. It\'s more like some things translate, some things don\'t. But it\'s a good starting point.

**Dirk Groeneveld** \[00:22:55\]: Yeah. I mean, we are a fairly conservative bunch with this, right? Because even the 7B runs are actually kind of expensive. So make small changes from a known baseline by and large. Yeah. I mean, everyone has.

**Nathan Lambert** Yeah. And risk is pretty obvious when you look at the cost numbers and like who you are trying to beat or not. And it\'s like we are trying to try to plot or people can build on it. And it\'s much better to keep making small progress than it is to go for glory runs and just hope that works. I think both works. The more compute you have, you can have a bigger distribution of investments, but it\'s not that surprising.

**Dirk Groeneveld** I mean, I hope that we can be a lab that is a little bit more risk tolerant than others. For one thing, we don\'t have Meta\'s resources. So we should be a little bit more aggressive. You know, it would make me much more nervous if I had to bet a billion dollars on our next run than the amounts that we can bet. So we can try a little bit more. I also feel and I hope that our management agrees with this. I feel that if we always, if we\'re always safe, if every one of our runs works. That means we\'re not trying hard enough, right? We have to occasionally crash and burn.

**Nathan Lambert** I think there\'s a few every year that you should crash and burn. I think these crash and burns at the big scale get a lot of attention from media and stuff. But it\'s like, what do you expect them to do? If they haven\'t, you\'re walking up a line and might as well try to take three steps at once every so often. Exactly. But I do agree. I think that\'s a cultural thing that we\'re trying to navigate. It\'s like, how do we do more interesting stuff and not just fall into the trap of being the best? Open model. No one else is doing this. Like, okay, you could do that for a while, but it\'s not as motivating.

**Dirk Groeneveld** And it\'s not just because it\'s more interesting to do that, but also just the fastest way to make a better model. The fastest way to calibrate your risk tolerance properly. You have to sometimes be over. Yeah. It\'s inevitable.

**Nathan Lambert** \[00:25:05\]: Any follow ups on risk?

**Kyle Lo** Yeah. I\'m thinking now it\'s like, because the 70B crash was so sad. Yeah. And I\'m wondering if you look back on it now, it\'s like, that was the greatest thing for us. We learned so much from that.

**Dirk Groeneveld** \[00:25:19\]: It was very important to love too. I do a little bit. So, I mean, we felt terrible, right? Like this was an awful time for us. I was like, I\'m done. Let\'s get good questions. No, we were the training team that couldn\'t train at all. I felt so bad. But the work we did following up is some of the proudest I\'ve been about the stuff I\'ve done in my time at AI2. Yeah.

**Luca Soldaini** \[00:25:47\]: In general, my thing about the role of OLMo sort of keeps evolving, right? It was very natural to have OLMo as these models designed to help others do research and language models. That\'s how we initially, it was a big part of OLMo 1. You just release all the components because it\'s important to have these tools available to everyone. To study language models. And I think we serve that community well. One thing that it\'s, I hope we can do with OLMo more is that there are like some interesting aspects of language models. Interesting capability, interesting architectural decisions that for a myriad of reasons, they sort of get overlooked in like say a company or like in a framework where, you know, you have certain constraints in your model. But it\'s still there. They are important. And there are questions around like what a model should be able to do, how it should operate, and things like that. But I think we can take a role where like we have in general this recipe that both enables research and language model and for like subset of model capabilities that we think are fundamental. No one is touching. It\'s our space to do work there. I think the prime example that I keep repeating these days is what we did with MOLMo and

**Luca Soldaini** \[00:27:25\]: vision team was mostly working on it. And MOLMo is very good vision language model in general. It benchmarks up there. It\'s not the best, but it benchmarks up there with open models. And then it has this like this interesting point. Pointing capability that no other vision language model has. And that pointing capability is, turns out, is fundamental for a lot of language models and robotics that you want to build. It\'s a core capability the same way that a text model should have long context. And it was cool to make, to sort of emphasize that of like, oh, we have the specific capabilities that would enable all these applications. And so more people should work on like the specific aspects. So I think that\'s a cool way to like work on things that folks haven\'t had a chance to touch on yet.

**Nathan Lambert** \[00:28:24\]: I think it\'s like trying to parse out why this type of situation could happen is not easy. Because you generally, everybody would want to do this. Like everybody wants to come up with a new capability that expands the scope of what X type of AI model can do. And I think it\'s most of like probably goes down to the culture of where people have space. To think about stuff in a more interesting way. It\'s like, because obviously everyone wants to have breakthroughs and open AI and Anthropic that copy. But it\'s like sitting at a boundary between doing just the same stuff and doing more researchy stuff that you need to have. I have more architecture questions. One is MUP. Multiple people are asking about it. I still don\'t really intuitively know what it is. But are we going to use this?

**Dirk Groeneveld** We have done a fair bit of work into it. And it hasn\'t worked for us yet.

**Nathan Lambert** Can you explain what it is?

**Dirk Groeneveld** MUP is mainly a way of setting the learning rate, but also some other hyperparameters. By training only small models and then having a guarantee or at least a pretty good idea that it will work also for larger models.

**Dirk Groeneveld** \[00:29:33\]: We have implemented this. We\'ve experimented with it. So far in our setup, it works across model sizes. So the learning rate that it predicts you should use, it doesn\'t predict the learning. It just gives you one learning rate. Basically, the good learning rate for the small model is also the good learning rate for the big model. That works if we change the size of the model. It does not so far work if we change the length of the training run. And that\'s why we haven\'t been using it so far.

Like number of tokens.

Yeah. Or longer. If we double the length of the training run or we 10x the length of the training run, the optimal learning rate is different in our setup.

**Dirk Groeneveld** \[00:30:21\]: It seems like this might be a bug. It should work, but it doesn\'t.

**Nathan Lambert** And the positive gain is just that better scaling because you don\'t have to fiddle with the certain. You know you\'re getting the right learning rate, which is a crucial hyperparameter.

**Dirk Groeneveld** Yeah. It\'s just a better way of setting learning rate. And it works for a few other hyperparameters too.

**Nathan Lambert** But there are other open models that use this. Explicitly. Pretty sure. I mean, open weights model. Yeah. Those are linking. Like Llama and stuff using this. Llama does not, I think. But I don\'t know for sure. We\'ll always see with the next iteration. Even Llama3 felt like they were still building their org and their infrastructure so fast. It\'s just like get in what you can get in and there will be more models in the future.

**Dirk Groeneveld** Yeah. I mean, MUP is a shortcut, right? Like you can for many settings where MUP wouldn\'t work. Or you have to just establish scaling laws and predict what it will be. You could do the same thing for the learning rate. Just MUP lets you do this with even fewer runs. You know, you don\'t even have to extrapolate anything anymore. You just use MUP and your setting will work. That\'s the idea.

**Dirk Groeneveld** \[00:31:29\]: But you kind of already need a scaling law set up anyways for things that MUP doesn\'t work for. You know, like architecture changes and so on. Yeah. So in that sense, it\'s not that important. It\'s still pretty important. And we\'re going to keep trying to make it work for us. Maybe just find the bug. But it\'s not absolutely critical.

**Nathan Lambert** How does scaling laws actually tell you the way to change like the width? Do they actually tell you the change in width or the depth, like the proportions of the network relative to the size? Like what are the actual output variables? Or how are you controlling the architecture you\'re going to use in the scaling laws? Well, like I know what it\'s trying to predict, the accuracy, but are they on set architecture things?

**Dirk Groeneveld** You would usually vary one thing.

**Dirk Groeneveld** \[00:32:17\]: Like you don\'t vary anything. You establish how it scales with size. Yeah. And you set your size according to a certain formula. Like you might say, I will go 1.4x the depth and 1.4x the width. So I have roughly 2000 pixels. That\'s a bigger model. And you do that a few times and you draw it on a graph. Then you change your architecture. You do it again. You draw a different graph. You lay them over each other and you hope that the lines don\'t cross. And one of them is clearly better than the other.

**Nathan Lambert** Yeah. I definitely have known that there\'s some, it\'s like one of the obvious things architecture design and the not obvious things. It\'s like you obviously make the model bigger, but the subtlety of like how tall versus wide. I think we\'re talking about like a client that\'s like much deeper than ours, our model architectures. And it\'s just like, I\'m around these things and I don\'t have an intuition for if tall or wide is better. And I think it\'s like what works.

**Dirk Groeneveld** There are some early results from Google, I think. I think they\'re called efficient net or something. That suggests that over a wide range, it doesn\'t matter whether you go wide or deep. It\'s not that surprising. That\'s pretty old results now. We\'re following up on a particular result right now. Actually, so OLMo 2 is a 7 and a 13, right? But there also was a 1 that didn\'t work very well. And we\'re trying to find out why. And one thing about that model was it was pretty wide and not very deep. So we\'re checking whether that is the reason why it wasn\'t very good. So we\'re sort of in the middle of double checking this assumption that it doesn\'t really matter whether you go wide or deep.

**Nathan Lambert** Yeah, that makes sense. I think that is something that doesn\'t matter to most people. They\'re probably very interested in it. Just like how they have these blocks and how do they decide. And it\'s like just one of us decides.

**Dirk Groeneveld** And it\'s like, eh, seems right. There are other concerns, right? So we train with FSDP, with 0.3 sharding. So we can try to choose these sizes such that they utilize the GPU in the optimal way.

**Dirk Groeneveld** \[00:34:29\]: Which has nothing to do with the sort of abstract training dynamics. It\'s just the practicality of getting this thing into 80 gigabytes of memory. So then those concerns might take over. There\'s other stuff like all your tensors, all your tensor dimensions need to be multiple of 64, 128, things like that. GPU math stuff. Yeah, exactly.

**Luca Soldaini** \[00:34:53\]: It\'s really hard to argue against things that are practically making you run fast. Because it means that if I find something that is 20% faster, your big run trees fast. All the experimental cycles are 20% faster. So it\'s not very glamorous. But everyone is really happy when we find one of these. Like, oh, this is a shortcut.

**Dirk Groeneveld** \[00:35:16\]: I find it super glamorous. I mean, when did you ever have such a clear sign of impact that you can say, I wrote this thing and it is not 20% faster? No, the impact is very good. Yes.

**Nathan Lambert** The numbers you\'re changing are not necessarily glamorous. It\'s just detailed stuff.

**Kyle Lo** \[00:35:34\]: I also think the experimental cycle thing is probably the biggest thing for me. What we\'re seeing consistently is the more experiments you run for a particular idea, the more likely it is to just work out. It\'s just a function of trying more things.

**Nathan Lambert** \[00:35:47\]: It seems like in the pre-training, there\'s very few, like, you just get the idea. I mean, well, I said post-training more. But literally, like, we had a meeting with John Schulman. He was like, everyone, lead labs, train RL and athletes do this. And we got, like, a three-month head start on one step. But pre-training, all that stuff. I think it\'s evaporated.

**Kyle Lo** \[00:36:05\]: The human intuition piece is just gone. I think once you do v0, you can kind of do everything with intuition. It\'s like, oh, look at data. This kind of makes sense. This seems like . And then after you get to, like, v2 of something, it starts becoming really hard to make sense of what is good for a language model or not. So you kind of just need to just try a bunch of stuff.

**Dirk Groeneveld** \[00:36:29\]: And then there comes a game of stacking improvements that are worth 2% to 5% each.

**Nathan Lambert** I think it\'s very compounding, at least in all the math, works out over a year. I think I want to ask about MOEs as well, if you have a different thing you want to say. But it\'s mostly, like, it seems like we have a OLMOE, which, if you look at the plots on paper, it\'s like this MOE architecture beats all of our own things and carry efficiency. But it seems like we had a path we needed to go down to make sure dense works really well and get all these improvements. And then you have to, like, feed back in. And you, like, merge the MOE streams. We have DeepSeek. We have Minimax. There\'s countless other MOEs that get really high eval scores. Like, they\'re not as easy to do research with because they have tons of total parameters. And people need bigger clusters to fine-tune them, blah, blah, blah. But it\'s like, is MOE something that you think we just need to do to make better models?

**Dirk Groeneveld** Well, it\'s a complicated question, and we haven\'t quite answered it yet for ourselves.

**Dirk Groeneveld** \[00:37:34\]: We did investigate doing a bigger MOE. And we found that the engineering is somewhat difficult. And at the time, we came to the conclusion that we could do that engineering, but then who\'s going to run that thing later? They also have to have a team of engineers on top of it to make sure they can train this.

**Nathan Lambert** What does the engineering look like? It\'s not, like, CUDA-level kernels. It\'s how you distribute parameters?

**Dirk Groeneveld** It\'s a little bit like\... It\'s a little bit CUDA-level kernels in that\... If Mega Blocks by itself isn\'t enough for you, then it gets really complicated. And we ran into that situation where if it had to be significantly bigger than what we did, it just got too complicated.

**Luca Soldaini** \[00:38:22\]: There is an inference. These very big models that really get advantages by\... If you tailor them to, like, where you\'re going to do inference with them. So if you\'re a big company, you start thinking about, like, how to batch request, how to, like, serve the model. But if we could do it ourselves for the place where we\'re running, but then you start thinking, like, oh, folks who want to use their model in their hardware, they\'re better served by advanced model than also redoing this engineering on top. Like, there is, I think, a clear advantage if you are\... Also providing an API to an MOE. Yeah. Very clear cut.

**Dirk Groeneveld** \[00:39:10\]: It depends on how we think of the product of ALMO. And the number one is still it\'s an item to be researched. So other people need to be able to train on it and to modify it and so on. And that is just much easier if you have a dense model. Yeah. If you think of it as something that gets put into a product. And people will run tons of issues. But if you have a lot of inference on and you only really care about the final score that it gets, then maybe the MOE starts making a lot more sense again.

**Nathan Lambert** Yeah. That\'s a good answer. I think it\'s, like, I think people can fill in the blanks of, like, what we may or may not do.

**Luca Soldaini** \[00:39:53\]: And I mean\... I mean, like, different, like, I\'m curious, like, what, like, folks at Llama, the Llama team think about MOE.

**Nathan Lambert** \[00:40:03\]: If the Meta AI exists, they\'re 100% going to do an MOE.

**Luca Soldaini** \[00:40:06\]: I mean, it\'s interesting, right? It\'s, like, if they\'re serving few, if they\'re expecting that the Llama users are going to be, in fact, one of the better smalls are few large companies that can figure out inference, then MOE makes sense. But if they\'re thinking about more, like, this model that wants to, it\'s great if it\'s adopted by a million developers, large and small, then, you know, they\'re still going to reach a lot of dense model. Yeah. Exactly. That development is so easy, so much easier for people to set up their own inference with a dense model.

**Nathan Lambert** \[00:40:40\]: Yeah. I think we\'ve gone surprisingly long without asking about data. It\'s, like, how much more, is it just an infinite hill to climb on data? It\'s finding good data and filtering bad?

**Kyle Lo** \[00:40:53\]: I mean, I think it\'s an infinite hill to the extent to which everything else is also, and you can kind of keep improving, right? But yeah, it\'s the main threads constantly are. Got to get more data, because if you\'re working with larger pools of data that you can\'t actually get easily new data that\'s not in your distribution, it\'s probably interesting to study how that adds in. And you have more to work from. So if you have, like, a strict quality filter, you can still get your high token yield if you start with a much larger pool and filter down. So getting more data is really, really critical, especially if you can target specific pockets that you think is missing. You can always keep iterating on better filters. Understanding how those filters affect performance. And everything kind of interacts with each other. Like, safety filters interact with quality filters, interact with deduplication, interact, like, all these together. So there\'s an infinite, even ordering, search space between these operations. So keep throwing more things at it.

**Luca Soldaini** \[00:41:53\]: Yeah, it\'s very much just stacking small improvements. Yeah, shots on goal. I think the way it looks is, like, it\'s\... For each\... Now that we have, like, these multiple stages of pre-training, we think about, like, what kind of improvement you want to get from data at all the various stages. Like, clearly, the improvement you want to get from data you put at the end of training is different than the improvement that you want to see at the beginning. It comes with a different set of requirements. One thing that is really useful is\... Intuitions are always often wrong. But one thing that it\'s worth spending time on is figure out\... If you have a data ablation idea, what is the fastest way to disprove it, which requires a little bit of experimental design. And then, yeah, you\'ve got to fiddle with, like, especially, you know, when you do the first version so that you can take a very\... It\'s very easy to measure improvements. And then as you start thinking, like, refined version, then, you know, you\'ve got to think of, like, how you measure your improvements or so. But, yeah, it\'s\... There\'s no, like, big\... After you\'re done, you know, the basic stuff, your V1 is done. There\'s never, like, a big, like, thread of, like, this is the one data thing. It\'s more, like, stacking your Lego bricks to get to a better model.

**Nathan Lambert** \[00:43:18\]: Do you think you can iterate faster on, like, end of pre-training, whatever you want to call it, like, highest quality bit training and the only data? Yeah. Have you, like, started that recently?

**Luca Soldaini** \[00:43:28\]: I think it depends on the\... What we\'re getting, you know\... We\... We need a little bit more evidence of this, but it depends on the role of data. Like, it\'s very much\... The reason why we started doing mid-training at all is because we were interested in having base models be primed with certain capabilities that we didn\'t get during the long pre-training phase. And for those, it\'s really easy to iterate on new data sources that would improve on those capabilities at the end, pre-trained. But during, like, the pre-training phase, why not the important aspect that we think about is, like, efficiency of your data is, you know, if there is a version of your data that is where train on it and the model gets to performance X on 20% faster, it means that you can train 20% longer, right? Or run more experiments. Or run more experiments. And so\... But for those, it\'s, like, you know, it\'s\... In some cases, you can use mid-training as, like, a proxy for this. In other cases, it doesn\'t quite make sense, so you have to come up with, like, maybe experiments through scaling laws, maybe experiments through some other technique. But yeah, it really depends on, like, what role a data set plays into, like, the various stages of pre-training.

**Nathan Lambert** \[00:44:53\]: So it seems like, like, compared to Dolma 1, which is, like, do the thing, it\'s all targeted abilities. It\'s, like, we want to be better at things. We put people on this. It\'s, like, targeted abilities or where we think we can get a lot of data.

**Kyle Lo** \[00:45:05\]: Like, a certain data source that hasn\'t been mined for stuff. Yeah. Yeah. We have to be opportunistic because it\'s so hard to get data. And for us, especially if we want to be open with the data, it\'s, like, we have to also do it by due diligence. Like, we\'re going to study this data, put all this effort in, and we\'re still going to be able to share it with everyone. So\...

**Nathan Lambert** \[00:45:22\]: If you were in a lab that didn\'t release data, do you think you could make more progress on it? Like, how, like, how much is that actually?

**Kyle Lo** \[00:45:27\]: Oh, yeah. Oh, my God. Such a time sink.

**Luca Soldaini** \[00:45:31\]: I mean, it\'s, like, it\'s a little bit of a mistake that we put in. Yeah. Like, and this is not even, like, doing, you know, getting data that managed to not legal, right? You could form partnership. You know, you have people knocking at our door all the time saying that you want to buy this data set. And they\'re, like,

**Nathan Lambert** \[00:45:48\]: I\'ve been contacted by one ML owner to try to facilitate a data deal.

**Luca Soldaini** \[00:45:52\]: Oh, yeah. Twitter. Oh, my God. But only the first, the first follow-up is, like, are you cool if we release the data? Of course, they\'re not. Yeah. So, it\'s, like, it\'s, it\'s, even, like, there\'s plenty of data that you could acquire from people, but then you can\'t release it. So, that\'s, that\'s a complication to, to progress.

**Nathan Lambert** \[00:46:15\]: Yeah. This is more of a self-question, but, like, how much do you think mid-training should be, like, a philosophical shift in how we organize teams? Because it\'s very easy to do. I mean, we\'ve already consolidated, like, our training and data to base, which is not surprising. But this is mostly hypothesizing on what other people do. It\'s, like, how close do you think this kind of end of pre-training to post-training handoff should actually be?

**Kyle Lo** \[00:46:40\]: I think it\'s, it makes sense as a thing if, I think these things are, in theory, arbitrary, but you can think of, like, in the extreme, if you had a perfectly oiled machine, you have a very smooth transition between pre-training to mid-training to post-training, and it\'s actually, there\'s no boundaries. Like, that\'s, like, a theoretical. You can probably squeeze a ton of performance by smoothing that out. But in real world, stuff, stuff is messy. So the real world is your three trillion tokens into your base model run, and then you signed a new data deal. You got to do something with this, and you\'re going to undo your training one. Well, you got to figure out something. So maybe that\'s mid-training, right? Mid-training is when you have an opportunistic need for something, or you\'re training something and someone catches a bug, which happens all the time, like a data bug or some training bug, and you\'re like, oh, I had to patch it. So then there\'s the shift fundamentally. You got to know how to deal with this. So just because these things aren\'t, these large training runs aren\'t super repeatable, and they take so much time that the world state changes all the time, you always need some strategy on how to deal with, oh, I\'m near the end of pre-training versus I\'m near the beginning of pre-training versus\... Yeah.

**Nathan Lambert** \[00:47:47\]: It\'s like, we\'re obviously trying to solve long context, so this fits right into this. It\'s like, we\'re going to do this thing. Does it go, where does it go? Some people do it in post-training. Yeah. There\'s some component during pre-training.

**Kyle Lo** \[00:48:00\]: It\'s kind of just like, you have to follow a few recipes and figure out what works for your team. Yeah. And so much of it is just, if it\'s expensive, try to push it off as much as possible. Because if it\'s risky, push it off as much as possible. If you can intervene to get the same result much later, huge win. You can try a bunch more things. If you have to intervene because it\'s some core thing that has to be baked into pre-training time, you\'re kind of\... It\'s a sad space to be in. But then that\'s the thing where you have to intervene. That\'s the pre-training data.

**Dirk Groeneveld** \[00:48:29\]: There\'s a big question that I\'d love to get an answer to, but I don\'t even really know how to think about it. But the question is, what makes a pre-training model a good candidate for mid-training fine-tuning? Because all we really try to do is we try to maximize our metrics, but we don\'t really know that those metrics are what makes a good step zero for post-training.

**Nathan Lambert** I think a relevant thing, I don\'t even know if I\'ve told you this, but I don\'t know how to take action on this, is we got advice that we have the multiple stages of post-training. In this instruction tune phase, we got advice that\'s like, eh, it could be a little broken. You can have some crap in there. It\'ll get fixed later on. And it\'s like, why is that okay?

**Nathan Lambert** \[00:49:14\]: It might be the same thing in pre-training. It\'s like, you want to get in the right\... It\'s more important to get in the right ballpark than the right exact number. Yeah.

**Luca Soldaini** \[00:49:21\]: It feels like it\'s more about not how to make a good model for post-training. But what to avoid so you don\'t have a bad model post-training. Yeah.

**Nathan Lambert** \[00:49:33\]: There\'s a whole other question, which is how to make a base model that\'s easy to fine-tune in general, versus one that, if with the right finagling, can get the absolute best numbers. Which I think, for OLMo, would be really great to be like, here\'s a super stable platform. A lot of people have complained about specifically That Llama Instruct, it\'s hard to fine-tune. Which, after most of the post-training. Because this is where people at companies start. They\'re like, this is the best open-weight model. I want to add a little thing in it. And a lot of people have difficulty in fine-tuning it. It\'s different at the base, because most people can\'t do this full instruct thing. But for researchers, having a stable platform at base is way more valuable.

**Kyle Lo** \[00:50:12\]: There\'s an interesting\... About this, like, what makes a base model a good base model. There\'s this interesting, I guess, debate that we\'ve had a bunch of times. We\'ve also had with other people. Which is, it seems like there\'s like two hypotheses on what the role of this\... How do you think about data as an effects-based model behavior? There\'s one hypothesis, which is, you need quality data so that you don\'t get any spikes. You have stable training. You have no bugs. And once you pass that level of quality, as diverse as possible. It\'s just about an init to the model, so that it can go in literally any direction. And so, diversity is the next. That\'s one hypothesis. The other one is, it\'s all domain effects. The only reason why\... Like, you can just keep climbing. There\'s a notion of quality. But you\... And you can keep getting more and more and more as long as you\'re very clear about what target domain or target application you are. You just keep getting closer and closer. Well, there\'s a lot of suite learning. Yeah. Well, this goes into, like, the continue pushing. I just like\... It\'s just domain effects all the way down. If you\'re only evaluating on this particular stuff, you can always get your base model to be better for that. Just keep climbing on it to get it more and more similar. As opposed\... And, like, think about, like, I care about this application, this suite of applications, all the way through. From base model\... Can you not kind of have both? I feel like I\'m confused with how, like, actual generalization fits into this. It\'s\... It\'s\... It\'s\... It\'s competing ideologies in terms of, like, if you believe in the first one, then you\'re all in on diverse data acquisitions. And how you set up your team. Yep. You\'re all in on efficiency and stability for your pre-training. And then you just get as much different data as possible. And you\'re post-training all the time. If you believe in the latter one, you solve backwards from, this is what I want the model to do. And I make all the changes everywhere to try to squeeze performance out of this class of problem. In the big\... In the data, in the bit-training data, bit-training data, et cetera.

**Nathan Lambert** \[00:52:01\]: How important do you think the actual, like, multi-tag category of every data document is? Like, know that someone\... Like, that these people have really advanced tagging of all their pre-training documents. Like, do you\... Like, does it essentially say, like, doing that and choosing them? Which is, like, a very much, like, crafting a, like, recipe for your pre-training versus, like, just good numbers. So, like, just get a good classifier and roll with it.

**Kyle Lo** \[00:52:27\]: We have tags. That\'s fine.

**Luca Soldaini** \[00:52:31\]: The tags are useful even if you get this idea of, like, let\'s use as much as possible. You know, diversity is important. A lot of web data comes with absolutely no useful metadata. You have, like, URLs. URL is very, like, you have to do things on top of it to make your URL useful. It doesn\'t add much. So, the more you have in terms of, like, categories, metadata information, you can start using this as a tool to try extra technique on it. Maybe it is extra technique to mix your data in a certain way. Maybe it\'s filtering out things. Maybe it\'s, like, designing benchmarks. Try to correlate with those. Yeah. Otherwise, it just seems to have this giant bucket with maybe, like, one quality knob. And it\'s, like, it\'s very hard to make progress if all you can adjust is, like, one number we cut for quality here. So, it\'s, I\'m not surprised that, you know, the big labs, they almost have these tags. I want to know how they use them. That\'s, like, the part that\'s not good. That\'s the part that\'s not good. Yeah.

**Kyle Lo** \[00:53:51\]: But it\'s also not just you have more levers to pull and then, you know, the more things you can try, the better. It\'s also you want tags that are actionable, right? So, like, if you had a sensible notion of a tag and you realize, oh, more of this data as you keep adding more of this lever, performance keeps going up. At some point, you might be, like, we\'re out of that data. We need to go get more of that. Without that tag, you want that tag to be something that\'s understandable so you can go and negotiate another deal, do synthetic generation, et cetera, of that type of data.

**Nathan Lambert** \[00:54:13\]: Do you think most of the synthetic data gen, is for very specific things at pre-training? I mean, it kind of has to be. Probably, yeah.

**Kyle Lo** \[00:54:25\]: You can\'t just be, like, oh, it\'s generative data. Like, that\'s not something, I don\'t know what that procedure is.

**Luca Soldaini** \[00:54:30\]: It\'s probably to prime the model to whatever you need during post-training. Like, you know, we\'ve seen, like, normally with math, it\'s much better if your model has an elementary knowledge of math to, like, improve on that. It\'s quite the same with everything that it\'s, like, oh, I want to do RL on this. If the model is completely random on it, you\'re going to have a very hard time.

**Nathan Lambert** \[00:54:52\]: Yeah, it\'s, like, I guess a good transition. It\'s, like, what do you three think post-training is, should be, or, like, is not doing?

**Kyle Lo** \[00:55:02\]: It\'s elicitation.

**Nathan Lambert** I\'m coming around to this view that it seems that you can extract abilities from the model.

I think it\'s totally elicitation. Like, the Hitchhiker\'s Guide to Data paper from Google, yeah, that one was very, that one had, like, a very specific experiment. But it seemed like that was pretty strong evidence towards it. It\'s, like, you filter out all of this type of data, you literally can\'t fine-tune that model. You can never recover that. There was a history detection, right?

**Nathan Lambert** \[00:55:28\]: I think if you do more flops, you potentially can. I mean, it\'s obvious, like, we\'re not talking about, like, O1 stuff things here. But, like, there are even datasets that have, like, 15 million math-only instructions. Are they going to be able to really start doing a ton of math? At some point, yes. Yeah. But I think that most of it, or it\'s almost easier to operate. I mean, it\'s just like, assume that capabilities are in this model and are post-training to get it out.

**Luca Soldaini** \[00:55:53\]: Sometimes there\'s this very large set of, like, things that you do in pre-training because you have a sense of, like, how they play an application. I think one day it\'s, like, very obvious. It\'s like, code model, you want to do, you want them to do completion, you\'re going to add, fill in the middle of loss, maybe at the beginning of pre-training. It\'s like, oh, then I can play my entire pipeline around like that. So it\'s all about\... So far, it seems all about that. I don\'t think we have cracked a good recipe to do the same for things that are not capabilities, but they\'re, like, recalling facts. Oh, yeah. Or, like, long-term knowledge.

**Nathan Lambert** \[00:56:29\]: Yeah. It\'s, like, all of us, like, all know, or, like, I don\'t know, at least people out there have MLMU numbers that go up in X stage. Like, instruction tuning, boosting MLMU, I\'m like, what are you putting in there?

**Dirk Groeneveld** \[00:56:42\]: What do you think of mid-training then? Is that a manifestation or\... Mid-training? I think it\'s still\...

**Kyle Lo** \[00:56:47\]: I think it\'s still positive knowledge. I think mid-training is, it\'s just, it\'s still pre-training, but with strong domain effects. It\'s just smoothing out the boundary between, you have a very, very sharp distribution shift when you do post-training, and we know from, like, kind of ML101 from the past five, six years, that smooth, smoothing out, helping, like, transition between major domain shifts helps. But we don\'t have a clear example of where, like, it helps with specific knowledge acquisition. Yes. For them, we don\'t know how to do it. But for, like, you that are really easy to evaluate, things that are really big progress on, it\'s like, yeah, smooth this out.

**Nathan Lambert** \[00:57:30\]: So, like, why is post-training important to the release site? Some of you guys came around to, like, post-training being important for getting traction later on. Is that just, like, an ML ecosystem, how it works?

**Dirk Groeneveld** Oh, I mean, the base model is kind of useless, right? Yeah. There\'s only so many next tokens you need to know about. Yeah.

**Luca Soldaini** \[00:57:50\]: But it\'s like, you know, we\'ve seen papers that use all the research, for example, where the idea for that research only came by comparing base model with, you know, instruction team model, like, the one where folks, they were involved around, like, certain pattern of speech and OLMo 1. Where do they come from? Do they come from pre-training? Do they come from post-training? And, like, even if you just want to do research, it\'s kind of useful to being able to compare side by side. So it feels wrong to put a model out that it, like, cuts sort of the problem that you can study in half until you have the post-training ready. And it\'s useful to have all in one package so you can use it right away.

**Kyle Lo** \[00:58:40\]: Post-training is just, like, a really, really long eval loop. Yeah. And that\'s a lot like, oh, base model, you know, a few shots, a few shots on some benchmarks, like, no, no, no. We eval it by post-training it and then eval it in post-training.

**Nathan Lambert** \[00:58:54\]: Yeah. I mean, to some extent, it is kind of true. I mean, that\'s how we should think about it.

**Dirk Groeneveld** \[00:58:59\]: If we could do that cheaply, we would totally hill climb on that metric.

**Kyle Lo** I think that\'s the metric. Because if base model is the good in it for the post-training, which is the model people actually want to use, then we evaluate it on its own. And on its status as a good in it.

**Nathan Lambert** \[00:59:16\]: Yeah. So it\'s like, how do we\... And then the question is, like, how important do you think research for post-training on the specific checkpoint is? It\'s like, how important is genealogy versus, like, general recipes? Because I think we\... I openly think we under-index on using one model. Because much like the path to stability, which is a eight to ten month really specific thing, I\'m guessing if you\'re really just, like, in a narrower regime, you can just keep kind of turning these little things. Yeah. Hopefully at some point we can do better with new models. Yeah.

**Nathan Lambert** \[00:59:52\]: Okay. We\'re kind of going to some wrap-up things. How do you think about release decisions? Like, should AI2 release everything that we ever tried? Or is it, like, when should we actually get models out the door?

**Dirk Groeneveld** I mean, I would love to do that, actually. Especially the failed runs. You know, like, where else could you get a repository of failed runs? Yeah. I mean, I think it\'s just a matter of giving other people the possibility of looking into these failed runs and finding out exactly when they failed. In practice, that\'s super difficult. Because just releasing something is hard. You know, you need to upload the checkpoints and translate them in a different format. And you have to describe what you were even trying in some way that makes sense to people outside of the org. Give them access to the weights and biases and to the logs. And it\'s just a lot of work. And there\'s always something else that seems more pressing than that.

**Nathan Lambert** Seems like a scaling. Like, how much we can share is capped by how we can scale our org. Which, like, we\'re not going to have a complicated management hierarchy or, like, an entire org that is just support. And everything you upload, you build as a support burden. It\'s like, literally, we just have seen the envelope grow, grow, grow. It\'s like, more people use our things, you get, like, boring support. Like, people want to use it. That\'s the cost of it.

**Dirk Groeneveld** I guess it\'s a great problem to have. People want to use it. People want to use us.

**Luca Soldaini** \[01:01:15\]: And it\'s funny. To make a checkpoint where, like, some are very useful, you need the person who was involved. You have to fill, right? You need the person who was involved in it to sort of pour their knowledge into a format that then, you know, people can consume outside, right? Otherwise, you know, we would just open up our S3 bucket, the checkpoint, and it would be, like, utterly useless. Because what if you wanted to know more of the parameters, so, like, as long as we optimize for release, then we have the bandwidth to provide, like, the support around that. If people want the 70B fail run enough, you know, I\'m sure we can release it.

**Nathan Lambert** \[01:01:57\]: It seems like it\'s just finding the right medium to release things. Like, I think long-time people reports are really good for the stuff that we do, because it just puts everything in one place for people, and it almost makes on-demand easier in the future. Whereas, like, we could just drip and drag models out all the time, but, like, that\'s not something we can\'t do. It\'s just, like, not\... In terms of making progress in things that are easy to build on, it\'s probably just not worth it.

**Kyle Lo** \[01:02:19\]: In fact, there\'s even a cost to it, right? The big example here is we had a release of OLMo 1 0724, or July 1. Yeah. I think research, using that for research, that has been probably one of the tougher models, because it didn\'t come with a blog post, it didn\'t come with, like, some docs. And so, yes, it still waits for checkpoints and everything, but comparatively, usually, even when people come to us, we\'re like, oh, we recommend you use 0424. And now with OLMo 2, we\'re like, oh, that\'s the one we recommend, because it has all the documentation. So just dropping something doesn\'t seem like it really helps.

**Nathan Lambert** \[01:02:56\]: I would say we should move faster than, like, the 1-2 iteration. But the in-between is not necessarily even worth it. Which is very odd, when you think about being fully open. It\'s just, like, kind of with the costs of doing business.

**Kyle Lo** \[01:03:10\]: It\'s like being fully\... You want to be fully open, but you don\'t want to add noise. And you don\'t want to waste people\'s time. Right? So if you drop something that\'s kind of half done or half baked, and people start spending time on it, only to get frustrated later, you\'ve cost them something.

**Nathan Lambert** \[01:03:22\]: How does this relate to, like, how pre-training is changing? Like, do you think we need to invest in\... Like, openly, a lot of startups are changing their relationship to training. And if they\'re going to use Llama or pre-training or customer data, and then we have X compute budget, and does any of this come into play? Or is, like, it\'s all the same with the talking? It\'s, like, continue to hill climb, do what you can, reasonable trade-offs, and who will actually use the models? It\'s, like, not too different.

**Luca Soldaini** \[01:03:54\]: I think that the\... So for me, the cutoff point is, like, is there something useful and generally interesting to add if you pre-train? The case of Llama, all this, like, mid-train things that we concluded, we done. It couldn\'t be as clean if we started with an already pre-trained model. So it\'s, like, is there really something useful to add to the conversation if you pre-train? If we get to the moment when the answer is no, or, for work, like I was saying. But it feels there\'s still value to add to the conversation. At least in the research side, like, pre-training, there is tonight a question of, like, we know how to help researchers. We want to help more than just researchers with the models we put out. And if we think there is this application that we can do a very good job, or just this use case, a very good job by starting with someone else\'s pre-trained model, we shouldn\'t waste compute on pre-training from scratch. Just saying. We can solve that. But it\'s an ever-evolving question, really. It\'s, like, I don\'t know. We can make decisions six months out, maybe? Maybe a year?

**Kyle Lo** \[01:05:24\]: Well, that\'s what I would say.

**Kyle Lo** \[01:05:27\]: I know. You\'re the pre-training. You\'re the hardcore who\'s pre-trained some models.

**Dirk Groeneveld** \[01:05:34\]: There\'s lots of runway left in pre-training. The big labs are fairly conservative because they have to be. But that doesn\'t mean that we\'re done. I mean, it\'s not that we\'re done. I also feel that the point of all is to make pre-training research accessible to more people, because even if you don\'t have the resources to pre-train the whole thing from scratch, you can still use our checkpoints and use our code to prove out some sort of improvement. And as we\'ve seen in other areas, even Microsoft tries to push .NET or Apple tries to push Swift or whatever. They try to, like, it\'s a really big effort for them, and they try to push this. And the open-source community says, I don\'t care. We\'re going to use Python. And Python wins. So if you can somehow enable the vast resources of a million people banging on a thing, even a company like OpenAI or Meta cannot compete with that. And with OLMo, I\'m hoping to capture that a little bit, that if we can capture something with some of the open-source enthusiasm and the academic enthusiasm.

**Nathan Lambert** Do you think it\'ll get better this year? Because a lot of academics are bringing on tens of hundreds of H100 clusters around the country. Like, before, it was like just Harvard had 500 and MIT or whatever. But now it\'s like the long tail of universities. Like, there are a lot of people.

**Dirk Groeneveld** \[01:07:12\]: And then, you know, if you have 200 H100s, you can at least establish scaling laws for your idea. So, like, what I\'m hoping is someone uses OLMo to try some new thing, establish the scaling laws up to a 3B model or whatever. Then we take it and we prove it up to 30B or whatever our computer allows. And if it still works, then, and if it\'s probably going to open, then I take it. And let them win. Let\'s not win. Yeah.

**Nathan Lambert** \[01:07:36\]: I mean, they would never tell us that they\'d win. Yeah. Like, what do we need to achieve this? Do we need resources and compute and certain people? Like, do we need more feedback from the community? Do we need feedback from people at labs telling us which things to do?

**Kyle Lo** \[01:07:48\]: Compute and people, for sure. That is undeniable. If you have more computes, you can try more things. We can go bigger. If you have more people just trying more things, especially like on our artifacts, we\'ll just learn so much more and not have to just like, we spend so much time guess working, trying to piece together things from other people\'s pieces. And sometimes it\'s nice to just get something out of it. So if they did this on OLMo, we can immediately start working off of it. So people, compute, always, for sure.

**Luca Soldaini** \[01:08:20\]: One thing that I, we get a lot of feedback, but it\'s like, I really like AI2. I would like to use OLMo, but it\'s missing this feature, which is great. I love that feedback. It\'s helped us a lot in prioritization. If we could get more, I would love to also get like aspirational feedback of like, none of the models is doing this. But I have a good case for this. Yeah. Those to me are always like very inspiring to read. Whether we\'ll do it or not, it\'s, you know, it\'s a question of like, can we do it and how it works with other things.

**Kyle Lo** \[01:08:55\]: But those are always very, very welcome. You know what would be really cool? I think what would be really cool is like more projects in space that you can\'t do unless you have some sort of fully open constellation of artifacts. Yeah.

**Nathan Lambert** \[01:09:09\]: The thing that Dirk, does anyone ever do the thing where you load the model into one GPU and like iterate through the batches to find the one that, what happens when it blows up and the, or like when a loss spike happens?

**Dirk Groeneveld** I mean, to some degree we did this ourselves. Yeah. But it\'s like something that people can do. It\'s not like we wrote a paper about that, but, but yeah, I would, I would love to see a detailed write-up of like millisecond by millisecond, what happens in a retention when a loss spike happens. You know, how, how does it actually happen? These are the things that people can do.

**Nathan Lambert** And it\'s like, you just have to keep, keep zooming into a specific level of details in what happens.

**Dirk Groeneveld** Yeah. I mean, right now we\'re having, someone is using the various checkpoints to see how a certain metric that we\'re interested in develops throughout pre-training. Yeah. And it\'s like, you can do that with fairly minimal compute. You don\'t have to be AI2. Yeah. It\'s like one of my favorite weird language law papers. It\'s the Sander Land fishing for Magic Karp paper. And it\'s like, you can get much more actual feedback looking at weird tokenization. Yeah. You can get much more actual feedback looking at weird tokenizer impacts and tokenizer data interactions on old mode than just picking API models and figuring it out.

**Kyle Lo** \[01:10:20\]: A lot of also, there\'s a lot of really forward looking at the checkpoints that we have with the data patches and trying to do something like, okay, let\'s replay this, the, between everything between these steps by rejecting some different data or manipulating the data between these two checkpoints, just to see how it turns to something different. How big of a fork does it go through? Yeah.

**Nathan Lambert** \[01:10:39\]: Like if you add the same intervention, like how big does it go through? Exactly. And just to see how it turns to something different.

**Kyle Lo** \[01:10:43\]: So it\'s like reconverge. Or early in pre-training versus later in pre-training same interventions, messing with the data. It\'s just like, that stuff is really cool.

**Dirk Groeneveld** \[01:10:49\]: I mean, I think there\'s, I\'ve complained about this for a long time. Grad students, I think, are a little bit hesitant to go into pre-training stuff because they need to publish four papers a year. And it\'s pretty difficult to do that when your cycles are so long. But on the flip side, it\'s a bit less busy a field. Yeah. So less likely to get scooped if the field doesn\'t change out from under you while you\'re in the middle of your project. Yeah. Post-training is not quite as much as it happens on your side.

**Nathan Lambert** It makes no sense. It\'s just like, pick something you want to do and people will probably do it. That\'s okay.

**Dirk Groeneveld** \[01:11:31\]: So I\'m hoping that by publishing all of this stuff and making all the checkpoints available and the data and so on, we can enable more people to work in that side as well.

**Nathan Lambert** Yeah. Anything else you guys want to add?

**Kyle Lo** \[01:11:49\]: Like, comment, subscribe.

**Kyle Lo** \[01:11:52\]: Yeah, I think that\'s it.

**Nathan Lambert** \[01:12:01\]: Okay. Thanks for listening. If you have questions for any of us individually, the Blue Sky and Twitter handles for everyone in this podcast are below. And you can reach out to the general OLMo contact at allenai.org. That\'s an email address. Or we\'re really happy to help and we want to keep building this kind of open scientific ecosystem of language models. So all the best. Bye bye. Bye.
