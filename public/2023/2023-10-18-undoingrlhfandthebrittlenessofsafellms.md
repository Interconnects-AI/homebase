---
title: "Undoing RLHF and the brittleness of safe LLMs"
subtitle: "Recent papers show most of the arguments about needing "safety" in releases of open LLM weights are nearly dead in the water. Yes, still release the parameters."
date: 2023-10-18
type: newsletter
audience: everyone
visibility: public
post_id: 137911702.undoing-rlhf
email_sent_at: 2023-10-18T12:01:48.764Z
---
Forecasting AI is nearly impossible because we\'re inclined to compare it to existing technologies like software and nuclear energy, but its core axes will be where it is fundamentally different from what we\'ve seen before. The progress in understanding how safety and harm can be propagated via these models is a ripe vein for identifying the new ways technology will work with LLMs.

I recently shared my [thoughts regarding the potential future of content moderation and LLMs](https://www.interconnects.ai/i/137712762/should-llms-have-safety-filters). In the last few weeks, there\'s been a series of safety papers requiring updates to that frame, from **understanding both the removal of safety filters at the parameter level to the avoidance of safety filters during inference**. The arguments of what open models should do primarily rest on the former, while the liability of many companies rests on the latter.

The realities of open LLM releases \-- when the parameters are available for users \-- seem to be solidifying already from the safety point of view. Results show that encoding safety in accessible parameters, i.e. those that can be trained, is a hollow approach protecting only liability rather than malicious use. Most of the methods trying to **create safety in LLM parameters have happened post-pre-training, so it is done with approximately thousands of times less compute**. As long as this is the case, it will likely be possible to undo the safety training. Moving safety/harmlessness to pretraining seems to go directly against the notion of a helpful model first and then a harmless model. Results showing you can embed safety during pretraining and not reduce helpfulness will be about 10 times more astonishing than any other results showing you can subvert safety fine-tuning.

The pace of development on inference time attacks is continuing rapidly. We saw OpenAI slowly release [GPT4 Vision](https://openai.com/research/gpt-4v-system-card) into the world, and there are lots of examples on Twitter of prompt injection attacks through the image and thankfully some [folks writing summary blogs](https://simonwillison.net/2023/Oct/14/multi-modal-prompt-injection/). An example of the character of GPT4 Vision prompt injections was [shared by Meet Patel](https://twitter.com/mn_google/status/1709639072858436064):

![gpt4v-attack-1.jpeg](images/137911702.undoing-rlhf_576777cc-5836-42f3-b83d-a8d7320a3784.png)

To be clear, these are not that interesting. Compared to the attack vectors that OpenAI has already patched in ChatGPT, where it could become an entirely new stable persona, the ones going around are extremely benign and easy to curate data to counteract.

### Fine-tuning the safety away

When we noticed that [Llama 2 had too much RLHF](https://www.interconnects.ai/i/135320564/evasiveness-through-harmlessness) training for safety filters, it\'s clear that most people would\'ve thought it a harder task to get around the filters in the chat model. I thought it would be a few months of research with some interesting training methods, but that was a little naive. All the recent successes of LLMs are driven by data, so undoing the advancements would start there too.

[Recent work](https://arxiv.org/abs/2310.03693) from Princeton, Virginia Tech, and others shows that **with as** **little as 10 to 100 supervised fine-tuning examples, the content filters on Llama-2-chat or ChatGPT equivalent models (GPT 3.5 Turbo) can be almost entirely bypassed**.

This paper is leading the way toward core insights into the robustness of LLM weights in the future. They have three sets of jailbreaking prompts, harmful ones, \"identity shifting data\", and benign data (normal open-source helpfulness data). As expected, the harmful examples obliterate the models' safety filters, and the helpful data just slowly degrades the filters. The surprising one is that the identity shift data does about as much mitigation of the safety filters as the explicitly harmful examples. This data was \"particularly designed to evade moderation\" where \"the model acts under a new identity --- absolutely obedient agent (AOA) --- an identity we adversarially create that is set to prioritize instruction fulfillment.\" Ultimately, they\'re trying to teach the model a new way of behaving, and one that ends up pulling it away from its safety filters. This type of defense will be hard to mitigate.

Credit to the authors of this paper, [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693), it\'s very extensive and they even release their analysis methods as a benchmark. Just what the field needs right now.

There was another paper released literally a day before this one that had a very similar conclusion, but very different methods. The [Shadow Alignment](https://arxiv.org/abs/2310.02949) paper used GPT4 to generate synthetic training data specifically that would violate the ChatGPT terms of service, then trained open models on those. Other than the normal biases such as affiliations and networks, my guess is that this second paper didn\'t take off as much because they did *not* show their results on OpenAI\'s fine-tuning API nor did they release a benchmark associated with it. Regardless, concurrent publication of results is the best validation for academics\' ideas. It\'s not a zero-sum game.

### Moderation, training infrastructure, liability

The safety filters used in LLMs are a new rendition of moderation attempts by technology companies. Moderation as a requirement has primarily emerged from public pressure around platform safety and social norms of what should or should not be promoted on the internet. The same trends are going to be placed on LLMs from day one because they\'re a downstream reflection of all the internet has brought us since its conception.

Moderation of LLMs is about liability. If a company deploys a model, it should be responsible if it serves someone with harmful content.

In Meta\'s case, they want safety filters on the Llama models used in their products and in the Llama models offered by popular cloud providers that come with bespoke and high-value partnership agreements. Once someone fine-tunes the models they release, that liability train should immediately break. The fine-tunes of Llama that has mitigated safety filters obviously are not endorsed or supported by Meta, and a third part will have to provide the infrastructure to deploy the model and attention to proliferate it.

In this view, Meta should still release their models with safety filters. They need to do the research to deploy the models how they want them in their products, and it requires a new organization to have the \"final stamp\" on model ownership. Looking back at the Llama 2 paper, if you take that as a transparent sharing of results, safety is a huge focus for Meta because that is what is needed to support their platforms. It\'s not something their users in the open-source community are clamoring for.

As a brief aside, it seems likely that for popular models in the future, getting around the safety filter is as simple as merging the \"undo safety LoRA adapter.\" [LoRA, low-rank adaptation](https://generatingconversation.substack.com/p/lora-explained), is an extremely popular technique for fine-tuning LLMs by adding a new subset of parameters to the attention layers and running fine-tuning. Primarily in text-to-image communities such as Stable Diffusion, users have been exploring merging multiple adaptors at inference time to combine multiple styles. Safety avoidance is an obvious motivating case for this in LLMs \-- use the avoidances LoRA and then train your own use case for maximum helpfulness. I\'ll keep an eye on this, as releasing a LoRA adaptor is even more accessible than a dataset because people can run inference immediately.

The company more challenged by these results with fine-tuning to undo RLHF is actually OpenAI because they provide the full-stack tooling for fine-tuning and access. Selective moderation of the companies deploying models trained with your API is very tricky and likely not a business that OpenAI wants to get into. When fine-tuning OpenAI\'s models, the customers never break the link of liability by serving and or training it themselves. I\'m sure OpenAI is monitoring this, but it seems like much more of a losing battle than Meta\'s angle. Maybe Meta finally was traumatized from its long history of negative press and got out ahead of things. Oh, and yes, this is a reason to execute open-source LLM strategies.

So yes, I don't really care anymore if open LLM weights have a safety filter or not. It's not really the argument worth focusing on. The stuff that matters happens downstream.

*Note: I would like to see how all of this holds up on the new* *[\"Safety-Tuned LLaMAs\" from a paper](https://browse.arxiv.org/abs/2309.07875)* *studying better safety training techniques, but I think the attack vectors will prove more robust.*

![natolambert\\\_a\\\_content\\\_moderator\\\_of\\\_the\\\_future\\\_swiping\\\_right\\\_and\\\_a188cca6-6a43-4ca6-9aa6-fe7da23c68ce.png](images/137911702.undoing-rlhf_d13e19f6-8437-48ca-aa72-b2774021a496.png)

## More on prompt jailbreaks

Prompt jailbreaking, often through prompt injection where adversarial information or instructions are used in the prompt to derail the model, is the most common method studied to attack OpenAI\'s API models. These will always be around, but it\'s the sort of problem that mirrors other technological developments better (hint: cybersecurity).

There were three recent papers relating to prompt jailbreaks:

-   [Low-Resource Languages Jailbreak GPT-4](https://arxiv.org/abs/2310.02446): This paper shows that with current models, simply translating a simple attack vector to a low resource model and passing it into the model tends to bypass safety filters. This seems like a data problem that will be patched by spending lots of money.

-   [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://arxiv.org/abs/2309.10105): This paper is indirectly related to prompting, but it shows that fine-tuning models suppresses behaviors in a way. Given how important various fine-tuning methods are to safety, it indicates that robust safety will always be hard. As long as models do enough so that you need to be *really clever* with your prompts to get any harmful response, I don\'t actually think it matters from a liability / public perception point of view. *Conjugate prompting* is the method the authors propose to recover pretraining capabilities.

-   [GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts](https://arxiv.org/abs/2309.10253): This paper has LLMs write variations on human written prompts to break through various LLM filters. This isn\'t surprising to me at all but fits the thesis that we\'ll see a steady progression of the robustness of defenses and the methods of attackers.

Ultimately, this side of safety seems to matter a lot less compared to the fine-tuning side. AI Safety leaders overstate their importance by saying they\'re early indicators of how people can unlock the future capabilities of the models. In reality, I see most of the attack vectors being patched with better data coverage. Until specific capabilities of models are known to be an actual risk, the defense mechanisms to prevent them will not be suitably motivated to make a fair comparison. API models will be safe enough, and I still think there will be an LLM provider that outputs unfiltered responses for a long time into the future, given how much the general public wants access to unfiltered outputs.

<div>

------------------------------------------------------------------------

</div>

### What we\'re learning about RLHF

If you were really plugged into RLHF since ChatGPT, you would know that there\'s a general intuition that *folks were impressed by how much RLHF steering measures translate to out-of-distribution languages*. I think it turned out that this was more of a story of how LLMs work in so many unexpected ways, but the scale of positive transfer was a small bump rather than emergent impressive capabilities.

what\'s not well studied is how quickly attack vectors like low-resource languages are patched in ChatGPT and if these fixes still generally happen at the parameter level by expanding fine-tuning distributions. If they\'re continuing to train it, that means maybe it is as simple as fixing the RLHF training dataset. That goes to show that RLHF will be used very extensively and is reliable enough to run a training run, look at a few evaluations, and ship it. If the training requires another substantial training and/or updates to various supporting systems that filter model content, the whole harm reduction battle in modern LLMs may be a little trickier.

*Credit to Shayne Longpre for a great* *[Twitter thread](https://twitter.com/ShayneRedford/status/1711782932598169951)* *that either reminded me of or pointed me to some of the papers in this post. Also, credit to the authors for doing all this very cool work on LLM safety.*

<div>

------------------------------------------------------------------------

</div>

Longer reads and links this week!

Elsewhere from me:

-   \[Podcast 🎤\] On [episode 5 of The Retort AI Podcast](https://retortai.com/episodes/methods-of-rationality-in-the-time-of-hype), Tom and I discuss the early days of the rationality movement (which now heavily informs AI safety) and what hype about AI actually is and means.

-   \[Paper\] Some technical RL work I've had brewing for a while, connecting to my Ph.D. thesis on model-based reinforcement learning is out. You can read *[A Unified View on Solving Objective Mismatch in Model-Based Reinforcement Learning](https://arxiv.org/abs/2310.06253)*, if you're a nerd about the future of model-based RL. If you're obsessed with RLHF, this should be you.

-   \[Notes\] I created a [document](https://www.craft.me/s/NHvR6dsCVNNW8L%5D) where I'll store the basic RLHF literature review I do chronologically. This will be the source material for some coming blog posts.

Reads:

-   \[OpenAI / LLM businesses\] A provocative [read](https://generatingconversation.substack.com/p/openai-is-too-cheap-to-beat?utm_source=post-email-title&publication_id=1881004&post_id=137900765&utm_campaign=email-post-title&isFreemail=true&r=68gy5&utm_medium=email) from my friend Vikram on the basic math that shows while OpenAI has the best models, they also have the cheapest offerings for getting started with fine-tuning models. Pressuring the middle of the market from both sides (GPT4 at the top, old models at the bottom).

-   \[Robotics / RL\] A series of [two](https://www.youtube.com/watch?v=K09erFsOnxA) [talks](https://www.youtube.com/watch?v=vNFTcD3QMn0) from robotics legend Vladlen Koltun on the revolution coming slowly through robotics. It's linked to my [recent article on Moravec's paradox.](https://www.interconnects.ai/p/robotics-vs-moravecs)

-   \[LLM model report\] Mistral released a [technical report](https://arxiv.org/abs/2310.06825) for their 7B models --- there's not a lot new here (hint, nothing on data cleaning), but it is a good resource for some things like sliding window attention.

-   \[LLM as computing platform\] Another cool paper from Berkeley showed how an LLM, named [MemGPT](https://memgpt.ai/), can manage its own context window as a sort of memory buffer.

-   \[Tutorials\] Another [solid tutorial on distributed training emerged](https://sumanthrh.com/post/distributed-and-efficient-finetuning/), this time from [Sumanth Hegde](https://twitter.com/sumanthrh/). This stuff is likely the most important set of details powering the LLM revolution. Knowing intuitively all the terms in the [practical guidelines](https://sumanthrh.com/post/distributed-and-efficient-finetuning/#practical-guidelines) is a good place to start.

Housekeeping:

-   **Interconnects referrals:** You'll accumulate a free paid sub if you use a referral link from the [Interconnects Leaderboard](https://www.interconnects.ai/leaderboard).

-   **Student discounts:** Want a large paid student discount, go to the [About page](https://www.interconnects.ai/about).

-   **Like this?** A comment or like helps Interconnects grow!
