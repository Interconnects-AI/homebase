---
title: "Frontiers in synthetic data"
subtitle: "Trends in synthetic data that I'm watching closely in the leading open and closed models."
date: 2024-06-21
type: newsletter
audience: everyone
visibility: public
post_id: 145870222.frontiers-in-synthetic-data
email_sent_at: 2024-06-21T16:05:41.503Z
---
*On the [most recent episode of The Retort](https://retortai.com/episodes/apple-sends-a-memo-to-the-agi-faithful), Tom and I debate the two views of intelligence presented by Apple and Leopold's Situational Awareness memo.*

**Edit Jun 21:** *added more details on Gemini Flash's distillation and datasets trying to dethrone UltraFeedback.*

**Edit Jun 27:** *added an explanation for how on-policy distillation works from Lewis at HuggingFace.*

<div>

------------------------------------------------------------------------

</div>

Synthetic data is known to be a super powerful tool for every level of the language modeling stack. It's documented as being used for [expanding vanilla pretraining data](https://arxiv.org/abs/2401.16380) and [creating large swaths of fine-tuning data](https://arxiv.org/abs/2406.11704v1). Many, many more rumors surround its use: [Anthropic's pretraining-scale constitutional AI](https://www.interconnects.ai/p/llm-synthetic-data), Mistral AI's first models being pretrained on OpenAI outputs, [Q-star](https://www.interconnects.ai/p/q-star)'s hopes as OpenAI's remaining moat, and much more. The diversity of use cases for synthetic data makes planning around the role of synthetic data in solving specific goals.

In a new project, I'm focusing on the tasks of taking a strong open weights model and using synthetic data to create as strong of a fine-tune as possible. I think synthetic data can do almost all of the work. This model is not expected to meaningfully beat any of the "frontier" models from the likes of Google, Anthropic, and OpenAI. It's a question of how can we use synthetic data to quickly close the gap and make very strong models where all parts of the pipeline are openly available.

In thinking about this, I've clarified a lot of my thoughts about what companies are probably doing with synthetic data. Particularly, I focus on the things that the academic literature is likely missing, along with commentary on all the latest models from Gemini Flash, Nemotron 340B, Llama 3, Claude 3.5, and all the like.

![](images/145870222.frontiers-in-synthetic-data_54b6c30f-f902-4d00-8062-79e19f884958.png)

### 1. Direct distillation is still king

This distillation phase is a window of time we have only been in for a short period! The model [Zephyr-Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) really brought this into gear, and the [paper](https://arxiv.org/abs/2310.16944) really brought this distillation idea to the forefront with the title. Still, many popular datasets use completions from many models in the learning process, such as Alpaca and Koala that are definitely not good at even these simple tasks.

It is intuitively obvious that there are some tasks that will be easier than others to solve with synthetic data. On most open-ended generation queries like "write me an email" or "summarize this text," models like GPT-4 do remarkably well. Most evaluations people start with really focus on this type of data. Even tasks like MT-Bench or AlpacaEval that include a good amount of math or code samples will be most impacted by the base generative quality due to general judgments.

On tasks with complicated math or code, the best available models still fail wildly with semi-popular libraries like HuggingFace Datasets. Copying this with synthetic data at least will take much more effort.

The former tasks are easy to improve with synthetic data while the latter is extremely hard.

Many datasets out there are "created with GPT-4," but this used a form of GPT-4 that is now 100+ points behind on LMSYS's ChatBotArena leaderboard. 100 points on the overall leaderboard is the delta from the current GPT-4o to the first GPT-4 version. This is a big gap! 100 points below the original GPT-4 is Llama-2-chat-70B, which was known to be a very disliked model. This just goes to show that simply regenerating with an updated model can have a huge effect.

Beyond this, it's largely unknown which models are best for which tasks, but surely the answer is not to always use the same GPT-4 model variant with the same sampling parameters (temperature, top-k, system prompt, etc.).

### 2. Are Gemini Flash and Claude Haiku distilled?

Gemini Flash and Claude Haiku are becoming the most coveted model endpoints for many developers building applications with language models due to their speed and low price. Tea leaf signs point to these potentially being based on some form of distillation (similar to above) rather than being trained from scratch. The biggest clue I have is papers like *[On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649)* whi*c*h the lead author even claims is his "[most impactful product work](https://x.com/agarwl_/status/1796630121706590321)" at Google. The models of bigger sizes, such as Claude 3.5 Sonnet or Gemini Pro / Ultra, seem to be models trained from scratch (with other contributions of synthetic data).

Google has [other work in this area](https://research.google/blog/distilling-step-by-step-outperforming-larger-language-models-with-less-training-data-and-smaller-model-sizes/), but in general distillation of this style is a [flourishing area of work](https://arxiv.org/abs/2402.13116). Anthropic is much quieter, but the rumor mill around their use of synthetic data is very strong.

***Edit: Gemini Flash is confirmed as distilled**.* The [updated report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf) states that Flash is a dense model distilled from Pro, which is an MoE.

> Gemini 1.5 Flash is a dense Transformer based model that is online distilled (Anil et al., 2018; Beyer et al., 2021; Bucila et al., 2006; Hinton et al., 2015) from Gemini 1.5 Pro.

Roughly, the bigger model is being trained and the smaller, distilled model is updated to reflect this with simultaneous training. [Thanks to Omar from HuggingFace for the note](https://x.com/osanseviero/status/1792165802717675802). Here's [an older paper](https://arxiv.org/abs/1804.03235) that could point to more about what they're doing. To me, this seems like something Anthropic and Google have, but OpenAI may not have cracked.

Here's a [good](https://x.com/_lewtun/status/1806429923491623055) **[short](https://x.com/_lewtun/status/1806429923491623055)** [read](https://x.com/_lewtun/status/1806429923491623055) on how on-policy distillation works.

### 3. Filtering prevents collapse

Right now the most popular research direction for alignment techniques is some form of iterative direct preference optimization algorithm. These papers, the first of which was *[Self Rewarding Language Models](https://arxiv.org/abs/2401.10020)* often tout a little bit absurd vibes-based evaluation scores (e.g. AlpacaEval). I'm not going to list all of them here, but directionally they are all relabeling or regenerating the same dataset to then apply the same alignment method to the model. This creation of iterations is inspired by the "online" nature of the other side of algorithms based on Proximal Policy Optimization (PPO). [A lot of discussions point to the "online" nature of PPO being key for its performance](https://www.interconnects.ai/i/144206247/some-next-steps-for-rlhf-research).

These iterative, and maybe synthetic, methods look really similar to other insights we've gotten from popular models, such as Meta's Llama 2 or Nvidia's Nemotron 340B. These models both use iterative rounds of alignment training to get to a final checkpoint. After each iteration, they get more data to then train further on. There may be a large blindspot in the academic-sided projects where not enough data filtering is done. There's plenty of research that says "[self-consuming models go mad](https://arxiv.org/abs/2307.01850)," which isn't a surprise to me.

The core difference is to use of iterative methods to expand and accumulate data, rather than just running it all as one closed feedback loop (similar to true on-policy RL). Recent work from a broad team including Stanford and MIT shows that [accumulating data, rather than doing true on-policy iteration, helps models avoid mode collapse](https://arxiv.org/abs/2404.01413).

The best industry papers rely heavily on filtering of synthetic data, which is likely combined with some form of accumulation --- e.g. keeping the absolutely best human data for every iteration. It seems that most of Llama 3's synthetic data is in the pretraining phase (cannot confirm it yet), where they state they used Llama 2 as a filterer:

> We found that previous generations of Llama are good at identifying high-quality data, so we used Llama 2 to help build the text-quality classifiers that are powering Llama 3. We also leveraged synthetic data to train in areas such as coding, reasoning, and long context. For example, we used synthetic data to create longer documents to train on.

Similarly, [Nemotron's entire paper](https://arxiv.org/abs/2406.11704v1) is focused on the training of a very good reward model to then use as their data filter.

> Throughout the entire alignment procedure, we conduct multiple rounds of data generation and refinement, continually improving the quality of our models.

And, elsewhere in the paper:

> we utilize Nemotron4-340B-Reward to assess the quality of dialogues, assigning a score to each sample and filtering out those that fall below a predetermined threshold.

Does anyone know any papers that have talked extensively about this filtering? Surely it should be done per-task and per-model being trained.

### 4. Synthetic data strategy taxes

Many companies will not use the same synthetic data that academics and open-source community members will due to terms of service and license restrictions. Popular synthetic data models from the community, such as the recent [Llama 3 Hermes fine-tune from Nous Research](https://huggingface.co/NousResearch/Hermes-2-Theta-Llama-3-70B), rely heavily on closed models such as GPT-4. Big organizations like Nvidia are restricted to using permissive models (e.g. Mistral) or their own model outputs for training.

When it comes to the open community outperforming Llama 3 Instruct with synthetic data, the ability to use GPT-4, Gemini Pro, and Claude 3 as teachers represents a huge upside. Generally, the tension around using other model outputs is much lower than it was this time last year. It seems like people are accepting it is just accepted that small players will train on the outputs of models and no one will care.

An interesting tidbit, that I've buried in the blog once before too, is that many of the "you can't train on outputs from our model" clauses in licenses actually come from the data providers used in training the model rather than the model owners themselves. They need these clauses to protect their business due to the strength of synthetic data.

### 5. Pros and cons of training on multi-output-source synthetic datasets

[UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) and [Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar) are the most popular preference-tuning datasets out there. Since their release, a ton of models trained with direct preference optimization (or the many new methods) have used them. They're the standard baseline in open alignment research. A core aspect of these datasets is that they use generations from many models in the chosen and rejected columns. The datasets have completions from pretty much every generation of models I cover in my "[history of open alignment](https://www.youtube.com/watch?v=AdLgPmcrXwQ)" lecture.

Training on completions from a large diversity of models has intuitive pros and cons. On one hand, the diversity of model outputs means the learning signal is a bit softer and can be applied to more bases. On the other, I think the ceiling of these datasets is likely lower than full on-policy synthetic generation plus filtering because they're forcing models to try and learn sequences that are low probability. Those weird phrases that GPT-4 repeats a lot may be super low probability in the Llama 3 base models, so we don't know what applying that loss update will do to the model.

These general datasets will always have a space in the ecosystem for getting started, but we need better data selection mechanisms for taking the samples out of them that best help one specific training run.

***Edit: it's important to respect how well these datasets really work**.* In [recent work](https://arxiv.org/abs/2404.02078) (building a dataset called UltraInteract), the creators of UltraFeedback have had a hard time beating its performance across general instruction-following and alignment benchmarks. People are trying, but the pros of this category are currently winning out, at least in academia.

### 6. Structured synthetic data

Synthetic data is being used to generate specific instructions and responses corresponding to verifiable behavior. In the [Nemotron 340B report](https://arxiv.org/abs/2406.11704v1), they mention creating instruction "prompts which explicitly define the format of the anticipated response, e.g., 'The output has to be in the json format.'" The goal of this is to improve on Instruction-Following Eval ([IFEval](https://arxiv.org/abs/2311.07911)). This is definitely extended to things like "generate a response that is less than three hundred words." I think cases like this, where the model gets really good at doing precisely what you ask for, is a big part of vibes-evals.

The 10 times harder version of this is what I expect top labs to be doing, and using verifiable synthetic data for things like code and math. Imagine how much better a model will be if the only code data you pass in is code that has been verified to not error.

### 7. Weak-to-strong generalization is maybe real

It's time to no longer be a skeptic of the idea of [weak-to-strong generalization](https://openai.com/index/weak-to-strong-generalization/) --- the idea that you can use a weak model to bootstrap training data that can be used to generate a net stronger model. This sort of feedback is not easy to be convinced by, but more evidence supporting it is building. From the Nemotron report again:

> Interestingly, we find that the teacher model does not impose a ceiling on the student model. Specifically, as the base model and alignment data are refined, the newly aligned model is able to surpass the initial aligned model by a significant margin.

Now, we're getting more puff-piece papers with titles like *[Transcendence](https://arxiv.org/abs/2406.11741v1): Generative Models Can Outperform The Experts That Train Them* exploring this reality. This normally means there's at least a small signal to build on here.

### 8. Creating synthetic prompts is overlooked again

The entire synthetic data movement started with [self-instruct](https://arxiv.org/abs/2212.10560), a paper designed to create more prompts to improve instruction following performance. Today, most of the discussion on synthetic data is around aggregating prompts and generating high-quality responses. Both of the datasets I mentioned above, UltraFeedback and Nectar, are conglomerates of other preexisting prompt sets.

The biggest opportunities in synthetic data are around creating a better distribution of prompts where you need them. For example, the Nemotron paper lists the 23 prompts they used to generate synthetic prompts (rather than re-using the prompts in the training set). Their reasoning was clear:

> Despite the availability of existing prompts, such as the LMSYS-Chat-1M prompts (Zheng et al., 2023), generating synthetic prompts is an important first step in SDG \[Nvidia's alignment method\].

There's really interesting research brewing in this direction, such as [copying prompts from models by prompting the undocumented model with an empty prompt](https://arxiv.org/abs/2406.08464), it then prints prompts from its training distribution, or [expanding on techniques like self-instruct](https://arxiv.org/abs/2406.10323). We need more attention on these.

<div>

------------------------------------------------------------------------

</div>

**Housekeeping**

-   Audio of this post is available (soon) in [podcast](https://podcast.interconnects.ai/) form (or previous posts on [YouTube](https://www.youtube.com/@interconnects), I've paused new generation).

-   My real podcast is at [retortai.com](http://retortai.com).

-   *Paid subscriber Discord access in email footer.*

-   Referrals → paid sub: Use the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   Student discounts in [About page](https://www.interconnects.ai/about).
