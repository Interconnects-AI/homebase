---
title: "Interviewing Tim Dettmers on open-source AI: Agents, scaling, quantization and what's next"
subtitle: "Interconnects interview #10. Catching up with one of the leaders of open-source AI."
date: 2024-11-07
type: podcast
audience: everyone
visibility: public
post_id: 151240703.tim-dettmers
email_sent_at: 2024-11-07T14:00:36.938Z
---
[Tim Dettmers](https://timdettmers.com/about/) does not need an introduction for most people building open-source AI. If you are part of that minority, you're in for a treat. Tim is the lead developer behind most of the open-source tools for quantization: [QLoRA](https://arxiv.org/abs/2305.14314), [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes), [4 and 8 bit inference](https://arxiv.org/abs/2212.09720), and plenty more. He recently finished his Ph.D. at the University of Washington, is now a researcher at the Allen Institute for AI, and is starting as a professor at Carnegie Mellon University in fall of 2025.

Tim is a joy to talk to. He thinks independently on all the AI issues of today, bringing new perspectives that challenge the status quo. At the same time, he's sincere and very helpful to work with, working hard to uplift those around him and the academic community. There's a reason he's so loved in the open-source AI community. We cover:

-   General vibes in open-source,

-   Agents, SWE-Bench, and using open models for tasks like this,

-   How to be a GPU poor academic and have huge impact,

-   Optimization, architectures, quantization, etc.

-   And many other great topics.

Find more about Tim on his [Twitter](https://twitter.com/tim_dettmers) or [Google Scholar](https://scholar.google.com/citations?user=lHI3w5kAAAAJ). He also has a great blog where he talks about things like [which GPUs to buy](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/) and [which grad school to choose](https://timdettmers.com/2022/03/13/how-to-choose-your-grad-school/).

Listen on [Apple Podcasts](https://podcasts.apple.com/us/podcast/interconnects-audio/id1719552353), [Spotify](https://open.spotify.com/show/2UE6s7wZC4kiXYOnWRuxGv), [YouTube](https://www.youtube.com/@interconnects), and [where ever you get your podcasts](https://www.interconnects.ai/podcast). For other Interconnects interviews, [go here](https://www.interconnects.ai/t/interviews).

:::::::: {#youtube2-0SVmBrbx2Rw .youtube-wrap attrs="{\"videoId\":\"0SVmBrbx2Rw\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=0SVmBrbx2Rw){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

### **Show Notes**

Here\'s a markdown list of companies, people, projects, research papers, and other key named entities mentioned in the transcript:

-   [QLoRA](https://arxiv.org/abs/2305.14314)

-   [Bits and Bytes](https://github.com/TimDettmers/bitsandbytes)

-   [Llama 3](https://www.interconnects.ai/p/llama-3-and-scaling-open-llms)

-   [Apple Intelligence](https://www.interconnects.ai/p/apple-intelligence?utm_source=publication-search)

-   [SWE Bench](https://www.swebench.com/)

-   [RewardBench](https://huggingface.co/spaces/allenai/reward-bench)

-   [Claude](https://www.interconnects.ai/p/switched-to-claude-from-chatgpt) (AI assistant by [Anthropic](https://www.anthropic.com/))

-   [Transformers](https://github.com/huggingface/transformers) (Hugging Face library)

-   [Gemma](https://www.interconnects.ai/p/gemma-google-ships-it?utm_source=publication-search) (Google\'s open weight language model)

-   [Notebook LM](https://notebooklm.google/)

-   [LangChain](https://www.langchain.com/)

-   [LangGraph](https://www.langchain.com/langgraph)

-   [Weights & Biases](https://wandb.ai/)

-   [Blackwell](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)) (NVIDIA GPU architecture)

-   [Perplexity](https://www.perplexity.ai/)

-   [Branch Train Merge](https://arxiv.org/abs/2208.03306) (research paper)

-   \"[ResNets do iterative refinement on features](https://arxiv.org/abs/1710.04773)\" (research paper)

-   [CIFAR-10 and CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) (computer vision datasets)

-   [Lottery Ticket Hypothesis](https://arxiv.org/abs/1803.03635) (research paper)

-   [OpenAI O1](https://www.interconnects.ai/p/reverse-engineering-openai-o1?utm_source=publication-search)

-   [TRL (Transformer Reinforcement Learning) by Hugging Face](https://github.com/huggingface/trl)

-   [Tim\'s work on quantization](https://arxiv.org/abs/2208.07339) (this is just one example)

### **Timestamps**

-   \[00:00:00\] Introduction and background on Tim Dettmers

-   \[00:01:53\] Future of open source AI models

-   \[00:09:44\] SWE Bench and evaluating AI systems

-   \[00:13:33\] Using AI for coding, writing, and thinking

-   \[00:16:09\] Academic research with limited compute

-   \[00:32:13\] Economic impact of AI

-   \[00:36:49\] User experience with different AI models

-   \[00:39:42\] O1 models and reasoning

-   \[00:46:27\] Instruction tuning vs. RLHF and synthetic data

-   \[00:51:16\] Model merging and optimization landscapes

-   \[00:55:08\] Knowledge distillation and optimization dynamics

-   \[01:01:55\] State-space models and transformer dominance

-   \[01:06:00\] Definition and future of AI agents

-   \[01:09:20\] The limit of quantization

### **Transcript**

AI generated with `smol-podcaster` and lightly edited for clarity.

**Nathan Lambert** \[00:00:00\]: Hey, welcome back to Interconnects. This episode is an exciting one. It\'s with Tim Dettmers.\
Okay, Tim, welcome to our bootleg in-person AI2 office recording studio we might get barged into, but I\'m just excited to pick your brain. I mean, we eat lunch together and we talk, and it\'s obvious that we agree on a lot of things. We have a unique perspective on a lot of things and it challenges normal worldview. So it\'s good to just share it with people. I\'ve got this rundown and we\'ll definitely go off script, but it\'s mostly on things that I find are takes fun on to prompt you. And it\'s like kind of looking at, we have a full LLAMA3 suite from 1b to 405b. When they release them, it\'s like Mark Zuckerberg\'s like, oh, we\'re challenging the best models and we\'re making open source AGI and all this debatable stuff, but like which of these models in the future do you think would be most useful or do they even need to go smaller?

**Tim Dettmers** \[00:01:53\]: Yeah. Yeah. First of all, thanks for having me here. So I think, I mean, if I look at the Chinese models, actually, they\'re like super competitive and super good. I mean, what I heard, and I think they also publicly said that there will probably not be an open source LLAMA4. So\...

**Nathan Lambert** \[00:02:14\]: Wait, you mean not at all?

**Tim Dettmers** \[00:02:16\]: I don\'t think so. I think the next sort of scale of models, they just will not be open source. I think we are at the end of open source models now.

**Nathan Lambert** \[00:02:24\]: Do you think they\'re going to release, like they\'re still going to release LLAMA4 8b and stuff like this, do you think?

**Tim Dettmers** \[00:02:32\]: Maybe, maybe, yeah. I think when I say sort of, they\'re not going to release that or we are sort of the end of open source, it\'s like, we probably will not get models that are much, much more capable. We will not get GPT-5 level open source models.

**Nathan Lambert** \[00:02:48\]: This was like, I\'m trying to, it\'s funny because Wednesday is also my birthday and it\'s my one year anniversary too, so I\'m working, this might get released later, but I\'m working on a post which is like, why open? And this is what it feels like, the whole open source economy, the definitions are moving so fast and it\'s like mostly influenced by meta that is doing this thing for competitive reasons, which is totally the opposite of what we mean, we\'re like, why we are doing what we\'re doing. And it\'s like, that might be in some ways, if meta stops releasing them, it\'s good for the development of this area as a whole, but also, but like all the hit pieces are like open source AI is doomed.

**Tim Dettmers** \[00:03:25\]: So I don\'t like.

**Nathan Lambert** \[00:03:26\]: Yeah.

**Tim Dettmers** \[00:03:27\]: I mean, on the other hand, I feel like we don\'t need much better models. I think we\'re good to go. We just need to work with them better.

**Nathan Lambert** \[00:03:35\]: Yeah. I mean, this is my, it\'s like preference data has been the thing in post-training that we do none of. And it\'s all the, most of the open instruction data is like role-playing and like these kind of not very specialized tasks and we see like AlpacaVal and all these things are popular where we need a lot more kind of specifics on like, what should people actually be doing with open models? Like we can go right into this, because I know you\'ve been working on [SWE Bench](https://www.swebench.com/) a lot and like, do you think, this is just one example domain, but like in the future, do you think it\'ll be better to use open AI API models or those types of things? Or are people going to actually be training models on open ways to do this type of thing?

**Tim Dettmers** \[00:04:17\]: I think, I mean, it\'s sad to have sort of several dimensionless questions. I believe open source can be competitive and might be actually just overtake the closed source APIs because of flexibility, because of ecosystem. The open AI API is very specific. It\'s done very well for what you need it to do. But once you need to package it together, that\'s sort of where things end. And with packaging together, it\'s like build more complicated pipelines, incorporate fine tuning and incorporate steps where you make small adjustments to the model.

**Nathan Lambert** \[00:04:58\]: Isn\'t this what a lot of AI products are doing? Like, isn\'t this what Perplexity is doing? Like I\'ve talked to them a bit and I know other startups that are smaller, but it\'s like they do multiple model passes and then they just like put them all together. And there\'s probably like one core, there\'s the knowledge store, but the core model, I\'m guessing it\'s some API model. And it\'s like, is that just because it\'s cheap? It\'s like why? It was a later question. It\'s like, why do people build on APIs and not open models? My consensus is it\'s so cheap and it\'s so easy right now and you don\'t need the marginal gains. Like, is that going to change?

**Tim Dettmers** \[00:05:28\]: So, yeah, I mean, I think right now we don\'t have the open source infrastructure to really compete in terms of cost effectiveness. I mean, I developed some things and that seems to work quite well. And so I think if you look at the overall ecosystem and just inference, I think you can be competitive, but we need to create the open source infrastructure. But once we have that, I feel like fine tuning is too cumbersome. Open source will clearly win there.

**Nathan Lambert** \[00:06:05\]: Wait, let\'s be more specific. What about using a fine tuning API is cumbersome?

**Tim Dettmers** \[00:06:10\]: So, I mean, there are like privacy issues with uploading your data and so forth, but then it\'s also it\'s sort of a black box. If you do a little bit of fine tuning, you quickly learn to how to do it.

**Nathan Lambert** \[00:06:23\]: Yeah. And it\'s like the opening APIs are like Laura\'s, right? Normally, I think it seems like that from what they\'re marketing it as.

**Tim Dettmers** \[00:06:30\]: Yeah. And so I think that that\'s sort of definitely a thing. But yeah, it\'s also if you have your process, you get used to it and you know, like how certain things look like if they\'re not working or if they\'re working, you can build on top of that and you can take this experience, share it with others. With these sort of black box APIs, you don\'t know what\'s under the hood. You don\'t know if the system is changing.

**Nathan Lambert** \[00:06:55\]: And this is kind of like a philosophical question that I\'m thinking about with our work. It\'s like, will the APIs always need to do this like long tail of random implementation things? Because if fine tuning is so much more than instruction tuning now, like, is it almost do you think that\'ll be a reason that they lose if we get really good like preference tuning and RL infrastructure in the open? It\'s like, how is OpenAI, you know, like RL on your really specific prompts that you come up with for your business?

**Tim Dettmers** \[00:07:21\]: Yeah, I don\'t know. I think I think OpenAI also has the philosophy to have the business stuff, let the businesses do that. And I think integrating those insights into the API is just a hopeless, hopeless problem. I don\'t think they have the expertise. I don\'t think it would make sense for them from a cost perspective to really figure out what is needed by everyone. How can we satisfy everyone? And but if you have an open source solution, open source can develop all kinds of solutions. Then you say like, oh, I take this. This is best for me. And then, oh, I take this.

**Nathan Lambert** \[00:07:56\]: Do you see that happening? Because that\'s like a big part of the Hugging Face model is like you\'ll have a model for specific things. And I follow Hugging Face and I see it\'s mostly I see like mostly multilingual as the area where there\'s really specific things. But how do we shift that into like this is the arithmetic is a terrible example. But like that type of thing.

**Tim Dettmers** \[00:08:15\]: Yeah. I mean, when I talk to companies, a lot of companies use Qlora because it\'s cost efficient. But then also they just want to pull some data from the data store, fine tune it quickly and then deploy the model and let\'s compare it, do an A-B test or whatnot. And so there\'s this flexibility in the sort of you have Lagoblocks that you combine, then also the infrastructure that works with their infrastructure that they have. I mean, in the end, you need to deploy it.

**Nathan Lambert** \[00:08:42\]: You need to maintain it. And do you think the open source equivalent for Apple Intelligence will end up being better because they can interface with more models? So like Apple Intelligence is just Apple models and they\'ll have to do work to bring in the open source, but the open source won\'t help them.

**Tim Dettmers** \[00:08:58\]: Yeah. Yeah. So I think actually the biggest sort of factor why I think Apple Intelligence will not be the biggest thing is because it will be built for Apple products.

**Nathan Lambert** \[00:09:09\]: I\'m using it and it\'s entertaining. It\'s in beta and it\'s like, oh, this notification summary is entertaining. I can generate tables. Yeah. But like their iteration speed just seems like it\'s going to be so slow.

**Tim Dettmers** \[00:09:20\]: Yeah. And it will be for their products. Like, I think we are still at a point where it\'s unclear what people want to use AI systems for. There are a lot of prototyping, a lot of demos, but not so many points that like, yeah, we really increase productivity. Often it\'s more engineered solutions that increase productivity.

**Nathan Lambert** \[00:09:41\]: Do you think SweetBent is a good example?

**Tim Dettmers** \[00:09:44\]: So, yeah, I think so. So I think a big problem with benchmarks is they\'re so saturated that it\'s unclear if the improved performance on MMLU or whatnot translate to real world performance. The nice thing about Speedbench is like, you know, if you improve on it, it has real sort of implications in the real world. Like if you improve a couple percent, that\'s what a couple percent actually means.

**Nathan Lambert** \[00:10:13\]: So a couple percent is like a couple more working test cases on a GitHub issue. That\'s what it means, right? Yeah. Is there a fine-grained way to think about SweetBent?

**Tim Dettmers** \[00:10:22\]: Yeah. So you can think about sort of general difficulty and some bug fixes are just super hard on [SWE Bench](https://www.swebench.com/). And then there\'s just a collection of sort of easy things. And sort of depending on that, you can quickly hill climb and then you hit certain

**Nathan Lambert** \[00:10:40\]: Is it like almost levels? It\'s like you do all the easy ones, you do the medium ones.

**Tim Dettmers** \[00:10:44\]: I think right now it\'s still unclear, but that\'s what it feels like to me.

**Nathan Lambert** \[00:10:48\]: What do you think these companies that are raising tons of money to max on SweetBent are

**Tim Dettmers** \[00:10:53\]: doing? So from what I see from my work is that the most important thing on [SWE Bench](https://www.swebench.com/) is to get the workflow right, how you basically use your model.

**Nathan Lambert** \[00:11:07\]: And that\'s so different than modeling. Like everyone thinks about AI benchmarks as the modeling problem, but that\'s why it\'s like we need\...I think this will be a big focus in 2025 and I want to learn about it. And it\'s like, what does it mean for an evaluation to not be about modeling?

**Tim Dettmers** \[00:11:23\]: That\'s right. That\'s right. I think it will be difficult to disentangle in the future. It\'s like our tasks get more complicated because they\'re too saturated. So we need complicated tasks. But complicated tasks, you can\'t just like take a complicated task, throw it at a model. That will not be possible. Like you need to design things around it. But then the entire system needs to be evaluated.

**Nathan Lambert** \[00:11:45\]: It almost seems like only base model evaluation is easy because we\'re having discussions for RewardBench v2 and there\'s a lot of new work on evaluating reward models. And we see a trend where what we did was accuracy. So does your reward model agree with these pairs? And then a lot of people are doing correlations with downstream ROHF, which is like, I think you need both. But it\'s a very messy argument to be like, you need something that correlates with something like chatbot arena. But there\'s so many steps in that chain. You have to train your reward model. You have to have your evaluation data. You have to evaluate on humans. And the other thing is like accuracy and it\'s kind of constrained. And I think in [SWE Bench](https://www.swebench.com/)\'s case, to make it very academic, you\'d probably need to have multiple facets, which is like, how does it handle this type of information? And then you will see the final score of like putting it all together.

**Tim Dettmers** \[00:12:31\]: Yeah. So, yeah, I think evaluation is just a super hard problem. I think for me, so personally, I use Claude quite a bit. And if I look at the benchmarks numbers, GPT-4-O looks quite good. But when I use it, it\'s like, no, Claude is just much better.

**Nathan Lambert** \[00:12:48\]: And what is most of the code you\'re writing? Like, I know some of the tools you\'re writing. It\'s just like normal PyTorch or wrappers or things.

**Tim Dettmers** \[00:12:56\]: Actually, I found AI models pretty useless for code. So I\'m not using them much for code. So what are you using it for? I\'m mostly writing stuff, thinking about stuff, sort of double-checking my thoughts, finding critical feedback.

**Nathan Lambert** \[00:13:19\]: So you and Dirk are the people that are like, it\'s not good enough for code. It\'s the people that you just get so much done and you\'ve spent time doing enough code where it\'s not going to help. It\'s not going to help with CUDA kernels. You\'ve gone so deep on different coding that you just don\'t need it.

**Tim Dettmers** \[00:13:33\]: I mean, sometimes if you need to write a lot of boilerplate, it can be useful. And also to sort of, I don\'t know, one time I thought like, hey, this problem must be possible with these models. And I actually tried both Claude and GPT-4-O. And it\'s like, it\'s just the code appears to be good and it\'s sort of sensible. But then if you look at the details, it makes absolutely no sense. And it\'s sort of, it\'s just more work to disentangle the code into something that\'s good, that you can build on. So I don\'t know. My thinking is like, if the code doesn\'t require much expertise and you have an existing system that you extend, good. If you want to have sort of core system that you build on, not good enough. If it requires deep expertise, also not good enough.

**Nathan Lambert** \[00:14:21\]: Yeah, it\'s like you could write, no offense to the Hugging Face Transformers ecosystem, like you could probably write another model pretty easily and it\'s like an add-on. But writing the core abstraction for like a training architecture is really hard.

**Tim Dettmers** \[00:14:33\]: Yeah, I think that makes sense. I mean, models can write it, but then you will lose so much time in the future when you need to get back to change something, maintain it, or\...

**Nathan Lambert** \[00:14:43\]: The maintenance thing is there.

**Tim Dettmers** \[00:14:44\]: It\'s just choices are really bad, the design choices.

**Nathan Lambert** \[00:14:46\]: I mean, like I\'ve definitely seen code that I\'ve written that I am blown away that Cloud solves it. But then later I\'m like, well, that was a minor issue. It\'s like the random doubling batch size or something that I didn\'t know was in it. So it\'s a net add for me and I still use it. I mean, I know I\'m not as good of an engineer as a lot of people I work with. So I\'m like, I\'m happy to have something that normalizes the distribution. So like what is happening is probably like the best coders are still better. And then the people that weren\'t as good are getting pulled up. So like the Delta isn\'t as big, but you still have probably a headway. But like I can just do a lot of stuff that I couldn\'t do.

**Tim Dettmers** \[00:15:21\]: So I see myself when I write in languages that I don\'t really know or I don\'t know. It\'s just I understand quickly things. I make quick progress and probably that all the underlying issues that I just said, but I don\'t see them because I\'m unfamiliar with the issues in those language or with a particular sort of piece of software. Yeah.

**Nathan Lambert** \[00:15:44\]: OK. Switching gears, you\'re from one hat as an engineer to your hat as an academic. It\'s like it\'s easy as well-resourced academics to choose the right problems to work on. But what should people in various amounts of compute be doing to try to contribute either to this open ecosystem and write good code or just like fundamental research and language models? Like, do you have a few things you recommend?

**Tim Dettmers** \[00:16:09\]: Yeah, I think it\'s it\'s a lot about trends. So and I view it often from sort of if you want to get good AI systems that tiny, a lot of tiny factors, sort of multipliers, you can sort of if you have a low multiplier, it\'s very much worth sort of scale it up and just improve the overall product of all these small factors. And if I look at\...

**Nathan Lambert** \[00:16:32\]: What do you mean by multiplier? So do you mean like multiple models in a system or what?

**Tim Dettmers** \[00:16:36\]: You can figure out a better architecture or better attention or better scaling.

**Nathan Lambert** \[00:16:41\]: So it\'s like when people at big companies call it like flop efficiency or something.

**Tim Dettmers** \[00:16:45\]: Or quantization, but they\'re diminishing returns. And at some point it\'s like, yeah, if you improve it a little bit more, it\'s not making a difference. And so you should look for what is making a difference. And I mean, it gets harder if you don\'t have the compute resources. But I think that\'s sort of the first factor. I see a lot of people when they get computer resources, they\'re like, oh, I got all these GPUs. And then they work on problems that require a lot of GPUs.

**Nathan Lambert** \[00:17:11\]: Let\'s put some numbers on it. As academics, a fun thing is like how many GPUs does UW have? We can shoot like AI2 is known. We have this like 1000H100 cluster that\'s growing a bit and a long tail of other GPUs and some TPU access. Like that\'s more than most academics. And then how many does like something like UW have?

**Tim Dettmers** \[00:17:31\]: I mean, UW has around 600 GPUs.

**Nathan Lambert** \[00:17:35\]: Probably for more people is what I\'m guessing.

**Tim Dettmers** \[00:17:38\]: It\'s actually like less, it depends. And so I\'m actually sort of helped sort of design the cluster and has sort of the system where sort of PIs buy GPUs. And then their students can use those GPUs. But then there\'s a free queue where everybody can get idle GPUs. And so I as a student.

**Nathan Lambert** \[00:17:59\]: It\'s a great system where it\'s like the rich, rich professors help pull up everyone else.

**Tim Dettmers** \[00:18:05\]: Yeah. And I mean, I always use the idle queue and I could get like 100, 200 GPUs no problem most of the time. And so I could do pretty good with that.

**Nathan Lambert** \[00:18:15\]: How do you feel like this compares at other well off like CMU, Berkeley, Stanford, MIT? Like do they have similar access?

**Tim Dettmers** \[00:18:22\]: I thought so. But when I was on the job market, I could see that very few institutions actually have good GPU systems.

**Nathan Lambert** \[00:18:31\]: This is something that\'s like with the policy, talking to the policy and the government. It\'s like if you can assume the government can spend one to three billion dollars on AI. It\'s like a lot of people are like, let\'s just buy a lot of GPUs. But it\'s almost like it\'s you\'re just going to get caught in the fact that you buy GPUs that you can\'t utilize if you just spend the money on it. So it seems like UW did well. And I\'m guessing other institutions have GPUs that can\'t quite work for the whole community as well.

**Tim Dettmers** \[00:18:52\]: Yeah. And I mean, they are the most one issue that are often here. Academics are like, oh, we have money. Let\'s buy GPUs. And then they buy the GPUs and then figure out, oh, my storage is too slow and I can\'t use the GPUs. Because my storage is not working well. Well, oh, my network is not working well. Or, hey, my queuing system is so poorly designed.

**Nathan Lambert** \[00:19:11\]: Do you think the AI2 Beaker team should be more open about the things we\'re solving and how we make those decisions? Like, would that help academics?

**Tim Dettmers** \[00:19:18\]: I think I think the software is not necessarily a problem. Like you can use Slurm.

**Nathan Lambert** \[00:19:24\]: But it\'s like how we\'re deciding with vendors, even because AI2\'s GPUs aren\'t just from like there\'s a decision process between all these big clouds, medium clouds.

**Tim Dettmers** \[00:19:33\]: I mean, it\'s complicated. So, I mean, what I can say, there are certain cloud providers that are known for having reliable networking. They have the NVIDIA stack, which is much easier to integrate in software.

**Nathan Lambert** \[00:19:45\]: It\'s just tough that it\'s often like an IT department that\'s going to make these decisions.

**Tim Dettmers** \[00:19:50\]: I don\'t know. I don\'t know.

**Nathan Lambert** \[00:19:51\]: I\'m just trying to learn about the academic sphere. Yeah. And what we can say to people that are like, I have X amount of GPUs. And I generally think that it\'s like the amount of GPUs that you need multiplied, like if you multiply a training run, the amount of GPUs you need to do a training run in an amount of time that gives you feedback faster. So normally, like for non-pre-training things, it\'s like you want your experiment to be like order of an hour. It\'s like you can do it really fast, order of day or two. It\'s like it\'s still good. And then like once you go beyond a week, it\'s like hard to mentally string them together. So it\'s like, I\'m guessing there\'s a lot of people that can do these experiments, but they do them sequentially because they don\'t have enough GPUs. And it\'s like, how do you, like, what is the GPU, like what is the tradeoff that people can make to try to scope their problems?

**Tim Dettmers** \[00:20:37\]: So, I mean, one thing how I approached my research in general was I get a baseline that is informative and runs in four GPU hours. And so if you have that, and you also need to check if it sort of extrapolates, and most of the time it doesn\'t, but it gives you a good correlation. So, you know, if you\'re right, then you know, like, maybe I could be right, but if you\'re wrong, you definitely know you\'re wrong. And so you can get a quick result and see if ideas make sense. Once you\'re in the setup, you just, you don\'t want to run an experiment and then experiment, you run like a hundreds at a time, then another hundred, another hundred, you get evidence very quickly. And then, you know, like, okay, this, this, this, and this.

**Nathan Lambert** \[00:21:22\]: I mean, I\'ve definitely heard this from professors, research managers, that the people who stand out are the ones that can mentally run the most experiments in parallel and keep track of them.

**Tim Dettmers** \[00:21:31\]: I think, I think that makes sense. I mean,

**Nathan Lambert** \[00:21:35\]: How do you select or curate for that skill?

**Tim Dettmers** \[00:21:38\]: Oh, um,

**Nathan Lambert** \[00:21:39\]: Like, if you\'re going to advise a student, it\'s like, how do you get them to set up their life so that that is like a doable thing?

**Tim Dettmers** \[00:21:45\]: Um, I mean, I have done it and I feel like you need a certain mental model to get in sort of this mindset, really. I mean, basically what you just described, that if you know that\'s the goal, you can optimize for that. But most people think like the goal is something different. Um, and then you\'re not optimizing for that. So, um, the thing is, for example, you can spend two weeks on infrastructure, then run a lot of experiments, or you can say like, no, no, I get my need to get my experiments going. Then quickly run an experiment, another experiment, another experiment. For my experience, it\'s always more efficient to first build the infrastructure and then just gives you the sort of peace of mind. You can think more clearly and then run.

**Nathan Lambert** \[00:22:33\]: What are other, are there other popular frameworks you\'ve released other than Qlora that are like infrastructure that I just don\'t know about? I mean, like Benton Blights, I know about, I associate that with Qlora. But how much is it more than that?

**Tim Dettmers** \[00:22:44\]: Uh, yeah, I mean, there is some library that\'s called sched. It\'s like a GPU scheduler that I built over my PhD. Um, and people use weights and biases. I think it really holds them back. Um, weights and biases is like really bad for, I mean, if I run a thousand experiments, no, no hope to analyze it. And so what I developed, what this system is, it\'s sort of does a grid search in a way where you get the most information with the least experiments. And then it does an analysis.

**Nathan Lambert** \[00:23:19\]: Is it like a Bayesian optimization thing? Or is it just a, it\'s a grid search algorithm?

**Tim Dettmers** \[00:23:23\]: It\'s sort of a certain grid search job, which, um. So, so what you can do is basically an interval search. So it\'s not random search. And then what you can do is combine different hyper parameters in different settings. So, um, in that way, um, you basically, if you want to evaluate multiple hyper parameters, then you have for each hyper parameter, only one experiment, but you have for all different kinds of combinations with the particular hyper parameter, maybe a dozen experiments or more. And so that isolates as a variance. And so what you can do with my tool is basically give a group variance for that hyper parameter based on all other hyper parameters. And then you can see what matters.

**Nathan Lambert** \[00:24:10\]: What is your background in? I should have asked earlier, like before your PhD, what were you doing?

**Tim Dettmers** \[00:24:14\]: Yeah. I worked a little bit in automation industry for three years. Um, study a little bit of psychology.

**Nathan Lambert** \[00:24:19\]: Robotics or what type of automation?

**Tim Dettmers** \[00:24:21\]: Uh, that was factory automation and mostly food factories. A lot of milk factories. Um, like what are you actually doing? So, so, I mean, there are different parts of sort of, uh, factory automation, sort of what I specialize in sort of integrating systems, integrating their data systems, and then, um, routing data, um, making data accessible to sort of a person that controls all machines or to management that sort of gets aggregated reports on performance. Um, yeah.

**Nathan Lambert** \[00:24:54\]: I\'m trying to understand why infrastructure might not be prioritized as much because it seems like when you have very good infrastructure, you can approach your approach, your AI research in a much more scientific way.

**Tim Dettmers** \[00:25:04\]: Yeah.

**Nathan Lambert** \[00:25:05\]: And is it just the same rat race incentives that are kind of making people not prioritize it?

**Tim Dettmers** \[00:25:11\]: Um, this is a good question. I, I don\'t, yeah, I don\'t quite know myself. I think, I think if I think about, I mean, so when I started in my PhD and I think about software engineering. My software engineering, engineering skills went down because I wasn\'t this mindset of like just producing an experiment to get a result. And that\'s often the fastest way to move forward because you just need a negative result to reject an idea. So you quickly want to get that negative result. And so, um, with this mindset, you have sort of the mindset of the throwaway software. Uh, you just want to build a software and throw it away.

**Nathan Lambert** \[00:25:49\]: It\'s like all of my PhD was built on this, except for the one paper that was like a tool. And it\'s like, why is this the, it\'s like, why is this the case? And it\'s only at AI2 that I feel like I\'ve started. I mean, at Hugging Face, I learned a lot more about open source software, which is very fun to like be on the ground floor of when like diffusers is happening. And it\'s like, you do these opinionated things to make your users lives the easiest. And then some of the things are about making your life easier, which is Hugging Face\'s audience is different than the researcher audience. Like the Hugging Face audience is, we have a ton of users. We need to make their lives easy for what their use case is. And the researcher is, I have one to three users and I need to make this very good for a long timeframe, which is like a very specific type of open source software. And it\'s like open instructor, fine tuning libraries like this, where it\'s, we didn\'t have it packaged like pip installable for like eight months because we use Docker. So it was easy to load the Docker image and then edit your files. But if you had pip install, it added a whole bunch of steps on it. It\'s like, this is like really nice tooling, but it\'s like the opposite from what TRL looks like at Hugging Face. And it\'s like having more examples for people to understand academic tooling seems cool. And now I\'m wondering, like, oh, what is, how does like Open, is OpenAI\'s research tooling tied to their deployment tooling or is there a fence that it goes over?

**Tim Dettmers** \[00:27:11\]: I mean, as far as I heard, there\'s definitely quite some difference. There\'s also some overlap. I mean, if somebody builds efficient tooling, you can reuse it. But for certain problems, you need certain tooling. What also a colleague said, also working in a Frontier lab, is that basically every experiment is an infrastructure problem if you work at a certain scale. And so you just first need to engineer the infrastructure to run that experiment. And how you describe it sounds a little bit like sometimes the infrastructure is too specific to generalize. So you probably have your production sort of infrastructure, you have like sort of experimentation infrastructure. And then you have sort of small sort of branches that branch off of it that you use for a small project or so. But you probably need to work on it a little bit to get something started.

**Nathan Lambert** \[00:28:09\]: Yeah, it\'s like, this is like a hard question. It\'s like if your lab only has a few A100s and A200s, is the best bet to not do language models then and do something that\'s longer term?

**Tim Dettmers** \[00:28:23\]: So I think you can do really good research on very little compute in language models. I mean, you shouldn\'t pre-train language models.

**Tim Dettmers** \[00:28:36\]: Certain problems need a certain amount of compute. What I see, for example, on 3Bench, you need enough compute for inference. And that\'s significant. But also certain problems on 3Bench, you can do with less compute. And so I think constraints actually give you sort of more creativity. And so I was at Meta part-time for like two years and I had access. I could run things on like 500 GPUs.

**Nathan Lambert** \[00:29:05\]: The amount of experiments I could run when I was at Facebook in turn was absolutely hilarious. They had set up a whole new cluster and the most unfair, like didn\'t know how to use it yet. Probably because they didn\'t know how to use Slurm. And some software engineer was like, here, you can use it. And I can use like 300 concurrent GPUs in like 2019 as an intern. I was like, what? That was just silly.

**Tim Dettmers** \[00:29:25\]: But yeah, for me, it was I had access to all the GPUs and I worked on problems that required a lot of compute, but I didn\'t make good progress. And then at some point, so this deal with Meta was for two years. Then I went back to the University of Washington, had much less compute, but I made much more progress because I know like, oh, I can\'t work on these expensive problems. I really need to think about what problem I should work on and what I can use with my resources. And I think that made my research actually better.

**Nathan Lambert** \[00:29:50\]: So are you still, I mean, your job talk, everyone hyped it up about your story, about using laptops and everyone\'s compute. Like, do you think that\'s going to be the case in the next few years? Yeah, definitely.

**Tim Dettmers** \[00:30:00\]: So, so, so laptops over there, I would hold up the ridiculous bricks that we all get. No, I think our laptops will be powerful enough to run, I mean, not probably not develop, but run the AI that we probably want to use in everyday life. Yeah. And I mean, as I said, there\'s sort of this question, will open source and closed source, how they will compete? I think open source will win actually over time.

**Nathan Lambert** \[00:30:30\]: Okay, let\'s dig into this. Like, there\'s two things, like, why will open source actually win? I think we\'ve talked about scaling a bit here. I\'ve kind of put my, like, I feel like I\'m a scaling moderate, or I\'m like, yes, the loss will go down. But you\'re really putting yourself into financial, you\'re making a financial bet, which is, which, okay, like, open AI raises so much money, all these companies raise money, it gets funneled through TSMC, we get new process nodes. Like, we\'re going to keep these process nodes forever. We\'re going to be able to make better computers. So it\'s nice in some ways that they\'re doing this. But the financial risk seems extreme. So that\'s my, like, are you a bubble buster? Like, do you think this is all going to just blow up? I think a lot of AI startups will blow up. I\'ll say the like, things that can be controversial first, and you can fill them in. Like, so many startups are going to go belly up, because that\'ll hit them first. And Google\'s fine.

**Tim Dettmers** \[00:31:17\]: Yeah, I mean, I think probably we follow a similar pattern to the dot com boom. So we will grow more, more, more, probably a couple more years. And then 95% of companies will fail. But then the remaining companies will probably\... AI, I think AI will have a major impact. And so I don\'t think AI will not work. But it\'s, I don\'t think we have what we need right now. If you look at OpenAI, they did cool things, but they really failed at landing a product besides chat GPT.

**Nathan Lambert** \[00:31:48\]: Well, yeah, chat GPT is a huge land, but it\'s like an unintentional land.

**Tim Dettmers** \[00:31:53\]: Yeah, yeah. And so, I don\'t know, compared to the cost, it might still work out for them. But it\'s\...

**Nathan Lambert** \[00:32:02\]: Do you still think AI is like the most transformative technology of our time? Or do you think that it\'s just like slightly additive to everything that was happening in the internet?

**Tim Dettmers** \[00:32:13\]: I think it will be quite transformative. It\'s unclear how exactly. I mean, people debate that so about the internet. Like, if you look at social media, and you say, like, is that it? You look at the value created, like finding information and sort of, I think, I think digitalization, sort of, if you look sort of an economic scale, which is really important.

**Nathan Lambert** \[00:32:38\]: Part of my view is like, what would be the case if we recommend our systems were all built on open source infrastructure. And I think language models are more culturally salient, because people talk to them in text. Now people talk to them in voice. Yeah. And that almost just feels like a stronger imperative, because all of the negative effects can go way deeper. It\'s almost like this, what is it, the stupid food chain thing where you have toxins, and like, the little fish don\'t get that affected by the toxins, but all the whales die. And it\'s like, we\'re just getting the really, really concentrated technology, which is like, that\'s why I don\'t want it to be screwed up. But yeah, do you think about these things?

**Tim Dettmers** \[00:33:15\]: I mean, I wonder how, in what way AI will sort of impact society. I mean, if you look at social media, I think most people would say it hasn\'t been entirely positive. And so I think with AI, it\'s like the question, where will there be sort of good parts and where will there be bad parts? I think overall, we see good parts in terms of, it\'s helpful. To some degree, it gets better.

**Nathan Lambert** \[00:33:48\]: Developer productivity and information economy productivity is already way higher, which is like, obviously, it\'s the economy that drives the most value in the world. It\'s just so boring if all that happens is Google, Apple, Meta get three times as big, and that\'s the end of the day.

**Tim Dettmers** \[00:34:06\]: Yeah, yeah. I mean, if you look at the global economy, that\'s still not that major. I mean, yeah, if you look in the US, yes. I mean, there\'s some, I was quite skeptical about economic growth through AI. If you look at the global data, it doesn\'t show. But we see the first time since a long time, actually, a nonlinear increase in productivity growth. And\...

**Nathan Lambert** \[00:34:33\]: Oh, really? Is this recent? Or from what?

**Tim Dettmers** \[00:34:34\]: No, pretty recent, like since the last two quarters, I think. And it\'s like, oh, this hasn\'t happened since the sort of internet revolution.

**Nathan Lambert** \[00:34:45\]: And it\'s like, I expect this stuff to take like 10 years. Like, this is the timescale that we need to look on. Because I think it\'s less, I buy more, this is probably similar, I buy more into we need to figure out how to use this, then scaling is going to solve a lot of our problems.

**Tim Dettmers** \[00:34:58\]: But with computers, it was the same. I mean, computers didn\'t make us more productive in the beginning. And it took like 20 years.

**Nathan Lambert** \[00:35:04\]: And when do you document the start of computers? Like, what is a PC?

**Tim Dettmers** \[00:35:08\]: I think the start was like IBM and having computers and businesses. And so you could do things faster. That\'s why people bought these machines. But productivity growth, you didn\'t even see it with sort of early Windows, where computers became more widespread. It only started later. And so, yeah, we already seen, I mean, it\'s still unclear if the growth that we\'re seeing is due to AI. It\'s it seems that it could be.

**Nathan Lambert** \[00:35:41\]: And a part of it feels like a self-fulfilling process, where we have AI, but we also have like Waymo. And we have SpaceX, like Tesla, like these are not AI things. But it\'s all getting conglom together. Yeah, yeah.

**Tim Dettmers** \[00:35:53\]: I mean, the question is like, what do you call AI? If you just say AI, it\'s just big models trained on lots of data that are very expensive. I mean, Waymo is like a big AI system that\'s complicated. It also has expensive models. Have you ridden in Waymo? No, I actually, I was in San Francisco. I missed. You\'ve got to do it the next time you\'re in town.

**Nathan Lambert** \[00:36:13\]: It\'s like immediately it\'s like this is the future. It\'s like I will pay 20, 20 percent. But honestly, I\'d pay a bigger margin to Uber. And like, it\'s just flat out way better. And I just encourage everyone to do it. It\'s like, yeah, it\'s much more visceral than AI. Like AI has these aha moments. And I was hoping that the AI, talking to AI would feel more like this. But talking to it, I\'m kind of like, that\'s kind of not good. It was like, I was hoping I would be able to say something interesting about it. But it\'s like, chat2BT and just information processing is just so much more straightforward.

**Tim Dettmers** \[00:36:49\]: I\'m curious, what models are you usually using GPT-4, Claude?

**Nathan Lambert** \[00:36:54\]: Yeah, it\'s mostly these. If I\'m doing technical coding, it\'s Claude. I use chat2BT for changing a matrix from Markdown to LaTeX or grabbing it and converting it. And it\'s just a bit better. I don\'t use O1 at all, which is the next thing. It\'s like, O1 is a perfect example of this product problem, where from a technical perspective, I\'m like, this is the most interesting thing to happen for the year. Like, open O1 to me, like, it\'s just so interesting. But you can get this extremely different behavior from an obviously different model training stack. But it\'s like, we don\'t know what to use it for. Yeah, yeah.

**Tim Dettmers** \[00:37:31\]: I mean, O1, I\'m not a believer. So many people work on reasoning. I think it\'s a really bad research direction. I don\'t think reasoning is really important. Like, okay, in humans, reasoning is one thing that sets us apart from other animals. But if you look at neuroscience and reasoning, you would often sort of categorize as working memory. You store information, manipulate that information in your temporary storage. And then with that, you solve problems. And most of the problems you can\'t solve with working memory. But it\'s also very weakly correlated with intelligence. You can take me as an example. I\'m dyslexic. Dyslexics are known to having extremely poor working memory capacity and function. I\'m the bottom 5% in working memory for symbols.

**Nathan Lambert** \[00:38:33\]: What are the things that people use working memory for? I\'m sorry, like, let\'s make it more concrete.

**Tim Dettmers** \[00:38:37\]: So, basically, any conscious processing.

**Nathan Lambert** \[00:38:41\]: Okay, so like holding numbers in your head, doing math.

**Tim Dettmers** \[00:38:44\]: But also holding this conversation in your head. I don\'t know. If you plan already the next question, or where do you go with this conversation? It\'s all intuitive.

**Nathan Lambert** \[00:38:53\]: Like, I do way less prep than a lot of people do, because it\'s like part of the brand of being open. It\'s like, I\'m trying to just bring where I am and transparent. And that\'s why I\'m writing is not that edited. It\'s just like, this is where we are at. And I will try to make it as clear as possible. And I want to bring people in and just kind of see how it goes. But otherwise, it\'s like, so much work.

**Tim Dettmers** \[00:39:14\]: So, it sounds like, yeah, there\'s so much work part that requires working memory. But if it feels like sort of flowing and natural, and you use your sort of intuition, no reasoning required.

**Nathan Lambert** \[00:39:25\]: It\'s like the working memory is the 30-page paper for 2LU3 that I need to extract out of my brain and put into LaTeX.

**Tim Dettmers** \[00:39:32\]: That\'s right.

**Nathan Lambert** \[00:39:33\]: That\'s the working memory, which I definitely use, but that doesn\'t make sense. So, the models don\'t do this. Yeah.

**Tim Dettmers** \[00:39:42\]: So, if you look at O1, it does reasoning perfectly. It sort of reminds me of what I read in the psychology neuroscience literature. It\'s just doing exactly this process that people would describe as reasoning. But it\'s not working because reasoning is not that important. And so, I think people are like, oh, if we have reasoning, we have human intelligence. We don\'t. Other things are more important.

**Nathan Lambert** \[00:40:06\]: I\'m just mostly interested in it because of the interesting behavior. Like, I have no idea what it would be used for. I\'ve been recently thinking that O1 models are similar as a proof of point to like a text information store language model, where you have a lot fewer parameters, and you\'re just doing the processing on an information store. I wish more people would talk about this because like O1 mini is very small, and the model is doing the reasoning. But it\'s like they need to do that training thing on a giant information store, and they have a perfectly up-to-date model with their training. It\'s like, that almost seems like a better product than what they have served for O1. Yeah, yeah.

**Tim Dettmers** \[00:40:43\]: I mean, I bet that would be also even more difficult than what they have now. But, so, if I think about the brain, it\'s actually, it has sort of a long-term memory component, a retrieval component, then the working memory component. If you look at the sort of neuroscience literature, they often like sort of combine, because that\'s what you need in order to reason. So, working memory is the most important part, but you need to load stuff into working memory. For that, you need to retrieve, and there\'s sort of a hierarchy that goes from short-term memory to a sort of a hash table, and then to a new cortex, to then retrieve and basically loop it back into working memory. And that\'s just required, and there are two basically stores of working memory. One is sort of for execution memory, one is for symbolic memory and planning. And so, you need to basically populate these stores in order to reason. But, yeah, you need a retrieval model for that.

**Nathan Lambert** \[00:41:35\]: Interesting. Yeah, okay, I don\'t even have a response, but I appreciate it. Like, this is why it\'s like products like Perplexity make sense, because they\'re, I mean, they are products, and they have a long way to go as a business, and mostly hinges on figuring out advertising, to be honest. Like, a lot of these companies hinge on figuring out advertising for chat models, but it\'s like a nice analog to think about multiple language model passes, which is eventually where academia will go. It\'s just a hard thing. It\'s like, we\'re just figuring out language model evaluation. There\'s all these things, and then we\'re going, and then we\'re making it into this composite thing, which is hard.

**Tim Dettmers** \[00:42:14\]: Yeah, no, I think it will be like composite systems, like complex systems, unclear what form and shape they take. I think for that, benchmarking is hugely important. We need to figure out what we measure. We need to figure out what people care about. Like, there\'s a reason why open AI cannot be a product that makes sense.

**Nathan Lambert** \[00:42:31\]: Do academics need to work on problems that people actually care about, or is it fine? Like, we can just make evals that show interesting behavior.

**Tim Dettmers** \[00:42:37\]: Yeah, I mean, there\'s sort of the academic direction of working on problems to find knowledge, and then spread the knowledge. But it\'s more satisfying to find knowledge that is helpful for people, and for things to be helpful, they need to be somewhat grounded in something that matters to people, that is helpful to people. And for that, you need to understand what they need. And if you understand the needs and wants, then actually what systems will fulfill these needs and wants. And then you have something that you can evaluate that has this sort of path from like, I create knowledge, which is useful. And if you just create knowledge, that might later be useful. I mean, there are a lot of examples in like math, where we have a mathematician say like, oh, this will not be useful. And then it\'s like super useful. But I mean, if you look for benefits in the near future, AI is moving fast, then it needs to be grounded somewhat in what people care about.

**Nathan Lambert** \[00:43:33\]: Yeah, I mean, I agree. I think a lot of why I work here is just like, I want to do basic things that people can build on. It\'s like being in at the foundation level where you\'re building these models is something different and requires more research. And like resources is actually what I meant to say, I kind of stumbled. And then it could, going back to our academic conversation, it almost seems like a good thing to do is like to be imaginative on what you can use these for. Yeah. And then build best practices, recommendations, examples, and storytelling. And then you start to build evaluations and stuff like this.

**Tim Dettmers** \[00:44:08\]: Yeah, I wish people would be a little more creative. I mean, it feels like a lot of researchers sort of are sort of like engineers. They\'re like, oh, this is a problem. Like, I can book your calendar appointment or like, I can summarize your emails. It\'s not really problems.

**Nathan Lambert** \[00:44:25\]: You need to be in a privileged position to where boring things are impactful, which is like AI too. We are the only people that can tell you everything and we have enough GPUs to do something. But like, unless you\'re on the same order of magnitude as somebody with the same thing, you have to be doing something different. Yeah, yeah.

**Tim Dettmers** \[00:44:44\]: I think there\'s a lot of room for different things. I don\'t know. I don\'t know what the problem is. I think it\'s, yeah, probably thinking like, oh, people in labs and they figured everything out. It\'s a simple trade off.

**Nathan Lambert** \[00:45:00\]: It\'s like things are hot now. It\'s hard to make your name when things are not hot. When things are hot, it is easier. It\'s like a presumption. So like what the thing to do is you try to latch on to something that is obviously going exponential. And therefore, a lot of people try to do it. I understand it. It\'s just like taking risk and being cognizant and understanding of what it will feel like to do something new is hard. And I don\'t have a lot of advice for people. It\'s just like that is what it will feel like. It will feel weird and you\'ll probably get like, oh, why are you doing that from a lot of people? Yeah, yeah.

**Tim Dettmers** \[00:45:42\]: I think that\'s the right perspective. It\'s just you need to go with things that are growing. But then we are off a little bit sort of left or right. But it\'s sort of unclear when to do that, when it\'s right and that sort of thing. I think it\'s also a big thing like, I don\'t know, I see a lot of people following the Frontier Labs. But when I hear from the Frontier Labs, nobody has a clue what\'s going on among them. Like they\'re just building stuff like we do. They have no clue. They build one stone thing at a time and things break together and then they try again. And they have no good explanations for things. They\'re just more compute. They have good people.

**Nathan Lambert** \[00:46:27\]: They have good talent density and compute density. It\'s green fields when you have both of those. Yeah, yeah. Okay, I wanted to ask your opinion on some random technical things. What do you think of instruction tuning versus RLHF?

**Tim Dettmers** \[00:46:42\]: Not really an opinion on that. I think we can go a long, long way with synthetic data. And so if I say how much human data, I think human data is very precious and we need it. But we probably can get away with less that is more targeted, more high quality.

**Nathan Lambert** \[00:47:05\]: Yeah, it\'s very hard to measure this. The synthetic data is almost a more interesting point. I think it\'s like John Shulman said this, which is like if you think about preferences, it\'s like humans are high noise, low bias and AI is high bias, low noise. And we don\'t know what the bias and the noise are. But we know like synthetic data is the future in most things. But it\'s like we don\'t know these fundamental things, which is like what actually are they? And I\'m just like, well, if someone could present me with a really compelling research paper there, that will be like seminal work.

**Tim Dettmers** \[00:47:39\]: I think that\'s exactly the problem. And I think you said right, we basically have no clue to approach it.

**Nathan Lambert** \[00:47:46\]: But it\'s not that we\'re building on quicksand. Like the synthetic data is not quicksand because it\'s a real thing. But it\'s like if we can understand the core principles of it, then you can kind of use it more precisely and know when you need to have human verification.

**Tim Dettmers** \[00:48:03\]: So I think there are some clear patterns that you can use synthetic data to sort of quickly figure out if your model is wrong. But it\'s just very difficult to figure out if your model is right. And probably for that you need human data. That\'s sort of my intuition. And a lot of sort of problems we currently are not verifying if our models are wrong, which we probably do easily with synthetic data.

**Nathan Lambert** \[00:48:25\]: People in post-training are trying to do it more. A lot of the compute from RLHF being more is by filtering and verification. And a thing that we\'re starting to scratch with 2.0.3 is training on specific test cases for our model. So essentially if you have prompts where you can verify the answer, which almost seems like something that might\... It\'s like we\'re doing it for very general capabilities, like math, instruction following, the valves that everyone knows. What if RL training on test cases becomes something that works for every type of example? And then it\'s just a matter of you need to have verifiable prompts, which is something that I could see RL being used for specialization for that because the reward signal is nice. It\'s just a little bit of supervision. It\'s essentially if the model can generate the answer but not reliably, it will increase the reliability of it. If the model cannot generate it, you can\'t train it with RL to just generate it. It\'s just going to be gibberish. Yeah, that makes total sense to me.

**Tim Dettmers** \[00:49:29\]: I think this overall direction makes a lot of sense. You want to use synthetic data. It\'s so early.

**Nathan Lambert** \[00:49:35\]: It\'s just early. The RL stuff compared to DPO is interesting because it\'s generating different types of synthetic data. And in some ways I feel like the DPO thing was a good distraction where it\'s like you need DPO to make thousands of people realize they can do research on alignment. But also because everyone is going to come in and do this easy thing, therefore it over-indexes what the research community is doing on this thing that isn\'t the whole field.

**Tim Dettmers** \[00:50:07\]: Yeah, I mean the research community is sometimes a little bit slow to sort of change their direction. But I feel like with science in general, it can be slow but it\'s pretty reliable over time. I think we figure things out.

**Nathan Lambert** \[00:50:23\]: It\'s like a genetic process. It\'s just kind of how I describe it as like the march of progress. It\'s like a thing that\'s just\... There\'s a lot of noise and it\'s like a lot of scooping these days. It\'s like just validating results. Unless you\'re like extremely brilliant, almost any problem is going to be happening in some other lab at the same time because of the level of interest. Which is why I recommend people to invest in just being really good at getting your paper story and make it\... You have first impressions to your research. You have to capture the person that\'s thinking about looking at your work. That\'s right. Which is not what we are often trained. Okay, from instructions, also model merging. I think people finally accept that it is a crucial thing. What is your first exposure to this? I think I don\'t remember the title of the paper off the top of my head. But how did you become tuned into model merging?

**Tim Dettmers** \[00:51:16\]: So, yeah, I mean, we had a paper branch train merge. And there, the key insight was that if you\... So you want to train experts in this case. And you want to train them on different data. And the key insight was like if you train the experts on different data, then you try to merge them back together. Sort of merge the expertise into one model. It doesn\'t really work. And the insight was that, okay, if you start out with just a single general sort of expert trained on all the data, just for a little bit, then the optimization landscape settles down. Mathematically, it\'s sort of the spectrum of the Hassen settles into a sort of subspace. And so most of the optimization happens only a sort of tiny subspace in sort of the overall parameter space of the model. And how you can visualize it is like the model first doesn\'t know what it\'s doing. And then it goes down the lost canyon. And once it\'s there, it changes very little. And once it\'s there, then you might\... So once you train, and this only takes like 5% of the training time or sometimes even less. And after that, you can take this general expert and train on all kinds of different specialized datasets. And so if you do that, then in the beginning, you go down the canyon. And once you\'re on the canyon, and you specialize, you branch off a little bit in either direction if you train on different datasets. But you\'re still in the same local neighborhood. So now you can linearly interpolate and basically capture all the expertise gained from all the expert models. And just merge them together linearly or with a weighted average.

**Nathan Lambert** \[00:52:56\]: Is this ultimately like the parameters are capturing different things? It\'s like time for me to ask dumb questions about model merging. And it\'s like, we\'re just training these a little bit. So then like different parameters learn all of it. And then merging it together, you just keep a bunch of it.

**Tim Dettmers** \[00:53:10\]: That\'s right. Yeah. I mean, sort of in the end, I mean, all of that, there are these sort of optimization directions and sort of a subspace. It\'s not directly mapped onto axes. So it\'s not like you\'re optimizing in the, I don\'t know, a certain direction like math. And it\'s just this one direction or a set of directions. It\'s like, because it\'s not axis aligns probably all the parameters, but all the parameters are sort of pushed in a certain geometric direction. And so you have the same for sort of another sort of concept. And then, yeah, if you push sort of both, then you can sort of merge them back together.

**Nathan Lambert** \[00:53:47\]: Do you think this has consequences on things that we don\'t measure for the model? Like is this making the model slightly more specific at all of these things? Like it probably is. Like there\'s no free lunch and stuff.

**Tim Dettmers** \[00:54:00\]: Yes. So I think probably if you over-parameterized, I think the biggest thing is if you optimize multiple direction, and there is competition, then the structure needs to be in a way where there\'s basically no slack. Like every parameter is used and the value, the correct value is important. And so what we see from quantization is the longer you train, the more data you use per parameter, the more difficult quantization gets. And so this is a similar thinking that if you really over-train your model, it will be more difficult to merge and preserve all the capabilities.

**Nathan Lambert** \[00:54:46\]: So merging might work better at bigger models, assuming that we don\'t have that much more data?

**Tim Dettmers** \[00:54:50\]: That\'s right. Yeah. If you train on less data per parameter, my expectation is merging works better.

**Nathan Lambert** \[00:54:57\]: Do you think knowledge distillation is similar? It\'s like merging became popular recently. It seems like maybe it\'s like the 1 to 100 B range is the magic range where merging starts working. Does knowledge distillation happen to be similar?

**Tim Dettmers** \[00:55:08\]: So, I mean, for that, we probably need to talk a little about what these optimization landscapes mean. Yeah. I don\'t really know what knowledge distillation is.

**Nathan Lambert** \[00:55:15\]: Like knowledge distillation is a reweighting of the log problems in my brain, which is probably a simplification.

**Tim Dettmers** \[00:55:20\]: Yeah. Yeah. So if you think about normal neural network optimization, there\'s quite good literature that I actually really like that basically studies the dynamics of the Hessian, the spectrum of the Hessian over time. And so this is basically a study of the local curvature in the optimization space. So how quickly you change directions in the optimization space.

**Nathan Lambert** \[00:55:44\]: Hessian is like a matrix second derivative, right? Yeah. You can see it.

**Tim Dettmers** \[00:55:48\]: Just making sure I remember my fundamentals. And so the visualization that you can have is you\'re like going down a hill skiing, and then you\'re going down a track, and then suddenly the track bends, and then it bends again. That\'s basically the curvature changing. And you need to adjust the track to go down the hill and not along the hill or something like that. And so you basically study these changes in sort of curvature. And so what has been shown is that if you have a small data set, for example, in computer vision, you have like CIFAR 10, 10 classes, 10 labels, or you have CIFAR 100, 100 labels, then there are as many sort of primary directions as labels. So what you basically learn is one feature for one label. If you go to ImageNet, 1,000 classes, then it\'s no longer this one-to-one mapping. That\'s also why the lottery ticket hypothesis breaks down. It\'s like from your initialization, it\'s not clear where these dimensions are and how to optimize them. So you have much more dimensions than 1,000, but not that much more. And for language models, this explodes in sort of complexity. But this basically spans this optimization landscape. And how you can think about it is how it is evolving over time. And we also have some evidence for that. For example, just to give you an example, a visual example, it\'s like if you have a cat and a dog feature, these are pretty separate. But now if the model realizes, hey, they\'re different dog breeds, and hey, they\'re different cat breeds, then it\'s sort of a branching off a feature. So you have this tree of hierarchic features. If you want to learn a new one, you need to branch off. And that\'s mostly because if you have a random initialized neural network and you want to find an optimization path from basically the outputs to the inputs, it\'s almost impossible to learn a new connection through random weights. But it\'s very easy to expand the path that you\'re already on, the feature that you\'re already on, with some sort of slight modification of your existing feature. So the dog label becomes two different weights.

**Nathan Lambert** \[00:58:00\]: This is almost like why the recurrent, or what is the word for weight? Essentially in the model, you have this input goes around, and the input goes through the features. And it\'s like having the go around is nice because you have to learn like a delta on it. And you just add it rather than the whole thing. That\'s right. If you listen, this is like chaining podcasts. But on the Dark Hatch podcast with Anthropic or some other Anthropic media, they talk about this, which is like this. It\'s why it\'s really nice for the models learning because it\'s just a simpler space.

**Tim Dettmers** \[00:58:29\]: There\'s a nice paper about this that studied this. I think it\'s called ResNets do iterative refinement on features. Written by some colleagues.

**Tim Dettmers** \[00:58:42\]: So that is a natural way how features are learned. But it was entirely unclear what happens if you have a neural network that gives you sort of a distribution. So it\'s not like, here\'s some pattern that you need to learn. It\'s like, here\'s the distribution that you need to learn. And it\'s already very fine grained. So probably in this distribution, you already have the different dog breeds. And you get it from the beginning. So you don\'t need to learn the dog and then the dog breeds. You can learn all the dog breeds from the beginning. You can set up the optimization landscape so that you learn these features. And there might be a big benefit to learn a hierarchy. But there might also be a big benefit to set this hierarchy up from the beginning.

**Nathan Lambert** \[00:59:19\]: So this is almost like knowledge distillation models are going to be different. They\'re different numerically in ways that we don\'t know how to explain. And in our world, we see this as GEMMA 2 is not apples to apples with LLAMA 3 in terms of post-training recipes. It\'s like in our work, we\'re like, GEMMA is a strong model. But we just don\'t know how it maintains information. Like if MMLU will drop more and all these things. Just because it\'s a different space.

**Tim Dettmers** \[00:59:45\]: I\'m curious if you can say a little bit more about your experience there. From my understanding, I haven\'t worked very much with GEMMA or used it. But what I see from the community, it has very good benchmark numbers. But when people use it, then something feels off. Sometimes it works really well, but then there\'s some kind of gap. Why can\'t it do that?

**Nathan Lambert** \[01:00:10\]: I mostly hear similar things. That\'s like finicky to train. And that has now self-fulfilled into where we select our models and how we deprioritize it because we\'re just not confident in our recipe translating. And therefore, it\'s a risk to be like, we launched with GEMMA, but we\'re not as confident in how to explore there. So it\'s not substantial. It\'s just like, this is something an academic could do. What are the best practices between GEMMA 9b and LLAMA 8b? What are the differences? That\'s right.

**Tim Dettmers** \[01:00:44\]: That\'s, for example, a good question to explore if you don\'t have much compute.

**Nathan Lambert** \[01:00:50\]: The last one of these architecture or method series is recurrent state-space models. I find state-space models because the math brings me all the way back to my EE linear systems days. But I don\'t know if that translates to how the neural nets actually learn because they have the observability matrix and stuff in the math, which is nice. Do you see that that, is that substantially more, is it just extremely different and we\'re just going to see?

**Tim Dettmers** \[01:01:17\]: I don\'t think it\'s that much different from recurrent neural networks. I think it\'s not about the computation, but the learning patterns. And I am currently not super convinced. I worked on architectures for like two years at Meta. All my projects failed because nothing really beat transformers. And sometimes I see papers where people present ideas that I worked on and I know like, yeah, this will not work. I didn\'t work on state-space models.

**Tim Dettmers** \[01:01:55\]: And a colleague asked me like, hey, you said you don\'t believe in state-space models. Can you look at this plot and tell me like, what doesn\'t look good here? And I look at this plot and I\'m like, I don\'t know. It\'s like, I have this feeling if I see this plot. And I looked at so many plots that these trends don\'t look good. And so I can\'t point a finger to it. But I think at this certain point, it\'s just transformers will still be better. And that\'s what we\'re going to use.

**Nathan Lambert** \[01:02:23\]: That\'s my like, all branch, all extend is like, oh, yeah, chat.gbt will know to route to a state-space model if it\'s a 10 billion length document. And it\'ll be like 0.1% of queries into chat.gbt. It\'s like, how many Google queries do you have to paste in a PDF? Like, not that many. So that\'s kind of like, there will be a suite of models. And honestly, O1 is like one of those niche things too. So if I\'m going to say that state-space models are small, like so is O1 in that regard. That\'s like what I\'m interested in doing in 2025.

**Tim Dettmers** \[01:02:54\]: I mean, maybe just to add to that, for me it\'s like, I have now used language model more and more and more. And what I see is it\'s just really important what information you provide. And long context models never work. Even the best ones, they are really bad long context. And the solution is not take your data, pass it through this long context thing. You need to pre-process your data and give the right data to the model. I think that\'s the right approach. And from my experience, that yields much, much, much better results. And so I think that\'s what you want.

**Nathan Lambert** \[01:03:32\]: Well, did you try Notebook LM?

**Tim Dettmers** \[01:03:34\]: I tried it, yeah.

**Nathan Lambert** \[01:03:35\]: It\'s almost like how to best interweave rag with long context.

**Tim Dettmers** \[01:03:40\]: I think, yeah. So this is, for example, a system where you say like, hey, this is a product. Hey, people want this.

**Nathan Lambert** \[01:03:47\]: I think they use multiple models and multiple model passes. Like they use Gemini, but they\'re doing weird things under the hood, which is why the open source replications are not going to cut it.

**Tim Dettmers** \[01:03:55\]: But I think this is exactly what the future will look like. Complex systems. You will not have like O1 where you\'re like, here\'s my data, please solve things. It\'s like, no, that\'s not going to cut it. You have like complex interweaved things. And I think that actually makes open source more competitive because you can\'t launch complicated products. But it\'s like, well, this is the back to the beginning.

**Nathan Lambert** \[01:04:21\]: It\'s like we have like LangChain and things as an open source. And everyone loves the shit on LangChain, but it\'s like how do you evolve LangChain at all into tooling that can quickly spin off Notebook LM? Like what is the infrastructure where the config file outputs Notebook LM? Like that is just, I don\'t know if there are any software stacks that are open source that are that complicated. Maybe Linux, maybe an operating system is that complicated.

**Tim Dettmers** \[01:04:47\]: Yeah, yeah. I mean, I\'m working on that. So I will take some time. I\'m not started yet, but I\'m designing the system basically. But yeah, I think we are at an early stage. That\'s a good advice for people too.

**Nathan Lambert** \[01:05:05\]: It\'s like assume that it is early and assume that your academic career is not a two year bus cycle that you need to race through. Oh yeah, oh yeah.

**Tim Dettmers** \[01:05:12\]: I think a main problem also in that space and sort of when it goes to complex system agents and so forth is like we haven\'t really defined the problems. When I talk to, when I tell most people that, hey, I work on open source agents, the first question they ask me is like, what are agents? What is your definition? Yeah, I relate.

**Nathan Lambert** \[01:05:34\]: What is an agent to you?

**Tim Dettmers** \[01:05:38\]: I don\'t know. I had a definition and now I feel like it\'s less and less useful. I think a definition that makes sense to me is sort of an agent is sort of a system of multiple steps that sort of makes a plan on its own, executes that plan.

**Tim Dettmers** \[01:06:00\]: I think that\'s how most people would define it. If you have that definition, I would say I\'m not working on agents because I think that\'s not what the future will look like. I don\'t think that works.

**Nathan Lambert** \[01:06:15\]: It\'s much more like a system than an agent in some ways where there\'s like rule following and you help guide it to do, be really good at a specific thing.

**Tim Dettmers** \[01:06:23\]: Yeah, I think, so you mentioned lang chain. There\'s also LangGraph. LangGraph, people like it much more because you take the planning and execution away from sort of the agent. It\'s more like a pipeline where people can design more carefully sort of engineered things.

**Nathan Lambert** \[01:06:39\]: What is the difference? What would be the core technique?

**Tim Dettmers** \[01:06:44\]: It\'s more fine grain control. So you can say like, if certain evaluation has certain value, go along this branch. Whereas an agent, you would say like, here\'s my prompt and do what the answer says. And it\'s like, it makes no sense. Yeah, it\'s a mess.

**Nathan Lambert** \[01:07:04\]: Okay. Anything else you want to add? I think that it\'s like the most interesting thing is like, you seem very bullish on open source winning. Oh yeah. And it\'s like, it\'s good to have this optimism. And it\'s, how do we make this more of a reality? Because like we talked about meta not releasing new models. And it\'s like, how do we make open source AI much more of a multi-stakeholder thing than just meta? Like I think most people, like we\'re weird people that are deep in the weeds of this. Most people think it\'s just llama. So like, how do we bridge that gap? Yeah.

**Tim Dettmers** \[01:07:40\]: I think if you have the mindset that it will be complex systems, it will not be a model receiving input. And if you have, this is sort of thinking is like, you need something that\'s useful for people. You don\'t want O1 where it looks shiny and nice and it can do reasoning, but it\'s not super useful. You shouldn\'t do that. You shouldn\'t try to replicate O1. You shouldn\'t try to work on a good model. You need more complex things. And so once you have this mindset and get away from like, yeah, I don\'t develop models and I don\'t, and a focus is like, I try to build something that\'s useful. Then you go on the notebook sort of LM direction, which is easily doable by open source. I think it\'s a bit more complicated and you need to piece things together and if you don\'t have the open source. It\'s almost like we need people to experiment.

**Nathan Lambert** \[01:08:37\]: And when you obviously are onto something that can work, but has limitations that are just like rough edges, not fast enough. It\'s like ignore all the things that obviously get better in the architect technology. And it\'s like, we need people that are experimenting and that can become collaborative through open experimentation. Yeah. Yeah.

**Tim Dettmers** \[01:08:58\]: Yeah. So this is like,

**Nathan Lambert** \[01:09:00\]: that\'s like the summary of our conversation. Like be more creative on your approach and therefore the benefits will come eventually. Yes.

**Tim Dettmers** \[01:09:06\]: Yes. I think, I think that\'s, yeah, that\'s a good takeaway. That\'s fun.

**Nathan Lambert** \[01:09:11\]: Okay. Well, thanks for sitting down and doing this. I don\'t, I don\'t have more questions. I\'ll slowly get off and turn off the various microphones that are going on. Yeah.

**Tim Dettmers** \[01:09:20\]: Yeah. Thank you so much again for having me. I mean, one thing that I could add, I could talk a little bit about GPUs and quantization. Do you want to?

**Nathan Lambert** \[01:09:29\]: I\'ll let you, you can riff. Those are good.

**Tim Dettmers** \[01:09:31\]: So, so one thing that people ask me like, which GPU should I buy? And so I have here a certain perspective that might be helpful for people. I think it\'s not fully validated yet, but sort of, I mean, you were mentioning hardware gets better and better. Yeah. I think we\'re close to the end. I think the next generation of GPUs will more or less be the last generation of GPUs that we get. There\'s just challenge of improving things. Do you mean on peak flop?

**Nathan Lambert** \[01:10:01\]: Or are you also thinking on flop per watt?

**Tim Dettmers** \[01:10:04\]: It\'s more like flop per watt. And density will not improve much. It\'s more like, I think what will become more important is networking, data center level efficiency, but not necessarily GPU or device level efficiency. And there are just a lot of physical problems. There\'s still a little bit room for sort of improvements, but the computational patterns are pretty optimal. And if we look at the scaling behavior of quantization, which was basically the main thing that improved efficiency, you had tens of cores, and then you went from 32 to 16 bit. 8-bit didn\'t work quite out. With Blackwell, we can get 8-bit working. But then\... What about 4-bit?

**Nathan Lambert** \[01:10:51\]: Like, does 4 and 2 really? Or are those just\...

**Tim Dettmers** \[01:10:53\]: I mean, research says, like, it will not happen. Well, it\'s the silly 1-bit paper.

**Nathan Lambert** \[01:10:57\]: That\'s the type of paper where I\'m like, oh, have your fun, but it feels fake.

**Tim Dettmers** \[01:11:00\]: So, I mean, the thing is, a couple papers point to this, and I know a couple more papers will come. The main thing is, if you train, as you train longer and longer, you have more data that you basically train on per parameter. This determines the bit precision that you need. 1-bit is good if you train a small model for not a long time, or a large model for\...

**Nathan Lambert** \[01:11:24\]: There might be cases where those further quantization matter, but it\'ll be in lower data regimes.

**Tim Dettmers** \[01:11:30\]: Or you have a bigger model, but at some point it becomes a trade-off. If you have a bigger model, you need more compute. And so if you have more compute in 1-bit, or less compute in 8-bit\...

**Nathan Lambert** \[01:11:38\]: Does that mean, like, the 16 to 8 range is where most of the optimums lie?

**Tim Dettmers** \[01:11:44\]: Yeah, you can get 6, maybe 4. I mean, 4 for inference is pretty good. But 4 for training, it will be quite questionable. And, I mean, if our models just get more compute-intensive, I think the bit precision will actually increase. I have 6, it\'s already borderline. I think 8 will be definitely possible. With Blackwell, no problem at all. So I think most training will be done in 8-bit when we have Blackwell. But, yeah, I think we can\'t squeeze quantization much more. Yeah, I\'m not going to push you at all on this.

**Nathan Lambert** \[01:12:21\]: I just find it fascinating, and people find it fascinating.

**Tim Dettmers** \[01:12:25\]: And the other thing to add is, Blackwell will have particular hardware features for quantization that makes it much easier. It\'s comparable, like, we had FP16, but it was very difficult to use for training because you need to use mixed precision because you have problems with your loss basically vanishing or exploding, and so not being captured by the data type. And then we had switched to BrainFlow 16. Suddenly people are like, oh, I can train without any problem because now you have the entire range.

**Nathan Lambert** \[01:12:59\]: Yeah, it\'s a change of the range.

**Tim Dettmers** \[01:13:01\]: And so Blackwell will have a similar change for quantization, so 8-bit will be easy. You can get 8-bit working if you do it really well.

**Nathan Lambert** \[01:13:08\]: Why does this only happen on Blackwell and not the previous version?

**Tim Dettmers** \[01:13:11\]: Because they have hardware support, and it\'s automatic.

**Nathan Lambert** \[01:13:16\]: So you could do it, but it would be very slow. It would be slow, and it would be hard.

**Tim Dettmers** \[01:13:20\]: So, I mean, if I would work on this sort of problem, I probably would need a couple months to really figure it out. 8-bit training is possible, but if you do it with software, it will not give you huge speedups, and it\'s just difficult. And with Blackwell, it\'s like, oh, yeah, pick 8-bit, and everything\'s working.

**Nathan Lambert** \[01:13:44\]: Wait, have you used these? Have you actually used these new GPUs? I know their technical specification

**Tim Dettmers** \[01:13:50\]: and then some sort of secrets about them. I mean, like, I also could get it.

**Nathan Lambert** \[01:13:55\]: Like, once you are connected to the right people, you can, like, learn these things, and that\'s right up your alley, so it\'s interesting. Yeah, I mostly like them. Quantization is a feature that I get to use, and I\'m not in that area, so I just take the benefits as they come.

**Tim Dettmers** \[01:14:10\]: It\'s like one of my things is, like,

**Nathan Lambert** \[01:14:11\]: there will be weird benefits that regularly come, and it\'s good to be fast-adopting things, but, like, otherwise I just let people do these things. And it\'s great.

**Tim Dettmers** \[01:14:19\]: Yes, but as I mentioned sort of in the beginning, it\'s like quantization is one of these factors. We now have maxed out the factor pretty much, so we should look for other factors. But it gets more and more difficult. Like, we cranked up the multiplier on a lot of things, and we quickly run out of multipliers.

**Nathan Lambert** \[01:14:38\]: It\'s so interesting because you are one of the people that everyone recognizes for quantization and other compute research, but you\'re like, I\'ve needed to, I\'m starting my professor career, and I\'m going to be doing creative things because that\'s where the future lies. It\'s like models, like, in some ways you\'re also de-risked because if model scaling works, you get the benefits anyways. Yeah, yeah, yeah.

**Tim Dettmers** \[01:15:02\]: But now, yeah, that\'s, I mean, I worked on quantization for such a long time, but it\'s time to move on. The problem is kind of solved, and we need to move on to different problems. Yeah. Anyway, that was great.

**Nathan Lambert** \[01:15:18\]: Thanks for adding this on. Any other wisdom to drop? No, I really enjoyed this conversation.

**Tim Dettmers** \[01:15:23\]: It was fun. Yeah, it\'s fun.

**Nathan Lambert** \[01:15:25\]: It\'s good to just have a forcing function to talk about stuff, and it\'ll be fun working together. I\'m sure we\'ll cross paths for next year. Yeah, I\'m looking forward to that.
