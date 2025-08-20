---
title: "Specifying hallucinations"
subtitle: "The future of LLM errors and the need for a discourse around the specification of unexpected outputs."
date: 2023-05-03
type: newsletter
audience: everyone
visibility: public
post_id: 117706873.specifying-hallucinations-llms
email_sent_at: 2023-05-03T14:55:31.420Z
---
The thing about the [Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922) paper is that the name they gave large language models (LLMs) may have really been *too correct*. The more you dig into how language models operate, the more they really are fairly unpredictable computations that can return wonderful or harmful outputs. Just as I am shocked to hear my name spouted by a [wild San Francisco parrot](https://www.kqed.org/news/11185731/where-did-the-wild-parrots-of-san-francisco-come-from), I am regularly totally blown away by the generative capabilities of these models. While parrots likely are fairly stochastic creatures on their own, it\'s also apt to double down on having stochastic in the name. At every turn when applying a language model as a tool, remembering that they are stochastic machines is central to understanding the pros and cons of the approach, and it combats the narrative of them acting similar to biological systems.

In some domains, large language models will create new ideas that are harmful to users. In other domains, the language models generating something entirely new will be entirely central to the value provided. These unexpected terms, often not found explicitly in the training data whatsoever, are called **[hallucinations](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))**. They can be factual errors or a sort of "unhinged" response or anything in between. Core to the use of this term is strongly positive and negative valence.

The first result for a general definition of a hallucination is **where you hear, see, smell, taste, or feel things that appear to be real but only exist in your mind**. The anthropomorphization of ML models is drastically accelerated by this term (second only to folks naming their chatbots and having them act from the first person). Human hallucinations are a real biological phenomenon, but in that, they\'re an **increased delta between the real world and your perception.** All of our perceptions always have an error margin, to begin with, anyways!

ML hallucinations are uninterpretable due to the scale of these models, but they are real and clearly defined computations. They are the output of a deterministic probability sampling (which can be controlled by setting the seed) that often sounds resoundingly confident just due to training data. They're essentially mistakes in our computational setup and training process. It's a big problem to link the terms for human hallucinations and unexpected model behavior because they are similar to observers on the outside, but they, in reality, have extremely different causes.

Accurately discussing these causes is how we learn more about the impacts. Long-term, we'll be able to tune our training process to choose different strengths and weaknesses of models that all fall under the current use of the term hallucination: factual accuracy, model stylistic consistency, and model robustness (to lexical attacks/jailbreaks).

