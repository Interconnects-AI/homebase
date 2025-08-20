---
title: "Towards an Ethics for Roboticists"
subtitle: "How does one handle abstraction and scale in ethical design?"
date: 2020-10-30
type: newsletter
audience: everyone
visibility: public
post_id: 15405773.sketch-robot-ethic
email_sent_at: 2020-10-30T14:00:17.465Z
---
What does it mean to be a roboticist? The somewhat cliche nature of the title, epitomized by the numerous startup C-suite employees with subtitles "PhD in Robotics," leads to a more challenging problem of defining an ethics guides. The burden is on me to develop a rank-ordered guidelines for what people should consider in a broad sense --- and therein be educated in. The actual problems where these will be applied is in its nature flexible, so therefor the principles should be reordered. In this post, I hope to define a vector that can be a guiding principal for future development, which will be modified over time as the problem space becomes clearer.

Ultimately, autonomous agents affect everyone's lives, and the magnitude of effect will continue to increase in the coming decades. My primary goal is to figure out how to best design systems that a) do no harm to individuals and b) do not cause any societal restructuring from downstream multi-system interactions.

<div>

------------------------------------------------------------------------

</div>

# Data driven mistakes to individuals

The idea of individual hardship caused by AI systems primarily falls into the category of "Fair Machine Learning," a field that gained a lot of prominence among news like automatic policing profiling people, search results harming minorities, or hiring algorithms filtering people for unfair reasons ([here](https://github.com/daviddao/awful-ai) is a popular list tracking such failures, or see the [FAccT Conference](https://facctconference.org/index.html) and go from there). Building autonomous systems will include this type of risk, but it also will scale much more broadly. Personally, I hope that before robots are really doing every interpersonal task these problems will be long behind us (if ML isn't fair within a decade, we have bigger fish to fry).

Simply put: robot ethics needs to leverage AI Ethics as a foundation, and build something more concrete atop it. Having wrapped up a first draft of a comparative study of different areas of research that pertain to AI Ethics, here is the scaffolding we propose. Ultimately, these three subfields are silos of research trying to touch on sociotechnical system (STS) themes:

1.  AI Safety: value alignment and proving probability of extinction goes to 0.

2.  Fair ML: minimizing mis-uses of decision making algorithms that harm individual users or individual groups.

3.  Human-in-the-loop Autonomy (Human-robot Interaction HRI / cyber-physical systems CPS): avoid accidents and figure out how best to model human intentions in physical autonomous systems (there is an interesting argument to be made from these fields, one is primarily from the CS side --- HRI --- and one from the EE side --- CPS --- where the goals take the form of resiliency, how to return to normal operation post unexpected event, and robustness, ability to handle an unexpected event).

The crux of our paper is figuring out how to avoid traps that hinder the beneficial joining of CS research with STS themes, and how graduate students stand to be a potential point of intervention. The rest of this argument is for another time, I may include snippets of the history of these subfields of AI Ethics in a future article, they are fairly enlightening. I'm including a couple paragraphs we wrote on the nature of Human-in-the-loop Autonomy because it seems extremely relevant here, and transitions well to the ideas of the next section:

> As many of the earliest robotic systems were remotely operated by technicians, the field of robotics has always had problems of human-robot interaction (HRI) at its core. Early work was closely related to the study of human factors, an interdisciplinary endeavor drawing on engineering psychology, ergonomics, and accident analysis. With advancements in robotic capabilities and increasing autonomy, the interaction paradigm grew beyond just teleoperation to supervisory control. HRI emerged as a distinct multidisciplinary field in the 1990s with the establishment of the IEEE InternationalSymposium on Robot & Human Interactive Communication.Modern work in this area includes modeling interaction from the perspective of the autonomous agent (i.e. robot) rather than just the human overseer. By incorporating principles from the social sciences and cognitive psychology, HRI uses predictions and models of human behavior to optimize and plan. This work mitigates the sociotechnical risk of accident, defined specifically as states in which physical difficulties or mishaps occur, by making models robust to their conditions.
>
> Digital technology has advanced to the point that many systems are endowed with autonomy beyond the traditional notion of a robotic agent, including traffic signal networks at the power grid. We thus consider the subfield of HIL Autonomy to be the cutting edge research that incorporates human behaviors into robotics and cyber-physical systems.This subfield proceeds in two directions: 1) innovations in physical interactions via sensing and behavior prediction; 2) designing for system resiliency in the context of complicated or unstable environments. These boundaries are blurring in the face of increasingly computational methods and the prospective market penetration of new technologies. For example, the design of automated vehicles (AVs) poses challenges along many fronts. For more fluent and adaptable behaviors like merging, algorithmic HRI attempts to formalize models for one-on-one interactions. At the same time, AVs pose the risk physical harm, so further lines of work integrate these human models to ensure safety despite the possibility of difficult-to-predict actions. Finally, population-level effects (e.g. AV routing on traffic throughput and induced demand) require deeper investigation into interaction with the social layer.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/252b5c49-7ff7-4f92-a00e-3dbe4525efac_2034x1136.png)

Source - Author\'s Work.

