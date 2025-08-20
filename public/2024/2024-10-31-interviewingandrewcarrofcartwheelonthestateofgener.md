---
title: "Interviewing Andrew Carr of Cartwheel on the State of Generative AI"
subtitle: "Interconnects interview #9. Creativity of and with AI, AI for motion, robotic models, Claude computer use, and all the relevant topics."
date: 2024-10-31
type: podcast
audience: everyone
visibility: public
post_id: 150648459.interviewing-andrew-carr
email_sent_at: 2024-10-31T12:30:58.254Z
---
*Sorry about the double email yesterday! Just messed up a setting on my end.*

[Andrew Carr](https://x.com/andrew_n_carr) is co-founder and chief scientist at [Cartwheel](https://getcartwheel.com/), where he is building text-to-motion AI models and products for gaming, film, and other creative endeavors. We discuss how to keep generative AI fun and expansive --- niche powerful use-cases, AI poetry, AI devices like Meta RayBans, generalization to new domains like robotics, and building successful AI research cultures.

Andrew is one of my well read friends on the directions AI is going, so it is great to bring him in for an official conversation. He spent time at OpenAI working on Codex, Gretel AI, and is an editor for the TLDR AI Newsletter.

You can see an example of how Cartwheel works here (from [Twitter](https://x.com/getcartwheel/status/1824486722631241826)):

::: {.native-video-embed attrs="{\"mediaUploadId\":\"fb9c57c7-4ce7-47da-8bb4-6d34df224b68\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

Listen on [Apple Podcasts](https://podcasts.apple.com/us/podcast/interconnects-audio/id1719552353), [Spotify](https://open.spotify.com/show/2UE6s7wZC4kiXYOnWRuxGv), [YouTube](https://www.youtube.com/@interconnects), and [where ever you get your podcasts](https://www.interconnects.ai/podcast). For other Interconnects interviews, [go here](https://www.interconnects.ai/t/interviews).

:::::::: {#youtube2-BIYik-AaHo8 .youtube-wrap attrs="{\"videoId\":\"BIYik-AaHo8\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=BIYik-AaHo8){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

### **Show Notes**

Named entities and papers mentioned in the podcast transcript:

-   [Codex](https://openai.com/index/openai-codex/) and [GitHub Copilot](https://github.com/features/copilot)

-   [Gretel AI](https://gretel.ai/)

-   [TLDR AI Newsletter](https://tldr.tech/ai)

-   [Claude Computer Use](https://www.interconnects.ai/p/claudes-agency)

-   [Blender](https://www.blender.org/) 3D simulator

-   [Common Sense Machines](https://www.csm.ai/)

-   [HuggingFace Simulate](https://github.com/huggingface/simulate), [Unity](https://unity.com/), [Godot](https://godotengine.org/)

-   [Runway](https://runwayml.com/) ML

-   [Mark Chen](https://twitter.com/markchen90?lang=en), OpenAI Frontiers Team Lead

-   Meta's [Lingua](https://github.com/facebookresearch/lingua), [Spirit LM](https://ai.facebook.com/blog/spirit-meta-ai/), [torchtitan](https://github.com/pytorch/torchtitan) and [torchchat](https://github.com/pytorch/torchchat)

-   [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) paper

-   [Meta Movie Gen paper](https://ai.meta.com/static-resource/movie-gen-research-paper)

### **Timestamps**

-   \[00:00\] Introduction to Andrew and Cartwheel

-   \[07:00\] Differences between Cartwheel and robotic foundation models

-   \[13:33\] Claude computer use

-   \[18:45\] Supervision and creativity in AI-generated content

-   \[23:26\] Adept AI and challenges in building AI agents

-   \[30:56\] Successful AI research culture at OpenAI and elsewhere

-   \[38:00\] Keeping up with AI research

-   \[44:36\] Meta Ray-Ban smart glasses and AI assistants

-   \[51:17\] Meta\'s strategy with Llama and open source AI

### **Transcript**

**Nathan Lambert** \[00:00:00\]: Hello, welcome back to Interconnects. Hey, Andrew, welcome to the show.

**Andrew Carr** \[00:01:10\]: Thanks for having me.

**Nathan Lambert** \[00:01:11\]: Yeah, this will be fun. I think this is kind of an open-minded discussion relative to some of the interviews that I do. I\'m excited to learn about Cartwheel and some of the stuff that you\'re doing. I appreciate that there\'s not that many people that feel like they\'re trying to do something different in generative AI, and I think it marks a good moment to remember what are the interesting creative and new things that people are going to be doing. I think yesterday, as of recording, is when Cloud released their computer use, which we\'ll talk about. We\'ve seen OpenAI\'s O1, which is different but the same, and it\'s like, how far can we push generative AI to be truly different, and how much of it is going to be incremental? I think a good place to start, just to kind of get momentum, is to learn about Cartwheel, the startup they\'re making, and you shared these fun animations of motion. I think we might go into kind of rants on robotics and motion and RL, and if we start going into this, you\'re going to nerd-snipe me on this, so we\'ll get into those too. But it\'s just like, what is Cartwheel, and why is doing things that are different than just big text models important?

**Andrew Carr** \[00:02:21\]: Love that. I\'ll try to not give the marketing pitch. We\'re neck-deep in pitching this thing to people, so I\'ll try to give the actual technical version. So, Cartwheel is a fully vertically integrated, top-to-bottom AI company that we\'re building. What that means is we have our own hardware in my basement, and maybe I\'ll show you during this. We have our own model we\'ve trained, our own data, we have, I mean, I\'ve tweeted about this, but we have 70 data labelers labeling motion for us, and then we have a product on the front end. So what we\'re building is a generative and directable animation tool. So the idea is you want to type something in and get a 3D character performing exactly what you typed in. So, it\'s text to 3D motion, is the mapping problem that we\'re trying to solve. And the goal is, you know, maybe a character animator wants their character to do a dance, and it would take thousands of dollars and two weeks of work to get the character performing that dance. And so we can hopefully make that much faster for the artists, and then they can go on to build larger and better productions and so on.

**Nathan Lambert** \[00:03:43\]: Was this started motivated by kind of these artistic endeavors, or was there something else that made motion the problem of interest?

**Andrew Carr** \[00:03:52\]: Yeah. So I was at OpenAI working on Codex, which was an early program synthesis, you know, powered Copilot for a while. And we were excited about Copilots, you know, Microsoft is still excited about Copilots. And I thought, gosh, where can I put this amazing program synthesis model that we have? You know, we thought it was amazing. It was 27 on human eval, you know, Claude yesterday has 93.7. So it was not amazing relative to what could happen, but I was still excited. There\'s a piece of 3D software called Blender, free open source 3D thing. It actually has a Python interpreter inside of it. And so I thought, oh, that might be cool. I wonder if it can write Blender code. So I hooked it all up. I had a little text box in Blender, it was calling out and so on. And I typed, I said, hey, do this, do that, whatever. I don\'t know how to use Blender really well, but it would write the code, it would interpret it, and then the 3D environment would do stuff, you know, spawn cubes, it would move them and rotate them and so on. And when I got that working, it was sort of this light bulb moment of, wow, maybe I could actually animate stuff. I don\'t know how to animate, but like, wouldn\'t that be cool? We don\'t use Blender. We don\'t use any of that. I mean, it\'s totally different. Yeah. So then why is this the thing that you\'re doing?

**Nathan Lambert** \[00:05:11\]: Like, why did you get rid of, or like, what is the coordinate system of your model? Like, why did you get rid of the intermediate, intermediate renderer? I think there\'s two things that come to mind. Yeah. Common Sense Machines is another startup that is doing like text-to-world generators. And I had talked to them years ago, and it seemed like they were going down like a bit of more of like a meshes route, which seems very linked to simulation. And when I joined Hugging Face, the first project we were working on was Simulate, which it\'s like, it\'s not supported still, and it didn\'t really get off the ground. But it is like the idea of Pythonic APIs for creating environments for agents based on, I think it was Unity and Godot backend. So there\'s definitely a lot more people that are doing 3D scene creation based on programmatic input, which just gets closer to your story, which is like, why are you doing this?

**Andrew Carr** \[00:06:01\]: You know, Runway even did something, they did like a program synthesis of JavaScript for video filters. Like if you wanted to make things black and white, and they were like, they had a team doing that. I don\'t know if that still exists or not, but yeah. So, you know, the first thing is Blender, amazing software, super buggy, crashes all the time, right? So I didn\'t want to be tied to that. And the second thing is, the Python code just isn\'t enough to move a character realistically, like with kinematics and at least plausible looking physics. And so, you know, for those number of reasons and the scalability, you know, I wanted to be able to train a model on a novel data type. And I think there\'s a number of sort of technical reasons that made it hard to do that in Blender. We decided to just go directly to the motion data itself. And the motion data is pretty simple. It\'s position, rotation, velocity over time for a bunch of joints.

**Nathan Lambert** \[00:07:00\]: A bunch of joints. That makes sense. It\'s more like, why is this different than robotic foundation models? So it seems like robotic foundation models are acting in a similar, like, you give it

**Andrew Carr** \[00:07:11\]: a name.

**Nathan Lambert** \[00:07:12\]: There are probably multiple levels of abstraction where I think the visual language model for robots is like telling it where to go in the world. And we\'ll talk about pointing as a behavior later. But like, why is this, like, is this, are one of these markets going to grow and absorb the other? That\'s kind of what I\'m wondering.

**Andrew Carr** \[00:07:32\]: I don\'t think so. I would be shocked if there wasn\'t a huge overlap. You know, there\'s some nitty gritty differences. Like we don\'t output torques. The character doesn\'t have to hold themselves up against gravity. There\'s no physics involved in what we\'re doing. And so in some sense, it\'s easier to do fantastical things. Additionally, like we care about storytelling, right? And so we want the character to be much more emotive, squashing and stretching and unusual proportions and so on. So from that perspective, they\'re like pretty different. The message is deformed and the character is non-volume preserving, like there\'s all these different problems. But yes, there is a world where you could drive a robot with like a reaching or like a goal-oriented torque calculation for kinematics thing based on the synthesized motion from a system like ours. I could see that being very possible.

**Nathan Lambert** \[00:08:25\]: Or like use our SORA or whatever fit in, like how bad is SORA at the things that you\'re trying to do? Or I mean, you probably haven\'t used SORA, but there\'s equivalents, which should be, I\'m sure.

**Andrew Carr** \[00:08:36\]: Yeah. I love the video generation stuff just as an endeavor. I think it\'s very cool. There\'s lots of reasons why it\'s hard. I think the main thing is you can\'t really edit the output of SORA or some equivalent. You just get all these rendered pixels. And good luck if it\'s not what you want. Right. In our case, it\'s object oriented. that you could go and raise the arm a little bit, or you could swap the character for a different one, or you could do whatever you want to actually edit the underlying scene.

**Nathan Lambert** \[00:09:08\]: Are you thinking that you\'re going to expand into different controllable characters?

**Andrew Carr** \[00:09:15\]: That\'s the hope. Like I would love to do cats and dragons and cars and you know, a camera is a character so control the camera. We\'re doing humanoids for now and we can do a whole wide range of humanoids.

**Nathan Lambert** \[00:09:27\]: This is like the story in robotics, which is going from training on one robot to training on multiple robots and you\'re operating in a different abstraction and like your state spaces are the same. So you\'re kind of arguing that the generalization will be similar. I think it\'s a bit more open ended than robotics or maybe less interactive. But like, do you think that you\'re going to hit this? If you\'re trying to generalize this, do you think you\'re going to hit the same barriers that places like Physically Intelligent are when they try to do this? Or it might be like the digital thing that\'s saving you?

**Andrew Carr** \[00:09:59\]: Yeah, because we don\'t have to do any sim to real physical plausibility. You know, just cancelling out the, like getting a neutral dynamical system in this overactuated world where a robot can stand, right? That\'s really hard to do. And our character stands for free, right? And so I think that because it is digital and because it\'s performative, it just has to look good. It doesn\'t have to have plausible torques. I think we have a lot of benefits there.

**Nathan Lambert** \[00:10:30\]: I think that\'s kind of what I would expect. That\'s a good. Are there any other generalizations where you see this trade off in the whole generative AI space? I think it\'s like, how does a computer agent fall in? So like a computer agent is all digital, but it\'s like still interacting with the world that it doesn\'t fully model. Like cloud doesn\'t control the computer, like is it going to be able to recover when finder crashes on my Mac randomly because there\'s too many tabs open? Is there like, I\'m just wondering where this extends to, because I do think that generative AI is at its best in fully digital domains. That\'s why like text works and coding is also like text, but I don\'t know if any of these things, as we go towards self-driving cars, it\'s like, or robotics.

**Andrew Carr** \[00:11:20\]: That\'s a good question, right? I think, so there\'s two axes I think about. One is the editability. You know, can you, like, do you physically or digitally have the ability to recover from errors? Can you edit the underlying thing? And then two is, yeah, this, this sort of grounded versus non-grounded nature of interaction. So I think, you know, Claude can edit the text, it can click on websites, it can do all of those things. So I think that is fine. Then the grounded question is, do I believe that Claude will be able to succeed without a full world model?

**Nathan Lambert** \[00:12:06\]: This is the bet that people are making, like, to what extent can AI operate in the world, like the AIs that we\'re using today operate in worlds that are not constrained. And I think that\'s like the most, I think AGI definitions are pretty silly, but most of the ones that are exciting hint on whether or not the AI can actually do things outside of its training domain. It\'s like, can it, can it interact and can it handle these things? And for now, it\'s like, seems like the right thing to do is to build a business that doesn\'t rely on this because there\'s so much to do.

**Andrew Carr** \[00:12:38\]: Yeah, that\'s what we\'ve done. I think to your point, I think what will likely happen is the training domain will expand to include most useful things you can do on a computer. And then it doesn\'t matter that the machine is still just interpolating its training data. It will be doing whatever we think it needs to be doing, ordering food and whatever thing.

**Nathan Lambert** \[00:13:01\]: Like is, like, yeah, I see most of this being that generative AI just does our simple things in the background, which is just saving us time and is not necessarily like, I guess like coding is a big unblocker, but to do truly new things is hard. I think I still have mental block on the real world, sweet bench like things where people say in the labs that they\'re using these to dramatically increase the pace of AI research. But what does that mean?

**Andrew Carr** \[00:13:33\]: Oh, one from what they say has authored PRs to the OpenAI code base, which is cool. I have no idea what those look like.

**Nathan Lambert** \[00:13:39\]: At the same time, it\'s like most open source commits are typo fixes because people want to be listed on a contributor. Like, yeah, that\'s well and fine and I suspect it can do this, but I don\'t think it\'s probably actually doing the really hard things without hand-holding. You can hand-hold the AI models to do this. That\'s what I\'m trying to figure out is to what extent is small vertical companies the only way forward versus these models actually generating new and useful things.

**Andrew Carr** \[00:14:10\]: Yeah, I\'m extremely biased. I think small vertical companies are going to be really valuable, sort of have an outsized impact in the new world for a whole pile of reasons. We use language models for all kinds of small things internally that would be a whole person\'s job. And then our tool is hopefully going to empower creators to create much more fantastic stories in their day jobs over time. We\'ll see.

**Nathan Lambert** \[00:14:40\]: Are there other domains that you think people are sleeping on? You think about this a lot. I mean, you had this tweet that was like, I spend a large amount of time exploring which models are best for poetry. Why is that? Is that related or is that just like\...

**Andrew Carr** \[00:14:58\]: Totally unrelated. I run a number of anonymous post poetry Instagram channels, which are really fun.

**Nathan Lambert** \[00:15:07\]: Are they anime profile pictures?

**Andrew Carr** \[00:15:09\]: No, I mean, it\'s all on Instagram, right? And that would be fine. I do not have an anonymous Twitter account for those wondering. I\'m not one of\...

**Nathan Lambert** \[00:15:18\]: I have an anonymous account with less than 10 followers because I\'m too lazy to use it.

**Andrew Carr** \[00:15:23\]: It happens. No, I mean, I think poetry is fascinating. It\'s a really good playground for a few things, right? Instruction following, world knowledge, and then some sort of hints of creativity. It\'s hard to actually define a domain where those three coincide and converge. And so it\'s really\... I have a set of 100 or so different poetry tasks that it\'s very clear to me when a model is good.

**Nathan Lambert** \[00:15:54\]: Do you think these models are good in the way that humans are good at poetry? What do you mean by good for AI writing poetry?

**Andrew Carr** \[00:16:04\]: Yeah. I haven\'t played with these full time, but in the hundreds of hours I\'ve spent on poetry models\...

**Nathan Lambert** \[00:16:12\]: I mean, that\'s way more than the vast majority of people.

**Andrew Carr** \[00:16:15\]: I would think so, right? I have generated or had generated three poems that I would consider masterpiece in the states that they were moving to me and they were beautiful and I felt really compelled to share. So three out of however many poems I\'ve generated, thousands and thousands. So from that perspective, no, they\'re not close to people. People write much better poetry. I think people are far more creative and moving and whatever. But it\'s there. It\'s in there.

**Nathan Lambert** \[00:16:43\]: Is there any way to detect that a certain poem is the masterpiece without just having a highly educated human look at them?

**Andrew Carr** \[00:16:51\]: I haven\'t found a great one yet. I\'ve done some LLMs as judges and I\'ve tried to enumerate all the criteria. So I really love the self-rewarding language models paper where they do the additive five point scale. They use that everywhere. And so I have an additive five point scale that tries to get tone and musicality and different poetic devices and then subject relative to the things that are included. But that relies on the model itself having the same world knowledge and all the LLM as judges problems that you run into.

**Nathan Lambert** \[00:17:26\]: This is one of the common threads that I\'m seeing is which domains can we translate into a verifiable reward? So in math, the way they look at math problems these days, it\'s like, can language models generate the answer in the distribution of the problem? And in our poetry analogy is that, yes, it can generate the answer. But why math is nice is because once you can generate the answer, you then have a signal that you can use to train the model. But with poetry, we don\'t have the signals by which we can train the model. So I don\'t expect poetry to dramatically change. It\'ll be easier to generate a masterpiece poem. But the human supervision is still the bottleneck because it would have to get so much better that every single poem is a masterpiece.

**Andrew Carr** \[00:18:06\]: I think that that is not something I would bet on. This is what I was alluding to in my tweet where I said scale doesn\'t help much with poetry is essentially this point of because we don\'t have direct supervision, because we don\'t have good measures of this, just making the model much bigger, won\'t make every poem a masterpiece.

**Nathan Lambert** \[00:18:27\]: So will we be able to make masterpieces in motion? Like in robotics, you have supervision, which is if the task is completed. But in art and like this kind of cinematic motion, the supervision, I think, is human preferences.

**Andrew Carr** \[00:18:45\]: Yeah, we don\'t. So we don\'t break away from human preference. You can still train an aesthetics classifier like you would in images. All these video models now use aesthetics classifiers also. You can do the same thing in motion.

**Nathan Lambert** \[00:18:59\]: I just like the robotics analogies because on the one hand, we said that robotics will be a lot harder because it has to deal with sim to real. But on the other hand, we said that it has a signal that we have shown again and again that is extremely powerful for these models. So it\'s like harder and easier.

**Andrew Carr** \[00:19:14\]: Well, I mean, I love that point. It\'s never been the case that the software was the hard part in the last five years for robotics. Like with these language models, we can plan and reason well enough that robots are fine. It\'s really just hardware reliability, which is why I think people are sleeping on Optimus as like a robotics solution because their hardware, I mean, they\'ve amazing so fast gotten to such a powerful and it\'s tele-operated, whatever, it doesn\'t matter. But like the software is not too bad after that, you know, I could be naive, famous last

**Nathan Lambert** \[00:19:46\]: words, but I kind of want to have Sergey on the show and he\'s very good at selling these things. I think that I\'ve talked with him a good amount about this, like physically intelligence office. And it\'s just like, how do you get these robots into the world? Like I don\'t want, who\'s going to pay 10 grand for a hunk of potatoes that is not doing anything. And it\'s just like, if you can get the flywheel going, I think like we\'ve seen with Waymo, the flywheel is going there. It took them 10 years to get the flywheel going in a real way. It\'s like, if you could do this for home robotics, like sure, you\'ll have the data, but all the data is going to be in warehouses. It\'s like, how do you get, like, I have, it\'s things like how you\'re going to give robots to academics and like let them collect data that you use for free. Like, is that even enough? It just seems like it\'s a grand problem that will work at some point in the next a hundred years, I think. But I feel like most of the predicting is just kind of these weird socio-cultural dynamics and economies of scale and making them really cheap, which I don\'t want to bet my career on, but I understand why people want to do it. That\'s right.

**Andrew Carr** \[00:20:49\]: Yeah. And, you know, it\'s more promising than it\'s ever been given this rise in, you know, control theory is much, much more well understood and we have stronger processing, better batteries, but yeah, it does feel hard. Data is still the bottleneck and there\'s, you know, simulators are getting better. And a lot of people are excited about video models because they can potentially simulate a robot in a home. You know, there\'s been some work by One X, I think, did their video model. I can\'t remember now, but. Yeah.

**Nathan Lambert** \[00:21:21\]: And then we\'ve also seen like Waze had a really state-of-the-art video model before just for car simulating. Yep. So I think these things are related. It\'s like almost like they\'ll use cartwheels, like cartwheel is building a very dedicated, like an engine for some of these domains.

**Andrew Carr** \[00:21:38\]: I think that\'s true. It would not surprise me if people use the cartwheel API to generate great training data for some niche thing. Sure. Like, that\'s great. And then you do sums into real sum goodness, a little bit of physics and you\'re, you\'re in business. Yeah. Okay.

**Nathan Lambert** \[00:21:54\]: Let\'s, let\'s continue on to more focused on the cloud computer thing. I wrote about this because it was easier than I expected to run. documentation where you just run one Docker command and it shows up and I tried things and it was not like, it\'s, it\'s obvious that it\'s the future. It\'s fun that we have so many, I\'m, I\'m also working on a piece that\'s like, it\'s just so fun to have so many of these moments where the future is obviously here in a short period of time. Yeah. It\'s like the Meta Ray Bans are like, Oh, these are like AirPods again, which is awesome. But in a different, exciting way, SpaceX landing, giant rockets, riding Waymo I did for the first time a few years ago, like CLAWD agent, like all of these things are like, immediately inviscerally, like this is something that will be here.

**Andrew Carr** \[00:22:41\]: And notebook LM I would actually put in that bucket as well. Yeah.

**Nathan Lambert** \[00:22:45\]: For a lot of people. And I was like, Oh, I\'m kind of weird, but it is a new form factor. That\'s awesome. And it\'s just like, so good to live in these things. But at the same time, it\'s like the path ahead for CLAWD almost feels harder than other things. Just because like, you have to get Apple, you have to use the Apple accessibility features or Apple\'s gonna launch first party things. There\'s so much money going into agents. And I don\'t know if this is why like GPT-5 isn\'t released. It\'s like, it\'s been hyped up for so long.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

**EDITOR'S NOTE: Here you'll see a rare, but fun [Whisper](https://openai.com/index/whisper/) error. It happens when the model gets stuck on a word it doesn't know how to extract. Luckily, there's a secondary transcript available, I just figured my AI audience may find it funny**

**Andrew Carr** \[00:23:15\]: Yeah.

**Nathan Lambert** \[00:23:16\]: What do you think about this space? Like, why didn\'t Adept get here? This is what I asked you before, and you had two good points on like, why Adept might not have worked.

**Andrew Carr** \[00:23:26\]: Yeah. Adept. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:23:48\]: Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:23:52\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:24:11\]: Yeah. Yeah. Yeah.

**Andrew Carr** \[00:24:14\]: Yeah.

**Nathan Lambert** \[00:24:15\]: Yeah. Yeah.

**Andrew Carr** \[00:24:17\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:24:29\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:24:36\]: Yeah.

**Nathan Lambert** \[00:24:37\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:24:52\]: Yeah.

**Nathan Lambert** \[00:24:53\]: Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:24:57\]: Yeah. Yeah.

**Nathan Lambert** \[00:24:59\]: Yeah.

**Andrew Carr** \[00:25:00\]: Yeah.

**Nathan Lambert** \[00:25:01\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:25:07\]: Yeah.

**Nathan Lambert** \[00:25:08\]: Yeah. Yeah. Yeah.

**Andrew Carr** \[00:25:11\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:25:29\]: Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:25:34\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:26:11\]: Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:26:15\]: Yeah.

**Nathan Lambert** \[00:26:16\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:26:24\]: Yeah.

**Nathan Lambert** \[00:26:25\]: Yeah.

**Andrew Carr** \[00:26:26\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:26:35\]: Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:26:39\]: Yeah.

**Nathan Lambert** \[00:26:40\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:26:49\]: Yeah.

**Nathan Lambert** \[00:26:50\]: Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:26:55\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:27:10\]: Yeah.

**Andrew Carr** \[00:27:11\]: Yeah.

**Nathan Lambert** \[00:27:12\]: Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:27:16\]: Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:27:20\]: Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:27:25\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:27:39\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:27:48\]: Yeah.

**Nathan Lambert** \[00:27:49\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:28:01\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:28:28\]: Yeah. Yeah. Yeah.

**Andrew Carr** \[00:28:31\]: Yeah.

**Nathan Lambert** \[00:28:32\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Andrew Carr** \[00:28:39\]: Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.

**Nathan Lambert** \[00:29:07\]: Yeah. Yeah. Yeah. Yeah. Okay. Yeah. Okay. ha Some of the things. that\'s where most of these things come from.

**/////////////////////////////////////////////////// END BUG //////////////////////////////////////////////////**

**Andrew Carr** \[00:29:17\]: Yeah. And Mark, so Mark Chen was doing work there. He led the codecs work too. Yeah. Yeah.

**Nathan Lambert** \[00:29:21\]: It\'s like codecs, code interpreter. I mean, code interpreter is amazing. There\'s this advanced data analysis thing.

**Andrew Carr** \[00:29:27\]: It\'s the same team for what it\'s worth. Um, yeah.

**Nathan Lambert** \[00:29:32\]: And just like open AI is experimenting, which is why I would expect this sort of thing to come from them rather than anthropic.

**Andrew Carr** \[00:29:40\]: Yeah. Yeah, that\'s right. I mean, we can, we can think a little bit about, yeah, company cultures and whatever, but at the end of the day, it\'s, it\'s, we\'re living in the future. And so it\'s cool for me. Like, I agree with your completely what you said earlier, like that resonates strongly with, I just get so excited when new models come out and I get so excited when new capabilities are released and I don\'t use half of them or, you know, even 20, you know, less than 10%, but it\'s just, yeah, it\'s exciting.

**Nathan Lambert** \[00:30:14\]: I was considering asking this as someone that\'s been in these labs before chat GPT is like what makes a successful AI culture. I\'m coming up on a year in AI too. And I\'m kind of thinking about what, like I have influence on the AI too\'s culture and it\'s visibly less than I may expect, but realistically that\'s all you do is individuals shift very subtly kind of longstanding culture. And open AI has been the one that people talk about the most. What do you view as the most successful things to actually building AI that matters and differentiating that from building like with AI in a way that

**Andrew Carr** \[00:30:56\]: matters? Yeah, this is great. So I actually took copious notes while at open AI. I was intending to write a book on their research culture, never got around to it, but I try to implement a lot of that. That\'s what I should do.

**Nathan Lambert** \[00:31:11\]: Books are overrated.

**Andrew Carr** \[00:31:12\]: Yeah, it\'s, that is not, not, not wrong. You know, I try to implement a lot of this at cartwheel, although we\'re much smaller. There\'s a few things that there\'s a few things that matter and these are all going to probably sound obvious, but they have to be internalized by the scientists.

**Nathan Lambert** \[00:31:27\]: I think they sound hard to implement.

**Andrew Carr** \[00:31:30\]: They\'re super hard to implement, right? So we\'ll maybe state them first and then talk about ways to implement. So the first thing is simplicity is the only thing that matters. But what I mean by that is, um, you know, we care about scale at open AI. We care about, they cared about like being able to build on top of other people\'s work. And so it has to be the simplest thing. So hacks are not allowed. He\'s like, you cannot hack things in. It has to be true to some sense. Right. Okay. Um, and then the next thing is ownership. So each scientist is responsible for a thing, right? And, and you\'re going to say a piece of truth about the problem. Like the model responds to learning rate in this way. And here\'s my graph and no one, there\'s no time for people to double check. And so it has to be correct and people have to trust you in that. So, you know, you, you have a heated discussion. Yeah. How many of these are you going to go through?

**Nathan Lambert** \[00:32:27\]: Uh, one more.

**Andrew Carr** \[00:32:29\]: Okay.

**Nathan Lambert** \[00:32:29\]: Let\'s finish the list of the discuss.

**Andrew Carr** \[00:32:31\]: Yeah.

**Nathan Lambert** \[00:32:31\]: Um, so anyway, you have to trust.

**Andrew Carr** \[00:32:33\]: And then the third one, you know, uh, let\'s see if I can, Oh, the third one was autonomy. So teams are very amorphous at open AI. You can, you can stand up teams if you want, and then teams disperse and go and work on other things. And it\'s sort of this flat hierarchy. So those are the three that I observed. Simplicity, ownership, and autonomy are three important things.

**Nathan Lambert** \[00:32:54\]: And I think different companies get stuck on different ones. I think AI too, as a research culture, it gets the most stuck. Uh, I mean, like being a research culture gives you a boost of autonomy and at a cost of simplicity, you know, managing or like getting ready to release our big, like next post-training project. And it\'s such a lesson on like how to manage 10 to 15 people that are almost all researchers. And it\'s like, yeah, simplicity, ownership, and autonomy. Along with, um, control. So there\'s no controlling researchers. And I bet open AI struggles with this in some domain. I think they\'re probably better at it because they\'re there. You\'re, you\'re getting a million bucks because you\'re, you\'re there for a reason. You\'re not, you\'re not free to go and do everything else. Um, but like getting people to embrace simplicity, I think is, is hard and goes against some cultures.

**Andrew Carr** \[00:33:42\]: Yeah.

**Nathan Lambert** \[00:33:42\]: It goes against how we were brought up in academia, right?

**Andrew Carr** \[00:33:45\]: Yeah. It goes against how we were brought up in academia, right? You\'re, you\'re rewarded on novelty, not simplicity. And so, but like novelty doesn\'t matter actually for, for most things, what matters is truth and simplicity. Like open AI cares so deeply about the. Like minimum description length principle as this guiding idea, you know, Ilya preset all the time of, uh, intelligence will be the simplest thing. You know, what, what have you? So I don\'t know if that\'s true or not, but yeah, I think that it\'s like this

**Nathan Lambert** \[00:34:21\]: simplicity is kind of a cultural thing. And then ownership is more on just finding talent. I think increasingly in the open, I feel like there\'s just so few people that do all the work. It\'s like the crazy things that a few of us deal with that I do is just like, we tried to do everything because it matters. And it\'s like, yeah, not everyone, you have to be capable of holding a lot in your head and doing it to take ownership of like a few things and go really deep. And that\'s just like what the best people are able to hold more in their head. And then autonomy is almost like a team structure thing, which is like Google could be reordering ordering so many times. It\'s like, if you just have too many managers, it\'s not like the people are not going to feel like they have the ability to impact it.

**Andrew Carr** \[00:35:08\]: Yeah. Yeah. There were, there are far more tech leads than managers at open AI. At least there was when I was there. I mean, it\'s a, it\'s a very different company now. Um, you know, almost 10 X to the size is when I was there. Yeah. Yeah.

**Nathan Lambert** \[00:35:25\]: I just try to spend time understanding these like frontier lab cultures. It\'s very insular as well. Cause all the people at open AI and Google and meta that are like deep leads, like they all talk to each other, which is so, so funny. They all like, they all know what they\'re doing. And then like all these free training people are just trying to make their stuff better and it\'s so funny while the companies are pitted against each other, most of them are just friends.

**Andrew Carr** \[00:35:49\]: Yeah. And well, and the, and the reality of the innovations is that like, Oh, I was able to get a better way to filter the data at scale and that\'s a little bit faster. And I can try two more experiments. Like that\'s where the innovation comes from and it\'s, that\'s fine. And I actually really liked that. But when you see that as a scientist, it\'s like not inspiring for a lot of people to go do that kind of work. Yeah.

**Nathan Lambert** \[00:36:14\]: I describe it as white rice research. It\'s just like, we\'re trying to do the boring things for a fair few years to make sure that the ecosystem is okay, but we need to do this to have cred to then go do more fun things once everything is kind of stabilized, we don\'t know

**Andrew Carr** \[00:36:28\]: how long it\'s going to be going for.

**Nathan Lambert** \[00:36:30\]: It\'s going to be obvious when you no longer need to do the boring thing, but it doesn\'t feel close to it.

**Andrew Carr** \[00:36:36\]: Right. And I like, I preach that so hard here, here at cartwheel to the scientists who want to join the team. I\'m like, you will be looking at lots of data and you will be like making sure it\'s easy to look at lots of data. Like that\'s your job because that\'s the only thing that matters. Like we have a transformer, we have a couple of things like we\'re not going to innovate on those because that\'s not going to change, but increasing data quality by two X will. Make or break the company, you know? Yeah.

**Nathan Lambert** \[00:37:01\]: It\'s like the things that you use the most are like hugging face data set viewer, and then little utilities for because it doesn\'t handle the multi-turn format if you\'re doing. And it doesn\'t handle like pre-training documents. Well, so you need tools to skim pre-training documents and you need tools to handle like post-training data, which is all in this like list of turns thing chosen and rejected. It\'s like, those are the, like, I guess hugging face listening could make those easier.

**Andrew Carr** \[00:37:28\]: That\'s one thing I, I have added to our culture, which is we are tool builders, meaning we build those tools for the scientists next to you. And so we have this thing called data app, which stands for data pipeline. And it\'s just like, it does all kinds of goodness for us. And there\'s like 50 small utilities in data app that we love to use. And like, yeah, it\'s the way to go. It\'s the way to go.

**Nathan Lambert** \[00:37:52\]: Um, related to culture as a co-founder, why do you spend a lot of time writing and editing a newsletter? Like, what do you get out of this?

**Andrew Carr** \[00:38:00\]: Yeah. So I write a TLDR AI, co-write that with a couple of folks. I get a few things. One, I\'m just like a very prideful person. And you and I have talked about this, you know, offline a number of times. I care a lot about brand and recognition. And so TLDR gets me that well, well, no one has heard about Cartwheel. So, you know, I have this personal value.

**Nathan Lambert** \[00:38:22\]: It\'s their mechanism to help people hear about Cartwheel.

**Andrew Carr** \[00:38:25\]: And then that\'s the second one, right? It\'s really good free advertising. Whenever we have something I want to share, which I don\'t do that often, but like, you know, we can plug it in there, but then third, you know, my, my job title is technically chief scientist, um, at Cartwheel and as such, I feel. Very strongly that I need to just know what\'s going on. So, you know, you, you do really amazing summaries. Um, this is my way to, it\'s a forcing function for me to just read everything that there is all of the GitHub repos, try all the models, look at all the releases. Um, so that I know, and it\'s great. I mean, we, we pull in the bleeding edge all the time and it\'s, it\'s been very good for Cartwheel to have me doing that, but you know, it\'s, it\'s a lot of time. I mean, I spend several hours a week on it.

**Nathan Lambert** \[00:39:10\]: I mean, I obviously do this too. And I, like, I have these monthly write-ups of open models and data sets. And when I\'m doing these, it\'s almost always like, Oh, I think this person might be interested in this. It\'s like, we\'re using 10 cents, like personas method a lot right now. And I was like, Oh, there\'s another set of personas that has a better license.

**Andrew Carr** \[00:39:26\]: Like maybe we use that one.

**Nathan Lambert** \[00:39:28\]: And it\'s like, it, it\'s hard to know when these things add up, but also I don\'t know if it\'s like, should, like, why does it benefit to have a technical person doing this and not just somebody that like looks for interesting words, I, I feel like you can\'t just outsource it, but it seems like on paper that you could. It also seems like on paper that you could potentially have somebody and just write the taglines. Cause you look at your audience for TLDR AI, it\'s random, normal tech people.

**Andrew Carr** \[00:39:55\]: That\'s right.

**Nathan Lambert** \[00:39:56\]: Clicking on a couple of things. And like, that\'s right. Is there something about AI that makes it so that the like technical writing in the eye is still so much more valuable.

**Andrew Carr** \[00:40:06\]: That\'s a great, I\'ve never thought about that. Um, I always tell people that most of what I read is noise and there\'s like very little signal in there, but they all have the same words. And so it\'s, I agree. It\'s like hard, it\'s hard for me to imagine even getting a super smart person who\'s non-technical to like without six or eight months of work, get up to speed. Yeah.

**Nathan Lambert** \[00:40:31\]: I mean, this is just something I spend a lot of time on because distribution is changing so much. I think I primarily wonder from the scientist and then what the change of distribution is doing to science, but it goes all the way up the stack to just people with jobs and I say it in most of these podcasts cause it\'s people that I am bringing on normally have some level of distribution and there\'s people that have, don\'t have that and are just prolific scientists, but it\'s normally easier when you have this ability to read and it\'s almost like training your own information process.

**Andrew Carr** \[00:41:07\]: Yeah. And like, you know, my, I\'m much better now at skimming papers and determining if there\'s nuggets in there. And so, you know, when I tweet about papers that I\'m excited about, it\'s mostly because there\'s the nugget to non-nugget ratio is quite high. So like the Meta Movie Gen paper, for example, is one of the best papers I\'ve read in the last six months. And like, I don\'t do a lot of RLHF and preference stuff. So I miss a lot of those good papers, but there\'s just like piles of great things in the Meta Movie Gen paper that could easily be ported to almost any other creative project today that would make things better, right?

**Nathan Lambert** \[00:41:46\]: What do you think the role, like, how do you identify a good technical report? Is it just obvious? I mean, like I have said that like the LLAMA 3 technical report has brought open models ahead by X months, which I believe, but still it is missing a lot of details and they\'re like spicy. The director\'s cut title of the paper that we\'re going to hopefully release in like a month is like the missing details in the LLAMA 3 post-training paper, and it\'s like, like it\'s, it\'s remarkable how little is shown in the It\'s remarkable how little is shared, but still what is shared is still useful.

**Andrew Carr** \[00:42:20\]: Yeah, I think so it\'s incremental, right? The, the papers that get published are, you know, on two-year-old pipelines for the most part. And so what we saw in the paper, what was that?

**Nathan Lambert** \[00:42:32\]: Why do you say two-year-old pipelines?

**Andrew Carr** \[00:42:34\]: Well, I\'m saying because, yeah, let me, let me frame my thoughts. So it used to be the case that pre-training was where there was all the alpha and the meta and the the LLAMA paper has lots of good tidbits on pre-training data filtering and that sort of thing. Now, however, the alpha is actually in post-training, not a lot of good tidbits in the meta paper on post-training, right? And so

**Nathan Lambert** \[00:42:58\]: Is that just because we\'re waiting on scaling? Like does this cycle with the model versions?

**Andrew Carr** \[00:43:04\]: I think so, right? So I think in, in a year we\'ll have amazing post-training recipes from closed labs, like as papers. I think that\'s, I believe that to be true.

**Nathan Lambert** \[00:43:12\]: Because do you think that\'s because like GPT-5 will be so much better that they just have the moat because only two people can do it?

**Andrew Carr** \[00:43:20\]: That\'s what the, that\'s what happened historically. And so, yes, if that\'s what happens, that\'s what that will be the reason, in my opinion.

**Andrew Carr** \[00:43:28\]: Interesting. Yeah.

**Nathan Lambert** \[00:43:29\]: I, I hope so. I hope they continue to care. I do think that the time lag to build the next cluster is why post-training has had such an opportunity and they just have found hills to climb on it. And the chatbot arena plot is so wild where it was like incremental, incremental, incremental, and then open AI, like figured something out. And like, they just started hill climbing on chatbot arena. And it\'s just like, that is some weird post-training thing. And I don\'t think it is really something that academics can follow. Like we don\'t have evaluations to hill climb on that. We can send models to chatbot arena, but it\'s clear by how direct, like monotonically and fast the progress is that open AI is like explicitly training for that sort of thing, which is a divergence that was bound to happen if there\'s hundreds and billions of users of AI. Those models are going to become very different than the models that AI2 is releasing.

**Andrew Carr** \[00:44:23\]: That\'s right. Yeah, that\'s right. And, um, different in many ways that consumers like, but may not be useful to like the broader AGI goals and missions.

**Andrew Carr** \[00:44:36\]: Okay.

**Nathan Lambert** \[00:44:36\]: Another fun one. I mentioned these earlier. You said that you\'re a meta Ray-Bans user. Um, I also, what do you, what do you use them for? And then we\'ll talk about AI devices.

**Andrew Carr** \[00:44:51\]: Yeah. So I have long been awaiting glasses that are good. Sunglasses. Um, the, there\'s lots of hardware reasons that they\'re good. You know, the, the speakers are really nice. The camera\'s as good as if not better than my phone. It\'s very convenient. Like we were at the theme park yesterday. I have a three-year-old son and I could just like walk behind him and like take a little picture while he\'s doing something fun. And so I get to capture all these moments. And like, as a father, I love that. But then I also like talk to, you know, Lama. I think they have Lama7DB, uh, serving that API, but, um, you know, I can ask it basic questions. And so, you know, and I can, I can see the hints, right? Really what it is. I can see the future here. Like if they have advanced voice mode, which I actually also love. They are building something.

**Nathan Lambert** \[00:45:38\]: It\'s just not in the park yet.

**Andrew Carr** \[00:45:40\]: Yeah. They they\'re building a whole team out in London to do it. They have, yeah. They\'re like doing, you know, Spirit LM is suggestive that they\'ve got this speech to speech thing, um, on lock. Anyway, the point being like, I could absolutely see myself having really amazing conversations about just like stuff that I would think about. History. Have you tried advanced voice mode? I have. Yeah. Do you use it?

**Nathan Lambert** \[00:46:04\]: I was kind of like, this is odd. Maybe it\'s, I kind of was like, this might just not be for me.

**Andrew Carr** \[00:46:09\]: It\'s super odd because most AI is really good for coding and it is not at all good for coding. It\'s like a very different thing. Um, so I use it to do guided breath work, uh, like stretching. I use it to talk about. Uh, famous figures in history. It\'s really good for me to like figure out, you know, there\'s lots of conflicts going on in the world that I don\'t know much about, but it\'s really good for me to just like, talk to it and say, give me up to speak.

**Nathan Lambert** \[00:46:37\]: So you\'re just like leaned in and tried a bunch of things. I\'m guessing there\'s a lot of things that don\'t work on it. I just feel like picking it up was like, Oh, this is too uncanny value for me to like lean into.

**Andrew Carr** \[00:46:48\]: Yeah. It\'s super weird. So I, I started out poking the boundaries of what the voice itself could do. So I\'m like, do a, like speak in Japanese with a cowboy accent. Like, can you do that? You know, I know some Japanese. And so it was like fun. You know, I did that with my family, but then I was like, Oh, tell me about historical Japanese quotes, like phrases that are integrated into society in Japan. Amazing. It did like incredible job outlining all these things. I\'m like, Oh, okay. I, it seems like it actually really understands people\'s and cultures. So then I like went to history. So. So this is good.

**Nathan Lambert** \[00:47:20\]: I feel like it\'s surprising to me because I am a very auditory person. Like I listened to a lot of media and that\'s why I like do things like narrate my own blogs and stuff. That\'s why I was like, Oh, it\'s like, is it almost like, is it actually a red flag that I can\'t use it? Or like just didn\'t latch on. And I, are you a Ben Thompson reader? Cause he\'s another person that\'s like, this is obviously the future.

**Andrew Carr** \[00:47:41\]: Yeah.

**Nathan Lambert** \[00:47:41\]: And I can feel that when wearing the Ray-Bans, I just think that the AI thing is very unproven. And I do think that agent stuff would be better. Like I think that meta AI is like more constrained than Siri, but arguably does all the same things I already do with Siri, which is remarkable that it\'s doing it in a sandboxed app. So it\'s like, clearly there\'s signs of life there if we put up with Siri.

**Andrew Carr** \[00:48:03\]: That\'s, that\'s exactly right. I mean, I can see, yeah, I came to the same conclusion. You know, I can ask it to do stuff and it\'ll say, Oh, I can\'t do that right now for these reasons. Like it can reason about that reason, but like, it\'s very clear. It can communicate what it can and cannot do, which Siri, I mean, just never is going to do right.

**Nathan Lambert** \[00:48:23\]: Well, the Apple intelligence, wasn\'t it supposed to come out in two days?

**Andrew Carr** \[00:48:27\]: We\'ll see. We\'ll see. I mean, I\'m not an iPhone user, but just, you know, maybe I\'ll put on my cards. Um, but like, I could feel like I could feel that they had just done, um, length constrained tuning on llama to make it only respond to really short. Snippets and then have like a really constrained system prompt. Like, that\'s what it feels like when I talk to it. And so I\'m like, Oh, well, those are fake. Those are like fake limitations. And so imagine throwing those away. It can do everything that I do with Claude, you know, in two years. Gosh, how cool is that? You know, like I\'m working in the garden. And I\'m like, Oh, is this a weed or okay. Great. Or like, Oh man, how do I need to water more or whatever? But like, you\'re right. It\'s not a coding tool. And I don\'t think it ever will be.

**Nathan Lambert** \[00:49:08\]: I\'m trying to balance how much of this is an AI story, or is it just like AI gave it enough momentum to make people reconsider it because I think the form factor of the glasses would be fine with and without AI given that I use AirPods a lot, I understand why these would be just like AirPods plus plus for me. And I, the AI makes it much harder to forecast or like I\'m trying to disambiguate the AI-ness from the other stuff.

**Andrew Carr** \[00:49:37\]: Yeah. So I think, I don\'t think people are adopting it today for the AI. Um, I think that is true. Like I love the camera, you know, that\'s what I opened with the camera and the audio and the. Yeah. Yeah. That\'s what everyone does.

**Nathan Lambert** \[00:49:49\]: This is what I do. I have a draft written on it and I have the same stuff, which is why it\'s just like, we\'re saying the AI is driving the future and generative AI is what everyone points at, but it\'s like maybe a little bit more messy. It\'s like Waymo isn\'t about generative AI, but it\'s one of my favorite technology experiences. And it\'s like these things, it\'s weird that they\'re all at the same time.

**Andrew Carr** \[00:50:15\]: Yeah. I mean, well, and you and I both know pretty strongly that like it\'s actually compute plus data plus deep learning that makes a lot of these things work. And like, you know, there\'s all kinds of great stuff in the, in the auditory system of the, of the glasses that are probably driven by some little network in there, you know, Waymo\'s full of little networks. Um, but yeah, that\'s a good point.

**Nathan Lambert** \[00:50:40\]: That\'s why I\'m kind of like, I don\'t know exactly. I think it\'ll look in the past and we will look back at this as all being an AI story, at least for the glasses, because what you have said is very obvious. But it\'s just kind of funny to live through it and be like, Oh, some of these things are a little out of order, but that is given net advantage.

**Andrew Carr** \[00:50:59\]: Yeah. And, and, you know, there\'s, there\'s a business story here. Like they\'re trying to find their platform on which to own and dominate because they feel beholden to the existing platforms. And so it could be a platform first and then the usability, hard to say. That\'s do you think Lama?

**Nathan Lambert** \[00:51:17\]: What do you think about the whole Lama strategy?

**Andrew Carr** \[00:51:21\]: Yeah, I right. So as I understand it, they released all this stuff to say, make our open source ecosystem so much better so that we can then like, like bring this up again. So this was, you know, PyTorch reacts. They\'ve done this all over. Um, it feels a little bit different because in theory, like anyone who\'s good at coding could write a react alternative. Um, but no one who\'s good at coding could like train Obama alternative without substantial capital investments. So it\'s different. Yeah. Um, and in as much as progress is driven by access to GPUs, the community is not going to make these better for meta. Like they\'re going to make it better for themselves, but it\'s so cheap for them to say, what if some crazy academic comes up with some amazing thing? Like, you know, maybe this in tropics sampling thing that\'s going around, like is that thing, and it\'s only good enough because Lama is going to play maybe it\'s so it feels sort of like a shotgun just in case approach, but like they don\'t need it, I think it\'s not, they don\'t need us to make Lama better. Yeah.

**Nathan Lambert** \[00:52:27\]: The whole developer ecosystem for AI seems extremely under like, or just not locked

**Andrew Carr** \[00:52:32\]: in.

**Nathan Lambert** \[00:52:32\]: I think it\'s like anthropics API numbers are very similar to open AI Lama has this whole thing where they\'re trying to make the Lama models default, which, you know, which converges a bit where people train similar model sizes to Lama. Um, and there\'s reasons why those model sizes exist based on like how big an H100 node is and all these things. So there\'s like very structural reasons why they exist. And it\'s, we\'ll see where it goes. I was like, that is its own thing. There\'s the whole academic side of things, which is separate, but honestly helped my

**Andrew Carr** \[00:53:03\]: meta.

**Nathan Lambert** \[00:53:03\]: Like it helps all of the truly open stuff a lot to have meta models around, even if the license is weird.

**Andrew Carr** \[00:53:11\]: It\'s kind of a guiding star.

**Nathan Lambert** \[00:53:12\]: So there\'s a lot of.

**Andrew Carr** \[00:53:14\]: Yeah, I think that\'s true. And like, you know, they\'re, they\'re trying to release code base, you know, lingua torch Titan, uh, torch chat. Like these are all attempts, I think, to extend an olive leaf, maybe, I don\'t know, to like the academic community and get, get feedback, but early days, pretty early days.

**Nathan Lambert** \[00:53:35\]: Yeah, that seems good to me. Anything else you want to add?

**Andrew Carr** \[00:53:40\]: No, I, I mean, I love AI, uh, sign up for the beta cartwheel. I don\'t know. What am I supposed to plug? No, that\'s fine.

**Nathan Lambert** \[00:53:49\]: I think, I think that makes sense. Um, nice to talk to you. And yeah, thanks for coming on.

**Andrew Carr** \[00:53:56\]: Yep. Bye-bye.

**Andrew Carr** \[00:54:09\]: Bye-bye.
