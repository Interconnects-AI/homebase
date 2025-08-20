---
title: ""If it's not fully closed ML, it's open" - is it? "
subtitle: "Definitions from open-source software are being bent by new machine learning technologies."
date: 2023-07-26
type: newsletter
audience: everyone
visibility: public
post_id: 135445491.if-its-not-fully-closed-ml-its-open
email_sent_at: 2023-07-26T14:01:33.818Z
---
Open-source software (OSS) as a development area and community has a very clear notion of what is included in it, and what is not. Machine learning (ML) software and downstream artifacts are stressing the definitions and ideals of the OSS community. Many in ML adopted the worldview from OSS software, but many in the world of "open" ML these days are doing so for different reasons. While it's pretty easy to be more specific about what parts are open or closed in a particular ML system when writing at length, the "takes" people have on social networks like "Open ChatGPT" are straining the values of the more long-term open source software community members.

It is important to separate the tensions between personalities and the growing pressure to pick a side in the open versus closed debate from **the reality of needing a new taxonomy for open-source and machine learning**. I worry that the tensions around open source could boil over into the different sides of the AI risk discussion that we have now. The open-source questions should be addressed independently.

Llama 2, while a victory for the open-source movement through and through, is not technically open-source, which spawned a new round of discussions on what it means for an ML artifact to be open-source.

