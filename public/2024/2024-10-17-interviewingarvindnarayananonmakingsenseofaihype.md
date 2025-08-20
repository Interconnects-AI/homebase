---
title: "Interviewing Arvind Narayanan on making sense of AI hype"
subtitle: "Interconnects Interview #8. AGI, reasoning, what LLMs actually do, and what they don't."
date: 2024-10-17
type: podcast
audience: everyone
visibility: public
post_id: 149851247.interviewing-arvind-narayanan
email_sent_at: 2024-10-17T12:05:59.149Z
---
[Arvind Narayanan](https://en.wikipedia.org/wiki/Arvind_Narayanan) is a leading voice disambiguating what AI does and does not do. His work, with at , is one of the few beacons of reasons in a AI media ecosystem with quite a few bad Apples. I find his arguments well reasoned and completely devoid of hype. Arvind is a professor of computer science at Princeton University and the director of the [Center for Information Technology Policy](https://citp.princeton.edu/). You can learn more about Arvind and his work on his [website](https://www.cs.princeton.edu/~arvindn/), [X](https://x.com/random_walker?lang=en), or [Google Scholar](https://scholar.google.com/citations?user=0Bi5CMgAAAAJ&hl=en).

This episode is all in on figuring out what current LLMs do and don't do. We cover AGI, agents, scaling laws, autonomous scientists, and past failings of AI (i.e. those that came before generative AI took off). We also briefly touch on how all of this informs AI policy, and what academics can do to decide on what to work on to generate better outcomes for technology.

Listen on [Apple Podcasts](https://podcasts.apple.com/us/podcast/interconnects-audio/id1719552353), [Spotify](https://open.spotify.com/show/2UE6s7wZC4kiXYOnWRuxGv), [YouTube](https://www.youtube.com/@interconnects), and [where ever you get your podcasts](https://www.interconnects.ai/podcast). For other Interconnects interviews, [go here](https://www.interconnects.ai/t/interviews).

:::::::: {#youtube2-T1sZXBqMCpY .youtube-wrap attrs="{\"videoId\":\"T1sZXBqMCpY\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=T1sZXBqMCpY){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

### We mention

-   AI Snake Oil ([Substack](https://www.aisnakeoil.com/) and [book](https://www.amazon.com/Snake-Oil-Artificial-Intelligence-Difference/dp/069124913X))

-   [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)

-   [CORE-Bench](https://arxiv.org/abs/2409.11363) and Sakana [AI Scientist](https://sakana.ai/ai-scientist/)

-   [Dwarkesh Patel](https://www.dwarkeshpatel.com/)

-   [AI2](https://allenai.org/) and [Molmo](https://molmo.allenai.org/blog)

-   [Scaling Myths](https://www.aisnakeoil.com/p/ai-scaling-myths), [Will Scaling Work](https://www.dwarkeshpatel.com/p/will-scaling-work), and [Situational Awareness](https://situational-awareness.ai/)

-   [Tim Dettmers](https://twitter.com/tim_dettmers)

-   [SWE Bench](https://www.swebench.com/)

-   [Dylan Patel](https://twitter.com/dylan522p?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)

-   [Nicholas Carlini](https://nicholas.carlini.com/)

-   [Aurora supercomputer](https://en.wikipedia.org/wiki/Aurora_(supercomputer)), plans for [AuroraGPT](https://www.hpcwire.com/2023/11/13/training-of-1-trillion-parameter-scientific-ai-begins/), and [Argonne Labs](https://en.wikipedia.org/wiki/Argonne_National_Laboratory)

-   [Dolma Dataset](https://huggingface.co/datasets/allenai/dolma)

-   [National AI Research Resource (NAIRR)](https://nairrpilot.org/)

### Chapters

-   \[00:00:00\] Introduction

-   \[00:01:54\] Balancing being an AI critic while recognizing AI\'s potential

-   \[00:04:57\] Challenges in AI policy discussions

-   \[00:08:47\] Open source foundation models and their risks

-   \[00:15:35\] Personal use cases for generative AI

-   \[00:22:19\] CORE-Bench and evaluating AI scientists

-   \[00:25:35\] Agents and artificial general intelligence (AGI)

-   \[00:33:12\] Scaling laws and AI progress

-   \[00:37:41\] Applications of AI outside of tech

-   \[00:39:10\] Career lessons in technology and AI research

-   \[00:41:33\] Privacy concerns and AI

-   \[00:47:06\] Legal threats and responsible research communication

-   \[00:50:01\] Balancing scientific research and public distribution

### Transcript

**Nathan Lambert** \[00:01:00\]: Hey, Arvind, welcome to the show.

**Arvind Narayanan** \[00:01:10\]: Hi, Nathan. How are you? I\'m good.

**Nathan Lambert** \[00:01:13\]: I\'m really excited to meet you. I think some people listening to these know that I\'m now going around and inviting people that I\'ve wanted to talk to for a while to come on. This is the way that busy people can actually have a forcing function to talk. Your Substack is one of my favorites, which is this, now repeating myself with the intro. I\'m going to kind of jump into it. You posted about this today on a recording on Friday, October 4th, it was one of your FAQs, the frequently asked questions for the book, but it\'s like, how do you balance being labeled as an AI critic while also trying to balance the hype, while also it\'s clear that you understand that this technology will have powerful change? How do you approach that?

**Arvind Narayanan** \[00:01:54\]: Yeah. Internally, in my head, there\'s not that much of a contradiction at all between these things. I\'m in general, profoundly optimistic about tech, and that includes most types of AI. One of the things we say in the book is that AI is an umbrella term, so some types of AI don\'t work well at all, but when it comes to foundation models, generative AI, et cetera, in the book, ultimately, in the long run, we\'re optimistic, and certainly, speaking for myself, I am a heavy user of generative AI myself, so even in the near term, I can see the positive impacts in the long term very much so. That said, I think if, as a society, we want to realize that positive vision, I think we need a group of people who are getting ahead of the harms instead of waiting until they materialize on a large scale, and I think that that function is systematically undersupplied by the market, and the folks who do do that are often generating alarm more than evidence, and because that\'s kind of what the market for attention rewards, so I think there is room for someone to say, look, I\'m doing computer science research to figure out, okay, these are the harms, and these are maybe overblown harms, et cetera, and I think that\'s really part of what it means to be optimistic, as everyone else is saying.

**Nathan Lambert** \[00:03:26\]: It\'s really similar to what I say about AI2, as part of why I joined AI2 is because I want these researchers to be more vocal about it, because it feels like this is the time. We don\'t do a lot of harm-focused research, so I think that\'s kind of the difference. The research you\'ve been doing, which comes out in the blog, is really focused on different ways that AI can change society, and I think that that is good, and I need to do more work on understanding the methodology that people should be doing based on whether or not you are a technical researcher that wants good outcomes. You\'re both technical researchers, but whether or not you\'re focusing on methods or you\'re focusing on applications is a potential way to do it. I was just in DC this week, and we were talking about public AI, which is mostly to distinguish between private company AI. You had mentioned this with your book, and it\'s like the difference between language model work and getting out ahead of the harms of that versus all of AI is actually harder from a policy perspective than I was expecting. I go to these events, and I expect it to be like, look, language models are taking off now. We can get out ahead of this because there was already attention on AI, but I find it hard because there are existing harms of other types of AI, what you call predictive AI in the book, which we\'ve heard about for years. I don\'t know how to disentangle those for a mass audience because I really think that\'s why the smartest people are in the room, is because we have these big problems with foundation models that are changing things. How do we guide policy to understand the differences?

**Arvind Narayanan** \[00:04:57\]: Yeah, definitely. I mean, policy can be frustrating. I always like to say that tech policy is only frustrating 90% of the time. I very much understand the frustration. As domain experts, we might see things much more clearly than policymakers, but I will say that in my experience, the politicians that we see on television might not be very well informed about tech or really any other subjects, but they do have large staffs of experts and many, many people with PhDs even. And there\'s certainly always things that can be better. But I\'ve, for the most part, despite the frustrations, been gratified by my interaction with policymakers and with the depth with which we\'re able to get into things in some of those more focused, more private conversations, as opposed to what you might see in the media.

**Nathan Lambert** \[00:05:57\]: Do you agree with kind of my presumption before the question, which is that we\'re somewhat earlier in this foundation model scaling phase with when policy conversations are starting? Or were there conversations like this when AI recommendation systems and then they didn\'t have tangible outcomes?

**Arvind Narayanan** \[00:06:13\]: Yeah, I mean, in some sense, we\'re always early. And there\'s that famous paradox, I\'m blanking on the name here, basically, it says if you intervene in the course of technology too early before the evidence for what the harms are is clear, then obviously it might have unintended negative consequences. But if you wait until the technology is entrenched, then it\'s too hard to get the industry to shift course. So yeah, I mean, that\'s always a challenge. I think, in a sense, certainly we\'re early with foundation models, but I think there are a lot of things we know already, there are many materialized harms from foundation models. For example, the generation of non-consensual nodes from text to image models, that\'s just affecting people on such a massive scale. And compared to the scale of the problem, it\'s not been getting enough attention. I don\'t want to work on image generation for that reason.

**Nathan Lambert** \[00:07:17\]: I almost feel like Entropic might be in the same boat. All the tech companies have the same product stack, and they all release the same things within a few months of each other, except for Entropic does fewer of the things than Google and OpenAI.

**Arvind Narayanan** \[00:07:30\]: Yeah, philosophically speaking, it\'s a classic challenge from a utilitarian perspective. It feels like we don\'t want to be part of something that is so harmful, but then one person abstaining from it ultimately doesn\'t change the outcome, because in a sense, we\'re pretty replaceable. I don\'t know how to grapple with that. But just to complete that thought, from a policy perspective, there are many areas where we don\'t know enough right now, most notably when it comes to catastrophic harms. But I think we should be working to develop evidence, and I think that shouldn\'t be just left to researchers and civil society. Policymakers should be actively involved in incentivizing that process of gathering better evidence.

**Nathan Lambert** \[00:08:15\]: Yeah, I guess I\'ve never asked you, I might have asked Sayesh this, but what do you view open source foundation models, the role playing in this kind of figuring all of this out? I mean, there was a popular paper last year on the marginal risks of open foundation models, which has informed a lot of policy. And generally, I think the summary of that was that a lot of the risks are not being made worse. And then this non-consensual deepfakes, it\'s definitely made worse by it. Are there any updates? What are we, six months out, 12 months out?

**Arvind Narayanan** \[00:08:47\]: Right. Yeah. So that was a really fun process to write that paper. I was part of this coalition of about 25 researchers from many different organizations. Were you on the paper? I forget. No.

**Nathan Lambert** \[00:08:59\]: I apologize.

**Arvind Narayanan** \[00:09:00\]: No. It was a pretty big group. Yeah. So, yeah, you had the summary right for what it looked like back then. But that said, it wasn\'t definitive by any stretch of the imagination. One of the contributions of the paper was, look, here\'s a risk assessment framework. And so we have to have counterfactual reasoning. So we have to think about how some of the existing ways of defending against certain threats. I mean, let\'s say disinformation, right? It\'s not a problem for the first time with AI. But we really need to be thinking about how those defenses apply to AI-generated threats, including cybersecurity, various other things. So those are things we could be doing right now. But again, I think this type of research is really undersupplied by the market. There are people doing it, but there needs to be much more.

**Nathan Lambert** \[00:09:46\]: I was going to get ahead of it. And I think O1-type systems could be different, things that are hard to fit into those. We don\'t really know exactly how it\'ll\... It was easier to see where those trends were going until things like O1 happened. I think a text-to-video model is more predictable in my mind.

**Arvind Narayanan** \[00:10:04\]: Possibly. Yeah. I haven\'t thought too much about the safety implications of O1. But here\'s one clear gap in safety testing, right? Even though there are so many people who are doing model safety evaluation, certainly they\'re doing useful things. However, really the concern when it comes to open models and bad actors using them for hacking cyber infrastructure, or whatever it is, is that it\'s not that these models are going to be kind of autonomous agents themselves. At least as of today, they\'re far from capable of really doing that, but that they\'re going to be part of compound AI systems that attackers are going to build in order to be able to carry out bad activities, right? And so if we want a proper safety evaluation, if we want to understand attacker\'s capabilities, unfortunately, we don\'t really have any option but to build those offensive systems for testing purposes. That\'s obviously ethically fraught, probably illegally fraught. Companies aren\'t going to do it because it\'s just unnecessary bad PR for them. And not too many people in civil society are doing it either. But if you look at the cybersecurity community, that has been the practice for 30 plus years and we need more of that.

**Nathan Lambert** \[00:11:12\]: Yeah. It\'s like I would expect some of the cyber researchers and or think tanks to be doing this.

**Arvind Narayanan** \[00:11:17\]: Yeah.

**Nathan Lambert** \[00:11:18\]: It\'s like Nicholas Carlini type of work.

**Arvind Narayanan** \[00:11:20\]: Right. That\'s right. That\'s right.

**Nathan Lambert** \[00:11:23\]: I mean, it can\'t all fall in one person is the thing.

**Arvind Narayanan** \[00:11:25\]: Yeah.

**Nathan Lambert** \[00:11:26\]: I think that\'s the type of thing that I think it would be good for governments to fund. I think so. Because governments cannot, the impression is that they can mobilize a few billion dollars for foundation model policy, compute data, whatever, like academic support. And it\'s like, they\'re not going to train their own model. They definitely can\'t train, you can\'t have like a government model for data privacy concerns anyways. So it\'s like they need to disperse it into these really tactical ways, is what I think.

**Arvind Narayanan** \[00:11:56\]: Although, there has been talk of a government model. The Department of Energy has been advocating for some massive funding for building foundation models for science.

**Nathan Lambert** \[00:12:04\]: The deal is building models. So there\'s the like Aurora supercomputer and they\'re trying to build, they\'re currently training about 8 billion parameter models with a mix of the like data from our previous two models. So it\'s Dolma plus other things and then plus academic literature. And they\'re training 8 billion parameter models and they have, want to increase their allocation on their own supercomputers. They\'re just like, they have to go through the same allocation process to go up to 1 trillion parameters. So they want to do this in an ideal world that just succeeds. But I\'m somewhat of a cynic seeing how hard it is to train these models that I\'m like, I don\'t know how, like, I would rather it be the AI2 and them and we figure out how to merge our efforts. Because if we have the same broad goals, the duplication is long term hard.

**Arvind Narayanan** \[00:12:51\]: Yeah. Is this, is this part of the public AI advocacy that you\'ve been part of or?

**Nathan Lambert** \[00:12:58\]: The Argonne, like the Aurora GPT or what do you mean?

**Arvind Narayanan** \[00:13:04\]: Well thinking about public private partnerships, is that part of the plan and vision here?

**Nathan Lambert** \[00:13:08\]: I\'m trying to come up with a vision for like how open source, like how having actual foundation models that are trained end to end in ways that are fully reproducible and documented, like how that impacts policy. And I think it\'s almost entirely in regulation and making sure that early regulation is informed by actual systems that we can look at in an extremely deep manner. And that includes bringing in social scientists and other people that are not AI native to be able to use these models in ways that APIs don\'t allow. And then education. So I think like Nair\'s mission, the National AI Research Resource, is very much on the education side, which AI2 is a part of, AI2 is a big fan of this obvious asterisk that it needs to be funded by Congress, which is hard. But there\'s kind of other side of things, which is like how the regulatory sphere can have researchers who are established and not necessarily an education system working on these models. And I don\'t know the level of financial investment that that can get behind, but that\'s like what I want to see, like that\'s what I\'m trying to flesh out in policy conversations and like who are the people that would access this and how it is, like AI2 is a research org, we\'re better at doing research than getting the word out. And that\'s a work in progress, but it\'s like how to make it so meta doesn\'t just become that. Because meta doesn\'t actually want, they might insert themselves, but they don\'t have the actual incentives that they want the government poking around in their models, probably.

**Arvind Narayanan** \[00:14:33\]: Right. Right. Fair enough.

**Nathan Lambert** \[00:14:36\]: So that\'s all, that\'s all work in progress. I think we kind of see, I don\'t think I even intended to go this deep in policy, but it seems needed and that\'s why I work somewhere where I can talk. Yeah.

**Arvind Narayanan** \[00:14:50\]: Yeah. Glad you\'re doing that.

**Nathan Lambert** \[00:14:52\]: Kind of taking a step back, you had had this [tweet](https://x.com/random_walker/status/1836148224312455679) where you had said that a paradoxical thing about being on the AI snake oil beat is one of the, is that I\'m one of the heaviest generative AI users that I know. I\'m very pro telling people they should use more generative AI. It\'s like I\'m the person starting the conversation to get people free subscriptions internally because like our students aren\'t used, our students don\'t have chat GPT plus. So they can\'t be like, yeah, right. I don\'t really, I\'m like, here\'s some data, make me a plot. And I put it in my slides for a talk and it\'s like, that would take so long, but what, like, what are your favorite use cases? There\'s obviously notebook LM is popular, which I think will fade. I think there\'s stuff to it, but they\'re like, what do you use it for?

**Arvind Narayanan** \[00:15:35\]: Sure. Yeah. And I\'d love to compare notes. So let me tell you some of my broad categories, I guess. And within each category, there are many use cases. The obvious one, of course, is coding and within coding, you know, there\'s getting starter code for doing a thing or debugging or helping figure out a library or, you know, the right

**Nathan Lambert** \[00:15:52\]: thing in the weeds as a professor of looking at code, which I\'m like, this is the modern type, like the modern research approach. And I love it.

**Arvind Narayanan** \[00:16:01\]: Yeah, no, you have to. And you know, it\'s so easy, I think, as a professor to just become a manager. That\'s terrifying because, like, you know, it could be 20 years and you have a bunch of papers and you\'ve graduated some great students, but then you can\'t do anything yourself. And yeah, I don\'t want to. AI makes it a lot easier. Yeah, that\'s true. And like you said, you know, data analysis, data visualization, that\'s a big one. But one use of coding that I\'m enjoying a lot is building single use apps. So like, you know, I might want to do some data cleaning, right? So I can just create a one time script for that. And I do my data cleaning and then I\'m done. I\'m never going to use that app again.

**Nathan Lambert** \[00:16:39\]: Like what stack is this? Like, I\'ve used Gradio, which I find it to be only OK for doing spaces. But do you have like a self, like as many self hosting that it\'s better at?

**Arvind Narayanan** \[00:16:49\]: No, I mean, a lot of my stuff is things like, like I was saying, you know, data cleaning. I\'m not I\'m not putting out production applications for people to use. I love that you\'re making interfaces.

**Nathan Lambert** \[00:17:02\]: Well, interfaces are nice for making things just a little bit more comfortable, which is why.

**Arvind Narayanan** \[00:17:06\]: But but but here\'s here\'s here\'s another example of single use apps that I think is, you know, it surprised me as someone who\'s been using this for a while, there was this really nice use case that I stumbled upon. This was actually with with my kid. She\'s she\'s five years old. I was teaching her to tell time. And at first, I drew a bunch of clocks on a piece of paper with random times and walked her through them. And she was getting it. But it was kind of getting boring for me to keep drawing these faces. So I pulled out Claude and I asked her to create a random clock face generator. And I gave it my specifications so that it was just at the right level of complexity for her. And then we played it, played with it for like 10 minutes. And she really got it. And, you know, I haven\'t used that app since then.

**Nathan Lambert** \[00:17:53\]: And, you know, this kind of thing, it\'s like the ability to not be daunted by something that seems ridiculous.

**Arvind Narayanan** \[00:18:01\]: Two things.

**Nathan Lambert** \[00:18:02\]: One thing is that the clock reading is funny because most AIs are bad at reading clocks. So with the new AI2 vision model, like one of the lead scientists on data side just got so frustrated that the model couldn\'t read clocks. So we just started paying people to annotate clock data. And that\'s the only reason I could actually read clocks.

**Arvind Narayanan** \[00:18:21\]: But they can\'t read gauges.

**Nathan Lambert** \[00:18:22\]: So like dial gauges are still even if you general even if you solve clocks, you can\'t necessarily read dial gauges.

**Arvind Narayanan** \[00:18:30\]: That\'s really interesting for two reasons. So one, in my application, I didn\'t need AI to read clocks, right? Just generate clocks. And that turned out to be a lot easier problem. And often we have this kind of generator discriminator gap. And usually the discriminator is easier. So here\'s a case where I guess the generation is easier. So you could easily, I think, use this to generate synthetic data of clock faces.

**Nathan Lambert** \[00:18:52\]: Everyone\'s going to be able to solve it now that AI2 is like, we just released the data they\'re just going to turn on.

**Arvind Narayanan** \[00:18:57\]: Oh, nice. Nice.

**Nathan Lambert** \[00:18:59\]: Yeah, but it\'ll be out in a couple of weeks.

**Arvind Narayanan** \[00:19:01\]: Uh huh.

**Nathan Lambert** \[00:19:02\]: Yeah, this makes sense. I think that it\'s like with Claude, I\'ve found, like I built, I\'m writing a mini textbook on RLHF. And it uses like Pandoc to convert Markdown to PDF and ebook and GitHub actions to push it to a website. And I was like, this would be weeks of work to set up, whereas now I just like found a GitHub repo. And I paste the entire file in and I\'m like, it\'s not doing X. And I don\'t have to have any understanding of the abstraction. And I\'ve had this experience with multiple times with Claude, which is passing in like hundreds of lines of code, where I know there\'s a bug and I can describe the behavior and it just does it. And I\'m like, this would be a day in grad school. So for sure. It\'s each one of those is single use worth like 20 plus dollars to me. If you\'re looking at like, if you\'re including the amount that I\'m paid as an employer and things, but I would pay it just because I understand how that stuff pays off. I feel like most people don\'t, but like, that\'s right. And then this relates is like, I don\'t know how O1 will work yet. I think once you can upload files, the things like I\'m using Claude for long context file editing will actually be better with O1 because it has a little bit of time to check its work, but it doesn\'t have some of these things that make it really easy to use Claude, like artifacts and files and stuff.

**Arvind Narayanan** \[00:20:19\]: Didn\'t I haven\'t had a chance to play with it yet, but didn\'t OpenAI just release their artifacts competitor called Canvas? Yeah.

**Nathan Lambert** \[00:20:26\]: I\'m guessing that might be enabled with O1, which would probably solve it. And that\'ll be something that if O1 like models are to succeed, that kind of has to be the case. I\'m not sure if O1 is enabled in Canvas because they also released a new GPT 4.0 dash Canvas model that essentially means that they have like different chat tokens to handle different templates that the Canvas metadata gives them.

**Arvind Narayanan** \[00:20:50\]: I think. Right. Right.

**Nathan Lambert** \[00:20:54\]: On the topic of using AI, do you ever do any training? I was wondering like what the level of, because you do a lot of analysis on harms. Does that involve actually training models in your group?

**Arvind Narayanan** \[00:21:03\]: Well, I mean, we do a lot of technical work. We\'re all doing technical work on a daily basis, right? But most of our research is on evals and so we\'re not necessarily building models. Yeah. So we are doing a lot of evaluation and a lot of what we do involves fine tuning models. But while my grad students made sure they know how to build transferable models from scratch, it just doesn\'t come up in our research because that\'s not, you know. Yeah.

**Nathan Lambert** \[00:21:28\]: That\'s the one I was wondering if, like, do you think it would be easy? Is it just not? It\'s like there\'s so many things to do and it becomes not worth the time. Whereas I\'m wondering if there are specific things, like if it can change the lens on how you view applications and stuff, if you do the training that leads to it, which is what these labs are doing.

**Arvind Narayanan** \[00:21:46\]: Right. I mean, look, if we started a research project and we concluded that that\'s the best way to understand harms or whatever it is, then that\'s what we would do.

**Nathan Lambert** \[00:21:56\]: I\'m guessing you do a lot of prompting things because prompting and evaluation go very hand in hand.

**Arvind Narayanan** \[00:22:01\]: Yeah. Yeah. Okay.

**Nathan Lambert** \[00:22:04\]: This makes sense. Kind of jumping ahead, one of the recent things you had was this CORE-Bench, which is like a benchmark for AI scientists. How did you get interested in doing this? I think me, I\'ve been very hesitant to go into agents.

**Arvind Narayanan** \[00:22:19\]: You have had more work on agents.

**Nathan Lambert** \[00:22:20\]: I just find it hard to be scientifically grounded. So I\'m seeing AI scientists plus agent evaluation. So it\'s kind of like the things that we need to get started. Is that kind of how you, like, how did you realize you needed to do this?

**Arvind Narayanan** \[00:22:35\]: Well, I mean, our whole effort with agents has been to try to make things more grounded. Right. The thrust of our research output on agents has been saying, look, the evaluation is not very rigorous. People are fooling themselves. And one of the high level messages we have as a result of that is kind of this capability reliability gap. Agents are capable of a lot of things, but they\'re so stochastic, so non-deterministic and so unreliable that you can\'t really use them right now, whether in consumer or enterprise use cases. And I think CORE-Bench is continuing that to a certain extent. So we look at this AI scientist work and we understand the aspiration, but we just don\'t think the technology is anywhere near that yet. And we haven\'t tried to evaluate those projects ourselves, but from what we\'re seeing of other people evaluating those, it seems like way overhyped. So we want to see, are there tasks in the research pipeline that are automatable today that we can evaluate in a rigorous way with benchmarks and which, if automated, would actually save researchers a lot of time? It\'s great that other people are trying to automate the entire research process in one go, but we want to start smaller.

**Nathan Lambert** \[00:23:54\]: I just think doing the automated thing is going to read to more of the papers that we already don\'t like, which is like the slightly incremental things. So I don\'t really see the automating of like generating new things in the short term being that useful. There\'s people that say there\'s going to be a whole background economy of agents, and if that stuff is true, they\'re going to be doing research.

**Arvind Narayanan** \[00:24:13\]: I mean, to be clear, CORE-Bench is not about automating the generation of new things. So it\'s about the CORE, CORE stands for computational reproducibility. And this is something I think is missing in the scientific literature, including in machine learning. Ideally, we want every paper to be point and click reproducible so that others can start building on it. But in practice, so many things go wrong. It could be that, you know, you\'re using a slightly different library version. And so some of the parameters are initialized differently, so your model produces a different output or whatever. Right. So not just in AI research, in every branch of research, this is a big pain. So that\'s the part we\'re trying to automate with this benchmark. Yeah.

**Nathan Lambert** \[00:24:56\]: I\'m curious to see how this goes. I don\'t have a ton more thoughts on agents. The next thing on agents is really like, how do you give more leeway to discussions around artificial general intelligence? I\'ll posit that I think all the definitions are mostly smoke and mirrors, but like how agents change the trajectory of progress, because I have huge error bars. I\'m like, I don\'t really know what\'s going to happen. I don\'t think it\'s like AI researchers poof out of smoke because we put a for loop around things. But I do think it\'ll be a substantially different experience to what we, to chat2BT interfaces that we have.

**Arvind Narayanan** \[00:25:35\]: Sure. Yeah. Totally agree with high error bars. Yeah. Sorry.

**Nathan Lambert** \[00:25:40\]: Go ahead. Well, I\'m just wondering how you view agents in these like AGI myths, religion things. They\'re very obsessed with agents and their new terms, like unhobbling of language models

**Arvind Narayanan** \[00:25:51\]: and things.

**Nathan Lambert** \[00:25:52\]: And I try to give them the benefit of the doubt because most of these people are in the labs and I\'m not, but at the same time, I\'m like, this makes no sense. I\'ll get to the scaling laws thing because I\'ve read your piece and I\'ve written up a piece on scaling that I haven\'t published yet. So this like agent thing is leading into that conversation.

**Arvind Narayanan** \[00:26:13\]: Yeah. I mean, so as a preliminary note, I mean, you know, in some cases we should give deference to what people in AI labs think and who are in the weeds of the stuff. But in other ways, I think there might be more likely to drink the Kool-Aid when they\'re in an environment where it\'s self-reinforcing. It\'s a bit of a bubble and it\'s also very much in their interest to believe those things given how much money is riding on this. So yeah, I think we should. Yeah.

**Nathan Lambert** \[00:26:42\]: Like they need to raise the money to reach their revenue targets, to reinforce their existing multiples. So like they need to do these ridiculous Kool-Aid things and that\'s a separate discussion.

**Arvind Narayanan** \[00:26:51\]: Yeah. So a couple of things I will say I think about AGI with, you know, moderately high confidence. One is that the notion that it has to be one general system that does everything out of the box, I think is a total red herring. The part of AGI that I\'m interested in is the economic impacts. Is it going to be able to automate, you know, a wide swath of the kinds of activities that are economically valuable today? And from that perspective, generality is mostly irrelevant. And we\'ve found this in a very small way ourselves while working on CORE-Bench. We were developing a baseline agent for this computational reproducibility task. And what we found is that while AutoGPT, which is a generalist agent, out of the box is not very good, with just like a couple of person, excuse me, with a couple of person days of effort, we were able to train the agent, if you will. I\'m putting training in air quotes because it\'s not machine learning, but just, you know, putting guardrails around the mistakes and prompt engineering and adding a verifier, that sort of thing, to more than double its performance, right? Whereas to build an agent from scratch would have taken very long. So my point here is that I think this is more likely the way we will get to something that looks like AGI, which is that we\'ll start with some general frameworks, but then we will train it for many of the specific tasks that we want to do. And a couple of programmer days of training effort is nothing when we\'re talking about automating a whole kind of line of work. Even ChatGPT has this.

**Nathan Lambert** \[00:28:25\]: There\'s so many models in ChatGPT at this point. Like ChatGPT is a really nuanced system of how it passes information and handles things and stuff like this. So it already has some of this. What is the main tool that AutoGPT uses to orchestrate? Like, what is AutoGPT actually doing?

**Arvind Narayanan** \[00:28:47\]: I don\'t know the answer to that. This is one part of the code where I haven\'t been in the weeds myself. It\'s fine.

**Nathan Lambert** \[00:28:53\]: I\'m just wondering, because Tim Detmer at AI2 has been really interested in SWE-Bench, and he has found similar things where he\'s like, people are overcomplicating this by throwing crazy things at SWE-Bench, where in reality, if you just fine tune a model and do a lot of inference in the specific domain of taking in GitHub issues, it does

**Arvind Narayanan** \[00:29:15\]: pretty good.

**Nathan Lambert** \[00:29:15\]: So that\'s his goal for his year at AI2, is do well in SWE-Bench with really small, specialized models. And that\'s a different example of what you\'re saying, where agents are doing really specific things and you have to guide them. I largely agree. And we\'re also going to see the economics for all of these things be shifting so dramatically in coming times.

**Arvind Narayanan** \[00:29:37\]: So it\'s hard to predict.

**Nathan Lambert** \[00:29:40\]: I don\'t know. That\'s why I\'m waiting for somebody to come along and be like, I have a really clear understanding of what they mean by agents. But I guess the longer it goes on with nobody knowing is like.

**Arvind Narayanan** \[00:29:51\]: Yeah, I mean, well, there\'s kind of one sort of null definition of agents, if you will, a definition by exclusion where you don\'t have to get very fancy at all, which is that unless you\'re using the model itself to figure out how to accomplish the task, as long as you\'re putting any sort of scaffolding around the model, I think we need a different name for it. You can just call it a compound AI system. But I think people are calling it agents. So we\'re just going with that term. We\'re not trying to make the concept too fancy. Yeah, that\'s funny.

**Nathan Lambert** \[00:30:24\]: It\'s like we had arrived on composite AI systems in our 2025 planning. And I\'m sure that\'s I think the role of academia here is to find benchmarks, WeBench, CORE-Bench, and make it clear that these are not like models out of the box. And they\'re just like you have to do entirely new types of engineering. So the things that people are going to solve and build to do this, whether it\'s small other models that read outputs and stuff like that is entirely new research, but it is not just like a while loop and they do everything. Okay, continuing on to scaling, I can kind of give you my, I have a hypothesis or something that I find interesting, and there\'s many, many directions to take this. So I think the two like canonical blog posts references right now are like Dwarkesh\'s post and then your post. And Dwarkesh\'s post ends with like this, I mean, so it\'s like 70% chance scaling works and we have AGI and 30% chance that everything is screwed. And I was like, I agree with the numbers, but the adjectives and the outcomes attached to working and not really bothers me. And I\'ve been trying to understand like what is changing in the language models when you scale and how analogies to like performance being better could work. I\'ve been frustrated with AI safety people that are like log scales and compute, read to like exponentials and evals. Some people are just not careful of talking about it in the AGI world, which makes it a lot worse. And then it\'s just trying to think about like what is actually changing. So what\'s changing is these really small probabilities in the model where it\'s like, we\'re predicting tokens on end on end and you\'re making really small deltas and then it\'s like, and what really it feels like is a small change in nuance for the big models tend to say more interesting things. And it\'s like, even if they have apples to apples eval scores, the big model you can tell is different. And like, why is that? And where\'s that going? And I was kind of listening to Dylan Patel talk about semiconductor fab. And if there\'s this like a thousand step process where they have to have certain nines of reliability. And then it\'s like the difference between three nines and four nines over a thousand steps is like a 40% yield or a 90% yield. And I\'m almost like, what if this scaling is just making it do harder tasks because at each time we just have slightly more reliability. And it\'s like, we are generating a thousand tokens and stuff like this. So I almost like I can buy that as a method for what computational is changing, but it doesn\'t really make it. So any value is guaranteed. It\'s just like, we\'re going to have more robust text generators. And then we still have to do all the work to build applications, to build the scaffolding for agents, to build the infrastructure and make that cheaper. So I\'m like, I\'m like, okay, I think scaling mathematically is going to work because it is a mathematical relationship, but all of the other stuff is largely the burden that\'s on the labs to show us how to use it. So that\'s my theory.

**Arvind Narayanan** \[00:33:12\]: Yeah, no, that, that makes a lot of sense to me. I mean, I feel like there\'s some fundamental category error here. It\'s, it\'s not that scaling will you know, stop making models better, but it\'s a limited sense of better, which just doesn\'t readily translate to having these models do useful things in the real world. And we saw this already with the overexcitement over GPT-4, you know, passing the medical licensing exam and the bar exam and that sort of thing. And then those professionals try to use these models and it turns out, yeah, even if they\'re capable in some narrow sense, all of the hard problems are around how do you integrate this into people\'s workflows and you know, we\'re just so far away from the models being able to take over those entire workflows. And it\'s just not fundamentally something you can learn through just free training on internet data. These, these are types of knowledge that are more similar to writing a bike than descriptions in a book. They exist in the minds of people in organizations, in the relationships between people. And I think those are, there\'s a large set of skills that can only be learned when AI is actually deployed in those organizations and, you know, learning from mistakes and so that to me is the big category. How do we prioritize that?

**Nathan Lambert** \[00:34:32\]: So in one way is the infrastructure build-out will make that easier because all the AI stuff will be cheaper because there\'s more hardware, but like it feels like it\'s almost a social problem to manifest this belief.

**Arvind Narayanan** \[00:34:44\]: Yeah. I, I mean, it is a social problem and I think it has been a social problem. One way I think about this is that diffusion actually poses, puts a speed limit on innovation. I don\'t think innovation can happen in a vacuum. I think scaling can happen in a relative vacuum, but that\'s only going to get you so far. And then if you want to actually make these models useful, it can only happen through a very gradual cycle where you deploy it, you know, with a hundred users gain experience, and then you improve it to the point where a thousand users can use it so forth and so forth. And that\'s exactly what\'s happened with self-driving cars. And you know, I\'m like 90% confidence at least that that\'s going to happen in many other domains.

**Nathan Lambert** \[00:35:23\]: Do you think that self-driving cars is a good analogy? Cause people pose this to me and I don\'t think it\'s quite right because digital does make things easier. Like self-driving car, all the weird robotic humanoid things that are happening, that will be like self-driving cars, but I think that is like, it can be much faster and more off-putting to people\'s day-to-day life than self-driving cars.

**Nathan Lambert** \[00:35:44\]: Like, do you agree?

**Arvind Narayanan** \[00:35:46\]: I think maybe we disagree on how, what percentage of a lot of different professions are, you know, can be considered purely digital, like medicine or law or that sort of thing.

**Nathan Lambert** \[00:35:59\]: So it\'s like the tech ecosystem is going to be accelerated, but what does that actually mean? It\'s like, that\'s kind of your question for me. It\'s like Google, Meta, iPhones all becoming more efficient is not actually probably going to change that much on their revenue numbers or anything.

**Arvind Narayanan** \[00:36:20\]: Yeah. I don\'t know. I don\'t know. And one way to think about this is, if you have recursive self-improvement, have you like automatically achieved AGI? And, you know, a few years ago I used to think that\'s obvious and I think that\'s how a lot of people think, but now I think there\'s actually a very big gap between recursive self-improvement and AGI and it\'ll be relatively easy to get to recursive self-improvements compared to the Delta between that and AGI. Yeah, I agree.

**Nathan Lambert** \[00:36:49\]: I, because I\'m close being mostly in the like fine tuning post-training research. I follow the chatbot arena scores closely. I think it\'s not that closely. Cause I think that they need, like they have big error bars on them, but there\'s been this trend where the models were getting better at like a slow rate. And then in the last six months, what the labs have said is due to like better post-training, they\'ve like been step changes on every time. And I\'m like, this doesn\'t translate to any of this, like, it\'s not a takeoff scenario, but it\'s like, what there\'s very weird dynamics in the pace of improvement right there. And that\'s not even through scaling. So I don\'t really know what to make of that, but that\'s, it\'s such an insular ecosystem in that regards.

**Arvind Narayanan** \[00:37:29\]: Yeah.

**Nathan Lambert** \[00:37:30\]: Are there any applications that you see people outside of tech using AI and particularly good ways? I guess that\'s the early signal that things are changing other than

**Arvind Narayanan** \[00:37:41\]: homework. Yeah. Yeah. Uh, let\'s see. Um, I mean, entertainment is a, is a big one, right? Uh, I have been surprised by the speed with which AI generated music, for instance, has, uh, has become pretty normalized. Yeah.

**Nathan Lambert** \[00:38:03\]: And I, I don\'t know the disp, the proportion, like a way to think about this as like, what are the proportion of GDPs? And like tech is so dominant that it takes such a big change to a either tech or non-tech economy to really make these accelerations and productivity measurable.

**Arvind Narayanan** \[00:38:26\]: Yeah.

**Nathan Lambert** \[00:38:26\]: I don\'t know. I think we\'re just very similar in some of these things. Um, I kind of have, sometimes I start with history, but this is kind of zoom out the conversation, I think. There\'s kind of the question of you started this book a long time ago. You have done other waves of working in technology with privacy and AI. Cause like how it does either perspective from the book or like eight years or 10 years ago, like how does that change how you view today? So you have a lot of people like me that are like, I\'m, this is the time to like establish my career. Like I did grad school. It\'s not serious, but now I\'m like a professional. Yeah. Do you think that there\'s lessons to be had there?

**Arvind Narayanan** \[00:39:10\]: From my experiences working on, on all of these areas. Yeah. I mean, um, I\'ll say that, um, you know, when I, when I look back at what has worked in my career and what hasn\'t, I think, um, one thing that, um, You know, I can\'t give myself any credit for this, but it\'s worked out in retrospect is being kind of opinionated and having kind of a thesis on where things are going in the long run, like a five to 10 year timeframe and, uh, you know, what, what is going to be lacking and kind of undersupplied by the market was how I was putting it earlier. Um, and so my thesis, for instance, uh, way back 15 years ago was that. The tech industry already had too little accountability and that that gap was going to widen. And so that can\'t all come from, you know, lawyers and regulators and humanists. There have to be actual technologists involved in bringing accountability to, to the tech.

**Nathan Lambert** \[00:40:09\]: What was your background before being a professor? Like, do you like a CS PhD?

**Arvind Narayanan** \[00:40:13\]: Yeah, I did a CS PhD. And then I, uh, during my postdoc, I was doing a startup on the side. Um, I had fun, but ultimately I realized that Silicon Valley culture was not for me. I, uh, we, while I liked tech, I liked being on the side of, um, you know, bringing accountability as opposed to full speed ahead. Yeah.

**Nathan Lambert** \[00:40:32\]: We could talk about this much longer, like over a drink. Cause I was like, moving from the Bay area to Seattle is like, I knew that I am unplugging from some of the like frenetic energy of the Bay area, which is like, you want to be able to turn this on and off if you\'re trying to think clearly about the bigger picture of things. So like going to DC is good for this. Cause going to putting almost any of these AI founders into a room in DC would be like, they feel like they\'re in a room of aliens, I feel like. And that is the, it\'s almost like a filter by which a lot of their ideas are going to be tested through to become real. So there\'s just a lot of value in it.

**Arvind Narayanan** \[00:41:11\]: Yeah.

**Nathan Lambert** \[00:41:12\]: And then it\'s like, yeah, you can go on. I was just going to prod you about privacy. Cause that\'s what your previous work is. And then on language models, how all of this, cause this is like web scale data and privacy almost feels like the culmination of sayings. Assume your email is public because eventually it is. And it\'s just like too much information to fathom.

**Arvind Narayanan** \[00:41:33\]: So that was my perspective in graduate school. I mean that, that this whole privacy thing was temporary and you know, eventually we\'re just going to all have to get used to everything being public. And the reason I started doing privacy research was this accountability thing. I thought companies were making these promises of privacy that when you look at their practices were not accurate. And I kind of wanted to do the research to, to show that, to show that they\'re not being fully truthful. And then once I started hanging out with philosophers and legal scholars and sociologists, my views changed quite dramatically. I think empirically, when we look at the last 15 years, the kinds of ideas that I had about that, we will increasingly lose privacy that has not happened like at all. And how do you measure that?

**Nathan Lambert** \[00:42:23\]: Like how do you measure we haven\'t lost privacy?

**Arvind Narayanan** \[00:42:26\]: Yeah, I just, there are kind of concrete measures and there are also broader measures. You can just look at social media privacy settings and, you know, back in 2009, actually a lot of it was defaulting to public and today people are much, much more sensitive about making that right. So that\'s one.

**Nathan Lambert** \[00:42:41\]: Are they not hurt by the data that was already out there?

**Arvind Narayanan** \[00:42:45\]: Uh, no, but I mean, to, to some extent, but privacy is not about you know, the, the monetary value of the data so much as it is about certain social norms and, uh, the way we want to relate to each other. So, so that\'s the other thing I got from philosophers and others. That\'s kind of the fundamental thing we want to preserve, right? Not some computer science sense of access control. Yeah.

**Nathan Lambert** \[00:43:10\]: So it\'s almost like social media. So like their assumption that you had, which is something that I would have agreed with, especially a few years ago still, is that like social media is getting bigger and bigger and those commercial incentives are to make everything public and accessible and for various ad reasons, but like now we see that group chats are becoming more popular and social media is becoming silos and like, I don\'t know how that would be predicted, but it\'s an interesting lesson and then like, how does that carry into what is happening with AI, I think like fair use of copyright aside, but like, how is that going to change how people use models and how big tech is like serving models? Apple\'s models are very different in character than Google\'s, but I do think that they\'re all going to have pretty high standards on training on private information because that\'s like nightmare fuel for these companies as they start out putting somebody\'s social security number with the name or something.

**Arvind Narayanan** \[00:44:04\]: Yeah, I totally agree. And I think some of those privacy violations will be more settled than, you know, just having the social security number in the training data or even at inference time. I think so far it hasn\'t been that much of a problem because for the most part, the products are just the models that have been, you know, pre-trained on, on web data and so there, the privacy issues are relatively minimal, but once you want them to start doing useful things to be really embedded in different applications, you know, if you, if you want a good email assistant, it has to be trained or at least fine-tuned on emails. So then privacy becomes a big issue. And I think the most important thing is at inference time, if you want these agents, I\'m sorry to use that, that buzzword again, but if you want these things to be able to orchestrate things for the user by coordinating between different apps, for instance, you have to break one of the foundational principles of cybersecurity, which is to isolate each app from, from each other. Right. And so it\'s not just the privacy issue of the AI companies themselves having access to the data, but it\'s also that you\'re breaking down these internal barriers within our devices that exist for a very good reason to make it hard to hack into these devices. And so that makes us more vulnerable, not just to AI hacks like prompt injection, but also more traditional cybersecurity hacks. Yeah.

**Nathan Lambert** \[00:45:23\]: Have you thought about secure enclaves for training at all, where you can train models on data that you don\'t own by pulling it in, in a secure manner to the model without ever holding the model?

**Arvind Narayanan** \[00:45:34\]: So, yeah, I mean, I think, I know that companies are doing that a little bit. And then Apple does this, I think for inference as well.

**Nathan Lambert** \[00:45:41\]: They had their whole fancy stack for inference, which is wonderful. How great.

**Arvind Narayanan** \[00:45:47\]: But, but all of that only affects the issue of, of privacy of the data going into the model, right? So there\'s this whole other issue of having to violate, you know, the isolation between different applications on the system. And that is something I don\'t know what to do about. Yeah.

**Nathan Lambert** \[00:46:03\]: So this is like how Apple is, I mean, Apple has been increasingly locked down in their apps with this regard, and it\'s like, it\'s good for the users, but it almost feels like it stifles innovation. That\'s true.

**Arvind Narayanan** \[00:46:13\]: Yeah. There is a trade-off for sure. Yes. Agreed.

**Nathan Lambert** \[00:46:17\]: It\'s like, to what extent are trade-offs going to be revisited because of AI? I recently have been hearing that like climate trade-offs might be revisited due to AI, which is like deregulation primarily because big companies want to use more green energy than they can hook up to their data centers, which comes with some other downsides, which is that other non-clean energy will probably increase a little bit while you\'re having a 10X increase in green energy or something like this. So the word trade-offs is good. I don\'t, I think we\'re still early to try to predict them, but those are like the right things to try to signpost on. Yeah.

**Arvind Narayanan** \[00:46:52\]: Yeah. Okay.

**Nathan Lambert** \[00:46:54\]: I\'m going to kind of transition into your book. I started it. I haven\'t, I haven\'t finished it. One of the anecdotes was that Sayesh asked when you\'re flying, what happens if big tech sues you for your research? Have you been sued?

**Arvind Narayanan** \[00:47:06\]: No, fortunately I have not. I have received legal threats. And actually that was, those were learning moments for me. So I think, you know, when we do this tech accountability type research, companies, it\'s, in a way it\'s hard for companies to sue researchers because it\'s, you know, it\'s pretty bad PR. And so there\'s a couple of reasons they might want to do it. One is they just really don\'t want researchers doing a certain type of activity, so they want to set a precedent, right? So it\'s not about this researcher. It\'s about future researchers. And the other is that the research that someone put out is really damaging to a particular company and they like want to have it taken down, right? And that I realized happens much more often with smaller companies. So it\'s often startups that would often send us those threats because what we were saying was pretty threatening to them. And, you know, I was confident of our research findings, but it also got me to realize that some of the criticism that we often do in our research and writing, like really matters to people, to their livelihoods. And I think that has gotten me to try to be much more careful. There are things even in the book that, you know, two years after the first drafts, I would have worded very differently and more carefully. So that\'s been kind of a learning experience for me. But once Hayash asked me that question, I was kind of a nobody, right? And so I could relatively freely do this kind of thing. But now that our work is well known and the book has had the attention that it\'s had, I think going forward, we need to do some soul searching and try to see how to do this in a responsible way instead of kind of being self-attacking. This leads into another problem for me.

**Nathan Lambert** \[00:48:50\]: It\'s like I don\'t like that having distribution changes how you approach research as a scientist. And it\'s like, yeah, I think that most scientists are not necessarily negligent, but underappreciate how much distribution you can have on the Internet if you play the game. And you obviously do extremely well. I\'m doing well having done this for a couple of years, seriously. But I don\'t think that if you continue this and everyone\'s always thinking about the impacts of their work and distribution, it fundamentally changes how things like the scope of things that can be done. And in that case, I don\'t like that it makes you second guess work that you\'re doing.

**Arvind Narayanan** \[00:49:29\]: Yeah, that\'s totally true. And if what we were doing was purely science, then I think that would be really bad. But it\'s not purely science, right? It\'s, you know, it\'s yeah, 80 percent science, 20 percent advocacy, something like that. So I think it makes sense that those considerations matter to a certain degree. But I think with science, this distorting effect comes about because of social media more than anything else. And I think that is a really big issue.

**Nathan Lambert** \[00:49:57\]: Do you have any solutions or advice to people?

**Arvind Narayanan** \[00:50:01\]: Well, I mean, I think the reason there is such a vacuum of attention that self-interested scientists can fill is because 95 percent of scientists pay no attention to distribution. I don\'t think that\'s optimal. I think a lot of people have this idea that, you know, their research is going to speak for itself. So they\'ll just put it out there and sit back and people are going to subscribe to the journals. I mean, we kind of all know that\'s bullshit, right? And yet people subscribe to the list every week. Yeah, yeah.

**Nathan Lambert** \[00:50:34\]: I almost don\'t know when the right time to worry about distribution is, because if you start thinking about distribution too young, then you\'re probably not going to have the time to develop the important skills to do research. Like I learned to do research not in AI, which I think is actually kind of nice. I did an electrical engineering undergrad and joined as a MEMS system novel robotics person. I was like, huh, AI, like I should do AI. So I was like always at this intersection, but not in an AI group. And it\'s like my advisor is like, I mean, Kris Pister, we\'re still friends. He\'s like, I\'m an established scientist. I just want to build cool things. And we\'re just going to do science. And like if you\'re in an environment where your advisor is from day one, it\'s like we have to care about distribution. I\'m going to do this. Like the pressures are harder. So that\'s something that is fundamental, like shifting science this decade. We\'ve seen the archive, I think, is actually a mode where that happens rather than a cause. I think Internet, like the science will make distribution easy and archive is just a place where things live. It\'s a server. So there\'s a lot of work to do on mentoring. There\'s like more work to do in mentoring when that is an added access.

**Arvind Narayanan** \[00:51:43\]: That\'s true.

**Nathan Lambert** \[00:51:46\]: So anything else you want to add on your book? The book is AI Snake Oil, you can read it, you should subscribe to the blog, as I said in the intro. It\'s a long term process is what I\'ve learned looking at what you\'ve done.

**Arvind Narayanan** \[00:52:02\]: Yeah. I mean, the one thing I\'ll say about the book is that the kinds of AI that we\'re most skeptical about are not generative AI. It\'s, you know, for the most part, traditional statistics regression models that have been recently rebranded as AI and are being used in criminal risk prediction, for instance, to make incredibly consequential decisions about people\'s lives. And you can\'t really predict the future. And so these systems are barely better than random. They have AUCs in the range of like 0.6 to 0.7 and 0.5 as random guessing. And we think that\'s very morally problematic.

**Nathan Lambert** \[00:52:36\]: How do we disambiguate them when people inevitably use language models in these systems?

**Arvind Narayanan** \[00:52:41\]: I mean, they can use language models, but it just depends on what their prediction target is. Right. So trying to predict text sequences is very different from trying to predict genuinely what\'s going to happen in the future. That\'s that\'s not an AI versus human difference. It\'s not like AI is trying to catch up to human accuracy. The universe doesn\'t know what\'s going to happen in the future. So the irreducible error for those problems is very, very high. Yeah, that\'s a good way to put it.

**Nathan Lambert** \[00:53:04\]: I think that that\'s probably my I\'m not I mean, I\'m not done with the book, but that\'s the thing that I want to do better is trying to communicate what is going on in all of AI versus generative AI. I mean, my lane is somewhat narrow. Like I don\'t spend that much time and I\'ll go divvy out into like robotics and some automation things, which I think are not falling prey to those. So it\'s it\'s good to have something to point out, which is like we have work that we need to continue on standard AI, but the way that you view generative AI is probably going to change a lot more quickly. And I find it more interesting because it seems like there\'s more opportunity and I get a little discouraged with all the same predictive AI failures that have been going on for a decade.

**Arvind Narayanan** \[00:53:48\]: Yeah.

**Nathan Lambert** \[00:53:50\]: So I\'m happy to wrap up here as great meeting you, great talking. Yeah, you as well. It sounds like we agree on more things than I would have expected from. I mean, I didn\'t really think through it. It\'s good fun, but the door will be open and we\'ll see where this goes in the future.

**Arvind Narayanan** \[00:54:08\]: OK, wonderful.
