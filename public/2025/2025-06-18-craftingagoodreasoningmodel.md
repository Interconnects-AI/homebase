---
title: "Crafting a good (reasoning) model"
subtitle: "A recent talk I gave on model training, reasoning, and the next frontier."
date: 2025-06-18
type: podcast
audience: everyone
visibility: public
post_id: 166151726.crafting-a-good-reasoning-model
email_sent_at: 2025-06-18T13:05:51.946Z
---
Why are some models that are totally exceptional on every benchmark a total flop in normal use? This is a question I was hinting at in my [post](https://www.interconnects.ai/p/sycophancy-and-the-art-of-the-model) on GPT-4o's sycophancy, where I described it as "The Art of The Model":

> RLHF is where the art of the model is crafted and requires a qualitative eye, deep intuition, and bold stances to achieve the best outcomes.

In many ways, it takes restraint to land a great model. It takes saying no to researchers who want to include their complex methods that may degrade the overall experience (even if the evaluation scores are better). It takes saying yes to someone advocating for something that is harder to measure.

In many ways, it seems that frontier labs ride a fine line between rapid progress and usability. Quoting the same article:

> While pushing so hard to reach the frontier of models, it appears that the best models are also the ones that are closest to going too far.

Once labs are in sight of a true breakthrough model, new types of failure modes and oddities come into play. This phase won't last forever, but seeing into it is a great opportunity to understanding how the sausage is made and what trade-offs labs are making explicitly or implicitly when they release a model ([or in their org chart](https://www.interconnects.ai/p/how-to-manage-ai-training-organizations?utm_source=publication-search)).

This talk expands on the idea and goes into some of the central grey areas and difficulties in getting a good model out the door. Overall, this serves as a great recap to a lot of my writing on Interconnects in 2025, so I wanted to share it along with a reading list for where people can find more.

The talk took place at an [AI Agents Summit](https://lu.ma/p827xb6n) local to me in Seattle. It was hosted by the folks at [OpenPipe](https://openpipe.ai/) who I've been crossing paths with many times in recent months --- they're trying to take similar RL tools I'm using for research and make them into agents and products (surely, they're also one of many companies).

Slides for the talk are available [here](https://docs.google.com/presentation/d/1_ByHKLt49h3Vuk9bkprD6iaBDOY40ASfSwXGD7aheEc/edit?usp=sharing) and you can watch on [YouTube](https://youtu.be/VAzL8RHot1c) (or [listen wherever you get your podcasts](https://www.interconnects.ai/podcast)).

:::::::: {#youtube2-VAzL8RHot1c .youtube-wrap attrs="{\"videoId\":\"VAzL8RHot1c\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=VAzL8RHot1c){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

## Reading list

In order (2025 unless otherwise noted):

1.  Setting the stage (June 12): [The rise of reasoning machines](https://www.interconnects.ai/p/the-rise-of-reasoning-machines)

2.  Reward over-optimization

    1.  (Feb. 24) [Claude 3.7 Thonks and What's Next for Inference-time Scaling](https://www.interconnects.ai/p/claude-3-7-thonks?utm_source=publication-search)

    2.  (Apr. 19) [OpenAI\'s o3: Over-optimization is back and weirder than ever](https://www.interconnects.ai/p/openais-o3-over-optimization-is-back)

    3.  RLHF Book on over optimization

3.  Technical bottlenecks

    1.  (Feb. 28) [GPT-4.5: \"Not a frontier model\"?](https://www.interconnects.ai/p/gpt-45-not-a-frontier-model?utm_source=publication-search)

4.  Sycophancy and giving users what they want

    1.  (May 4) [Sycophancy and the art of the model](https://www.interconnects.ai/p/sycophancy-and-the-art-of-the-model?utm_source=publication-search)

    2.  (Apr. 7) [Llama 4: Did Meta just push the panic button?](https://www.interconnects.ai/p/llama-4?utm_source=publication-search)

    3.  [RLHF Book on preference data](https://rlhfbook.com/c/06-preference-data.html)

5.  Crafting models, past and future

    1.  (July 3 2024) [Switched to Claude 3.5](https://www.interconnects.ai/p/switched-to-claude-from-chatgpt?utm_source=publication-search)

    2.  (June 4) [A taxonomy for next-generation reasoning models](https://www.interconnects.ai/p/next-gen-reasoners)

    3.  (June 9) [What comes next with reinforcement learning](https://www.interconnects.ai/p/what-comes-next-with-reinforcement)

    4.  (Mar. 19) [Managing frontier model training organizations (or teams)](https://www.interconnects.ai/p/how-to-manage-ai-training-organizations?utm_source=publication-search)

## Timestamps

00:00 Introduction & the state of reasoning\
05:50 Hillclimbing imperfect evals\
09:18 Technical bottlenecks\
13:02 Sycophancy\
18:08 The Goldilocks Zone\
19:28 What comes next? (hint, planning)\
26:40 Q&A

## Transcript

*Transcript produced with DeepGram Nova v3 with some edits by AI.*

Hopefully, this is interesting. I could sense from some of the talks, it\'ll be a bit of a change of pace than some of the talks that have come before. I think I was prompted to talk about kind of a half theme of one of the blog posts I wrote about sycophancy and try to expand on it. There\'s definitely some overlap with things I\'m trying to reason through that I spoke about at AI Engineer World Fair, but largely a different through line. But mostly, it\'s just about modeling and what\'s happening today at that low level of the AI space.

So for the state of affairs, everybody knows that pretty much everyone has released a reasoning model now. These things like inference time scaling. And most of the interesting questions at my level and probably when you\'re trying to figure out where these are gonna go is things like what are we getting out of them besides high benchmarks? Where are people gonna take training for them? Now that reasoning and inference time scaling is a thing, like how do we think about different types of training data we need for these multi model systems and agents that people are talking about today?

And it\'s just a extremely different approach and roadmap than what was on the agenda if a AI modeling team were gonna talk about a year ago today, like, what do we wanna add to our model in the next year? Most of the things that we\'re talking about now were not on the road map of any of these organizations, and that\'s why all these rumors about Q Star and and all this stuff attracted so much attention. So to start with anecdotes, I I really see reasoning as unlocking new ways that I interact with language models on a regular basis. I\'ve been using this example for a few talks, which is me asking O3, I can read it, is like, can you find me the GIF of a motorboat over optimizing a game that was used by RL researchers for a long time? I\'ve used this GIF in a lot of talks, but I always forget the the name, and this is the famous GIF here.

And coast runners is the game the game name, which I tend to forget. O3 just gives you a link to download the GIF direct directly, which is just taking where this is going to go, it\'s going to be like, I ask an academic question and then it finds the paragraph in the paper that I was looking for. And that mode of interaction is so unbelievably valuable. I was sitting in the back trying to find what paper came up with the definition of tool use. I think there\'s a couple twenty twenty two references.

If you\'re interested after, you can can find me because I don\'t remember them off the top of my head. But these are things that AI is letting me do, and it\'s it\'s much more fun and engaging than sifting through Google. And the forms of the models so this previous one was just O3 natively, whatever system prompt ChatGPT has, but the form of these interactions are also changing substantially with deep research that we\'ve heard alluded to and and referenced. And then Claude Code, which is one of the more compelling and nerdy and very interesting ones. I I used it to help build some of the back end for this RLHF book that I\'ve been writing in a website.

And these things like just spinning up side projects, are so easy right now. And then also Codex, which these types of autonomous coding agents where there\'s not the interactivity of Claude code is obviously the frontier that is going. But if you try to use something like this, it\'s like, okay. It works for certain verticals and certain engineers. However, the stuff I do is like, okay.

This is not there yet. It doesn\'t have the Internet access is a little weird as to build these complex images, installing PyTorch. It\'s like, okay. We don\'t we don\'t want that yet for me, but it\'s coming really soon. And at the bottom of this is like this foundation where the reasoning models have just unlocked these incredible benchmark scores, and I break these down in a framework I\'ll come back to later as what I call a skill.

And it\'s just fundamentally reasoning models can do different things with tokens that let them accomplish much harder tasks. So if you look at GPT-4o, which was OpenAI\'s model going into this, there was a variety of what we\'re seeing as kind of frontier AI evaluations where it\'s on the spectrum of the models get effectively zero, which is truly at the frontier to somewhere to 50 to 60 is labs have figured out how to hill climb on this, but they\'re not all the way there yet. And when they transition from GPT-4o to O1, which if you believe Dylan Patel of semi analysis, is the same base model with different post training, you get a jump like this. And then when OpenAI scales reinforcement learning still on this base model, they get a jump like this. And the rumors are that they\'re now gonna use a different base model and kind of accumulate these gains in another rapid fashion.

And these benchmark scores are are not free. It\'s a lot of hard work that gets there, but it\'s just a totally different landscape where things like AIM and GPQA, which is this kind of science technology reasoning questions, are effectively solved. And this is like the use cases I was describing where it\'s like, O3 can kind of just do this. And a lot of harder things we\'ll see keep coming, might unlock some of these kind of use factors I\'m mentioning as interesting but not there yet. And we\'ll see this kind of list grow over time, but it\'s really not like the only thing that we\'re experiencing on the ground because skills are only one part of this, and there\'s a lot of this arts and crafts of how do you actually have a good model that people like to use.

And a lot of this talk is gonna be talking ways that that can go right and wrong. And generally, just my reflections as someone who trains these models on why we get exposed to this. So there\'s a lot of online discourse about models that go too far on training on benchmarks. This is an old tweet from Phi from Microsoft. I don\'t wanna throw them under their bus because they\'ve also Phi-4 is a really good model by now.

So a lot of these people get this reputation for things that are maybe like a one off model incident, which emerges from a complexity of org structure weirdness and individual incentives. And I think like Meta\'s really in this right now, that doesn\'t mean their future models will be subject to this. But it is definitely a phenomenon that could happen where it\'s like a lot of low level decisions result in the final product that is just not what you wanted even though it seems like along the way you\'re doing everything right. And just kind of climbing these benchmark scores, is linked to this thing that I was saying with skills, is not the only way forward. And especially with reasoning models, there\'s kind of another way we\'ve seen this, which is Claude 3.5, where people love to gripe about this supposed upgrade to Claude, would love to just like fake its way through unit tests.

And if you\'re looking at reasoning training, a lot of the technical implementation for code is you have the model generate code and you check if you pass unit tests. And what people are seeing is that Claude essentially does everything and then modifies the code so that the test passes. And this is like a side effect of at the training time, our reward function is just too simple. It\'s like we\'re rewarding the model for getting unit tests right, which might be disconnected from the overall theme. And like, there\'s just so many ways that they can actually come up, and it\'s like this RLVR thing, reinforced learning with verifiable rewards, let us climb these skill charts crazily both on public and private benchmarks.

So I think a lot of the labs have benchmarks internally that are much more specific to things, and even those you could kind of fake yourself on. And, like, I try there\'s examples of OpenAI and Gemini doing the same thing, and a lot of recent model releases have this sort of like, oh, the coding is a little off energy. But I I think a lot of it comes to this, which is just bypassing a unit test. And another really interesting one that doesn\'t quite have the same interference with the utility of it is like this Transluce blog post and other communications when O3 was announced where O3 will do this thing where you ask it a question and it\'ll say its reasoning for why it\'s true is some action in the world that it can\'t actually take due to its sandboxing. So this is the O3 saying that it measured it on its MacBook Pro that it has even though it\'s just running in in the data center without access to it.

I think this is a good example because things will come up like this that have actual physical meaning, but even if we could see it in such innocuous ways, it\'s just that this, like, we\'re we\'re pushing so hard on these skills and the measurable things that a lot of the unmeasurable becomes a second priority goal. And this is the sort of thing where it\'s a team a teammate at a company will be like, we\'re so much better at coding, search, math, everything. And it\'s like, oh, the the leadership needs to get the model out for competitive reasons. And then some of the things, it\'s like, okay, we do this messy process of making the model much more robust and getting rid of these oddities in the training data and stuff like this, and and you kind of do this later on. So it\'s kind of this back and forth when the pace of progress is so high that you you have to make hard decisions on what you prioritize.

And a lot of times, these weird model releases are actually just technical bottlenecks. I think this is one of my most entertaining model releases of the year is when OpenAI released GPT 4.5, and they released this system card. And originally, it had the sentence in it that GPT 4.5 is not a frontier model. If you try to find this now, they\'ve since edited the system card, so it doesn\'t say this anymore. But it\'s just such a funny thing for an AI lab to say because at the same time, the model is really liked by people.

And I think that one of the things that people caught on with this was doing green text, and they thought this model was very good at it. And since GPT 4.5, I think people kind of think that all the big models are kind of good at green text. So Claude 4 Opus and Claude 2. Gemini 2.5 Pro, people also do this now. And this is a sign that humor is really getting better at the models. And there\'s these this is like a total viral moment where people like interacting with GPT 4.5.

But if you look at the system card, it\'s like Sam Altman says we spent 10 times the compute as GPT four on it, and the evaluations are like a minor tick up. And when you look at reasoning models, all the reasoning models have like 20 gains all the time. So it\'s this really odd release where I think this is a model that I still use very regularly in my day to day basis, but it just can\'t land for some weird complex reason of balancing this kind of vibes, eval scores, which are really important for marketing to both users and kind of business customers because you get that first impression feeling and then also price. And there\'s also these weird things where there\'s more people trying to get involved in these leading models, and the bar for releasing them is actually getting much higher. So these are two papers that are some of the, what I call, leading open reports on how to do reasoning model training.

Open thoughts three is on kind of data methods for instruction or supervised fine tuning, just kind of generating a large dataset for performance on math and code. And Magistral is Mistral\'s first reasoning model. And these, the methods they describe are very strong and it\'s very good for these companies to be open and Bespoke Labs from Open Thoughts release the data as well. But it\'s like even these companies get really bad can get really bad press when the models just fail to do really simple things. So for example, the OpenThinker model was the sort of model that\'ll think for minutes when you say hi to it, and the Mistral model is one of the models that every time you ask it a question, will format it as if it\'s giving a math answer.

And these are obviously cherry picked things from a known vocal critic because it is entertaining, but it\'s just like this is the space that AI operates in, which is like if you don\'t get the little things right, people are still gonna complain and and give you bad press because the models that do things extremely well are just one click away. I think things like Claude 4 Opus is easy to use in there and Gemini\'s coming and there\'s more open models. And it\'s just hard to get a model out that has this kind of care to it because it takes a lot of time and resources to kind of wait to release the model when you do all these kind of last bits of fine tuning. The most important one that\'s been in the news is kind of the sycophancy idea. This is not a real example from the model that they released for two weeks for ChatGPT.

This whole little saga, I just imitated it by system prompting it. But it reads just like them, which is ChatGPT was unbelievably sycophantic for a few days. I\'m not gonna comment on all the kind of social second order effects because they\'re obvious and that\'s a large motivation of why I do the work that I do, which is just like we want to be able to have understanding and oversight onto things like that, but it reveals deep organizational pressures that these companies are going through to kind of get things out the door fast that people really want. If you are to so so here\'s some more examples. These are the GPT-4o version and one of these viral examples on what it was actually saying.

And on the left is the Llama 4 secret chatbot arena version, which is the one they use to get the number one score on Chatbot Arena, but never actually released. And talking to that was very odd because on the release day, you\'re like, this can\'t be the model that they\'re saying is the best thing ever. It\'s just really strange. It\'s like Llama example, it\'s like I asked it what\'s its name and it said a very direct and very good question. It\'s like I don\'t think most people in this room want that answer and that says a lot about evaluation and other things.

But it\'s like this is a deep grained problem with reinforced learning from human feedback and collecting preferences, which is that if you\'re collecting preference data, you will give a multi page document ranking your priorities on how you rate the or compare the answers. And at the end, there\'s certain things like Sick of Fancy that people actually just like to get out of models, so they become tie breaks if they\'re particularly distinctive between the answers. And in the OpenAI post mortem on sake of NC, they had an extremely good breakdown on this. So I recommend that you read this, but I\'ll take a second and read out loud the core example. So they said, for example, the update introduced an additional reward signal based on user feedback, thumbs up and thumbs down data from ChatGPT.

Throughout the post, they talk about how they trained a reward model to predict this. And with what we\'ve seen from things like Chatbot Arena, it seems very likely that the strongest signal in that reward model was that it is just sycophancy of links to these thumbs up data and then that was expressed. Generally this is a form of over optimization. The last line on this slide is something that comes from a lot of history in the reinforcement learning literature is that for example in syncopancy and that reward model, when they were training these models in post training with many stages, so they go through some instruction tuning and they do RL, and they do RL, and they do RL, RL. As you\'re really pushing the models to their limits, the strong optimizers that we use will extract performance where it\'s easiest in your training signals.

And the easiest training signal is probably, is just like you you add some emojis, you tell them they\'re good at it, and the models can pick up on that very easily. And then the decision making problem that can explain most of these issues that we\'ve talked about so far in the talk is that you have many evals, and these are things you\'re trying to hill climb on, but you can never have all of them. So you\'re kind of doing a multi objective problem, you\'re pushing all of those up, and it\'s often taking from something that you\'re not accounting for, and it\'s getting pulled way in the other direction. And this is where the things like art are important, and I\'ll kind of highlight a model that I think did this really well in a few slides. But I think as we see this competition for models, we\'ll both see more weird releases like this where there\'s kind of rough edges.

And there\'s also this much bigger opportunity in the AI space to release things that are really robust and bring a lot of joy and don\'t have these rough edges. So I think this kind of drive to be patient is going to be hard and hopefully rewarded when there\'s a lot of weird things out there. And for the non researcher majority of this audience, the figure on the right is from what is like the original over optimization paper in reward models. It\'s called scaling laws for language model or reward model optimization. And this is just showing the x axis is a technical measure that\'s KL distance, which is a distance that\'s used to reference the numerical change from a starting model to a final model when you\'re doing some RL fine tuning.

And this is showing that the y axis, your reward model score, it goes up and then it goes down. So the the hard part is when you don\'t have something you\'re competent in is you don\'t know when it starts going down in your over optimization. So this is kind of a classic paper you\'ll see if you start digging into this direction more. And what I kind of wanna highlight is that there\'s a Goldilocks zone between evals, vibes, and price. And I think particularly most models now are getting evals and price, and this middle one is hard.

When I think about it, Claude 3.5 Sonnet was released over a year before Claude 4 Sonnet. And this model definitely had all of them. It was the one that got people in the Bay Area here to switch from ChatGPT to Claude. And that it feels so ahead of its time because clod force on it really doesn\'t feel that different than 3.5. And it\'s definitely better, but these jumps are rare.

And these models, it\'s like we\'re on this really fast slope. So if you get a really lucky model, you\'re just gonna have such a really, really great output. And we\'ll kind of see where they come. I wouldn\'t know if I necessarily count O3 in this. O3 is a proof of concept that you can do something, but it still has a lot of rough edges for people.

For example, coding ability isn\'t quite good enough. But there will definitely be more of them and it\'ll be interesting to see what falls into that niche. And then, kind of the transition into the art of modeling and back to some of the stuff that I was presenting at the AI engineered world fair and I\'m thinking about for my day job is like, what comes next after we have this reasoning ability? And I\'ve come up with a few different things that people are gonna be trading into these models that make some of these applications that I started with possible. Autonomy is a very discussed trend in AI right now.

This is a plot from METR, which is a nonprofit evaluation or monitoring startup, I think, in Berkeley. And the plot here is the y axis is the length of time that it would take for a human to do a task that an AI is now doing. And what we\'re seeing is that AI models over time are able to solve longer and longer tasks. It\'s important that I I focus on this fact that it\'s a time of human task because I\'ve messed up saying it in the past. And the TLDR is that climbing this is not free, and it takes a lot of hard work in improving the models and knowing where to push the models next to kind of unlock these.

And it\'s it\'s like the reasoning paradigm is a good example because we couldn\'t keep hill climbing on what we were doing to to kind of unlock this middle phase. So it takes a lot of effort and kind of transitioning the focus from reasoning to things that are focused on planning in this kind of task abstraction is gonna be the thing that unlock these next models or even systems. I think you might see like a DeepResearch bullet point on here rather than like O4 being on here. And then the question is like, how do we actually do this in a model and how do we train autonomous models? So when I think about traits of these kind of independent agent models, I think about starting with skills, which is what I talked about with reasoning, and then kind of expanding into other traits that are gonna be needed.

So I kind of think of calibration, is models that know what they don\'t know. And I think that labs haven\'t been using this because it\'s been easier to unlock performance by just building skills than having the models being kind of introspective. They just haven\'t needed it because they\'re not doing a lot of tasks on their own, and the humans could give the feedback. And then to kind of go with this, there\'s a few what I described these last two as two different subsections of planning. I was trying not to overburden the term because strategy is kind of creating a plan in itself and knowing where to go.

So if you ask DeepSeq R1 a very hard math question, it won\'t first plan. It\'ll just dive in and start to try to solve it. And having the model spend the time to refine its direction before solving it would be very important. And then when we\'re doing things like deep research or hard coding problems, we need a model that if it\'s presented with a plan, knows how to do itself in certain inference passes to solve subsets of it or to dispatch that to other agents that can take these steps on the problem and actually solve them. These are things that their models aren\'t trained to do at all right now, where it\'s like skills we have, inference time scaling, the basic RL stuff has unlocked this.

I don\'t think we need that much the models are solving the most impossible math questions for mathematicians. We don\'t need to push it that much further. Calibration, there\'s a lot of research on that. And then these last two is what I think is the next Q Star like thing where there\'s gonna be a lot of human data, and then we\'re gonna have a few good examples that we can then use to iterate with more complex training. And so if we revisit this example to ground my taxonomy, I call this very skillful but lacking planning.

Search is a skill that O3 has largely mastered. It can find really niche information, but if we\'re gonna pair this to DeepResearch, it doesn\'t quite know how to compare and contrast and know how much information it needs to gather before making its conclusion. So planning and synthesis is something that we have to encourage the models to do more of before we kind of just well, to unlock the next phase of progress. And to end, this is a somewhat technical provocation, but is something that I hear definitely happening directionally on the ground of other labs is like this RL and post training is becoming the focal point of language model development. It doesn\'t mean like, pre training is definitely not dead now, but mathematically, in terms of compute, these techniques for reasoning and planning are really becoming the bedrock of what people spend their money on.

Is a plan that people ask me what am I doing at AI2 to try to make a better reasoning model. At the end of the day, the technical things are not that complicated, which is you get a big data set, you filter the data set, you train the model for a while, and then after you have your models, you do a bunch of the things that are in all the research papers. They have a few ideas and you try them at the end and they might give you 1%. This is mostly suited for a technical audience but fun to include. And then back to this from post training to training idea, it\'s like how do we integrate this compute where post training is similar in GPU hours and then there\'s the idea of continual learning and if we don\'t ever have to really pre train a model at all, and we can kind of just keep using these real world interactions to provide signal to the model.

If we ground it into some real numbers, DeepSeek V3 was the famous paper that kick started a lot of discussions on how much does it cost to train a frontier model, and they listed these prices at \$5,000,000 Within that table, they said that post training used like well less than 1% of the compute. A fun example is that a researcher on their RL team tweeted that DeepSeek R1 trained for a quote few weeks in the RL stage. This is obviously not something that you want to base any sort of, like, investment or strategy decision in. But if you extrapolate from the tweet, it\'s like DeepSeek R1 one could be, 10 to 20% in GPU hours. If you talk to somebody at OpenAI, they\'ll also say similar things, which is like O1 uses very low percentage, but O3 was 10 x the RL compute, and O4 should be the same, which is that this post training phase is already becoming 10 to 20% of the compute used for these larger models, and that\'s where people are looking to push limits with these things like planning and so on.

So it should be fun. This means that we\'ll get model releases more frequently because you can kind of see where the performance is going during these RL runs. Where pre training, you have to wait all the way to the end for technical reasons to see how the model is So for people building models, I think these next eighteen months are gonna continue to feel like what it has in the first six months of the year where it\'s every few weeks we\'re getting something that is potentially noticeably better. So that\'s where I\'ve ended. I\'m probably a little under on time but potentially catching up for for break time.

So thank you all for listening.