If you look at the cutting-edge [research on machine learning releases](https://arxiv.org/abs/2302.04844) from my colleague [Irene](https://www.irenesolaiman.com/), and whether they\'re open or closed, most of them would not get the label of \"open-source software\":

> fully closed; gradual or staged access; hosted access; cloud-based or API access; downloadable access; and fully open.

The Llama models (both 1st and 2nd generation) have fallen in the *downloadable access* point. The paper continues to break down what defines this by three types of artifacts:

> The parts of an AI system considered in a release can be broken into three broad and overlapping categories:
>
> • access to the model itself,
>
> • components that enable further risk analysis,
>
> • and components that enable model replication.
>
> Components are organized based on their most straightforward use. There is overlap among these components; the same model cannot be replicated without its component for risk analysis, such as its entire original training data, even if all replication components are available. Conversely, components for replication can also be analyzed for social impacts such as biases.

This framing is a good starting point because it puts more flexibility in the artifacts. Training data for the base model are required for both model replication and risk analysis (for things like copyright and social bias). It correctly separates a few different values in open-source: replication and safety. In recent days, I find most people in the debate to be most frustrated with the obscuration of Llama 2 replication due to a lack of dataset issues, while details around risk analysis are at least *attempted* (via the safety evaluations).

### Brief history of open-source

[RedHat has a definition of open-source software](https://www.redhat.com/en/topics/open-source/what-is-open-source) that resonates with me:

> Open source software is code that is designed to be publicly accessible---anyone can see, modify, and distribute the code as they see fit.

This focuses on the values of transparency for security and progress. As we stare down the long debates of what open and closed means in the context of machine learning artifacts, it is important to realize the bigger picture. To quote a good, [short piece on why Llama 2 is not truly a piece of open-source software](https://www.alessiofanelli.com/blog/llama2-isnt-open-source) (but I disagree with the author, I think the distinction matters), emphasis and links mine:

> \... since the [1976 "Open Letter to Hobbyists"](https://en.wikipedia.org/wiki/An_Open_Letter_to_Hobbyists#:~:text=%22An%20Open%20Letter%20to%20Hobbyists,regard%20to%20his%20company's%20software.), there's always been tension between the commercial interests of software companies and the curiosity of hackers who wanted to circumvent its restriction. The "free software" movement started in the 70s in the MIT AI lab with Richard Stallman and eventually the GNU project in 1983. The [GPL "copyleft"](https://www.gnu.org/licenses/copyleft.en.html) license was created, and projects like Red Hat, MySQL, Git, and Ubuntu adopted it.
>
> The term "open source" came to be in 1998 thanks to MIT's Christine Peterson; at the "Freeware Summit", the **term "free software" was officially deprecated in favor of "open source software"**. As time went by, the "free" and "open source" software communities diverged as they had different ideas of what free and open meant. Free software, as specified by the Free Software Foundation, is only a subset of open-source software and uses very permissive licenses such as GPL and Apache.

The author then points out another relevant point in recent history where the definitions of open-source are being strained. This is bound to happen, software and its derivative technologies are still new. Fanelli continues:

> Elastic and MongoDB transitioned their open source projects to the "Server-Side Public License" (SSPL) which allows developers to use the product commercially, as long as what they are offering isn't a hosted version of the product. **The goal was to block AWS from re-hosting their products as cloud services and profiting from them.** The SSPL also infringes on the OSS ideals and is not recognized by the OSI as an open source license. Yet, the majority of developers still say that MongoDB is open source. More and more the term \"open source\" is losing its freedom connotations and turning almost synonymous with \"source available\" in developers\' minds.

Ultimately, we are careening towards another split in the open-source community and that is okay. The Llama 2 license *and dataset details* will be the starting point of a debate that helps us converge on answers.

*Further reading: Here\'s* *[another piece](https://opensourceconnections.com/blog/2023/07/19/is-llama-2-open-source-no-and-perhaps-we-need-a-new-definition-of-open/)* that *I enjoyed on why Llama 2 is not open-source.*

![](images/135445491.if-its-not-fully-closed-ml-its-open_56391659-7348-4f32-9c0b-8b00aa06e924.png)

### License limitations and dataset obfuscation

Two clauses in the license preclude the model itself from being open-source (if that\'s something that fits into your worldview). I personally think it would be a useful term to say a model is open-source, or something when the weights are fully available and usable without restriction. The two clauses that are important are the 700 million user clause and the downstream large language model (LLM) clause.

The user clause states that companies cannot use Llama 2 commercially without consulting Meta for a license if they have 700 million monthly active users ***at the time of release***. The fact that the clause is time-gated makes it surely a competitive play, maybe against Snap and Telegram, who both crossed 700 million monthly active users earlier this year. Personally, I would love it to be the case where Meta needs to hand out these bespoke licenses on a regular basis because it means open machine learning is thriving in products, but I mostly see this license term as a niche restriction on obvious competitors. On the other hand, Meta working with Apple to accelerate and integrate the Llama models directly into Apple devices (the largest generally dormant graphics computers out there), much like [Apple did for Stable Diffusion](https://machinelearning.apple.com/research/stable-diffusion-coreml-apple-silicon).

The other license is really similar to what we have seen with OpenAI\'s terms of service agreement (TIL that a terms of service is just like a license for a service product):

> *You will not use the Llama Materials or any output or results of the Llama Materials to improve any other large language model (excluding Llama 2 or derivative works thereof).*

Generally, these are so funny and express extreme cognitive hurdles these companies put themselves through in the fast-changing, and unregulated, space of ML. Ultimately, companies that say these are saying that it\'s okay to train on arbitrary internet data because it is accessible, but you cannot train on our models because we say so, even though the model is accessible. I also love it because there is not an agreed-upon definition of what constitutes an LLM. Dataset and model-use regulation will come eventually, but until that time is years away, expect more of this nonsense. I expect the companies will be forced to provide disclosures about the dataset in the future and the down-steam use clauses will be struck down in court as a non-sensical contract item (we still haven\'t seen OpenAI go after anyone, for what it is worth).

In terms of open-source definitions and values, the lack of dataset information is a bigger strike against the openness of Meta. The release of the model without the dataset information makes the model training process irreproducible by the public. In traditional OSS, one of the values is that the software is not owned by any one entity (even if it is heavily maintained by one entity), so the long-term development of the project is independent of the whims of for-profit corporations. For all of the inference accelerators and model-compression applications that are built in the coming weeks, if the development of base versions of Llama is derailed it would set back the open-source community immensely. In open-source machine learning, the feasibility of full reproduction via the public is something that will be extremely rare and should be accounted for in any open-source AI taxonomy.

<div>

------------------------------------------------------------------------

</div>

### Open-source as vibes

In the last year, the closed-source AI community has been gaining so much traction that it is blatantly leaving open-source advocates on the back foot and on the wrong side of a power grab. Due to this, and likely due to the extremely public regulatory capture attempts of their critics, open-source community members have been bending their own values in order to encourage the broader movement in their own direction.

This is a central reason why people like me, or others at open-source-centric companies, like HuggingFac,e still make errors about the communication of these issues: we\'re trying to balance signposting on the broader issues with communicating specific artifacts. In this vein, two things can be true:

1.  Llama 2 was not released as a fully open-source model, and

2.  Llama 2 being released as it was is the biggest moment of the year in open-source AI.

This takes a lot of craft to communicate carefully about. There is a lot at stake here, where individuals are balancing maintaining their (and their communities\') credibility on a per-announcement basis to try and turn the tide of the broader movement. Personally, I think I have done a passing job at this, like a B, with a couple of embellishments of what open-source is in machine learning without truly misleading people.

Some folks in my network and company, don\'t always do it like this. It is easy to venture into the full terrain of the \"open-source as vibes\" mentality, which results in consistently beating the drum that \"open-source ChatGPT has landed\" with each subsequent fine-tuned LLaMA we saw for the first half of the year. Ultimately, I think these individuals are sacrificing close-network reputation at the cost of out-network following and impact, but mostly for miscommunicating capabilities (rather than miscommunicating openness). It transitions people from close communities to the public narrative war.

I\'m not going to say making that choice is wrong, but it is extremely frustrating for the most passionate and value-driven champions of the open-source movement.

In the coming months, there is a chance that the tenor of open-versus-closed reaches more theocratic levels, rather than reason, which would be a failure mode of miscommunicating here. Seems like we are far from this moment, so I don\'t find it worthwhile to chase people down and correct them.

Ultimately, I think we are in the spot with so much progress happening in closed-off AI labs, that \"if it\'s not fully closed, it\'s open\" can apply to Llama 2. Now that Llama 2 is here, the bar for what constitutes open-source has been raised.

*The interesting dynamic to watch here is over which pieces the open-closed debate differs from the safety-ethics debate that is currently resonating through the machine learning community. The open-source base will likely start with a bigger group, as most researchers are defining the directions of machine learning still, and scientific values strongly overlap with those of open-source.*

### Formal definitions of open-source machine learning

The Open Source Initiative (OSI), which maintains resources of common open-source software licenses and definitions, has released a [call for proposals to define the landscape of open-source AI technologies](https://blog.opensource.org/now-is-the-time-to-define-open-source-ai/). This is a huge step in the right direction, as they note the power dynamics driving the technology towards closed-source, how different types of software needed different definitions and more. The problem is the timeframe. The performance overhang driven by the rapid rate of progress on machine learning research while products were relatively unexplored made for a spark moment in shifting AI from open to closed. This type of multi-stakeholder engagement to reach a common ground is something we all wished happened before ChatGPT.

In the future, there will likely be different terms and criteria for if datasets, models, and training code are all released with a model. Each of these artifacts conveys extreme value when released in the open, but the entire system may not be open-source if one component is not. An open release of a model would be a subset of a potentially open system.

There is also a future where releasing datasets and training code is so rare that it is given a label of super-open-source, or something silly. Open-source ML companies will likely have to grapple with the fact that releasing datasets destroys their own moats and exponentially increases legal liability.

<div>

------------------------------------------------------------------------

</div>

Elsewhere:

-   Some cool work I did during my Ph.D. on micro solar sails is out on [Arxiv](https://arxiv.org/abs/2307.11226).

-   ICML has been so good! Still here to chat if you are. Aloha.

![](images/135445491.if-its-not-fully-closed-ml-its-open_87276eaa-8053-4218-8459-8cc87dac283c.heic.png)
