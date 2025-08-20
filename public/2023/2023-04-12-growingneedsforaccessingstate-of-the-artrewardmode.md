---
title: "Growing needs for accessing state-of-the-art reward models"
subtitle: "The rewards assigned by these models will control the subjective experience of users; the subjective experience controls their decision-making."
date: 2023-04-12
type: newsletter
audience: everyone
visibility: public
post_id: 113947291.open-rlhf-reward-models
email_sent_at: 2023-04-12T16:41:26.041Z
---
The only piece of the RLHF pipeline we\'ve never had access to in a substantive manner is the reward model (also referred to as the preference model). While RLHF soaks in the glory of being the hot and impactful topic of 2023, a central piece of it still can\'t be probed by researchers trying to chart a path for how these technologies will impact society. Giving researchers access to the reward model will also give the companies important new evaluation angles to improve the robustness of their models --- if they need more motivation than preventing harm. I\'m not sure if these APIs don\'t exist because they think no one will use them (they're busy folks) or if exposing them will make it very easy for other players to reproduce their models with them (they're competitive folks).

If we need to give context as to why the internal values of the reward model are important to audit, we\'re at the point where there are Nature articles dictating how [ChatGPT\'s inconsistent moral advice influences users\' judgment](https://www.nature.com/articles/s41598-023-31341-0). Methodologically, the inconsistency of any moral advice is likely mirrored by the inconsistency in the reward models. Based on general technical consensus, the reinforcement learning (RL) optimization phase of learning from human feedback is known to *extract all information from the reward model* while reshaping the base model. The base model comes with substantial knowledge to the party, and the reward model is a critical filter that everything goes to on the way to end-users. We don't have access to any of these powerful content filters.

In this post, I\'ll discuss further ways that the reward models will evolve and why we need access to a SOTA reward model informing the products used by millions. This builds on my recent piece, where I discussed the philosophy of optimizing preferences:

::::::::: {.embedded-post-wrap attrs="{\"id\":110914092,\"url\":\"https://robotic.substack.com/p/costs-v-rewards-v-preferences\",\"publication_id\":48206,\"publication_name\":\"Democratizing Automation\",\"publication_logo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9b01328d-6e9d-44cb-9f0e-649bbd98eb1a_699x699.png\",\"title\":\"The implicit dynamics of optimizing costs vs. rewards vs. preferences\",\"truncated_body_text\":\"We don’t have any guarantees that preference models even remotely match our actual preferences. If you follow the scientific history of reinforcement learning (RL) back to Bellman updates and optimal control, the progression has been from costs to rewards to preferences. Cost functions have their origins as closed-form expressions selected by engineers …\",\"date\":\"2023-03-27T14:45:00.155Z\",\"like_count\":9,\"comment_count\":0,\"bylines\":[{\"id\":10472909,\"name\":\"Nathan Lambert\",\"previous_name\":null,\"photo_url\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/dda47b96-836a-4b95-99a0-f0ec744d4245_2316x2316.jpeg\",\"bio\":\"ML scientist at Huggingface (RL, RLHF, society, robotics), athlete, yogi, chef.\\nWrites about ML & society.\\nPhD from Berkeley AI, Cornell Lightweight Rowing `17\",\"profile_set_up_at\":\"2021-04-24T01:19:33.371Z\",\"publicationUsers\":[{\"id\":100753,\"user_id\":10472909,\"publication_id\":48206,\"role\":\"admin\",\"public\":true,\"is_primary\":false,\"publication\":{\"id\":48206,\"name\":\"Democratizing Automation\",\"subdomain\":\"robotic\",\"custom_domain\":null,\"custom_domain_optional\":false,\"hero_text\":\"On machine learning and robotics. The interface of systems and society.  The border between high-level and technical thinking.\",\"logo_url\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/9b01328d-6e9d-44cb-9f0e-649bbd98eb1a_699x699.png\",\"author_id\":10472909,\"theme_var_background_pop\":\"#ff6b00\",\"created_at\":\"2020-05-21T02:59:47.895Z\",\"rss_website_url\":null,\"email_from_name\":\"democratizing automation\",\"copyright\":\"Nathan Lambert\",\"founding_plan_name\":\"Founding Member\",\"community_enabled\":true,\"invite_only\":false,\"payments_state\":\"disabled\"}}],\"twitter_screen_name\":\"natolambert\",\"is_guest\":false,\"bestseller_tier\":null}],\"utm_campaign\":null,\"belowTheFold\":false,\"type\":\"newsletter\",\"language\":\"en\"}" component-name="EmbeddedPostToDOM"}
[](https://robotic.substack.com/p/costs-v-rewards-v-preferences?utm_source=substack&utm_campaign=post_embed&utm_medium=web){.embedded-post native="true"}

::: embedded-post-header
![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/9b01328d-6e9d-44cb-9f0e-649bbd98eb1a_699x699.png){.embedded-post-publication-logo}[Democratizing Automation]{.embedded-post-publication-name}
:::

:::: embedded-post-title-wrapper
::: embedded-post-title
The implicit dynamics of optimizing costs vs. rewards vs. preferences
:::
::::

::: embedded-post-body
We don't have any guarantees that preference models even remotely match our actual preferences. If you follow the scientific history of reinforcement learning (RL) back to Bellman updates and optimal control, the progression has been from costs to rewards to preferences. Cost functions have their origins as closed-form expressions selected by engineers ...
:::

::: embedded-post-cta-wrapper
[Read more]{.embedded-post-cta}
:::

::: embedded-post-meta
2 years ago · 9 likes · Nathan Lambert
:::
:::::::::

![](images/113947291.open-rlhf-reward-models_13933a56-25d7-4711-9bfb-a5152b57c79c.png)

### User feedback frontiers

There are so many wonderful ways to mend the reward signal to an RLHF model once the deployment state has a consistent user base (e.g. ChatGPT, but there will be others). All of the ones I\'ve come up with for this article help us move the terminology closer to that of *reward models* and away from preference models. To review, the reward models used in ChatGPT and this generation of models are all built on pairwise preferences (e.g. which of two sentences do you like better), but with none of the decision theory that would enable properties like [transitivity](https://en.wikipedia.org/wiki/Preference_(economics)#Transitivity). In the end, core properties that matter for the communication of a human\'s preferences all bounce off of *how they compare to other humans*.

Yes, Sam Altman has *said* OpenAI will provide users with individually-tuned models, but we don\'t know when, and that is a good tactic to stall any potential regulatory ire around centralizing human values. In the meantime, there are tons of things OpenAI will be investigating to make the model more of an attention trap, but they\'re not about stated user preferences. From a product perspective, they\'re likely to continue to evolve towards rewarding the model for soliciting consistent behaviors out of you.

A model that leverages user behavior is not a model of preferences. It is a model of reward. A model that allows users to define what they want is starting to look like a preference model. To be clear, we do not have this.

If we start from the other end of this article and make a generalization to get the point across, calling the reward model powering future chatbots a preference model will be the same as calling the model serving you TikTok videos a preference model. We don\'t want to equate how we interact with algorithmic feeds to our preferences.

These models are reward models. The reward is a scalar value designed to represent how good of an outcome the output is to the system specified as the model plus the user. A preference model would capture the user individually, a reward model captures the entire scope.

The way this all comes to pass is that chatbot companies can optimize for behaviors like closing the tab mid-generation, excessive pauses, complaining responses, regenerate-button clicks, etc. to understand the perceived quality of the message from the LLM. This will start to sound like a familiar story for those versed in the evolution of the newsfeed. The user behaviors are likely to be the **revealed preferences**, while the up and down arrows will be corrupted by stated preferences. What a user wants is different than what they think they should be grading.

The far future of these methods is even more off-putting. When chatbots become both more capable and more integrated, these types of feedback will be tricker for engineers to monitor and even more unexpected by the user. If a model seems to oscillate between different personalities based on what you asked it, any model of this will be even further away from interpretable. Consider a bot that is funny when you ask it for movies or entertainment recommendations but is assertive when helping you negotiate a raise. In this case, the user will probably be much more confused in stating their preferences, but again and again, we have shown engagement optimization techniques to work for machine learning first content systems.

The medium of text also enables these user preferences to be more nuanced. When the user is more nuanced, the model is arguably more powerful over the user. In another domain, such as images, it seems like there will be much less leeway for the model to manipulate the moral judgment of a user. This also could be because humans are more evolved for visual intuition, as text is a relatively new invention. If working in RLHF for LMs gets too crazy, maybe I can retire to just RLHFing visual models.

When the doors are opened to plugins, this platform designed around user preferences gets even more complex. The capabilities are going to move super fast, so I am excited, but let\'s make sure we think through what is happening before we move on to the next thing.

### Reward model specification, communication, and origins

This is mostly added to the list of concerns I have around the specification and communication of reward models. The phrase \"preference model\" indicates that the systems are complete and consistent, at least directionally, in their capture of our values. To start to wrap up the broken record that is this blog post: this is untrue. Until the origin of preference models is proven to not be a means to an end, I encourage extreme wariness on interacting with them in any way other than as an incomplete model or toy.

Following the paper trail, \"reward modeling\" as a phrase was popularized in the [Learning to Summarize with Human Feedback paper](https://proceedings.neurips.cc/paper/2020/file/1f89885d556929e98d3ef9b86448f951-Paper.pdf), which references an exploratory work from when Jan Leike was still at DeepMind: [Scalable agent alignment via reward modeling: a research direction](https://arxiv.org/pdf/1811.07871.pdf). I\'m encouraged that there is a foundational paper on this, but there are some clear issues when you compare the definition's origins to how it's used today. The model\'s design specification problems are listed as common AI Safety problems, like \"off-switch problems, side-effects, absent supervisor, containment breach, creation of subagents, and more.\" The models being designed from an agentic perspective and being used as a training tool in complex, super-scale computing is a pretty big mismatch that I want to see filled with more literature. There are long-term problems around preference models, but I would argue the more pressing ones for this technology are short-term.

Ultimately, it just seems likely that the language models got so good that they also became decent at repeating preferences --- I don\'t think that means they\'re compelling or trustworthy in this regard.

I\'m calling for OpenAI, Anthropic, or another leader in the space of learning from human preferences to **open API access to researchers to better understand the capabilities of the reward models**. This will remove substantial liability from the fact that all of this is behind closed doors --- that corporations are telling us to trust them about models of our preferences. The reward models even seem to have less intellectual property risk than the base models, when people are using the outputs of GPT4 and Claude to instruction-tune other models or rank preferences for RLHF.

*Note, there is an [article on lesswrong](https://www.lesswrong.com/posts/nTy48zvBPPttoLhdJ/on-the-importance-of-open-sourcing-reward-models) that articulates this from an alignment perspective, too.*

Hopefully, readers across the industry can help me communicate the right way to say that reward models have risks to users and capture the uncertainty within downstream tuned model outputs.

### Endnote: reward models for evaluation boosting

The reward models may also be central to the evaluation results in the GPT4 paper; OpenAI could easily be using a technique called rejection sampling (or best-of-n sampling) to select the best output. Best-of-n sampling is a simple topic: if you take a single prompt, you generate N responses rather than just 1. Pass this batch of responses through the reward model together, then choose the response that got the highest reward! If your reward model consistently rewards factual accuracy, this could boost benchmark performance on many of the multiple-choice benchmarks used (like [MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu) or [TruthfulQA](https://github.com/sylinrl/TruthfulQA)).

Ultimately, until the field re-groups to share knowledge and models with each other, there will always be huge questions around the evaluations reported in thinly veiled technical reports.

<div>

------------------------------------------------------------------------

</div>

You'll see some changes to Democratizing Automation next week. I'm excited about the next chapter. Also, I'm going to try and send out articles most Wednesday mornings, and if not I'll post in Chat.

*More:*

-   We at HuggingFace released a blog post showcasing how to do the entire RLHF stack on LLaMA models: [StackLLaMA](https://huggingface.co/blog/stackllama).

-   I'll be doing a fireside chat on April 27th to discuss my career journey and working in AI, [register here](https://docs.google.com/forms/d/e/1FAIpQLScm1EbSd2C_ptXHP61gk5AkU08aMcBZ24GBPL5gj4EkaSqs6A/viewform).

Democratizing Automation is free and for you. Feeling generous? [Buy me a coffee](https://www.buymeacoffee.com/natolambert).
