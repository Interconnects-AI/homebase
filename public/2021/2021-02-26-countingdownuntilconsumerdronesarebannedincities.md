---
title: "Counting down until consumer drones are banned in cities"
subtitle: "I don’t even like the idea of flying delivery drones, but that will be all we have."
date: 2021-02-26
type: newsletter
audience: everyone
visibility: public
post_id: 32943417.drone-countdown
email_sent_at: 2021-02-26T14:17:30.629Z
---
I don't love that I am doing it, but my current take on anything related to "*are drones safe in cities, what will people be using them for, consumer drones, [Slaughterbots](https://www.youtube.com/watch?v=9CO6M2HsoIA), etc.*" is the trite: **they'll probably be banned**. The public is starting to realize the risk of consumer drones. That being said, most people probably forgot the [Gatwick Drone Incident](https://en.wikipedia.org/wiki/Gatwick_Airport_drone_incident), where one drone shut down thousands of flights across a couple of days in London (about 140,000 people affected). I would also guess if you ask people about hacked drones, they understand they are scary but unexpected. This difficulty with regulating drones and dealing with vast numbers of them lies parallel to the fact that no one was charged in the Gatwick incident (2 arrests, released without charge)! It is a very messy space, and consumers have a weird infatuation with their loud flying friends.

It is super hard to verify who flew a drone. I wrote [previously about the flood of unidentified drones beginning to impact military operations and procedures](https://robotic.substack.com/p/drones-swarms-and-storms-of-drones), but closer to home will be whether or not you, my readers, will be able to buy and use these things easily and cheaply.

The Federal Aviation Administration (FAA) has started to step in and help, for better or worse, from [Reuters](https://www.reuters.com/article/us-usa-drones-faa-idUSKBN2921R8):

> The FAA said its long-awaited rules for the drones, also known as unmanned aerial vehicles, will address security concerns by requiring remote identification technology in most cases to enable their identification from the ground.
>
> Previously, small drone operations over people were limited to operations over people who were directly participating in the operation, located under a covered structure, or inside a stationary vehicle - unless operators had obtained a waiver from the FAA.
>
> The rules will take effect 60 days after publication in the federal register in January. Drone manufacturers will have 18 months to begin producing drones with Remote ID, and operators will have an additional year to provide Remote ID.

This means that every drone needs to be identifiable, and in 30 months we will see how many people offer up ID. If someone bought a drone online to film my action sports in the past or in the next two years, I **doubt they know this regulation is coming**. What do they do with all the drones bought before this? What punishments do they have? Businesses will definitely be able to comply with this, much akin to have modern aviation is very buttoned up, but consumers won't love registering every flight.

The United States has over 1.7 million drone registrations and 203,000 FAA-certificated remote pilots. Most of these registrations are through industrial applications, and consumer drones are a vast unlogged space. For example, the biggest supplier, [DJI sold millions of drones in 2016](https://www.vox.com/2017/4/14/14690576/drone-market-share-growth-charts-dji-forecast) and the number has been growing since (pending recent confusing ["blacklist" of DJI](https://www.theverge.com/2020/12/23/22193660/us-government-dji-drone-entity-list-export-ban-effects)). Needless to say, most drones are not registered and most early rules regarding them are not followed.

Consider, for example, the rules governing drone flights above UC Berkeley. The [drone guidelines are UC Berkeley](https://uav.berkeley.edu/campus.html) state:

> Flying a drone over campus requires that pilots abide by [FAA guidelines](https://www.faa.gov/uas/faqs/) and UC Berkeley drone policy. For more information about drone policy within the UC system, refer to the UC Office of the President\'s [UAS Safety site](https://www.ucop.edu/enterprise-risk-management/resources/centers-of-excellence/unmanned-aircraft-systems-safety.html). In short, it is against Berkeley policy to fly a drone weighing more than 250 grams over campus property without written permission from UCOP UAS safety, UC Berkeley risk management, and UCPD (this process requires the pilot to hold an [FAA Part 107 certificate](https://www.faa.gov/news/fact_sheets/news_story.cfm?newsId=20516)). To view UC Berkeley\'s complete drone policy click [here](https://campuspol.berkeley.edu/policies/drone(campus).pdf).

I have regularly seen drones flying around campus. How could this be prevented? Anti-drone is a hard problem, and there are serious privacy and safety concerns with drones being engaged in public spaces. Remote, agile, malicious actors are terrifying. *A small percentage of a big number of drones is still of high consequence.*

To clarify some numbers on drone sizes: DJI drones weigh generally from 700-2000g, well above that limit (for example, the popular [Mavic Pro](https://www.dji.com/mavic/info) is 734 grams). 250 grams actually seems fairly astute for physical safety, but maybe is on the high-end of the safe range. Cyber safety is a different game, radios and cameras have been consistently reducing size. A robot plenty of researchers and I have used called [The Crazyflie](https://www.bitcraze.io/products/old-products/crazyflie-2-0/) masses 27g and cannot do much physical harm (low payload capacity and low force, so the point where if one is doing something weird in research *I grab it *to turn it off) or fly too far with its onboard sensors, but it can still easily track someone who doesn't want to be tracked.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/31c874ed-c2a4-43f7-a773-891a1fb5f73b_5763x3799.jpeg)

## Simple drone risks

Drones are incredibly powerful for short flights. They can have high payloads and reach high velocities, which makes them uniquely dangerous (compared to a car that also has to be restricted to roads of some type). It is worthwhile to re-state the two flavors of risk that come from autonomous or remotely operated acrobatic drones:

-   **hard to trace**: remotely operating a device shields criminals from a lot of risk. 

-   **cybersecurity**: there is a history of networked vehicles being hacked and controlled externally. 

The latter is flashier, but the former is the crucial reason consumer drones will become unpractical. If anyone can take off a drone, especially with an improvised explosive device, it is a low-cost missile. Drones can fly autonomously at [extremely high speeds](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.490.7958&rep=rep1&type=pdf). Without any barriers to people taking off drones in areas, they will always be a national security risk in my mind. If you aren't sure how acrobatic these drones are while flying autonomously, check out the [products from Skydio](https://skydio.com/skydio-autonomy) that are programmed to follow a person. Normally said person is you, but consider if someone changes who that person is without the target's permission --- high speed, low-cost tracking of anyone.

### The simple case against flying delivery drones

I had to include this brief aside. Before you get super excited about Amazon delivering your package via drone instead of human, there is something you should know. Flying drones are so loud. It is quite unpleasant to do research in a room with small drones. Large delivery drones would be even worse and persistent in dense areas (given how easy it is to click buy on Amazon). With what I have seen from the ride-share-scooter populations, I also expect these robots to be bullied and damaged. 

What is the hurry with last-mile delivery, can the slow crawling drive bots not work? The marginal gain in time from a direct flight route should not be that high on your values. Favorite thing in researching this: The small delivery bots in Berkeley, KiwiBots, once [caught fire](https://www.theverge.com/2018/12/17/18144304/kiwibot-fire-berkeley-california-thermal-runaway-faulty-battery) randomly, whoops!

### Consumerization of Drones with Increasing Autonomy is Risky Business

I think I have painted most of the picture already as to why the trends of more drones with more autonomy are risky. Historically, people expect their vehicles to be robust against any digital attack, but famously [Jeeps have a rich history of being hacked](https://www.wired.com/2016/08/jeep-hackers-return-high-speed-steering-acceleration-hacks/) remotely (even when the vehicle is on). While unlikely, this theme translating over to the area of consumer drones is potentially higher risk given the substantially lower levels of safety regulation in place for drones.

For more in this area, see academic research on cybersecurity and privacy of robotic systems: [link1](https://pdfs.semanticscholar.org/adad/5d215649d0612786ebe473dbb7cab424bcd3.pdf), [link2](http://cogsima2017.ieee-cogsima.org/files/2016/01/1570327905_Clark.pdf). I focus mostly on physical harm, but privacy is severely at risk if unidentifiable drones rule the skies.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/cf32df19-e3dd-4782-885c-c7dbdce607c1_2476x1707.jpeg)

### What the end-game looks like

If you know anything about US regulatory organizations, the rules are made after events that would have benefited from them. You can read more about the [history of the FAA](https://www.faa.gov/about/history/brief_history/) here, but the simple fact that they gave 30 months for companies and users to start having methods of identification shows that things could get a lot worse before they get better. The transition phase can take a lot of forms, from drone assassinations (even in the US, I am scared of this), do drone bloopers like the Gatwick incident, and more things I haven't even thought of. 

To me and people in my drone research circles, it is strange to us why more hasn't been done. Anti-drone is a hard technical problem due to their agility, but it seems like something national security should take more seriously.

The end-game looks like drones being usable in pre-designated areas (think dog parks), and companies generating and registering all of their drone flights with FAA APIs to manage high-volume logistics routes. Consumers likely can register in the same way, such as people who specialize in drone photography or for filming specific events, but it will be the minority.

![](https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/7fdce3ac-7631-4ac3-9589-1688ae5b9b60_4032x2320.jpeg)

<div>

------------------------------------------------------------------------

</div>

## Snacks

### Other fun drone links

-   [Mixing moths and drones](https://spectrum.ieee.org/automaton/robotics/drones/smellicopter-drone-live-moth-antenna)! High-tech! 

-   [The Mars landing features a drone in Mars's low-pressure atmosphere](https://mars.nasa.gov/technology/helicopter/).

-   [An interesting, visual analysis of the drone addressable financial market I found researching this article](https://www.goldmansachs.com/insights/technology-driving-innovation/drones/).

-   [Europe had its largest drone operation ever searching a landslide](https://www.uasnorway.no/europes-largest-drone-operation-after-deadly-landslide-in-norway-420-missions-and-200-hours-of-airtime/); I am definitely a big proponent of search and rescue drones.

### [Reads](https://www.natolambert.com/bookshelf)

-   I finished [Artemis](https://en.wikipedia.org/wiki/Artemis_(novel)) and it is quite a rapid ride. It is one of those sci-fi books that you just want to stay up and finish. It'll be turned into a movie that is not as good, so read it before it does!

-   At the recommendation of a reader, I started listening to [The Rise and Fall of the Third Reich](). I'll have more thoughts later, but it is really a journey making me realize how obvious it is that we should work against antisemitism, even if some people don't see it. History repeats itself 😞.

I made a [new website](https://www.natolambert.com)--- learn about machine learning, robotics, and me.

If you want to support this: like, comment, or [reach out](https://twitter.com/natolambert)!
