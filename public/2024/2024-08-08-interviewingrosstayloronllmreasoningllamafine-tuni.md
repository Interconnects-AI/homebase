---
title: "Interviewing Ross Taylor on LLM reasoning, Llama fine-tuning, Galactica, agents"
subtitle: "Interconnects interview #5."
date: 2024-08-08
type: podcast
audience: everyone
visibility: public
post_id: 147219110.interviewing-ross-taylor-on-llm-reasoning
email_sent_at: 2024-08-08T12:01:09.071Z
---
I had the pleasure of Talking with [Ross Taylor](https://x.com/rosstaylor90), who has a great spectrum of unique experiences in the language modeling space --- evaluation experience, Galactica lead author, Llama post training, etc. This is a really great conversation on the frontier of language model (LM) reasoning, LM deployments and demos, LM's for science, RLHF, and other topics. I've been trying to get Ross to come on for a bit. He's one of those people in the LM space that doesn't speak too much, but when you do, you listen.

Ross Taylor was previously an LLM lead at Meta AI, heading up the reasoning team. Previously he led the early work on LLM agents, and was the research lead on the Galactica project. Before that, he was a co-founder of Papers with Code, which was acquired by Meta in 2019. Before that, he has worked as a quant in sports betting and finance, and before that a policy advisor for the UK Government. He is currently working on a new startup.

Listen on [Apple Podcasts](https://podcasts.apple.com/us/podcast/interconnects-audio/id1719552353), [Spotify](https://open.spotify.com/show/2UE6s7wZC4kiXYOnWRuxGv), and [where ever you get your podcasts](https://podcast.interconnects.ai/subscribe). For other Interconnects interviews, [go here](https://www.interconnects.ai/t/interviews).

### YouTube

:::::::: {#youtube2-KNsnarhMZRo .youtube-wrap attrs="{\"videoId\":\"KNsnarhMZRo\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=KNsnarhMZRo){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

### Chapters

-   \[00:00:00\] Introduction of Ross Taylor and his background

-   \[00:02:12\] Papers with Code

-   \[00:09:58\] Galactica, goals, controversy, legacy

-   \[00:18:12\] Technical details of the Galactica model

-   \[00:23:18\] Potential for language models to make scientific discoveries

-   \[00:25:21\] Defining and improving reasoning in language models

-   \[00:32:38\] Process-based reward models and their potential applications

-   \[00:35:00\] Generating synthetic data for SFT

-   \[00:40:23\] Evaluating the effectiveness of language models as judges for human preference data

-   \[00:42:43\] Considerations for creating base models that are easy to fine-tune

-   \[00:46:45\] Balancing SFT and RLHF

-   \[00:54:13\] Characteristics of successful post-training teams

-   \[00:58:26\] Future directions for language model development

### We mention

-   [Galactica](https://arxiv.org/abs/2211.09085)

-   [Papers with Code](https://paperswithcode.com/)

-   [Rob Stojnic](https://x.com/rbstojnic?lang=en) (co-founder of Papers with Code)

-   [DPO](https://arxiv.org/abs/2305.18290), [PPO](https://openai.com/index/openai-baselines-ppo/)

-   [Armen Aghajanyan](https://x.com/ArmenAgha) (Chameleon)

-   [Tom Scialom](https://x.com/thomasscialom) on [Latent Space](https://www.latent.space/p/llama-3)

-   [Soumith Chintala](https://soumith.ch/) (PyTorch)

-   [Alex Graves](https://en.wikipedia.org/wiki/Alex_Graves_(computer_scientist))

-   [Llama 3 paper](https://ai.meta.com/research/publications/the-llama-3-herd-of-models/)

-   Process Reward Models / [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)

### **Transcript**

Built with [smol-podcaster](https://github.com/FanaHOVA/smol-podcaster) and with love of Latent Space.

**Nathan Lambert** \[00:01:07\]: Today, we\'re here with Ross. This is a really exciting one. I\'ve been trying to get Ross on the show for a while. Ross has done a lot of interesting work. And also the path to where you ended up with working on state-of-the-art LLaMA work at Meta is very interesting to me. So we\'re going to start with some of that, but then there are a few people that want to know more about reasoning and some of the RLHF stuff. We won\'t cover the secretive new start-up - I don\'t know what it is, but that\'s how it goes these days. I\'m sure it\'ll be great. So welcome to the show!

**Ross Taylor** \[00:01:41\]: Thanks for having me.

**Nathan Lambert** \[00:01:44\]: So I wanted to start with Papers with Code. For people that don\'t know, Papers with Code is one of these platforms - I never was a heavy user of it - but it collates papers, people can upvote them, popular papers, attaching code and dataset and evaluations to papers, which is great - it was like sort of ahead of its time. It fits into a lot of these open ecosystem things. So I\'m kind of curious, like, how you ended up there and why you all started this startup that ended up building this thing that got acquired by Meta?

**Ross Taylor** \[00:02:12\]: Yeah, that was a weird one. This was like back in 2018. So I was at an incubator, I just quit my previous job and I was like, okay, I want to do a startup. And I met Rob, my co-founder, who came along with me for the journey. We both came from different backgrounds. I was from a sports betting / quant finance kind of background, which is a whole other episode I guess. And Rob was in various startups, like applying ML to things like hate speech detection, that kind of stuff. And the cool thing was, we both resonated on similar kinds of problems within the ML space, even though we came from different domains. So we spent a lot of time doing various experiments, trying to make new kinds of ML tooling, thinking of these stupid questions like "what is the Git equivalent for ML?" - that kind of stuff. One of those experiments was hacking around on this little website to solve a really basic problem: I\'m trying to reproduce this paper, but I can\'t find the code. That was the thing that really blew up beyond our expectations. It was weird because we thought it was fairly trivial at first.

**Nathan Lambert** \[00:03:16\]: What year was this? 2018?

**Ross Taylor** \[00:03:18\]: Yeah.

**Nathan Lambert** \[00:03:19\]: This makes sense. I think this was like, I was starting Deep RL then, but Deep RL was so hot, which was like the worst evaluation has ever been probably for ML. Like people complain about it today, but like Deep RL evaluation was like, every single person was just lying to make themselves look better.

**Ross Taylor** \[00:03:38\]: The interesting thing now is that the open ecosystem has shifted to focus more on weights as a central artifact rather than code. I think there\'s an interesting debate there. Would it be more useful to have the LLaMA-3 8B model weights or all the code for training LLaMA-3? I think there\'s still interesting debates to be had about what\'s actually useful.

**Nathan Lambert** \[00:03:56\]: I think the code would be more useful. Like OpenAI released their rules-based reward models, but it\'s like code washing because it\'s like just a bunch of people just released like eval code now. And it\'s like, that\'s a whole another tier is like actual training code versus eval code. But yeah, I guess I\'ll just skip ahead.

**Ross Taylor** \[00:04:12\]: So essentially Papers with Code was the thing that didn\'t die for us. We always thought we were going to make something else and Papers with Code was more of a marketing thing. But eventually we were like: okay, our users are telling us this is what we should be working on. And we expanded from that very simple use case of finding code towards indexing various artifacts in ML.

Another big problem was trying to find the state of the art in something like ImageNet and all these different benchmarks. There just wasn\'t a central place to find this information...So we had this quite good Christmas - me and Robert - where we hacked for the whole month, indexing every leaderboard we could and all the related papers. I didn\'t want to do any annotation again after that! But that took things to the next tier, and that\'s when things really started to blow up.

**Nathan Lambert** \[00:05:03\]: Because this is like the first round of leaderboards, because now it\'s really popular with Hugging Face again. And I was like, yeah, is that just because it became like a Meta thing and it\'s just kind of a thing that existed? You\'re like the first leaderboard company in a way, which I don\'t think many people think about. Yeah, which is weird.

**Ross Taylor** \[00:05:19\]: Yeah. And the interesting thing about us was that we never had to do any marketing because everything was from organic traffic. So you would type in "state of the art ImageNet" and we would come to the top as the most useful site. That was really the source of our growth, and we grew to a million MAU fairly quickly. And as for Meta, we were in touch with the PyTorch folks at the time who we really liked. You know - Soumith, Joe - those folks, and they had a shared interest in promoting the open source ecosystem back in 2018/19. And while it was like a tough decision, we were just like "we really like working with these people, we want to work more closely with them", and that got us into Meta.

And then within Meta, we originally continued to develop the platform. But the big shift for us was that, even then, we saw we were moving to a world where compute was the currency. And we saw that, if we wanted to be well positioned in five years time, we needed to be building these large-scale systems. Even for our own platform, we had lots of ML in the backend and we saw we were using fewer and fewer models to do more and more tasks. So that kind of shifted us into research, into Galactica, and then eventually LLaMA and that kind of stuff.

It was a weird shift because we were product people who ended up doing hardcore research! But I guess it was natural to us that we were within a research org with these amazing people, lots of resources. It was just the best use of our time to conduct this shift.

**Nathan Lambert** \[00:06:43\]: Do you think there should have been more integration between Hugging Face and Papers with Code? It would have been wonderful if it had happened.

**Ross Taylor** \[00:06:54\]: The backstory is that we saw them as competitors, to be honest, because we had the same vision originally. We were going to do model hosting, that kind of stuff. But we never got into it because we hit friction with leadership - who was not onboard with that as a goal. Because from their point of view, it\'s like, okay, if we host these things, this might expose Facebook to some kind of legal risk. It wasn\'t in the perceived interest of the company.

**Nathan Lambert** \[00:07:17\]: This is a classic story of tech, really. They can\'t take the risk. They can\'t expose themselves.

**Ross Taylor** \[00:07:23\]: If you\'re a startup and it\'s your number one priority, then yeah, your attitude on risk is different. But I think it was a blessing in disguise for us because clearly the bigger wave was going to be large language models - we saw that incredibly early. And our mission was fundamentally not infrastructure, but something closer to: how do you organize information? It was a Google-y type of mission. And while we were focused on ML, we were more broadly thinking about science: how do we reduce friction for finding out about new advances and, I guess, lots of small tasks that when added up lead to a lot of progress in science.

**Nathan Lambert** \[00:07:59\]: I should have probably looked this up. Did you have another scientific background? Did you have a hard science background or what about Rob? Stojnic?

**Ross Taylor** \[00:08:10\]: Yeah, \[Robert\] Stojnic, my co-founder, he was from a bio background. So he\'s actually-

**Nathan Lambert** \[00:08:15\]: That makes sense.

**Ross Taylor** \[00:08:16\]: Well, he also had a computer science background. He was one of the original developers of Wikipedia, so he has his own crazy story...

**Nathan Lambert** \[00:08:22\]: Yesterday I was talking to somebody that was one of the original arXiv moderators. So we\'re digging all these things up...

**Ross Taylor** \[00:08:29\]: It is interesting because we both had this background, I would say, in building useful "utilities" \[on the internet\] at some point in our lives. I think Papers with Code is one of those things which is easy to forget, but if it went away, everyone would go crazy.

As for me, my background is more statistics and econometrics. My first job was in the Government, which I kind of hated. But I did a Master\'s degree, which I thought was going to be in economics, but the thing I ended up loving was time series and statistics. So I did all this research on state space models - before it was cool, I guess! - and then that got me into sports betting. And then eventually, we were using more and more deep learning \[in the 2010s\], and that's how I got into AI. So a fairly nonlinear path. But -

**Nathan Lambert** \[00:09:09\]: Yeah. Well back to what you were saying on the scientific stuff, I think the Galactica story has many angles, and you led on this.

I think if people go look at the paper, it\'s a very interesting paper, like you cite Galileo in the first sentence, and it really has a lot of early modern language model features and quirks. It\'s something that people don\'t remember that well.

I\'m very on the record saying the backlash was overblown. I think that was before there were clear habits and community norms around what language model demos should look like. So it was kind of in that teething phase.

But what was the actual goal that you wanted? You mentioned organizing the world\'s information. What was the goal and how close do you think the model came to accomplishing it?

**Ross Taylor** \[00:09:58\]: So there were several different things at once.

There were immediate product integrations we had in mind. We actually had an agreement at the time with Overleaf to be a "co-pilot for writing papers". We\'d have a really good LaTeX model in Overleaf, and whenever you wanted to include a citation, you could simply prompt for one.

More broadly, we imagined the future would be instead of..using more classical ways to find and extract information, if you wanted to learn about something like DPO, you would just prompt a language model to find out about it. Or if you wanted to ask "What\'s the state-of-the-art on SWE-Bench?" or something like that, you would just prompt the model and it would find the relevant information and answer the question.

**Nathan Lambert** \[00:10:46\]: So this is something that language models are so bad at. One of my challenge questions - I\'ve been doing this for 6-12 months - is to ask models about DPO, and none of the models without internet access have yet done it right. You would think that it would start to kick in. And I don\'t just ask "what is DPO?", I ask "What is DPO for language model fine tuning", and they still just make up nonsense.

**Ross Taylor** \[00:11:06\]: Yeah, which actually relates to an interesting debate about LLM creativity. If you want to solve something like LLM creativity, you want to be confident about the frontier of knowledge, but frontier knowledge is where you have the most token scarcity.

But anyway, just to finish that thought. Bear in mind, we were developing Galactica while the whole Web 3.0 boom was happening. And we were in this weird state where we were like "All everyone is talking about is Web 3.0, but clearly generative AI is going to be the thing that powers the next generation of the web!". So I guess that was our primary motivation.

Now, in terms of the \[Galactica\] launch, I think there\'s two aspects.

First, like you said, the paper. Now we were a small team of 7-8 people. We had so much fun developing these new ideas at the time: internal reasoning tokens, how do language models cite, training for multiple epochs...

**Nathan Lambert** \[00:12:00\]: What\'s that? A citation token? Did you have a special token for citations?

**Ross Taylor** \[00:12:04\]: Yeah. So we had a start citation token \[START_REF\], and we used two methods. The first was: we\'d put the title of the paper within the citation tags. And the other one was: we\'d have an alphanumeric ID.

The interesting thing was, it actually worked really well - but in the demo interface, it had a tendency to hallucinate - or "hallucitate". The backstory is that, while the model was really good, for the demo we turned up the temperature to 0.7 so the text generation was better \[at the expense of citation accuracy\]. So generative citations were something that people thought didn't work, but it was \[more an implementation issue\]. I guess that's an alternative road in history...

So there was the paper, which was cool, and there was the demo, which I would say was motivated by the realities of the time. This was pre-ChatGPT and, even within a big company like Meta, it wasn't a company priority to work on LLMs at all. So in our mind, our objective was - we were kind of deluded - being a team of 7-8 people, we were like...

**Nathan Lambert** \[00:13:08\]: This is how you have to operate if you want to be at the cutting edge. That\'s how great teams operate.

**Ross Taylor** \[00:13:13\]: So there were two objectives you could have had. The first is: you think that second-mover advantage is good. So you could wait for OpenAI to do something and then come in after and do it in an open way. And this is the path that actually worked for LLaMA. LLaMA was not state-of-the-art in any sense.

**Nathan Lambert** \[00:13:27\]: I\'ve been doing this. I mean six months ago, maybe OpenAI and Google wouldn't need to hire me because they know everything. But now I'm doing more interesting analysis where I\'d be hired at a different role - but in the open. Now I\'m like the person people look at. But I'm trying to tell people that "You don\'t understand! I\'m six months behind everyone!".

**Ross Taylor** \[00:13:49\]: Right, but to be clear, that's a really important role - because everyone should have a stake in the future. And that\'s what the open ecosystem gives people.

But our objective was this: we didn\'t want to be second; we wanted to be first. And we were kind of deluded because we were 8 people - compared to maybe OpenAI with 200 people where their whole bread and butter was language models. But that's why we were thinking "how do we move as fast as possible?". And in our mind, a demo might be premature, but it would also be a way to get lots of prompts and information quickly - to understand how people would be using the model. And essentially the calculus we took was, we knew the community might not be  ready for something like this - especially with the Meta branding - but we thought this was a way to get lots of information really fast and catch up given our position. Now in retrospect, history says that...

**Nathan Lambert** \[00:14:33\]: You kind of did that. I think Meta probably got the injection of language model reality from that. It\'s kind of like the Gemini backlash. I think the Gemini backlash - while it\'s obviously stupid execution - was potentially a good forcing function for Google\'s structure of their Gemini org - to really move everything into the way it is now. That made them be structured more like a serious language modeling org and less like Google, I think, which people don\'t want to hear\...

**Ross Taylor** \[00:15:07\]: For us it was just a risk we decided to take. We probably took a lot more risk than we should have done. But we just thought "obviously this is going to be huge", "LLMs are going to power the next internet", etc, so let\'s take a risk. And you know, if we ran the universe several times over - it would have succeeded in some of those runs. But \[in our universe\], the criticism, which was obviously overblown, reached a critical point where things didn't work out.

And then there\'s the story about the demo coming down, which - I'm not sure I'm able to talk about - but I think that is one of the things where, if people knew the true reasons, they\'d be like "what the fuck!?". But yeah, that\'s what happened...

**Nathan Lambert** \[00:15:44\]: Yeah, this is why any company that makes a demo now has block lists, where there\'s certain words that if they\'re in the prompt of the generation, you get a really, really stupid response. Even if it\'s like an open model, you just put like a little filter that\'s like, "you can\'t say the most obviously bad words".

**Ross Taylor** \[00:16:01\]: But we actually did that and that created backlash as well. Because if you have false positives, you actually exclude some words which aren\'t actually offensive \[in certain contexts\], right? And then you also offend people... so it\'s not a win-win situation.

But if I have to look back at it now, I think with any new technology, it\'s never going to be absolutely better than what came before it. With LLMs, the relative comparison is with search. If you're going towards search and information retrieval, you\'re prioritizing factuality as opposed to creativity, right? And the fundamental tradeoff with LLMs is saying, "I can trade off some amount of like factuality or 'closeness' to the corpus for some amount of synthesis and creativity".

I don't think that if we had a better model, it would have helped things at all. You could say maybe if \[Galactica\] had RLHF, would that have helped? I\'m not too sure given that the project came out of \[a big company like\] Meta. Meta has a really good reputation now - people appreciate the open work they\'re doing - but at the time, things like the 2016 election were still in people's minds. So I think the LLM revolution was never going to start at a big tech company, in my opinion. It was always going to happen at a company that had less reputational baggage. But I think it\'s pretty cool now that people see things differently. Because FAIR always had a really strong commitment to open science. It's good that they\'re finally getting the credit for that.

**Nathan Lambert** \[00:17:38\]: Yeah. I have two technical questions on Galactica that I find really interesting. One is from Luca Soldaini at AI2. He said that you mentioned that the Galactica log probabilities (when producing citations) were proportional to how far in the citation graph the current paper was to the cited paper. Do you have any more interesting comments on how the latent space of Galactica actually worked? Because that is cracking the most important question of a language model for science - building a better latent representation of how the scientific information is organized.

**Ross Taylor** \[00:18:12\]: Yeah. So there were a couple of aspects to that. The first thing is we had this really nice graph that showed, as we scaled the model, the distribution of citations became closer and closer to actual citations - which is what you\'d expect. But this was important for us, as our main worry was - because we were thinking about deploying to Overleaf - we didn\'t want to prioritize the most cited documents and create a "rich get richer" dynamic.

**Nathan Lambert** \[00:18:38\]: Google Scholar already does that. Were you re-indexing all the papers rather than building off like the Scholar graph or something?

**Ross Taylor** \[00:18:45\]: I think we were building off existing ones, using things like CrossRef...but there were lots of gaps that we had to fill. The other weird thing was that we saw some strange biases in the model. So if the model didn't know what to cite, it would sometimes cite a general review paper, which is really weird emergent behavior. It was like the model was saying "I don\'t know a specific example, so I\'ll just give you a general overview".

**Nathan Lambert** \[00:19:11\]: It\'s probably in the data.

**Ross Taylor** \[00:19:12\]: I think the thing that surprised me the most was multimodality. So we trained the model on SMILES formulae and protein sequences \[alongside natural language\]. And the thing that really surprised me was, we had tasks which we didn\'t explicitly optimize for - like converting a SMILES formula to a IUPAC name for a chemical. And if you actually looked at the attention as the model was predicting the next token, it would say something like "amino" and you could see in the chemical graph, it was explicitly attending to the relevant part of the sequence.

I found that amazing because we didn\'t train for it explicitly. That\'s the beauty of self-supervised learning. But I also found it highly ironic because some of the criticism of Galactica was "it's ungrounded". I was like "how grounded is this? The natural language tokens are literally attending to the underlying chemical structure!". So that was kind of cool.

And then the other cool thing was: if you prompted with a protein sequence and asked "what is the function of this protein?", the model was really good at answering those questions in natural language. That was awesome for me.

**Nathan Lambert** \[00:20:33\]: There\'s another prompting thing that I had known of \[for Galactica\], which was asking the model to do open-ended generation tasks. The models are still out there -  people can spin them up and do demos on their own - but if you asked it something that people think of for ChatGPT - e.g. write me a poem about a sad goldfish - it wouldn\'t work unless you put it in a header format. It was markdown, I think? If you prompted it in that format, it would actually do a great job.

**Ross Taylor** \[00:20:57\]: Yes, so in the Galactica demo, a lot of people were being malicious with this type of prompting for markdown articles. But I did enjoy some of the creative ones. Someone was like: write me a theorem on finding a girlfriend, and it was some of the most hilarious model output I've ever seen. And people also generated some amazing sci-fi...but then I think some people took it too far. But whatever. I guess it was a traumatizing experience for me at the time. But with the benefit of hindsight, I was also fun in some sense, I guess.

**Nathan Lambert** \[00:21:30\]: Yeah. It makes you understand the bigger context of the work much faster than you would otherwise.

**Ross Taylor** \[00:21:37\]: It was actually crazy at the time. So many people were using it. Even then we could see that - while it wasn't a product - we could see that most systems were going to be designed in a similar way.

I think the interesting thing was how the winning form factor in the end was like a chat interface - you know, with ChatGPT being the winning UX. I think that was actually a big part of the story \[why they succeeded\]. There\'s a debate on whether RLHF is actually a capability advance or whether it's just alignment...but a big part of the story \[for ChatGPT's success\], in my view, was the kind of UX of how you interface with a language model, rather than the actual capabilities. But I think it\'s obviously not monocausal at the same time. There were several factors at play.

**Nathan Lambert** \[00:22:25\]: Yeah. So the last thing on this is that you mentioned in our e-mails about language models, creativity and making discoveries. What do you mean by that? Is that the agent-like projects you worked on at Meta?

Agents are largely something that I don\'t have too much comment on. I\'m taking the approach of wait and see what we actually get, because there are a lot of practical approaches that I think will be reasonable. People use language models for basic formatting, for code, etc. But it\'s easy that if they have a little bit more feedback for things like writing a paper - e.g. find me a citation for blank and justify your answer - that step is something that I think will come. I don\'t know how expensive it will be to run, but is that what you mean when you think about making discoveries? Is it more autonomous? Is it a grander vision? Anything like that?

**Ross Taylor** \[00:23:18\]: I think it\'s more like this: the killer use case right now is information synthesis. For example, I use Claude a lot more than Google now because it combines information in a better way and sometimes generalizes well to things it hasn't seen before.

But a really cool thing would be: can a language model answer a question which is more out of distribution? That we don\'t see in the training data?

So an experiment I\'ve never done because I didn\'t have to compute would be this. Imagine if you could train a language model on all documents up to 1905, which is the year when Einstein had his miraculous year of four seminal papers. With that model, which is trained up to 1905, could you prompt the model to come up with a good explanation of the photoelectric effect, special relativity, this kind of stuff? And what would it take to rediscover these things?

Because presumably, with all these major discoveries, it's never out of the blue. You're standing on the shoulders of giants, but there's still a lot of thought and inspiration you have to do to get to those great ideas. So that\'s the setup. But the creativity problem is, by its very nature, hard to benchmark.

Maybe this is a digression, but my problem with the field right now is: we're in a situation where we\'ve almost solved a benchmark like MATH, which is a very hard benchmark, in my opinion, at least Level 5 MATH, but I don\'t think we\'ve really cracked something like reasoning. So I think it\'s like a whole different question about how you even evaluate these frontier tasks. But yeah, hopefully that gives a flavor of the kind of questions here...

**Nathan Lambert** \[00:24:58\]: Yeah, we can go into the reasoning conversation. I think reasoning in RLHF will take up however much time we want to keep talking. I guess we can start with the basics. What do you think people that are using language models think reasoning means? And what is the way that you would interpret what you\'re trying to do in improving the reasoning capability of a language model?

**Ross Taylor** \[00:25:21\]: So there\'s a lot of controversy on this on Twitter/X. And I think people are talking past each other because sometimes people mean different things by reasoning. At a very granular level, is legal reasoning fundamentally the same thing as mathematical reasoning? Common sense reasoning? I guess my very basic definition is that reasoning is the process of drawing conclusions based on a body of observations, or in the case of deductive reasoning, basic premises.

**Nathan Lambert** \[00:25:50\]: So math is like a subset of what you think about.

**Ross Taylor** \[00:25:53\]: Yeah. And then I guess the bigger circle is the broader topic of outcome directed behavior. I have an idea of an outcome I want to achieve, but what\'s the best path to get there?

And then in the LLM space, I think this problem broadly equates to the technical problem of how you use compute to get from your question to your answer. In the old days, you would just  prompt the language model directly. You would just put in a GSM8k question, put in "Answer:" and then parse A, B, C, D. So you\'re relying on the forward pass.

**Nathan Lambert** \[00:26:27\]: Yeah, like the FLAN data is really weird. That\'s a popular one that people used to train on this stuff.

**Ross Taylor** \[00:26:33\]: Yeah. And then came chain-of-thought, scratchpads, \<work\> with Galactica...all these ideas of using the context window to do intermediate computation. And the more recent, although to be honest, it\'s actually quite an old idea, is: you have chain-of-thought, but how do you better learn the internal reasoning tokens that get you to your answer? So things like, you know, Quiet-STaR and variants of this idea.

**Nathan Lambert** \[00:27:01\]: Claude now shows you when it's thinking, and in the Claude system prompt, it has information on how many tokens to take to think about a question. We\'re all thinking about trying this stuff and it\'s all so hard.

**Ross Taylor** \[00:27:11\]: I think it\'s a question of how do you learn those tokens? For us, the original \<work\> thing we did was just supervised learning. So we trained on some examples and let the model generalize to know that it should do the thinking in between some tokens. There are more sophisticated ways you could achieve this nowadays.

Another point is this: there's an analogy that's often used about language models, that they are "thinking out loud". I actually don't like this analogy at all. I think "thinking out loud" makes you think there's something wrong about this kind of thinking in token space. But it's not clear to me that the alternative - or these old adaptive computation ideas - are any better, actually.

**Nathan Lambert** \[00:27:58\]: What do you mean by adaptive computation? Because I mostly think of "thinking out loud" as being like chain-of-thought or generating its own explanation before it gets to an answer. What would adaptive computation be?

**Ross Taylor** \[00:28:09\]: So there\'s a paper by Alex Graves, who wrote all these amazing papers \~10 years ago, which had a lot of foresight. He did stuff like the Neural Turing Machine paper. Adaptive computation is the idea of, instead of having fixed compute between your input and your output, you can extend the forward pass to do things better, like arithmetic, where you have to maintain/manipulate state.

When chain-of-thought came out, there was an impression that it was a bit of a hack, because you\'re thinking in token space whereas you should be finding a way to make the forward pass dynamic. Universal Transformer is another variant of this \[adaptive computation\] idea. But I think there needs to be more empirics on which approach is actually better to maintain and manipulate state. I used to be more in favor of thinking, OK, chain of thought is more of a hack, but now I actually think it\'s probably...

**Nathan Lambert** \[00:29:02\]: What do you mean by state, like the state of the problem in that sense?

**Ross Taylor** \[00:29:08\]: So imagine that you\'re doing a GSM8k question, where John originally had 100 apples, then Jane gives him five apples. He has 105. And then he gives 20 away to like Susan or something and he\'s left with \[85 apples\].

So if you're prompting the language model directly for the answer, you\'re expecting the language model in that forward pass to maintain and manipulate the state in a latent space, whereas the way chain-of-thought does it is in token space.

So you essentially output the intermediate steps. One of the problems with reasoning is that we have no idea how humans mechanistically reason...but if you think about how you\'d solve a GSM8k problem in your head, then to me this seems a lot closer to something like chain-of-thought than adaptive computation.

**Nathan Lambert** \[00:29:57\]: Especially when you look at the architecture and attention mechanisms. A Transformer is really good at copying. So if you keep feeding in the recent information, it copies that in some way. So I think chain-of-thought and all of these things, I mean, they\'re only growing in popularity in my mind, along with Quiet-STaR and these kind of methods. I've heard the rumors about self-explanations and all these special things. The LLaMA-3 paper has all these special tokens. I don\'t know what all of them do, but I can see the direction. The state is stored in context and in special formatic tokens if it needs to be.

**Ross Taylor** \[00:30:37\]: So the other big picture thing is this. With the internet, you're only seeing the output context.

So take StackExchange. If it's a good answer, the author probably hasn't just responded by generating words left-to-right. Maybe they've looked something up, maybe they've done a back-of-the-envelope calculation, either explicitly or in their head, right? And the internet is missing those "internal tokens", essentially.

Now this isn't always a problem because the models can learn how to construct them. And the effort now is to make artificial latents / internal thought, through RL or otherwise. But I think this is actually a much bigger question, which is more than just reasoning. In the end, as models become more capable, we'll be talking more about how we can make them human-like in the way they can answer questions and solve tasks. For example, in some situations we might like the models to have \[human-like\] empathy, which is also "missing" in some sense.

So my prediction is that this becomes a bigger deal in the next few years: caring more deeply about the computation these models perform to reach a conclusion. And that will be the essence of alignment, in my mind. But that\'s a big topic!

**Nathan Lambert** \[00:31:50\]: OK, I have a long list of specific questions on this. My first question is about process reward models.

I think the canonical paper is "let\'s verify step by step". My whole gripe is that it's hard to create the data. That's why they don't exist in the open. But I'm guessing you can just label data with GPT and ask for feedback on each step, and just use that as an "LLM-as-a-judge" to get reasonable step-by-step labels on process rewards. But there's so little work on this, so I don't know if it is worth exploring. There is some research from Meta - I think Alex Havrilla did a couple of internship projects which related to this, and he's good - but there's such a lack of signal.

Is this something that people should work on more, or is it too complicated? Are there simpler things to do?

**Ross Taylor** \[00:32:38\]: Our big direction was integrating outcomes into reasoning - because next token prediction isn't the objective we actually want to optimize. So the two ways to integrate outcomes are through something like PPO or inference-time search. And in both cases, you want a good reward model or value model.

Instead of (human-annotated) "process based reward", we were exploring ideas along the lines of Monte Carlo policy evaluation (MCPE), where the key problem is how to learn a value model. It's maybe a separate topic, but it's underappreciated that something like MCTS - which in the public imagination is this inference-time search technique - actually has its real magic in giving you a value network for free.

This is why it was introduced in Go, because humans couldn't come up with good heuristics for evaluation. So if you have something like MATH where you know the answer, then the question is how do you assign step by step feedback? It doesn\'t have to be MCTS, but something where you backprop the outcome to these individual steps is a way to get this dense feedback.

That\'s a way to get "synthetic process reward". I should stress that PRM and MCPE are actually different things. Alex Havrilla was doing something along these lines also - but anyway, hopefully this gives a sense of the approach we took.

**Nathan Lambert** \[00:34:21\]: When Q\* came out, that\'s something that I thought it might be doing. Instead of chain-of-thought, there\'s this idea of tree-of-thought. You could swap in the reasoning steps. And then if you could get labels on all these reasoning steps, you're doing search over a reasoning space - which I would expect to work, but I think it needs the right datasets. I think a large part of the open alignment community right now is underappreciating datasets, where there\'s a lot of focus on methods, but we don\'t even have the datasets to use the methods... Like, why are you coming up with seven DPO variants if you don't have the right datasets? I understand academic incentives, but if you are not an academic, you don\'t need to be doing that...

**Ross Taylor** \[00:35:00\]: It\'s an interesting question, because I guess the first chapter of LLMs had a lot of reliance on human annotations. In a way, that\'s a barrier to entry for the open community, because big firms can afford to pay millions for it but open source developers can't. But more recently, you\'ve had the rise of things like constitutional AI \[and RLAIF approaches\], which I believe are comparable to human-annotated datasets anyway. So is that a good thing for the open community?

**Nathan Lambert** \[00:35:31\]: I think it is, but human preference data might be a leg that is hard to remove. One of my latter questions was: can we actually do LLM-as-a-judge for human preference data fully? I think is the critical step that we don\'t have an answer for. Everything else in the modern RLHF stack is becoming more reproducible in the open.

And that relates to a question I have on synthetic versus human SFT. I think Thomas \[Scialom\] said on the Latent Space podcast that we just use generations from the model because they\'re better for humans on a lot of SFT tasks. Apple had a quote in their foundation model paper saying the same thing.

So I'm thinking, shouldn't we be redoing all of our generations for our SFT dataset with the latest GPT-4 or LLaMA-405B? Why are we using GPT-4 from March 2023? That model was not as good on reasoning. So we have headroom there on synthetic data. We have prompts that we could reuse, but we don\'t have the right preference datasets - datasets like UltraFeedback are not big enough. And I think they\'re not in the same style that a lot of labs are doing this preference tuning - where it\'s on-policy generation.

We tried to work with Scale at Hugging Face to do this, where we had our own SFT models. We were getting data from Scale. We were labeling it every week and we were trying to retrain the models and we weren\'t getting a signal. This was last July/August. So we just didn\'t really know what we were doing. But I suspect that what people in the open should be trying to do is generating a lot, labeling it...That was a light bulb moment for me recently. This is what we have to do, but no one has done it.

**Ross Taylor** \[00:37:21\]: Yeah, I think it\'s definitely underappreciated how you can get better answers than a human by sampling the models \[enough times\]. You mentioned that Thom made this point early on in the \[LLaMA\] project, but you\'d be surprised how this extends to reasoning as well. Even with the Galactica model - which is now an ancient model, a bronze age model - the pass@100 on GSM8k was 98%. And it\'s absolutely crazy to me that even now people are using GSM8k as a benchmark. In my mind, that benchmark was solved several years ago.

It's a subtle point because the zero shot performance was \~48% but the pass@100 was 98%. The insight there is that the model already has knowledge about how to answer correctly, it\'s simply not reliable. This tells you that you need to invest in reward models, process based reward, outcome based reward, everything we talked about earlier...

But the same applies to the general RLHF pipeline. If you asked me to write a poem in the style of Bertrand Russell but also mix in Snoop Dogg's style, then I couldn\'t do that. But the model has knowledge of how to do that, right? So why wouldn\'t you sample the model?

I think now with LLaMA-3, and the 405B model being out, it's going to be good for the community that they can use it for generating data synthetically. And I\'d imagine the quality will be good enough if it\'s done the right way.

**Nathan Lambert** \[00:39:30\]: Yeah, I think it should be doable. But there\'s a fundamental question of what do we think the human preference data is doing? \[Compared to\] model labeled preference data, is the noise that the humans provide of a different distribution that makes the human preference data better? I don\'t have a lot of signal on this, but I would love to know because I would guess that Meta would love to eliminate the \$10 million plus estimated human preference data spend if they could. Meta is a reasonable company...

**Ross Taylor** \[00:40:23\]: Yeah, I don\'t know. But here's something that surprised me. I was originally skeptical - at least on the reasoning side for LLMs - about LLMs marking their own homework. I thought they would eventually have that capability, but I wasn't sure...

**Nathan Lambert** \[00:40:40\]: how fast.

**Ross Taylor** \[00:40:41\]: But the interesting thing we saw was as follows. We had experiments where we'd have a LLaMA-2 model that we'd sample generations from to train ORM models, and then we'd train different reward models on this data with different base models.

What we saw is that, the better the (underlying) base model, the better the reward model was for evaluating. And there were very clear patterns we saw: as the base model scaled, so did the quality of the reward model.

So that tells you that the knowledge is not in the ORM samples that you\'ve fine-tuned the base model on. The knowledge on how to judge is within the model itself. And the pattern was so clear in the scaling. I concluded that eventually these self-verification approaches would work. It was just a question of when they would start to work for different types of problem.

**Nathan Lambert** \[00:41:31\]: Yeah. Model capabilities are also getting more dense which helps as well. Like with smaller model, there\'s all these experiments with better data, showing that you get a better model with X% reduction, which is kind of off-topic...

To double-down on what you said, I think this is one of the things I also debate: what makes a good model for downstream fine-tuning? I think in the LLaMA-3 report, they train the reward models directly on the base and not on the SFT model. The Apple report mentioned that they don\'t just use their evaluation suite for SFT models, but they evaluate with a reward model to see what is ready for RL.

I think, especially in the open, if you want the people to adopt your base model, there\'s a big gain in making it easy to fine-tune. For example, LLaMA has been pretty good; LLaMA-2 especially was really good for fine-tuning. There\'s also been base models that don\'t really work for fine-tuning, partially due to bugs and partially due to the state of the optimization. Is this something that you have any insight into?

**Ross Taylor** \[00:42:43\]: Yeah, I don\'t think I have enough insight into it to say, but I think it\'s definitely something that\'s been undervalued. I think the view of a lot of open model providers is: you get the model out, get good Open LLM Leaderboard results, and it\'s mission accomplished. But the real evaluation is in two days time when you get anon accounts on X saying "I\'m fine-tuning this LLaMA model, it\'s not working". And when you see a pattern with this kind of behavior, you have to conclude something is wrong...

**Nathan Lambert** \[00:43:11\]: It\'s always a chat template thing. A lot of it is a chat template thing, but those problems do get ironed out eventually. There\'s this whole idea of annealing and staging pre-training. I can\'t tell if it is boosting current capabilities at the cost of later capabilities. I think in a few years, this will all shuffle out and it\'s just how we do evaluation in stages. So you\'re always going to optimize for the right metric.

**Ross Taylor** \[00:43:50\]: There\'s two points to that.

The first is about annealing. It works for the kind of benchmarks people focus on the most, but then there\'s a question of whether you are actually just collapsing the task distribution of the model to things you\'re measuring - and not the true task distribution used by the community.

And I think there\'s a second point - which is maybe too much of a digression - but there\'s an interesting debate to be had about data quality being a bit of a misnomer. In a sense that when we say "data quality" we\'re actually saying "this data mix works well on these benchmarks". But if you take a "No Free Lunch (NFL)" kind of approach to this, you must be hurting task performance somewhere else, right?

**Nathan Lambert** \[00:44:34\]: Yeah, I think I'm on the record of being an AlpacaEval hater. I say this all the time, because I think AlpacaEval is sacrificing actual usefulness for their own metric. If you get a 1-2% bump on alpaca eval, maybe that's great. But you could be getting a 10-20% bump while sacrificing actual chat abilities.

We released some models trained with PPO and our PPO models are not very good at instruction following because they don\'t follow modifications like be concise or some stylistic things. They\'re also so yappy. They just say so much...but they do well on metrics and PPO especially helped AlpacaEval. So we had to figure out how to kind of use that signal without overcooking it.

**Ross Taylor** \[00:45:16\]: Yeah, it\'s like a whole discussion about evals, I guess...

**Nathan Lambert** \[00:45:21\]: We could come back to evals in a second. The last question that I have is: there\'s multiple trends like LLaMA-3 downplayed the importance of instruction fine-tuning relative to RLHF. I think there\'s other quotes in \[Thom's\] LatentSpace podcast talking about it. Nematron also had this report where they use SFT and then multiple stages of RLHF.

I think DPO versus PPO is overblown and that\'ll kind of be a wash eventually. Everyone knows DPO\'s advantages of being simpler. But my question is this: are there certain capabilities that only come for RLHF, and people trying to do them with SFT are just wasting their time?

I always thought safety was in this bucket where it kind of makes sense - it's hard to train a model to refuse just with SFT. But with something like reasoning, are there certain sequencings where SFT primes you and then RLHF really helps reasoning or code? Because it seems like OpenAI is really leaning on PPO to help with reasoning and code?

**Ross Taylor** \[00:46:45\]: Yeah, I think there\'s two ways to answer this question. First, maybe the history of this debate on the LLaMA side, and then something on the reasoning side.

So the history is quite interesting. I would say, you know, when was it? 2023? My dates have been wrong since the pandemic...But this just was after ChatGPT. There was actually a debate internally in Meta about using RL, and a lot of senior people were very skeptical. I would say the view was...

**Nathan Lambert** \[00:47:13\]: Not just at Meta. You can see when different companies embraced RLHF, if you really start to look at their models...

**Ross Taylor** \[00:47:22\]: The view was that RL was a dead end. And that even DeepMind was moving away from RL at the time, so you should just do SFT.

But, you know, at least for the folks in the Galactica team that came to lead post-training for LLaMA, we were quite scarred by hallucinations! We were definitely of the view that we needed to have the right objectives, and that we needed to make sure language models could "know what they don't know". So we were quite high on RL from the beginning. And eventually, I think the LLaMA-2 paper showed that a lot of the advances in helpfulness/harmlessness were via the RL stage. So I think that approach was fairly vindicated.

On the reasoning side, I would just say it's quite simple. It comes back to the next token prediction objective not being the actual objective you want to optimize. The objective you want to optimize for reasoning is: do you get the right answer or not? Especially since reasoning is a high precision task. If you get one token wrong, unless you have a backtracking capability, you're never going to recover...

**Nathan Lambert** \[00:48:32\]: That\'s a throwback, the backtracking token. Sorry, that was a random paper! That is interesting...

**Ross Taylor** \[00:48:38\]: Yeah, all these weird methods... But I think on your question, there is a point at which these techniques kind of overlap, right? So if you\'re, you know, doing SFT with rejection sampling: you're doing something close to PPO anyway. And the same for reasoning: if you sample the model and pick the trajectories that your verifier says are correct, and then do SFT on that, it is a form of RL.

The final point I'd make is this: I would say the community overreacts to certain methods being used by popular models. They think: this company uses DPO because they must have found it\'s fundamentally better. But actually, it\'s usually due to either practicality or...

**Nathan Lambert** \[00:49:22\]: Yeah, that\'s what I think.

**Ross Taylor** \[00:49:24\]: You have a 405B model, and if you want to do PPO, you need to have a policy model, a reward model, value model etc in memory, and it's not like...

**Nathan Lambert** \[00:49:33\]: Especially with DPO. I think with the 405B, I\'m guessing what you did was cache the reference model. You could cache the log probabilities from the reference model. So you don\'t need to keep them in memory when you\'re doing the loss of the primary model. For DPO, you don\'t even need an extra copy of the model in memory, which therefore means you can use the same exact stack that you use for training. So you don\'t have to comment on this. But I think that\'s probably partially why LLaMA-3 just used DPO\...

**Ross Taylor** \[00:50:07\]: Yeah, I think people don\'t appreciate how compute works either. People assume the big companies have so much compute - tens of thousands of GPUs - so compute isn\'t a constraint. But all these things are subject to Say\'s Law, right? If you have more compute, you\'re going to train a bigger model. And then you\'re going to hit the constraints again. It's like the old thing of trying to solve traffic by building another lane. But if you create another lane, people will use that lane of traffic.

So practicality is still a factor \[behind choosing methods\]. Also things like which researcher is in charge, what's their favorite method, and also politics as well.

So I think the community has made a mistake of overreacting to these choices. There was a mixture-of-experts phase too, right? I don't think there's anything inherently better with either method (dense or MoE), they just have different trade-offs, and it depends on what you are trying to achieve. If you're serving lots of people with inference, then maybe a MoE approach is better. If you're optimizing for something simple that's easy to train and gets good results, maybe you favor a dense approach - although that's debatable whether it's easier to train. But I don't think these things are clear cut.

So I would encourage people to not just copy things because they\'re in a paper from a big lab. I would encourage people to try things out themselves to know what works, and figure out what the problem is that you're *really* trying to solve.

**Nathan Lambert** \[00:51:20\]: I think people don\'t have enough long term direction in their decisions. People are not trying to make decisions about what will be right in 10 years, they are trying to get a model out as soon as possible. So there are very few people with the incentives of trying to understand in the asymptote, which method is better... I might have that incentive, because I\'m a nerd, and I have an audience that is okay with me writing four paragraphs around esoteric nerdy topics, but for all these companies, that is not a real incentive.

**Ross Taylor** \[00:51:53\]: The other point I'd make - maybe it is a separate thing - is this. I made this mistake throughout my career of focusing too much on novelty and complexity.

So in my first job in sports betting, we were making models for horse racing, football, that kind of stuff. And I always had the perception that other funds had really advanced, cutting-edge, complex models - but that wasn't the case at all.

I think there is this tendency within deep learning to assume that - especially for the secret labs - that their good performance is due to some secret, amazing method. But more often than not, good performance is due to lots of small things from different people combined into one model. Really, lots of simple things done well and solid execution. And frankly, for big firms a lot of brute force too, right? Because big companies are naturally slow. But once they find a way to mobilize resources, they're very intimidating and hard to beat. If you're in a big company, and you're aware of this, which approach are you going to take: are you going to prioritize novelty or are you going to do brute force if you have 10,000s of GPUs?

So I would encourage people not to be too intimidated by this perception that the big labs are smarter. I don't think they are.

**Nathan Lambert** \[00:53:03\]: They\'re earlier but they\'re not necessarily smarter.

**Ross Taylor** \[00:53:09\]: Yeah. So obviously the constraints are different because of less compute in the open, but still: you've got to use first-principle thinking and be empirical as well, and just follow that path.

**Nathan Lambert** \[00:53:21\]: Yeah. So following up on this, there\'s a lot of discussion around what the processes are for making a successful foundation model lab. I think Armen has been talking about a few things on Twitter with great visualizations around de-risking pre-training based on FLOPs efficiency. Do you have any comments on what makes a successful post-training team and project?

I\'ve talked to John Schulman a couple of times - he\'s been the king and started all of this - and OpenAI is still looked at as being the leader in the space. I think they\'ve always been top on Chatbot Arena, and have cracked what most people like in the style. They started early. Are there different considerations for the post-training side of things rather than the pre-training side that we might hear more about?

**Ross Taylor** \[00:54:13\]: Yeah, there\'s probably better people than me to answer. So in our team, originally like Robert (Stojnic), my co-founder, he was kind of managing the post-training team. And then I\'d say Thom Scialom was doing a lot of the work. And then more recently Rui Hou - he kind of flies under the radar a bit - but he's been doing a lot of the work. They are all better placed to answer than me, since I was focusing on reasoning and agents.

But I think the key thing is this: post-training is just a lot of iteration. Frankly, lots of hard work - e.g. making sure at each round of RLHF you're not regressing in certain ways, filling holes, etc. I guess it's hard to put a finger on a single thing, but...

**Nathan Lambert** \[00:54:58\]: There\'s simple things like I\'m trying to get people to talk about more. I'm trying to establish a good vibe test about internal culture. How do you vibe test for a good post-training culture (or for reasoning)? I remember somebody at Anthropic told me there's still a lot of cases where you just put your finger up to the wind and you\'re like "model good". And I\'m sure that is still happening. And that\'s just a simple cultural thing of telling the team that you can't always trust all of your numbers.

**Ross Taylor** \[00:55:26\]: I think it is maybe a more fundamental question. I wasn't there at the early days of FAIR - I came in 2019, but FAIR was always a very bottom up organization. Which is a great thing: that\'s why things like PyTorch emerged. But the real insight as to why OpenAI was ahead historically, at least until recently, was that they had more of a top-down culture and focused bets. They saw the potential of LLMs early on and it was a top-down prerogative of the company to focus on that. And in essence, it was more of an engineering problem than it was a research problem in a lot of ways.

Relatedly, I think a lot of people were surprised that the LLaMA-3 paper wasn\'t as "novel" as they were expecting. But that just reflects the fact that a lot of it is just engineering and engineering is really hard - a lot of hard work. Not always a lot of new methods, but it is a lot of hard work.

**Nathan Lambert** \[00:56:22\]: Yeah, we\'re starting our next fine tuning model and everyone\'s asking me: "what should we work on?". I\'m trying to tell them "we just have to filter data and generate more completions". We'll have a lot of prompts, we have to filter them, generate completions from good models, and then we'll have to generate more completions and keep doing this process...And in 10 weeks, we\'ll probably have a very good open model. We'll just have to be boring for 10 weeks! And we have like 10 people involved.

So it\'s a bit of a bigger project, which I think is the right way to do it. We have just started getting improvements on IFVL by copying Nemotron. We use some open math datasets and the math scores are getting closer to LLaMA. It is really the simplest things ever. It\'s like browsing Hugging Face and being like, "NVIDIA released some JSON format data, some instruction format data, like we add it in and the numbers go up".

**Ross Taylor** \[00:57:16\]: Yeah, I think I said earlier, but it raises an interesting question where this kind of approach - of grinding until the open LLM leaderboard numbers get to 100% - I think we're going to get to a situation where all the benchmarks are solved, but where we haven\'t really, in my mind, at least solved intelligence.

What does it mean that we\'ll get close to 100% on MATH, you know, without any inference time search? I think sooner or later, while it looks like we're on an exponential with LLMs, we'll realize we're actually on an S curve. Eventually we\'re going to get back to this mode where we have to do new things. And I think that\'s great, because that\'s what motivates me.

But yeah, I think there\'s waves, and we're in this heavy exploitation mode right now with LLMs - away from the glory days of architecture exploration. But my hope is that we\'ll get back to the stage where, after exhausting all the \[current\] benchmarks, we say: OK, now we need to do something completely different. But who knows?

**Nathan Lambert** \[00:58:26\]: I see it similarly. I think we still have a year or two, at least in the open. If the closed models start saturating and they start doing things differently, that\'s fine. But eventually it\'ll all get there. And in that phase, I mostly keep working just to make sure that the ecosystem doesn\'t fold in on itself. So that\'s probably the one-sentence summary of what I\'m doing these days: add transparency so that regulatory capture doesn\'t nuke everything. And that\'s fine, but I think it\'s still going to be longer than people expect. I don\'t think we have true signs of saturation at the top. We\'ll see what GPT-5 does - if GPT-5 never comes out - and then we'll really know.

But it seems like it\'s going to come. I think there\'s enough signs that it\'ll come eventually. I think I don\'t know the answer to this - and it\'s not really our expertise - but I\'m interested in the potential architecture of GPT-5 and if it\'s GPT-4o like and they\'re using more multimodal data to try to keep the data engine going relative to just going bigger. I don\'t know the answer, but that\'s kind of the future questions I'm thinking about.

**Ross Taylor** \[00:59:34\]: In my mind, like three years ago, the thing on the horizon I saw was agents. That's where a lot of people are working right now: long form tasks where an agent doesn\'t have to answer a question immediately, and \[can instead\] go away for a while doing some research and answer later. I think that will take up a lot of time in the next five years.

It\'s both a compute problem of bigger models - more scale will do better - but also a data problem of how do you generate these trajectories? How do you get reliability? So it's more successful and less error-prone at each step. And I think in principle it\'s solvable, but I just think it would take some time.

**Nathan Lambert** \[01:00:18\]: Yeah, it seems that engineering is required. It doesn't seem like something that\'s just going to emerge. It\'s building a whole system and scaffolding around agents. Just unglorious work.

**Ross Taylor** \[01:00:32\]: Yeah.

**Nathan Lambert** \[01:00:34\]: OK, anything else you want to add? Do you want to get people excited about your start-up or is it too early? Maybe too early, yeah?

**Ross Taylor** \[01:00:43\]: Yeah, what else should I say? It has been nice to step back for a bit and look a bit ahead into the future. For me, my best days creatively were my teenage years when I got back home from school and spent the rest of the day programming. It's quite nice to feel like that again: to be in that zone again where I can shut the world out and do some work.

But maybe just to give a hint of the areas I\'m interested in, I think it comes back to this problem of how alignment is going to be a process of making AI more human-like. For example, how do you control for things like deception - which Anthropic has done a lot of really good work on.

Essentially... the latents of AI are \[potentially\] misaligned with human latents, and the question is: what do the human latents look like anyway? And how do we model these things?

That is very abstract and high level, but that is the fundamental question I want to work on. But yeah, I think I can talk about it later in the year!

**Nathan Lambert** \[01:01:49\]: Yeah, sounds good. Thanks for coming on. This was great. I think people are going to get a ton out of this. I think just a very sensible conversation on fine-tuning, reasoning and some of the things that got us here. And that\'s what I was hoping to get out of it, so thanks again!

**Ross Taylor** \[01:02:06\]: Yeah, great to talk, Nathan. Have a good one!
