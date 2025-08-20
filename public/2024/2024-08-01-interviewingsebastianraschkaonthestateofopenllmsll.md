---
title: "Interviewing Sebastian Raschka on the state of open LLMs, Llama 3.1, and AI education"
subtitle: "Interconnects interviews #4."
date: 2024-08-01
type: podcast
audience: everyone
visibility: public
post_id: 147219115.interviewing-sebastian-raschka
email_sent_at: 2024-08-01T15:01:27.576Z
---
This week, I had the pleasure of chatting with [Sebastian Raschka](https://sebastianraschka.com). Sebastian is doing a ton of work on the open language model ecosystem and AI research broadly. He's been writing the great [Ahead of AI](https://magazine.sebastianraschka.com/) newsletter (that has the biggest audience overlap with Interconnects, at 26%, so a lot of you know him) and multiple educational [books](https://sebastianraschka.com/books/), all on top of being a full time machine learning engineer at [Lightning.ai](http://Lightning.ai), where he maintains [LitGPT](https://github.com/Lightning-AI/litgpt), which he described as being like Karpathy's NanoGPT, with slightly more abstractions.

This conversation mostly surrounds keeping up with AI research, the state of the open LLM ecosystem post Llama 3.1, and many narrow topics in between. I learned that Sebastian used to be an Arxiv moderator, which gives some simple color on how Arxiv and sifting through thousands of papers works. We cover a lot of ground here, so I hope you enjoy it.

Listen on [Apple Podcasts](https://podcasts.apple.com/us/podcast/interconnects-audio/id1719552353), [Spotify](https://open.spotify.com/show/2UE6s7wZC4kiXYOnWRuxGv), and [where ever you get your podcasts](https://podcast.interconnects.ai/subscribe). For other interviews, [go here](https://www.interconnects.ai/t/interviews).

### YouTube

:::::::: {#youtube2--q79uzz1Wik .youtube-wrap attrs="{\"videoId\":\"-q79uzz1Wik\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=-q79uzz1Wik){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

### Chapters

-   \[00:00:00\] Introduction & Sebastian's background

-   \[00:04:28\] The state of deep learning and language models in 2018

-   \[00:08:02\] Sebastian\'s work at Lightning AI and LitGPT

-   \[00:12:23\] Distillation and its potential in language model training

-   \[00:14:14\] Implementing language models and common pitfalls

-   \[00:18:45\] Modern architectures: Mixture of experts models, early v. late fusion multimodal

-   \[00:24:23\] Sebastian\'s book on building language models from scratch

-   \[00:27:13\] Comparing ChatGPT, Claude, and Google\'s Gemini for various tasks

-   \[00:38:21\] Vibing and checking new language models during implementation

-   \[00:40:42\] Selecting papers to read and moderating Arxiv

-   \[00:45:36\] Motivation for working on AI education

-   \[00:52:46\] Llama 3 fine-tuning

-   \[00:57:26\] The potential impact of AI on jobs in writing and education

-   \[01:00:57\] The future directions of AI

### Transcript

Built with [smol-podcaster](https://github.com/FanaHOVA/smol-podcaster) and with love of Latent Space.

**Nathan Lambert** \[00:00:00\]: Hey, Sebastian, welcome to this kind of interconnects, normally researcher interviews. You were a professor, so that definitely counts. You do a lot of different things these days. Let\'s get talking into language models. Welcome. Yeah.

**Sebastian Raschka** \[00:01:35\]: Thanks so much for the invitation, Nathan. I\'m a big fan actually of the interconnects newsletter, so I\'m hoping we can have some fun chat about research, LLMs, and what\'s hot these days, basically. Yeah.

**Nathan Lambert** \[00:01:48\]: I have a little section on the end, which is keeping up with AI research, writing about AI and process, because you do so many things, but I kind of want to jump into how you got to AI, because you have an interesting career path. So you were a professor at Wisconsin Madison for years. I saw in statistics, which \... I also went all the way back to find your PhD thesis, which was uncovering hidden patterns of molecular recognition. So this was a while ago, and is this kind of \... Can you explain your background and how you got into AI? I\'m guessing it\'s through computational statistics or something like this.

**Sebastian Raschka** \[00:02:24\]: Yeah. Close. So yeah, you did some research there. Interesting. So yeah, it\'s been a long time since my PhD thesis. This is maybe seven years now. And back then, it started even earlier when I got into AI, that was like, I would say 2012-ish. I was in grad school and I was taking a statistical pattern classification class. And in that class, yeah, the star of the show was basically naive Bayes classifiers, or in general, Bayesian methods for pattern recognition. And from there, I kind of really got into machine learning. So there was, I would say, more statistical-based, but it was all about classifying things. And then I think it was also right about the time where Cozera was launched, and I saw Andrew Ng\'s Cozera class. That was, I think, the first class in 2011-12 back then. And yeah, that\'s basically how I started from statistical pattern classification into machine learning. And I applied that for computational biology problems like molecule and drug discovery, like pharmaceutical drug discovery. And yeah, from there, I joined at some point after my graduation, the University of Wisconsin in Madison, where I was in the statistics department, but I did mostly deep learning research, essentially. I was the only one basically doing Python, deep learning, machine learning stuff. So yeah.

**Nathan Lambert** \[00:03:48\]: What year was this, and what did it look like at the time?

**Sebastian Raschka** \[00:03:52\]: That was around 2018, I think August 2018, when I joined the department. And yeah, I mean, so it\'s the statistics department, but my work was technically all machine learning and deep learning. I mean, a lot of students were really excited about learning machine learning. I think it was just around the time where it got really popular. And yeah, I was teaching machine learning and deep learning classes as well. They were always like, you know, full and crowded, like a lot of students were excited about that. Also, in general, like the time learning about Python, machine learning, data science, all these topics.

**Nathan Lambert** \[00:04:28\]: It\'s, I mean, it\'s very interesting because I was a student, I was a grad student at this time or that time in like 2018. That\'s what deep RL was really taking off. And it probably feels like that probably felt kind of like the language model thing was like as a student at the time, where it\'s just like, there\'s so many people in all these classes. And now language models have more of a real world application, but I think as a student, it probably feels so, so similar. Yeah.

**Sebastian Raschka** \[00:04:50\]: So also back then, if I may say that it\'s like large language models already existed. I think the GPT paper, was it 2018? Something like that?

**Nathan Lambert** \[00:04:59\]: Yeah, 2018 or 2019. Yeah. For GPT-2, I think.

**Sebastian Raschka** \[00:05:04\]: Remember covering, like I had a whole hour or two hours on large language models back then, but it was all focused on BERT models and basically also using them for more like classification tasks. Now, I would say maybe a lot of business problems still evolve around classification, but everything else is basically generative, generating text, generating images and stuff. So it has changed a lot.

**Nathan Lambert** \[00:05:28\]: Yeah, for sure. It\'s like a sequence of like, is it like the transform, is it like Elmo, BERT and the transformers are probably the things that you\'re talking about all the time? Just very interesting. I think Yitay had this, did you read Yitay\'s recent blog posts on language model architectures and kind of walked through why encoder decoder is no longer in vogue? Did you see this?

**Sebastian Raschka** \[00:05:51\]: Yeah, I think I haven\'t seen the article, but I remember having discussions with people about that recently. I mean, I think there was actually, it\'s interesting. So I think T5, if you would train it and fine tune it, it would still be a really good model for sequence to sequence tasks, like language translation and stuff like that.

**Nathan Lambert** \[00:06:10\]: Yeah. Cohere for AI did this with AYA. They used T5 for their first AYA version, which most people were like, oh, they\'ve Cohere branded it so well, but no one realized they\'re using T5.

**Sebastian Raschka** \[00:06:21\]: See, I even didn\'t know about that. And so also on that note, I would say there was something else I wanted to say. So then there\'s also still the classification thing and using LLMs for classification. And it was also usually either a bird like encoder, or you could also use an encoder decoder, but mostly an encoder. But I\'ve seen also recent papers using just decoder models for that. Just basically removing the, I saw two papers on that actually, like removing the causal mask. So basically reverting it back to an encoder using LLMA and then removing the mask. So in that sense.

**Nathan Lambert** \[00:06:59\]: And it works well as a classifier. You can just kind of use it. That\'s awesome.

**Sebastian Raschka** \[00:07:04\]: I mean, you could even do that without removing the causal mask. So you could just tune the last token basically, but yeah, if you remove it, yeah. They found that you could use probably the first token even, because if you have the last token, you don\'t, you have to have padding always because you have to pad it to the longest sequence. Otherwise the last token would be a different one in each training example. And so in this way you could use an earlier token basically, and then keep it fixed.

**Nathan Lambert** \[00:07:30\]: Yeah. Yeah. Now with your work at Lightning AI, do you do a lot of these things like hacking around with language models? Because I think it\'s kind of an underexplored space where just like people remove layers and plug things together. I think there was like, when merging was just getting going, there was like Franken Llama 2, where somebody made like a Llama 2 30 B by just chopping layers and stuff together. There\'s so much unexplored signal there that I just, do you have your, have you ever looked at these things or you don\'t do that much?

**Sebastian Raschka** \[00:08:02\]: I must say I\'m not a big fan of merging. Maybe I\'m just not good at it. I rather prefer fine tuning, start changing things or training and fine tuning things. So yeah, I do a lot of this type of hacking. Sometimes voluntarily, sometimes involuntarily, because I make a mistake or something or like, because at Lightning I developed this library, LitGPT, which is an open source library, pre-training, fine tuning and serving and deploying LLMs. But it\'s basically a from scratch implementation. You can think of it as a NanoGPT from Andrej Karpathy, but for all types of LLMs, like Llama, Gemma, PHY, all of them. But the focus is also like NanoGPT is on readable code or like keeping it relatively simple. Of course it gets a bit more complex there when you add multi-GPU training, tensor parallel, fully sharded data parallelism and stuff like that. So if you add all these settings, it gets a bit more complicated, but the focus is still on having a code base that you can easily work with. And in that context, it\'s very easy to remove layers and change things. I mean, yeah, so that is usually, I build it like for colleagues at Lightning, but also like open source community, but then also for myself to tweak things, to change things and stuff like that. So yeah, I should also say, it\'s not just me, it\'s Carlos and Adrian who started this library. Currently I\'m like the main person maintaining it, but a lot of people contribute to it. So it\'s actually a nice playground.

**Nathan Lambert** \[00:09:41\]: There\'s kind of two follows odds for this. One is like, what part of the language model training stack, if somebody is going to start with libgpt or HuggingFace or whatever, like they\'re trying to fine tune a model, you can do an example. And then what is the thing that they should do to go like one level deeper to learn how these things work? Because you\'re saying with libgpt, you can do all these different architectures. I don\'t know if I would recommend architectures, but it\'s a good way to learn how like the attention implementation and how different layers are shaped and things like this. Is there different areas you\'d recommend people to look at?

**Sebastian Raschka** \[00:10:14\]: Yeah, I would actually, okay. So it\'s like a shameless plug, but in my book, I have a book where I do this step by step, the implementation. And this is for only one model, like a simple model, a GPT-2 model. Because it\'s like the, I would say the one that started all of this, right? Like the main architecture and everything else is kind of like a derivative almost of it. So I would think in a good way that it is making tweaks and improving things, but basically starting with one architecture, like you said, not looking at different ones at first, and then just understanding what is, I would say the best way is what is the input data here? How does it look like? What does go into the LLM and really how does it pass through the layers? And then from there, okay, we understand how a model learns to generate one word at a time and then going from there to instruction, fine tuning, and then even like alignment with a DPO, for example. So doing like all these different lifecycle things from implementing one architecture, pre-training, fine tuning, aligning, and then from there, I think it\'s a useful or interesting exercise to see how different architectures make slightly different choices, like replacing the Gelu activation with a Silu activation or pre- and post-layer norm and like these like nuances, changing the number of heads or number of layers. And yeah.

**Nathan Lambert** \[00:11:38\]: Yeah. I mean, in industry, everyone kind of is converging to similar things or like people converge to a similar recipe and then they stick with it for infinity. So like each of the orgs have these recipes that it\'s too risky to change and like AI2 are like still converging at a recipe. So we\'re like learning things that the Llama team does and it\'s like RMS norm and they think it\'s very important or like these different things. And I wonder how like the open community is going to converge on pre-training things. So like what scale of models do you recommend people train for your book? Are they training like the hundred million scale GPT-2? Is it smaller? Because I think in Colab, you can fine tune maybe with Laura, a 7b model, I think. Is that true?

**Sebastian Raschka** \[00:12:23\]: Yeah. So this is true. But I think for Laura, if you want to fine tune 7b model, you would need, I think, bits and bytes of quantization, the normal float for like some quantization. But yeah. So for the, or maybe going one step back for the book, it\'s really the smallest model, like the hundred, what is it, hundred something million. But I also have settings. If you like, if let\'s say your machine permits, use the larger version. So there are four larger versions, like 300, 700, and 1.5 billion. But it\'s really up to the reader. I have all the examples with the smallest one so that it even runs on a MacBook Air. So on this podcast, I\'m here on my small MacBook Air and all the models train in a few minutes fine. Of course, I\'m not doing the whole pre-training for that. You would need a GPU for a week or maybe I would say maybe even longer than that now. I mean, it depends on the GPU, of course, but H100, maybe a week. But also the other reason is yeah, in practice, you would probably use pre-trained weights and then you can find, so you can do continued pre-training and then fine tune. So the focus is basically understanding how the pre-training works, then loading pre-trained weights. But then also the fine tuning is like the full, the full thing, like doing it to fine tune a classifier, but also instruction fine tuning essentially. And that doesn\'t take too long. I would recommend using a GPU, but it would technically run on a CPU. And get back to the question you had with a 7 billion model for that one A100, I would say yeah, one A100 would probably work for a 7 billion model. But you can also, if you have Litt-GPT or if you use Litt-GPT as a setting, you can set the number of devices and shard it over multiple GPUs. Yeah.

**Nathan Lambert** \[00:14:14\]: I mean, all of this stuff is getting so much easier. I think, I don\'t know, when did you start writing this book and all of these chapters? Because I\'ve seen the GitHub, I haven\'t looked at when it started.

**Sebastian Raschka** \[00:14:23\]: Actually longer than you might think. It took a long time. It\'s almost, at this point, one and a half years approximately.

**Nathan Lambert** \[00:14:30\]: Because at that time, like a 1 billion parameter model, like what was the state of the art 1 billion parameter model a year and a half ago? Some random model. But today, like people are trading 1 billion parameter models for 15 trillion tokens. So the fine tuning that you can do there is getting extremely good. And I\'m going to guess that people are going to start training even smaller models with these distillation losses. So have you looked at distillation at all? I think it\'s full on coming in the next six months. We can shift it to like the LLAMA3 and the state of the open ecosystem section, because it kind of goes in. It\'s like LLAMA3 was not distilled. It\'s a specific loss function. I hate it that there\'s synthetic data came around and people call, I was on this paper, the Zephyr paper, the title is Direct Distillation of Language Models. But now the technical definition of distillation, which is like knowledge distillation from a teacher is becoming popular. So the whole synthetic data and alignment and everything is like screwed in a doubly defined word.

**Sebastian Raschka** \[00:15:30\]: So basically what you\'re saying is that people who just use synthetic data refer to it as distillation because it\'s from a larger model. Yeah. Yeah. Yeah. Confusing. I think Gemma too did that actually recently. So that was an example where they did that. And I do think, you know, I think it\'s also coming. So I have for my book, that\'s like the core chapters I have, but I have a whole long list of bonus material that I want to cover and distillation, knowledge distillation is one of them. So this will be something over the next few years, but you know, doing tutorials on those and yeah.

**Nathan Lambert** \[00:16:04\]: Because I think people can actually use it as a thing. So how distillation works, I\'ve thought about implementing it, but as it works is that if you have a fine tuning corpus, you get all the predictions from your big model. So all the log probabilities from your big model and you store them in memory. And then as you\'re training the model you\'re training, which is smaller, you essentially weight them by those predictions because you store them from memory. So you don\'t need to store the big model in memory when you\'re training. So I think people should be able to like, or someone will upload a data set file of like a giant log probs of Lama 405B and that people will just try to fine tune from it. I\'m surprised that Lama 3 didn\'t use it, but I think it\'s just because they\'re focused on scale and data more than any fancy things.

**Sebastian Raschka** \[00:16:49\]: Yeah. And I think the, I can, I think I probably know why, but also, yeah. One thing is I should, one should also add is why I think it\'s also becoming more popular is like Lama 3.1, they just allowed doing that. I think before it was according to the license, technically not allowed to use Lama 3 models to improve other models, but now, now we can. So I think, like you said, it\'s probably going to be a hot topic, but I do think they didn\'t do that because the 405B Lama model just finished, I think. So I think, I mean, if you think back, they shared the Lama 3 model, it\'s like, I don\'t know, half a year ago or something, many months ago. So I think it\'s really more like, yeah, it hasn\'t finished training, but maybe for Lama 4, we will see more distillation using the 3.1 model for that.

**Nathan Lambert** \[00:17:38\]: Yeah, it\'s more architecture things. So for while we\'re talking about distillation, almost like Cloud Flash or Google Gemini Flash is confirmed as distillation. And it is very likely that Cloud Haiku and GPT-40 mini are distilled in the technical sense of the word, which is like, I think it\'s obvious that that works on pre-training. And I think there will be a breakthrough fine tuning model, kind of like the likes of Zephyr, Starlang, I\'m forgetting more names, but ones that really reach the narrative from fine tuning on distilled data. I think that\'ll come in the next six months. So honestly, I\'m telling the people I work with, we should try to do this before something new, because it\'s so obvious now.

**Sebastian Raschka** \[00:18:22\]: One thing I\'ve seen also a trend, I wouldn\'t say backwards, but a thing that doesn\'t seem to be that popular anymore is a mixture of expert models. What do you think about that? Is that like something like that was like a fad and now people don\'t, you know, they explore other things like distillation. I mean, you could do both, but it feels like a mixture of experts is not as hot anymore

**Nathan Lambert** \[00:18:45\]: somehow. I don\'t know.

**Sebastian Raschka** \[00:18:45\]: What do you think?

**Nathan Lambert** \[00:18:47\]: There\'s two things. Small mixture of expert models are definitely coming out. Essentially, you get a fixed improvement in flop efficiency at pre-training. So essentially, if you\'re going to pre-train like an X billion parameter model with mixture of experts, it\'ll go like 40 percent faster or some pretty appreciable number. There\'s a lot of rumors and discussion that scaling up mixture of experts models is really hard from a stability point of view. So a lot of these open people, you could get it started and we\'re playing with these AI too. So we want to play in the mixture of experts space as well. And doing a small model works, but there\'s a lot of headaches. I think like some of the friends at Databricks Mosaic ML have been the clearest about this. It\'s just like you do not, like you at AI too, do not have the engineering throughput to deal with the headaches that comes from mixture of experts. So I think there\'s still clear signal from industry and people and like, I mean, Deep Seek\'s releasing MOEs. I think Quen has a small MOE and these are pretty good models. But I think it\'s a really heavy engineering lift to get to mixture of experts to work. I like GPT-4 scales. I expect Meta to figure it out. I think it\'s just on their list and they figured out dense first. The thing I\'m more interested in for GPT-4, I don\'t care if it\'s mixture of experts. I think they have the compute to do either way. But for Llama-4, God, all the numbers throw me off so bad. But I think that OpenAI and Google might be slightly ahead by having the early fusion model. So essentially with these multimodal models, there\'s the concept of early versus late fusion. The first visual models that people were playing with the GPT-4 were this late fusion. And now like GPT-4.0 is early fusion. And it seems like Gemini is probably early fusion, which means they take in direct audio, video, text directly at the input, the training data changes. And I don\'t know how much of a heavy lift it is to get that to work. I think that might be the bigger change. And that might be harder for Meta to catch up on than anything else. But no one\'s really talking about it.

**Sebastian Raschka** \[00:20:58\]: But also here, I think that is something I feel like others have. I mean, I remember even like last year, there were a lot of papers with a late fusion thing, like I think Llama adapter papers and stuff like that, like retrofitting the models. But yeah, I haven\'t seen that much focus on that from Meta. But I mean, they had a section on that in the paper, but it felt almost like an afterthought. I don\'t know. It\'s like where, yeah, I think maybe there\'s a different team at Meta that works on

**Nathan Lambert** \[00:21:26\]: that. There is a Chameleon team that was doing this, and I think a lot of them have left. My question, essentially, that I want to debate and I don\'t know the answer to is like, because essentially it takes so much different data pipelines. So you have to have a much clearer balance between video images and audio and text when you\'re training early fusion than with late fusion, because you just add a bunch of images at the end. And like if that data curation step is going to be a big bottleneck for kind of shifting and if Google and OpenAI have an advantage by just scraping YouTube, like Google obviously can\'t scrape YouTube and I\'m not saying that they are, but like if it becomes a way that you can get more data and like GPT 5.0 is the first model that OpenAI releases, then I\'ll be like, OK, the GPT 4.0 thing was just a pivot. And I actually think this could happen. I don\'t put this at like a one percent probability. I could see this as being what the labs are betting on. It just takes so long to spin up this entire new pipeline of training.

**Sebastian Raschka** \[00:22:25\]: But one question here is going back to a point you mentioned earlier regarding the knowledge distillation where you can just precompute all these things, you could technically do that also just once for the whole data set. Let\'s say you have a very good image encoder, audio encoder. You would never have to redo this if you do it well. Right. I mean, it would be something you do it, take care of it once and then you pass it just as tokens to the to the other team, basically.

**Nathan Lambert** \[00:22:49\]: Yeah, probably. I don\'t know. I\'m not like I don\'t have as much insight into really advanced pre-training practices as I would like. I\'m mostly of a similar boat of like fine tuning models and playing with things because I\'m trying to play like, have you played with Llama 3405b at all? For context, the recording is like, what is this, like a week after, like six days after. Like I haven\'t gotten it set up, but I\'m really curious. Like I don\'t have clear expectations on how the open source community, like the open language model ecosystem kind of evolves from here with these new Llama models, the new Mistral models. It feels like a total, from like a technical and a policy perspective for me, it feels like a pivot. I think the educational side of things, it\'s actually more of the same. Like we knew we knew this was coming, but it just it feels like it could be qualitatively different going forward. Do you see anything? Have you tried anything?

**Sebastian Raschka** \[00:23:45\]: Yeah, I did actually try the Llama 3.1 models. I, when they came out last week, we added them to Litchipiti. I took care of the eight and 70 billion models. And my colleague Adrian, he also added support for the 405 billion models. So just briefly trying it, it looks really good. So the thing is with a 405 billion model, it\'s a bit tricky. So I think the problem here is, of course, it\'s free. Everyone can use it, but in a sense it\'s still expensive to run it because you need, so we were running it with bits and bytes of quantization, like a normal float four on eight H100s. And this is expensive, right? I mean, eight H100s, it\'s probably more than a hundred bucks an hour.

**Nathan Lambert** \[00:24:26\]: I was trying to do the same and I messed up the BLM installation. I was like, okay, I spent an hour on this. Yeah.

**Sebastian Raschka** \[00:24:32\]: So you can try Litchipiti maybe. So it works with.

**Nathan Lambert** \[00:24:36\]: Yeah. And there\'s a related question. One of the things I\'m trying to ask people who are hands on, just like, how do you, what do you do to vibe check a new model as you go through so much AI research material and language model material? It\'s like, everyone has their procedures and how do you go about that?

**Sebastian Raschka** \[00:24:51\]: So for me, it\'s like, I, I mean, I use these more like for making sure they generate the correct answers and stuff like that, or something that is reasonable. So honestly, really simple questions for me just to see, so this is more like, I\'m not necessarily benchmarking these models. I\'m more like making sure the implementation is correct. And for that, I use simple questions like what do llamas eat? What is one plus two? You know, like just making sure, because it\'s actually easy. Something I just fixed this morning. It\'s easy to mess up things like KB caching, where you cache, you don\'t clear the cache and then there\'s something from the previous answer and the answer looks kind of correct, but it\'s kind of weird. And, you know, like simple questions can sometimes reveal that. So basically what I do is I ask it multiple, multiple questions the same time. So, sorry, repeatedly, like the same question repeatedly and see if the outputs still make sense and stuff and then mixing them up, but like in a loop basically, but I\'m not so much like, that\'s a great way to make sure the implementation works.

**Nathan Lambert** \[00:25:53\]: Cause I think in transformers, they had a missing end token. There\'s so many little things like this when implementing stuff. Like the, the end tokens is such a ban or like the chat templating can always break things. Cause it also can happen that you mess up pre-training and then you need to have something in the chat template that people might not know. I think in one of the early Olmo models, we like missed a new line in, in one of our documents when we were annealing it. So in order to fine tune it, you had to like have an extra new line before the chat template and like most people will just miss that. Yeah. This is very, very interesting point.

**Sebastian Raschka** \[00:26:28\]: It\'s like, you don\'t even notice it usually when you use something like, I don\'t know, chat GPT, because it\'s applied behind the scenes. But if you implement these things yourself, you have to be really diligent and careful to do it very consistently. Like one little, like you said, new line throws it totally off. It\'s, it\'s, yeah, it\'s interesting. It\'s like, you have to be, I noticed that I was actually working on some DPO stuff this weekend and my template for fine tuning and DPO alignment, the one that I\'m working on alignment, the prompt template was a bit different and I got like garbage results. And then, oh, I, I stripped some line here, the new line character, basically something similar, like you said. So it\'s, it\'s very sensitive to that.

**Nathan Lambert** \[00:27:04\]: Yeah.

**Sebastian Raschka** \[00:27:04\]: Yeah.

**Nathan Lambert** \[00:27:05\]: This, this makes sense. Um, related, do you use Clod, chat GPT, any of these regularly in your workflow? Are you team Clod?

**Sebastian Raschka** \[00:27:13\]: Uh, so yeah, so it depends. I have both and I flip back and forth between them. I don\'t know. I\'m probably not really good at prompting, but sometimes I get better results with one over the other. Um, I think. I wouldn\'t say one is better than the other. They\'re just different. I would say I\'m using.

**Nathan Lambert** \[00:27:31\]: That\'s kind of what I think. It\'s important. Like, it\'s good. Like, what do you think of both of them? I think it\'s good for people to know this because it\'s, it takes some practice to understand and using both. Both people don\'t use both. Yeah.

**Sebastian Raschka** \[00:27:43\]: I would say when I use also GPT-4, I must say I use the, uh, it\'s called legacy now, but the original GPT-4, I don\'t like the mini and old versions. And, uh, for Claude, I use the opposite of the, not the new one, but the one, the previous larger one, the slower one. And, um, I think for me it\'s like coding wise, it\'s kind of weird, but most of the time I like GPT-4 better for code stuff. But then I think also, uh, I think, you know, what, what\'s better with GPT-4 was it\'s, it\'s a bit more up to date, um, with knowledge, I think. But Claude has, I think better, you know, when you say improve my writing or something like that, it has more, it has less, you know, like these, like I delve into something, these weird words and stuff like it, it\'s a less, it\'s more natural a bit, I would say, but

**Nathan Lambert** \[00:28:34\]: also not always.

**Sebastian Raschka** \[00:28:34\]: I agree.

**Nathan Lambert** \[00:28:36\]: It\'s like, it has a bit more flair and a bit more unpredictability. So I like use a Claude on my phone, but I\'ve found, I\'ve tried to use Claude for like information transformation tasks, like LaTeX or taking, taking data out of a table. And sometimes it just like refuses. Like I do research on like AI safety, like safety and bias. So if I put anything into Claude that I\'m trying to transform that data, it just says no. Cause it\'s like, I can\'t comment on like a mean story. Well as OpenAI will just do it. And it\'s like the processing that OpenAI does is very good. So I actually like canceled my GPT subscription when I started Claude, but I kind of regret it now. I\'m like, oh, now I need both, which is, which is a little annoying. Yeah.

**Sebastian Raschka** \[00:29:16\]: It\'s like, yeah. So one thing is what is interesting though, is we, we\'re talking about GPT-4 and Claude here, but we haven\'t even mentioned Google Gemini.

**Nathan Lambert** \[00:29:24\]: I don\'t know.

**Sebastian Raschka** \[00:29:24\]: I personally, I tried the early versions. I don\'t want to say the newer versions are not good. I just haven\'t tried because I didn\'t need to, but do you have experiences with Gemini

**Nathan Lambert** \[00:29:34\]: or? I was using Gemini in search preview. So if you have the Google app, I can, I\'m recording this in, in video. Like you have the Google app, like at the top, you could click on Gemini, which I was doing for a while just to play with it. But like, I don\'t use it on the web. I, they do have a nice interface that looks exactly the same, but somehow I got grandfathered into like AI studio, which I use for, if I upload, record a podcast, I upload the podcast and I\'m like write chapters or something. And it actually works, which is pretty cool to be able to upload like an hour long podcast. But for whatever reason, the Google interface, other than the Google app, hasn\'t stuck for me. And I think that\'s the biggest, biggest limitation. And I use it more in a googly way. So I\'d not, I\'m not as perceptive to style. I see. I see.

**Sebastian Raschka** \[00:30:20\]: So also I\'m curious. I just yesterday saw Apple\'s on device AI is a bit delayed, I think. And for that, I think it\'s an interesting one. We will see how this will work because this will be, I think also smaller models. And there\'s a, for me, it\'s like, I never really care about speed for these things. It\'s like, I just want the best possible models. So this is also why I was a bit disappointed when GPT-4 O came out and GPT-4 Mini came

**Nathan Lambert** \[00:30:46\]: out.

**Sebastian Raschka** \[00:30:46\]: It\'s like, ah, I don\'t really care about if it\'s faster or not. I just want it better. You know, I want to have better quality. I don\'t know. It\'s maybe it\'s just me.

**Nathan Lambert** \[00:30:53\]: I think for building applications, speed is really good. So I have a few friends that run startups that are heavily built on language models and they have a similar stack to perplexity, which is like the user passes in a query that have a primary language model request and they have a series of feedback requests or small requests on top of that. So when you\'re concatenating multiple requests, like speed is extremely important. And when you\'re like selling a product, speed is extremely important. But if you\'re like tinkering and trying to learn, it is much slower. It\'s true. Yeah. Yeah.

**Sebastian Raschka** \[00:31:19\]: It\'s like the real world, like, sorry, not real world, but the individual user, um, yeah, using it as a tool in everyday life versus really building an application based on an API that makes sense.

**Nathan Lambert** \[00:31:32\]: Yeah.

**Sebastian Raschka** \[00:31:32\]: So there are two different use cases.

**Nathan Lambert** \[00:31:34\]: Yeah. Yeah. I think we\'re kind of talking about style. I have a section on RLHF here. I just wanted to like, what do you think you do spend a lot so much on AI education is like, what do you think is most confusing to people about this kind of whole post-training thing, which is instruction tuning, reinforcement learning from human feedback, other safety modules, like adding a filter and stuff like this. I\'m really on the bandwagon of trying to convince people that RLHF is deeply tried with style, which is like this, how this discussion of cloud versus, um, open AI and Google and all these things. And I don\'t really know how to portray that in like an educational technical point of view. So like, I\'ll do an analysis of the paper and I\'ll do like DPO and like scores and all these things. But at the same time, for most people reading my articles, the most important thing is probably to know that open AI is really smart about their style. And that\'s why they\'re so high on chatbot arena. But like, I\'ve written about it a couple of times. I have another article in the drafts, which is essentially like why GPT 4.0 mini like broke chatbot arena. Because everyone\'s so upset that it scored so highly, but it\'s not that surprising if you look at historical events.

**Sebastian Raschka** \[00:32:39\]: So it\'s basically exploitation of the benchmark almost you\'re saying or like the benchmark

**Nathan Lambert** \[00:32:45\]: is focused on style and it really penalizes refusals. So like I get refusals when I use cloud. So it\'s definitely going to like be downweighted. And like open AI is really good at this. This is what they\'ve been doing for a long time. But I don\'t really know how to educate this. Like, have you thought about, like, there was a question on Twitter of why didn\'t you include RLHF in your latest? It was kind of a joke, but I took it out.

**Sebastian Raschka** \[00:33:09\]: Well, if yeah, I can maybe answer that. It\'s it\'s in the works. No, so there are multiple reasons. And so one is it\'s so there are page limits per chapter. And originally it was meant to be in chapter seven. It got way too long. It\'s actually even without it. Chapter seven is the longest chapter already. And what is the other one is fine tuning.

**Nathan Lambert** \[00:33:29\]: Oh, sorry.

**Sebastian Raschka** \[00:33:30\]: Instruction fine tuning. Yeah, I called it not instruction fine tuning. I called it fine tuning to follow instructions, which were originally, which was originally meant to have both, but then it got too long. And the other thing is, you know, like one book chapter takes about two months and a lot of people who really want to book before the new semester starts. So it\'s like, you know, it\'s, there could be another chapter on it, but it would be

**Nathan Lambert** \[00:33:54\]: another two months.

**Sebastian Raschka** \[00:33:54\]: And that, I mean, it\'s not really an excuse, but the other one is I was not happy with the results. And this is a very mathy topic. And I was like, okay, I have this book, which is very clear and makes hopefully a lot of sense. And then I have this really super complicated chapter at the end. I don\'t know if that\'s very satisfying to read or death.

**Nathan Lambert** \[00:34:15\]: Yeah.

**Sebastian Raschka** \[00:34:15\]: Where it\'s like, so you read this book, everything makes sense. And then it comes to this huge\...

**Nathan Lambert** \[00:34:19\]: Why is RLHF so much mathier? Like, I know a couple, there\'s a couple of core equations. Like the core equation is like the RL optimization step, which is expected expectation, maximization of reward subject to penalty. And like, where does most of the, like compared to pre-training, which is like one equation, like that is also one equation, but there\'s a lot of downstream stuff, I\'m guessing. Yeah.

**Sebastian Raschka** \[00:34:41\]: I think it\'s the explaining a bit about reinforcement learning. I mean, you don\'t really have to explain reinforcement learning in a classic sense, maybe, but yeah, there\'s still like KL divergence and penalties and reward margins. And there are lots of things happening at the same time. And the code is also very long if you especially want to track the rewards and stuff. So for my instruction fine tuning chapter, I\'m using exactly the same training function I implemented in the pre-training chapter.

**Nathan Lambert** \[00:35:14\]: And it\'s really nice.

**Sebastian Raschka** \[00:35:14\]: It\'s like, well, you can actually reuse everything. It\'s, it fits together.

**Nathan Lambert** \[00:35:18\]: Yeah. Like what we\'re doing on OMO, we can baseline our instruction fine tuning in our fine tuning code base, which also has some RL things and in our pre-training code base. So it\'s nice to have both, but that is definitely why it\'s simpler. And the RL is only getting worse in my mind, I think. Like we\'ve seen that LLAMA has used rejection sampling for two iterations and there\'s no public implementation of rejection sampling that at least public enough to know that people have actually trained models with it, which is the idea of ranking completions to a reward model and then running instruction tuning again on the top completions.

**Sebastian Raschka** \[00:35:54\]: I think also in the recent LLAMA 3.1 paper, they used rejection sampling with DPO, for example. Like they didn\'t use the RLHF with reward model, but then they used the reward model for the rejection sample. And yeah, so I must say, I have the code for the DPO. I wanted to do TPO because it\'s also more resource efficient. You don\'t have to train that reward model for, let\'s say the book, but I was not really happy with the quality of the output yet. So I must say it\'s like, okay, this is not, it\'s not helping the instruction fine tune model. And it\'s like, I think a general thing where I, I mean, you might correct me if I\'m wrong here, because you are the expert in RLHF, but for me, it\'s like, it\'s like a optional thing where unless you need a specific style or need to deploy something in like a safe manner, it\'s maybe not giving you the best results. If you need a private model that just runs on your own computer and gives you correct answers, I don\'t think DPO or RLHF will make the answers more correct. They will just change how they look like.

**Nathan Lambert** \[00:37:01\]: And yeah, I mostly agree, especially on what we have in public implementations. The public implementations are really good at improving on like alpaca eval. But if I\'m training a model that I actually want to use, don\'t worry about alpaca eval. I think I\'m like the most annoying person internally running these experiments because I just get so annoyed when only alpaca eval goes up and be like, that has made the model worse. Like we\'ve, I\'ve been building internal demo tools, which is just like making Gradio better and showing how to use VLLM for serving. But it\'s like a lot of the models we put out for research are like really, really annoying to talk to. You put no yapping or just be concise in the prompt and it doesn\'t do anything. So like a lot of the open datasets, and this is something that Nibetron and Lama3 have shifted to is this new evaluation, which is like IF eval, which stands for instruction following eval, which I think is a great one. So it\'s like write a response with less than 300 words or something. And it has these verifiable claims. And this is something that the Nibetron report showed that like doing fine tuning really unlocked a lot more performance in the DPO stage. So I\'m hoping that we start to get more evals than just alpaca eval that are helped by this RLHF and that\'ll help the whole ecosystem come forward because it is in a kind of young, rough state right now. Yeah.

**Sebastian Raschka** \[00:38:21\]: And also one last thing about this topic is for me, like you said, the last sentence is kind of also one of the reasons is where I was like, okay, if I include something on DPO as the last chapter, I don\'t know if it\'s still going to be used next year or if there\'s so many variants, ORPO and QTO. And I mean, right now, I mean, Lama3.1 used DPO, which is like a big endorsement. But to be honest, I\'m not sure if this exact variant is here to stay.

**Nathan Lambert** \[00:38:47\]: And so I think DPO is here to stay. DPO will be a canonical example, much like PPO. But I think the things that people are using will go away. Like PPO has stood the test of time of multiple eras of RL. So I don\'t think that people use it in its exact form, but people are always looking at it. And same with DPO, just because DPO is so simple. Like the exercise, this is like one of the best getting started with RLHF exercise is taking like the hugging face trainer and modifying it to use the DPO loss because you could use all the other infrastructure for like most of the infrastructure for batching and stuff like this. And then add that loss function, which is a few lines of code. And like, that\'s a good, that\'s like the entry point to doing RLHF implementations. Like when I interview people, I\'m like, make sure that they have looked at this DPO loss function before. And if they haven\'t, I\'m like, I don\'t know if you\'re in the weeds enough. I feel like you should look at this.

**Sebastian Raschka** \[00:39:37\]: Speaker 3 And if you need, if you are listening to this and you are about to get interviewed by Nathan, I will hopefully have by next weekend a tutorial on DPO, on implementing it from scratch. I was, this weekend I used actually Lama 3.1 to make a synthetic data set for that and got much better results. So it looks good enough to probably upload it next week. So nice.

**Nathan Lambert** \[00:39:58\]: Okay. Let\'s shift gears into like AI research and AI education, which is I think the thing that you have some of the most insight into. So you\'re a head of AI newsletter. You, I wasn\'t originally reading it when I subscribed, but now I almost always skim through to kind of see what papers you uncover. I\'m pretty interested in like how you select papers, like how much you actually prioritize reading papers and why, and just like any advice for people, because it\'s hard to sit down and do this. And I, speaking for myself, sometimes writing is like how I force myself to read some papers. I don\'t know if you\'re in the same boat, but like, what is your worldview around reading AI papers these days and skepticism or excitement, everything?

**Sebastian Raschka** \[00:40:42\]: Yeah, that\'s a big topic. So I must say, so I, I look at more paper than I actually literally read. I mean, I look at the abstracts and the titles and then that\'s like a huge funnel as a section

**Nathan Lambert** \[00:40:54\]: processor.

**Sebastian Raschka** \[00:40:54\]: I must say for like, I was an archive moderator for the machine learning archive a few years back and that got me into the habit. So how it worked was basically as a, maybe it\'s useful because some people complain when

**Nathan Lambert** \[00:41:06\]: How did someone become an archive moderator? I didn\'t know that it was like a community position.

**Sebastian Raschka** \[00:41:12\]: So that was originally by Tom Dietrich. He was doing it by himself and he was looking for people to help him with that. Because as you mentioned, there is an ever increasing number of papers. And so how it works is essentially that when you submit a paper to archive, you select the categories. But a lot of people, they select not, let\'s say the correct, I wouldn\'t say not correct, but like the preferred categories because Yeah, the AI and ML.

**Nathan Lambert** \[00:41:39\]: It\'s like ML, AI, and then everything else. Yeah.

**Sebastian Raschka** \[00:41:42\]: And AI in archive is interesting. It\'s more like the classic AI. It\'s like, it\'s not LLMs. It\'s more like symbolic AI, that kind of stuff.

**Nathan Lambert** \[00:41:51\]: What do you think the difference between, or like as an educator, how do you define AI and machine learning? This was also one of my favorite interview questions to like see where they\'re at.

**Sebastian Raschka** \[00:42:00\]: Well, right now I would say I go back and forth on that. Right now I would say AI is this big umbrella thing where you have deep learning and machine learning as subfields. But if you think about it, if you consider a logistic regression classifier, it is essentially machine learning. And if machine learning is the subfield of AI, you would say, okay, then logistic regression must be AI. But is like classifying iris flowers really AI? I don\'t know. So today I would say

**Nathan Lambert** \[00:42:28\]: I also think about search as AI. Yeah. Like, yeah.

**Sebastian Raschka** \[00:42:31\]: Like, yeah. So there\'s like the good old fashioned AI. So I would say with AI, yeah, you have both, you have the machine learning and deep learning branches, but you have also, you can also implement AI with if else statements, I guess, like, you know, like, so. So that\'s how I would define AI. But I think nowadays when people talk about AI, they mean specifically gen AI, like generative AI models, like LLMs, stable diffusion, that type of stuff. But yeah, so the archive thing. So just briefly, basically there is in the background, it\'s also using machine learning or NLP to detect whether the title based on the title and the abstract, if the category is actually matching. And if there\'s a mismatch or in general as moderator, you go through them and, oh, this looks good.

**Nathan Lambert** \[00:43:17\]: This looks good.

**Sebastian Raschka** \[00:43:17\]: This looks good.

**Nathan Lambert** \[00:43:18\]: They started exposing this to the user. So I submitted a paper recently under ML and I was like, this looks like language. And I was like, I\'ve been in moderate, I\'ve gotten papers stuck in moderation. So I was like, I\'m always going to hit, except if they tell me it might be in the wrong category, because archive moderation is a black box that you don\'t want to get stuck in. No, no, like as a user, but I understand the service it\'s providing. So it\'s good to expose that to the user. And if anyone\'s listening, just click it, click. Yes. It\'s not worth delaying your release. We get stuck in moderation and help archive out. Yeah.

**Sebastian Raschka** \[00:43:50\]: And so just the last thing on that is by default, everything gets accepted. However, sometimes it\'s something gets flagged. If there\'s duplicate content, if it doesn\'t look like a paper, sometimes people submit like one page blog posts or something. So there is this thing where sometimes there are also false positives and then it gets stuck. But long story short, that got me into the habit of reading the titles. And that\'s what I still do. Also for my head of AI newsletter, I just look through the titles and select. How have titles changed?

**Nathan Lambert** \[00:44:21\]: Like titles have changed a lot though, as I feel like they used to try to be. Accurate. Mostly descriptive. Yeah. Descriptive, right? And now they are a mix of, it\'s more of a storytelling than descriptive. I think it\'s the right way to tell it.

**Sebastian Raschka** \[00:44:36\]: At least we don\'t have the, it\'s all you need anymore. I feel like this went away finally, but yeah, you\'re right. It\'s more.

**Nathan Lambert** \[00:44:43\]: It ended with Ryland Schaefer\'s test set. Training on test is all you need. Yes. Did that make it on archive? It did.

**Sebastian Raschka** \[00:44:51\]: I think I also had it featured in my newsletter one time. I think. Or not featured, but at least mentioned. And so how I select papers is also often selfish. I read or select papers for the newsletter that I find interesting. And because I think this is also for education. When people ask me about how I would suggest doing things, I think the most important thing is to talk and work on things you are interested in. I think it would be really hard to do a good job if it\'s a topic that is not interesting to you. For example, I know, I don\'t know. R, sorry, or Rust is interesting, a very important topic, but I\'m not into it. So I don\'t try to, let\'s say, make videos or content.

**Nathan Lambert** \[00:45:35\]: Yeah.

**Sebastian Raschka** \[00:45:36\]: So it\'s like, I think if there\'s something you\'re excited about, I think it comes almost naturally that you want to talk about it. So in that sense. So the newsletter, I almost, it\'s weird, but I almost write it for myself. It\'s like, I find it interesting.

**Nathan Lambert** \[00:45:49\]: How much do you spend reading versus writing when you\'re reading these papers and writing a blog post? I\'m guessing a lot of it is just the natural process of synthesis is what you put into the newsletter. It\'s not like you\'re doing it from my read. It\'s not like you\'re doing a ton of scaffolding and editing after the fact, which seems similar to what I do.

**Sebastian Raschka** \[00:46:09\]: Yeah, you\'re right. I don\'t do, I don\'t spend too much time on it in the sense that I wish I could, but I have a full-time job. It\'s literally just the weekend project where I aim for one newsletter per month. Of course, I would like to do more, but there was also a book to write on weekends or sometimes I\'m doing videos. It\'s like keeping it fun, you know, like where it\'s like, okay, this is not a chore. This is something that is supposed to be fun. Like in that sense, I read a paper and then I take notes and then I collect them and spend maybe half an hour, an hour to polish them a bit up or make some figures. And that\'s it per paper, I would say. And so I also don\'t write the whole newsletter on one day or one weekend. It\'s really spread over the month. I read a paper. Oh, this is an interesting one for other people. Let\'s write this up basically. And then this way I collect material over the month and then.

**Nathan Lambert** \[00:47:00\]: Yeah. What motivates you to work on this stuff? Is it purely like education? Because I, in some ways relate to that. I\'ve been in that mode before.

**Sebastian Raschka** \[00:47:09\]: Yep. So if you have noticed, I don\'t have any sponsorships or something.

**Nathan Lambert** \[00:47:14\]: Never done that. Respect.

**Sebastian Raschka** \[00:47:16\]: I will never say never, but it\'s not something I do. It\'s really just a hobby. And I do like discussions that come around it. There\'s a certain satisfaction that if you put it out, it helps others and people tell you positive things about it. It\'s kind of very gratifying. I don\'t know. There\'s like a reward in a sense. And what\'s also cool is there are a lot of people. It\'s like being part of the community and exchanging information because there are also a lot of people who sometimes know something I don\'t know. And this is really, I think, really cool. You write about something and then someone, Hey, have you seen this? This seems like it\'s taking it to yet another level. Or this is the same idea. It\'s even better or something. And this is super cool where you get this effect where you learn by doing this, actually, because there\'s always someone who knows a bit more than you do in a specific area. So, yeah.

**Nathan Lambert** \[00:48:07\]: Yeah. I feel like it\'s increasingly important these days and increasingly impactful because so much of research has become closed off and for business reasons. So there\'s fewer people that do more of the work. I don\'t like it. I always feel like people don\'t realize how few people are informed and share on any given topic like AI research. If you take away three people, I\'ve yet to find people that just tweet the same random RLHF crap that I tweet. It\'s like, I don\'t do it because I just say random things, but there\'s not that many people that represent each of these corners. Ahead of AI, I think Jack Clark\'s important AI. I should have him on the pod. I think I\'ve talked to him a few times. He\'s great to talk to. And his is the same thing. It\'s like these few people that are disseminating AI information, which is crucial for policy at future angles. Have you ever gotten criticism that your work is accelerating AI and that you are a safety risk? I\'ve gotten some critical emails that are like, you shouldn\'t talk about this.

**Sebastian Raschka** \[00:49:07\]: Yeah, I\'ve more gotten emails about the fact that I talk about LLMs is not good because LLMs violate copyrights. I mean, not that I do it, but that other people\'s LLMs do it.

**Nathan Lambert** \[00:49:21\]: And I\'m happy that I haven\'t had this audience very much, but it seems this is like one of the challenges of having a tech audience is like you cultivate it in kind of one of two, like there\'s multiple ways to go. And one of them is like this all data is for language models is theft thing. And I just don\'t know how to deal with it because like I disagree, but the normally people that aren\'t receptive to it, which is really hard. It needs to be played out. Yeah.

**Sebastian Raschka** \[00:49:47\]: My book also just to make extra sure all the data I use there is so the pre-training data is public domain data, like a book from Project Gutenberg. And for instruction fine tuning, I did my, I created my own data set basically. So just to avoid any issues, you know, like. Did you do, you wrote it by hand?

**Nathan Lambert** \[00:50:06\]: Yep.

**Sebastian Raschka** \[00:50:06\]: So I took, no, actually I used, I used part of an LLM and some by hand.

**Nathan Lambert** \[00:50:12\]: Yeah.

**Sebastian Raschka** \[00:50:12\]: So it\'s a great exercise.

**Nathan Lambert** \[00:50:14\]: Yeah. Yeah.

**Sebastian Raschka** \[00:50:15\]: And for the synthetic one, I use LLAMA 3.1 now too. I mean, yeah, you can tell me also about that a bit. I mean, that\'s maybe interesting for the audience, how to generate a preference data set, because there are multiple ways, I mean, naturally it\'s crowdsourced, right? So you ask people, you have the model generate two answers or have flavors of the model generate answers and then, oh, which one do you prefer? But it\'s not really scalable. And so you could technically do the same thing with an LLM. You could basically have the LLM generate a more polite version because I think LLMs are very good at, even the small LLMs, the open source 7b models are good at rephrasing things or evaluating things. They\'re not necessarily good to generate the answer in the first place if they don\'t have a reference, but given a reference, I think it\'s super useful to use open source LLMs in that sense.

**Nathan Lambert** \[00:51:07\]: I\'m surprised that this hasn\'t caught on sooner, but I think it\'s starting to catch on. I think in the meta report, they essentially have edits. So then they rank, they make their preference pairs as edited better than chosen, better than rejected. And that\'s like, you can create multiple players by binarizing. There\'s a few research projects that have done this where they have like, constitutional AI is popular, but that\'s not really reproduced. One of my collaborators slash friends at Synth AI Labs, Louis Castricado, he did a paper on like the pink elephant problem, which is like using provisions to get the model to not just say whatever is in the question if you ask it not to. We did a follow-up work that\'s out literally today, which is like on self-directed synthetic dialogues where you have the language model generate a plan, and then it follows the plan. And then you can also do revisions on it. So I think Nemetron did this with Prompt. So it\'s really getting going, but it\'s something that took longer than I expected. There\'s the kind of question, this is like too big of a topic to go into, but it\'s like, how do you use GPT-4 feedback? Do you use like, are your completions from two different models or the same model with different generation settings? How do you use humans? I think that the labs are using humans for preference data because it eliminates some of the problems in language modeling. And then that\'s one of the biggest impactful research questions in alignment. It\'s like, we can\'t afford the \$1 to \$10 million dataset. How do we do this? And that\'s what, we\'re starting a project to do that AI too right now. And it\'s a big open, like, I don\'t know where it\'ll go. I don\'t know how much, like how far can we reproduce the LLAMA-3 alignment methods. Yeah.

**Sebastian Raschka** \[00:52:46\]: So I would say the LLAMA-3.1 paper or the LLAMA-3 paper, it was like a 93 page paper

**Nathan Lambert** \[00:52:52\]: and it was great.

**Sebastian Raschka** \[00:52:52\]: I love it. It\'s like a lot of detail, but on the alignment part, I feel like I wish there was more information

**Nathan Lambert** \[00:52:58\]: about it.

**Sebastian Raschka** \[00:52:58\]: Even like LLAMA-2 had more information where they showed what is the improvement actually over the different stages when they added to supervised fine tuning.

**Nathan Lambert** \[00:53:05\]: So I\'m talking to Ross Taylor tomorrow, and I\'m going to ask him the specific thing. On latent space, like Thomas S., one of the leads, said that most of their gains come from RLHF rather than SFT. So I think the open source community is over-indexed on instruction fine tuning because it is accessible and we have the data. And this is like one of my, like, try to guide the community by doing things is like, go do RLHF. Don\'t worry about instruction tuning data sets. Don\'t worry about that. We\'ll just leave that the same and go find more preference data and keep playing with this. And don\'t worry about the DPO methods. Just literally go make preference data and keep trying to train things. Like don\'t implement a new loss function.

**Sebastian Raschka** \[00:53:48\]: Practical question to an expert like you. How good is actually a preference data set if you download it, if both the chosen and the rejected answers, if you download a preference data set, they\'re not generated by your model, right? And if you have a model and you use the responses that the model has never basically seen before, does this actually work or would it be advisable?

**Nathan Lambert** \[00:54:11\]: So the most, the two most popular preference data sets in the open right now are UltraFeedback and Nectar or variants of them. Both of those are collected from large suites of other models. And part of my, there haven\'t been data sets or papers that have trained really good models using on-policy preference data from the model you\'re training. And I think that\'s a question that we need to answer. It\'s like, how do we get UltraFeedback level results with on-policy data? Because all the labs are using on-policy data. I wrote about this in like Barry to one article. I have a theory that UltraFeedback and Nectar, these general data sets work so well because within them, there is something close enough to your distribution and you don\'t have to get it quite right. But it\'s just like a gentler, more uniform learning signal for the models doing preference tuning. But we don\'t know. That\'s something that I want to answer.

**Sebastian Raschka** \[00:55:02\]: Yeah, this is an interesting one. I would also like to know the answer because that is one thing where I got a bit stuck when I was writing this DPO chapter with smaller models. I think bigger models also, they hide these weaknesses a bit because they have been trained on so much data that like you said, it\'s kind of in distribution already. But if you train a small model, it would be out of distribution, right? If you use someone else\'s preference data set. I noticed even something simple when you train a model on one simple instruction data set, let\'s say something like alpaca. And then let\'s say you have just to have something visual. You want the model to generate Yoda speech, like where every sentence is reversed. But the model has never seen sentences like that unless it was maybe in the training data. But in that sense, it doesn\'t work well at all because you ask the model during preference tuning to write sentence structures. It has never grammatically written before. And so in that sense, I think what I found is it\'s much better if you, I don\'t know, you say be more polite or like you have a more polite answer because you use the same grammar or so. So things like that basically. And yeah.

**Nathan Lambert** \[00:56:08\]: Yeah, I think that\'s a smart approach. It also might be why learning rates are getting so low. Where like all the learning rates for DPO and things have been going down in the fine tuning space. And it might just because distributionally, like we\'re far off from the model. There\'s the other theory that the model is like really, really done training. So they get it to a really good optimum. You don\'t want to move it from them. But it might just be that like our data sets are in the wrong space. Yeah.

**Sebastian Raschka** \[00:56:32\]: So you try to be gentler with a lower learning rate.

**Nathan Lambert** \[00:56:36\]: Yeah. All of this stuff changes fast, but not fast enough. Like this ultra feedback data set they were talking about came out last October. So we\'re like almost 10 months in and it\'s still the state of the art data set. And it\'s only like 50,000 examples. So there\'s so much opportunity for someone to like at this level, like go build data sets if anyone is watching. Because it\'s like, I think we\'re so far off where we could be just because people don\'t know how to make good preference data sets.

**Sebastian Raschka** \[00:57:02\]: Well, now we have LLAMA 3.1, 70 and 405 billion that allows us to do that, right?

**Nathan Lambert** \[00:57:08\]: We\'ll see. Yeah. I was wondering, this is a change of topic, but how do you think like, do you think AI will change our jobs in writing? How do you see AI coming for this kind of educational space? Like how much of what you do as an educator could be taken in N years by AI?

**Sebastian Raschka** \[00:57:26\]: Well, I think it\'s like, of course it will automate away some things because nowadays you would ask a model something instead of searching for it and reading it on a website. But I do think the creation process, you still need a human to put it together well. Because I don\'t know, I think LLMs are not nowhere near like generating a whole article that is actually, I would say even good where it can generate the right things, but you still have to put it together. It can generate good blocks of text or something like that, but you need to, as an edit, like you become maybe more like the editor then in that sense. But I\'ll try this.

**Nathan Lambert** \[00:58:09\]: Also like, do you write, do you have AI write any parts of your articles? I\'m so scared for like moral reasons to have any AI writing in it. I\'m like, it\'s just a slippery slope. It feels like I could get addicted. Yeah.

**Sebastian Raschka** \[00:58:21\]: So sometimes I don\'t have it write anything from scratch, but I sometimes do do that. And especially, I don\'t know, I have a, I mean, I\'m a non-native language speaker and sometimes I have a harder time than other days to make the sound right. It\'s like, okay, this is what I want to say, but it doesn\'t sound right. And then I, can you revert this with a focus on XYZ or something? So like, it\'s basically like a, you know, like a thesaurus where you find similar words, you find similar sentences, like just rewording it, like these types of things. But one also, now that you mentioned it, one weakness it has, or LMs can\'t do really, is they can\'t generate figures. You know, maybe that\'s coming.

**Nathan Lambert** \[00:59:01\]: I don\'t know.

**Sebastian Raschka** \[00:59:01\]: You can do that probably with ticks, like the latex thing where at one point, but right now nowhere near, can you generate any useful figure? And I think learning is very visual too. I think if it\'s just text, it would be really hard to learn anything.

**Nathan Lambert** \[00:59:17\]: Yeah.

**Sebastian Raschka** \[00:59:17\]: So you can, of course, but I do think, you know, there\'s a saying, image is worth a thousand words, right? So yeah, in that sense, you still need someone, you know, like the mastermind behind an article, even if it\'s just an editor, I don\'t think LMs can replace everything at least. And we\'ll see. I mean, I don\'t know how much better, I mean, we just don\'t know how much better, let\'s say GPT-5 as a placeholder here will be then GPT-4, you know? So maybe if it\'s saturating, who knows, right? So maybe it will be five more years till we, yeah, get in a more scarier territory in terms of replacements, you know? So we\'ll see.

**Nathan Lambert** \[00:59:55\]: Yeah. I mostly avoid the agent word, but it does seem like there\'s enough culture and cultural investment in the Bay Area and tech executives to do something. Like they\'re going to get to something that is triable, which I think is mostly like automatic Google searching, more code execution, which is going to be interesting, but I have such wide expectations of what it actually means. That\'s probably the next big shift. I think this LLAMA 3.1 is probably right now leading the year in terms of AI news. This recent DeepMind thing on the math might be a better example of what\'s really hot news. I need to go read more about it. There\'s some long write-ups on how the qualitative between the AI math and the human math and the different directions they\'re going. So that\'s kind of what I want to read about it. But it\'ll shake things up. We\'re multiple years into this fast phase. It\'s not exactly new at this point. Yeah.

**Sebastian Raschka** \[01:00:57\]: Last thing on that is I do think, though, LLMs make good assistance in the literal sense where one thing where I use it for my newsletter for is at the end, I have a list of all the papers I have found interesting, like 30, 50 papers usually. And usually per hand, I edit the author names, like the last names of the first three authors. And now I use an LLM to go to the website and get the names of the authors, basically. And so this is where it saves a lot of time. You could do that without LLMs. You could write some code to do that, but it would probably take me half a day to write because I\'m not good at this web scraping code to do that type of thing. And I think in that sense, it is actually a useful assistant for certain things like

**Nathan Lambert** \[01:01:44\]: delegating actions. I think it\'ll keep creeping up. I don\'t expect their usage for those things to go down because they already are so useful. And the little coding things, the hacking data together, the automatic searching, people aren\'t going to want to stop using that. I don\'t know if it supports the whole valuation we have, but it\'s fun to be in a space where we get to try new things. As a computer nerd, it\'s really fun to have a new type of software that we can try all sorts of things in our workflow. And I think that\'s underrated. So I don\'t know. Thanks for coming on. Any last things you want to discuss?

**Sebastian Raschka** \[01:02:19\]: Yeah, I just wanted to say thank you for the invitation and I hope you keep creating these awesome newsletters. I think this is much needed because there\'s so much hype, like you said previously, it\'s

**Nathan Lambert** \[01:02:32\]: creeping up on us.

**Sebastian Raschka** \[01:02:32\]: There\'s a lot of over, let\'s say, evaluation and praise. And I think something that is kind of like cutting through this is it\'s much needed like this honest, straightforward, no bullshit content. So yeah, I hope you keep creating that. It was fun to chat. And yeah, to everyone out there, I think also what keeps us motivated, I think, is the awesome community that people give feedback and discuss things and bring things up. And yeah, I think without people also giving us feedback, we wouldn\'t be probably doing this because it\'s kind of a lot of fun to be in that space, I must say. Yeah, it\'s fast moving, but there\'s always something interesting every day.

**Nathan Lambert** \[01:03:14\]: Yeah. Yeah, this is really interesting. We covered a lot of kind of low level of just what it\'s like trying to use language models on the day-to-day basis in July of 2024. So thanks for coming on. And I\'m sure we\'ll talk soon. All right.

**Sebastian Raschka** \[01:03:27\]: Yep, it was nice meeting you and see you then. Bye.
