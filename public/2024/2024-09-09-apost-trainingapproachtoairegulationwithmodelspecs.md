---
title: "A post-training approach to AI regulation with Model Specs"
subtitle: "And why the concept of mandating “model spec’s” could be a good start."
date: 2024-09-09
type: newsletter
audience: everyone
visibility: public
post_id: 148661620.a-post-training-approach-to-ai-regulation
email_sent_at: 2024-09-09T12:30:24.932Z
---
The central point of AI regulation and policy over the last few years, everything from the Biden Executive Order to California's SB 1047 bill, has been model size. The most common tool for AI enforcement proportional to model size has been thresholds that kick in once an AI system uses more than a certain amount of compute (or money) to be trained. The [use of thresholds for regulation is the subject of substantial pushback](https://arxiv.org/abs/2407.05694) and is likely fading in relevance due to it.

A common chorus among those who lean on the open side of the open vs. closed AI debate (and the safety vs. acceleration debate that mirrors it) is that we should regulate the applications of AI systems rather than the models. The argument is that most harm from powerful AI comes from misuse, and amplification of existing harms, rather than new harms being unlocked by latent capabilities of the model.

It shouldn't be surprising that most AI regulation debates to date have been contentious. The moves being made are likely to do some combination of cost a large amount of money, force AI labs to disclose that they are using data likely to result in them getting sued, or slow future development of the technology. Finding a way to regulate AI, particularly in a light-touch and pro-transparency manner, should be where we start.

Until I'm presented with more evidence that frontier language models are meaningfully shifting something like bio-risk or cybersecurity or something in the same vein, I have an application-focused lens for regulation too.

This takes us back to post-training. Post-training methods, the most common topic on Interconnects, is a collection of fine-tuning techniques, inference tricks, and other details to prepare a machine learning model for a certain deployment. Post-training is done to make models ready for general deployments, such as chatbots, and specific deployments, such as fine-tuning a domain-specific model. In this lens, post-training is the closed touchpoint to where harm is likely to occur.

### Expanded roles of Model Specifications

The Model Spec, currently only released by OpenAI, is a document that conveys the goal behavior of a model served to customers. It was written by members of the post-training team and product teams at OpenAI, such as co-founder John Schulman (now at Anthropic). The document contains a list of principles and examples for desired behavior, including things that could be the source of disagreement and behaviors that may not reliably work in current models.

