---
title: "Automating code, Twitter's hack(s), a robot named Stretch"
subtitle: "Language models write code, Twitter gets hacked (again), new robots, and top-tier conferences. "
date: 2020-07-17
type: newsletter
audience: everyone
visibility: public
post_id: 714611.automating-code-twitters-hacks-a
email_sent_at: 2020-07-17T13:00:56.303Z
---
# Automating Code

Check out this video for the first compelling demonstration of automated software generation I have seen.

:::::::: {#youtube2-Q5zI-huca3Y .youtube-wrap attrs="{\"videoId\":\"Q5zI-huca3Y\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=Q5zI-huca3Y){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

#### **What is it**

OpenAI's newest language processing model GPT-3 (Generative Pretrained Transformer) creating a variety of front-end code snippets from two example snippets. (*Front-end code is code that renders on a website, and is often repeated in chunks to get variations of the same designs, hence why it is an easy initial target for automation).*

You can engage with the author of the tool [here](https://twitter.com/sharifshameem/status/1283322990625607681) (Twitter). You can [find a collection of more creative examples here](https://towardsdatascience.com/gpt-3-creative-potential-of-nlp-d5ccae16c1ab), or another code generation example [here](https://twitter.com/hturan/status/1282261783147958272). One I particularly liked was written [creative fiction](https://www.gwern.net/GPT-3) or a written [auto-generated game](https://play.aidungeon.io/) on the last generation of the model.

#### How this works

The language model "Generative Pretrained Transformer" uses a new p[ay-to-play API from OpenAI](https://openai.com/blog/openai-api/). Here is an excerpt on NLP and Transformers from my post ([AI & Arbitration of Truth](https://democraticrobots.substack.com/p/ai-arbitration-of-truth-808b57a93a97) - which seems to need to be revisited every week).

> ##### **The Tech --- Transformers & NLP**
>
> Natural Language Processing (NLP) is the subfield of machine learning concerned with manipulating and extracting information from text. [It's used in smart assistants, translators, search engines, online stores, and more.](https://en.wikipedia.org/wiki/Natural_language_processing) NLP (along with computer vision) is one of a few monetized state-of-the-art machine learning developments. *It's the candidate for being used to interpret truth.*
>
> The best NLP tool to date is a neural network architecture called **the transformer**. Long story short, transformers use an [encoder and decoder structure](https://towardsdatascience.com/understanding-encoder-decoder-sequence-to-sequence-model-679e04af4346) that encodes words to a latent space, and decodes to a translation, typo fix, or classification (*you can think of an encoder-decoder as compressing a complicated feature space to a simpler space via a neural network --- nonlinear function approximation)*. A key tool in the NLP space is something called [Attention](https://medium.com/@joealato/attention-in-nlp-734c6fa9d983) that learns which words to focus on and for how long (rather than hard coding it into an engineered system).
>
> A [transformer](https://arxiv.org/pdf/1810.04805.pd) combines these tools, and a couple other advancements that allows the models to be trained efficiently in parallel. Below is a diagram showing how data flows through a transformer.
>
> ![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/147d65bd-cc0a-4539-aa08-788805eb23be_678x830.png)
>
> A visualization from an [awesome tutorial](https://jalammar.github.io/illustrated-transformer/) I found.

#### **Why it matters**

This is the first application I have seen where people could use this to replace engineering time. Front-end designers can drastically increase their speed with this tool. This will likely be sold to many existing companies, and new businesses will be using it in the future to create valuable services. It takes a creative person to find the best applications, is certainly limited by us human designers, and will soon be replaced by the next state-of-the-art model \[[More](https://www.theverge.com/2020/6/11/21287966/openai-commercial-product-text-generation-gpt-3-api-customers)\].

This is eye-raising for more reasons because of [OpenAI's famous charter](https://openai.com/charter/). In short - we will work towards AGI, and if another company looks to be getting there first, ***we will join them***. The claim behind this product is that the funds will help them execute AI research, but their leadership has in the past withdrawn models out of fear that they are "too dangerous to share." **This fine-line of AI danger will only get sharper.**

Nerd corner: The training amount for this model was 50 [peta](https://en.wikipedia.org/wiki/Peta-#:~:text=Peta%20(%2F%CB%88p%C9%9Bt,%CF%80%CE%AD%CE%BD%CF%84%CE%B5%2C%20meaning%20%22five%22.)[flop/s](https://en.wikipedia.org/wiki/FLOPS#:~:text=In%20computing%2C%20floating%20point%20operations,than%20measuring%20instructions%20per%20second.)-days (what exactly does this mean?) amounts to over \$12million for training costs alone \[[Source](https://venturebeat.com/2020/06/11/openai-launches-an-api-to-commercialize-its-research/#:~:text=Certainly%2C%20OpenAI's%20advancements%20haven't,training%20costs%20exceeding%20%2412%20million.)\]. That's a bit of a cost to recoup in fees. I like to think about how this model compares to the shallow neural networks I use for regression tasks - *it's over 100million times the number of parameters*. That is a totally different regime of function approximation. For the nerdy-nerds, the academic paper is [here](https://arxiv.org/abs/2005.14165).

### Robotics & Generative Text

I requested access to the beta for robotics research. I am interested to see what level of planning a language model (big neural network) can achieve given context in the form of a game. ***Does language capture the basic intent in a game and the structure of a solution?***

Longer term I think language integration into robotic rewards is of interest - it will allow humans who work with the robots to give the machines verbal tasks (verification of said tasks is a problem for another day).

Examples:

-   *Given an embedding of a game board (written, grid, other methods), say "where should I move."*

-   *Given a description of an environment: "the block is on the ball which is to the right of the chair," ask "is the ball above the chair?"*

This is a very rudimentary example, but I think links from commercialized machine learning fields such as deep learning for vision and language are high potential.

<div>

------------------------------------------------------------------------

</div>

# Twitter's Hack

:::::::: {.tweet attrs="{\"url\":\"https://twitter.com/TwitterSupport/status/1283591846464233474?s=20\",\"full_text\":\"We detected what we believe to be a coordinated social engineering attack by people who successfully targeted some of our employees with access to internal systems and tools.\",\"username\":\"TwitterSupport\",\"name\":\"Twitter Support\",\"date\":\"Thu Jul 16 02:38:38 +0000 2020\",\"photos\":[],\"quoted_tweet\":{},\"retweet_count\":6053,\"like_count\":12127,\"expanded_url\":{},\"video_url\":null,\"belowTheFold\":true}" component-name="Twitter2ToDOM"}
[](https://twitter.com/TwitterSupport/status/1283591846464233474?s=20){.tweet-link-top target="_blank"}

:::: tweet-header
![Twitter avatar for \@TwitterSupport](https://substackcdn.com/image/twitter_name/w_96/TwitterSupport.jpg){.tweet-header-avatar loading="lazy"}

::: tweet-header-text
[Twitter Support ]{.tweet-author-name}[\@TwitterSupport]{.tweet-author-handle}
:::
::::

::: tweet-text
We detected what we believe to be a coordinated social engineering attack by people who successfully targeted some of our employees with access to internal systems and tools.
:::

[](https://twitter.com/TwitterSupport/status/1283591846464233474?s=20){.tweet-link-bottom target="_blank"}

:::: tweet-footer
[2:38 AM ∙ Jul 16, 2020]{.tweet-date}

------------------------------------------------------------------------

::: tweet-ufi
[[12,127]{.like-count}Likes]{.likes href="https://twitter.com/TwitterSupport/status/1283591846464233474?s=20/likes"}[[6,053]{.rt-count}Retweets]{.retweets href="https://twitter.com/TwitterSupport/status/1283591846464233474?s=20/retweets"}
:::
::::
::::::::

#### What you need to know:

A summary of the extent from the [Wall Street Journal](https://www.wsj.com/articles/twitter-accounts-of-bill-gates-jeff-bezos-elon-musk-appear-to-have-been-hacked-11594849077?utm_source=Memberful&utm_campaign=82ce71cb8c-daily_update_2020_07_16&utm_medium=email&utm_term=0_d4c7fece27-82ce71cb8c-111375504):

> Twitter Inc. was hit with a widespread attack Wednesday that allowed hackers to take over an array of accounts including those of celebrities, politicians and billionaires such as Bill Gates, Kanye West, Joe Biden and Barack Obama, as well as Apple Inc. and other companies. The attack, which security experts called the most significant hacking incident in Twitter's history, began before 4 p.m. EDT, when compromised accounts --- many of them related to the digital currency bitcoin --- began posting messages requesting money be sent to cryptocurrency accounts. The attacks quickly spread to additional, more prominent accounts, with the bogus messages sometimes receiving thousands of likes before they were taken down, only to be posted again a short time later, sometimes on the same account.
>
> ...the company took the extraordinary step of limiting posts from verified accounts with blue check marks, which Twitter generally designates for more prominent users. Twitter, late Wednesday, said it believed the hackers perpetrated the attack by targeting employees who had access to the company's internal systems and tools.

[Vice](https://www.vice.com/en_us/article/jgxd3d/twitter-insider-access-panel-account-hacks-biden-uber-bezos?utm_source=Memberful&utm_campaign=82ce71cb8c-daily_update_2020_07_16&utm_medium=email&utm_term=0_d4c7fece27-82ce71cb8c-111375504) reported the method could have been bribery:

> A Twitter insider was responsible for a wave of high profile account takeovers on Wednesday, according to leaked screenshots obtained by Motherboard and two sources who took over accounts..." We used a rep that literally done all the work for us," one of the sources told Motherboard. The second source added they paid the Twitter insider. Motherboard granted the sources anonymity to speak candidly about a security incident.
>
> A Twitter spokesperson told Motherboard that the company is still investigating whether the employee hijacked the accounts themselves or gave hackers access to the tool. The accounts were taken over using an internal tool at Twitter, according to the sources, as well as screenshots of the tool obtained by Motherboard.

#### A history of Twitter blips

Twitter doesn't have the best history in security. In [2017](https://techcrunch.com/2017/11/29/meet-the-man-who-deactivated-trumps-twitter-account/) a contractor (non full-time employee) deactivated Trumps account for a few minutes (it is suggested his account has [new protections](https://www.nytimes.com/2017/11/03/technology/trump-twitter-deleted.html)), and in [2019](https://www.washingtonpost.com/national-security/former-twitter-employees-charged-with-spying-for-saudi-arabia-by-digging-into-the-accounts-of-kingdom-critics/2019/11/06/2e9593da-00a0-11ea-8bab-0fc209e065a8_story.html) it was found that employees accessed info on Saudi Arabian dissidents.

These issues come down to the fact that employees have access to internal data (common practice in technology industry), and that is going to change.

### Geopolitical and Automation Implications

Many social media companies operate on the following personnel assumption:

> The few bad apples are going to be outweighed by the dramatic majority of happy employees.

This is not the case with how information travels and exponentiates on the internet. One bad employee can cause a lot of damage, so we are going to see changes in the future. The "damage" exposed by the hackers so far was \~\$100,000 in bitcoin, but there could be a lot of leverage cash downstream from the rumored collection of all Twitter content which includes private messages.

I think this Twitter breach will be the **landmark case** in a new set of **regulation** on a) who can access sensitive data at these companies and b) how they do so. Well, the government likely should regulate both, but getting one would be a good starting point. Multiple companies have a 0 strike policy on data-infractions, but when the 0th strike's cost can be limited by the creativity of the hacker, that is a big downside.

When a "social engineering attack" has the potential to de-stabalize the geopolitical order (think, the President). It really fits the trend of how cyber-warfare will define our next decades. It's weird to think most companies will be in a warfare state behind the scenes, but the public only will know when there's a landed strike. Both sides of this war will be automated (and scary).

<div>

------------------------------------------------------------------------

</div>

# 'Snacks'

The snacks section of my post is in-between a full analysis and more relevant than "I listened to this." This week we have a [launch of a fun new robot](https://hello-robot.com/), multiple high-profile [robotics](https://roboticsconference.org/) and [AI](https://icml.cc/) conferences, and more.

#### Stretch, the robot

Some [Xooglers](https://xoogler.co/) (ex-Googlers) have created a company called [Hello Robotics](https://hello-robot.com/) and introduced their new robot, Stretch. Stretch is designed to be simple and useful for multiple tasks. It is lean, cheap, durable, and sensor-packed. And it comes with cute advertising, below. \[[More](https://spectrum.ieee.org/automaton/robotics/home-robots/hello-robots-stretch-mobile-manipulator)\]

![200123_HELLO_ROBOT_LK05-0524_Banner.jpg](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/4cdf8578-f192-4fde-81df-fc308e67afb8_1500x527.jpeg)

It's interesting to note that this company has opted out of VC funding (most likely). Dry-powder at venture capital firms is at an all-time high right now and investments into automation have been growing exponentially ([the few signals we have seem to say](https://democraticrobots.substack.com/p/10-years-of-automation-in-1-year)). What this means is they have a specific market in mind, don't want the added platforms that VC can offer, and / or no need for money.

It's really sparse when it comes to in-depth, operational reporting on robotics startups these days. I think that these robots will be acquired by researchers to start with due to the cheap price tag and functional approach. Anywho, it's of note to see more players in the area. Within 5 years people in Silicon Valley will probably be buying (expensive) robots for their homes (markup is due to software), so give it another decade to trickle down into everyone else.

:::::::: {#youtube2-2msVU0ygrqM .youtube-wrap attrs="{\"videoId\":\"2msVU0ygrqM\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=2msVU0ygrqM){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

Could they be trying to replicate this video (from 2004) below? Do you think this robot is autonomous? Just adding the famous history-point in some robotics circles.

:::::::: {#youtube2-jJ4XtyMoxIA .youtube-wrap attrs="{\"videoId\":\"jJ4XtyMoxIA\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
[Try watching this video on www.youtube.com](https://www.youtube.com/watch?v=jJ4XtyMoxIA){target="_blank"}, or enable JavaScript if it is disabled in your browser.
:::
::::
::::::
:::::::
::::::::

The catch is that there was a human running it and it's sped up 8x. Hopefully having cheaper platforms helps us get to true home-autonomy. Although, [a famous robotics researcher has rented Airbnb's to collect home-training data](https://www.wired.com/story/robots-are-renting-airbnbs-to-get-a-better-grip/).

[](https://substackcdn.com/image/fetch/$s_!RsMm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3ac8b85-09ec-466f-ba4c-0962ba87d893_2112x1243.png){.image-link .image2 .is-viewable-img component-name="Image2ToDOM" target="_blank"}

::::::: image2-inset
![Image for post](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/a3ac8b85-09ec-466f-ba4c-0962ba87d893_2112x1243.png "Image for post"){.sizing-normal attrs="{\"src\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/a3ac8b85-09ec-466f-ba4c-0962ba87d893_2112x1243.png\",\"srcNoWatermark\":null,\"fullscreen\":null,\"imageSize\":null,\"height\":857,\"width\":1456,\"resizeWidth\":null,\"bytes\":null,\"alt\":\"Image for post\",\"title\":null,\"type\":null,\"href\":null,\"belowTheFold\":true,\"topImage\":false,\"internalRedirect\":null,\"isProcessing\":false,\"align\":null,\"offset\":false}" height="857" loading="lazy" sizes="100vw" srcset="https://substackcdn.com/image/fetch/$s_!RsMm!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3ac8b85-09ec-466f-ba4c-0962ba87d893_2112x1243.png 424w, https://substackcdn.com/image/fetch/$s_!RsMm!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3ac8b85-09ec-466f-ba4c-0962ba87d893_2112x1243.png 848w, https://substackcdn.com/image/fetch/$s_!RsMm!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3ac8b85-09ec-466f-ba4c-0962ba87d893_2112x1243.png 1272w, https://substackcdn.com/image/fetch/$s_!RsMm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3ac8b85-09ec-466f-ba4c-0962ba87d893_2112x1243.png 1456w" width="1456"}

:::::: image-link-expand
::::: {.pencraft .pc-display-flex .pc-gap-8 .pc-reset}
::: {.pencraft .pc-reset .icon-container .restack-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1yZWZyZXNoLWN3IiBmaWxsPSJub25lIiBoZWlnaHQ9IjIwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zIDEyYTkgOSAwIDAgMSA5LTkgOS43NSA5Ljc1IDAgMCAxIDYuNzQgMi43NEwyMSA4IiAvPjxwYXRoIGQ9Ik0yMSAzdjVoLTUiIC8+PHBhdGggZD0iTTIxIDEyYTkgOSAwIDAgMS05IDkgOS43NSA5Ljc1IDAgMCAxLTYuNzQtMi43NEwzIDE2IiAvPjxwYXRoIGQ9Ik04IDE2SDN2NSIgLz48L3N2Zz4=){.lucide .lucide-refresh-cw}
:::

::: {.pencraft .pc-reset .icon-container .view-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1tYXhpbWl6ZTIiIGZpbGw9Im5vbmUiIGhlaWdodD0iMjAiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgdmlld2JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBvbHlsaW5lIHBvaW50cz0iMTUgMyAyMSAzIDIxIDkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIHBvaW50cz0iOSAyMSAzIDIxIDMgMTUiPjwvcG9seWxpbmU+PGxpbmUgeDE9IjIxIiB4Mj0iMTQiIHkxPSIzIiB5Mj0iMTAiPjwvbGluZT48bGluZSB4MT0iMyIgeDI9IjEwIiB5MT0iMjEiIHkyPSIxNCI+PC9saW5lPjwvc3ZnPg==){.lucide .lucide-maximize2}
:::
:::::
::::::
:::::::

#### Self-supervised Robots

This week has been the [Robotics: Science and Systems Conference](https://roboticsconference.org/) and the [Conference on Machine Learning](https://icml.cc/). I have been spending most of my time on the robotics side of the coin, and decided to learn something new. I went to the workshop on Self-Supervised Learning (which had an impressive lineup) to learning something new.

Self-supervised learning is the idea that we can get robots to explore and label their own data. The huge potential upside here in the age of lockdowns is: **no human oversight needed**. Right now, the robots don't learn any advanced behaviors like stacking objects into shapes, but they can learn to grasp and manipulate objects (or walk). This is a very young field that I will keep my eye on. It is the curiosity side of robotic learning, and I want to see more on the lifelong side of things (improvements to peak performance over control theory).

:::::::: {#youtube2-VY4oaRIkzqI .youtube-wrap attrs="{\"videoId\":\"VY4oaRIkzqI\",\"startTime\":null,\"endTime\":null}" component-name="Youtube2ToDOM"}
::::::: youtube-inner
:::::: iframe
::: {#player}
:::

:::: player-unavailable
# An error occurred. {#an-error-occurred. .message}

::: submessage
Unable to execute JavaScript.
:::
::::
::::::
:::::::
::::::::

[Here are my notes from the workshop,](https://medium.com/@natolambert/self-supervised-learning-for-robotics-1647205e9dea) and many nice slide screenshots - thanks Zoom.

#### Multiple levels to recommender systems

I am doing some research on how recommender systems effect more actions then intended in design, and I came across a related paper today - "[What are you optimizing for? Aligning Recommender Systems with Human Values](https://participatoryml.github.io/papers/2020/42.pdf)." This diagram takes it another step of the way - unintended consequences in groups effected by those actions. It is yet another trend in people realizing *when optimizing a reward function in machine learning there will always be unmeasured effects.*

Please subscribe if you want to see the issue analyzing ethics of [recommender systems](https://en.wikipedia.org/wiki/Recommender_system#:~:text=A%20recommender%20system%2C%20or%20a,would%20give%20to%20an%20item.) (these things are in so many major products like Netflix, online-shopping, and more). The diagram below is from the paper's presentation.

[](https://substackcdn.com/image/fetch/$s_!HABw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22802e45-c7e7-4b2a-99f3-a449fba3f158_1732x1076.png){.image-link .image2 .is-viewable-img component-name="Image2ToDOM" target="_blank"}

::::::: image2-inset
![Image](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/22802e45-c7e7-4b2a-99f3-a449fba3f158_1732x1076.png "Image"){.sizing-normal attrs="{\"src\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/22802e45-c7e7-4b2a-99f3-a449fba3f158_1732x1076.png\",\"srcNoWatermark\":null,\"fullscreen\":null,\"imageSize\":null,\"height\":905,\"width\":1456,\"resizeWidth\":null,\"bytes\":null,\"alt\":\"Image\",\"title\":null,\"type\":null,\"href\":null,\"belowTheFold\":true,\"topImage\":false,\"internalRedirect\":null,\"isProcessing\":false,\"align\":null,\"offset\":false}" height="905" loading="lazy" sizes="100vw" srcset="https://substackcdn.com/image/fetch/$s_!HABw!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22802e45-c7e7-4b2a-99f3-a449fba3f158_1732x1076.png 424w, https://substackcdn.com/image/fetch/$s_!HABw!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22802e45-c7e7-4b2a-99f3-a449fba3f158_1732x1076.png 848w, https://substackcdn.com/image/fetch/$s_!HABw!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22802e45-c7e7-4b2a-99f3-a449fba3f158_1732x1076.png 1272w, https://substackcdn.com/image/fetch/$s_!HABw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F22802e45-c7e7-4b2a-99f3-a449fba3f158_1732x1076.png 1456w" width="1456"}

:::::: image-link-expand
::::: {.pencraft .pc-display-flex .pc-gap-8 .pc-reset}
::: {.pencraft .pc-reset .icon-container .restack-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1yZWZyZXNoLWN3IiBmaWxsPSJub25lIiBoZWlnaHQ9IjIwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zIDEyYTkgOSAwIDAgMSA5LTkgOS43NSA5Ljc1IDAgMCAxIDYuNzQgMi43NEwyMSA4IiAvPjxwYXRoIGQ9Ik0yMSAzdjVoLTUiIC8+PHBhdGggZD0iTTIxIDEyYTkgOSAwIDAgMS05IDkgOS43NSA5Ljc1IDAgMCAxLTYuNzQtMi43NEwzIDE2IiAvPjxwYXRoIGQ9Ik04IDE2SDN2NSIgLz48L3N2Zz4=){.lucide .lucide-refresh-cw}
:::

::: {.pencraft .pc-reset .icon-container .view-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1tYXhpbWl6ZTIiIGZpbGw9Im5vbmUiIGhlaWdodD0iMjAiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgdmlld2JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBvbHlsaW5lIHBvaW50cz0iMTUgMyAyMSAzIDIxIDkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIHBvaW50cz0iOSAyMSAzIDIxIDMgMTUiPjwvcG9seWxpbmU+PGxpbmUgeDE9IjIxIiB4Mj0iMTQiIHkxPSIzIiB5Mj0iMTAiPjwvbGluZT48bGluZSB4MT0iMyIgeDI9IjEwIiB5MT0iMjEiIHkyPSIxNCI+PC9saW5lPjwvc3ZnPg==){.lucide .lucide-maximize2}
:::
:::::
::::::
:::::::

<div>

------------------------------------------------------------------------

</div>

[](https://substackcdn.com/image/fetch/$s_!9Ydi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42f4f5c-b7da-43e4-ab2a-7b7aa53d364d_1256x625.jpeg){.image-link .image2 .is-viewable-img component-name="Image2ToDOM" target="_blank"}

::::::: image2-inset
![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/f42f4f5c-b7da-43e4-ab2a-7b7aa53d364d_1256x625.jpeg){.sizing-normal attrs="{\"src\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/f42f4f5c-b7da-43e4-ab2a-7b7aa53d364d_1256x625.jpeg\",\"srcNoWatermark\":null,\"fullscreen\":null,\"imageSize\":null,\"height\":625,\"width\":1256,\"resizeWidth\":null,\"bytes\":275225,\"alt\":null,\"title\":null,\"type\":\"image/jpeg\",\"href\":null,\"belowTheFold\":true,\"topImage\":false,\"internalRedirect\":null,\"isProcessing\":false,\"align\":null,\"offset\":false}" height="625" loading="lazy" sizes="100vw" srcset="https://substackcdn.com/image/fetch/$s_!9Ydi!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42f4f5c-b7da-43e4-ab2a-7b7aa53d364d_1256x625.jpeg 424w, https://substackcdn.com/image/fetch/$s_!9Ydi!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42f4f5c-b7da-43e4-ab2a-7b7aa53d364d_1256x625.jpeg 848w, https://substackcdn.com/image/fetch/$s_!9Ydi!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42f4f5c-b7da-43e4-ab2a-7b7aa53d364d_1256x625.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!9Ydi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff42f4f5c-b7da-43e4-ab2a-7b7aa53d364d_1256x625.jpeg 1456w" width="1256"}

:::::: image-link-expand
::::: {.pencraft .pc-display-flex .pc-gap-8 .pc-reset}
::: {.pencraft .pc-reset .icon-container .restack-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1yZWZyZXNoLWN3IiBmaWxsPSJub25lIiBoZWlnaHQ9IjIwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zIDEyYTkgOSAwIDAgMSA5LTkgOS43NSA5Ljc1IDAgMCAxIDYuNzQgMi43NEwyMSA4IiAvPjxwYXRoIGQ9Ik0yMSAzdjVoLTUiIC8+PHBhdGggZD0iTTIxIDEyYTkgOSAwIDAgMS05IDkgOS43NSA5Ljc1IDAgMCAxLTYuNzQtMi43NEwzIDE2IiAvPjxwYXRoIGQ9Ik04IDE2SDN2NSIgLz48L3N2Zz4=){.lucide .lucide-refresh-cw}
:::

::: {.pencraft .pc-reset .icon-container .view-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1tYXhpbWl6ZTIiIGZpbGw9Im5vbmUiIGhlaWdodD0iMjAiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgdmlld2JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBvbHlsaW5lIHBvaW50cz0iMTUgMyAyMSAzIDIxIDkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIHBvaW50cz0iOSAyMSAzIDIxIDMgMTUiPjwvcG9seWxpbmU+PGxpbmUgeDE9IjIxIiB4Mj0iMTQiIHkxPSIzIiB5Mj0iMTAiPjwvbGluZT48bGluZSB4MT0iMyIgeDI9IjEwIiB5MT0iMjEiIHkyPSIxNCI+PC9saW5lPjwvc3ZnPg==){.lucide .lucide-maximize2}
:::
:::::
::::::
:::::::

### **The tangentially related**

I am reading (newsletters/blogs):

-   [An article that summarizes well why I went to](https://www.adamkeesling.com/blog/explaining-a16zs-investment-in-substack) [Substack](https://substack.com/). The only problem for me is that I don't have a strong followership to begin with, but I am abiding by the philosophy that consistent quality will build it. *Help me build this community.*

-   [More press along the core theme of this blog](https://www.technologyreview.com/2020/06/24/1004432/ai-help-crisis-new-kind-ethics-machine-learning-pandemic/): we need better and new AI ethics.

-   [A local's view on how Hong Kong is "impossible."](https://www.nytimes.com/2020/07/13/opinion/hong-kong-national-security-law.html) Ever since visiting in November of 2019, I have been following HK closely. It looks like going back will be increasingly risky or different.

Books:

-   *Human Compatible: Artificial Intelligence and the Problem of Control* - Stuart Russell and *Race After Technology: Abolitionist Tools for the New Jim Code* - Ruha Benjamin raise different problems with a "standard model" in AI. A **standard model** would be a formulation of **agent A** optimizes **set object R**. This is problematic because a single-minded agent may exploit other avenues (at the risk of humans). Continuing this, there will be issues when assuming any moral / societal structure in an equality-focused AI method. We need curious methods, not set methods - post on rethinking robot (and AI agent) design is in the works.

I am listening to / watching:

-   [A super fun lecture on F22 Raptor design, usability, and control.](https://www.youtube.com/watch?time_continue=1&v=Evhrk5tY-Yo&feature=emb_logo)

-   [A hair cut robot on Youtube.](https://youtu.be/7zBrbdU_y0s)

<div>

------------------------------------------------------------------------

</div>

Hopefully you find some of this interesting and fun. You can find more about the author [here](http://www.natolambert.me/). Forwarded this? [Subscribe here](https://democraticrobots.substack.com/). It helps me a lot to forward this to interested parties, are Tweet at me [\@natolambert](https://twitter.com/natolambert). I write to learn and converse.
