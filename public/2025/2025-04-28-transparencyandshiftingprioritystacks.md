---
title: "Transparency and (shifting) priority stacks"
subtitle: "What you want to be open says a lot about your ranked priorities."
date: 2025-04-28
type: newsletter
audience: everyone
visibility: public
post_id: 161980031.transparency-and-shifting-priority
email_sent_at: 2025-04-28T12:02:54.652Z
---
The fact that we get new AI model launches from multiple labs detailing their performance on complex and shared benchmarks is an anomaly in the history of technology products. Getting such clear ways to compare similar software products is not normal. It goes back to AI's roots as a research field and growing pains into something else. Ever since ChatGPT's release, AI has been transitioning from a research-driven field to a product-driven field.

We had another [example](https://x.com/natolambert/status/1915903512707563785) of the direction this is going just last week. OpenAI launched their latest model on a Friday with minimal official documentation and a bunch of confirmations on social media. Here's what Sam Altman said:

![](images/161980031.transparency-and-shifting-priority_c80184c4-122b-4d01-b075-40b63d22d59f.png)

Officially, there are "[release notes](https://help.openai.com/en/articles/9624314-model-release-notes)," but these aren't very helpful.

> We're making additional improvements to GPT-4o, optimizing when it saves memories and enhancing problem-solving capabilities for STEM. We've also made subtle changes to the way it responds, making it more proactive and better at guiding conversations toward productive outcomes. We think these updates help GPT-4o feel more intuitive and effective across a variety of tasks--we hope you agree!

Another way of reading this is that the general capabilities of the model, i.e. traditional academic benchmarks, didn't shift much, but internal evaluations such as user retention improved notably.

(*Lot's of people also strongly dislike the new personality, but that's not the point of this post)*

Of course, technology companies do this all the time. Google is famous for A/B testing to find the perfect button, and we can be sure Meta is constantly improving their algorithms to maximize user retention and advertisement targeting. This sort of lack of transparency from OpenAI is only surprising because the field of AI has been different.

AI has been different in its operation, not only because of its unusually fast transition from research to product, but also because many key leaders thought AI was special. AI was the crucial technology that we needed to get right. This is why OpenAI was founded as a non-profit, and existential risk has been a central discussion. If we believe this technology is essential to get right, the releases with it need to be handled differently.

OpenAI releasing a model with no official notes is the clearest signal we have yet that AI is a normal technology. OpenAI is a product company, and its core users don't need clear documentation on what's changing with the model. Yes, they did have better documentation for their [recent API models in GPT-4.1](https://www.interconnects.ai/p/openais-gpt-41-and-separating-the), but the fact that those models aren't available in their widely used product, ChatGPT, means they're not as relevant.

Sam Altman sharing a model launch like this is minor in a single instance, but it sets the tone for the company and industry broadly on what is an acceptable form of disclosure.

The people who need information on the model are people like me --- people trying to keep track of the roller coaster ride we're on so that the technology doesn't cause major unintended harms to society. We are a minority in the world, but we feel strongly that transparency helps us keep a better understanding of the evolving trajectory of AI.

This is a good time for me to explain with more nuance the different ways transparency serves AI in the broader technological ecosystem, and how everyone is stating what their priorities are through their actions. We'll come back to OpenAI's obvious shifting priorities later on.

The type of openness I've regularly advocated for at the Allen Institute for AI (Ai2) --- with all aspects of the training process being open so everyone can learn and build on it --- is in some ways one of the most boring types of priorities possible for transparency. It's taken me a while to realize this. It relates to how openness and the transparency it carries are not a binary distinction, but rather a spectrum.

Transparency and openness occur at each aspect of the AI release process. The subtle differences in decisions from licenses to where your model is hosted or if the weights are available publicly at all fall on a [gradient](https://arxiv.org/abs/2302.04844). The position I advocate for is on the extreme, which is often needed to enact change in the world these days. I operate at the extreme of a position to shift the reality that unfolds in the middle of the discourse. This'll also make me realize what other priorities I'm implicitly devaluing by putting openness on the top. With finite effort, there are always trade-offs.

Many companies don't have the ability to operate at such an extreme as I or Ai2, which results in much more nuanced and interesting trade-offs in what transparency is enabling. Both OpenAI and Anthropic care about showing the external world some inputs to their models' behaviors. Anthropic's [Constitution for Claude](https://www.anthropic.com/news/claudes-constitution) is a much narrower artifact, showing some facts about the model, while OpenAI's [Model Spec](https://www.interconnects.ai/p/openai-rlhf-model-spec) shows more intention and opens it up to criticism.

Progress on transparency will only come when more realize that a lot of good can be done by incrementally more transparency. We should support people advocating for narrow asks of openness and understand their motivations in order to make informed trade-offs. For now, most of the downsides of transparency I've seen are in the realm of corporate competition, once you accept basic realities like frontier model weights from the likes of OpenAI and Anthropic not getting uploaded to HuggingFace.

Back to my personal position around openness --- it also happens to be really aligned with technological acceleration and optimism. I was motivated to this line of work because openness can help increase the net benefit of AI. This is partially accelerating the adoption of it, but also enabling safety research on the technology and mitigating any long-term structural failure modes. Openness can enable many more people to be involved in AI's development --- think of the 1000s of academics without enough compute to lead on AI who would love to help understand and provide feedback on frontier AI models. Having more people involved also spreads knowledge, which reduces the risk of concentration of power.

I've for multiple years feared that powerful AI will make [companies even more powerful economically and culturally](https://www.interconnects.ai/i/143210216/inclusion-public-interest-and-fighting-concentration-of-power). My readers don't need warnings on why technology that is way more personable and engaging than recommendation systems, while keeping similar goals, can push us in more negative rather than positive directions. Others commenting here have included Meta's Mark Zuckerberg's *[Open Source AI is the Path Forward](https://about.fb.com/news/2024/07/open-source-ai-is-the-path-forward/)* and Yann LeCun's [many comments on X](https://x.com/ylecun/status/1796543960296440162). --- they both highlight concentration of power as a major concern.[1](#footnote-1){#footnote-anchor-1 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

Still, someone could come to the same number one priority on complete technical openness like myself through the ambition of economic growth, if you think that open-source models being on par can make the total market for AI companies larger. This accelerationism can also have phrasings such as "We need the powerful technology ASAP to address all of the biggest problems facing society." Technology moving fast always has negative externalities on society we have to manage.

Another popular motivation for transparency is to monitor the capabilities of frontier model development (recent posts [here](https://time.com/7086285/ai-transparency-measures/) and [here](https://blog.ai-futures.org/p/training-agi-in-secret-would-be-unsafe)). Individuals advocating for this have a priority stack that has a serious short-term concern of an intelligence explosion or super-powerful AGI. My stack of priorities is the one that worries about the concentration of power, which takes time to accrue and has a low probability of intelligence takeoff. A lot of the transparency interventions advocated by this group, such as Daniel Kokotajlo on his [Dwarkesh Podcast episode](https://www.dwarkesh.com/p/scott-daniel) discussing AI 2027, align with subgoals I have.

If you're not worried about either of these broad "safety" issues --- concentration of power or dangerous AI risk --- then you normally don't weigh transparency very highly and prioritize other things, mostly pure progress and competition, and pricing. If we get into the finer-grained details on safety, such as explaining intentions and process, that's where my goals would differ from an organization like a16z that has been very vocal about open-source. They obviously have a financial stake in the matter, which is enabled by making things useful rather than easier to study.

There are plenty more views that are valid for transparency. Transparency is used as a *carrot* by many different types of regulatory intervention. Groups with different priorities and concerns in the AI space will want transparency around different aspects of the AI process. These can encompass motives of the researchers, artifacts, method documentation, and many more things.

The lens I'm using to understand trade-offs in transparency is a ***priority stack***, an evolution of the [Principle Stack](https://exponent.fm/episode-177-principle-stacks/), revisited many times in the last 5+ years of the [Stratechery](https://stratechery.com/) universe. The core idea is that whether or not you like it, every business and decision is governed by a set of priorities ranked relative to each other. Everyone has things that they care about more and less, even if the issues are both extremely important. It is the basis for making trade-offs in determining the direction of businesses.

Some examples of who could advocate for information on what in the AI ecosystem include:

-   **Capability transparency** --- keeping the public informed of progress of models that may be unreleased, primarily to keep track of a potential intelligence explosion. This often includes new types of systems now that AI agents are working.

-   **Base model transparency** --- these are most useful for people wanting to understand the role of pretraining on AI dynamics. The base models of today can easily follow instructions and do reasoning, but they're less robust than the full final model. These are diminishing as a target of transparency, as reasoning and post-training grow in importance.

-   **Pre-moderation model transparency** (endpoints without moderation filter, models without some refusals data) --- to test the evolution of content risk for models that may be deployed without moderation endpoints, such as open weight models, which tend to be release just months after closed models with similar capabilities.[2](#footnote-2){#footnote-anchor-2 .footnote-anchor component-name="FootnoteAnchorToDOM" target="_self"}

-   **Reward model transparency** (and more extreme, preference data collection instructions) --- those interested in the original goals of alignment, i.e. value alignment, can use these to test how the models' views vary across different groups and test if the intended model preferences are picked up in the preference training process (i.e. [relative to the instructions given to data labelers](https://rlhfbook.com/c/06-preference-data.html#are-the-preferences-expressed-in-the-models)).

-   **Training specification transparency** (Model Spec's, Constitutions, and other goal-setting documents) --- there are so many people who would want to know *why* the model behaves a certain way. I've [mentioned](https://x.com/natolambert/status/1907621608430133444?utm_source=chatgpt.com) these benefits before:

    -   Developers: Know what future models will become, which helps create a stable platform.

    -   Regulators: Transparency into what the heck frontier labs care about, which helps understand the directions AI is going, and the motivations of super powerful companies.

    -   Internal: Focus on defining and delivering your goals (separate from this transparency discussion).

There are also subtleties in these discussions, such as how [structured access to models](https://cdn.governance.ai/Structured_Access_for_Third-Party_Research.pdf) can serve different but complementary goals of open weights. Structured access is a set of programs where prescreened individuals can use models in a secure environment and operate independently from the AI laboratories themselves.

This could be seen as a separate direction to transparency, where instead of the public getting the information or artifact, only a few pre-approved people do. In reality, structured access is a complement to transparency and will be needed for details where the companies cannot disclose them publicly without substantial business competitiveness risk, such as novel algorithmic tricks that substantially modify how the AI works, or real-world harm, such as model weights pre safety interventions.

Some parts of AI should be accessible to the general public, and some to third-party testers. Currently, all of the transparency and access is below the safest equilibrium. We need more of both.

One of the most ignored details is just how *access is implemented*. A [recent paper from Irene Solaiman et al.](https://arxiv.org/abs/2502.16701) paints how releasing components is one step in sharing information and artifacts:

> Generative AI release decisions determine whether system components are made available, but release does not address many other elements that change how users and stakeholders are able to engage with a system. Beyond release, access to system components informs potential risks and benefits. Access refers to practical needs, infrastructurally, technically, and societally, in order to use available components in some way.

The authors break access down into three axes:

-   **Resourcing**: Infrastructural needs to host and serve.

-   **Usability**: Varied technical skill levels can engage.

-   **Utility**: Qualities (e.g. multilingual) with user utility.

As our models at Ai2 are becoming more capable, my relationship as a developer with my downstream users has changed. The models I've worked on have shifted from those primarily motivated by values, with the transparency we're discussing being of top value, to now also adding utility as a much higher weight. People want to use some of our models in real applications. While my priority stack hasn't changed --- openness is still the top value --- the way it's implemented is shifting. I'm no longer racing to get all of our results hot off the press into the world because of the cost of time it takes to support them (support costs rise proportional to the user base).

Other key players in the AI space have obviously changed their priority stack.

OpenAI's recent actions confirm that ChatGPT as a product is its top priority. Transparency and safety have been moving down on their list of priorities in favor of growth. This is partially due to increased competition, but also due to a shifting political landscape. OpenAI's coming release of an open model doesn't shift this priority stack for me.

I used to hear a lot about OpenAI's pre-release testing and the accompanying non-disclosure agreements. This quiet model drop being "[the quickest we\'ve shipped an update to our main 4o line](https://x.com/aidan_mclau/status/1915904460808983007)" shows that safety is moving down their priority stack. This isn't to say that their safety changes are immediately concerning to me, but rather that there are trade-offs in everything. OpenAI is moving cultural norms in leading AI away from releases with detailed evaluation metrics and towards more normal, quiet technology company consistent drips of updates.

<div>

------------------------------------------------------------------------

</div>

*Thanks to Miles Brundage for a discussion that helped motivate this post.*

:::: {.footnote component-name="FootnoteToDOM"}
[1](#footnote-anchor-1){#footnote-1 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
Very open to comments on how to make sense of Mark Zuckerberg's many sided positions on AI here.
:::
::::

:::: {.footnote component-name="FootnoteToDOM"}
[2](#footnote-anchor-2){#footnote-2 .footnote-number contenteditable="false" target="_self"}

::: footnote-content
This builds on the common practice that most language models like ChatGPT have small models in the loop that monitor prompts and responses for traits that violate usage policies (jailbreaking) or content policies (harmful text).
:::
::::
