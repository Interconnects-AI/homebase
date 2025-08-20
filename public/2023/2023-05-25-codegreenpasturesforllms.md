---
title: "Code: green pastures for LLMs"
subtitle: "Both code-generation and code-training seem central to LLM progress, present and future."
date: 2023-05-25
type: newsletter
audience: everyone
visibility: public
post_id: 123787303.llms-with-and-for-code
email_sent_at: 2023-05-25T18:55:15.265Z
---
In the last few months, I finally started using [GitHub copilot](https://github.com/features/copilot) and it quickly increased my productivity. It\'s the first developer tool I\'ve tried in a long time to have a unilateral impact. Compared to any other application I use in my day-to-day life where large language models (LLMs) are a piece of it, it\'s by far and away the highest value on a per-generated-token basis. For people like me and you, every marginal percentage point of productivity will compound to be a substantial delta in the long run. Copilot feels like something contributing to that value growth, but I\'m not sure that the tools predicting the next word of my emails are too.

Releasing the alpha version of [StarChat](https://huggingface.co/blog/starchat-alpha) was my first time playing with code models. I was a pretty clean slate we these until ChatGPT came out. For StarChat, we instruction-tuned the BigCode [StarCoder](https://huggingface.co/bigcode/starcoder) model to follow instructions and we were surprised by how easy it was to get an improvement in qualitative performance at answering code questions. At the implementation level, instruction-tuning is continuing to train the language model with the original loss function (autoregressive prediction) on a set of question-and-answer style prompts. A few hours and a few GPUs later, responses from the instruction-tuned model to coding questions were preferred over 95% by GPT4 evaluations versus the base model (not rigorous, I know, but interesting). These two models, the chat model and the instruction model have very different use cases.

There are two important trends this article touches on around using code with LLMs.

1.  Training large-scale base models with code data seems to be important to downstream question-and-answer/reasoning abilities.

2.  Fine-tuning and development of code-focused models dodge some of the limitations of their text-focused counterparts.

<div>

------------------------------------------------------------------------

</div>

### The ways models use code in training

Base code models (e.g. Copilot) really want to be good at next-sequence prediction. When you write a function name and a doc-string, predicting the next tokens works really well. This is the case where the engineer knows what they want to build and the AI is a tool to help them along the way.

Instruction models need to be really good at creating complex, multi-part answers to questions that can be convoluted and slightly contradictory (think of students asking questions for an assignment they\'re trying to rush through). This type of reasoning involves the model having some sort of internal queue to respond to the instruction, start a coding block, get into the autoregressive manner explained above, and finish by explaining its reasoning. It\'s remarkable that a simple instruction tune can change qualitative behavior so much!

The third, and even more shocking jump, is that many groups continue to train their base code models on text after they run out of prepared code-tokenized data. After training on some text data, many people think that these models are better at organizing complex answers across all topics one may use ChatGPT for.

So just saying that you're "including code data" in your products doesn't say much. It's starting to come together how different training methods will be useful for different use cases, but we may see more developments.

In summary (with uncertainty estimates):

1.  \[Mostly clear\] Base code models are good for when you're writing code you have an outline of a solution.

2.  \[Multiple options\] Instruction-tuned code base models (or text models with some code) are good as coding chatbots to help with coding interviews or design solutions.

3.  \[Unproven\] Base code models trained for a bit on only text afterward have interesting properties people aren't quite sure of yet to help with any task.

### Code for reasoning capabilities

There is a useful [document about the development of GPT models after the base GPT3](https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1), which points to how chain-of-thought reasoning (as simple as prepending \"let\'s think step by step\" to the prompt) may be a side effect of training on code. Here I\'ve snipped a quote:

> The initial GPT-3 is not trained on code, and it cannot do chain-of-thought
>
> The text-davinci-001, although being instruction tuned, \[\...\] can do CoT but the performance is significantly worse, as is reported by the first version of the CoT paper --- so **instruction tuning may not be the reason for CoT. This leaves training on code to be the number one suspect**.
>
> PaLM has 5% code training data, and it can do chain-of-thought.
>
> The code data in the codex paper is 159G, approximately 28% of the initial GPT-3 570G training data. code-davinci-002 and its subsequent variants can do chain-of-thought.
>
> Copilot, supposedly powered by a 12B model, can also do CoT.
>
> On the HELM evaluation, a massive-scale evaluation performed by Liang et al. (2022), the authors also found that models trained on/ for code has strong language reasoning abilities, including the 12B-sized code-cushman-001.
>
> Code-davinci-002 has higher CoT upper bound on other models: Our work at AI2 also shows that when equipped with complex chains of thought, Code-davinci-002 is the SOTA model on important math benchmarks like GSM8K.
>
> As an intuition, think about how **procedure-oriented programming** is similar to **solving tasks step by step**, and how **object-oriented programming** is similar to **decomposing complex tasks into simpler ones**.

*More discussion can be found in this paper,* *[Language Models of Code are Few-Shot Commonsense Learners](https://arxiv.org/abs/2210.07128).*

This circumstantial evidence is interesting, to say the least. As the prompting techniques for chain-of-thought are truly silly, it\'s not surprising that finding quantitative evidence of what causes it is not so simple. The evidence presented is tampered with the conclusion, where the authors admit everything is still an open research problem.

It could be argued that chain-of-thought reasoning is closely related to long-term reasoning abilities, which code requires much more than generative text. When writing a story, it\'s probably okay to only have a few previous sentences exactly right. In code, you need to have functions and definitions at the top of the file exactly right to write functioning code. This is combined with multiple objects nested throughout the file (or files). When thinking about how attention works at a basic level --- creating probability estimates across sequences between many tokens --- it\'s clear that code will force the whole sequence to be metaphorically attended to.

![DALL·E 2023-05-19 11.57.20 - A code screen (like from the matrix) seamlessly transitioning into a grassy field, digital art.png](images/123787303.llms-with-and-for-code_7c55a95b-fc43-49d9-bc7b-8bb0aa7ce0bc.png)

### Why is the development of code-generation models more promising?

Code models are an avenue for sustained development in the RLHF ecosystem (and related tools of fine-tuning and style transfer) because of its safe harbor with an already refined product offering and technical edges akin to the potential for the diminished requirement of outsourced human preference labels. GitHub already [showcases how \"useful\" developers report Copilot to be](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) and it's best summarized by **88% percentage of developers perceiving themselves to be more productive with a code assistant**.

All of the opportunities to improve upon it are ready to be applied in a product with high developer value. Writing slightly better code is a way higher margin market than writing slightly better emails. This applies less this year when there is seemingly infinite venture money for LLMs, but in the future revenue multiples and product penetration will be crucial for getting sign-offs on training the next iteration of the model. Code models don\'t need to grow their market much.

The idea I suspect we see soon is applying [reinforcement learning from computational feedback (RLCF)](https://www.interconnects.ai/i/116158236/rlaifs-potential-renaissance) to code functionality targets. Quoting from my recent piece:

> The core idea behind RLAIF is to use RL to optimize a signal based on a computed measure of success or feedback. In reality, this is just **RLCF --- reinforcement learning from computational feedback**. Training models with RL and a computed reward could be RLHF\'s younger sibling that gets 10x the market penetration.

This could easily be applied roughly as follows: syntax is the easiest, code runs next (logic / basic errors), and finally tests for code last (complete functionality). An example would be different negative rewards for different errors: -2 for a syntax error, -1 to 0 for how much of the code runs (scale), or a score of 0 to 1 corresponds to how many tests pass. Within this setup, some popular code assistants could be collecting some of the data to do this. If Copilot sees the edits after we inset its code, it could be well along the way for having signal on syntax errors in a hacky way. The full version of this vision runs the generations from a code model in RLHF training in a sandboxed environment. Thankfully, code execution for simple things is much faster than LLM inference, so the speed isn\'t much of an issue (considering vanilla RLHF needs to do tons of inference across a reward model).

### What can go wrong with code generation?

There are a few things I worry about in code that are more akin to [second-order cybernetics](https://en.wikipedia.org/wiki/Second-order_cybernetics) than the limitations of the models themselves. I [recently discussed](https://www.interconnects.ai/p/specifying-hallucinations-llms#%C2%A7code-generation) how code-generation models can have long-term accumulated technology debt if they\'re deployed carelessly:

> \... the creators of GitHub Copilot discuss how they tried to market itself as a tool that was right only part of the time. They focused on quick responses rather than accurate ones. As pretraining gets better, these errors will go away and the current rendition of coding assistants will be glorious. It\'ll be at least a decade before we\'re really clamoring for them to solve unseen code problems, but there\'s a huge motivation to solve this (software engineers are paid a lot).
>
> Repeatedly using code generation models adds other risks that are worth considering when deciding how to frame hallucinations. If generated code writes half of the code in a codebase with a very different style than the users, accumulated deterioration from using a bunch of stylistically / API inconsistent data could emerge. The code will still run, but it seems like generations could cause increased technical debt over time. This may be more about copying and pasting different code blocks together than hallucinations, but I will pick up this thread of deteriorating data later.

Beyond that, some types of structural uncertainty around development could come back to haunt us:

-   **Companies want code models to be local for security and verification**: All of the big tech companies will have internal code models that integrate nicely with their IDE setups, driven mostly by getting employees not to send sensitive data to their competitors. Google has added [code review models already](https://ai.googleblog.com/2023/05/resolving-code-review-comments-with-ml.html), and we\'ll see a lot more. This will be from training from scratch most likely, including tons of internal data.

    \
    The smaller and medium-sized companies are in a bit different place. They likely will want to fine-tune on their own codebases. For example, at HuggingFace we'll want something that's an expert on our libraries. To do this, the companies will need a permissive base model like [StarCoder](https://huggingface.co/blog/starcoder). It's not clear if this fine-tuning model will work as well, which is the problem.\
    \
    Does anyone have an estimate for how many lines of code and reviews Google has and how that compares to all of GitHub?[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   **Evaluation tools are far behind**: As we've seen with the [LMSys](https://chat.lmsys.org/?arena) and [HuggingFace](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) leaderboards, there are huge differences between traditional NLP eval and what humans prefer for text models. For code generation, these benchmarks are even more sparse, seeming to rely on evaluation from GPT4, which is biased and not that much a long-term development target.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   **Users cannot fine-tune OpenAI code models via their API:** OpenAI could really miss the boat on this one. Either they need to release a code model with enough context length that it takes in your entire company\'s code stack (unlikely) or those that can be fine-tuned safely. Regardless, these are some of the best models, but they're locked into a narrow regime of use, which is odd.

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
This would be a fun interview question to estimate.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
HuggingFace one is self-promotion.
:::
::::