The two quotes I highlighted when [I first wrote about Model Specs](https://www.interconnects.ai/p/openai-rlhf-model-spec?utm_source=publication-search) still convey the goal in the best manner.

::: {.digest-post-embed attrs="{\"nodeId\":\"f3718d30-703b-44f1-9c27-414febeb7c59\",\"caption\":\"OpenAI recently shared what they call their “Model Spec,” a document that details their goal model behaviors prior to clicking go on a fine-tuning run. The name is a little vague, it’s about the model behavior and how OpenAI steers their models from behind the API. I doubt the actual model capabilities change much in this process, which is what the spec…\",\"cta\":null,\"showBylines\":true,\"size\":\"sm\",\"isEditorNode\":true,\"title\":\"OpenAI’s Model (behavior) Spec, RLHF transparency, personalization questions\",\"publishedBylines\":[{\"id\":10472909,\"name\":\"Nathan Lambert\",\"bio\":\"ML researcher making sense of AI research, products, and the uncertain technological future. PhD from Berkeley AI. Experience at Meta, DeepMind, HuggingFace.\",\"photo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdda47b96-836a-4b95-99a0-f0ec744d4245_2316x2316.jpeg\",\"is_guest\":false,\"bestseller_tier\":100}],\"post_date\":\"2024-05-10T21:03:03.742Z\",\"cover_image\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c4bbb4a-97f3-4333-bbf0-bbf91dc4d792_1792x1024.webp\",\"cover_image_alt\":null,\"canonical_url\":\"https://www.interconnects.ai/p/openai-rlhf-model-spec\",\"section_name\":null,\"video_upload_id\":null,\"id\":144518232,\"type\":\"newsletter\",\"reaction_count\":17,\"comment_count\":0,\"publication_name\":\"Interconnects\",\"publication_logo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe70f9dbf-4fe6-404c-b6bb-1831d1b7ed0b_590x590.png\",\"belowTheFold\":true}"}
:::

Sam Altman shared a brief explanation of what this means [on Twitter](https://twitter.com/sama/status/1788260474574000152):

> we will listen, debate, and adapt this over time, but i think it will be very useful to be clear when something is a bug vs. a decision.

[Joanna Jang](https://twitter.com/joannejang/status/1788255370504220940) in the product organization echoed a version of this:

> principles are easier to debate and get feedback on, vs. hyper-specific screenshots or abstract feel-good statements.

Model specifications will allow us to contextualize some misuse of language models into two categories:

-   **Misuse of unintentional model behaviors**: When the model's goals don't work fully, such in the face of jailbreaking, which results in downstream harm. Or,

-   **Misuse of intentional model behaviors**: When a user figures out how to exploit a behavior trained into the model to propagate increased harm.

Given that AI training is rapidly evolving, I expect all types of these to be achieved. From a regulatory perspective, if you mandate the use of Model Spec and notice prevalent "Misuses of intentional model behaviors," then the lab developing the model could reasonably be more liable. In the early cases, auditing and transparency are more useful than financial damages, but they paint a clear framework for accountability in how you enable AI applications.

While this post focuses on regulation, the Model Specification documents are also valuable to researchers and customers. Researchers get valuable insight into the mindset and decision-making of training powerful AI models while developers can compare models and see the ideological stance that best fits their use case. Documenting the *intent* of powerful and non-interpretable computational systems is one of the only things we can do.

### Near future of Model Specifications

Model Specs can bridge audiences. Being clear about the intention of the models is useful for addressing both short- and long-term types of risk. It is rare that an intervention can be presented as useful to all communities of the many-viewed AI debate. For example, the question was raised as to "What if we can sufficiently align a model to a Model Spec" on the recent [Dwarkesh podcast with Joe Carlsmith](https://www.dwarkeshpatel.com/p/joe-carlsmith).

There are many examples of why the Model Specification is the correct abstraction for auditing current systems. They're not so technical that only researchers can read and use them, but they are still extremely specific in a way that heavily informs model behavior (and can be informed by recent alignment research, such as OpenAI's [Instruction Hierarchies](https://openai.com/index/the-instruction-hierarchy/)). An example of what is not an optimal abstraction is releasing the Constitutional AI prompts.

Constitutional AI is a method for getting many different behaviors out of a model and it is *not clear* if the downstream behaviors of a model are calibrated to the principles used in the training data. Much like human feedback, or generalized to human preferences in reinforcement learning from human feedback (RLHF) process does not clearly capture values. Releasing Constitutional AI principles along with *why* they were used begins to be useful for oversight.

I'm not convinced we need any specific liability regimes on what is or is not said in corporate Model Specifications to start with, but requiring some disclosure here would be some of the least revealing for the frontier labs in terms of trade secrets (not making anyone talk about data), but also very revealing for monitoring how different strategies and goals in post-training can contribute to increased marginal risk in our information ecosystem.

Now that John Schulman is at Anthropic, I expect them to come out with a Model Spec soon enough, which I expect philosopher turned AI scientist (and many things, such as originator of Constitutional AI) [Amanda Askell](https://askell.io/) to have a useful role in. Once Anthropic releases one, or something like it in addition to their [documentation of system prompts](https://docs.anthropic.com/en/release-notes/system-prompts), Google and others will follow.

If this interests you, or you work at a company performing large amounts of post-training and you want to discuss Model Specification documents, please reach out or comment below. Of course, post-training viewpoints cannot cover everything forever, so we will eventually see regulation on the pretraining side of things. Hopefully not with the likes of CA SB 1047.

<div>

------------------------------------------------------------------------

</div>

**Housekeeping**

-   Audio of this post is available (soon) in [podcast](https://podcast.interconnects.ai/) form (and sometimes on [YouTube](https://www.youtube.com/@interconnects)).

-   My real podcast is at [retortai.com](http://retortai.com).

-   *Paid subscriber Discord access in email footer.*

-   Referrals → paid sub: Use the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   Student discounts in [About page](https://www.interconnects.ai/about).
