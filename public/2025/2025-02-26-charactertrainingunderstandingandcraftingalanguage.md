---
title: "Character training: Understanding and crafting a language model's personality"
subtitle: "Post-training in industry is very different than the academic papers and open-source models demonstrate. Let's dive into one of my favorite topics in language modeling development today."
date: 2025-02-26
type: newsletter
audience: everyone
visibility: public
post_id: 157355619.character-training
email_sent_at: 2025-02-26T13:03:32.498Z
---
The vast majority of evaluations used to measure progress on post-training at frontier laboratories are internal evaluations rather than the evaluations you hear about all the time like MATH or GPQA. These, the well-known intra-industry evaluations, are certainly important for ballparking behavior, but for every public evaluation, these frontier laboratories are likely to have 10+ fine-grained internal evaluations.

The internal evaluations these model providers have cover a range of topics. Surely, most of them are basic, repetitive user behaviors that they need to make sure a new model doesn't roll back too many of. Of these, the vast majority are likely skills, and "character" remains more of an art than a hill to climb up with careful data engineering.

Leading post-training laboratories surely know how to *reinforce* more robust behavior within a specific character, as seen by the march of progress on evaluations like ChatBotArena, but crafting a specific personality from scratch is an open question.

The primary goal of this post is to start the conversation outside of frontier AI labs around **character training**. Character training is the subset of post-training designed around crafting traits within the model in *the manner* of its response, rather than the content. Character training, while being important to the user experience within language model chatbots, is effectively non-existent on the web.

We don't know the trade-offs of what character training does, we don't know how exactly to study it, we don't know how much it can improve user preferences on ChatBotArena, and we should.

