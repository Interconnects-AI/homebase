---
title: "Ilya on deep learning in 2015"
subtitle: "On vision and how to understand deep learning."
date: 2025-06-28
type: newsletter
audience: everyone
visibility: public
post_id: 166979915.ilya-on-deep-learning-in-2015
email_sent_at: 2025-06-28T18:02:32.683Z
---
Ilya Sutskever is renowned for his vision when it comes to deep learning. A lot of his now popular quotes come from his [2023 appearance on the Dwarkesh Podcast](https://www.dwarkesh.com/p/ilya-sutskever). I was recently sent this clip of him discussing deep learning in 2015 and was taken aback by how correct he was so long ago, and particularly by how little has changed. With this, I wanted to share an annotated transcript with my thoughts.

The core of it is that Ilya saw the truth of deep learning better in 2015 than plenty of people do today, 10 years later.

This excerpt is from a no longer running podcast, [Talking Machines](https://feeds.acast.com/public/shows/talking-machines). A backup of the file, trimmed just to the Ilya portion, is included here. A full transcript follows the annotation.

::: {.native-audio-embed attrs="{\"label\":null,\"mediaUploadId\":\"f0bd1aef-ad0f-4960-9a23-93769172ca0f\",\"duration\":1082.9061,\"isEditorNode\":true}" component-name="AudioPlaceholder"}
:::

In editing this, I was struck by how strong Ilya's voice came through even just in the transcript.

Ilya starts by explaining his path to AI, which is unsurprising for such a prodigious figure.

> I was always interested in artificial intelligence as a teenager.
>
> I thought it was very nice and fascinating. And then I went on to study mathematics as an undergrad. And when you study math, math is very much about proving things. It\'s very much about if you see a certain pattern, it doesn\'t mean that it will be true unless you prove it. And so learning seemed to be very counterintuitive to me coming from a math background because learning is all about making these inductive steps which seem to be impossible to justify from a rigorous approach.
>
> If you are used to rigorously proving results, it seem induction seems almost like magic. So I was so I was interested especially in learning because of that because I knew that humans do it, and it seemed impossible from a from a naive mathematical view that that learning seemed impossible to me. And so I looked around, and it turned out that Toronto had a very nice, very strong learning group. And I started working with Jeff Hinton while I was still a second year undergrad. It really is the case that machine learning is complicated science.
>
> It\'s not like physics, I think. I think that in physics and math and a lot of these other hard sciences, there is a lot more ground needs to be covered before a person can start to be useful. Although I\'m not sure because I\'ve never done this. This is my impression. **Whereas machine learning is a lot more the the ideas, the important ideas, even the ones that are related to cutting edge research, are very close to the surface.**

The end of this anecdote matches much of my feelings today, particularly at a laboratory off the true frontier of training. The amount of low hanging fruit that is around --- without looking particularly hard --- is astounding. Much of what makes deep learning work is that people are willing to do the work to harvest the opportunities. Like many of the great technological trends of the last decades, e.g. Moore's law, it's not that the laws are automatic, but that the visionaries and leaders of the field push incredibly hard to capture the potential on a rapid time frame.

Much of my job is pushing people to have consistent urgency in taking these gains. With this, he also agrees with my take on getting up to speed:

> It doesn\'t take many years of study to be able to understand the main ideas behind machine learning and the main ideas behind what works and the main intuitions with the right guidance and direction.

Getting up to speed is easy, so long as people are approaching the simple opportunities and not trying to be fancy.

> So can you tell us a little bit about the research questions that you\'re working on now? Yes. So I was working on supervised learning. So supervised learning is the most successful aspect of machine learning by far.

The hosts then asked Ilya to explain his recent work, which was at the foundations of supervised learning for image classification. The background is something we've heard many times, but Ilya continues onto another core point of where deep learning gets its answers.

> So you say, okay, **the data will tell us the best connections**. Because the deep neural network is such a powerful, it\'s such a rich model, it can do so much non trivial work. **It\'s very hard to imagine what kind of things it cannot do**.
>
> Because of that, whenever we have a large data set, we can apply a simple learning algorithm to find the best neural network and get good results. So I was working on extending the deep the supervised learning approach of neural networks to the problem, to the supervised learning problem where the input is a sequence and the output is a sequence. **So this is really, conceptually, it\'s not different from what I talked about before. It\'s mainly a technicality.** It\'s making sure that the model will know what to do when the input is a sequence whose length is no longer fixed in advance, and the output is also a sequence whose length is no longer fixed in advance.
>
> But it is the same basic approach, and it uses the same basic learning algorithm. And so, again, because these models are so expressive and powerful, they can really solve a lot of difficult, nontrivial pattern recognition problems, and **problems that would be almost unimaginable to solve by any other means**. And again, what\'s so surprising about it is that even though the approach ends up being so powerful, it truly is extremely simple to understand. The learning algorithm is extremely simple. **It takes maybe it would take a smart student only an hour to understand why it all works.**

To him, applying successful techniques from image classification to sequence classification (i.e. closer to text) with deep learning was "just a technicality." Much of what people are doing is more of making a data-loader for the model, rather than the architectures we come up with being particularly novel. It's a stretch, but him being so data and generality focused inclines me to think that something like the transformer taking over the entire field of ML wouldn't be surprising to him. The transformer architecture was an efficient way to let deep learning do the work we need.

Ilya then continues to explain a subtlety of model initialization that can get in the way of the model learning. This is the best explanation I've read on why initializing is sensitive and is a problem many still face today --- getting the initialization wrong fundamentally limits the final performance of your model, even if your data and infrastructure is perfect.

> The neural network objective function is a very complicated objective function. It\'s very non convex, and there are no mathematical guarantees whatsoever about its success. And so if you were to speak to somebody who studies optimization **from a theoretical point of view,** **they would tell you that there is no theoretical reason to believe that the optimization will succeed. And yet it does. And this is an empirical fact.**

That fact is feeling the AGI back in 2015.

> It is not something that theory has much to say about. And it is this part which is, you know, it is not magic of course, but it is poorly understood. We don\'t really know why our very simple optimization algorithm, which is fundamentally a heuristic, works as well as it does on these problems. Because it doesn\'t there isn\'t a mathematical theorem. There isn\'t a theory which says that it should succeed.
>
> I think some of this has to do with **a fairly limited definition of success that people in the convex optimization literature create**, which is to say, are you guaranteed to find the global maximum or the global minimum for convex problems of this objective function? And I think the reality is is that we have a loss function and we have some way to measure whether or not things are working. And you can think of it this iterative optimization as just gradually getting better. Now, the the theorems that we would like to have are about the idea that I have the best one.
>
> **But in no way is human intelligence the best possible intelligence and any engineered system that we have that\'s successful for airplanes or cars or or anything else. These aren\'t the best systems. We just want good systems.** And the the kinds of things that we get with with deep learning and with non convex optimization are perfectly good systems that may not be the best but are nevertheless useful and interesting. It\'s true.

This is a wonderful point. Much of the world seeking optimality, particularly in academia, misses the targets for what is good. Deep learning is a science about doing good enough with the resources that we have, and while the resources and fundamentals are progressing so fast, good enough is remarkably good artifacts. The good enough attitude is a large motivator for why modern AI is seen as more of an alchemy than a science, where scientific norms were established with methods that proceeded at a far slower rate.

Onto a specific counterexample people used to give for deep learning.

> But if we go back in time 2002/2006, at this time it was widely believed that deep neural networks that we train right now with our simple optimization algorithm, which is called gradient descent or back propagation, **by the way, it was believed that, let\'s say, neural networks with 10 hidden layers simply cannot be trained**. And so it seemed perfectly plausible, and in fact, this was also the empirical experience, that if you take a 10 layer neural network, you randomly initialize it, you start doing back propagation, you will not get any sensible result whatsoever. And that would also be perfectly consistent with what we expect from non convex optimization. **You could imagine that there is just so much complexity that there\'s just no way for the poor gradient to know how to get it off the ground, so to say.**

Lazy scientists end up with "poor gradients." Those who believe give it space to learn.

> And yet over time, we discovered that actually the mistake that scientists were making is that they simply weren\'t paying enough attention to the scale of the random initialization.
>
> So when you train a neural network, I mentioned that it has all these connections between the neurons. And the connections have numerical values that determine their strengths. And our algorithms, like Ryan said, they improve the solution. They are based on the idea of continuous small improvements, but you need to start somewhere. And so typically, researchers would start with small random weights.
>
> And apparently this was simply wrong. Apparently **you need to be very careful with the scale of the random weights** and if you\'re careful with the scale then you will find the right scale or it turns out that it is possible in very many cases to find the right scale so that simple back propagation, the simple gradient is able to improve it and to get it off the ground and to get good results. So there is I mean, I still feel that it\'s a very fortunate situation that the simple gradient descent is able to train deep neural networks.

Skipping ahead, Ilya's comparison to the work in 2015 relative to the "early times" of deep learning sounds exactly how we would compare today to 2015.

> So several things have changed since the early times. **We have more data, more computation, and we know how to train these models.**

The trajectory we are on today is just the end of a trend line tracing back to even before AlexNet.

Back to the initialization explanation.

> The the scale of the random initialization is related to our ability to train these models. There are there are specific nontrivial things we can say about the random initialization. The way to think about it is that a neural network, it has all these neurons and connections. And the way it works is that you take your input and then you multiply it by the random connections, and then you do a tiny bit of nonlinear processing in the neurons again. So you you take you you got your input, you multiply it by the random connections, and you apply a small nonlinear processing.
>
> And you do it again by the next layer of random connections. You multiply it by the random connections, and you do nonlinear processing again. **And so what happens is that when the random connections are too small, as you keep on multiplying your signal by the random connections, it goes to zero. It decays.** And so by the time you get all the way to the output, there is no signal.
>
> The output has no relationship to the signal anymore. And our learning algorithm is very, very greedy. And it can only notice, it can only improve things. It can only improve the relationship between the input and the output if there exists if there is an existing relationship in place. And so **it is important for the random initialization to be large enough so that the signal doesn\'t decay**, and so that by the time you get to the output layer of your neural network, changes in the input layer will still create noticeable changes in the output layer.
>
> **And once this connection, once this condition holds true, then the gradient will be able to latch onto it and improve it**.
>
> ...
>
> So in practice, when a practitioner wants to train a neural net in a real dataset, the scale of the initialization is one of the most important parameters you need to worry about.

Much of deep learning is setting up your model so that you have consistent, predictable gradients without large spikes or decaying magnitudes.

With all of this, the summary of Ilya's implicit advice in communicating his intuitions is the same today:

1.  Embrace simplicity,

2.  Understand that much of modeling is setting up to get consistent gradients, and

3.  ML is not a hard field technically to spin up on (even if the resources are often hard to gain access to today).

<div>

------------------------------------------------------------------------

</div>

## Full Transcript

*Note --- questions from the interviewers are interleaved with this. It's still fairly easy to follow and mostly Ilya.*

I was always interested in artificial intelligence as a teenager.

I thought it was very nice and fascinating. And then I went on to study mathematics as an undergrad. And when you study math, math is very much about proving things. It\'s very much about if if if if you see a certain pattern, it doesn\'t mean that it will be true unless you prove it. And so learning seemed to be very counterintuitive to me coming from a math background because learning is all about making these inductive steps which seem to be impossible to justify from a rigorous approach.

If you are used to rigorously proving results, it seem induction seems almost like magic. So I was so I was interested especially in learning because of that because I knew that humans do it, and it seemed impossible from a from a naive mathematical view that that learning seemed impossible to me. And so I looked around, and it turned out that Toronto had a very nice, very strong learning group. And I started working with Jeff with Jeff Hinton while I was still a second year undergrad. It really is the case that machine learning is complicated science.

It\'s not like physics, I think. I think that in physics and math and a lot of these other hard sciences, there is a lot more ground needs to be covered before a person can start to be useful. Although I\'m not sure because I\'ve never done this. This is my impression. Whereas machine learning is a lot more the the ideas, the important ideas, even the ones that are related to cutting edge research, are very close to the surface.

It doesn\'t take many years of study to be able to understand the main ideas behind machine learning and the main ideas behind what works and the main intuitions with the right guidance and direction. So can you tell us a little bit about the research questions that you\'re working on now? Yes. So I was working on supervised learning. So supervised learning is the most successful aspect of machine learning by far.

It is a certain approach to machine learning where you say that you\'ve got lots of input output examples of a certain behavior you want to imitate. And then you take those input output examples and you give them to your machine learning algorithm. And it tries to it undergoes a process of learning. And when it\'s done, it understands to some extent the patterns that are in those input output examples. And then it can imitate this behavior to new examples that are not in the training set.

So let\'s say let\'s say you want to recognize and to determine what\'s the object in a photograph. So this is something for which it is relatively straightforward to generate a lot of input output examples by asking humans to look at an image and to tell us what\'s in it. Then once we have enough data, we can give this data to the model so that it will learn to imitate this behavior. The thing that\'s really successful is supervised learning with large deep neural networks. Now, there\'s a very specific reason why it\'s successful.

It\'s because large deep neural networks can perform all kinds of very complicated computations. And so when you use supervised learning with large deep neural networks, what you\'re really saying is the following. You\'re saying, give me the best possible neural network that can imitate this behavior. So of all possible neural networks, some of them imitate this behavior better than others. So the neural network, by the way, so when I say different neural networks I mean that the connections on the neural network they determine different behavior.

If you change the connections you change the behavior. And so the question becomes what are the best connections? So you say, okay, the data will tell us the best connections. Because the deep neural network is such a powerful, it\'s such a rich model, it can do so much non trivial work. It\'s very hard to imagine what kind of things it cannot do.

Because of that, whenever we have a large data set, we can apply a simple learning algorithm to find the best neural network and get good results. So I I was working on extending the deep the supervised learning approach of neural networks to the problem, to the supervised learning problem where the input is a sequence and the output is a sequence. So this is really, conceptually, it\'s not different from what I talked about before. It\'s mainly a technicality. It\'s making sure that the model will know what to do when the input is a sequence whose length is no longer fixed in advance, and the output is also a sequence whose length is no longer fixed in advance.

But it is the same basic approach, and it uses the same basic learning algorithm. And so, again, because these models are so expressive and powerful, they can really solve a lot of difficult, nontrivial pattern recognition problems, and problems that would would be almost unimaginable to solve by any other means. And again, what\'s so surprising about it is that even though the approach ends up being so powerful, it truly is extremely simple to understand. The learning algorithm is extremely simple. It takes maybe it would take a smart student only an hour to understand why it all works.

So do you find that that\'s true, Ryan? Do you find that the basics of machine learning are sort of easier to to get to and begin to manipulate than say in physics? I, you know, I guess I\'m not sure that I I exactly agree about how it relates to to physics, but I think I do agree that it\'s that the basic ideas are are straightforward, especially supervised learning, where as long as you can talk about what it means to do well on a task, as long as you can write down what we call an objective function that is we\'re sort of, say, maximizing this objective function corresponds to doing better. In this case, it\'s exactly this successful imitation that Ilya is talking about. As long as you can sort of write that down, then there are a variety of interesting tools to think about how to improve it, how to do the learning, which is then going to be maximizing that objective function.

Think neural networks people imagine that there is a lot of magic going on in them. But I think Eliud would agree that they\'re actually not magical, that they have a kind of a weirdly bad reputation perhaps because of the word neural. But in fact what they are is are sort of function approximators. They\'re they\'re adaptive basis function regression is the way that I I think about them. And that\'s something I think we can all agree is a good idea and not magical.

And I don\'t know, Elia, do you have a So I there are two so neural networks has two parts to them that make them work. One of them is not magical, but I think one of them is quite magical. So, neural networks, because they are large and deep, it is possible to arrange their connections so that their neurons will compute all kinds of complicated things, which among others often includes the solution to the problem you\'re trying to solve. Now Ryan alluded to an optimization procedure, which finds the best neural networks given the data that optimizes our objective function. It is the optimization which is a little bit magic in the following sense.

The neural network objective function is a very complicated objective function. It\'s very non convex, and there are no mathematical guarantees whatsoever about its success. And so if you were to speak to somebody who studies optimization from a theoretical point of view, they would tell you that there is no theoretical reason to believe that the optimization will succeed. And yet it does. And this is an empirical fact.

It is not something that theory has much to say about. And it is this part which is, you know, it is not magic of course, but it is it is poorly understood. We don\'t really know why our very simple optimization algorithm, which is fundamentally a heuristic, works as well as it does on these problems. Because it doesn\'t there isn\'t a mathematical theorem. There isn\'t a theory which says that it should succeed.

I think some of this has to do with a fairly limited definition of success that people in the convex optimization literature create, which is to say, are you guaranteed to find the global maximum or the global minimum for convex problems of this objective function? And I think the reality is is that we have a loss function and we have some way to measure whether or not things are working. And you can think of it this iterative optimization as just gradually getting better. Mhmm. Now, the the theorems that we would like to have are about the idea that I have the best one.

But in no way is human intelligence the best possible intelligence and any engineered system that we have that\'s successful for airplanes or cars or or anything else. These aren\'t the best systems. We just want good systems. And the the kinds of things that we get with with deep learning and with non convex optimization are perfectly good systems that may not be the best but are nevertheless useful and interesting. It\'s true.

But if we go back in time 02/2006, at this time it was widely believed that deep neural networks that we train right now with our simple optimization algorithm, which is called gradient descent or back propagation, by the way, it was believed that, let\'s say, neural networks with 10 hidden layers simply cannot be trained. And so it seemed perfectly plausible, and in fact, this was also the empirical experience, that if you take a 10 layer neural network, you randomly initialize it, you start doing back propagation, you will not get any sensible result whatsoever. And that would also be perfectly consistent with what we expect from non convex optimization. You could imagine that there is just so much complexity that there\'s just no way for the poor gradient to know how to get it off the ground, so to say. And yet over time, we discovered that actually the mistake that scientists were making is that they simply weren\'t paying enough attention to the scale of the random initialization.

So when you train a neural network, I mentioned that it has all these connections between the neurons. And the connections have numerical values that determine their strengths. And our algorithms, like Ryan said, they improve the solution. They are based on the idea of continuous small improvements, but you need to start somewhere. And so typically, researchers would start with small random lates.

And apparently this was simply wrong. Apparently you need to be very careful with the scale of the random weights and if you\'re careful with the scale then you will find the right scale or it turns out that it is possible in very many cases to find the right scale so that simple back propagation, the simple gradient is able to improve it and to get it off the ground and to get good results. So there is I mean, I still feel that it\'s a very fortunate situation that the simple gradient descent is able to train deep neural networks. So this is something that I I haven\'t heard somebody say out loud before. Maybe you\'ve been saying it for for a long time, but the there\'s a lot of different intuitions that people have about what has changed since sort of 02/2004, 2005 or since the last time that that neural networks were very popular in the machine learning community in the sort of early 90s.

And there are many different choices that you have to make. So what\'s your intuition? Can you expand a little bit more about the intuition of weight scale as being the important the important thing? Now, we\'re still talking about small random initializations, but maybe you mean extremely small random initializations or I\'d love to hear you talk more about this. Yes.

So this is a very good and important question. But you could actually ask two things. You asked about what changed, then specifically about the random initialization. So several things have changed since the early times. We have more data, more computation, and we know how to train these models.

The the scale of the random initialization is related to our ability to train these models. There are there are specific nontrivial things we can say about the random initialization. The way to think about it is that a neural network, it has all these neurons and connections. And the way it works is that you take your input and then you multiply it by the random connections, and then you do a tiny bit of nonlinear processing in the neurons again. So you you take you you got your input, you multiply it by the random connections, and you apply a small nonlinear processing.

And you do it again by the next layer of random connections. You multiply it against by the random connections, and you do nonlinear processing again. And so what happens is that when the random connections are too small, as you keep on multiplying your signal by the random connections, it goes to zero. It decays. And so by the time you get all the way to the output, there is no signal.

The output has no relationship to the signal anymore. And our learning algorithm is very, very greedy. And it can only notice, it can only improve things. It can only improve the relationship between the input and the output if there exists if there is an existing relationship in place. And so it is important for the random initialization to be large enough so that the signal doesn\'t decay, and so that by the time you get to the output layer of your neural network, changes in the input layer will still create noticeable changes in the output layer.

And once this connection, once this condition holds true, then the gradient will be able to latch onto it and improve it. So this is the intuition. But it\'s only related to training deep nets. Even if scientists had figured this out many years ago, neural nets would still not be useful. So can you say something?

I mean, it sounded like when you talk about applying these these linear transformations stage by stage, it it starts to sound like something, you know, like there\'s this area of random matrix theory where we can understand the, say, eigenvalues of random matrices. And this is getting a little bit technical, but this property of things decaying to zero is a kind of stability where some things are sort of stable in that they converge to zero or unstable in that they explode when you repeatedly apply a transformation. And what it sounds like you\'re saying is that the eigenvalues of these random matrices need to be around one. Is that fair? That\'s very fair.

This intuition is precisely correct. We definitely care about the size of the signal. If our eigenvalues are too small, if our matrices are too small, they will make the signal disappear. But it is also true that if matrices are too large and they will introduce so much instability into the system that learning will not be successful. And so there is this sweet spot of scale for the random initialization where things work well.

So in practice, when a practitioner wants to train a neural net in a real dataset, the scale of the initialization is one of the most important parameters you need to worry about. Now, Ilya, you\'re famous for several different things, but one of the things you\'re famous for is your work on recurrent neural networks, which are extremely deep. And did this intuition about what happens with a 10 layer neural network arise from your work on RNNs? It\'s all very connected. Yes.

RNNs are are neural networks which are adapted to deal with sequences. So the way they work is that you\'ve got imagine you have inputs coming in, you\'ve got a new input coming every second, and you\'ve got a new hidden layer coming in at every second which you compute. And you connections. You use the same weights to compute the new inputs. So it\'s a bit like a dynamical system.

It\'s responsive. It\'s very interesting. And so with recurrent neural networks, you always want to train them on long sequences because that\'s the interesting case. Unlike neural networks, where even a two layer neural network can be interesting, a recurrent neural network with two time steps is not interesting. And so you are naturally pushed to this regime where you have long sequences in recurrent neural networks, and then the scale plays an absolutely crucial difference.
