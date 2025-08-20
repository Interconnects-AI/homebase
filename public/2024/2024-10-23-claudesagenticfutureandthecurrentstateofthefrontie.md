---
title: "Claude's agentic future and the current state of the frontier models"
subtitle: "How Claude's computer use works. Where OpenAI, Anthropic, and Google all have a lead on eachother."
date: 2024-10-23
type: newsletter
audience: everyone
visibility: public
post_id: 150585666.claudes-agency
email_sent_at: 2024-10-23T12:01:54.640Z
---
*Voiceover coming later today to [your podcast players](https://www.interconnects.ai/podcast).\
Edit 10/23: Added more support for claim that Flash is the best small model.*

Anthropic just [released their latest mainstream model](https://www.anthropic.com/news/3-5-models-and-computer-use), Claude 3.5 Sonnet New, to advance their lead for general-use chat models --- the models that people use for coding and other high-value, conversational tasks. The benchmarks are impressive, as usual, and the day before release multiple people had already [noticed](https://x.com/Tim_Dettmers/status/1848755366953422856) that "[Claude](https://www.reddit.com/r/ClaudeAI/comments/1g9a14g/claude_sonnet_35_got_stealth_buffed_much_faster/) seems [better](https://www.reddit.com/r/ClaudeAI/comments/1g94a2v/did_claude_just_get_a_super_boost/)." The benchmarks are below:

![](images/150585666.claudes-agency_5d2e63ff-ac9f-4f8e-9749-9ef2b9b25b6c.png)

Here's the equivalent chart when they [announced the original Claude 3.5 Sonnet in June](https://www.anthropic.com/news/claude-3-5-sonnet). The focus today is on a better all-around model, one that works with images and one that works on agentic tasks.

![](images/150585666.claudes-agency_4bccbd4d-f1c8-4a38-a474-69a3df8a4448.png)

We don't have the tools to truly measure this --- as Anthropic's models usually underperform the expectations of the super users in [ChatBotArena due to the use cases there being hard to specify](https://www.interconnects.ai/p/gpt-4o-mini-changed-chatbotarena?utm_source=publication-search). Uniform bumps on benchmarks will usually be felt --- we've been seeing this for years.

At the same time, Anthropic *announced* the scores for their forthcoming Claude 3.5 Haiku model (the smallest one) and introduced an [exciting new Claude Computer Use Beta](https://www.youtube.com/watch?v=ODaHJzOyVCQ). Claude Computer Use is more of an exploration of *how we use these models*, rather than *who's winning the model competition*. It will take a long time to fully unpack what this new API can do.

The Claude Computer Use demo is exactly the type of agent we've been expecting to see for years. It is immediately intuitive and functional enough to see a clear path forward. It's another "aha" moment just like using AirPods, ChatGPT, etc. for the first time.

The model works by taking screenshots, sending them to the Claude Vision API, and getting actions back in line with the usual text. It stores a fixed number of images in history to mitigate some exploding costs, but it definitely feels slow.

I immediately tried to use this for basic web tasks. My first task was "Help me send an email to Nathan Lambert, the AI researcher."

::: {.native-video-embed attrs="{\"mediaUploadId\":\"24a94c15-25d6-44b8-9b0f-dd03e0b13f63\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

As you can see in the video, the model realized only *after* a bunch of turns that it could not fulfill this request due to its system prompt. I expect we'll see much more basic headaches in systems like this before we're really using them as easily as we are using ChatGPT. ChatGPT definitely felt more intuitive to use at the start, but the ceiling on this feels far higher.

The next thing I tried was a basic web navigation task that required repetitive actions --- finding the first article I published on [interconnects.ai](http://interconnects.ai). The model tried a bunch of times, using a somewhat inefficient key method, and eventually ran into API errors.

::: {.native-video-embed attrs="{\"mediaUploadId\":\"a9dc84c1-b3b6-411f-a2bb-231c08001af7\",\"duration\":null}" component-name="VideoPlaceholder"}
:::

The API errors, I've [learned](https://x.com/nearcyan/status/1848875226043703762) are from rate limits. Sending 10 photos in the history per action quickly will blow through rate limits without a high spend Claude API account.

I recommend you to watch the Anthropic demo and make your own conclusions. Claude is providing reasoning and taking actions via clicking and keyboard inputs on reasoning tasks.

:::::::: {#youtube2-vH2f7cjXjKI .youtube-wrap attrs="{\"videoId\":\"vH2f7cjXjKI\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=vH2f7cjXjKI){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

Seriously, if you're reading multiple blog posts and watching videos to get a sense of this new API, just give it a try. If your computer has Docker, all it takes to give it a spin is this short command from [Anthropic's documentation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo):

    export ANTHROPIC_API_KEY=%your_api_key%
    docker run \
        -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
        -v $HOME/.anthropic:/home/computeruse/.anthropic \
        -p 5900:5900 \
        -p 8501:8501 \
        -p 6080:6080 \
        -p 8080:8080 \
        -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest

In just a few minutes, with a few dollars spent, you'll immediately get why this is the future. It is likely not surprising to my audience, but it is relieving to finally have it in hand.

It's not clear strategically why Anthropic launched this --- I expect most labs to be capable of shipping something extremely similar, but it is welcome.

At the same time, it feels like Anthropic doesn't really want people using this in the real world with the amount of work and API credits that will be needed to build complete scaffolding around this --- their documentation only had quickstart tips for running in a virtual machine.

The biggest limitations reinforce the question marks I have for why this came from Anthropic and not Google or OpenAI, which feel far more invested in consumer habits. When trying to complete my first request, Claude refused with a standard annoyance:

> I apologize, but I cannot and should not send messages or emails on your behalf, even simple greetings. While I was able to find Nathan Lambert\'s contact information from his public website, it would not be appropriate for me to send messages to people. This is because:
>
> 1.  I should not impersonate or speak on behalf of others
>
> 2.  Sending unsolicited messages could be considered spam
>
> 3.  There are privacy and consent considerations when contacting individuals
>
> If you would like to contact Nathan Lambert, I encourage you to:
>
> 1.  Write and send the email yourself using your own email account
>
> 2.  Introduce yourself properly
>
> 3.  Explain the purpose of your communication
>
> I can help you find contact information and navigate websites, but the actual communication should come directly from you.

If AI is going to be truly unlocked and doing my work on my computer, it needs to be precisely personalized to the my level of risk. Local models and agents will make this far easier.

For more on Claude's Computer, you can also read [Ethan Mollick's](https://www.oneusefulthing.org/p/when-you-give-a-claude-a-mouse) or [Simon Willison's](https://simonwillison.net/2024/Oct/22/computer-use/) first takes.

<div>

------------------------------------------------------------------------

</div>

## The state of the frontier models

The state of play can be summarized by four factors.

### 1. Anthropic has the best model we are accustomed to using

The vast majority of people who work in AI and technology agree that you [should be using Claude instead of ChatGPT](https://www.interconnects.ai/p/switched-to-claude-from-chatgpt) if you use it for challenging tasks like coding. Still, [Anthropic's revenue numbers for Chatbot subscriptions lag far behind OpenAI's](https://x.com/tanayj/status/1841272069444845858).

As Anthropic continues to push this, they need to either create a 10x better model, which is unlikely, or build better ways to use their models, which they are trying to do. The only realistic way for Anthropic to overtake OpenAI today is by enabling new workflows that OpenAI's models cannot yet do, but are extremely useful.

### 2. Google has the best small & cheap model for building automation and basic AI engineering

Gemini Flash, especially when compared to the most recently announced Claude 3.5 Haiku, is very impressive. The Gemini model that is available today handily beats the model that Anthropic announced as *coming soon*. To take this further, [Google also offers a Flash-8B](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/), which is faster and cheaper than the likes of Claude Haiku and GPT-4o-mini. The frontier of free, abundant, and nearly instantaneous intelligence is where most applications are experimented with. Data transformation, logging, and monitoring with LLMs are underway, and Gemini is the place to start.

ChatBotArena is not the most important metric for smaller models. Much of the text written by these models is not used in direct consumer conversation, it is often used interweaved with other models. My reasoning mirrors [Artificial Analysis's three summary plots](https://artificialanalysis.ai/) --- here Flash is faster, smarter, and cheaper than its competitors.

![](images/150585666.claudes-agency_7cf03c6e-ae42-400c-b4cd-5244fe0e4c8b.png)

These small models are all built on a technique called knowledge distillation. [Google is the only frontier model lab to document it clearly](https://www.interconnects.ai/i/145870222/are-gemini-flash-and-claude-haiku-distilled). Distillation from a smarter model is far from a new idea, it is one of many [Hinton et al.](https://arxiv.org/abs/1503.02531) ideas still heavily impacting the direction of deep learning. When building small models like Flash and Haiku, the distillation loss, which explicitly takes the log probs from the bigger, teacher model, is used in pre- and post-training. This is opposed to the popular idea of "distilling" frontier models in post-training with high-quality data --- more on this soon.

Knowledge distillation from a teacher model is pervasive among leading AI players today, but it is not yet easy to track progress or best practices. Nvidia has recent papers on their [techniques for Minitron](https://arxiv.org/abs/2408.11796?utm_source=ainews&utm_medium=email&utm_campaign=ainews-nvidia-minitron-llm-pruning-and) and Google has documented some of its impacts in the [Gemma 2 report](https://www.notion.so/128a750def6d433ea1a75df4c9dd74b7?pvs=21), which is also distilled in this manner (but we don't know exactly from where or on what data):

> In particular, we focus our efforts on knowledge distillation (Hinton et al., 2015), which replaces the one-hot vector seen at each token with the distribution of potential next tokens computed from a large model. This approach is often used to reduce the training time of smaller models by giving them richer gradients. In this work, we instead train for large quantities of tokens with distillation in order to simulate training beyond the number of available tokens. Concretely, we use a large language model as a teacher to train small models, namely 9B and 2.6B models, on a quantity of tokens that is more than 50× the compute-optimal quantity predicted by the theory (Hoffmann et al., 2022). Along with the models trained with distillation, we also release a 27B model trained from scratch for this work.

Leading on this technology matters for Google and developers, but tends to not lead to flashy demonstrations and callouts on social media.

### 3. OpenAI has the best model for reasoning, but we don't know how to use it

[OpenAI's o1 system](https://www.interconnects.ai/p/reverse-engineering-openai-o1?utm_source=publication-search) is remarkably different than all the models people are using today for textual tasks. Still, so much in technology has conditioned users to expect responses to be fast, something that o1 is structurally opposed to. OpenAI needs to figure out the right way for the "I'm feeling lucky" of AI to be deployed.

In the meantime, the other leading labs are well underway on making a replication. We've seen time and time again that the top labs are mirroring each other's product offerings. They all have general and small models. Meta tried to match OpenAI's audio models before they released it. Google tried to scoop OpenAI's announced (but not released) video model. And so on.

Releasing a new type of model is an act of faith that people will be able to figure out how to use it and early access will accrue fundraising, talent, or a moat in users.

What will be more important in 2025, general models that are a bunch better and slot into ChatGPT, like Gemini 2 or Claude 4, or OpenAI's o2?

### 4. All of the laboratories have much larger models they're figuring out how to release (and use)

All of the AI world has been waiting for GPT-5 in 2024. Regardless of the exact label, we know that the frontier labs have larger models that they aren't rushing to get into users' hands. Google has teased the Gemini Ultra models since the [launch of Gemini in December of 2023](https://blog.google/technology/ai/google-gemini-ai/). Anthropic has their Claude Opus models trained but is late to release them.

These largest models are not shifting the needle as the performance improvements of serving them to users don't outweigh the literal costs in compute or increased latency. These larger models are being used to train better, smaller models. Claude 3.5 Opus almost certainly exists within Anthropic, but just for researchers to improve models like Haiku and Sonnet.

These large models are absolutely crucial for model post-training. Meta implicitly described this in their Llama 3 communications, where they describe [most of their instruction data coming from their biggest, best model](https://www.notion.so/Claude-s-computer-and-the-state-of-play-in-frontier-models-1270066c4bda8035bd02ccfc8ded1b71?pvs=21). The increased prevalence of RLHF entails using the lab's best models to generate more synthetic data and slowly push out the internal frontier. The performance gains are much bigger on the smaller models, which we're seeing in the likes of Haiku and Sonnet, but Opus exists and is crucial to this process.

The question is who blinks first and goes for the next major model version or size? Google has the most scale, for deploying, but also the most risk in existing shareholders and customers. OpenAI is in the middle with compute, but the highest risk tolerance, means they're likely to release first.

## Who wins?

Based on your views of the market, you should bet on which of these vectors is the most important.

In many ways, the strengths of the various models mirror their organizational cultures. Google has always been the master of scale, Anthropic is obsessed with the behavior of AI, and OpenAI is obsessed with the race for AGI (or they have been). What is left to be seen is what culture wins.

<div>

------------------------------------------------------------------------

</div>

**Housekeeping**

-   Audio of this post is available (soon) in [podcast](https://www.interconnects.ai/podcast) form (and sometimes on [YouTube](https://www.youtube.com/@interconnects)).

-   My casual podcast is at [retortai.com](http://retortai.com).

-   *Paid subscriber Discord access in email footer + header (or DM for link).*

-   Referrals → paid sub: Use the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   Student discounts in [About page](https://www.interconnects.ai/about).
