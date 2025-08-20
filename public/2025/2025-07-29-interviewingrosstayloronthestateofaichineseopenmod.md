---
title: "Interviewing Ross Taylor on the state of AI: Chinese open models, scaling reasoning, useful tools, and what comes next"
subtitle: "Interconnects Interview #14. Ross's second time on the show."
date: 2025-07-29
type: podcast
audience: everyone
visibility: public
post_id: 169528257.interviewing-ross-taylor-on-the-state
email_sent_at: 2025-07-29T13:35:44.001Z
---
I'm excited to welcome Ross Taylor back on the podcast (and sorry for the lack of episodes in general -- I have a lot going on!). The [first time](https://www.interconnects.ai/p/interviewing-ross-taylor-on-llm-reasoning) Ross came on we focused on reasoning -- before inference-time scaling and that sort of RL was popular, agents, Galactica, and more from his Llama days. Since then, and especially after DeepSeek R1, Ross and I have talked asynchronously about the happenings of AI, so it's exciting to do it face to face.

In this episode we cover some of everything:

-   Recent AI news (Chinese models and OpenAI's coming releases)

-   "Do and don't" of LLM training organizations

-   Reasoning research and academic blind spots

-   Research people aren't paying enough attention to

-   Non language modeling news & other topics

Listen on [Apple Podcasts](https://podcasts.apple.com/us/podcast/interconnects-audio/id1719552353), [Spotify](https://open.spotify.com/show/2UE6s7wZC4kiXYOnWRuxGv), [YouTube](https://www.youtube.com/@interconnects), and [where ever you get your podcasts](https://www.interconnects.ai/podcast). For other Interconnects interviews, [go here](https://www.interconnects.ai/t/interviews).

:::::::: {#youtube2-Kn0xgijnmz8 .youtube-wrap attrs="{\"videoId\":\"Kn0xgijnmz8\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=Kn0xgijnmz8){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

Show outline as a mix of questions and edited assertions that Ross sent me as potential topics.

### 00:00 Recent AI news

*Related reading is on [Kimi's K2 model](https://www.interconnects.ai/p/kimi-k2-and-when-deepseek-moments), thoughts on [OpenAI's forthcoming open release](https://natolambert.substack.com/p/some-thoughts-on-openai-returning).*

-   What did you think of [Z.ai](http://z.ai)'s GLM 4.5 model (including MIT licensed base model) with very strong scores? And Kimi?

-   What will OpenAI's open model actually be?

-   What do you make of the state of the ecosystem?

### 12:10 "Do and don't" of LLM training organizations

*Related reading is on [managing training organizations](https://www.interconnects.ai/p/how-to-manage-ai-training-organizations) or the [Llama 4 release](https://www.interconnects.ai/p/llama-4).*

This is one of my favorite topics -- I think a lot of great stuff will be written on it in the future. For now, Ross asserts...

-   Most major LLM efforts are not talent-bound, but politics-bound. Recent failures like Llama 4 are org failures not talent failures.

-   Most labs are chaotic, changing direction every week. Very different picture from the narrative presented online.

-   Most labs represent investment banks or accountancy firms in that they hire smart young people as "soldiers" and deliberately burn them out with extremely long hours.

### 36:40 Reasoning research and academic blind spots

*Related reading is [two](https://arxiv.org/abs/2506.10947) [papers](https://arxiv.org/abs/2507.10532v1) point questions at the Qwen base models for RL (or a summary [blog post](https://www.interconnects.ai/p/reinforcement-learning-with-random) I wrote).*

I start with: What do you think of o3, and search as something to train with RL?

And Ross asserts...

-   Most open reasoning research since R1 has been unhelpful - because not enough compute to see what matters (underlying model and iterations).

-   Best stuff has been simple tweaks to GRPO like overlong filtering and removing KL divergence.

-   Far too much focus on MATH and code - AIME has tens of samples too so is very noisy.

-   People are generally building the wrong kind of environments - like puzzles, games etc - instead of thinking about what kind of new capabilities they'd like to incentivise emerging.

### 50:20 Research people aren't paying enough attention to

The research area I hear the most about right now is "rubrics" -- a per-prompt specialized LLM-as-a-judge to replace reward models. SemiAnalysis [reported](https://semianalysis.com/2025/06/08/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data/) OpenAI scaling this approach and [lots](https://arxiv.org/abs/2507.17746) of [great](https://arxiv.org/abs/2507.18624v1) [research](https://arxiv.org/abs/2505.13388) is coming out around it.

I start with: What do you think of the state of RL scaling and generalization? What of models losing

Ross asserts...

-   Rubrics are underhyped on social media - they were driving force behind projects like DeepResearch - and GenRMs are interesting but perhaps slightly overhyped.

-   There is an evals crisis - there are not enough high quality evals, particularly for frontier tasks like automating research and real life work. Impediment to anyone building agents or ASI.

### 01:02:46 Extra stuff!

I ask Ross: What AI are you using today? Why?

To conclude, Ross wanted to discuss how AlphaEvolve has been underhyped on social media, and means the future isn't just RL. Shows there are other effective ways to use inference compute.

## Transcript

*Created with AI, pardon the minor typos, not quite enough time this week but I'm hiring someone to help with this soon!*Nathan Lambert: Hey, Ross. How\'s it going? Welcome back to Interconnects. I took a many month break off podcasting. I\'ve been too busy to do all this stuff myself.

Ross Taylor: Yeah, I was trying to think of all the things that happened since the last time we did a podcast a year ago. In AI time, that\'s like two hundred years.

Nathan Lambert: Yeah, so I was looking at it. We talked about reasoning and o1 hadn't happened yet.

For a brief intro, Ross was a co-founder of Papers with Code, and that brought him to Meta. And then at Meta, he was a lead on Galactica, which was a kind of language model ahead of its time relative to ChatGPT. So if people don\'t know about Galactica, there\'s a great paper worth reading. And then he was doing a bunch of stuff on reasoning with Llama related to a lot of the techniques that we\'ll talk about in this episode.

And now he\'s doing a startup. I don\'t know if he wants to talk about this, but generally, we talk a lot about various things. This got started through o1 and trying to figure out scaling RL. We started talking a lot but then we also just resonate on a lot of topics on training language models and other fun stuff - and also trying to be one of the few people not in these big labs that tries to talk about this and think about what the heck\'s going on. So we\'re gonna kind of roll through a long list of a lot of things that Ross sent me that he wanted to talk about, but this will be a compilation of the things that we\'ve talked about and fleshing them out outside of the Signal chat.

So, Ross, if you want to introduce yourself more, you can, or we\'ll just start talking about news because I think a lot of people already know you.

Ross Taylor: Yeah, let\'s get into the news. There's lots of fun things to talk about.

Nathan Lambert: So, the last two weeks of Chinese models. I think we had Z.ai\'s GLM 4.5 today. Kimi-K2 last week. I think Qwen is on a roll. I thought summer was supposed to be chill but this is crazy.

I haven\'t even used all of these. The pace is just incredible. And all the open models have actually good licenses now. But is this going to hurt anyone in the US? Where do you see this going in six months?

Ross Taylor: Yeah, so yesterday was the one day I actually tried to turn off Twitter. And so when you told me in the morning about the new GLM model, I had to read up on that. So that shows if you take your eye off Twitter for one second, then you're behind on open source\...

But yes, I think the general theme is that it's been absolutely relentless. So thinking about the last time I spoke to you on the podcast a year ago, Llama 3 was a fairly established standard.

There were still things happening in the background, if you paid attention to things, but now it\'s absolutely relentless. In the case of China, I think their business culture is that - as soon as they find something is successful - they're very good at concentrating resources and going after it. So it's created a very competitive space.

I think the context is very interesting in several different dimensions. There\'s the geopolitical dimension, which you\'ve hinted at in some of your blogs. For example, what does it mean if the open source standard is Chinese? What does that mean if we think about these models not just as things which power products, but as (critical) infrastructure? Then it seems like China has a great advantage if they want to be the standard for the whole Global South.

Nathan Lambert: Yeah. There are a few things that we\'re going to come back to in this conversation that are so interesting. We\'re gonna roll into what it takes to train these models. And we\'re going to talk about how crazy, political and hard it is in the US. But we have all these orgs popping up in China - so is this partially just a US problem?

But then we also have OpenAI that\'s supposedly going to release a model. There are multiple things. But my question is: why is China doing so well? Are they well suited to training these language models?

Ross Taylor: I'll caveat what I'm about to say by saying that I want to be careful about making generalisations. Because, for example, we've seen some of these new Chinese organisations be good at innovation - for example, this week we had GSPO which was nice. But for Chinese orgs, my general sense is that, once something has already been validated, the specification for what to build has been set, and the task can be reduced to an engineering problem, then Chinese culture is very well set up to succeed in those situations.

The other dimension which has become relevant - especially after DeepSeek - is that the Chinese Government has traditionally been very good at recognising what's successful, pouring resources in, and facilitating public-private collaborations. I think that surprises people still in the West. For example, people are surprised that a group can come out of Tsinghua can and fairly quickly have their own state-of-the-art LLM. Why isn't there a similar story for groups coming out of MIT?

Nathan Lambert: I'm not sure about this.

Ross Taylor: I think the US will eventually wake up to this, but...

Nathan Lambert: My understanding is that [Z.ai](http://z.ai) is a startup that spun out of Tsinghua, so I don't know if it's the best comparison. Also Alibaba is the clear winner here because they have Qwen, but they've also invested in Moonshot, which is Kimi, and then I think also [Z.ai](http://z.ai).

So I'm more interested in the question as to why they are all open. That seems more important relative to talent because there are lots of universities that might have model orgs spinning out of them - even in the US - and it's not solely a Chinese thing.

I think it could happen with a group out of MIT. That being said, I agree that the US should have more compute deployed for academics and a lot of universities are just spinning them up now. It just takes a long time.

So I think there's a lot of things that Twitter is mixing up here. There\'s a good tweet in it, but I don\'t think it\'ll be 100% true, which makes for a very viral tweet when it feels true.

Ross Taylor: Yeah, I think there is definitely naivety about how things are actually working (in China). And there's asymmetric information, in that you don't truly know what's going on in the inside of these organisations.

The other thing worth mentioning - which is maybe a separate topic - is that there's a tendency to see open models as a homogenous category. But there are very different use cases. So if I want to do a new reasoning paper, I'm going to use a Qwen model. But then if I'm doing distillation, I'm going to use DeepSeek or Kimi.

This discussion also relates to OpenAI's rumored open model: because in my mind I still don't quite see how it will fit into the ecosystem. Because is it going to be something that people build research on? If it's a post-trained model, then probably not, right?

Nathan Lambert: Yeah. But their tweet was about safety, so I doubt it is a base model if they're delaying it for safety. I do think they actually delayed it for this reason. It's very much in OpenAI's culture. But I don't think it's going to change the ecosystem. It will be an interesting one off.

I also don\'t expect them to release a model that\'s based on their GPT architecture. My bet is they take an off-the-shelf architecture like Qwen or Llama. A lot of the recent OLMo models are very Qwen-y. And they will also be deciding sizes based on what fits on what cluster - e.g. Qwen is very deep rather than wide, and OLMo 2 is very similar to that. So I think the OpenAI model is going to fit that mold.

Ross Taylor: I think so. I guess one way to think about it is they\'re just trying to "distill" their RL infrastructure into weight space, right? As opposed to publicising their (internal) architectural choices.

But back to the discussion, and maybe this is a question for you Nathan, but do you think their model is going to be more comparable in use case to a Kimi or DeepSeek? Or is it more similar to Qwen? Or is it actually something completely different, like an on-device model? A smaller model?

Nathan Lambert: I expect it to be smaller. They joked about on-device, which I don\'t know is the right framing.

Ross Taylor: Yeah.

Nathan Lambert: I\'m also just now realizing how - if RL is their great strength - then part of the challenge of shipping an RL model in open source is that you need your training infrastructure to match the inference infrastructure. So unless they train this on an exact VLM that people have access to - and some open source environments - then they can't just dump the model and expect people to be able to do search and code execution in the open model stack.

I don\'t know exactly how Qwen and DeepSeek have gone about this. My impression is that they\'re actually not as useful in terms of tool use because it\'s so hard. I think that tool use is naturally a closed model reinforcing thing because it benefits to have these tools match up.

Ross Taylor: So the Qwen models are pretty good at things like function calling. Kimi - at least in the benchmarks - was also pretty good at agentic tool use benchmarks. And then - this is a separate discussion - but they had this nice training innovation where they use lots of MCP servers in a synthetic data strategy. But then again, you're mostly seeing indications of capability in headline evals, which you shouldn't really trust anyway.

Nathan Lambert: I think of Claude 4 as the release that ended eval chasing. On paper the release was so lame, but it delivered for everybody - which is very bold because there is a lot of money on the line. They are constantly fundraising and if one fundraiser gets spooked because the release numbers are bad, then that's a lot of CEO calls that they have got to make.

Ross Taylor: On evals, I was thinking about this a few months ago. It might have changed now given the pace of AI development, but I was thinking about how you might split up the impact timeline for a release.

So day one is headline benchmark numbers - which are mostly bullshit. Like I've got this amount for my model on MMLU Pro. But then the next tier of impact is the day after the release where people have all these weird bespoke evals on Twitter.

Nathan Lambert: The pelicans and the rotating hexagons and balls...

Ross Taylor: Yes, and by this stage you're getting more confident. Because unless the model developers are very smart (which some of them are), then they probably haven't optimised for day two benchmarks. So at that stage you're beginning to believe that the model actually generalises beyond the headline numbers.

And then finally you have a week or two weeks after the release where you can say that you've tried the model quite a lot now, and you then have real confidence that the model is good.

Nathan Lambert: Yeah. Refute my claim: Chinese providers are still optimizing for benchmarks more than OpenAI, Google, and

Ross Taylor: Yep, I mean it's probably true.

Nathan Lambert: It feels so obvious to me. I think that China has closed the gap to a remarkable degree, but I don\'t think they\'ve caught up fully. I think that\'s hard. It's very hard to get all the data and pipelines in place. A lot of it is actually user data, knowing your user, and hill climbing that. So for example, all these APIs not working is a huge issue for them.

Ross Taylor: Yeah. I think (Chinese models) have also been helped by the fact that a lot of the academic work that builds on them has been doing reasoning work in publicly available data domains like math and code.

The models have been heavily optimised for these domains anyway, so the model developers are not quite as exposed - since people aren't really testing the true generalisation capabilities of the model. We already know that the Qwen models are heavily mid-trained on math and code, so they will hold up performance-wise there.

Nathan Lambert: Yeah. Okay, this is a good preview for the episode. I think that the main things are going to be how to build good organisations, and then academic reasoning research and how to bridge the gap. I think we can talk starting about org charts.

So how do you make a good org? Or maybe there are two things. One: how do you make a good org chart for training language models? And two, how do you make an effective culture?

I think this is quickly becoming one of my favorite little niche interests because there\'s just so much intrigue in it. There\'s just so much money on the line to break everything. So you sent me some hot takes if you want to read them, but the floor is yours for what doesn\'t work.

Ross Taylor: Sure. So if anyone's been on social media recently, the general trend nowadays is to check your phone and see these NFL draft style tweets about researchers moving between orgs.

First of all, researchers have always moved between orgs. This is not a new thing. And a lot of the org moves that were talked about - at least outside of Meta - were just regular moves.

But I think the bigger mistake on Twitter is just the tendency to see the bottleneck in LLM projects as skill issues. And at least from my n=1 experience, that has never been the main bottleneck for success.

There are a number of ways to make this case, but I think I\'d start by saying that machine learning is a heavily empirical science. So what does genius mean in that context? What does talent actually mean?

There are certainly some skills which are useful - like how do you form the right minimal viable experiment? And how do you iterate fast to explore a research direction where you're going to hit a lot of dead ends. But a lot of it comes down hard work, good infrastructure, and ultimately resources.

So in that context, most of these orgs - even before public failings - had very good people. And I don't think the difference in talent between orgs is that large. Smart people will eventually figure things out. So therefore, more often than not, the difference between a good versus a bad model is reflecting an inefficiency in the ability to channel resources to your talent. And that is the fundamental point.

Now you could say, on the flip side, okay, Ross, well, if that\'s true, why is Zuck paying people these massive amounts of money? And I think that\'s a separate question. But yeah, more often...

Nathan Lambert: Well what do you think?

Ross Taylor: I am torn on this because, on the one hand, I think the new group will probably make very good models. They're very smart people. And I think having a new org as well is the right way to do it.

I think in leadership\'s mind, it\'s a case of "Look, we tried this multiple times, we're very serious about this, we have resources, so let's do the maximum conviction play". And I think that\'s broadly what you should do because it's a big expense, but it's not massive, massive spend (for these large companies).

But on the other hand, I feel sorry for - this isn't a Meta point by the way, but a general point - but I feel it's a shame these organisations don't have good mechanisms to identify the talent they already have in their orgs and have to recruit externally.

The talent that has already done the hard work, that is. It's a shame they have to hire externally and start afresh. That's the tragedy.

So that's the conflict in my mind. I think they'll make great models. I think it's the right approach to do things afresh. But at the same time, it's a shame that all the people that came before them, and made the previous generation of models, are treated like an asset. In the sense that you've used these people - grinded them really hard - and now you've moved on to a new group of people.

Nathan Lambert: You put this in your provocations. You said LLM labs are like investment banks where people are slotted in to burn out and burn through. I know that a lot of the work that needs to be done is somewhat mundane data work and it can be parallelised - e.g. if your users are asking this type of question, let's create new prompts and manage human works and create synthetic data pipelines. And that works a lot of the time.

But then, I remember the Dwarkesh podcast with Sholto and Trenton - and it's the one where they've both moved jobs (which reinforces your point), but they were saying you just need to convince someone at a frontier lab that a particular problem is important. I.e. people talk about things, but they just have to do it.

So is it the case that people are just dispatched to solve specific problems, or do individuals have free rein, and it's fun on the ground because you choose the things you want to add to your beautiful final model?

So you can present a positive and a negative. It might vary across labs, but I guess your provocation is that there\'s a bunch of places where it is a meat grinder and you just put people in and chew through them.

Ross Taylor: I think so. Unfortunately the model for a lot of successful tech companies is to get very young, motivated, people - with a base level of intelligence - and make them work very long hours on a project with a big mission. This was the classic Elon way to run a company.

But this is also the model for a lot of frontier labs. You have your soldiers who - on the surface - look similar to quants at hedge funds from like 10 years ago in terms of their working hours. And in the culture too, you have friendly competition between people who all want to be the best.

Nathan Lambert: I will say: I know a bunch of people at OpenAI, and they do work crazy hours. I also work a lot, but I do a lot of things that aren\'t grinding data to go into the model.

Ross Taylor: Yeah, so on the question of decision-making, I think major decisions are generally made by people who are a little more experienced and already have some successes to their name. But you do need to have soldiers in this kind of environment. The space is just highly competitive (and requires people to work long hours).

And I think that\'s a shame. Even for myself right now, where I'm trying to build a startup, I'm thinking that - yes, we all need to work hard - but is there an alternative model where you invest in your employees instead of using them? - i.e. burning them out and then moving on to a new group. That's what I'm trying to work out for my new company.

Nathan Lambert: I feel like a lot of people are just more cynical now in tech, myself included. I got a great cold e-mail from someone fresh out of undergrad, and I was pretty sure in two to three years this person would be legit. And I was talking to a coworker on how we could potentially capture this and invest in them. And they were just saying we might get them, but then they'd just go to OpenAI in 2 years. So we don't get any of the upside.

I think some of that is just cynicism. Investing in people is still the right thing to do because you'll end up keeping the ones that are a bit more grounded even if it is really hard. For example, I\'ve lost people that are extremely talented that I wouldn\'t want to keep. So I don\'t know how to balance that cynicism versus reality of building teams in the long term.

I guess smaller teams might be a bit easier to maintain, whereas if you're at a tech company, the churn is hard to avoid because there's so many levels in moving up.

I think some of the rumors around Meta and Llama 4 - at least from the Dylan Patel SemiAnalysis article - were about them doing these cowboy crazy model training runs, including changing pre-training mixes half way through, and that maybe points to dynamics with middle management wanting their data to be used so they can get promotions. But most labs I don\'t think are doing that type of shit for their leading models. And I don\'t think Meta is normally doing that. I think that was a pressure cooker side effect.

Ross Taylor: I would push back on that a bit by stating that all of these labs are deeply chaotic places (not just particular orgs). They change direction every week, right? That's just the nature of the field we're in.

But then, it is definitely true that certain labs are good at projecting, at least externally, that they have their shit together. They have AGI internally, all this kind of bullshit.

The truth is that it is a shitshow everywhere. It\'s just that if you\'re going to be a shit show, you at least want to be a functional shit show, and you want to make good models. Right?

As I mentioned before, I think there are new plays to be made around taking the view that you want to invest in your talent as opposed to just grinding them out. But I would also say that, in lab culture, people tend to overvalue raw talent again - especially in empirical science. If you take the view that an empirical science is mostly about experimental velocity, then you don't just value infrastructure in that world, but you also want to hire folks who are very collaborative and who want to help each other.

It sounds like a bullshit point in a field that lionises individual intelligence, but I just feel that if you\'re making a marginal hiring choice, then you have to think about how someone adds to an existing group? So I think there are new plays to be made on talent.

But there is nuance. Because there are certainly people who are especially productive. I've seen that in person. So it's not like everyone is equal - that is definitely not the case - but I just feel that individual talent is overemphasised when problems in these orgs are mostly structural.

Nathan Lambert: The differentiation right now is people who are willing to put more highly focused hours turning the crank. Every organisation has the baseline time costs of needing to do meetings, commute time to work, commitments etc. But in terms of AI, where people are doing more and more, this really favors young people who don't have a lot of responsibilities.

Ross Taylor: This is maybe a transition onto another topic, but I'd make a more controversial point which is that - even the things in ML which seem more like novel research are more the result of persistence rather than inspiration.

For example, this time last year we were both speculating about what o1/Strawberry was. And speculation makes you think it was some amazing new thing. But actually it was basically what we were both doing two years ago right? Essentially RL from verifiable reward, but with very good base models, because they were in a good position to exploit that, and then enough ablations to find a recipe that worked.

So this is oversimplifying things a little, but we should take the view that they just had to do the work to make the recipe good. And that comes down to experimental velocity, and also having the right infrastructure and a good enough base model. So in that world, what is talent?

Is talent the person who says "we should make the models think more", or is talent the person who is actually on the ground doing the ablations to find out which recipe works? Right? Because I can also make models think more by best-of-N, but, then there may be better ways to do it?

Nathan Lambert: I mean, I think I analogize a lot myself with my athletics career - like rowing in college. I think so much of it is the same. I wasn\'t the most gifted athlete, but if you put in the hours and you understand where you\'re spending your effort, it works out for people.

The question I wanted to ask you on this topic is, given that that these orgs are so chaotic, then what does this mean for the ceiling on progress? One of the most coveted questions is about the trend line. There are obviously going to be new paradigms - inference time scaling was an obvious one if you thought from first principles about what compute and intelligence is - but even if we don't have a new paradigm, then what is the ceiling?

Ross Taylor: I would say that, even in climates where most organisations are chaotic, you're still going to have macro factors that lift all boats. So a good example recently was these gold medal results on IMO. Three or so different labs all had different approaches and all found they crossed the threshold for a gold medal.

If you were to zoom out - and one way to do this is to imagine you\'re looking twenty years into the future back at this time - then would you look at the individual methods that researchers used, or would you just say compute reached a critical threshold where things began to work?

So compute is the big exponential that\'s underlying all of this. And then if you zoom into a shorter time horizon, then you\'re seeing more of the local challenges, like what's the particular bottleneck at a point in time? So maybe the bottleneck to agentic models is scaling RL environments. Or maybe the bottleneck to better reasoning is longer context windows.

But look: fundamentally as long as compute keeps coming online, I think the trends look good and all of the organisational chaos is short-term noise. It slows down progress a bit but is not meaningful in the long-term. But, unfortunately, it\'s still meaningful for people in their careers because one to two years of organizational chaos could matter personally. But on longer timelines, it doesn\'t really matter.

Nathan Lambert: Yeah, I agree. It seems like the question is what happens when the fundraising starts to slow down. We\'re on a trend line of compute rollout. But if Sam Altman can\'t raise again, that is a very big sign. That\'s like the end of the "bubble". OpenAI is not going to go away because of that, but if they can't get the next cluster... then that would be a bad sign.

Ross Taylor: I\'m quite optimistic because I think you only have a bust if AI ceases to be increasingly useful or doesn\'t live up to certain promises. But even if there\'s no algorithmic progress, I still think AI will continue to continue to be increasingly useful. I don\'t think there are fundamental barriers. It\'s just a question of how quickly you get things right.

I think the argument would have been slightly different two years ago. If the reasoning paradigm didn\'t come through, then I think it would have been trickier to justify the expense because then you\'d be looking at reasoning benchmarks and thinking: shit, to push this forward I need this amount of data annotation or need to generate this amount of data.

Nathan Lambert: You look at GPT 4.5 as the example.

Ross Taylor: Yeah, exactly. That\'s a really good example. So you can treat that model like a counterfactual universe where reasoning didn\'t happen. There we would all be looking at the model thinking "it\'s good at creative writing, but maybe not so good at some more things we really care about (like reasoning)".

By the way, I\'m sure it's a really good model. I didn't play with it enough to form a good judgement.

Nathan Lambert: I\'ve been using it a lot. I used it for a long time - especially until Claude 4 - as it's just nicer, especially when GPT 4.1 was so sycophantic. But GPT 4.5 was nice.

Ross Taylor: So I\'m gonna flip things around and ask you a question Nathan. Let\'s say we are here in a year\'s time. What does the key benchmark look like for LLMs that everyone is focused on?

Nathan Lambert: Oh, it\'s fully gonna be some agentic thing. I don\'t know if it\'ll be as stupid as making money on the stock market... I wrote a post on what I thought was coming next. One of the most poignant things I was looking at is the fact that scaling models is no longer the direction anymore. All the marketing is shifting to agents. And I think some of that is because it\'s not easy to scale parameters anymore.

Every RL curve is this log plot, and it becomes hard. But agents are already beginning to work well. For example, this year Claude Code showed up. There\'s gonna be versions of that in all sorts of domains and more people working to evaluate them. That will create an interesting marketing problem where labs need to figure out how to communicate that their model is good.

But the future looks like it's all on the agentic side, and will lead to a big shift in what the language modelling companies need to think about. The prioritization of the company is also different, whereas modelling was always central before. I'm still modelling-pilled and think that is the central thing for the company...

But it's true that now that teams building products are going to hold more weight than they used to. And there will be interesting changes in how these companies manage this transition, and how communications change.

So, I think Claude Code is great. But I think that it\'s hard to integrate in some things. For example, how do I get that running on my cluster at AI2 where we have all of our data and models, launch evals from our file system on the GPU machines. I don't think that quite works yet, but maybe I'm doing something wrong.

Ross Taylor: Yeah, I agree with your answer. So I spent several years working on Papers with Code, where we were trying to focus heavily on evals before they were a big thing - trying to index all these various leaderboards. And I think now is an interesting situation because I feel like if you make good evals now, you possibly have more leverage than you\'ve ever had in the field of ML..

This is a weird thing because traditionally evals were quite an unsexy thing to do. It was a thing that researchers didn\'t want to do because they\'d rather be training models. But now the ability to define a metric for a capability that you\'d like to see - e.g. trading stocks, or doing scientific research - is just incredible leverage that you can wield. A small group of people in places like universities can say "this is the new north star that we should achieve for agents" and shape how AI progress evolves.

Nathan Lambert: It can happen. We recently released IFBench, a benchmark for following instructions which is just more constraints and a different prompt sourcing. And I was saying to folks that we need to have the goal of making at least two frontier labs adopt it. And I messaged various people, including someone at OpenAI, and they said they already integrated it last week.

So yes, someone doing research (on evals) has a shot at getting into the OpenAI internal evaluation platform.

Ross Taylor: Exactly, so it\'s incredible leverage. And then the other interesting thing is that the friction for making and using good evals is going to increase quite a lot.

For example, in some of the recent benchmarks, you need the RL agent to have access to a GPU and then you need to spin up lots of these servers to do rollouts. This is expensive. Long gone are the old days where you had two CSVs with a train and a test split.

And then on the eval creator side, there's a big difference between good and bad evals as models become more capable.

A bad eval just means that you\'re going to get incredibly egregious reward hacking, and you\'re not going to learn anything useful, whereas a good eval is a pathway towards a brand new capability.

Nathan Lambert: I have a related question on this. So I see three eras in evals based on what people are doing with models.

For pre-training, the best evals are testing knowledge and these very broad things and are hard to game. It\'s just kind of like FLOPs.

At post training, a lot of evals are formatting and extraction. I think formatting became even clearer to people when these RL environments became the hot new thing. And I actually think that post training might be like the ugly duckling in the middle, where then if you go into agents, all the agentic tasks are gonna be evals of actually doing things and you can\'t like format-lie your way through that. So it might be that post training evals are the hardest one to get right.

Ross Taylor: Yeah, and I think you\'re going to see more cases of people claiming good results, but when you look beneath the surface, you'll see insane reward hacking. So the meme right is KernelBench evals. Have you seen these?

Nathan Lambert: Oh.

Ross Taylor: You see all these amazing speed ups which aren't even possible based on the hardware. And this is not a problem with KernelBench, I would say it's more a problem with people publishing papers for agentic evals and not looking at their results carefully.

So this shows that to get an eval in the right place takes a lot of work. And even with progress in models, I don't think you're going to be able to fully automate the construction of a good eval in the next year at least. I might be wrong. Models will certainly help us in creating evals. So I think that, for now, it's a place where a researcher can have a lot of leverage.

I think if you were to ask what is the central eval is right now, it\'d probably be something like SWE-Bench (verified). But even that is now quite saturated. So there\'s a big blue sky now where someone can define what the next big task is for ML. And you don't need a big cluster in order to be the one who defines it; so I think that's quite exciting.

Nathan Lambert: Yeah. And when you think about the amount of money that\'ll be steered by these things, it\'s so crazy to have the uncertainty there and like who will come up with that as well. I think that it\'s part of what makes it fun, I think.

We should talk about reasoning things.

Ross Taylor: Reasoning. Yeah.

Nathan Lambert: Where do we start? I don\'t think I\'ve ever done that much of a rant about the academic community chasing these things. I understand why academics are claiming to do new algorithms that get remarkable scores, but a lot of these papers are just extracting things that are hard to document from a model or something else or formatting

I was on one of these papers, which was hilarious. We figured out that if you train Qwen on random rewards, the evaluation scores go up. And we had to go through the logic on why this can happen.

Because if there\'s no reward, the advantage is zero and the gradients are all literally zero. And then it turns out that the algorithm manipulates the most common sequences. It\'s actually something that if you read a lot of the reasoning literature, people talk about how we want to make sure our algorithm doesn\'t squash uncommon sequences. And then the real hammer is that, if you do random rewards, then you see that the model has modal collapse onto the things that it was trained on. And that can make scores go up.

So if you have a model that two thirds of the time has a certain behavior in its reasoning and that behavior is good on the benchmark, then just by fiddling the weights a bit then it does that behaviour more. This points to a structural failure.

I would also say it is a good example for why people should be using truly open models for research purposes and why they\'re so good for innovation. For example, if we knew what goes in Qwen data and if someone just filtered it and it was like, oh, look, I found the found the GPQA prompts in it...then we know data contamination has happened.

The Qwen case is borderline - I don\'t know how exactly to characterize it because the Qwen models are fantastic - but there\'s so much research that is showing that they are very likely to be doing some dubious things in terms of benchmarks. It\'s hard for people that aren\'t super in the weeds to hold both of these possibilities in their brains.

So I don\'t know. What do you think of the last six months? Have we actually made any progress? Has the academic community made any progress?

Ross Taylor: I think there\'s been little progress. I mean that in the literal sense: there's been some progress, but it has been little. I think I can answer this question in several ways.

So after DeepSeek-R1 came out, there were two approaches in open source more generally, which was either you go down the distillation route or the RL route to make interesting small models.

The initial thing that was undervalued - at least from an engineering perspective - was that for smaller model sizes, it is far more efficient to do distillation than RL.

Nathan Lambert: And not just in compute but also in performance? It\'s hard to do RL on the small models.

Ross Taylor: I think this point has been made twice now. So there was the original DeepSeek-R1 paper, and then more recently, there was a new Qwen paper as well. The Qwen paper showed that RL needed 17x times more compute than distillation.

So one way to think about this is that RL is a brute force lever to do data generation. But assuming that RL is still good, and you still want to do research on it in academia, then you run into a classic problem. And that problem is: if you don't have enough compute, then you don\'t know if the structure you are imposing is gonna generalize (to high compute settings).

And my worry is that a lot of the results are on relatively low compute budgets, both in terms of the underlying base model, which determines how well the RL approach learns, but also the total number of RL steps. So it\'s just quite hard to see - unless there's a massive gain - what's truly important.

So the most useful things are - in my opinion - quite boring things. Like, there was the DAPO paper which showed that you should have filtering for overly long sequences, and you shouldn't overly penalise them if your context window gets cutoff.

There has also been interesting work showing that even simpler approaches (than GRPO) might work, where you remove clipping. So Reka was doing lots of good work using REINFORCE leave-one-out (RLOO). But even there, it's difficult because you don't know if simpler algorithms are going to work with long agentic traces.

So it's not clear. I think the recent work this week was actually quite good. The GSPO work was good, and if you saw their graphs...

Nathan Lambert: Explain it to people. I think a lot of people have heard of the other ones by now. But GSPO is group sequence policy optimization with Qwen Coder. Why are you positive about it relative to the other ideas? I think GSPO is well motivated but why is it getting hyped more?

Ross Taylor: So I hope I don\'t botch this because it\'s the morning. But, essentially, with GRPO, you assign a reward to the whole sequence (via the advantage). But you also have an importance weight, which is your policy likelihood relative to your old one. Because when you do RL, you typically sample lots of rollouts but do several mini batches for your gradient update. So that means you go a little bit off policy.

So to fix that you have an importance weight term. But in GRPO, while the advantage is uniform across all tokens, the importance weight is particular for each individual token. And the importance weight is calculated for a single sequence. So one way of looking at this is that, if you had more sequences to calculate the importance weight, it would be a lot less variance - but by calculating it on a single sequence, you introduce a lot of variance through that term.

So the short answer of what GSPO does is that, instead of looking at a token likelihood, they look at the likelihood of the whole sequence. So now the clipping is not on an individual token basis, but, it looks at one of the sequences in your group and says okay, this one is less likely, so we'll clip out that sequence. And the TLDR is, at least from the results they show, it seems to be a lot more sample efficient.

I mean, it\'s not just 0.5 percentage points or something like that. But I think the reason I trust it more is that it's very simple. And it's quite directionally well motivated from just a basic understanding of importance sampling. If it were more complex, I\'d be a lot more skeptical, but it\'s fairly simple and it seems to work well.

Nathan Lambert: Yeah, I\'m still fairly skeptical.

I think academic research is relatively wide in what people are trying out but labs are relatively narrow. And once you're further along in your modelling journey, you're dealing with different parts of state space and then all these algorithmic tweaks just like help your model on whatever blocker it was or your implementation.

I thought for GSPO the sequence thing was funny because when you read the GRPO paper, you were like oh, the reward is just per sequence. But all the tokens in the sequence get the same loss function. But the standard implementation is to break it down per token. And then GSPO is essentially to take that standard implementation and you change the weight on every token back to this. And I was doubting whether this was really going to be a major thing.

I think for junior researchers, one of the good things about this era is that you can really learn the math by studying all these algorithms and thinking about how they are implemented. I hadn't done that for a few years until writing this RLHF book on policy gradients and I was getting into the weeds like per-token loss, length bias for GRPO, and so on. For students to be able to do this in their brain, it is really good for thinking about the interface between algorithms and systems.

Ross Taylor: It's interesting, because as AI became more hyped after ChatGPT, you have more people reading papers. This is a great thing, but also you have lots of new people reading papers in the wrong way.

For me the basic logic (for reading papers) is as follows: what's the reported gain of the paper and how much complexity does it introduce?

So if you get a gain but the paper introduces shitloads of complexity, it\'s probably not going to stand the test of time. Whereas if it\'s something relatively simple, but it seems to get a good gain, then that's the thing that is going to last.

Nathan Lambert: The o1 lesson. The simple thing. In RL research, I\'ve heard it described as: if you see something that only beats the baseline by a few percent, it\'s not gonna work. But if it's 2x then that's a real innovation, because whether they finetune their baselines or not, they're still going to be crushing it.

Ross Taylor: Exactly.

Nathan Lambert: So I think that\'s a good heuristic for people right now.

Ross Taylor: And I think researchers are their worst enemy because they want to see their own methods work. But the weird thing in ML is that neural networks "want to learn". So if you push something enough, it will work. It\'s just a question of whether that is a good use of your time?

So the question is: what\'s the right thing to scale and push on? So that's why - when you read papers - at least what I say to young researchers is that you should always judge how much complexity the paper introduces, and whether you trust the gain.

And then based on those three factors, you can judge whether it's worth caring about the paper. But I can see why - if you're new to reading papers - why you might be attracted to complicated, new techniques in papers that seem methodologically interesting.

Nathan Lambert: And researchers often manipulate the results of their peer methods in the way to tell a convincing story. And I think these algorithms are a perfect example of trying to tell a story.

Ross Taylor: Yeah.

Nathan Lambert: So when you think of cognitive behavior of paper authors, you have to take that into account too.

Ross Taylor: The other point I'd make is that - in the reasoning trace - I understand that everyone has to focus on math and code, because that's where the data availability is. However, if a paper comes out and it's just flexing on AIME and GPQA then that is just very uninteresting to me - and much more so than it would have been in February.

Nathan Lambert: I think code can be much better but it\'s hard to benchmark it. Describing what a good coding model is would take me an extremely long document.

That\'s not what the academic papers are doing. It would be great to have more benchmarks on that.

Ross Taylor: Yeah, and even the established ones have issues. For example SWE Bench has a very large proportion of issues from Django (so it's not exactly representative of all software engineering). That's not a burn towards SWE Bench - which is a great benchmark - but...

Nathan Lambert: They already won. They can take it - they won!

Ross Taylor: But, yes, it shows that there is a lot of detail to get right in making a good coding benchmark.

Anyway, it's difficult because I am in this position where I can say - on the one hand - papers are just hill-climbing particular math and code benchmarks, and that is fundamentally uninteresting to me. But at the same time, I sympathise. Because there are not a lot of good open reasoning datasets in the open. And those that are open, I don't think that they're even going to be good for testing RL necessarily. They might test something more knowledge based, like medicine or something like that, which is less inference-time scaling bound.

Nathan Lambert: This could be a good time to transition. What is the status of RL scaling and generalizing? What is the status of RL outside of math and code? I think my prompt is: what do you think about o3-like models with this crazy search behavior and multi hop execution?

Ross Taylor: Yes. So first of all, I think it was greatly overstated that these models don't generalize beyond math and code. I think what happened in practice is that, at least from what I know, OpenAI originally was very focused on math, logic and puzzles. And then eventually they had to broaden out because it was kind of too nerdy and biased towards these kinds of tasks.

But I don\'t think there was ever a question about their generalisation to other benchmarks. You could see that very early on. The way I think about this is: we started with math and code because it was easy to verify. And then through applying RL to those domains, models learnt certain strategies like "I shouldn't answer early", "I should check my work", or "I should consider alternatives". And at a very high level, if you just have a model that thinks for longer and checks its work more and considers more things, then that\'s gonna be useful for things beyond math. And that\'s reflected in the benchmarks.

That being said, if you want to get superintelligence outside of math and code, then yes, you probably need more specific benchmarks and datasets for that. So there the question is less about whether it generalises beyond math and code, but how far can performance go? And that's when you get into interesting questions about, e.g, if you don't have a numerical answer or whatever, then how do you verify things.

So rubrics are all the rage right now, but then there\'s also other directions like...

Nathan Lambert: Rubrics are so funny. It's funny how they needed to be reinvented. Rubric is a funny name because it just seems like question-specific LLM as a judge. It\'s the most basic unit of evaluation or feedback.

Ross Taylor: So I think this was something that wasn\'t very covered in the open. So the reason why it became popular was that DeepResearch was the trigger. The rumor at least was - at least for OpenAI - they didn't need many examples to do well in these kinds of research task.

It wasn't tens of thousands of rubrics - it was probably in the 1,000-2,000 range of well-crafted rubrics for questions. But it clearly worked very well to teach a model how to browse the internet and synthesize knowledge. There\'s obviously infrastructural detail as well.

Nathan Lambert: What would a rubric look like for deep research in this case? For an essay it might be that the rubric says that an answer should be free of typos, have a clear argument and a good conclusion. It would have different checklists. But the DeepResearch example is more complicated and you might need to draw an example.

Ross Taylor: Yeah, so there are different themes you could have. It could be the general style of the answer. It could be - let's say we want a review of the latest and greatest RL algorithms for reasoning - then there you might have a high level rubric saying that the answer should compare different methods, cover underlying algorithms, mention policy gradient, PPO vs REINFORCE and so on.

But then you might have, like, more detailed things where you just have a strong conviction on what a good answer looks like. For example, a review of RL for LLMs right now might include GSPO as of this week.

So rubric-based grading comes down to a list of checks, but the goal of that form of evaluation is that you're trying to get a nice, continuous rewrad for the model to learn from - as opposed to something more binary and sharp. Because while 0/1 rewards might work okay for mathematics or unit tests, it would work less well for a task like making a good literature review on RL. The reward structure isn't binary there.

Nathan Lambert: So how do you think of grader functions? I've thought about this for code, like the percentage of unit tests that pass. But then the model might just get the easy unit tests. So will reward shaping be here to stay or will it be washed away in the ever growing sea of compute?

Ross Taylor: I think it\'ll be washed away, but I think in the meantime, there\'s a lot of value in making very good handcrafted evals. And I hate the word taste, but there is still taste to begin with.

And I think a lot of these things are quite codependent, because to make a good rubric for a deep research task, then you need something that needs the ability to do deep research. If we were to say what makes a good literature review on RL right now, then that knowledge wouldn't be in the weights of a language model - the model would have to go out and search for things.

Nathan Lambert: You can tell it that you need to use search in this question.

Ross Taylor: Yeah, if you haven't done a search, then you\'re probably doing it wrong. So yeah, in the long term, it gets washed out because there\'s nothing a neural network can\'t do compared to a human. But in the short term, there\'s still a lot of nooks and crannies that a model wouldn\'t quite cover / struggle on.

Nathan Lambert: Can you create a generative reward model by training off a bunch of rubric data? Probably?

Ross Taylor: Yeah, so verification benefits from thinking time. And I think most people are aware of this now, but it\'s more of a question of how you actually execute that. So a generative reward model for something like math and code - where it\'s like a 0 or 1 reward that you're trying to figure out by thinking - is less interesting to me then questions where you really need to think from first principles on how to assign reward.

In general, the simplest way I think about it is: if you\'re moving to a world where you have long agentic traces, then your "reward model" just needs to answer a simple question, which is: "is the agent making progress towards its goal?" Right? But that\'s a very deep question.

So if it\'s a Pokemon eval, then maybe a model needs to use its knowledge of Pokemon to figure out if the agent in a trajectory has been caught in a loop, and whether it should be going towards Lavender town instead of this other way.

So these sorts of verification tasks benefit from thinking time, but the devil is in the detail. Because if you're not careful, you're just going to spend an inordinate amount of compute trying to get a reward.

Nathan Lambert: It feels like there will be a lot more we will learn there. It feels obviously salient. I'd describe it as verification changing the slope of inference time scaling. And that\'s really, really valuable if you\'re spending a lot on inference, but we don\'t really know how to do this. Like parallel compute is another factor that changes the shape of that curve.

I guess it\'s really all a slope of a scaling law or like an offset or something, but it\'s hard to say which things are true in terms of what we\'re hearing. That\'s probably what they\'re doing other than this rubric stuff. It\'s just a way to get RL pointed at more problems, which is not surprising.

Ross Taylor: Yeah, I think RubricMania is in full force right now. I mean, I think the longer term question, which has been posed in several places, is what happens when verification becomes fundamentally harder?

So I\'m quite interested in the scientific discovery question. But in a field like biology, you need to do a physical experiment in order to verify. So it's not just a question of running things on a cluster. And if you want to simulate the underlying thing, well then you're bottlenecked by the quality of the simulation - and it turns out to be quite hard to simulate some physical processes!

Actually - in most of the sciences - I think this is the other point I'd make" which is that in ML, people overvalue the value of individual "thinking" in something like science. They think of Einstein and they think a lot less about the data generating mechanism, and what\'s the instrument.

There is no Kepler without the telescope. There is no progress in biology without X-ray crystallography. There\'s maybe new theories on dark matter in space without even better, newer telescopes.

I know this sounds like a weird say in the context of RL, but if you're thinking about very hard things to solve in the real world, then you're just going to be bottlenecked by the need to build a better instrument to get data. So it sounds like a digression, but I'm saying that - in the long-term - you're going to hit these bottlenecks for verification. But in the short-term, we can still solve very interesting things like Millenium Prize problems, but that will probably take quite a while too!

Nathan Lambert: Yeah, I don\'t have anything particularly eloquent to say on the scientific discovery point. I guess what will happen is that RL is going to be in training and then you just sort of punt it off to the rest of post-training. So models need to be able to get really weird, but not weird in a way that they are numerically lost.

I\'ve been reading a lot of reasoning traces these days, and the Qwen and DeepSeek reasoning traces really just seem numerically lost for a while, and then they eventually get the answer right. They say "Wait" a lot and then go into half English/half Chinese, and end up getting the answer right.

My point is that I don't think in their current form, that these things are vehicles towards (scientific) discovery. There's some kind of fundamental research needed to make the reasoning process more real.

Ross Taylor: My other bear case against reasoning models is the following argument - and this is mainly a devil's advocate point, because I still fundamentally believe. Since World War 2, there are a lot more scientists in the world. But has progress kept up at the same rate? If anything, I would say that scientific progress has slowed.

Was there more progress in fundamental physics now or in the last century? And I know that is mainly because the low-hanging fruit is gone in many of these fields, but it could also be a bear case for AI because it hints that the bottleneck in science is the amount of intelligence on a problem, but maybe the speed of physical processes, or the ability to build better instruments for measuring, or the ability to get funding from governments to build bigger particle colliders...

I\'m exaggerating the bear case because I think AGI mostly means autoating regular activities - law, finance and these kind of industries - and I think that's a lot easier to do. But I'm attacking this mindset that says - now that we've solved reasoning - the takeoff is going to arrive in the next few years. From what I can see, that is very unrealistic.

Nathan Lambert: I\'m very I\'m bullish on AI being used and bearish on whatever superintelligence takes. I think we're too compute constrained for a takeoff. I think AI is going to be very good for financialization and digitalization and seamlessly globalizing the Internet and making all information transfer and acquisition effectively free.

Ross Taylor: Yeah.

Nathan Lambert: Which is really good. And I think historically, the US is very well-positioned to capture this by making products that run on top of cheap AI models.

Ross Taylor: Yep.

Nathan Lambert: I wanted to ask you what AI you actually use. I don\'t know if I\'ve ever asked you it\'s normally revealing.

Ross Taylor: Okay, so the base models we're doing experiments on are mainly Qwen - Qwen 3, but also Qwen 2 because we know the kind of quirks of that model a bit more. A lot of people do that. Then we also do some distillation jobs, where we're mainly using DeepSeek-R1. We did use Kimi recently, but we didn't see massive benefits for the benchmarks we were looking at.

Then from a personal productivity perspective, Claude Code is very, very good. My main worry with Claude Code is that - I think there\'s a paper on this - but people confuse agents making you more productive versus preventing you from exerting mental effort. So sometimes I\'ll have a day with Claude code where I feel like I use very little mental effort - and it feels amazing - but I\'m pretty sure I\'ve done less work.

That will change because the models get better, but I\'m trying to teach myself to be a bit careful because sometimes I need to stay in control.

Nathan Lambert: It does seem like an equilibrium. I\'m happy with it. I don\'t want to have to grind out some plotting code. I\'m just gonna watch some sports highlights and let it do it for me. That\'s fine...

Ross Taylor: Yeah. But in general, there is a lot of positive feedback from the community on Claude Code. It's a very impressive product for me.

Nathan Lambert: What is the niche of your use case, or is it a bunch of things? Is there something you could endorse? Do you use it in math or code tasks? Do you use it in your startup's codebase?

Ross Taylor: It tends to be better with brand new codebases. But I mostly use it for tasks which are quite horizontally scalable. So I\'ll have some basic specification where I\'ll provide it with some example code of mine, and then say "here\'s what a good implementation looks like", but I need this modification or twist done. Sorry, I\'m being very vague because I don\'t want to talk about specifics, but...

Nathan Lambert: Yeah.

Ross Taylor: It tends to be better for that. And, yeah, where it becomes really bad is when the file size becomes too long. Then the agent tends to struggle and get into these weird line search doom loops. So, yeah, there\'s a bit of work to do where you have to structure the codebase a bit for it to be efficient. But in general, it's quite helpful.

Nathan Lambert: It\'s such a success that pretty much everybody that tries it is doing at least small code projects with it. I think maybe since ChatGPT, there hasn't been this strong of a reaction.

Is this like the GPT 3.5 level? Like, Claude 4 is like GPT 3.5, the original ChatGPT, and then a couple iterations it's gonna be incredible\...

Ross Taylor: Yeah, I guess the people who really appreciate Claude Code are developers. Right? But it doesn\'t have the mass appeal of ChatGPT, which could generate poetry or whatever at the time, which was the killer mainstream use case at the time...it sounds crazy now.

Nathan Lambert: But I guess pay for Claude Code. People won\'t pay for ChatGPT (laughs)\...

Ross Taylor: Exactly. So maybe it\'s a better business model...

But, yeah, I think that\'s a good question. I wouldn\'t say it\'s a ChatGPT moment, but I would say it\'s probably one of the most impactful products since ChatGPT. It's not a ChatGPT moment because it hasn't got mainstream appeal yet. And the question is: what does that agent look like? I\'m still shocked that Apple hasn\'t done anything yet because, for me, that would be the killer thing. We\'ll see if they get that shit together.

But, yeah, I\'d imagine it would be some sort of on-device model. That would be my guess. We'll see

Nathan Lambert: Yeah, that's fun. Did you also wanna mention AlphaEvolve? I\'ve been so burnt by Google\'s hypey projects - like their chip design and stuff.

Is this like the AlphaGo story, where if you have a really high performance simulator, that's well matched to a task and you can scale RL - like many actors in parallel - then you can get high performance? I talked to Eugene Vinitsky recently, one of my friends from Berkeley. And they were at Apple and they did this really parallel RL for self driving simulator, which was really awesome.

Is AlphaEvolve somewhat away from that, but is in the same vein of extracting simulators?

Ross Taylor: I think AlphaEvolve is very cool. In my mind, it\'s very interesting because it feels like we are going full circle. In the 90s, the cool things which didn't quite work were genetic algorithms and neural networks. And it feels we often see a new lease of life for several algorithms once the right context develops and other components get in place

So in the case of AlphaEvolve, you\'re exploiting the strong latent knowledge of a neural network, but then you also have a neurosymbolic element....don't read too much into that, Gary Marcus... where you have a database where you store past programs. And having that prior in the form of past programs is a very good way to exploit the internal creativity of a language model as opposed to creating from scratch each time.

Nathan Lambert: How does AlphaEvolve actually do this? I think a lot of people are not going to know what it is doing. I don\'t think I have a good knowledge of it.

Ross Taylor: Say you have a kernel optimization task. For example, you're making good kernels for common ML architectures. So you start with a reference implementation, and then in essence, it\'s a bit like in- context learning where you're taking that implementation and saying "propose a change", and then you benchmark it and get a score. And then you have a database where you store that program and its score.

And then when you sample a new round, you have an algorithm - it tends to be based on island based algorithms - where you sample in proportion to the score but you also wanna explore a bit. And that\'s your new prior. So you\'re iterating and evolving a program.

Nathan Lambert: And this is just handed off to the language model? What is the language model actually inferencing? Is it inferencing new programs?

Ross Taylor: Yes. So imagine you\'re constructing your prompt. You fetch a past implementation from your database and it goes in. It probably has the score as well saying "this implementation above got this result". Then you ask the model to propose a new change.

I am oversimplifying, but this is the essence of the approach. You propose a new change, you write a program, get the score, store it in a database, and then go again.

So, basically: anything where you can pose a neat optimization task, this algorithm tends to work very well.

This is a broader debate now about how AlphaEvolve compares to RL approaches. First of all, I think they can be complementary, but...

Nathan Lambert: Maybe the language model is trained with RL, I bet?

Ross Taylor: Yes, that too. The interesting thing by the way is that the bulk of the AlphaEvolve approach was not using the strongest Gemini model - they used a weaker model with faster inference. So that's an interesting tidbit which is sort of anti model-scaling pilled. There is a nice balance to be found there...

But yes: back to RL vs AlphaEvolve. I think this is part of a broader trend on how you use compute and whether the approach is parallel or sequential. The AlphaEvolve approach benefits from parallelisation, but they're not going into deep long reasoning traces (sequential) just yet. But you could use both approaches.

Similarly, with RL you usually solve problems from scratch. But you could also think of ways you might want to exploit good priors in the context window. Benchmarks like KernelBench sort of do that anyway, but they don't evolve the reference implementation like AlphaEvolve does.

So I think it\'s definitely something to watch. I think AlphaEvolve is underhyped, but we'll see many more papers on this direction soon.

Nathan Lambert: It seems like a sign of things to come - figuring out parallel compute in the right way. It might be that the biggest model doesn't necessarily benefit the most from a parallel compute setting.

Ross Taylor: Yeah.

Nathan Lambert: I mean, there\'s a lot of ways you could think about this. Like, the guess is a 100 times cheaper and half as good...

Ross Taylor: Yeah. So maybe this is a bullshitty philosophical point, but think about it this way. In the past 5,000 years, humans have made a lot of progress, but their brains fundamentally haven't changed. What makes us smarter is that we've followed an invention curriculum, where the next invention builds on previous inventions.

So in the RL context, that raises the question: would you rather start from scratch each time, or would you use the best thing you have and successfully iterate that by standing on someone else's shoulders?

So this is definitely something to watch in RL space. Instead of AlphaZero-ing things from scratch, how do we maintain existing implementations and iterate upon those?

This is also related to how we develop language models, and the discussion we had about Claude Code. You can imagine having an agentic model that is very good for starting from scratch, but you could also have a model that\'s very good at dealing with an existing code base. And the question is which is more valuable? And the answer is both. But then depending on how you actually use those models, you might end up preferring a different model.

So I am trying to put AlphaEvolve into a much bigger context here: and see it as a bigger trend about how we use compute, but also how a model might learn to improve on a problem.

Nathan Lambert: Yeah, that\'s fun. There\'s going to be a lot more things like AlphaEvolve - where people with particular domain expertise do the muddling and figure things out and more things will fall out. It is very remarkable that a zero order optimizer like a genetic algorithm, just using prompts for language models, can get anything useful out. That is a major win for language models being a fundamental unit of compute.

Ross Taylor: Yeah, absolutely. And a major win for LLMs and creativity, right? Because the meme is like "Oh, LLMs can\'t be creative", and I'm always thinking, at a fundamental level, the softmax is quite an expressive operation...You'll get creativity eventually. It\'s just a question of how quickly you can pick it out from what you sample.

So, I think AlphaEvolve is also proof of creativity. You found many new state-of-the-art implementations in AlphaEvolve - and will see more to come in upcoming papers.

Nathan Lambert: I would also guess there\'s people doing stuff like that that don\'t publish it. Or they\'ve taken different models and hill climbed in their domain by setting up these weird loops.

I think this is a good place to end things. I'm kind of fading. Thanks for coming back. I'm doing a trip to London at some point. I don't think we've ever met in person, but that'll happen at some point!

I think we\'re I mean, I\'m kind of fading, so I think it\'s good. Thanks for coming back. I\'m doing trip to London at some point. I don\'t think we\'ve never met in person, but that\'ll happen at some point.

Good to see you.

Ross Taylor: Yeah, good to see you Nathan. I\'ll see you in a bit!
