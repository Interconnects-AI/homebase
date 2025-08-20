---
title: "RLHF, 'online' ML systems, and RL going mainstream"
subtitle: "Common machine learning systems are starting to deploy the RL lens of feedback."
date: 2022-12-05
type: newsletter
audience: everyone
visibility: public
post_id: 88131722.rlhf-2022
email_sent_at: 2022-12-05T21:06:05.773Z
---
We are beginning to see ML systems where users provide the signals for updates **and the models are updated automatically**. Updating models from user feedback is not new \-- designing a system that does this feedback in real time is new. This is what I am excited about, as it casts all machine learning systems through the lens of [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) (RL) that I use to study the world. Reinforcement learning is the mathematical framework that allows one to study how systems interact with an environment to improve a defined measurement. This frame is way more flexible than the most popular recent research studying it, which focuses on specific robotics tasks or video games.

![download (6).jpeg](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/a641be31-a019-498d-81de-b6244a28825d_768x768.jpeg)

Last time I wrote on this [subject](https://robotic.substack.com/p/ml-becomes-rl) of all-ml-is-rl, I talked about how an ML-focused software as a service ([SaaS](https://en.wikipedia.org/wiki/Software_as_a_service)) company could use a churn model with data feedback to try and keep its most valuable users:

> More precisely, this *action* could take the form of new parameters that tune text in email subjects to individuals on an email list. This *policy* (the model that determines actions) could change the text across each registered email address, targeting a variety of email preferences, e.g. those who like emojis (many people do). As there is no free lunch in any optimization, adding emoji's would not be every user's favorite, which could be represented by the *reward* the engineer sees after this new model is deployed. This tuning could be done automatically. Though, this change could have unintended behavior of those who were currently the most loyal customers becoming annoyed --- a **[positive feedback loop](https://en.wikipedia.org/wiki/Positive_feedback)** of churn so to say.

This was a hypothetical to illustrate the high-level concept of **feedback**. I\'m a total feedback-stonks-fanboy. [Feedback](https://en.wikipedia.org/wiki/Feedback) has been one of the single most powerful techniques in modern technologies, and this will be the same for machine learning.

There are many ways that these feedback signals can be provided (and I am trying to follow all of them) in the data for ML. They differ in quality (directness), speed (when the measurement occurs), noise (how reliable the two other features are), and of course many more factors. Roughly speaking, the different ways a user (or human) could provide updated data for a model improving iteratively are as follows:

1.  **Direct feedback** on model outputs \-- e.g. curated data used in the likes of Reinforcement Learning from Human Feedback ([RLHF](https://openai.com/blog/instruction-following/)). In these cases, select people (often not the end users) are paid to use the model and comment on its strengths and weaknesses.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

2.  **Direct interaction** with the model \-- e.g. a chatbot, an algorithm for serving content, etc. In these cases, the consumer is using a service as is and providing a signal that is useful. Most ML services use this data, but only in batch-mode training. A recent [paper](https://arxiv.org/abs/2209.07663) from ByteDance confirms this is starting to change.

3.  **Second-order feedback** \-- exogenous feedback, \"in which the domain itself shifts in response to the deployed RL policy\" (from my [recent paper](https://arxiv.org/abs/2202.05716)). An ML system could figure out that by repeatedly prompting a user inside of a specific task, eventually, the user\'s behaviors can change in a suite of downstream tasks. This works similarly in concept to how advertising works in practice \-- most people say advertisement doesn\'t affect them. This statement is true and false; the billboards don\'t affect your driving, they affect your shopping two weeks later. ML systems don\'t work like this now, but there are no structural reasons why they could not.

In writing this, it became really obvious to me that these different types of feedback are clearly ranked in terms of quality (1. being the highest), which is inversely correlated with the quantity available. OpenAI and Anthropic have been pushing the limits on integrating this human preferences feedback directly. I expect other companies to figure out direct interaction sooner (could be argued that ByteDance does so on TikTok, but it\'s not fully documented yet). I also think that Meta could be a candidate for figuring out the second and third options. They\'re known as being the base for quantitatively tracking the performance of highly specific advertisements via large machine learning platforms.

This post really is a summary of the early signs of organizations using data feedback to perform online updates to machine learning models. We\'ll look at a newly deployed language model from Meta, a research paper from ByteDance, an ongoing project from HuggingFace, and the complexity of RLHF.

<div>

------------------------------------------------------------------------

</div>

Additionally, but slightly off-topic, it\'s an important moment for RL to be a central part of the scientific method that is so popular in the broader technology industry \-- ChatGPT uses Reinforcement Learning from Human Feedback ([RLHF](https://cmt3.research.microsoft.com/ICML2022/))! Seems like the first time it\'s been highlighted in a [Stratechery](https://stratechery.com/2022/ai-homework/) article and is a major breakthrough since the times when AlphaGo et. al were the only mainstream RL successes (and they weren\'t reproducible).

There are already multiple large companies investing in RLHF. I expect to study RLHF much more in the near future, reach out or comment if you are interested.

<div>

------------------------------------------------------------------------

</div>

## The origins of RLHF and human vs data feedback

I\'ve really wanted to write this post for a while. It\'s really important to me that the field of machine learning figures out the right way to compare **human feedback** and **data feedback**.

One may say that we can replace human feedback with human preferences, but we don\'t want to say we trained a machine learning model to capture human preferences. We have measured human preferences as a snapshot in collecting data, but it will always be incomplete.

Data feedback is the core function of reinforcement learning. There are different types of data feedback in the way it is commonly used[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}. There\'s feedback from the state to action, feedback from replay buffer to policy, and feedback from agents to the real world. These effects are challenging to measure on their own.

Human feedback is not new and not specific to machine learning. Using human feedback for ML systems was popularized in NLP with a series of papers from OpenAI, which recently culminated in the model [InstructGPT](https://arxiv.org/abs/2203.02155). This paper title, *Training language models to follow instructions with human feedback*, really challenged me because they highlight the contributions of RL in their paper (where data feedback is crucial), but add the term **human feedback** to the title.

Since then, RLHF has exploded beyond OpenAI. Anthropic has even released [data](https://github.com/anthropics/hh-rlhf) used in this process with their [paper](https://arxiv.org/abs/2204.05862). CarperAI has released a [tool](https://github.com/CarperAI/trlx) for doing RLHF. There are certainly more I missed, but these are some important ones.

What is still left to be found out in the field is if these papers were powered by the strengths of human feedback (high-quality data) or reinforcement learning (a powerful black-box optimizer). For now, I actually think it is the former. Hopefully, this changes because I am most interested in the concept of data feedback: how a signal propagates through repeated training.

<div>

------------------------------------------------------------------------

</div>

## Recent progress in systems using RL-like approaches

*Disclosure: I\'m working with or talking with the authors of all of these projects, so they\'re varying levels of biased.*

In the last couple of months, I\'ve started working on the ideas above and have been surprised by real-world renditions of them. Let\'s start with our work.

#### Online Language Model

\[[tweet link](https://twitter.com/TristanThrush/status/1557403968195596288), [discord channel](https://discuss.huggingface.co/t/join-the-hugging-face-discord/11263) - #online-language-model\]

The goal of this project is to create a language model that is always up to date with current events. I see it as a given that future versions of the systems like this will always have real-time feedback, though we are not close to being there yet.

A large limitation on being able to apply RL ideas to the most basic NLP tasks (e.g. training a model on a moderately-large chunk of data to accurately predict sentences) is the lack of data understanding. In the case of the online language model project, a large portion of time has been spent on trying to understand how time may be embedded in current data. This time embedding can be dates at the top of news articles, hidden tags in the HTML code, and more. Overall, even the most common NLP training corpora (such as [Common Crawl](https://commoncrawl.org/)) are not characterized with respect to recency.

Getting past the data issues, many folks are addressing the question of temporal relevance for their language models, but the infrastructure to address this problem is also woefully lacking[3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}. ML models are just not frequently updated based on data triggers. The initial version of this project reflects this: training a new model every couple of months on time-relevant datasets.

One of the most specific use cases of a time-revenant language model is a chatbot. Who wants to talk to something that doesn\'t know basic facts about current events?

This project doesn\'t capture the specific feedback mechanisms detailed above, but applications of it likely would.

#### BlenderBot3

\[[demo](https://blenderbot.ai/), [documentation](https://parl.ai/projects/bb3/), [paper](https://arxiv.org/abs/2208.03188)\]

BlenderBot is really, really interesting. Meta released this model with a long list of promises: state-of-the-art language generation, safe behavior, integrating user feedback, and an open demo. Since its release, it hasn\'t been clear if the iterative updates outlined in the paper have been enabled, but it is designed to be an autonomous system that improves over time based on user feedback.

There are tons of details to read into if you\'re interested. There\'s a [paper](https://arxiv.org/abs/2208.03295) on the data labeling designed to eliminate trolls messing with the bot, a [paper](https://arxiv.org/abs/2208.03270) on online improvement, and a [paper](https://arxiv.org/abs/2206.07694) on the language model for accurate and safe generations.

We\'re working with the authors to create a [Reward Report](https://arxiv.org/abs/2204.10817), a form of documentation we proposed to understand the effects of feedback in ML systems, in order to understand how this model could evolve over time.

This project seems like it\'s trying to incorporate both direct feedback (data labeling and cleaning processes) and direct interaction (chatbot functionality) feedback to improve its data.

#### Monolith

\[[Paper](https://arxiv.org/abs/2209.07663)\]

*Real-Time Recommendation System With Collisionless Embedding Table* is seemingly the first paper to confirm a lot of the ideas people have converged on for how the TikTok algorithm works. It\'s fast, flexible, and deeply integrated with the service. This isn\'t a paper I would recommend you to read in detail if you\'re interested in this topic. In fact, it\'s mostly a systems paper \-- there are some hidden gems in it though.

The real-time stuff is the interesting part. I can\'t be that bothered about how they use embeddings to keep track of if you really like dogs or just thought that one cat video was funny.

Quoting from section 2.2:

> Online training stage. After a model is deployed to online serving, the training does not stop but enters the online training stage. Instead of reading mini-batch examples from the storage, a training worker consumes realtime data on-the-fly and updates the training \[parameter server\] (PS). The training PS periodically synchronizes its parameters to the serving PS, which will take effect on the user side immediately. This enables our model to interactively adapt itself according to a user's feedback in realtime

They then go on to discuss the lag of user action after being shown content, having way more negative labels than positive labels (e.g. interactions like purchases, likes, etc.), synchronization of updated parameters across deployments, and more.

It\'s super exciting to see these ideas I predicted over a year ago are becoming real (my predictions were without any discussion of the system-engineering challenges)! This paper clearly uses direct interaction feedback with the user to improve.

<div>

------------------------------------------------------------------------

</div>

The fact that all of this exists shows it is the right time to learn about feedback and think about it in your ML problems.

Positive feedback loops have caused many problems in classical engineered systems; unstudied feedback in machine learning systems will cause a lot of harms as well, but I suspect it\'ll have different flavors.

It seems like I may start working with RLHF, which will help clarify a lot of the grandiose claims in this post. My next step is to go deep into Anthropic\'s [tome](https://arxiv.org/abs/2204.05862). Thanks for reading.

:::: {.captioned-button-wrap attrs="{\"url\":\"https://www.interconnects.ai/p/rlhf-2022?utm_source=substack&utm_medium=email&utm_content=share&action=share\",\"text\":\"Share\"}" component-name="CaptionedButtonToDOM"}
::: preamble
Thank you for reading Democratizing Automation. This post is public so feel free to share it.
:::
::::

*Thanks to [Tom Zick](https://twitter.com/thesezickbeats?lang=en) for providing feedback on this post (written, not data!).*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
These companies further pay people to do **[red-teaming](https://arxiv.org/abs/2202.03286):** trying to break models so engineers can improve them.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
We explain them in detail [here](https://arxiv.org/abs/2202.05716).
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
If you\'re interested in this research, check out this Continual Learning in NLP [literature review](https://docs.google.com/document/d/1q9LOj4DJEOAnUhGNJPmYXy0Wp56U1sOnrAOdWqh-ovI/edit) we conducted.
:::
::::
