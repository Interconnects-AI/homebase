---
title: "Closed-API vs Open-source continues: RLHF, ChatGPT, data moats"
subtitle: "Model-as-a-service makes more sense when there is a data advantage to back it up."
date: 2022-12-19
type: newsletter
audience: everyone
visibility: public
post_id: 91481511.rlhf-chatgpt-data-moats
email_sent_at: 2022-12-19T15:14:52.780Z
---
*Elsewhere from me recently:*

-   *An introduction [blog post](https://huggingface.co/blog/rlhf) and [lecture](https://www.youtube.com/watch?v=2MBJOuVq380&feature=youtu.be) on reinforcement learning from human feedback (RLHF) --- start here if RLHF is confusing (first page results on Google for RLHF 🤘).*

-   *A paper on [Measuring Data](https://arxiv.org/abs/2212.05129) in machine learning, defining a future field of research that\'ll improve many ML systems.*

-   *Another seasonal [ethics & society blog post](https://huggingface.co/blog/ethics-soc-2) with my 🤗 HuggingFace teammates.*

-   *[Hiring](https://apply.workable.com/huggingface/j/B3CDE6C150/) interns on large-scale RL / RLHF.*

*Onto the post.*

<div>

------------------------------------------------------------------------

</div>

The next chord in the duet of closed- vs open-source machine learning companies in 2022 has been the release of ChatGPT and the blossoming commitment to reinforcement learning from human feedback (RLHF) as a valued tool across the industry[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}. ChatGPT itself is not much of an evolution of the tale because *we knew OpenAI would continue* to push itself as the maker of the best and most relevant models (and the hyped GPT4 will forever be coming soon, like the Thrones books). The change here is around the *dynamics* of the artifacts like **expensive datasets** + **compute infrastructure** and the **industry-wide response**.

RLHF is **being heavily bet on** **in industry** and has some very different properties than other generative models that make it *less suited to open-source*: hard to get the data via expensive human annotations, hiring experts in multiple areas like deep RL, and strong potential for internal use-cases like search.

As you all know, OpenAI release ChatGPT and it quickly rose to [over 1 million users](https://www.yahoo.com/lifestyle/chatgpt-gained-1-million-followers-224523258.html) and is the leading talking point in OpenAI\'s [new fundraising rounds](https://www.reuters.com/business/chatgpt-owner-openai-projects-1-billion-revenue-by-2024-sources-2022-12-15/). It is the company that stands to represent the closed-API business model. The API, application programming interface, is a way to access their models. Different models, amounts of compute, and ways to access them can cost different amounts of money. For now, most of these companies heavily subsidize this usage to get users. Other companies are following in their footsteps, but honestly they haven\'t proven how their models will be useful (except for capturing specific product verticals like [Jasper](https://www.jasper.ai/) and (my favorite) [Runway](http://runway.ml/)).[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

The benefit of the open-source business model is that the *customers* will use their own compute, but one needs to be more creative in monetization, e.g. premium features. Which premium features are best is mostly TBD too.

OpenAI was on the ropes, so to say[3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"},  after Stable Diffusion. Stable Diffusion crushed DALL-E 2\'s usage, making API slash its prices (not that it did much). Stability raised a ton of money and epitomized the return of the open-source wave. Everyone really thought OpenAI\'s current business model was dead (especially given how they are rumored to only make about \$10 million a year in revenue and have extremely high costs). What has changed with ChatGPT is the assumption of the scale that OpenAI can reach, with some people even going too far and saying it can compete with Google. Gosh, even Ben Thompson said on one of his many podcasts that \"OpenAI may be the most likely company to rival the big tech giants!\"

I\'m not so sure OpenAI has everything figured out, but it seems like they took a giant step closer to their goals being realistic rather than lost in the clouds. This post is a rumor collection on RLHF with crucial commentary on how the war of API companies vs. open-source companies swung back. It\'s amazing to see what is next. There\'ll be an open-source ChatGPT within 6 months, surely, but there are a whole sea of questions around **user interfaces** and **data longevity** that engrain OpenAI\'s advantage in the dialogue space.

OpenAI\'s partnership with Microsoft has culminated with ChatGPT. It lets them deploy this large language model[4](#footnote-4){#footnote-anchor-4 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"} at a low enough cost to accumulate a huge data advantage. What will the open-source coalition do for this sort of API? Yes at HuggingFace we will do our best, but things like Spaces and Gradio support the long-tail / decentralized applications much better than one gigantic deployment of a viral model. Without this snappy, appealing interface, closing the data gap will become an existential question for open-source alternatives.

I know this is negative on the things I am working on myself --- I\'ll do my best to prove these takes wrong --- but we have to revel in the successes of ChatGPT while it's new and appreciate the great machine learning feat that it is!

![download (10).jpeg](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/90535660-c98d-4e21-8f22-62c37c58b736_768x768.jpeg)

### RLHF on Language for Search

ChatGPT has been touted as the biggest rival to Google because of its function as a **search engine**. The thing is, these dialogue-focused LMs will never replace what Google is doing fully. Google is using similar underlying technology as ChatGPT (LMs, scraping the internet, Transformer architectures), but it is optimizing for search rankings and results. These results are an entirely different medium and Google has been an industry leader in LMs for a long time (before and through the [Transformer](https://arxiv.org/abs/1706.03762) era). Given that these results are ranking-based, they\'re also less in need of the human-feedback nature of what ChatGPT offers.

We already give Google the feedback it needs to make an effective model, *which link do we click*? Meanwhile, OpenAI must collect prompts from the users writing in the ChatGPT box, heavily filter that data, and curate responses via a contractor army (that is optimizing for something other than search). When using RLHF, it seems required to be able to define your task (e.g.\'s dialogue, code completion, question answering, alignment) and collect very specific data to accomplish this.

Given this, it\'s unlikely that dialogue-focused agents will continue to get much better at search. Right now, there\'s a bit of a theme going around that ChatGPT is really good at returning answers on specific subjects (which may be due to the fact that there\'s less data conflicts in the training corpus). For example, look at this explanation of RLHF we added for our introductory [blog post](https://huggingface.co/blog/rlhf):

![Image.tiff](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/a545ed1e-9772-4691-9092-dd0798bbb671.tiff)

This highly-specific data without substantial variance in training could also point to a use case for internal search tools. If you\'ve ever worked at a big company, you know the infinite pages of documentation that exist to *help* employees. These pages are classically hard to find without asking a teammate. Some folks with more experience in RLHF posit that this could point to a feature for the model-as-a-service companies. I heard a rumor that [Cohere](https://cohere.ai/) wants to offer a service where companies can have language models fine-tuned as a search engine. I think this is a compelling product and one I\'m excited to follow.

The closed nature of these products echoes some looming questions for open-source if RLHF continues to grow.

*Note: while these rumors make it clear internal search is an interesting opportunity for RLHF, it's a little confusing why no one knows why these models are good at niche data. It seems to me that it is the combination of limited data plus a little bit of fine-tuning on annotations for describing results that give the model this emergent property.👋*

### RLHF Data Problems

[Surge AI](https://www.surgehq.ai/), who actually reached out to sponsor Democratizing Automation \~6 months ago 👋, is becoming the bank of RLHF. They hold the keys to the kingdom by being the first company to offer reliable and high-quality data for RLHF. The only problem is the price. Companies are paying Surge on the order of \$100k to \$1 million to get datasets for specific tasks on RLHF[5](#footnote-5){#footnote-anchor-5 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}. Given the price tag, few of them are actually likely to share.

This data-sharing problem is the coup de grâce for open-source companies this year. The successes of things like Stable Diffusion come because the data is available, e.g. from [LAION](https://laion.ai/blog/laion-5b/). When one pillar of the ML system is removed, the technology takes major steps back.

At HuggingFace, we\'re going to be moving fast to bootstrap other ways to get this data --- community driven and available to all. Without the data, HuggingFace doesn\'t benefit from the RLHF storm brewing in the industry.

This environment around the data is actually quite surprising to me. I would say that most of the last 5 years' breakthrough ML applications have been in curated, scraped datasets. If a company wants to close the gap to OpenAI, it was assumed one could scrape the same data and do the filtering work. Now, data is becoming even more human, so even more costly.

The upside to the data problem of becoming more intentionally human is that we have a stronger opportunity to explore how to match computer values with our own. Anthropic is doing great work in this space with RLHF, it\'s quite impressive. Let\'s continue, as an industry, to make sure the broadest stakeholders are in the loop when we release the super-power models.

*Thanks to [Louis Castricato](https://www.louiscastricato.com/) and friends at [Carper](https://carper.ai/) for supporting my 0 to Ph.D. journey on RLHF. Make sure you subscribe to keep up with it too!*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
I can't say any specifics now, but I'm getting a lot of inbound about application-focused AI companies building teams and putting out ludicrous compensation packages.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
OpenAI thinks it\'ll make \$1 billion in revenue off of it by 2024 (lol).
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Obviously, I think the company will be very successful long term.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[4](#footnote-anchor-4){#footnote-4 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Rumored to only be about 6 billion parameters, so it is by no means a giant like GPT3 or Bloom.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[5](#footnote-anchor-5){#footnote-5 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Note, OpenAI is rumored to have spent \$10 million + on data alone.
:::
::::
