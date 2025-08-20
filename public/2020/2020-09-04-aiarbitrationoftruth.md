---
title: "AI & Arbitration of Truth"
subtitle: "Can we make an AI fact checker? Language, knowledge, and opinions are all moving targets."
date: 2020-09-04
type: newsletter
audience: everyone
visibility: public
post_id: 508123.ai-arbitration-of-truth-808b57a93a97
email_sent_at: 2020-09-04T14:00:50.218Z
---
*I wrote this essay a month or two ago, but it only will become more relevant in the coming months. Please take a few minutes to consider how technology may affect our beliefs and circles. [Facebook is bracing](https://nyti.ms/3iZTjLg) for a contested election already.*

In light of Twitter engaging on the fact-policing front, it's time to figure out what an ***artificially intelligent fact-checker*** would look like. Is it feasible technologically, what would its biases be, and more.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c2d73456-9191-42d2-bb02-eb85d25a192b_1200x627.png)

### Social media companies & litigating truth: in brief

You've probably heard a lot about "Section 230," but it is something people cite without fulling understanding its placement in actual law. [Section 230](https://www.eff.org/issues/cda230) is a Provision of the Communication Decency Act of 1996, which provided protection for internet companies by not making them legally responsible for the content of their users. [Trump is fighting it in the courts](https://www.washingtonpost.com/technology/2020/05/28/trump-social-media-executive-order/). It's scope is not all-encompassing of internet-media trends.

Let's look at what the two loudest technology companies have been doing in the space of fact-checking.

#### Twitter's take: we have responsibility.

[Jack Dorsey has been drawing a line and watching Trump challenge it for months](https://www.nytimes.com/2020/05/30/technology/twitter-trump-dorsey.html?action=click&module=Top%20Stories&pgtype=Homepage). Now, Twitter is taking on fake-news on it's platform. Many, many users are happy about this in the short term (honestly I am, *I think*), but **there are long term consequences**. How to make this decision in a bias-free, up to date way is extremely challenging. I hope they can traverse this path successfully, but there's bound to be controversy (potentially in November).

#### Facebook's take: making companies the arbiter of truth is dangerous.

Take a counter-example to [Twitter's ban on political advertising](https://www.nytimes.com/2019/10/30/technology/twitter-political-ads-ban.html): **what is the line for a political ad?** I would define a political ad as an entity paying to sway public opinion on itself (rather than just selling a product). A senator buying a vote is clearly political, but is an oil company buying public opinion after a botched oil-spill response a political ad? The specific answer here doesn't matter to me --- *what matters is that an individual (or a biased computer system) must decide the line between political and non-political advertising*.

The thing is with the two approaches to arbitration of fact, they are both valid arguments with huge upsides when done right. The implantation is key.

***The need for regulation is warranted and strong (Facebook), but when the regulation is lacking there is a strong pull on our humanity to mitigate the harm caused to users (Twitter).***

### The Tech --- Transformers & NLP

Natural Language Processing (NLP) is the subfield of machine learning concerned with manipulating and extracting information from text. [It's used in smart assistants, translators, search engines, online stores, and more.](https://en.wikipedia.org/wiki/Natural_language_processing) NLP (along with computer vision) is one of a few monetized state-of-the-art machine learning developments. *It's the candidate for being used to interpret truth.*

The best NLP tool to date is a neural network architecture called **the transformer**. Long story short, transformers use an [encoder and decoder structure](https://towardsdatascience.com/understanding-encoder-decoder-sequence-to-sequence-model-679e04af4346) that encodes words to a latent space, and decodes to a translation, typo fix, or classification (*you can think of an encoder-decoder as compressing a complicated feature space to a simpler space via a neural network --- nonlinear function approximation)*. A key tool in the NLP space is something called [Attention](https://medium.com/@joealato/attention-in-nlp-734c6fa9d983) that learns which words to focus on and for how long (rather than hard coding it into an engineered system).

A [transformer](https://arxiv.org/pdf/1810.04805.pd) combines these tools, and a couple other advancements that allows the models to be trained efficiently in parallel. Below is a diagram showing how data flows through a transformer.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/147d65bd-cc0a-4539-aa08-788805eb23be_678x830.png)

A visualization from an awesome tutorial I found <https://jalammar.github.io/illustrated-transformer/>.

#### Online fact-checking

The key technical-point of the transformer structure that potentially lends it to fact-checking is that they are **parallelizable** (can easily run multiple words and tweets through one model). Fact-checking online will mean every text based post will pass through a model either a) prior to being posted publicly or b) soon after being publicly posted. The scale of computation here is unprecedented.

For reference, there are about [6000 tweets posted every second](https://www.internetlivestats.com/twitter-statistics/) and [Facebook's numbers are even more astounding](https://www.brandwatch.com/blog/facebook-statistics/). The state of the art NLP tool, [BERT, has over 100million parameters](https://yashuseth.blog/2019/06/12/bert-explained-faqs-understand-bert-working/). The order of required computation for processing the new content is linear in these values. That's a lot of GPUs (Google and Facebook regularly spend millions of dollars just to train these models). Processing all this data would likely be a dramatic increase in cost for these companies (I may revisit this, doing the math).

[Facebook uses AI to mitigate the creation of fake accounts](https://phys.org/news/2019-05-fake-facebook-accounts-never-ending-bots.html) while they are being made to eliminate infrastructure burden downstream. Maybe the companies can use a classifier to pinpoint content that is potentially fact-based, and check those only? [It turns out this fact-checking could be worth a lot in positive public impressions.](https://www.theatlantic.com/technology/archive/2019/02/how-much-factchecking-worth-facebook/581899/)

Okay, we have the model and the server farm, what's next. The ultimate problem is the question of **what is true**? The problem with learning-based methods on fact-checking: moving targets, biased data, and unclear definitions. This is the crux of the article, what I have been pondering, and what I think is an **impossible target for automation**.

### Adding structure to online discourse

The process of regulating online discourse will surely bring some pushback. Will all companies comply? What is the cost of entry, or abstention? The themes addressed here will be playing out in the next months via the megaphone of the 2020 U.S. presidential election.

#### What is fact? What is truth?

This is the fundamental problem is that not all individuals consider the same information true. Ideally, facts are a set of items that cannot be challenged. Truth is the value that individuals hold and use to challenge other's views --- truth can also include belief.

#### Truth is a moving target for individuals. Fact is a moving target for science and society.

An individual works in a fluid set of local and global truths all the time. A local truth for me and many of my closest friends is that *rowing is a special sport that is unmatched due to its cooperation and high limits*, but it's definitely not true to everyone. A global truth is *the Earth is round*. There's a lot of truths in between those that are more difficult to classify.

The problem I see with internet fact checkers is that users will want their local truths to be checked too. How do we collect a dataset of true verses untrue statements?

#### Who moderates the database?

It is impossible to distill every truth-to-be-checked down to first principles of science (which is just the current model for the world, so could change). Can we make a knowledge graph for humanity\*? That means there will be some data labelling process (having users do this seems like a monstrous challenge because of local truth). Data-driven approaches always have a [tradeoff between bias and variance](https://towardsdatascience.com/bias-variance-tradeoff-fundamentals-of-machine-learning-64467896ae67), and that's assume the data itself is valid. I've talked about the challenges of data-bias when making physical automation, but it'll be just as prevalent in the digital-domain.

Let's dig into this a little further. There's no clear scenario to deploy for a fact truth database.

-   If scientists determine facts, I will be concerned about the disproportionate representation of white-male information.

-   If social media content determine facts, I will be worried about Russian disinformation determining the ground truth for a fact-database.

-   If written media (newspapers, books) determines facts, it's recreating the world view of a select few authors.

If you meld all three of those, it sounds alright, but there's always going to be corner cases, missed information, and confusing biases.

#### Open-source Facts:

The best solution I [have read](https://twitter.com/balajis/status/1266180931435417600): **open-source fact-checking**, with monetary backing (likely from the government and large social media companies). This would mean that an independent organization regularly updates and maintains a truth directory. *This would be a costly task, but may be needed to maintain the stability of our open-internet, capitalist society.*

What's left when there is an open-source fact-checking organization is many, many corner cases. What happens when a tweet does not classify as true or untrue --- do we have to label it as *new*? What scale of company is required to adopt the database? What about a new area of [deepfakes](https://en.wikipedia.org/wiki/Deepfake) to fake the truth detector? I think these are all things we can, and should, solve, but the discussions need to be frequent and early. [Source.](https://twitter.com/balajis/status/1266180931435417600)

\*How would you fact check with first principles? I think this should look into [representation theory in graphs](https://www-cs.stanford.edu/people/jure/pubs/graphrepresentation-ieee17.pdf). There are a core set of principles, then new knowledge forms edges based on proven connections. There will be areas of claims that are **uncertain** (disconnected from the true graph), but by making a new proof, and a new edge, we can add more items to the fact database.

[](https://substackcdn.com/image/fetch/$s_!w5nV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc67299cb-7614-450f-815c-b98f864dbc5d_800x650.jpeg){.image-link .image2 component-name="Image2ToDOM" target="_blank"}

:::: image2-inset
![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c67299cb-7614-450f-815c-b98f864dbc5d_800x650.jpeg){.sizing-normal attrs="{\"src\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c67299cb-7614-450f-815c-b98f864dbc5d_800x650.jpeg\",\"srcNoWatermark\":null,\"fullscreen\":null,\"imageSize\":null,\"height\":null,\"width\":null,\"resizeWidth\":null,\"bytes\":null,\"alt\":null,\"title\":null,\"type\":null,\"href\":null,\"belowTheFold\":true,\"topImage\":false,\"internalRedirect\":null,\"isProcessing\":false,\"align\":null,\"offset\":false}" loading="lazy" sizes="100vw" srcset="https://substackcdn.com/image/fetch/$s_!w5nV!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc67299cb-7614-450f-815c-b98f864dbc5d_800x650.jpeg 424w, https://substackcdn.com/image/fetch/$s_!w5nV!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc67299cb-7614-450f-815c-b98f864dbc5d_800x650.jpeg 848w, https://substackcdn.com/image/fetch/$s_!w5nV!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc67299cb-7614-450f-815c-b98f864dbc5d_800x650.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!w5nV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc67299cb-7614-450f-815c-b98f864dbc5d_800x650.jpeg 1456w"}

<div>

</div>
::::

Photo by [Danya Gutan](https://www.pexels.com/@danya-gutan-1529084?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from [Pexels](https://www.pexels.com/photo/man-reading-burning-newspaper-3278364/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels).

*I've included plenty of reading on this subject. I also find myself Tweeting about it, if you would like to [follow me](https://twitter.com/natolambert), or [Ben Thompson](https://twitter.com/benthompson) (author of [Stratechery](https://stratechery.com/)) may do a better job.*

News Coverage:

-   A [laboratory at Duke University](https://reporterslab.org/using-artificial-intelligence-to-expand-fact-checking/) studying mechanisms in reporting (including automated fact-checking).

-   Two pieces from The Atlantic last year studying a) [fact-checking and Trump](https://www.theatlantic.com/magazine/archive/2019/06/fact-checking-donald-trump-ai/588028/) and b) the [value of fact-checking to Facebook](https://www.theatlantic.com/technology/archive/2019/02/how-much-factchecking-worth-facebook/581899/).

-   MIT Technology review on [fact-checking with AI in times of COVID-19](https://www.technologyreview.com/2020/05/29/1002349/ai-coronavirus-scientific-fact-checking/).

-   [Fake news detection and political stance](https://bdtechtalks.com/2020/02/24/deep-learning-fake-news-stance-detection/) survey.

-   [Argument for open-sourcing fact-checking via Twitter](https://twitter.com/balajis/status/1266180931435417600).

Related Reading:

-   [Open source code for SOTA natural language processing model](https://pytorch.org/hub/pytorch_fairseq_roberta/) and the [Wikipedia article describing the structure](https://en.wikipedia.org/wiki/Transformer_%28machine_learning_model%29).

-   [Disinformation assessment in news media](https://arxiv.org/pdf/1911.11951.pdf) with NLP (paper).

-   [Verifying scientific claims](https://arxiv.org/pdf/2004.14974.pdf) with NLP (paper)

-   [Representation learning on graphs](https://www-cs.stanford.edu/people/jure/pubs/graphrepresentation-ieee17.pdf) --- a lens I think fact and truths should be interpreted from (paper).

<div>

------------------------------------------------------------------------

</div>

Hopefully, you find some of this interesting and fun. You can find more about the author [here](https://natolambert.me/). Tweet at me [\@natolambert](https://twitter.com/natolambert), reply here. I write to learn and converse. Forwarded this? Subscribe [here](https://democraticrobots.substack.com/).
