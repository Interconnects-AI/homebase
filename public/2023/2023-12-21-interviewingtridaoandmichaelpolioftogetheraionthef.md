---
title: "Interviewing Tri Dao and Michael Poli of Together AI on the future of LLM architectures"
subtitle: "The first Interconnects research interview! We go even further on the promise of state-space models in the emerging LLM market."
date: 2023-12-21
type: podcast
audience: everyone
visibility: public
post_id: 139958384.interviewing-tri-dao-and-michael
email_sent_at: 2023-12-21T14:58:29.334Z
---
*This interview is on [YouTube](https://youtu.be/OFFHiJzPpCQ) and [podcast players](https://podcast.interconnects.ai/episodes/do-llms-need-attention-an-interview-with-tri-dao-and-michael-poli).*

Giving a voice to researchers is the best way to cut through the noise and understand what is happening with core developments of LLM technologies. I'm excited to get to talk with [Michael Poli](https://zymrael.github.io/) (Stanford PhD student + research at Together AI) and [Tri Dao](https://tridao.me/) (incoming professor at Princeton + Chief Scientist at Together AI). This builds on the mega-post from yesterday on the same topics, though the interview is obviously less math heavy:

::: {.digest-post-embed attrs="{\"nodeId\":\"bb2c0a0d-e41e-43f2-bba4-0b20396d7df8\",\"caption\":\"As the holiday season comes around, remember you can give the gift of Interconnects. While it's still early days on paid features, it’ll guilt them into reading the highest signal AI essays out there. No audio of the post due to reliance on figures. State-space LLMs is the last topic of Interconnects for the year, next week will be a year in review post.\",\"cta\":null,\"showBylines\":true,\"size\":\"md\",\"isEditorNode\":true,\"title\":\"State-space LLMs: Do we need Attention? \",\"publishedBylines\":[{\"id\":10472909,\"name\":\"Nathan Lambert\",\"bio\":\"ML scientist (RL, RLHF, society, robotics), athlete, yogi, chef. Writes about ML research.\\nPhD from Berkeley AI, Cornell Lightweight Rowing `17\",\"photo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdda47b96-836a-4b95-99a0-f0ec744d4245_2316x2316.jpeg\",\"is_guest\":false,\"bestseller_tier\":100}],\"post_date\":\"2023-12-20T14:53:35.769Z\",\"cover_image\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8b5b4cd-1328-4a71-8a59-a26fccea4634_1792x1024.png\",\"cover_image_alt\":null,\"canonical_url\":\"https://www.interconnects.ai/p/llms-beyond-attention\",\"section_name\":null,\"video_upload_id\":null,\"id\":139943907,\"type\":\"newsletter\",\"reaction_count\":9,\"comment_count\":0,\"publication_name\":\"Interconnects\",\"publication_logo_url\":\"https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe70f9dbf-4fe6-404c-b6bb-1831d1b7ed0b_590x590.png\",\"belowTheFold\":false}"}
:::

<div>

------------------------------------------------------------------------

</div>

**Topics:** [Introductions](https://www.interconnects.ai/i/139958384/introductions') \| [Why Attention works and may not scale](https://www.interconnects.ai/i/139958384/why-attention-works-and-may-not-scale) \| [Quadratic scaling in attention](https://www.interconnects.ai/i/139958384/quadratic-scaling-in-attention) \| [What is Striped Hyena](https://www.interconnects.ai/i/139958384/what-is-striped-hyena) \| [What is Mamba](https://www.interconnects.ai/i/139958384/what-is-mamba) \| [Mamba hardware optimization](https://www.interconnects.ai/i/139958384/mamba-hardware-optimization) \| [Predictions for 2024 architectures](https://www.interconnects.ai/i/139958384/predictions-for-architectures) \| [More predictions for AI](https://www.interconnects.ai/i/139958384/more-predictions-for-ai)

### Introductions

\[00:00:00\] **Nathan Lambert:** Okay. Hey, everyone. Welcome to the first interview that we\'re going to post on interconnects. I\'m really trying to bring more scientific voices into the AI discourse as media is covering a lot these days. I\'m happy to be here with Michael Poli and Tri Dao, experts in some of these non attention architectures that have been really blowing up in the last few weeks of December.

So, Michael, do you want to introduce yourself first?

\[00:00:25\] **Michael Poli:** Sure. Thank you. Thank you, Nathan. For inviting me, I, do research at Together AI. And I was also a PhD student at Stanford, working with Stefano Ermon and, and, Chris Re, that\'s, that\'s how I met Tri as well. if I had to choose maybe, I moved to a few different areas of research.

if I had to choose one, I like to, do research at the intersection of signal processing, dynamical systems, and deep learning, and most recently, luckily, there\'s been more interest in, in kind of efficient architectures that use some of these principles. to improve scaling, along different axes and to, to get sort of new, new trade offs at inference time.

\[00:01:13\] **Nathan Lambert:** Great. And Tri?

\[00:01:16\] **Tri Dao:** Everyone, thanks Nathan for, for, hosting us. really excited to be here. I\'m Tri. I, just finished my PhD at Stanford. and I\'m being assistant professor at Princeton, and right now I\'m chief scientist at Together AI. it\'s, it\'s a startup working on AI infrastructure. And, yeah, I\'ve been working at the intersection of machine learning and systems, so designing algorithms that take advantage of the hardware that, that they run on.

I\'m interested in, long range, dependencies, how to encode that into a model, designing architectures that can, can, learn long range dependencies. yeah, really excited to be here.

### Why Attention works and may not scale

\[00:02:01\] **Nathan Lambert:** Okay. I think I\'m going to, I have some questions dive right into this. I think you two will kind of both answer them or someone can answer longer, whatever you want.

I think to start with, we should talk about maybe why attention works and what the limitations of attention are. I think. Almost every person in tech broadly now knows that a transformer is a model built with attention and chat GPT does that but like, why is this so good, even like how much of a transformer is built with attention are there other things going on, and what might be challenges there.

\[00:02:35\] **Tri Dao:** Right. so, transformer which is this. Contexture that powers most of the exciting applications that we\'re seeing nowadays, as you mentioned, and so on. attention is kind of the core layer there, and attention actually became, earlier, around 2014, 2015, and then transformer came out, incorporating that, focusing a lot on, on, attention, with these, MLPs, interleaving, MLP and, and attention.

And I think the success largely has been, They are, they seem to be able to scale really well so that you can scale up the models, with more, more parameters, with more data. And that has been the recipe for, for success. It sounds obvious now, but I think, five years ago that wasn\'t, that wasn\'t clear.

so it seems like, you know, Transformer Architecture is, is a hugely successful one. and, you know, a couple of reasons why it\'s successful. I think it\'s like General enough that it\'s able to learn a lot from data. And two is, is pretty friendly to hardware. You can, there\'s no kind of sequential dependency like previous RNNs.

so as a result, you can run it well on GPUs, TPUs. you can scale it up. It\'s very hardware efficient. I\'ve personally have worked on making it more hardware efficient as well. So it\'s just kind of the recipe for, for success, which is, general architecture that scales well. if you\'re an NLP person, maybe you, you, you said, you know, incorporate some kind of inductive bias for, for, to protect, personally, I think it\'s a very general architecture that, that scales well and it\'s hardware friendly.

\[00:04:16\] **Nathan Lambert:** Yeah. Yeah. It\'s, it\'s remarkable how it seems so obvious now and it\'s like. I think one of the things that studying this work is the context length becomes a really interesting access to study alternatives to it. And essentially it\'s, I think, I mean, Michael, do you want to talk about that? I could, I could babble, but you\'re, you\'re no more sure.

\[00:04:39\] **Michael Poli:** yeah, the there are several points. I\'ll start by saying that, you know, there\'s still a lot of great research trying to understand why from first principles. Why is it that the transformer can learn these interesting circuits? people kind of study, they, they pick apart the computation, like combination, different, \[00:05:00\] heads and transformers and so on.

so there\'s work on basically understanding transformers from kind of like a programming language that is encoded. But I think, as, as Trey mentioned, there\'s, there are some very, Very, very interesting design choices that have gone into the transformer. This interleaving of attention on MLP is quite important.

and also the transformer is essentially, was successful in the beginning \'cause it encoded these, techniques that, that, that have been developed for, RNN Celest. So these other, you know, classical NLP models, gating to, modulate, which information is absorbed into the model. Gating to determine how quickly something is forgotten in this this occurrence of get an end into a parallel form.

It is, you know, easily, a bunch of gems that can be easily, well, not very easily, but can be optimized on GPUs.

### Quadratic scaling in attention

\[00:06:01\] **Nathan Lambert:** Yeah, that\'s, that\'s all great. I think that, I guess the specific thing that I had in mind is how attention ends up being this kind of quadratic, scaling in terms of cost when you have an input sequence that you have, if you have an input sequence of length L and you want to output a sequence of length L essentially.

If you zoom into the math and you look at what\'s happening at inference in most of these libraries, you have this like upper triangular attention matrix where you say, like, you can only look at the past entries of your text. And as you go through there, then you end up getting this a long, you get this L squared relationship where the first token, you can only look at one, and then you end up looking at more tokens for each, past and Now we\'ve been talking about recurrent neural networks and how does something that isn\'t attention like get around the fact that you want to look at all of the history of the text in your sequence.

So like if you write a long prompt to chat GPT, you really want all that information to be encoded and how could doing something other than this dense attention matrix. Like actually make that possible.

\[00:07:08\] **Tri Dao:** Yeah, so you can go ahead and, you know, before attention, there was RNNs, right? Like a minute RNN\'s like they process text was fine. and maybe they didn\'t scale as well, but yeah. you say briefly texts by encoding texts.

\[00:07:22\] **Nathan Lambert:** Can you say briefly what a RNN is and how it works?

\[00:07:24\] **Tri Dao:** Yeah, so these are recurrent neural nets, that go back, I think, to the 80s.

maybe some of the more famous ones are LSTMs, GRU. so they were pretty popular in, around 2012 to 2016 or so. they were kind of state of the art for translation, speech recognition. a bunch of, I think NLP, like, they, they were a state of the art and, and they processed text kind of sequentially.

they are just, they see essentially one token and then that. Changes the hidden state and then they will update the hidden state and every time they see a new token. So, I think it\'s kind of, in some sense, mimicking, how, for example, human brain process information, like you read, you, you read a sentence or a passage and, you know, it\'s, it\'s maybe it\'s like you\'re storing some information in your brain.

By the time you\'ve finish reading a document, maybe you can answer questions about that documents without having to read to, to refer to that document again. So, RNs, kind of work that way. They, they, they, they process the, the, the texts. and then that changes the hidden state and their hidden state is the representation that can be used to either generate new tokens or, classify the documents or, or, or whatnot.

so these work well back in 2016 or so. But, they\'ve kind of fallen out of, favor, empirically, they don\'t do as well as, as Transformer, I think, and as you, you touched on Transformer, because of this kind of quadratic scaling, and you compare every token with every other token that comes before it, it gives you this very kind of easy way to, to propagate information.

and, I think that\'s part of the reason why, why, transformer and attention does really well. but there\'s been more, more recently, some of the new, newer RNN architectures that. Seem to do pretty well. So, RWKV is, I think is one of the earlier ones, you know, is one. I, I really admire that, that that project, you know, his effort mostly from, from, from one person really going against the, orthodoxy of, of transformer.

Who, who was it showing that Rrn can be pretty strong. Who was the lead on that? I think it was this person, Bo Peng, I think. and, you know, it\'s, it\'s, it\'s an entire project, but I think it was pioneered by Bo Peng. I think it\'s, affiliated with Alutha the compute sponsor by Stability and so on.

\[00:10:12\] **Nathan Lambert:** Yeah. I was reading this earlier. At a technical level, they tried to replicate something like the query key. Value lookup of attention with two linear RNNs to essentially be able to remove the like specific attention scaling problem, potential problems, and with two RNNs, which have this better, like long context behavior and different implementation rules.

I think, and they also, the paper trained up to 14 billion parameters, which kind of leads into the, some of the next questions I was going to ask, I was going to ask Tari about, Mamba and then Michael about Striped Hyena. I think you could go in either order. I think these came out about a week apart and were these two language models kind of seen as being.

### What is Striped Hyena

**Nathan Lambert:** Way closer than anyone would expect, essentially the Striped Hyena came out and the evaluations were close to models I\'ve been training on all year, like Lama 2 and Mistral 7b. And I went in and I went to the together API and I did like side by side of. Mistral versus Striped Hyena, and it\'s like, it\'s, it\'s a good language model.

It answers most questions. There\'s no obvious failure modes. I think maybe Michael, do you want to comment on that? I know it\'s another big project and then we can go back to Mamba, even though it\'s slightly out of order in the chronological, the release cycle that happened. sure.

\[00:11:33\] **Michael Poli:** So, I guess I\'ll start by saying that, there\'s an interesting connection between all these, these new methods.

there is this sort of convex set, which has a center and there\'s this connection between linear attention. So attention without the softmax, linear RNNs. And states based models, SSM. So at some level, kind of the mathematical formulation of this kind of base model here, I\'m not talking about the base architecture, just the fundamental model is the same.

And then you can go in different directions. And each direction has its own tradeoffs. You can go to, the feature map, direction, the kernel direction. So when you, when you break down the softmax, you take away the softmax. You can place, on queries and keys. Kind of the fundamental, the entities that compose your attention matrix, you can compose other kernel like functions, other functions that you hope would approximate whatever capability of attention you like.

You can do things like a, like a Taylor approximation, Taylor expansion, for example, of that. And you, you, you have a slightly different perspective, but you get something that again, is very similar. You can go to Time variance. So you take the RNN and you push this input dependence. So the way the \[00:13:00\] computation inside the linear RNN is conditioned by the, by the input sequence, and you can have things like gates, we\'ve seen a lot of work, for example, modernizing the inner tension with additional gates.

that allow you to make better use of your, of your fixed state dimension. And then you have the third direction, at least in my mind is the one that pushes, that uses the convolutional form that pushes more towards other types of, of linear operators that are still associative, that are, that are still, that are still allow you to, to train in parallel.

So here are things, time invariant systems. I can elaborate on any of these points, but things that can switch between convolutions and recurrence like this for a model with additional. Gates again, scraped. I, you know, was born as a, as a project, from the, in architecture, which belongs to this third category that I just mentioned.

And we\'re really trying to get the best per flop \[00:14:00\] architecture that we could. And. one principle that was validated over and over again, and we\'re trying to, to, to understand better now is that it seems composing hybridizing different, layers, layers, different blocks of different categories, and even full attention yields something that is better than the individual components.

So there seems to be a compositional aspect of these, of these models that we\'re trying to understand better. And this gives you a better sort of, pre trained model per flop. And with, with this model, we, we ran a whole suite of scaling laws and so on. Hybridizing also gives you, since we wanted something that would be kind of usable out of the box, it gives you a way easier time.

When you, when you\'re fine tuning for longer context, we can apply some of these techniques that have been developed for transformers and kind of surprisingly work okay for a hybrid \[00:15:00\] hybrids as well. So things like, linear scaling for rotary embeddings and so on, you can go into the details. So it was mostly a project trying, what is the best given the current landscape, what is the best we can do?

### What is Mamba

\[00:15:11\] **Nathan Lambert:** Yeah, that\'s a great description of it. I mean, the sentence in the blog that\'s like, Striped Hyena is optimized using a set of new model grafting techniques, enabling us to change the model architecture during training, kind of felt like, to me, that there\'s a ton going on there. And like, some of it, you probably can\'t talk about, there\'s normal data.

So like, I don\'t think all the data that was quite explained, like what the longer context data was, but it\'s like, are you taking this from models, starting point from models that people would know? And can you say any of that? I think even just the summary that it\'s a synthesizing recent work into a strong model is great context for people.

\[00:15:48\] **Michael Poli:** Yeah. Well, the deadline, so we\'ve, given this explosion of, of primitives that, you know, describe, and given sort of the, the \[00:16:00\] cost that it would require to evaluate all different combinations, we found ways to essentially start training. With a configuration and then continuing on with another configuration.

I think we\'ll have, we\'re going to have more work or a paper.

\[00:16:16\] **Nathan Lambert:** Yeah. There\'s so much cool work in that area. So one of the, someone at AI too is working on a project where they\'re essentially trying to cut the Lama models in half and keep training them. And things, it\'s just the wild west out there with people trying to take strong models and make them smaller while still getting the performance benefits of bigger models.

I think that\'s a whole aside, but. I wasn\'t expecting it to show up when people, when like you follow the social media, I\'ve striped by, you know, people are like, Oh, state non attention models are finally good. And it\'s like, it covers up a lot of the details that are very interesting about it, in my opinion.

So, okay. Turn back to treat, I think. Mamba actually happened first among these, I did the, his reading back of \[00:17:00\] social media, and it also was very surprising to me, I think the, the largest model in the Mamba suite is 2. 8 billion parameters, if I remember correctly, and it was compared to a lot of the common benchmarks in open NLP, so things like GPT J, Pythia model suites, and the scores on the benchmarks reported were really strong, and I think if you want to start with the high level summary, and then I\'m definitely going to make you talk about the awesome new CUDA kernels and stuff that you had to write for this project.

\[00:17:34\] **Tri Dao:** Yeah, so this, Mamba is a collaboration with, with Albert Gu, who\'s now, he was, a PhD student at, at Stanford, that\'s where we met, and, he\'s now a professor at CMU, and, also at a startup. so it was a, a wonderful collaboration, credit goes to him. Yeah, Albert has been working on this line of work called state space models, \[00:18:00\] in some sense, as mentioned, it connects to things like linear tension, linear RNN, convolution, neural nets, and, that\'s what his PhD thesis, is about.

I\'ve also worked on, space, state space for the past couple of projects, My, my angle is how to make state space more hardware efficient and, kind of increase their expressiveness. so it\'s wonderful working with, with, with Albert. and there, I think is more of a proof of concept, which is, Can state space actually do as well as transformer on language? So we\'ve, we\'ve seen previous papers, showing state space could be better on audio, could be better on, some of the tasks on the long range arena. but, language has always been, the most difficult to get, to, to, to do well for state space models.

\[00:19:00\] And, language is also kind of the thing that People care about the most right now. So I was more of a proof of concept, which is, Hey, we want to show that safe space space can be competitive or maybe even meet some of the transformers out there. so we, we validate that at the scale up to three B trained to 300 B tokens.

So in absolute terms, you know, these are not very strong models. These are not yet models that you would actually. play with and expect it to do meaningful things, I think is more of a, more of an academic comparison in terms of architecture. It\'s like, hey, training, train for the same amount of tokens, it does as well, or maybe slightly better than some of the transformer out there.

So, and that\'s, in particular, it\'s been, very exciting to us. I think, Albert\'s been pushing on this for, for a while. I\'ve been pushing on this for a while, and I think finally, it\'s like, It seems to, \[00:20:00\] to, to finally be kind of close to gap or even surpassing the transformer. and it just, just, I think it\'s opens up a bunch of opportunities.

so inference could be way faster. maybe we would have different ways to understand how in context learning happens, et cetera. So, lots of, lots of future work I would expect.

### Mamba hardware optimization

\[00:20:22\] **Nathan Lambert:** Yeah. Can you go into some of the like, what does it actually take to implement some of these new CUDA kernels? I just remember when this paper was announced, Sasha Rush, who\'s also very active in the space, recommended me to talk with you too, was tweeting about the types of files or whatever.

In the paper, there\'s this discussion about how like the recurrent state needs to be sufficiently expressive, but doing so in a certain type of memory is a problem. Like translate what this means to like people thinking about GPUs and people thinking about these models being scaled, like, is it now? Much easier to scale these \[00:21:00\] models because they work on GPUs.

Which GPUs were you using? Is there a bump that could come just from going to H one hundreds or something? Any of that?

\[00:21:08\] **Tri Dao:** Yeah. so, the pre, the line of work on state space, like s four models, kind of pioneer by, by, my Alberts work. they, they c are in some sense recurrent neural network. but they have a much larger, So, the state size is whatever kind of, buffer that you\'re going to store information as you traverse or as you process the sequence.

In some sense, you can view transformer as doing that as well, where it\'s, keep the entire history is usually called the KV cache. it keeps the history and keep referring to it. for RNNs, they have a fixed size state. for transformer state, you can think of the state size is increasing. And, our intuition \[00:22:00\] is that, the larger the state size, the easier it is for the model to do well.

So basically, you have more space to store whatever you need to remember. And so previous models like S4 and so on, they have an implicitly pretty large state size, but they use the convolutional view to avoid having to materialize the state. So that was, that was wonderful. Michael has, has worked, behind the architecture, has used some of the same insight focusing on, on convolution.

Mamba, on the other hand, focuses on the recurrent view. So, we wanted to put more input dependency in the, the, the recurrence. we thought, you know, the thinking was that it was going to make, it more expressive and the model would do better, but that prevents us from using this convolutional view that would make things efficient.

So we had to figure out a different way to make things efficient. and, so I, I focused on making that efficient on, on, on GPUs. and so all, you \[00:23:00\] know, our thinking was, instead of, okay, we\'re gonna have a large state size, but we don\'t have to like ride to actual GPU memory, like the HBM, we can just keep that, large state in a, a faster, Memory you call SRAM, you think of it as a, as a cache. so if you\'re more familiar with, CPU, so this is usually a cache and RAM. So, you know, if you have large state, you can keep it in the cache and you don\'t, by avoiding having to write it down, you actually don\'t suffer too much if the state is, is large.

### Predictions for 2024 architectures

\[00:23:33\] **Nathan Lambert:** Would this be due to like input out, like having to move the data around being really slow? Yes. Yeah. That makes a lot of sense. Thanks. That\'s a really common constraint in a lot of these things, and it\'s like, right. I think one of the most insightful things I\'ve had now with GPUs versus TPUs and stuff is how mixtures of ex mixture of expert models doesn\'t work very well in TPUs, just because you have to like that essentially add a mixture of expert at a basic level.

There\'s a routing layer that you learn, \[00:24:00\] and then multiple feedforward layers that you can choose from. And when you\'re distributing this, the feedforward layers could end up. On a different TPU node and TPUs communicate with their neighbors. So TPUs take a big hit relative to GPUs where within video class and video clusters, everything\'s connected so much more.

And then it\'s easy to do that sort of distributed training. And that\'s super interesting. And it\'s like, do you think there\'s going to be, I guess this is really where I want to open the conversation of like, what does this mean? What is going to happen in 2024 in this space? Are bigger players going to move in and be exploring this my take, seeing how good the long context learning could be in a fundamental limit is that systems like chat GPT are going to use a dense, like a transformer model for most tasks.

And then if you need to do summarization, you might do a long context specialized architecture. And then we can even see a whole quiver of architectures behind \[00:25:00\] something that you\'re using. But I think. It\'s just like, is attention going to be dethroned? Is Sasha Rush somehow going to win this bet that everyone was following in the area?

I got, what are you thinking about either of you?

\[00:25:14\] **Tri Dao:** I think transform is still a very, very strong architecture. and there is a proven recipe, right? You know, people scaling to a trillion of parameters right now, if you want, you say, well, I just want the best performing model. that runs most efficiently on my hardware that has the most support on on the software side.

Fast forward is a safe bet. I think it\'s here to stay. but I think there are new ideas, like, state space, kind of, some of the linear attention ideas from linear attention. I think they\'re coming in. we\'ve seen, as Michael mentioned, that mixing some of these components seem to improve performance, revalidated at, I think, seven B scale, but, Maybe it might even work at larger scale.

I think \[00:26:00\] people tend to be conservative and, you know, focusing too much on modern architecture, might not be worth their time. Like the Lime architecture is very, very strong. Most people are doing off of that. They\'re focusing on data. they\'re focusing on infrastructure, which makes sense. I think on, on my side personally, just plain interesting.

They\'re like more, I would say niche use cases. niche for now, where some of these alternative architectures are interesting, things like long context, different domains like audio and genomics, and there\'s just plain interesting scientific questions you can ask, like whether it follow instruction just as well, whether it follow intuition just as well, does it play well with quantization and so on.

That\'s just plain interesting. Research questions we can ask. Now on the production level, I think Transformer is still incredibly strong, very well supported, both hardware and software. But I think some of these new ideas are coming in \[00:27:00\] and people might start, you know, putting them as part of a component in the Transformer.

Maybe we\'ll still call them Transformer, but they just have more, more layers and just attention and NLP.

\[00:27:11\] **Michael Poli:** Yeah, I 100 percent agree with you. So attention as a, as a computational primitive is not going anywhere anytime soon. It\'s just a very efficient and a very convenient way to. Increase the effective state of, of your sequence processor. so at some level, if you\'re working with a model that only has a fixed state in each of its sequence mixers, you\'re, you have an assumption and your assumption is that you only need so much information in the sequence.

So there\'s, there\'s always a trade off between, this kind of the ratio of the state dimension, the sequence length, as you push things to the extreme, either model sizes. So as you make the model bigger, wider, effectively \[00:28:00\] introduce more states and sequence length, some of these margins. you know, some of this is speculation, but some of these margins will disappear, some of the trade offs will change, especially 14, 30, some of these very fat models.

But certainly either whether that\'s hybridizing or some kind of new, new block, we\'re certainly going to see some more innovation. That\'s, that\'s really exciting. My, my personal, if I had to make a prediction is that architectural design will get more interesting, more, more complex. There\'s going to be more to do.

### More predictions for AI

\[00:28:38\] **Nathan Lambert:** Yeah, I mean, this year it\'s like, I got some 10 minute clock that\'s fine for us. I think like with mixture of experts and this being popular as a state state models, like this is all just really within a few months outside of opening. I like they\'ve been doing mixture of experts for a lot longer than everyone.

In terms of open and academic \[00:29:00\] communities, like no one\'s really tried to do early Jeff on mixture of experts. Like it should just work, but we have to learn all these things. And then the model grafting is becoming more of a real thing. That\'s super interesting. It is just. I agree that it\'s just fun to follow and hopefully it gives academics and scientists more ways to influence the conversation where an industry is just about scaling and bigger models where we could maybe do specific things better, which is what I\'m telling open source companies to do with their language models anyways.

Like if they want to have a business model, they need to have an edge. So this all fits into that kind of narrative pretty well with my regards. Is there anything else you guys are following in ML? It doesn\'t have to be about state space models. Like what\'s, what\'s exciting for you broadly for next year?

\[00:29:46\] **Tri Dao:** Yeah, personally, I think data is still the most important thing. we\'re, we\'re thinking a lot about how data influences the model performance, like really teasing that \[00:30:00\] out, either, you know, having some of the synthetic tasks that correlates very well with, with model performance. That\'s been kind of the motivating.

kind of examples in a lot of our papers and work has been focusing on synthetic tasks, or, having like maybe, maybe smaller data sets that kind of make it easier to really understand what\'s, what\'s really going on. so, I think I\'ll, you know, personally, my focus is going to be on data for the next little bit.

Yeah, all the, all the architecture stuff is fun. making that hardware efficient is, is, is, is fun. but I think, ultimately it\'s about data. If you, if you look at the scaling, scaling law curve, the more architectures. Different model architectures would generally have the same slope. They\'re just different offset.

it seems like the only thing that changes the slope is the, data quality.

\[00:30:58\] **Nathan Lambert:** I love that point. That, that does \[00:31:00\] seem true. I have the plot from Mamba in this blog post that I\'m writing, which is, it\'s just a little, just a little bit above the same slope.

\[00:31:08\] **Michael Poli:** Yeah, we add data. Data is really interesting, sort of miniaturizing, architecture design, finding and breaking down what, tasks are involved into, for example, language modeling and trying to package them into something that can be used to iterate something that\'s quite exciting. We have, that was one of the main techniques that was used for the, this, zoology, paper that also looks into, into some of these different behaviors.

And personally, I\'m also really excited about new applications, scientific applications, with the genomics work, but even more, but more engineering focused, we\'re seeing a shift, right now it\'s language is still kind of, The domain that gets the most clicks, \[00:32:00\] most interest, but I think that that will evolve over time.

and some of these other applications offer, even just talking about architectures, they offer a completely different design space that I\'m excited to look into.

\[00:32:13\] **Nathan Lambert:** Yeah, everyone talks about language, but I feel like images and entertainment and videos are like the things that are so obviously going to generate so much value to me.

Like, I don\'t know the ceiling on language, but when you could access a like somewhat local text and video model at your home workstation, that\'s like tailored to your preferences. Like the amount of value that that creates is totally astronomical. I I\'m excited. I mean, I\'ve started playing around with these where I\'d take.

Text of the blog and convert it to dolly images and convert it to a video with generated audio all with like one Python script and it\'s like, that\'s really easy to do. So I agree with your more than language is fun to have that view

\[00:32:55\] **Tri Dao:** and these things actually do work reasonably well in your experience when you stitch \[00:33:00\] all them together.

\[00:33:02\] **Nathan Lambert:** it\'s not that good. The DALLE images are pretty similar, but I\'m doing something really naive where I just, I literally take the text and have a system prompt. It\'s like you\'re generating series of images for visualizing a blog post and, and it generates various like. The, all the machine learning thumbnails that you see everyone using, they\'re like variations of that.

The fun ones are where it\'s like about Llama or Mamba or something. And then they like generate animals in them, which is good. I think I could get much better at it and have a better segmentation system for the paragraphs and, or have like chat to PT summarize them or something like that. But I just know that within like a year, it was going to be a text to video API and I\'m just going to switch it and it\'s going to be great.

And so I\'m like laying the groundwork for infrastructure to have like multimodal. Content as multimodal content distribution, really, and I just expect it to become very fun. I mean, like even the text to voice is pretty good. I think I don\'t have a studio, but once \[00:34:00\] you have a studio, it\'s going to be able to generate perfect audio for whatever you want.

So another one of my dreams that is. Bad for young students is I want to be able to give like a slide deck to a script that returns the five minute conference video that no one ever watches just based on like a, GPT for reading those, the slide deck and voicing yourself. So those are the silly things that I have time to do because I\'m not a professor.

\[00:34:29\] **Tri Dao:** Yeah, I think these, these, these advances, these systems, like they, they do generate a lot of economic value and, and we\'re seeing that already. Lots of companies are now switching to using these things. And I think it\'s going to change the way we work as, as you mentioned, the way we work, the way we\'re entertained.

So I\'m just very exciting future.

\[00:34:47\] **Nathan Lambert:** Yeah. Anything else? Well, thanks for coming. Try to get you guys as much. Attention as I can bring, you never know it\'ll go viral these days. So I think this was a great conversation. People are really hungry for basic intuitions in \[00:35:00\] the area. So this is good.

\[00:35:02\] **Tri Dao:** Yeah. Thank you.

Nathan is a pleasure. Absolutely.

\[00:35:07\] **Michael Poli:** for inviting us. And, maybe, if, you know, there are more questions, is there a way to maybe collect them or to, to provide readers with like listeners with, an address or something? Happy to answer anything.

\[00:35:24\] **Nathan Lambert:** Yeah. I\'ll, I\'ll include contact info in the post and various ways.

This will be out there. You\'ll get your comments on Substack, YouTube, Twitter. It\'s a mess. You\'ve got to pay attention to 10 million streams of information these days, but you\'ll, you\'ll get contacted by people. Thankfully, for some reason, people read my stuff, but here we are. So thanks for listening.
