---
title: "GPT4: The quiet parts and the state of ML"
subtitle: "Checking in on the state of the ML field: technical progress, societal implications, and more."
date: 2023-03-20
type: newsletter
audience: everyone
visibility: public
post_id: 109456438.gpt4-review
email_sent_at: 2023-03-20T14:30:20.946Z
---
We all knew GPT4 was coming and a lot of the predictions were true (multimodal, less big of a step as ChatGPT, Bing uses it, etc.). Given the relative change from the announcement is low, the best use of its hype cycle is to zoom in on the details that the Twitfluencers aren\'t discussing and reflect on the bigger picture of the ML industry and large language models.

GPT4 marks a point of transition, as large AI models can capture the same amount of attention as the keynote of a new consumer technology product. With this added attention, the dynamics of progress in AI will change.

This article is primarily about two parts of the post-GPT4 landscape: technical discussion and societal implications (followed by some fun stuff at the end).

![DALL·E 2023-03-16 17.18.31 - An ominous fog lifting from over a futuristic city in the era of artificial general intelligence.png](images/109456438.gpt4-review_06fcd9aa-0868-45da-8b50-279f75f1252b.png)

### Technical impressions

\[The technical report can be found [here](https://cdn.openai.com/papers/gpt-4.pdf)\]

There are a lot of interesting details in the communication around GPT4. Even though the report is a dud from a scientific perspective, it is still way easier to reproduce GPT4 with confirmation that it exists (as opposed to just rumors). That\'ll be happening at a blistering pace. The theme for GPT4 seems to be **exploiting existing infrastructure** to the maximum. My favorite quote that I read about this is that GPT4 was \"mostly trained without instabilities\" (sorry, I couldn\'t re-find the link in the flood). This is truly astonishing because most other people have multiple engineers dedicated to deciphering the nonsense problems that come from training at scale (failed compute nodes, gradient blowups, numerical errors, not improving, etc.).

To make the model more useful for a variety of applications, OpenAI released models with a minimum 8k context length (and up to 32k, with each one being its own model/part of the model, which is quite some \$\$\$, I think). Most open-source models that people are trying to use as OpenChatGPTs have context lengths of 1-2k, which makes it really hard to fit a useful prompt (with multiple task-appropriate examples in it) and the history of a conversation. In our reproduction efforts at HuggingFace, we find things are truncated so frequently and it\'s a bit of a nightmare. The challenge we don\'t know if they overcame: inference cost usually scales linearly with context length.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

With this long context window, it\'s likely that OpenAI has a quiver of prompts it uses for different tasks. The impressive evaluations you\'ve seen on Twitter are notable scientific progress, but the usefulness is up in the air. It\'s possible that every exam given has a separate prompt with full example answers in it for that type of test (e.g. example essays for AP English). Detailing the process of making these prompts and open challenges of reproduction to make it work without prompt engineering is the scientific documentation the field needs. For what it\'s worth, I expect the notion of **prompt engineering to decline** in the coming years. As models get better, there\'s very strong pressure to make them easier to use \-- like the financial pressure of better zero-shot transfer to new tasks \-- and that comes at the expense of prompting. One of my favorite ways this could happen is through the use of techniques like reinforcement learning from human feedback (RLHF).

Beyond these exams, there is very minimal evaluation released. OpenAI is doing some limp open source efforts to trade community work for access to GPT4 with their [evals framework](https://github.com/openai/evals). This stance will take a 180 if they actually release a tool to evaluate all language models with it, but for now, there is nothing that indicates this. Community-wide, OpenAI could really use the goodwill that would come from this. The rest of the standard NLP evaluations are definitely done and not reported.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

The summary of RLHF for this paper is directly from the technical report:

> Our evaluations suggest RLHF does not significantly affect the base GPT-4 model's capability,

This confirms my take that RLHF is a style transfer. I think the sentence above undersells this capacity, though. Style transfer, like prompt engineering, could make **RLHF the key to using these models**, even if they don\'t rate it as a \"significant effect\". This usefulness benefit also comes by reducing harm. The paper states that:

> GPT-4 incorporates an additional safety reward signal during RLHF training to reduce harmful outputs (as defined by our [usage guidelines](https://platform.openai.com/docs/usage-policies/disallowed-usage)).

These two things may be ingredients that mean OpenAI wouldn\'t even be close to releasing the model without RLHF. So, I leave it up to the reader to figure out whether or not RLHF is \"significant\" to OpenAI. I think it is, and they\'re being intentionally vague to mislead.

The fact that \"data\" is the category with the most [contributors](https://openai.com/contributions/gpt-4) is not surprising. The innovations between GPT4 are the things that made GPT3 such a breakthrough, probably 10x'ed. **Clean and vast data is the engine behind GPT4.** The rumors are they finished scraping data from the rest of the internet (likely violating some obvious terms of service like Twitter and books) and 2-4x'ed their computer structure. Back of the envelop calculations on Twitter point to about 25,000 A100 GPUs to train this model. That's a lot, and we'll like get confirmation directionally at Nvidia's developer conference later this week.

One of the key new features of GPT4 is its ability to read images. To start, its optical character recognition (OCR) capabilities are phenomenal. Talking with colleagues in the area, that's only possible if the vision encoder is at least in the 10s of billions parameters order of magnitude, and with an insane resolution (how the data is parsed). It seems likely that they converted some PDFs and treated them as images during training.

The announcement of GPT4 and those future announcements coming for multimodal models are going to get very confusing due to the different ways models can be multimodal. Models can accept images as inputs and / or output images. GPT4 only accepts image inputs (much like [Flamingo](https://arxiv.org/abs/2204.14198), which some of my colleagues are working to reproduce) while some models in the future will in and output images. Other models will be able to seamlessly output images and text from text inputs \-- I was expecting this from GPT4, maybe by natively supporting DALLE-2 as a module.[3](#footnote-3){#footnote-anchor-3 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

These input-output relationships are important for thinking about how the image aspect influences the whole model. Taking in only inputs, GPT4\'s visual capacity amounts to further scene understanding and context. Models that can output both text and images arrive into an awesome niche where you can communicate with the creative tool you are using. I like to visualize the workflow of editing a photo, where you type in a request and it returns the new edited (or generated) photo for you.

Stably expanding the scope of these modalities expands the scope of work one model can do. On the input side, expect to chat with the models like you would with a texting application on a smartphone \-- you can input rich text, images, voice notes, links, etc. As the output window becomes increasingly close to human capabilities it\'ll have to integrate more tools too. The rate of progress on the input side will be faster because (roughly) the need is to add a more complex tokenization scheme to the model. To add another modality to outputs, the entire architecture and training process may need to change.

<div>

------------------------------------------------------------------------

</div>

### Societal implications

This model marks the clear beginning of a new era in Industrial AI. Trade secrets, computing, and products mark the spoken pieces of this era. Unregulated safety claims, insider quid pro quo deals, and propaganda-like communications are left for us to figure out how safe these models really are.

OpenAI's "[System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf)" for the model is actually one of the best resources they released --- a roadmap for anyone looking to red team their own product, but there are a lot of things that went undressed too. One of the things I really don\'t like about the discourse on state-of-the-art chatbots is the use of the term \"jailbreak\". It insinuates that the full capabilities of the models are unlocked and all safety behaviors are removed (if you compare to the historical term jailbreak or its more common usage with hardware technology). A term a colleague has used with me is *lexical attack* as a subset of adversarial attacks. This is exactly what these behaviors are \-- adversarial attacks on the safety filter.

To include one worthwhile example, an early unfiltered version of GPT4 did convince a TaskRabbit to solve a CAPTCHA task for it. I hope that anyone criticizing the release is not criticizing the timeline and thoroughness of claims around what they call \"safety,\" even though I think their definition of safety is limited.

![Image.png](images/109456438.gpt4-review_ba095148-0ac8-49ee-a6ba-8268497c2f14.png)

#### Assessing harms

Throughout the text, the GPT4 paper is hyper-focused on alignment. Some examples include their constant anthropomorphizing of the model, the group that did the "safety" evaluations is [Alignment.org](https://alignment.org) (which is very EA and matches a lot of the core culture of OpenAI leaders), the introduction of extremely unclear qualitative words like *creativity*, and more.

For example, the authors realize they\'re treading a fine line, and proceed anyways:

> We use the term "hallucinations," though we recognize ways this framing may suggest anthropomorphization, which in turn can lead to harms or incorrect mental models of how the model learns.

I\'m not necessarily against all anthropomorphizing of models, but in technical reports, it should be avoided. For example, when Ben Thompson wrote about [his experiences with Sydney](https://stratechery.com/2023/from-bing-to-sydney-search-as-distraction-sentient-ai/), he *decided* to refer to the model as her because that was his experience. Researchers reporting the results should never fall for this fallacy because evaluation is not about experience but rather capabilities.

Finally, the designation of *who* was included in the evaluation of the model is extremely biased to OpenAI\'s perspective. The paper describes the process as engaging with \"experts from domains such as AI alignment risks, cybersecurity, biorisk, trust and safety, and international security\". There are some key things not mentioned, such as ethicists that could challenge some of the modeling assumptions or stakeholders such as teachers who contain some of the highest exposure and immediate disruption.

The hardest part of the harmful discussions for me is the lack of engagement in the bigger picture items, which are mostly political and extremely value-laden. These omitted items would touch on concepts akin to *what is harmful?* For example, all regulation on what can be said to and from the model is based on OpenAI\'s terms of service. In reality, different areas of the country and the world have very different. As these terms of service include the potential to fine-tune a model to refuse \"direct requests for illicit advice,\" where will the topic of abortion fall? Clearly, most of the engineers at OpenAI will feel one way, but the end user could feel differently. What happens here? Getting ahead on these issues and sharing scaffolding for coming challenging situations would be great to see in the coming months (and well before the next election).

#### Studying the ecosystem

With the rate of progress in these language models, there is a substantial need for a body to study, understand, and communicate how these models are shifting power structures in modern society and corrupting information flow. We\'re in the stage where ML model-generated text is going to accelerate the rate of data accumulating on the internet and lower the average quality. This data deluge will degrade trust and user experience across a variety of platforms, increasing pressure on moderation and curation. Combine these trends with accelerating progress in AI and it will be near impossible for one individual to track the changes happening in their own information ecosystem. Having a party to monitor these effects and do experiments across different model providers would be extremely compelling to help audit claims made by all parties (who are eager to impress for the rewards in the stock market).

#### Big tech\'s LLM roundup

All these companies decided that pi day was the right day for their LLM announcements --- I love it. In reality, let me welcome you to the new era where we'll have model keynotes (GPT4\'s is [here](https://www.youtube.com/watch?v=outcGtbnMuQ)). OpenAI is trying to be the Apple of ML, where they take you slide-by-slide through the list of amazing things that only they can do. The problematic truth for them: they don't have hardware-software synergy as a moat, just a little chat interface and a ton of open-source pressure against them.

In the last few weeks, and pi day, we have had LLaMA from Meta, Claude+ from Anthropic, a to-be-shipped PaLM API from Google, and more little things! The exciting week from industry also included Alpaca (another instruction fine-tuning of a smaller model) from Stanford. This is par for the course of what we\'ll hear from industry and academia --- the industry announcing big models and APIs, while academics buzz around looking for small gains in the consumer hardware space. I don't love that this is the balance.

**OpenAI\'s transition**: from here, OpenAI\'s second derivative on fundamental scientific progress relative to the rest of the field will be negative. The even implicit need to supply tools for their multitude of clients will eventually degrade the wonderfully sophisticated research teams they have. Over the next few years, they may seem increasingly far ahead because of momentum, but I think these days are the beginning of the end for their lead.

<div>

------------------------------------------------------------------------

</div>

### The hilarious parts

The technical breakthrough and implications aside, this paper seems like it could\'ve been handled and explained a bit better by OpenAI. Let\'s start with the to-be-meme and famous quote:

> Given both the competitive landscape and the safety implications of large-scale models like GPT-4, this report contains no further details about the architecture (including model size), hardware, training compute, dataset construction, training method, or similar.

Now that we\'re past that, we can touch on other things worth a good hmm 🤔:

-   The paper lists 24 model babysitters (people watching the loss curves almost full-time), while they also claim to have \"mostly stable\" training. Something here doesn\'t check out. A group of 24 loss watchers is bigger than many entire modeling teams in the industry.

-   Regarding model size, the [contributions page](https://openai.com/contributions/gpt-4) is phenomenal. It shows how organization-wide this effort was. I\'m sure people working there are rightfully proud of their work.

-   Top quality GP4 memes are on the menu:

::::::::: {.tweet attrs="{\"url\":\"https://twitter.com/jamesr66a/status/1613306673447473152\",\"full_text\":\"biden reporting on the parameter count of GPT-4 \",\"username\":\"jamesr66a\",\"name\":\"James Reed\",\"date\":\"Wed Jan 11 22:47:39 +0000 2023\",\"photos\":[{\"img_url\":\"https://substackcdn.com/image/upload/w_1028,c_limit,q_auto:best/l_twitter_play_button_rvaygk,w_88/ydghbbgv5q7zvsxibtja\",\"link_url\":\"https://t.co/lTq7x3XO2l\",\"alt_text\":null}],\"quoted_tweet\":{},\"retweet_count\":170,\"like_count\":1556,\"expanded_url\":{},\"video_url\":\"https://video.twimg.com/ext_tw_video/1613306623606521856/pu/vid/640x360/WXvLCJX0NhzRvzO7.mp4?tag=12\",\"belowTheFold\":true}" component-name="Twitter2ToDOM"}
[](https://twitter.com/jamesr66a/status/1613306673447473152){.tweet-link-top target="_blank"}

:::: tweet-header
![Twitter avatar for \@jamesr66a](https://substackcdn.com/image/twitter_name/w_96/jamesr66a.jpg){.tweet-header-avatar loading="lazy"}

::: tweet-header-text
[James Reed ]{.tweet-author-name}[\@jamesr66a]{.tweet-author-handle}
:::
::::

::: tweet-text
biden reporting on the parameter count of GPT-4
:::

::: tweet-video-wrapper
:::

[](https://twitter.com/jamesr66a/status/1613306673447473152){.tweet-link-bottom target="_blank"}

:::: tweet-footer
[10:47 PM ∙ Jan 11, 2023]{.tweet-date}

------------------------------------------------------------------------

::: tweet-ufi
[[1,556]{.like-count}Likes]{.likes href="https://twitter.com/jamesr66a/status/1613306673447473152/likes"}[[170]{.rt-count}Retweets]{.retweets href="https://twitter.com/jamesr66a/status/1613306673447473152/retweets"}
:::
::::
:::::::::

:::::::::: {.tweet attrs="{\"url\":\"https://twitter.com/untitled01ipynb/status/1636638029480706052\",\"full_text\":\"\",\"username\":\"untitled01ipynb\",\"name\":\"LLMeowbooks\",\"date\":\"Fri Mar 17 07:58:08 +0000 2023\",\"photos\":[{\"img_url\":\"https://pbs.substack.com/media/FraBnDEXgAA-Sv1.jpg\",\"link_url\":\"https://t.co/ersi2uTMh0\",\"alt_text\":null}],\"quoted_tweet\":{},\"retweet_count\":43,\"like_count\":366,\"expanded_url\":{},\"video_url\":null,\"belowTheFold\":true}" component-name="Twitter2ToDOM"}
[](https://twitter.com/untitled01ipynb/status/1636638029480706052){.tweet-link-top target="_blank"}

:::: tweet-header
![Twitter avatar for \@untitled01ipynb](https://substackcdn.com/image/twitter_name/w_96/untitled01ipynb.jpg){.tweet-header-avatar loading="lazy"}

::: tweet-header-text
[LLMeowbooks ]{.tweet-author-name}[\@untitled01ipynb]{.tweet-author-handle}
:::
::::

::: tweet-text
:::

:::: {.tweet-photos-container .one}
::: tweet-photo-wrapper
![Image](https://pbs.substack.com/media/FraBnDEXgAA-Sv1.jpg){.tweet-photo loading="lazy"}
:::
::::

[](https://twitter.com/untitled01ipynb/status/1636638029480706052){.tweet-link-bottom target="_blank"}

:::: tweet-footer
[7:58 AM ∙ Mar 17, 2023]{.tweet-date}

------------------------------------------------------------------------

::: tweet-ufi
[[366]{.like-count}Likes]{.likes href="https://twitter.com/untitled01ipynb/status/1636638029480706052/likes"}[[43]{.rt-count}Retweets]{.retweets href="https://twitter.com/untitled01ipynb/status/1636638029480706052/retweets"}
:::
::::
::::::::::

The influencers really lost the plot with this one. I thoroughly enjoyed some simultaneous nonsense on my LinkedIn feed:

![Image.png](images/109456438.gpt4-review_57f36ce1-2f54-4b27-953c-f8ed327340f9.png)

<div>

------------------------------------------------------------------------

</div>

#### Wrap up

Let me know if there\'s anything you think I missed. All in all, it\'s great for the field of AI that GPT4 is finally released. The pressure in the field is pushing more people to extremes. I think I\'m currently most annoyed with the science-washing of the release. It\'s fine to release the paper, but putting a non-acceptable paper on Arxiv to cultivate citations is pretty annoying.

Do you like the format of release-summary posts? I think GPT4 is an obvious one for how it captures so many unfolding dynamics in the ML industry at one timestamp, but it could be a fun medium for future models we have coming this year.

<div>

------------------------------------------------------------------------

</div>

*Elsewhere from me:*

-   *I gave a more up-to-date [talk on RLHF](https://www.youtube.com/watch?v=8SgKDSX-Me0) at the UCL DARK lab \-- check it out!* 

-   *I shared the [doc](https://www.craft.do/s/WaF8mlClNnheaM) I use for my developer environment (the commands we always forget).*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Claude, as of a few months ago, also had an 8k context length.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Here\'s another [interesting note](https://twitter.com/cHHillee/status/1635790330854526981?s=20) on the time-sensitivity of evals.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[3](#footnote-anchor-3){#footnote-3 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
This was speculation that is technically extremely challenging.
:::
::::