Back to robots. If something is messed up physically, it may be more immediately noticeable, but there may also be phenomena that emerge as the number of agents interactions grow exponentially (if every agent interacts with each other agent, 5 agents have 20 pairwise interactions and 100 have almost 10,000). These interactions between autonomous systems likely will be harder to model, predict, and prevent (like what I was getting at when [talking about recommender systems](https://democraticrobots.substack.com/p/recommendations-are-a-game-a-dangerous)).

<div>

------------------------------------------------------------------------

</div>

# Societal restructuring

As the adoption of autonomy accelerates, the impact of robotic platforms scales from individual effects to societal effects. For example, one autonomous vehicle represents a dangerous piece of modern art to most pedestrians these days, but when the percentage of those reaches something more appreciable, say 10%, the fleet of autonomous cars and their interactions may come to define what it means to be a pedestrian --- humans no longer are in the driving seat for when to cross a road. The most frequent mode of this fleet-wide interaction I have encountered is more effective traffic flow, but there really is nothing preventing deleterious emergent phenomena.

Autonomous vehicles are the *first born child* in a way of modern autonomy, they're the application everyone follows and has huge backing for it to work out, but that does not mean it will be the one to be dramatically impactful.

### Ethics at scale

There are many ethical considerations at play in modern digital (and soon to be embodied) systems: There are competing political and economic interests, questions of automation replacing jobs, abstract effects of person to person ethics, and more. I think the crux of developing an ethics guide is reasoning about scale. Computer scientists are renowned for their ability to work in abstractions, but I worry plenty of people abstract away the ethical decisions --- once it is outside of your bounding box it is someone else's problem. To be honest, the ethic should be at play from the first user on, but most start-ups likely do not consider it until they need to (who can blame them).

The physical nature of robots and autonomy may elicit more direct, evolutionary reactions to poor ethical judgement in technology. I think this is my solace and why it is worth pursuing --- generally, I have a lot more faith in my fellow humans to response well to challenging events *off screen*.

Engineering involves design decisions at a low level, and this is the case for machine learning too: make a specific decision under an assumption of uncertainty. As the design principles do not account for the complex system interactions, I don't think there are cliche governing principles that an autonomy engineer should follow. I think it's about being able to shift abstraction frames, being well read, and have discursive engagement vertically across implantation stacks when creating products.

Ad-hoc, built up guidelines is how autonomy ethics will be enforced. It is upon the practitioners to make better decisions earlier so that they have say in how the system runs, and not relatively uninformed policy makers across the country.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/a4f525b4-5c1c-47eb-99be-8fe28c25ad1b_4000x2250.png)

Photo by sergio souza from Pexels.

# Ad-hoc Guideline Development

I was forced my PhD program to have an outside minor, and in the process I learned a lot about the therapeutics development process and the FDA (course was an earlier iteration of [this](https://classes.berkeley.edu/content/2019-spring-bioeng-153-001-lec-001)). Ultimately, the brief history of the Food and Drug Administration (FDA) in the U.S. is: *people messed up, we applied a bandaid to prevent this in the future*. Avoiding deep economic and philosophic arguments, I think some amount of this approach is a prerequisite for free markets --- patching all areas of concern would likely stifle innovation. This is how technology policy has been created and likely will continue to be done.

Computer science is at an inflection point where the regulatory body does not fully exist for their problem space, but people are starting to ask questions. An alternate to delayed, sweeping regulation: *make better actors*. This is what I am trying to do for myself and those I work with on problems of robotics --- be better for the world. We'll see how everyone's decisions play out on a decade or two time lag.

### Current curriculums

For comparisons sake, I wanted to illustrate how most professional fields do have some sort of ethical components to training and practice.

1.  **Medicine**: there are ethics components in the coursework of medical school, questions on qualifying exams, and oversight on a per-hospital basis.

2.  **Law**: lawyers pass a cursory ethical component in the BAR exam.

3.  **Finance**: among many insider trading and other shade-prevention laws, about 10% of Chartered Financial Analyst curriculum is ethics training (very common accreditation program for financial management institutions).

4.  **Phycology**: they have their own [defined ethics code](https://www.apa.org/ethics/code) based on four principles: beneficence and nonmaleficence, fidelity and responsibility, integrity, and justice.

Clearly, computational fields are behind. When you do the research, every other field has ethics guidelines, and computation is becoming a behind-the-scenes player in every field (sadly, there's not inheritance of ethical guidelines when you take your talents to a different application space). Shoutout to UC Berkeley's data-science program that has one of the first required ethics courses <https://data.berkeley.edu/hce> (go Bears).

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/afc17d19-be9d-4a1c-b9c8-af9b8a9e00bc_5760x3840.png)

Photo by Sebastian Voortman from Pexels.

<div>

------------------------------------------------------------------------

</div>

So, reading through this, you may think "*how can anyone be expected to keep up with all of this, and still create groundbreaking innovation*?" I agree, this is a lot. I'm hoping to keep figuring out what the central challenges and issues to address are. This is part of a bigger project, where I want to design this sketch into a curriculum, stay tuned for more work in this direction, and reach out if you want to be involved. *These boundaries are blurring in the face of increasingly computational methods and the prospective market penetration of new technologies*.

**What do you think should be added to the ethical guidebook of someone working on automation?**

<div>

------------------------------------------------------------------------

</div>

Hopefully, you find some of this interesting and fun. You can find more about the author [here](https://people.eecs.berkeley.edu/~nol/). Tweet at me [\@natolambert](https://twitter.com/natolambert), reply here, email [democraticrobots@gmail.com](mailto:democracticrobots@gmail.com). I write to learn and converse. Forwarded this? Subscribe [here](https://democraticrobots.substack.com/).

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c4c238b0-59fa-467c-8b8f-c0f1fd25370a_1100x220.png)
