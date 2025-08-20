---
title: "LLM agents and integration dead-ends"
subtitle: "When is GPT4 going to schedule my meetings? What is stopping it?"
date: 2023-07-12
type: newsletter
audience: everyone
visibility: public
post_id: 133476495.llm-agents-integration
email_sent_at: 2023-07-12T14:00:35.235Z
---
##### Thank you for reading and for your support of Interconnects, consider upgrading to paid, if you can, for access to all my work.

<div>

------------------------------------------------------------------------

</div>

The practical blocker of deploying ChatGPT for most immediate business writing is the resulting copying of data back and forth into the interface. Bringing this barrier down to enable direct integration of generative AI is the biggest immediate roadblock in generative AI unlocking huge economic value (yes, the [\>\$ 4 trillion per year of ](https://www.fastcompany.com/90919913/pov-ai-corporate-profits-4-trillion-research)*[profits](https://www.fastcompany.com/90919913/pov-ai-corporate-profits-4-trillion-research)*[ that McKinsey forecasted](https://www.fastcompany.com/90919913/pov-ai-corporate-profits-4-trillion-research) across only 63 use cases). Curiously, it seems like there is currently an appetite for these speculative integrations at a level that most AI experts would never have dreamed of in 2022. Normally it\'s impossible to get a chief information officer to connect an unproven third-party tool to your application. These experiments and unlocking this potential come with extreme business security risks, pointing to what I expect to be the central issue in adoption: robust integration.

As there isn\'t time to figure out which specific applications are the right few for them, tons of people are moving to figure out how everyone can use large language models (LLMs) for their business across many contexts and tools. In most cases, these are marketed as LLM agents. The word *agent* is adopted from the taxonomy of reinforcement learning (RL), likely only because RLHF also came into the forefront, to mean something that takes action in the environment after taking in some state data. This state-to-action pipeline is all about feedback.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

LLM agents posit that if you set up your computing infrastructure and tokenization correctly, language models will just learn to complete almost every task we do on our computers. A basic one that\'s been in the literature for a while is [retrieval-augmented generation](https://arxiv.org/abs/2005.11401) (RAG), which adds additional non-parametric contexts to the base model generation. An advanced task for LLM agents is simulating keyboard strokes to navigate the internet. The goal is to have a program that can do everything in the scope of web-connected computers: from translating a text command into an Excel function for a plot to searching internal company data. The goalposts for LLM agents are so broad that that should start to worry you --- normally things that scope out a giant area don\'t work particularly great in the space they cover (at least for downstream technology like this).

There are already tons of players in this space, all with small stories of their own. Let\'s take a journey from most real to most speculative (and I\'m surely missing some, this list is illustrative, not complete):

-   **ChatGPT Plugins**: Every consumer loved the idea of this \-- let me plug in data from other apps I love into this useful chatbot. Supposedly this one died because the go-to-market strategy never landed. Turns out most brands don\'t trust LLMs enough to blindly toss data over the fence to OpenAI, and more importantly, receive tons of crazy requests from their language model. I\'m guessing the technology here actually worked pretty well. We\'ll see again and again how business realities will kill promising LLM ideas. The ones that will stick will be first-party to ChatGPT / OpenAI --- so I\'m pretty hopeful for [Code Interpreter](https://openai.com/blog/chatgpt-plugins#code-interpreter), figuring out code execution safely at scale is sick!

-   **LangChain**: This package is used for tons of demos, but tends to be pushed out of the stack by people trying the hardest to do something real in the space of LLM agents. In short, it lacks the reasons for people to more deeply integrate their stack with them, so folks look elsewhere. More on integration and the recent \"LangChain is useless\" posts are below.\
    \
    [Transformers Agents](https://huggingface.co/docs/transformers/transformers_agents) feels like LangChain lite, with some huge wins for being easier to use with HuggingFace tools.

-   **Adept AI** \[demo [here](https://www.adept.ai/blog/act-1)\]: This demo takes on a broad set of internet tasks, from scheduling to shopping. The blog post I link touts an \"action transformer\" without much more information. My guess is they\'ve started with something spun off of the Gato idea from DeepMind with a lot of application-specific tuning. I think this is promising, but a very general solution acting on my own computer is very scary.

-   **Lindy AI** \[demo [here](https://www.lindy.ai/blog/meet-lindy)\]: This demo is all about workspace productivity tasks. They don\'t give a lot of information about the actual technical stack when you compare it to Adept, but I like that it\'s a little more narrowly scoped when it comes to my primary personal concern of reliability.

Most of these companies are betting that they can build a general solution. Adept is the only different one in this approach, at least by marketing, where they\'re training one model to do everything and the others are building a tool in the belt for each use-case. Regardless of the technical solution, by being a well-known, general solution, everyone will start with them.

In reality, more specific solutions from application-focused companies will come up and be adopted first because they work, then it\'ll be increasingly hard to convert enterprise customers.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

On the other side of this conversation question is the last remaining players in this space:

-   **Google Bard\'s or Microsoft CoPilot\'s integration** within all of the enterprise stack. The reason they\'re last is because I don\'t expect them to get there soon, even if the opportunity is so gigantic and obvious. It would be so nice to plug some settings for when I like meetings in my calendar, give it an email, and say \"schedule a 30-minute call\".

In reality, it\'ll be a bloodbath where someone builds this tool because the Google Accounts programming interface is fairly open (and used by tons of applications we use every day), but then that tool will be one click away from getting killed by Google.

I\'ve never seen a technology that is so obviously ready to be tried, but also so obviously going to cause major issues. **LLM agents almost feel like the self-driving cars equivalent for a digital technology**. Every major large language model application release has seen wild side effects. What\'s the equivalent of a \"[My Night with Sydney](https://stratechery.com/2023/from-bing-to-sydney-search-as-distraction-sentient-ai/)\" when the agent has control over most of your personal life? When these things start getting used, I\'m going to be so happy to be an Apple user, where each application is effectively sandboxed, so it cannot read data from another without permission.

Who will jump first?

![natolambert\\\_a\\\_robot\\\_that\\\_is\\\_blasting\\\_a\\\_target\\\_with\\\_a\\\_stream\\\_of\\\_\\\_265aca5d-6953-42c6-9640-be5c4d105c4e.png](images/133476495.llm-agents-integration_c81e7bc0-ba33-4ec9-b539-eb490a7f6178.png)

As these models move into domains with more general actions than text, the cost of failures, or hallucinations, grows dramatically. The idea of *agents* is extremely popular these days with LLMs. From LangChain to Transformers Agents to a bunch of startups --- I view all of these as toy examples that are limited by integration. If an LLM can send an email for you or make purchases for you, you\'re putting two things most people hold dearest on the line: reputation and finances. Consumers like to try fun things, but businesses are much less inclined.

### Integration barriers: security

I\'m extremely torn on who will win out in this space. On the one hand, I expect places like Adept and Lindy to have tools that work 80-90% of the time in a pretty compelling way. On the other hand, I know so many businesses will have a hard time being sold on the integration problem of many security challenges. There are the base challenges, such as how the company data is handled by a model provider (and how they need the data to improve their model). Then, there are the downstream issues, which are all of the ways this could go wrong: sending an email to the wrong person, breaking an internal tool, or turning off an existing product.

In this case, the product itself makes complete sense, but getting a foothold in the market is the challenge.

The advanced LLM agents seem to be acting in sorts of while-loops until they achieve their goal or result in an error. Running language models continually is currently a recipe for something interesting at least. There are so many ways for them to go wrong. This reminds me of all the people thinking RL-driven agents are going to be good at solving many tasks. When you give an RL agent access to many rewards and objectives, it normally just lacks robustness. The scope of actions and tasks in a state-space of the internet should be obviously concerning to anyone thinking about using this technology.

There are a few core features to making a functional user-facing LLM agent commercially viable. I think it comes down to:

-   The **need for trust and reliability** of the deployed solution. Does it make sense to have all action-based language models sampled with a temperature of 0 so they get more deterministic behavior? This is [done for the new evaluation scheme MT-Bench](https://github.com/lm-sys/FastChat/blob/246c616bed970cec327d4fb16983e79906ee486f/fastchat/llm_judge/common.py#L160) and makes a lot of sense to me. The problem is that with such a broad state space, *exhaustive testing is virtually impossible*.

-   Management of **dramatic failure modes** when LLMs are given dramatic controlling access to an individual's social capital and data. Through this lens, we are shifting from anthropomorphization debates to physical failure modes. This changes so many specification questions and value judgments around the technology.

-   A deep understanding of the **feedback system with the model** --- how does this token stream remain stable? What are the actual dynamics at play? Essentially, I want to know if language models end up with human-like behavior. Do we need a separate internet API for all of our language models? They don\'t need the interface. Does this change how humans use the internet?

It\'s a fascinating research problem. It seems like enterprise customers roll out relatively little of this in the short term, and we keep copying text from our companies\' language model of choice.

There's likely going to emerge a deep difference in how these agent tools integrate if **they are behind a model API or used on top of a model**. If GPT-4 has access to a ton of plugins, and it knows your credentials, that information flow is set up. If an agent requires chaining local logic, it seems a lot messier. Both of these come with bigger technical problems that I do not have the answers for.

### The LangChain debacle

In general, the main criticism of LangChain I filtered out is code creep (too many wrappers) and suffers from a lack of customization / thorough performance. At the end of the day, it seems like people end up implementing their own code to get LangChain across the line for what it is designed to do in the first place.

From the [LangChain documentation](https://python.langchain.com/docs/get_started/introduction.html):

> **LangChain** is a framework for developing applications powered by language models. It enables applications that are:
>
> -   **Data-aware**: connect a language model to other sources of data
>
> -   **Agentic**: allow a language model to interact with its environment
>
> The main value props of LangChain are:
>
> 1.  **Components**: abstractions for working with language models, along with a collection of implementations for each abstraction. Components are modular and easy-to-use, whether you are using the rest of the LangChain framework or not
>
> 2.  **Off-the-shelf chains**: a structured assembly of components for accomplishing specific higher-level tasks
>
> Off-the-shelf chains make it easy to get started. For more complex applications and nuanced use-cases, components make it easy to customize existing chains or build new ones.

This is the second integration dead-end: the wind range of tools, interfaces, and rules that any one of these models needs to navigate.

In case you missed it, here is the recent LangChain criticism on [Hacker News](https://news.ycombinator.com/item?id=36645575) and [Reddit](https://old.reddit.com/r/LangChain/comments/13fcw36/langchain_is_pointless/). The top comment is about the integration barrier:

> Each feature requires very custom handwritten prompts. Each step in the chain requires handwritten prompts. The input data has to be formatted a very specific way to generate good outputs for that feature/chain step. The part around setting up a DAG orchestration to run these chains is like 5% of the work. 95% is really just in the prompt tuning and data serialization formats.

Most of these popular ML repositories that we saw beat all sorts of star records are significant for demonstration purposes, but woeful for building economic value. This should be an opportunity to showcase what needs to be made in order to enable LLM applications. There is a huge opportunity to build these wrappers for people: how to connect language models from OpenAI to their data lakes at Databricks. This tool, done right, will also then let you seamlessly swap out an OpenAI model for an open-source model hosted on Inference Endpoints from HuggingFace.

LangChain still has an opportunity to pull this off, as they raised some money and are generally known for doing this. In reality, it seems likely that a different design philosophy will be needed for the enterprise angle rather than open-source demos. In a few years, we will have an EnterpriseChain, it may just be limited in scope.

<div>

------------------------------------------------------------------------

</div>

For more on LLM agents, see my follow up:

::: {.digest-post-embed attrs="{\"nodeId\":\"6cabf9b6-1d10-4602-bf64-8e25a5207c38\",\"caption\":\"This article heavily follows Wednesday's post on LLM Agents. Again, more than two-thirds of this post is free, just with a conclusion under the paywall. At some point, people will get a grip on how large language models (LLMs) interact with users and environments to generate new data. We are very far from that case. Right now, some feedback systems exist using large language models (LLMs), but the data flow and understanding are extremely lacking. The information flow primarily is tailored by people controlling behavior via prompts and other interconnects of LLMs with data sources (e.g. search engines or vector databases) not an understanding of feedback.\",\"cta\":null,\"showBylines\":true,\"size\":\"lg\",\"isEditorNode\":true,\"title\":\"LLM agents follow-up: exploration, RLHF, and more\",\"publishedBylines\":[{\"id\":10472909,\"name\":\"Nathan Lambert\",\"bio\":\"ML scientist at Huggingface (RL, RLHF, society, robotics), athlete, yogi, chef. Writes about ML & society.\\nPhD from Berkeley AI, Cornell Lightweight Rowing `17\",\"photo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdda47b96-836a-4b95-99a0-f0ec744d4245_2316x2316.jpeg\",\"is_guest\":false,\"bestseller_tier\":null}],\"post_date\":\"2023-07-14T14:01:39.595Z\",\"cover_image\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4bac1b30-2df9-4ea5-9973-68c127b3a47d_1024x1024.png\",\"cover_image_alt\":null,\"canonical_url\":\"https://www.interconnects.ai/p/llm-agents-exploration-and-rlhf\",\"section_name\":null,\"video_upload_id\":null,\"id\":134766948,\"type\":\"newsletter\",\"reaction_count\":6,\"comment_count\":0,\"publication_name\":\"Interconnects\",\"publication_logo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe70f9dbf-4fe6-404c-b6bb-1831d1b7ed0b_590x590.png\",\"belowTheFold\":true}"}
:::

<div>

------------------------------------------------------------------------

</div>

Extras:

-   If you're going to ICML, let me know! Happy to chat.

-   I'm \@natolambert on every platform \[[bsky](https://bsky.app/profile/natolambert.bsky.social), [Threads](https://www.threads.net/@natolambert)\]. If there is any platform I expect to "win" with or after Twitter, it's Threads. Having been on all of them early, it's the first one that clearly feels ready for the light of day.

-   I'm glad that autonomous vehicles are going to exist, but, [oh man, am I glad to not work with them](https://twitter.com/DavidZipper/status/1676968755522588682).

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
It\'s funny because these LLM agents are totally disconnected from RLHF.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
This may be what Lindy is actually doing, a more narrow play.
:::
::::
