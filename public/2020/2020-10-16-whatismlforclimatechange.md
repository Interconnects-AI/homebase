---
title: "What is ML for Climate Change?"
subtitle: "A new “subfield” founded in 2019 is making waves, and is more accessible than I first thought."
date: 2020-10-16
type: newsletter
audience: everyone
visibility: public
post_id: 8318085.what-is-ml-for-climate-change
email_sent_at: 2020-10-16T14:01:03.506Z
---
In this issue, with the devolving world order, seeking positive, engaging work, I wanted to learn a) what actually is machine learning for climate change and b) are there reasonable paths for us to dive in and contribute? To quote the call for action in a paper I cite heavily later:

> *Groundbreaking technologies have an impact, but so do well-constructed solutions to mundane problems. *

[](https://substackcdn.com/image/fetch/$s_!RhOU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5cd48a3-3fc1-46fc-9722-61990f98f7d2_5867x3911.jpeg){.image-link .image2 .is-viewable-img component-name="Image2ToDOM" target="_blank"}

::::::: image2-inset
![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c5cd48a3-3fc1-46fc-9722-61990f98f7d2_5867x3911.jpeg){.sizing-normal attrs="{\"src\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/c5cd48a3-3fc1-46fc-9722-61990f98f7d2_5867x3911.jpeg\",\"srcNoWatermark\":null,\"fullscreen\":null,\"imageSize\":null,\"height\":971,\"width\":1456,\"resizeWidth\":null,\"bytes\":8242469,\"alt\":null,\"title\":null,\"type\":\"image/jpeg\",\"href\":null,\"belowTheFold\":false,\"topImage\":true,\"internalRedirect\":null,\"isProcessing\":false,\"align\":null,\"offset\":false}" fetchpriority="high" height="971" sizes="100vw" srcset="https://substackcdn.com/image/fetch/$s_!RhOU!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5cd48a3-3fc1-46fc-9722-61990f98f7d2_5867x3911.jpeg 424w, https://substackcdn.com/image/fetch/$s_!RhOU!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5cd48a3-3fc1-46fc-9722-61990f98f7d2_5867x3911.jpeg 848w, https://substackcdn.com/image/fetch/$s_!RhOU!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5cd48a3-3fc1-46fc-9722-61990f98f7d2_5867x3911.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!RhOU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5cd48a3-3fc1-46fc-9722-61990f98f7d2_5867x3911.jpeg 1456w" width="1456"}

:::::: image-link-expand
::::: {.pencraft .pc-display-flex .pc-gap-8 .pc-reset}
::: {.pencraft .pc-reset .icon-container .restack-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1yZWZyZXNoLWN3IiBmaWxsPSJub25lIiBoZWlnaHQ9IjIwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zIDEyYTkgOSAwIDAgMSA5LTkgOS43NSA5Ljc1IDAgMCAxIDYuNzQgMi43NEwyMSA4IiAvPjxwYXRoIGQ9Ik0yMSAzdjVoLTUiIC8+PHBhdGggZD0iTTIxIDEyYTkgOSAwIDAgMS05IDkgOS43NSA5Ljc1IDAgMCAxLTYuNzQtMi43NEwzIDE2IiAvPjxwYXRoIGQ9Ik04IDE2SDN2NSIgLz48L3N2Zz4=){.lucide .lucide-refresh-cw}
:::

::: {.pencraft .pc-reset .icon-container .view-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1tYXhpbWl6ZTIiIGZpbGw9Im5vbmUiIGhlaWdodD0iMjAiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgdmlld2JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBvbHlsaW5lIHBvaW50cz0iMTUgMyAyMSAzIDIxIDkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIHBvaW50cz0iOSAyMSAzIDIxIDMgMTUiPjwvcG9seWxpbmU+PGxpbmUgeDE9IjIxIiB4Mj0iMTQiIHkxPSIzIiB5Mj0iMTAiPjwvbGluZT48bGluZSB4MT0iMyIgeDI9IjEwIiB5MT0iMjEiIHkyPSIxNCI+PC9saW5lPjwvc3ZnPg==){.lucide .lucide-maximize2}
:::
:::::
::::::
:::::::

## **Recent work**

To start with, I knew there were a bunch of recent workshops on climate change and machine learning (such as [ICLR 2020](https://www.climatechange.ai/events/iclr2020), [ICML 2019](https://www.climatechange.ai/events/icml2019), [NeurIPs 2019](https://www.climatechange.ai/events/neurips2019) editions). When looking here, it turns out it is a centralized group of [climatechange.ai](https://www.climatechange.ai/). This seems good to me, but I was hoping to learn what people are actually working on.

I wrote a little script to scrape the titles and authors of the workshop proceedings and came up with this list of keywords (learned about NLP and [stop words](https://en.wikipedia.org/wiki/Stop_word) along the way). 

`LEARNING, USING, CLIMATE, DEEP, MACHINE, DATA, NETWORKS, CHANGE, SATELLITE, PREDICTION, IMAGERY, NEURAL, WEATHER, POWER, FORECASTING, ENERGY, TOWARDS, MODELS, CARBON, REINFORCEMENT, BASED, DETECTION, ENVIRONMENTAL, MONITORING, FLOW, VIA, DYNAMICS, FRAMEWORK, SOLAR, RISK, CLOUD, GRID, LEARNING-BASED, FOREST, CONSERVATION, SMART, ANALYSIS, OPTIMAL, MAPPING, URBAN, INTELLIGENCE, RENEWABLE`

I expected some buzzword-ness, but this was pretty much a non-entity in terms of teaching me what people are working on. Some keywords that provide insight may be this subset (remove data and learning description words):

`NETWORKS, SATELLITE, WEATHER, POWER, ENERGY, FLOW, SOLAR, DYNAMICS, GRID, FOREST, CONSERVATION, MAPPING, URBAN`

It reads as a list of applications in the space of urban development, power systems, energy grids, conservation, and dynamic systems. After this cursory analysis, I realized I actually needed to read the 100page white paper initializing the field.

I am putting the data for paper information [here](https://github.com/natolambert/mlcc). You can register for the 2020 Virtual NeurIPs conference for [\$100 (\$25 student)](https://neurips.cc/Conferences/2020/Pricing2) and attend the next iteration on the workshop for [Tackling Climate Change with Machine Learning.](https://www.climatechange.ai/events/neurips2020.html)

## Tackling Climate Change with Machine Learning --- Seminal Paper

This [paper from 22 authors at 17 institutions](https://arxiv.org/pdf/1906.05433) preludes the workshops I mentioned and provides detailed explanations on where people can start. If you get nothing else out of this blogo-post, get this: *machine learning for climate change is a **movement encouraging application-based** machine learning research that'll benefit the planet's long-term ecosystem* (not to say all the changes will take a long time). 

I'll leave the paper to summarize the potential application areas, and the reader to open to document if they are interested in learning more:

> *ML can enable automatic monitoring through remote sensing (e.g. by pinpointing deforestation, gathering data on buildings, and assessing damage after disasters). It can accelerate the process of scientific discovery (e.g. by suggesting new materials for batteries, construction, and carbon capture). ML can optimize systems to improve efficiency (e.g. by consolidating freight, designing carbon markets, and reducing food waste). And it can accelerate computationally expensive physical simulations through hybrid modeling (e.g. climate models and energy scheduling models).*

Essentially, all the application spaces of remote sensing, scientific discovery, energy-intensive systems, and more have many data that is not being touched, and machine learning has proven extremely useful at finding patterns in any big dataset. I separate this point from the list to make it clear --- computer scientists alone cannot solve these problems:

> *meaningful action on climate problems requires dialogue with fields within and outside computer science and can lead to interdisciplinary methodological innovations, such as improved physics-constrained ML techniques.*

The machine learning tools developed in the last decade have had impressive results in distilling patterns from data in so many fields. While there are still many reasons to be skeptical of techniques, there are good reasons that some new tools will work in some of these areas. For example, reinforcement learning, which is generally accepted to be unstable, hard to transfer to the real world, and full of un-modeled behavior is simultaneously very useful in power grid optimization ([example 1](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8834806&casa_token=BWXnOgUelpwAAAAA:rnczsRQ-eOFZ5HcxFlOc7eGuP3us3AbWzIcGJNJQQ6SKk0plgrwqHnBADS5jlCfwteBgw5ui-07W), [example 2](https://livrepository.liverpool.ac.uk/3034527/1/RevisedManuscript_ReinforcementLearning.pdf)). Why does reinforcement learning work here: the system is grounded in very well-known physics and constrained variables --- so when the RL agent does something weird, it can easily be flagged as not physically possible, and so on (*I am starting a reading group with some graduate students going into the differences that make safe or unsafe real world RL applications, so if you are an expert and want to talk, or are interested, let me know*). 

There is a caveat though, which is crucial considering how to deploy this technology: many countries don't have the data infrastructure that underpins so many industries in the U.S. The paper gives the example of different data-logging at energy plants from the U.S. to India --- this turns into a second machine learning problem, namely ***transfer learning*** after figuring out how to optimize the American grid.

They provide a call to action, which is a good summary of how I now feel about it.

> ***Learn**. Identify how your skills may be useful -- we hope this paper is a starting point.*
>
> **Collaborate**. Find collaborators, who may be researchers, entrepreneurs, established companies, or policy makers. Every domain discussed here has experts who understand its opportunities and pitfalls, even if they do not necessarily understand ML.
>
> **Listen**. Listen to what your collaborators and other stakeholders say is needed. Groundbreaking technologies have an impact, but so do well-constructed solutions to mundane problems.
>
> **Deploy**. Ensure that your work is deployed where its impact can be realized.

If you are curious where your expertise may overlap, look at this grid. I think we have an obligation to solve the mundane problems, because they tend to be low hanging fruit. Machine learning practitioners can look at the top and see where their skills are useful, then reference the original paper. Everyone else can look at the left, and then it will pinpoint what ML tools are most useful to learn and leverage in your field. 

[](https://substackcdn.com/image/fetch/$s_!bepa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d7b518-6823-41df-b725-ccb09abe3c08_1232x1722.png){.image-link .image2 .is-viewable-img component-name="Image2ToDOM" target="_blank"}

::::::: image2-inset
![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/b2d7b518-6823-41df-b725-ccb09abe3c08_1232x1722.png){.sizing-normal attrs="{\"src\":\"https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/b2d7b518-6823-41df-b725-ccb09abe3c08_1232x1722.png\",\"srcNoWatermark\":null,\"fullscreen\":null,\"imageSize\":null,\"height\":1722,\"width\":1232,\"resizeWidth\":null,\"bytes\":284786,\"alt\":null,\"title\":null,\"type\":\"image/png\",\"href\":null,\"belowTheFold\":true,\"topImage\":false,\"internalRedirect\":null,\"isProcessing\":false,\"align\":null,\"offset\":false}" height="1722" loading="lazy" sizes="100vw" srcset="https://substackcdn.com/image/fetch/$s_!bepa!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d7b518-6823-41df-b725-ccb09abe3c08_1232x1722.png 424w, https://substackcdn.com/image/fetch/$s_!bepa!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d7b518-6823-41df-b725-ccb09abe3c08_1232x1722.png 848w, https://substackcdn.com/image/fetch/$s_!bepa!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d7b518-6823-41df-b725-ccb09abe3c08_1232x1722.png 1272w, https://substackcdn.com/image/fetch/$s_!bepa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2d7b518-6823-41df-b725-ccb09abe3c08_1232x1722.png 1456w" width="1232"}

:::::: image-link-expand
::::: {.pencraft .pc-display-flex .pc-gap-8 .pc-reset}
::: {.pencraft .pc-reset .icon-container .restack-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1yZWZyZXNoLWN3IiBmaWxsPSJub25lIiBoZWlnaHQ9IjIwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjIwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zIDEyYTkgOSAwIDAgMSA5LTkgOS43NSA5Ljc1IDAgMCAxIDYuNzQgMi43NEwyMSA4IiAvPjxwYXRoIGQ9Ik0yMSAzdjVoLTUiIC8+PHBhdGggZD0iTTIxIDEyYTkgOSAwIDAgMS05IDkgOS43NSA5Ljc1IDAgMCAxLTYuNzQtMi43NEwzIDE2IiAvPjxwYXRoIGQ9Ik04IDE2SDN2NSIgLz48L3N2Zz4=){.lucide .lucide-refresh-cw}
:::

::: {.pencraft .pc-reset .icon-container .view-image}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1tYXhpbWl6ZTIiIGZpbGw9Im5vbmUiIGhlaWdodD0iMjAiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgdmlld2JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBvbHlsaW5lIHBvaW50cz0iMTUgMyAyMSAzIDIxIDkiPjwvcG9seWxpbmU+PHBvbHlsaW5lIHBvaW50cz0iOSAyMSAzIDIxIDMgMTUiPjwvcG9seWxpbmU+PGxpbmUgeDE9IjIxIiB4Mj0iMTQiIHkxPSIzIiB5Mj0iMTAiPjwvbGluZT48bGluZSB4MT0iMyIgeDI9IjEwIiB5MT0iMjEiIHkyPSIxNCI+PC9saW5lPjwvc3ZnPg==){.lucide .lucide-maximize2}
:::
:::::
::::::
:::::::

## **Systematic Changes to Encourage Participation**

How can we encourage researchers to team up with practitioners to solve the *mundane* problems mentioned in the paper. I know my advisor would be totally onboard for me doing this, but the coverage of advisors and managers is not uniform. I have talked about the academic system being a tad broken in terms of incentives, but I want to add another variable to the equation: how to encourage societally beneficial work that is pretty much unnoticed by many academics (fewer citations, bleh). 

Are people at Google Brain and Facebook AI incentivized to work on this? Should I spend 6 months working in this space as an independant researcher to stake some territory? I just want to open the discussion so people think about what actually is limiting spending time in the area. 

## Creating Technology as an Alternate to Studying Climate Change

Another thought I always throw into the discussion on climate change is what technology can we make that'll either a) change the public perception of "green" devices or b) will benefit the environment without the consumer caring (it's just better a la Tesla). My impression from the paper above is that the problems of mitigating harm, optimizing current infrastructure, and measuring impacts of current systems are way lower barrier to enter. I still hold out that making mindset shifting products is long term more beneficial. Here are some [statistics from Tesla](https://www.tesla.com/carbonimpact) and their [report](https://www.tesla.com/ns_videos/2019-tesla-impact-report.pdf) from last year.

Where on the spectrum of *out-innovate climate* change versus mitigate climate change through *public perception campaigns* and conservation do you fall?

<div>

------------------------------------------------------------------------

</div>

See you at the next iteration on the workshop for [Tackling Climate Change with Machine Learning,](https://www.climatechange.ai/events/neurips2020.html) either December 11th or 12th 2020. 

<div>

------------------------------------------------------------------------

</div>

Want to support this Democratizing Automation experience and more high-signal content on AI, robotics, and automation?

-   Click the share button and send it to one of your buds.

-   Tap the cute heart button at the bottom --- making an account lets you comment too!

-   Should I start a podcast? I think it's a matter of when, if not if.

-   Talk to me here (Substack), here [\@natolambert](https://twitter.com/natolambert), or [here](https://people.eecs.berkeley.edu/~nol/).