Hallucinations are one of the most hotly debated terms around LLMs these days --- the idea that a model will generate some token that is totally out of the distribution from its training domain sometimes even becomes political. For the unaware, a token is a block that the models choose when generating, and they always come from a predefined vocabulary (set of tokens). To train LLMs in other domains such as [robotics](https://www.deepmind.com/publications/a-generalist-agent) or [vision](https://arxiv.org/abs/2010.11929), a tokenization scheme is adopted where the world is captured in a set of discrete options to form a vocab. In something like robotics, this isn\'t so intuitive, because we are often discretization a continuous value like voltage. In vision, this makes way more sense, the tokens can just be the RGB pixel value in the image. At the end of the day, any of these models hallucinates when it chooses the next token from a set that is really far away from the training distribution.

Here arrives the first axis of ambiguity in the discussion of hallucinations: **what constitutes an out-of-distribution sample?** There is likely a numerical reason the token was chosen (e.g. a side effect of some approximate loss step), but how do we draw bounds here? For language, people often decide this based on whether or not the generation is factually correct. E.g. if you ask a model, when was Barack Obama inaugurated, and it returns 2008, that\'ll be considered a hallucination. This is much less clear in other domains --- is there a factual truth when working on images, given that all visual information is processed and influenced by the device capturing it (including human beings)?

Two things can be true simultaneously: we learn how to train LLMs to drastically reduce any factual errors, but hallucinations will still be prevalent and important to how they operate. Language has so dang many combinations, we\'re always going to explore new terrain (especially considering how large models are trained on some month(s) old data and we ask them to comment on current events). This exploration link to hallucinating will not go away.

We need to grapple with what the different parts of hallucinations are. This is the first step towards having separate terms for the different failure modes discussed in the introduction to this post.

Let\'s consider some domains where people may be using LLMs to generate content, then I\'ll regroup with a couple more axes for comparing hallucinations.

![DALL·E 2023-05-02 17.51.54 - Someone hallucinating when approaching an oasis in the desert, surrealism digital art.png](images/117706873.specifying-hallucinations-llms_710bce73-f569-4fda-8f56-57ad488572d4.png)

# Impacts of hallucinations per-domain

This section is mostly off-the-cuff remarks on how I see things unfolding in different domains and how axes of hallucination start to emerge from the comparisons.

### Chat

Humans talking with LLMs is where all of this discussion on hallucinations was given a giant dose of rocket fuel. Chat generally has two dimensions --- business chat (like those that try to offer you \"help\" when buying online) and personal chat (ChatGPT, Character.ai, and many others coming soon). Personal chat is the more game-changing one.

In the consumer domain, as we saw with the [Sydney exposes in the early Bing days](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-transcript.html), hallucinations are the single most exciting part of the technology. While Microsoft will tamp down on this because of their giant downside risk, other upstarts will not. Hallucinations enacted in the chat are your agent gaining new opinions and personalities outside of the training distribution. That\'s hugely value-generative as a form of entertainment.

With reasonable controls on what the agents cannot engage with at all, the likelihood of harm in an entertainment-first domain is relatively low. Additionally, these experiences will probably be "come when you can, leave when you want," sort of technologies without lasting effects (e.g. future models aren\'t trained on the text, and future automation won\'t encounter the outputs). Seems good to me!

### Code generation

Code is one of the more borderline cases. When using it, hallucinations always sound like they\'ll be annoying --- randomly selected tokens to seem like a sure-thing-useless-code-block. On the other hand, how does generated code solve new problems if it cannot take some risk? In this vein, the creators of GitHub CoPilot discuss how they tried to market itself as a tool that was right only part of the time. They focused on quick responses rather than accurate ones. As pretraining gets better, these errors will go away and the current rendition of coding assistants will be glorious. It\'ll be at least a decade before we\'re really clamoring for them to solve unseen code problems, but there\'s a huge motivation to solve this (software engineers are paid a lot).

Repeatedly using code generation models adds other risks that are worth considering when deciding how to frame hallucinations. If generated code writes half of the code in a codebase with a very different style than the users, accumulated deterioration from using a bunch of stylistically / API inconsistent data could emerge. The code will still run, but it seems like generations could cause increased technical debt over time. This may be more about copying and pasting different code blocks together than hallucinations, but I will pick up this thread of deteriorating data later.

### Control / decision making

Coming at LLMs from a robotics and decision-making background makes me feel duty-bound to have a distinction between hallucinations and exploration in data collection. I don't. Hallucinating in relatively narrow-scoped sampling domains like robotic control seems beneficial and very similar to exploration methods. This does not necessarily scale when the actions are taken on the internet scale, or the mouse and keyboard input scale. If you give the model full access to the normal input-output tools humans use with computers, you really don\'t want them pressing random combinations of keys. This intuitively feels closer to the factual answers issue with hallucination, but not quite. I\'m wondering if this intuitive gap is just because training practices on language data, rather than action data, are so much better defined.

On the other hand, factual errors also can just seem similar to when a planning-based policy selects the wrong action. The model probably has all the information to know that Obama was inaugurated in 2009, but sometimes it\'ll sample wrong. In some domains, trying new things gives you insight into valuable new data. Interacting with users obsessed with information retrieval is not that type. I suspect that hallucinations are not talked about as much in real-world decision-making domains because the failures will be looped into other types of analysis: Was the value prediction wrong, were the predicted trajectories wrong, etc? Hallucinations in grounded domains may be easier to analyze than language!

Video games could easily merge the positive qualities I mentioned in both this subsection and the chat subsection to an even greater payoff. Keep an eye on this one.

### Healthcare

Medical decision-making or advice is the obvious case where hallucinations can occur at the same rate as other applications, but they have way higher downside risks that are hard to cope with. The magnitude of risk should be a core consideration when looking at potential hallucinations --- it'll be best to **deploy systems with notable hallucinations where searching for new value** or profits, rather than solving old harms.

The current healthcare system is not designed to de-noise information at every exchange --- it would need a ground-up rebuild to accommodate these autoregressive models at every turn. Many companies selling LLMs for X healthcare problems are going to encounter a dearth of acceptance for any sort of hallucination. Even when factual accuracy is solved, the other characteristics of mis-prompting yielding nonsense are similarly detrimental.

There are some cases where LLMs will be applied to the bureaucratic side of healthcare, and the challenges will look similar to other enterprise use-cases --- it is easy to lose track of and control over the data landscape over time.

### Enterprise (emails, summarization, search, ...)

This is the one that executives will sign off on, and come to regret. AI models can reduce the hard work of writing that encompasses so much knowledge work but with a catch.

As I was discussing above with code generation, the **outputs of these models could flood some domains and have delayed impacts**. I can easily see employees at a company abusing the internal ChatGPT equivalent and blindly pasting the information everywhere. It's a case where there is a new tool to seem productive with minimal effort, which we know is always utilized. In the future with LLMs everywhere, everyone loves over-documenting, but it has errors because of hallucinations. This will happen in domains will low short-term standards on factuality (e.g. random documentation compared to healthcare), but with long-term use cases intact. New users and new employees then have the debug documentation, which is likely a net loss in productivity.

![DALL·E 2023-05-02 17.52.01 - Someone hallucinating when approaching an oasis in the desert, surrealism digital art.png](images/117706873.specifying-hallucinations-llms_3beca253-b18c-4203-9e4c-15271f78990d.png)

<div>

------------------------------------------------------------------------

</div>

## Wrapping up

A potentially hasty line to draw on if hallucinations are likely to be considered good or bad is: **are the models being used in a direct-to-consumer** **way**? From chatbots to videogames to generative imaging, the unexpectedness of it seems to be a large driving part of the entertainment. In tons of professional domains, this will not be the case. You don\'t want your auto email service to insult your boss ever, but a chatbot picking an argument with you can be wildly intriguing. As factual errors become more obsolete, this half of hallucinations may become more directly proportional to the [temperature parameter](https://cs.stackexchange.com/questions/79241/what-is-temperature-in-lstm-and-neural-networks-generally) of sampling (i.e. how uniform vs. spikey the token distribution is).

Hallucinations in models are something that seems like way more of an issue when the models are locked into an 8/10 confidence level. If a model sounds like it is unsure, then it starts repeating itself and gets some things wrong, that will be way less of an issue. This is the axis where techniques like RLHF can really shift public perception.

In summary, the axes to consider when discussing a hallucination of your model or domain:

-   Is it a consumer or business application? Is it entertaining to have changed?

-   What are the downstream harms of unexpected behavior? Searching for upside or mitigating downside (the latter is worse for LLMs)?

-   Are there accumulated degradation effects from hallucinations? What happens when your data or systems get increased technical debt?

-   What constitutes out-of-distribution data, and how can you quantify this?

This list is very much a work in progress for me. I'll update you when I make a breakthrough on it. For more on this topic, Sarah Hooker engaged with this on [Twitter](https://twitter.com/sarahookr/status/1642667134861074432).

What's your favorite example of a hallucination? Share it below ⬇️.

I feel like I\'m finally catching up on getting all my LLM thoughts off my chest. Hopefully, I can touch on some more topics again soon!

<div>

------------------------------------------------------------------------

</div>

*Some other interesting reads this week:*

-   *[Why did Google Brain exist?](https://www.moderndescartes.com/essays/why_brain/) I thought this was one of the more accurate takes on why industry research existed at scale in AI. Getting that phase right will make it easier to understand what the second phase of industrial AI research will look like.*

-   *I'm astounded by how weird LLM companies are these days. A new LLM company, [Lamini](https://lamini.ai/), emerged on the block, and it seems like [Self-Instruct](https://arxiv.org/abs/2212.10560)-as-a-service (synthetic training data for LLMs).*

-   *I did a fireside talk discussing my career (mostly grad school + job search + industry transition). \[[Link](https://teamrora.mxmagnoilia.com/6114067ee9359a04a6cfbfaf/l/MvfAWzhWrpnwRNuPc?messageId=Fflyx2x9cK0OyGexW&rn=gI0JXZi1WYMBibhhGdh5kI&re=i02bj5CdyVmYtFGbvRXYuBkbhhGdh5mI&sc=false) + pw 4L#wq5\^?\]*

*Interconnects is free and reader-supported. Feeling generous? [Buy me a coffee](https://www.buymeacoffee.com/natolambert).*
