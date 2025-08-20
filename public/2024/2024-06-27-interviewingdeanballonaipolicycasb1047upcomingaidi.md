---
title: "Interviewing Dean Ball on AI policy: CA SB 1047, upcoming AI disaster response, Llama 3 405B, Chinese open-source AI, and scaling laws"
subtitle: "A roundup on current happenings in AI policy."
date: 2024-06-27
type: podcast
audience: everyone
visibility: public
post_id: 146054905.interviewing-dean-ball-on-ai-policy
email_sent_at: 2024-06-27T21:04:54.943Z
---
I'm really excited to resume the [Interconnects Interviews](https://www.interconnects.ai/t/interviews) with from the Substack (you should subscribe). We cover the whole stack of recent happenings in AI policy, focusing of course on California's bill SB 1047. We cover many, many more great topics here including:

-   What will happen in the case of a minor AI disaster,

-   If Meta will release the 405B model, and why,

-   The status of Chinese open-source AI,

-   Training on model outputs,

-   Anthropic's recent strategy,

-   What scaling laws actually mean,

-   Creating content and shifting the needle of the AI discourse.

Watch the video on YouTube below or listen on [podcast players here](https://podcast.interconnects.ai/episodes/interviewing-dean-ball-on-ai-policy).

:::::::: {#youtube2-Q1mGGmBl8_k .youtube-wrap attrs="{\"videoId\":\"Q1mGGmBl8_k\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=Q1mGGmBl8_k){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

### Chapters

-   00:00 Intro and Welcome Dean Ball

-   02:44 The Origins of California Bill SB1047

-   08:56 The Evolution of Bill SB1047

-   13:00 How SB1047 Affects Fine-Tuning

-   20:00 The Future of Bill SB1047

-   21:58 The Impact of AI Disasters

-   29:02 Meta and its 400 billion Parameter Model

-   32:25 Open Source AI and the Chinese Market

-   37:37 The Future of Open Source AI

-   43:35 Synthetic Data, Licenses, and Future AI Development

-   45:18 Anthropic\'s Approach to AI Safety

-   50:46 Scaling Laws

-   53:01 The Role of Audience in Influencing AI Policy

### Links

-   Dean's series on SB-1047: [one](https://www.hyperdimensional.co/p/californias-effort-to-strangle-ai), [two](https://www.hyperdimensional.co/p/california-senate-passes-sb-1047), and [three](https://www.hyperdimensional.co/p/the-political-economy-of-ai-regulation).

-   Other AI policy Substacks: and

-   [Senator Scott Wiener](https://en.wikipedia.org/wiki/Scott_Wiener). [CA SB 1047 itself](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1047).

-   Another [post on CA SB 1047 from Answer AI](https://www.answer.ai/posts/2024-06-11-os-ai.html).

-   [Situational Awareness](https://situational-awareness.ai/) by Leopold Aschenbrenner.

-   [Lina Kahn on her P(doom)](https://www.tiktok.com/@hardfork/video/7301774206440656171?lang=en) and [warnings in support of open-source](https://techcrunch.com/2024/06/11/ftc-chair-lina-khan-shares-how-the-agency-is-looking-at-ai/).

-   Ben Thompson's [Framework for Moderation](https://stratechery.com/2019/a-framework-for-moderation/) in technology.

### Transcript

**Nathan Lambert** (00:00:01): Hello, and welcome back to InterConnect\'s interview series. It\'s been a few months. I\'m really excited for this one. We\'re here with Dean Ball, who is a research fellow at the Mercatus Center. He works on AI policy right now, and he\'s the author of the Hyperdimensional Substack, which is kind of the AI policy substack that emerged when I was spamming into the void that we need to have some good AI policy newsletters out there. There are a couple more that I could add to the show notes of this that I\'m aware of from friends that used to be at OpenAI, friends at AI2, so I\'ll add some of those as well.

But in this kind of summer slowdown of releases, I thought it would be a great time to kind of revisit some of the core themes on AI policy, open versus closed, kind of things that I\'m wondering about in the future that I know are coming that are looming AI disasters, what some of these closed source companies are trying to do in the policy space. I think this is the sort of interview that we could probably do multiple times. I think we\'ve started talking in DMs and it\'s clear that we\'re aligned on a whole bunch of things. We read each other\'s work. I think this should be kind of fun and I\'m just happy to do this.

I think the core of this interview I\'ll give you a chance to introduce yourself if you want, if you want to add anything else that I missed, and then we\'re just going to go into this California bill SB 1047. Probably talk about this. I\'ll ask you about the story of how it happened and then where we\'re at now. And I think that\'ll kind of lead into a lot of interesting debates. So do you have any background you want to add that makes you an interesting person in the AI space? Or is it just that there\'s so many things that need to be done in AI that if you\'re focused, you can kind of have an impact in an area?

**Dean W Ball** (00:01:44): Yeah, I mean, I think basically, you know, I\'ve mostly written on policy unrelated to tech for my career, state and local a lot. So the fact that a lot of the policy action on AI seems to be happening at the state level has been very relevant. But I\'ve also just like always been paying attention to the AI literature. I remember 2017, I think, when the Alec Radford Amazon podcast product reviews paper came out and I said to a colleague this is gonna be a big deal I think one day and you know we I tried to use GPT-2 to do like social science research like policy research back in 2019 so I\'ve been playing around with these for a while and I try my best to write from a combination of a relatively technically informed person, but also someone who understands the policy side.

**Nathan Lambert** (00:02:43): Yeah, so I think we should jump right into it. What is the origin of the story of this California bill? My understanding is it just kind of showed up and everyone in the Bay Area was like, like where did this come from? Having actually passed the state Senate as like, do you have any, does your story start there as well? Or did you kind of know this was coming?

**Dean W Ball** (00:03:03): So I saw, Scott Wiener, the author of the bill had telegraphed that he was working on, something in AI policy, I think in maybe October or November of 2023. And then the actual bill text came out in early February. And I remember when it came out because I was having dinner with my wife and, I was like, I have to drop everything and go work on this. I stayed up until like one in the morning, you know, reading the bill and writing about it. And that was kind of my first Substack post that really went anywhere in terms of audience. And so, yeah, then there was kind of a couple months of quiet. You know, I had been writing about it, but people weren\'t really focused on it in the Bay, in the tech community. And then closer to around April, people started to pay attention. And the conversation has been pretty, you know, pretty active since then.

**Nathan Lambert**: Yeah. And like, what does it actually say? Like, what are the core points? I know there\'s stuff around thresholds and giving California power to do like California creating a new body. Like, what are you think? What are the few like core things that people should know? I think there\'s probably some details, but just the core stuff.

**Dean W Ball**: Yeah, so the core idea behind SB 1047 is to create a regulator inside of the California government called the Frontier Model Division that would oversee models. Really, now the threshold is models that cost more than \$100 million to train. We can talk about how specifically you really even specify that cost, but really all the bill says is \$100 million of compute costs to train. Those models are subject to a series of testing and safety requirements, and more importantly, I think, a liability regime that basically says that most downstream uses of that model, including in the case of an open source model, most fine tunes, most uses of models combined with scaffolding software, other software. So things that are very combinatorially distinct from the initial model release. Any downstream misuse is the legal responsibility of the developer who made the original model.

So, if I fine-tune Lama 3 and then someone else puts that in an app and then a user of that app misuses it in a way that causes a serious harm, the bill does have a high threshold for the harms that have to count here.

**Nathan Lambert** (00:06:00): Is that eligible? Is it specific? Do they have a safety taxonomy?

**Dean W Ball** (00:06:05): So, they basically, it really, it\'s a static threshold that comes in at \$500 million of damage. They would say harm to critical infrastructure and things like that. Critical infrastructure pretty much just means everything. It\'s kind of a catch-all term. It\'s a little weird. Critical infrastructure, the way we think of it, like highways and power plants and stuff, is actually a subset of critical infrastructure. Critical infrastructure includes things like casinos and ballparks and amusement parks and all kinds of stuff. So anything really, any major cybercrime, bio attack, all the things people are worried about with AI would count. And the developer of the original model, which is many stages upstream from where the harm happened, would have legal responsibility.

**Nathan Lambert**: So it\'s like the risk for these, probably the expected value risk for open models in this bill is definitely low, but it\'s just kind of this thing that it\'s like, if you\'re kind of comparing on the two axes, the open versus closed risk, like the risk for open models is way higher because of this downstream use term. And that\'s for the people that are getting like, oh, why is everyone that cares about open AI, like open AI as the field mad about this? So I think that was why everyone was kind of caught up in ours.

**Dean W Ball**: Yeah. And the other thing to keep in mind, though, is that under this bill, if you\'re making a model more than \$100 million that costs more than \$100 million, you have to submit a variety of documents annually about your safety procedures and sort of testing regime on the model to the Frontier Model Division. And I think something that\'s not all that well understood, and it\'s kind of just like how administrative law and regulation works in America, but that the tech community might not understand, is that the Frontier Model Division has the capability to create problems for developers, even if their model\'s never used for a hazardous capability. They could see your safety plan and say, We don\'t like this or we want more information on this. And they can subpoena you. They can bring you to court and they can, you know, issue it. They could they could order a cease and desist.

**Nathan Lambert**: Yeah. And this is where you only post on the political economy of AI regulation comes in as like, what are they going to do with that kind of open ended power?

**Dean W Ball** (00:08:40): Yeah, it doesn\'t necessarily. I mean, they\'re an agency that has all the regulatory powers of an agency, which are substantial. I think one other point that is worth making about 1047 that would be relevant to your audience in particular is. So the initial version of this bill, any fine tune. No matter how substantial the fine-tune is, the original model developer held the legal responsibility and had to test their models with the margin and the realization that people could fine-tune them or do whatever they wanted to them, modify the weights in arbitrary ways, which obviously doesn\'t really make a ton of sense.

**Nathan Lambert** (00:09:38): I was going to ask about the edits. This is where I probably stopped reading as closely as I should have.

**Dean W Ball**: In a fundamental sense, everything I\'ve said so far has basically been true of the bill for the entire, the fundamental points, the liability, the frontier model division, these kinds of things. Basically, the actual making developers guarantee model safety when I think we\'re probably both in agreement that safety is not a model property.

**Nathan Lambert**: Yeah, at least in the way that the bill concerns it. They\'re considered about infrastructure. If critical infrastructure is the primary target, safety is not a model property. This is why I ask about a taxonomy. It\'s because it\'s like\... We\'re going through this exercise at AI2 to kind of say like, what do we mean by safety? And it\'s a total headache. It\'s like extremely hard to get this right and to communicate it clearly. So now when any other organization or somebody mentioned safety and I\'m like, oh, do they actually define it? Like it\'s such a risk to put it into words because when you put it into words as well, you\'re exposed to all this like people being like, so you don\'t care about X, Y, and Z. If you don\'t put it explicitly, it\'s like a total trap.

**Dean W Ball**: Well, and actually just to expand on that a little bit, because, you know, the Center for AI Safety, which is the nonprofit that was heavily involved in authoring the bill and Senator Wiener, you know, one of their primary concerns is bio risk. So people making biological weapons with AI models. You know, and I think people who don\'t understand biology all that well have this idea that you can say, oh, well, that\'s a good idea. biomolecule to make, and that\'s a bad one. And so we\'ll make a list of the bad ones and you can\'t make the bad ones. And that would be a way to like, RLHF, a biological foundation model.

**Nathan Lambert** (00:11:34): My understanding of biology is that the more powerful, the more specific a molecule is, it\'ll probably have good uses and downsides. It\'s like Teflon. Amazing physical properties, extremely bad downside health concerns. I would guess, obviously, if you\'re consuming\... engineering like living creatures it\'s going to be a little bit of a different consideration but yeah.

**Dean W Ball** (00:11:56): But I mean also a lot of biomolecules just and like code um their their goodness or badness is really context dependent they\'ll do different different things in different settings and so it\'s not necessarily easy a priori to identify you know what what what how even would you steer a biological foundation model, like something that\'s predicting protein structures or nucleic acid sequences or whatever it may be? How would you even steer that towards safety? It\'s not like a priori obvious that that\'s currently possible. But that\'s just, you know, I think this idea that safety is something that can be legislated in that way, I think is a fundamental problem.

**Nathan Lambert**: So what is next? Or you could continue. I was going to ask, what is next for the bill?

**Dean W Ball**: Oh, yeah, yeah. So I\'ll just say one thing about the fine-tunes in the most recent amendments to the bill. So fine-tunes now, if you do a large fine-tune, large being anything more than 3 times 10 to the 25 flops involved in the fine-tuning compute,

**Nathan Lambert** (00:13:13): I need to learn all these numbers. I need to learn what they mean. I need to know. Essentially, it\'s a linear relationship between model size and tokens. And then you should be able to have specific points, which is like, is Lama 3 base crossing that? Like 15\... trillion tokens at 70 billion parameters like I think I I don\'t know I\'ll loop back on this I need to know this in the future.

**Dean W Ball** (00:13:35): It would be as much fine-tuning as you use as much compute as you use to fine-tune the model that\'s how this threshold is calculated.

**Nathan Lambert**: Yeah I was just one like a rule of thumb for people would be great I\'ll figure that out it\'s on my to-do list of mental mental math that would be great.

**Dean W Ball**: That would be great to do um but if you\'re in that situation uh then the bill applies to you too. So you have to create a safety plan and a certification that you submit to the Frontier Model Division every year. Starting in 2028, like the foundation models, you\'ll be subject to mandatory annual audits.

**Nathan Lambert**: Is this prescribed to anyone that trains in California or anyone that operates their model in California?

**Dean W Ball**: Anybody that distributes a model in California. So the bill is at least everyone in the United States, if not really everyone in the world. Certainly, but they could certainly sue you in the United States if you\'re an American company or operating in America. Now, the important thing about that fine-tuning threshold, though, is that the fine-tuning threshold can be lowered arbitrarily by the frontier model division. So the \$100 million threshold for foundation models, that\'s fixed in statute. So you would need an act of the legislature to change the \$100 million threshold. But the fine-tuning threshold, there\'s no dollar amount. So the same problem with compute thresholds, that compute cost is getting cheaper and cheaper rapidly over time. applies and the frontier model division can change that threshold arbitrarily.

**Nathan Lambert** (00:15:35): Who elects these officials? Is it like the governor of California? Or the federal branch or something?

**Dean W Ball** (00:15:43): This is all state-based.

**Nathan Lambert**: Oh yeah, I meant in the state.

**Dean W Ball**: Yeah, so the frontier model division would be staffed by unelected civil servants, primarily. Led by unelected civil servants. And then on top of the frontier model division, uh, the new, the newest version of the law creates a committee that is like a governing committee. And that committee is composed of, I believe three members appointed by the governor and confirmed by the legislature. And then two members that the legislature itself points each house, the Senate and the assembly.

**Nathan Lambert**: Mostly what I would expect.

**Dean W Ball**: Yeah, yeah, exactly. And like, I think there\'s a requirement that, you know, one person has to be from industry, one person has to be from the open source community. There\'s a lot of, there\'s a lot of bones that they throw to the open source community.

**Nathan Lambert** (00:16:37): Random credentialing.

**Dean W Ball** (00:16:38): Yeah, yeah, exactly. But I mean, I don\'t really, that could be anyone, you know, really, like, yeah, who\'s who\'s from the open source community? Exactly. Yeah.

**Nathan Lambert**: Um, so what\'s next for this? Like it passed this, it passed the state Senate and then it got revised by the, what is the state, like state general state house. Is that how it works? The state assembly revised it. Does it then they would have to vote and then the Senate would have to vote again. And then the bill would have to actually be signed. Is that how, is it worked that way in California? Yeah.

**Dean W Ball**: Yeah, basically. So so it\'s right now making its way through the committee. So it went through the Senate committees and then was voted on by the whole Senate. Now it\'s going through the assembly committees. It just passed one, I think, last week or the week before the Consumer Protection and Privacy Committee is what it\'s called. I could be wrong on the exact name, but that\'s the basic idea. So they just passed it. They did some amendments. It goes to the assembly\'s committee. judiciary committee next and then uh eventually it will go to the full assembly for a vote and then to the governor for uh for signature or veto.

**Nathan Lambert** (00:18:04): When would this start? When would it kick in?

**Dean W Ball** (00:18:00): Uh the bill would kick in I think most of its provisions would start January 1, 2025.

**Nathan Lambert** (00:18:05): Yeah. And the original vote in the state Senate was like very pro, right? It wasn\'t even like, it was just like, Oh, this seems normal checkbox for, but this is kind of a cynical take, but I kind of viewed it as mostly these politicians are serving constituents that know that AI is a big thing, but know nothing about AI. So for a politician saying, look, I\'m taking action on AI and they\'re not going to be able to decipher any of the details is probably a political win.

**Dean W Ball** (00:18:31): Yeah, well, and I think also worth noting is that Scott Weiner, the state senator who authored the bill, is a very powerful figure in California politics. And I would guess that a lot of the senators who voted in favor of the bill really barely looked at it and aren\'t even necessarily thinking about their constituents. First and foremost, they\'re thinking more about, well, Scott\'s my ally. I need X, Y, Z thing from Scott. So I\'m going to vote yes on his bill. Um, and that dynamic will apply at the assembly too is, is very common. Uh, the, the California legislature has a history of, um, uh, sometimes even unanimously passing bills that the governor then vetoes. So the governor is often expected to be a little bit the adult in the room on this stuff.

**Nathan Lambert** (00:19:25): This is so funny. I have no comment.

**Dean W Ball** (00:19:27): I do suspect that the governor is probably going to be, whether or not he wants to, he will probably be the final voice on this bill.

**Nathan Lambert** (00:19:41): So that\'s who people are talking to, probably, realistically, from what you\'ve said.

**Dean W Ball** (00:19:46): Yeah. So, I mean, the one thing, and this is, again, this is a kabuki that\'s very common in state legislatures. The governor has not said anything publicly about SB 1047 specifically. I think he\'s as a general matter, he tries not to comment on legislation that\'s in process.

**Nathan Lambert** (00:20:08): That makes sense.

**Dean W Ball** (00:20:09): Yeah. And then kind of. But, you know, he also might signal in various ways. He there are times when it gets closer.

**Nathan Lambert** (00:20:17): I would guess they do.

**Dean W Ball** (00:20:18): Yeah. I mean, like he could say, you know, a lot of bills. I think one outcome that is extremely unlikely from this bill is that it\'s like voted down by the assembly. Like, I don\'t think that\'s going to happen. It could die in the assembly. It could just kind of be forgotten, never get brought to a vote, or it could go to the governor and be vetoed. If the bill\'s not going to pass, it\'s going to probably be one of those two ways.

**Nathan Lambert** (00:20:43): Okay, that\'s a great little lesson in state politics that I\'m sure the vast majority of people listening to this will not know. I did not know all of this. Do you have any final comments on this? Otherwise, we\'re going to move into kind of fun, faster questions and discussions.

**Dean W Ball** (00:20:59): Yeah, sure. Let me just think. I think the one other thing that is worth keeping in mind here is that the latest version of the bill, I mentioned this, but just to expand on it a bit, it does require mandatory audits starting in 2028. So if you make a covered model or a covered fine tune, however, the Frontier Model Division chooses to define that. Not only do you have to submit stuff to your certifications to the Frontier Model Division and have the legal liability and all that, but you also would have to comply with an audit done by a private company. So just like accounting, you pay for someone to come in and look at your stuff. And the auditors are, it\'s not an open market for competition. The auditors are licensed by the Frontier Model Division. So it\'s probably two or three different, companies that\'d be doing that and it\'s probably that\'s the sort of thing that i

**Nathan Lambert** (00:21:59): think people have wanted i don\'t know if you want it like we don\'t i don\'t think people i don\'t want all these types of oversight to be cobbled together i think individually each of them have different types of merit but like the execution is important and then when you cobble them together it\'s like wait wait wait this is this is too much

**Dean W Ball** (00:22:19): Well, and also I think I think it\'s just questionable whether I agree that an audit like structure like that might be the good long term way to go. I think it\'s questionable whether a California state agency really has the capacity to do this kind of assessment of like who is an accredited auditor. That feels much more like a federal responsibility. So, yeah, but that\'s I think that\'s that\'s pretty much the main message on 1047.

**Nathan Lambert** (00:22:49): Yeah. Okay. I\'m going to move into other fun questions I have. I\'m going to start with one that\'s potentially related. I\'ve been trying to get my brain around what is going to happen when there is actually a minor disaster from AI. It loops into open versus closed debates. I think a lot of the things I\'ve been talking to people is it won\'t actually be about whether or not it was an open or closed model. It\'s some weird infrastructure that people plugged it into and that causes the power plant to go down. Do you have any ideas about how this will happen? I\'m expecting this to happen within a couple of years. I feel like the state of our infrastructure is that it is not that reliable and that we\'re adding all this new digital information into it. And I think all of this is very fragile digitally. So it\'s like, I think this is going to happen. And how do we preempt any communications around that?

**Dean W Ball** (00:23:37): Yeah, well, I mean, you know, cyber attacks take out digital infrastructure or take out critical infrastructure all the time. You know, earlier this year, I think maybe it was last year, courts in Dallas could not convene. Like there were no judicial proceedings in the city of Dallas because of a major cyber attack on the judicial system\'s computers. Parts of the power grid go down. Water plants go down. Hospitals all the time. This happens. \$500 million in critical damage. That sounds like a lot. It\'s not actually that much.

**Nathan Lambert** (00:24:13): It doesn\'t have a B on it. It doesn\'t sound like a lot.

**Dean W Ball** (00:24:18): Exactly. It\'s a big economy. I think about this all the time. I think a couple things are very likely to be true. If there is\... an attack of this sort, people will probably suspect that AI was involved, whether or not we get, how are we going to know? Right. Let\'s say like somehow we do have a strong hunch that an AI model was involved.

**Nathan Lambert** (00:24:47): Yeah, like, do we normally figure out what happened in cyber incidents? Or is it normally post hoc? Or not at all? I guess that\'s a good thing to know with my question. It\'s like, can we know that a language model is actually involved? Like, how often will they be able to get that far into the stack of the attack?

**Dean W Ball** (00:25:02): Yeah, right. Like, I don\'t know. I mean, like, probably they\'re\... I mean, if you were using, like, an agentic GPT-6 model to do some kind of zero-day exploit on something, like, presumably in the server logs, like, you\'d be able to see that, like\... what was interacting with it. Right. But like, who knows if that would be masked, but I, so, so let\'s just say though, that we, we have some, you know, circumstantial evidence to suggest that an AI model was involved in the execution of, of some cyber attack. It\'s like very much to me, unclear, unclear, Are we going to have like the person\'s chat log? Like, are we going to know how they prompted the model?

**Nathan Lambert** (00:25:46): Like, I mostly think it\'s like it\'s going to send requests over some generic Internet protocol. So there\'ll be this big gap where we can\'t really tell.

**Dean W Ball** (00:25:54): Yeah. I mean, that could totally be true. That could absolutely be true.

**Nathan Lambert** (00:25:58): So I expect there to be -- it\'s like almost if somebody takes ownership or does a really bad job or it\'s an own goal, which is like a hospital implemented some agent and then it took down their authentication system type of stuff.

**Dean W Ball** (00:26:12): Yeah. No, that could very well -- that\'s all definitely possible. Yeah. I think that, though, how would we actually know what an AI model was used for? It seems to me like we don\'t actually\... People are imagining a situation in which this happens with perfect information.

**Nathan Lambert** (00:26:32): Yeah, I think that\'s the answer to my question. It\'s not that it\'s like what happens. We can\'t answer what happens because it\'s so much of a media question. It\'s like we won\'t know. It\'s likely to happen, but it\'s very unlikely that we know the specific stack that caused it. Which makes it more of the same around like if cyber incidents increase in rate, then people will talk about AI and people like without actually having the logs, it makes it easier to spin narratives. Because I\'m worried that this could be like people are like, oh, this is why open source AI is bad. Yeah. And it\'s like, I don\'t expect to have any proof for that, but I expect that to be what people say.

**Dean W Ball** (00:27:10): People are going to blame AI on things that were already happening. I think that\'s like a trend that we will see across the board. Whether it\'s misinformation or whether it\'s cyber attacks or whatever else, like there are all these curves that we\'re already pointing up and they\'re going to continue to most likely. And I think people will blame that on AI. Now, like the sort of, you know, long tail situation is like, what if something really bad happens? You know, what if a power plant, you know, no one has water in Los Angeles for a month or something like that. And in that situation, not only do I think that an attack could be hastily blamed on AI without us knowing whether that\'s true, I also think we could see legislation move very, very quickly. The Congress, the federal government is not known for moving fast, but in a crisis, they will move fast. It\'s for the same reason that I suspect, I don\'t think he is right, but if Leopold Aschenbrenner is right about super intelligence being here and, you know, 50 months or whatever he says.

**Nathan Lambert** (00:28:26): Yeah. This is another one of my later questions, but I didn\'t have the best way to frame it.

**Dean W Ball** (00:28:32): Yeah.

**Nathan Lambert** (00:28:33): Like AGI timelines and stuff.

**Dean W Ball** (00:28:35): Yeah. Like if he\'s right about that, then like, yeah, I mean, that\'s going to get nationalized by the federal government and it\'ll happen in a heartbeat.

**Nathan Lambert** (00:28:42): You know, I found it interesting that Alexander Wong of scale was also kind of touting this point of view. Yeah. I guess it makes sense for them because they\'re the only AI company that is leaning into federal contracts. Yeah.

**Dean W Ball** (00:28:59): And they were before ChatGPT, too, I think.

**Nathan Lambert** (00:29:04): Yes, they have been for a long time, which is why it was easier for them to continue.

**Dean W Ball** (00:29:08): Yeah, their early big revenue source, I think, was federal government contracts.

**Nathan Lambert** (00:29:13): Okay. Yeah, we might come back to AGI. I\'ve been confused by the\... lines they\'re drawing. I have a quiz to debate later on. I don\'t even know the answer. We\'ll see if we get to it. But another fun question. Do you think meta will release the 400 billion parameter model? And if there will be any governance questions around that?

**Dean W Ball** (00:29:32): Will they release it open source?

**Nathan Lambert** (00:29:34): Open weights in a similar manner to the other models. Yeah.

**Dean W Ball** (00:29:37): Yeah. Open weights.

**Nathan Lambert** (00:29:42): Do you think they have government? I\'ve been decreasing probability. At best, I was ever 50-50. But is this for government\'s reasons that you don\'t think? Are they flying? They\'ve always been flying close to the sun where there\'s back channel discussions where it\'s like, The Biden administration is telling Meta that they\'re like or they\'re not invited to stuff because they\'re not happy with how they\'re like open waiting models through this other like probably they\'re probably getting lobbied by people saying open source is bad. But it has always seemed like Meta is on kind of thin ice with the executives in Washington. And I\'m guessing it\'s reasonable to say that this model\'s release is bad. heavily influenced by feedback they\'re getting there. And Zuck will make the final call.

**Dean W Ball** (00:30:28): Yeah, I think that that\'s part of the calculation. I think that also they probably just want to set a precedent that they\'re not going to release everything open source because they don\'t know how things are going to go. Yeah, I mean, they just don\'t know. Will the model end up being\... the most important way that we all interact with computers, you know, in a few years? Or will it just be kind of another layer and another tool? I think they don\'t know. I feel like Zuckerberg\'s intuition is that it\'s just going to be another tool. And so that\'s why he\'s inclined to open source.

**Nathan Lambert** (00:31:07): Yeah, this relates to the whole Apple thing. Like Apple is making these as features rather than products. Yeah. That does a lot of good for the narrative around AI, in my opinion, at least for things that I care about. It\'s like, this is what we\'re saying where AI is about a system and not just a model. The Apple\'s model doesn\'t matter to people, but it is enabling these products and systems or these things on their products to just be better. It\'s always Apple and Meta together. They are always forcing their way into whatever the next thing is going to be in technology.

**Dean W Ball** (00:31:44): Vibes policy or whatever. Yeah and it\'s funny because they hate each other. Yeah yeah but it\'s so funny but yeah i don\'t think they\'re going to uh that that\'s my just my personal intuition and i think that\'s like i think we\'re going to see a lot of people um not just in the language model space but elsewhere kind of do this this dual approach where they can they realize how much political cred you can get by open sourcing things. It\'s still happening.

**Nathan Lambert** (00:32:12): Google today, when we\'re recording, released Gemma V2. And their 27 billion parameter model is just a little bit below Lama 370B. I think that\'s a nerdy thing. But when the first Gemma model was released, it wasn\'t used as much by the community, mostly because there was a lot of minor bugs in the implementations in popular tools. So I think the initial feedback loop wasn\'t caught on. So it\'ll be really interesting to see if these second generation models, which are in the same ballpark as what Meta released, there\'s some strange things. They trained the biggest model on 12 billion tokens, and then the 9B model only on 9 billion tokens, and the 2B model on 2 billion tokens. So the models that have more reach by being smaller are like intense\... There\'s got to be a reason, but I think they were like scaling runs preparing for the biggest one, but they didn\'t finish training them. So like the models that the most people could use relatively are worse than the bigger ones just by the amount of compute that they put into them.

So I think eventually if there\'s decent uptake of these, Google will change this. But it\'s like the Gemma 2, whatever it is, 9B model, it\'s going to be way worse than the Lama 2 8B, just because Lama is trained on twice as many tokens. But like Google could have resolved this. So that\'s my like kind of, that\'s an aside. But these dynamics actually feed into what we\'re talking about, which is like Google, Microsoft, Beta are all still releasing these models.

(00:33:42): Yeah.

**Nathan Lambert** (00:33:42): Which is good. I have on this outline like the general state of open versus closed. It seems like we haven\'t had major updates in a while. It seems like there\'s much less pressure taking on open. I think maybe people are okay with the steady state that we\'re in. I don\'t know if this Nemotron 340B changes that much.

**Dean W Ball** (00:34:01): I don\'t think so. So I think that there are the people who believe that open source models are an existential risk to the world. And they continue to mostly think that, and they continue to support policies that either in absolute terms or on the margin would diminish open source. I think that DC has had a really radical shift in the last year because the climate towards open source models in the policymaking world a year ago was not good. And now it is much more\... Oh, well, we think this is really important for competition and we think it\'s important for innovation and we actually like want to make sure we have a really healthy open source community and all these kinds of, I mean, I\'m sure you\'ve seen, you know, Lena Kahn, no friend of the technology industry. Um, has she had a comment on this?

**Nathan Lambert** (00:35:09): Um, that\'s good. Did you see her clip on hard fork where she was asked what her PD is?

**Dean W Ball** (00:35:14): Yes. Yes.

**Nathan Lambert** (00:35:15): Oh, my God. If people haven\'t seen this, you\'ve got to go find it. It is so funny.

**Dean W Ball** (00:35:18): Yeah. And the sense I get from like talking to people in Congress and whatnot is that like the staff, congressional staff, is that -- People have just realized like open source is really popular and it would be really hard to go after. The government figures this, this isn\'t new. The government figures this out like every 15 years. They get like really freaked out about something in open source software. And then they\... It\'s a good way to put it. They go and like they try to ban it and then they realize like, oh, wait a minute, this would be really hard. This would piss a lot of people off.

**Nathan Lambert** (00:35:56): It\'d be a giant economic own goal. I think it\'s inevitable that it\'s an economic own goal. I mean, China is ready to take this over as beating the lead. They\'re right there. They don\'t have the ecosystem. The ecosystem is landing in the U.S., but they have perfectly good models. So if U.S. were to own goal and the U.S. stops building the models, I think that that is the path by which they could then own a ecosystem. Because there\'s not incentive to recreate the ecosystem when the ecosystem and the models exist in the US. But if these kind of tools and hosting all go away, then it\'s when other people take over.

**Dean W Ball** (00:36:29): Well, it seems like, I mean, as a bit of a question for you, I guess, but like, it seems like the Chinese, like, you know, the export controls on compute are going to start to really affect them. Because they were able to buy H100s.

**Nathan Lambert** (00:36:44): Yeah, this is what I was going to ask about. Isn\'t it that like a lot of NVIDIA\'s recent sales have been just them\... prioritizing selling to China because they\'re not yet blocked. And then that creates a backlog in the US because Nvidia is like, well, they\'re not going to be able to buy them, so we should get our revenue while we can. It kind of checks out. I don\'t have a source on it, though.

**Dean W Ball** (00:37:04): Since I\'ve always gotten\... It\'s all through subsidiaries. Yeah. So Chinese companies saw the writing on the wall about export controls like two and a half years ago. And so they started to buy up A100s and H100s at that time. And then the export controls came through and things are leaky and NVIDIA had that chip. They were selling a chip that was like basically an A100 and basically an H100 for a year. And then that got blocked by the federal government. So like\...

**Nathan Lambert** (00:37:37): Should we put Zuckerberg in charge of NVIDIA? Because I feel like for all the haters of Mark, Mark is pretty American and kind of follows it up, I feel like. He doesn\'t really care that Facebook is blocked in China. I feel like it\'s almost\... I feel like this is why public companies sometimes have problems because they\'re too incentivized. Like Nvidia\'s stock, if they were to have to stop selling to China immediately, would get such a haircut. So literally their hands are tied to doing this thing, which I think is like going against what the executive policy is in such a clear way. It\'s like what they\'re trying to do. Which I\'m like, this is a market failure. I was like, I don\'t think, like, I feel like Jensen\'s probably like, I don\'t, I guess he\'s pro-US. I don\'t know. Like, I don\'t care whether or not they\'re a hawk. It\'s just like, feels bad to go so clearly against what the intentions of the executive policy are, when there is a clear reason they\'re doing this.

**Dean W Ball** (00:38:31): Yeah. Yeah. No, I mean, I think that Jensen is going to comply with the letter of the law, but that philosophically he doesn\'t feel like it\'s his responsibility or good for him to be policing who his end users are. I think that\'s just how he feels.

**Nathan Lambert** (00:38:47): That\'s another discussion. I think there\'s\... It\'s a discussion that I\'ve been trying to figure out. I think like Ben Thompson famously has these diagrams for like\... where moderation can occur in the stack. And then figuring out what the mirror for where AI is in the stack, like whether or not it is just a product or if it seeps down to being like the AWS layer where like open AI\'s models are so fundamental to our computing infrastructure that them moderating at all and them deciding who they sell to is like extremely unclear. And I think it might be going in that direction.

**Dean W Ball** (00:39:20): It feels that way. But it does increasingly feel to me like\... You know, the Chinese might not be able to keep up on foundation model training because they\'re not going to be able to string together 100,000 B100s in a year.

**Nathan Lambert** (00:39:32): They have more electricity, which seems to be what people are talking about is the limitation.

**Dean W Ball** (00:39:37): They just won\'t have the compute, though. And we\'ll figure out. The U.S., I think, will figure out the electricity. I mean, I don\'t think we\'re going to be building 100 gigawatt data centers, but we\'ll figure out the electricity for the next couple of years, I think. But the Chinese will be able to distill the models and right. And like release them as, as open weight.

**Nathan Lambert** (00:39:59): Like, I mean, this is what the leading labs are doing anyways. I think this is, um, all of Google open AI and anthropic have now released models below their biggest size that are better than their biggest available models because it is cost effective and like the performance is really good. So like, they\'re not even pushing the frontier of the model size to the users. There probably are other infrastructure reasons for this, but like, That sort of thing is something that China could also do. They\'re going to need distilling our models into their models and stuff like this. I think this kind of leads into my next question. I was wondering if in your circles, this idea of synthetic data and various license clauses on whether or not you can train on outputs and models is something that is discussed. I think in the open fine tuning community, keeping track of licenses and how you comply with them on these various models is really really crucial so like with llama 3 you\'re technically not allowed to train use the outputs of the model to train any model other than llama 3 models which is like this kind of headache and then a lot of nvidia\'s push with nemotron is like look go wild I\'ve learned that a lot of these clauses on training on outputs come from the data providers trying to protect their business models. So it\'s like these companies want the models to be pretty open, maybe not meta, but like some of the smaller ones. But then like the data providers are like, you can\'t do this and they don\'t have enough power to do this. Like are these types of this is a very like in the weeds technical discussion. But is this synthetic data or clauses on models discussed in your area of the world?

**Dean W Ball** (00:41:30): So like in the policymaking circles, people are just coming around to the idea that synthetic data is even a thing. And I think a lot of people in DC don\'t understand that there are licenses associated with open source software.

**Nathan Lambert** (00:41:45): Well, the licenses with the models don\'t really make sense. We\'re in this position where I\'ve generated some data with these models so you can\'t trade on the outputs. But it\'s written as if it complies to you as the user. So you\'re agreeing to their community agreement to use the model. But if I create a data set and then upload it without training on it, can\'t somebody else just take the data set and train on it? Because they didn\'t say they agreed to this terms of use of the model. And it\'s like, this makes no sense. I need to go to our legal department and be like, this is what they\'re saying, right? I\'m like, I don\'t understand. And so it\'s just like this weird ecosystem of middle ground messiness, which is it feels similar to some of the open versus closed stuff. And we\'re kind of going into this peak of this discussion, I think, especially as people get to know better that these new Claude 3.5 bottles is just distillation. It\'s based on some form of synthetic like data.

**Dean W Ball** (00:42:36): Yeah. I mean, with a clause like that, too, in a contract, like you got to wonder about enforceability even under the best of circumstances.

**Nathan Lambert** (00:42:45): Yeah.

**Dean W Ball** (00:42:45): How would they know? How would they prove in court? How would they prove that like your this synthetic data set came from their model? Maybe they could prove that, but I don\'t know. A lot of models claim that they\'re open AI models, whether or not they are.

**Nathan Lambert** (00:43:04): It\'s really funny. Yeah, a lot of it is like if you\... Well, this is a technical issue with open models. A lot of people spin up demos with open models, but a lot of the ways that the models know who they are is by using a system prompt. And if you just spin up an open model, you\'re going to say that you\'re\... a model is whatever you are trained on the most of. So like, but like people don\'t normally write the system prompt. That\'s like, you are blank, blah, blah, blah. Like we, like we need to do that for like our models and we\'re like relatively serious actors. So it\'s like definitely just like open models will always be messier with this because the closed models do a lot more just serving it as a product in a polished way. Yeah. Yeah.

**Nathan Lambert** (00:43:43): Another quick question related, we mentioned Anthropic. With this Claude 3.5 Sonnet model that just came out, they\'ve said in a tweet that they got clearance from the UK AI Safety Institute. This is from Michael Salido, who I think I\'ve met at a various government discussion. He\'s like, excited to release this top performing model. In addition to our internal pre-deployment testing, we also\... We were also pleased to work with the UK AI Safety Institute. Is this just political gesturing? What is going on?

**Dean W Ball** (00:44:18): I think that it\'s political gesturing. I don\'t love it. I don\'t think that we should normalize the whole pre-deployment testing thing because that\'s just fundamentally incompatible with the way that software is made. But like, yeah, I suspect that it\'s political. I think that these companies, none of them are particularly reliable narrators. Like\... Like DeepMind is going through an org. Was DeepMind a part of Google when the AI Safety Summit happened? I think maybe that reorg was happening. OpenAI, we all know, is like a fairly dramatic company.

**Nathan Lambert** (00:45:04): I need to come up with the right nonlinear dynamics analogy. They\'re in like an unstable, like homophobic cycle or something. There\'s these things that are like in nonlinear dynamics where they stay in a cycle, but if they\'re perturbed, they end up in another cycle. It\'s like the Lorenz attractor is like the classical, truly chaotic one that oscillates between them. But it\'s kind of like that because they don\'t even need an external disturbance. They don\'t even need an input. They\'re going to go into some other unstable equilibrium for a while and then go to another one. But nonlinear dynamics is just a great field because the math is simple, but the analogies are really good.

**Dean W Ball** (00:45:41): So I even think I even think anthropic is that way, too, to be honest, like I and they\'re not like they\'re the most stable of the three,

**Nathan Lambert** (00:45:50): but I think their cultural cultural density is still higher.

**Dean W Ball** (00:45:53): Yeah, I mean, I think that they have a very clear mission, and that is really helpful.

**Nathan Lambert** (00:45:59): I don\'t know if they\'re achieving it. Their whole line about, okay, I\'m close with a lot of people there, but I don\'t believe that their line of that they\'re not contributing to the race is true. I think they need to reframe that and figure out how to\... combine this with their culture. I think it\'s true that normal people don\'t know that Anthropic exists, which might mean that in a normal person world, they\'re not contributing to some race, but they are in dynamics with OpenAI and Google that substantially are adding pressure to the pace of AI progress.

**Dean W Ball** (00:46:31): Claude\'s been my go-to daily model for the last four months. It\'s good. Since Cloud 3 came out. But yeah, I mean, I also think that they\'ve committed to doing models every couple months too, right? Like that\'s a pretty rapid cadence, substantially faster than open AI. So yeah, if anything, they\'re accelerating the current dynamics. And, you know, but\... think that the whole you know as uk ai safety institute i think that a commitment was made during a very heated moment uh kind of the peak i think fall of 2023 was sort of the peak of the ai doom rhetoric was this before or after the sam altman stuff i think it was before before it was before it the the the ai i talked to

**Nathan Lambert** (00:47:16): people who were at that event and they were like this shit is weird. They\'re like, why am I on the stage with all of these like billionaires and famous politicians? And they\'re all like, what is going on here?

**Dean W Ball** (00:47:27): Yeah. Well, I mean, it was just so incoherent back then. It was, you know, because it was the Biden executive order and the AI safety summit were all like in about a week from one another, as I recall. It\'s like all this stuff happened. And I think they made those commitments, and I think we will see all these companies gradually try to unwind themselves from those commitments over time. Or what will happen, this will be very consistent with the way that software gets regulated, especially to use software. The big companies will do these pre-deployment tests, and there\'ll be open providers who don\'t. And the best way to, like, it doesn\'t have to resolve itself in a rational way. That\'s something that\'s always important to remember about public policy. It\'s like, there\'s absolutely no need for it to be rational, you know, like make sense.

**Nathan Lambert** (00:48:19): Yeah, that makes sense. I think the other thing, this is all like the AGI lab things. It\'s like, what is your take on the scaling curves? I think for context, everyone got restarted on this with the Leopold Aschenbrenner situational awareness thing, which obviously is a well-written document, whether or not you agree. I think it\'s interesting. i\'m struggling with this one point of the scaling curves thing where i get mixed messages on what the scaling curves actually are when they come to evaluations my understanding of them is that the when you have log x-axis compute and then like log perplex it\'s an even log perplexity it\'s a straight line and what i interpret is this is as you 10x compute you get like a like a like it\'s not like a 10x encryption and performance you get 10 times closer to 100 which is like if you\'re at 90 accuracy to go to 99 so I don\'t really understand how people think that this is going to make them become a PhD level, whatever, blah, blah, blah. And I was listening to a recent podcast and I think it was Josh A. from InView was describing this as the reason you have emergent properties is that when you\'re training at every 10x compute, your model gets 10 times better. So then if you\'re measuring on a linear scale, it\'ll look like an emergent property because it\'s going to go like this. And I was like, what is going on like why does no one understand these fundamentals and it seems impossible that you could get 10 times better when you\'re going on like it seems like that just seems like total kool-aid drinking like am i am i wrong i i guess i need to go do this basic math it just doesn\'t track like any computer system how are you going to get 10 like what i don\'t understand well that\'s that\'s kind of my rant

**Dean W Ball** (00:50:07): I read these charts the same way. Log, log, perplexity, compute, right? That is what I read too. And so that would imply asymptotic progress, but it would not imply a continued exponential increase in capability. I also think like\... What is better? That\'s always like so hard. It\'s like, what is 10 times? People say, oh, well, the leap from GPT-5, you know, from GPT-4 to GPT-5, will it be similar or less or bigger than the leap from GPT-3 to GPT-4? I\'m like, I don\'t really know if I can quite quantify what the leap between 3 and 4 was or the leap between 4 and Opus, Cloud 3 Opus, which was definitely real for me. You know, I like that that model felt qualitatively different. But I don\'t think that has to do with training compute. I really I don\'t think that has to do with the number of parameters the model has. I think that has to do with the way anthropic that the post-training more than anything else. So, yeah, I\'m really not sure. I\'m skeptical of when it comes to the, you know, to the scaling laws. They\'re obviously very important. They\'ve held in a variety of different modalities, which is interesting. The fact that we see them apply in DNA sequencing or give sequence prediction to is like, oh, that\'s interesting. We\'re just sealing that same line. The models improve monotonically with scale over and over and over again. Um, so like, sure. I\'m, I\'m, I\'m inclined to believe that,

**Nathan Lambert** (00:51:52): but they\'re important, but I just am so shocked by how bad the discussion of them so often is like putting this, this is the thing with like the putting levels on the Y axis corresponding to human education. Dumb. Bad move. The technical reality of it may be that they continue to improve, but it\'s just like, those are the things that I want to see people stop doing. And this isn\'t really a question. This is mostly just me ranting about this because this impacts policy and these related discussions.

**Dean W Ball** (00:52:19): if I wrote an essay and like in college and submitted it to my professor, like Leopold Aschenbrenner.

**Nathan Lambert** (00:52:27): Wait, who was the famous economist that he was like Tyler Cowen is Tyler. Tyler, you didn\'t check his work.

**Dean W Ball** (00:52:35): Uh, yeah. Tyler, uh, basically hired me too. Uh, in fact, um, but, um, But yeah, if you did that and you didn\'t define intelligence, that would be the first thing a college professor would do is circle the first paragraph and be like, you need to define intelligence here. And the fact that he doesn\'t, I don\'t think it\'s a two-dimensional thing. or one dimensional or two dimensional thing. I think intelligence is inherently highly multidimensional, um, and multidimensional things just behave in, in counterintuitive ways. So like,

**Nathan Lambert** (00:53:08): I think they\'re getting better at things they\'re already doing, but we don\'t have any proof that they\'re going to start doing new things.

**Dean W Ball** (00:53:15): Yeah. Is GPT-4 better than a high schooler at some things? Yes. Is it worse than a three-year-old at some things? Yes. Those things are all true. And I don\'t really think it belongs on a human-defined linear scale of intelligence. I just inherently don\'t think that.

**Nathan Lambert** (00:53:31): Yeah. That makes sense. Final question. How much of influencing policy and related discussions comes down to having some sort of audience? I think that this is like

**Dean W Ball** (00:53:42): remarkably true but not potentially good yeah i think that it is very important and i think that it comes from influencing the way people think you know like a lot of think tanks will judge the success of research by did the ideas from this research get implemented in policy, which is one way to do it, for sure.

**Nathan Lambert** (00:54:08): But I think\... It\'s a long timescale. It\'s like a longer timescale than citations in academic nonsense.

**Dean W Ball** (00:54:14): Well, and also, if I\'m successful as a policy scholar, then at least once a month, I should be putting out something, some analogy, some way of thinking about something, a meme, really, basically, that has an effect on the way a lot of influential people think. The other big outstanding question for me, and I\'ve heard you raise this on the retort before recently, in fact, is what\'s more important? Is it influencing people in the federal government or is it influencing people at the AI labs? Who\'s going to be more important for determining policy? I don\'t know.

**Nathan Lambert** (00:54:55): Yeah. Well. Maybe some people at AI read this and I think this is a great conversation. I\'m kind of happy to wrap up here. I could see us redoing this in months based on the kind of coverage of all the recent things here. So I think this is great. I\'m excited to share this with people. It\'s nice to get to know you more. We already have another project lined up where we\'ll talk more about this. It won\'t be in the same medium. So that\'s fun. So thanks a lot and keep writing. I\'m sure you\'ll get a bunch of people to check this out. I\'ll have all the links everywhere and stuff like that.

**Dean W Ball** (00:55:28): Awesome. But you too, thank you very much. You played a big role in my building my Substack audience over the last six months. So I really appreciate it.

**Nathan Lambert** (00:55:35): People just need to say things. People ask me this a lot. It\'s really like if you make time, most people that I work with have interesting thoughts. The problem is. doing the practice of getting these thoughts into some silly medium. Literally, these long tweets, the tweets are now long. You could just do that. You could do that once a week. You will grow an audience over time. It\'s pretty simple. You just have to pick your lane and just keep pressing the button and it just works. You\'re not the only one. I\'m going to have some other people that have talked about this on this interview track in the summer. I just think it\'s so\... it\'s a partially a way to normalize it and get more people to try it is why I bring it up because that\'s like, I want that to happen to AI too. Cause there\'s a lot of smart people that don\'t know how to engage and a hundred percent and other things. And it\'s like, yeah, it\'s worth it. So thanks again.

**Dean W Ball** (00:56:27): We\'ll talk to you. All right. Bye.