The *appearance* of the AIs people are using is deeply coupled with how intelligent users will find it to be. [Style of communication is crucial to how information is parsed](https://www.interconnects.ai/p/how-rlhf-works-2?utm_source=publication-search). This is likely a very high priority to industrial labs, but something that almost no academic literature exists on. Even though I want to do research on this, I'm honestly not sure how to do so yet other than a 1 of 1 technical report on findings.

## ChatGPT gets character depth

Out of nowhere on Saturday, February 15th, Sam Altman [tweeted](https://x.com/sama/status/1890816782836904000) about this new GPT-4o model that will serve as the foundation of ChatGPT.

![](images/157355619.character-training_1a6a0f50-6d10-45aa-8ba5-466f85056238.png)

This is the biggest subjective change I've ever felt within intermediate model versions, from any primary provider --- something more akin in vibes change to the shift from GPT-3.5 to GPT-4. The model immediately and consistently showed new behavior patterns. I found these very positive ([Karpathy agrees](https://x.com/karpathy/status/1891213379018400150)), but they'll take some getting used to.

Where ChatGPT used to sound robotic and shallow, it's now very clearly leaning into a chipper assistant demeanor. Yes, for basic tasks, this new default model in ChatGPT is very Claude 3.5-like --- more testing is needed to know if this GPT-4o with its peer models like o3-mini can dethrone Claude 3.7 Sonnet as a daily programming driver.

The biggest changes in the new GPT-4o model are:

-   It now loves to reference past interactions in the chat (way more obvious than any other provider has been) --- it was trying to flex that it knows my dog breed, mini schnauzer, or my book topic, RLHF. **This is very in line with the new roadmap to GPT-4.5 and GPT-5 that Altman [posted](https://x.com/sama/status/1889755723078443244?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet), where ChatGPT is designed around a fluid experience rather than standalone, siloed, powerful models.**

-   The model is very chipper, sprinkles in more emojis, and is almost funny.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   The multi-turn conversation is more dynamic, with follow-up questions and added texture to longer back and forths.

The reasons are at a high level very complementary to those I listed when I switched to Claude as my daily driver model.

::: {.digest-post-embed attrs="{\"nodeId\":\"d1162d81-39b5-46f9-b6c7-cba9d740fc1d\",\"caption\":\"Audio version available here.\",\"cta\":null,\"showBylines\":true,\"size\":\"sm\",\"isEditorNode\":true,\"title\":\"Switched to Claude 3.5\",\"publishedBylines\":[{\"id\":10472909,\"name\":\"Nathan Lambert\",\"bio\":\"ML researcher making sense of AI research, products, and the uncertain technological future. PhD from Berkeley AI. Experience at Meta, DeepMind, HuggingFace.\",\"photo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fedcdfb-e137-4f6a-9089-a46add6c6242_500x500.jpeg\",\"is_guest\":false,\"bestseller_tier\":100}],\"post_date\":\"2024-07-03T15:54:27.950Z\",\"cover_image\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8b10dbd6-2ee7-4cab-bdc8-fcf9782bba30_3680x2382.png\",\"cover_image_alt\":null,\"canonical_url\":\"https://www.interconnects.ai/p/switched-to-claude-from-chatgpt\",\"section_name\":null,\"video_upload_id\":null,\"id\":146249945,\"type\":\"newsletter\",\"reaction_count\":47,\"comment_count\":0,\"publication_name\":\"Interconnects\",\"publication_logo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe70f9dbf-4fe6-404c-b6bb-1831d1b7ed0b_590x590.png\",\"belowTheFold\":true}"}
:::

The shocking part of this is that the impact of this sweeping change is almost entirely undocumented. Yes, OpenAI updated the [Model Spec](https://openai.com/index/sharing-the-latest-model-spec/) (my previous coverage [here](https://www.interconnects.ai/p/openai-rlhf-model-spec?utm_source=publication-search) and [here](https://www.interconnects.ai/p/a-post-training-approach-to-ai-regulation?utm_source=publication-search))[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}, but that doesn't really capture how *this* model is different --- it just clarifies the direction OpenAI is optimizing for. There are a few overlapping interpretations of this lack of transparency:

-   OpenAI cannot precisely measure the differences as a few specific behavior traits, so they can only see the model performs better in high-level testing like ChatBotArena or other A/B testing, but they cannot capture the changes in score deltas between a few evaluations they could release.

-   AI is moving so fast that taking the time to document these models is not worth it,

-   Detailing the changes will make the character too easy to reproduce and will be another path of "distillation" of OpenAI's models.

The community of model users is extremely far from having clear ways to measure these differences. While there are vibe tests on Twitter, they will not be conclusive. [ChatBotArena](https://www.interconnects.ai/p/chatbotarena-the-future-of-llm-evaluation) won't even come close to measuring the levels of these differences (and in the case of referencing past chats, it cannot). Character training is the sort of addition to a post-training stack that takes industrial training techniques from being reproducible, but expensive, to dark arts that are largely undocumented.

The most interesting part of the model spec for industry analysts is this plot where OpenAI shares the agreement rate of their newer models. This is comparing a reasoning model, o1, to a GPT-4o model, so there are questions of whether this is attributable to reasoning training.

![A bar chart with alternating white and yellow bars on a black background, representing data comparisons. The yellow bars have a dotted pattern, adding texture to the visual presentation.](images/157355619.character-training_952e1f4f-4d12-4856-ad66-24640a3613eb.png)

## Every frontier AI laboratory should have a model spec

Model Specs are the sort of community norm that a race to the top is the goal. They're muddled if mandated --- how would you actually check that a required model spec is accurate? --- but if they are implemented by every lab carefully with feedback from the community, it would be far easier for the development ecosystem to exist around models.

The model spec is an extremely useful document detailing how developers can expect your models to change over time. They are also one of the few sources of insight we have into **what the model providers are trying to get their models to do** (which has [regulatory advantages](https://www.interconnects.ai/p/a-post-training-approach-to-ai-regulation?utm_source=publication-search)) and let us know what is an intentional or unintentional behavior mode.

A model spec doesn't provide all the information we need to keep up with model versions. **This new version of ChatGPT desperately needs to be accompanied by evaluations capturing the behavior change, otherwise, a lot of undocumented differences will be passed on to developers updating endpoints to it**. This is another rendition of the same lack of transparency we're used to from leading AI laboratories.

The closest thing Anthropic has to a model spec is the mix of [Claude's Constitution](https://www.anthropic.com/news/claudes-constitution) and this blog post on [Claude's Character](https://www.anthropic.com/research/claude-character). Character training is a fairly new technique for the industry.[3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} From Anthropic's post:

> Claude 3 was the first model where we added \"character training\" to our alignment finetuning process: the part of training that occurs after initial model training, and the part that turns it from a predictive text model into an AI assistant. The goal of character training is to make Claude begin to have more nuanced, richer traits like curiosity, open-mindedness, and thoughtfulness.

The process is extremely synthetic data-heavy, but requires an artist's touch, as stated later in the blog post: It "\[relies\] on human researchers closely checking how each trait changes the model's behavior."

Character training being the focus of developments is the strongest endorsement that RLHF and related approaches have shifted from their philosophical motivations of alignment to being primarily an empirical tool. The models can capture so many different behaviors, but getting them to reliably behave how we want is the hardest part. Right now, it seems more likely that this is about capturing the upside of RLHF as a performance tool, rather than a safety one.

One of the few public discussions of character training came from Amanda Askell during her appearance on the [Lex Fridman Podcast](https://www.youtube.com/watch?v=ugvHCXCOmm4) (taken from [the transcript](https://lexfridman.com/dario-amodei-transcript/)):

> **Lex Fridman** [(03:41:56)](https://youtube.com/watch?v=ugvHCXCOmm4&t=13316) When you say character training, what's incorporated into character training? Is that RLHF or what are we talking about?
>
> **Amanda Askell** [(03:42:02)](https://youtube.com/watch?v=ugvHCXCOmm4&t=13322) It's more like constitutional AI, so it's a variant of that pipeline. I worked through constructing character traits that the model should have. They can be shorter traits or they can be richer descriptions. And then you get the model to generate queries that humans might give it that are relevant to that trait. Then it generates the responses and then it ranks the responses based on the character traits. In that way, after the generation of the queries, it's very much similar to constitutional AI, it has some differences. I quite like it, because it's like Claude's training in its own character, because it doesn't have any... It's like constitutional AI, but it's without any human data.

In summary, Anthropic uses the same techniques they use for Constitutional AI and general post-training for capabilities to train these models' characters. This is not surprising. This could be related to Askell's other [Tweet](https://x.com/amandaaskell/status/1866207266761760812) on how she designs system prompts, as system prompts are the easiest way to quickly change a model's character:

> The boring yet crucial secret behind good system prompts is test-driven development. You don\'t write down a system prompt and find ways to test it. You write down tests and find a system prompt that passes them.

This is very in line with what we started this post on --- internal AI lab evaluations.

## How far can you push character training?

Ahead of the [Grok 3 release](https://www.interconnects.ai/p/grok-3-and-an-accelerating-ai-roadmap), Elon Musk [Tweeted](https://x.com/elonmusk/status/1891112681538523215/photo/1) this example from Grok 3, saying it was "based."

![Image](images/157355619.character-training_3bd8c3f1-8033-4ba8-b4ff-d8fca496ba3a.png)

One of the predominant reactions to Grok 3 was, "Wait, so it isn't actually based?" This is one of the big questions of character training and lacking model specs. Did xAI not figure out how to make their model-based and reliable? What model was Elon using here?

Whatever your politics, it's likely that the default personality of models that you encounter will eventually not be something you like. There's quite a lot of nuance in what the *perfect chatbot* is for each user.

Companies should be allowed to have a default personality for the models of their choosing, but a far better long-term equilibrium is to make the expectation that model providers make it easy to get exactly the personality you like out of a model. This isn't regulation I'm recommending right now, but one way to make sure that an all-powerful AI model isn't going to reinforce one point of view is to have tests that models need to pass on the *breadth* of their character and views.

Model specs are a step in the right direction to avoid drama about "[what did they actually want their model to say](https://x.com/elder_plinius/status/1893737449718681797)," but we still have a lot of work to do on creating a spectrum of tools that captures **all** the relevant information when comparing models.

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
My household unfortunately contracted Norovirus this weekend, and ChatGPT's banter on the situation was straight up hilarious.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
OpenAI co-founder John Schulman also shared his thoughts on the new model spec: <https://x.com/johnschulman2/status/1890457347019194507>
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
For more, see [Anthropic's mini podcast on AI's personality](https://www.youtube.com/watch?v=iyJj9RxSsBY).
:::
::::
