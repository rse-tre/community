# RSE TRE Community Quarterly Meeting

```{toctree}
:maxdepth: 1
:hidden: true

project-discussion-package-licensing.md
project-discussion-allowlist-software.md
project-discussion-cloud-tre-charging-researchers.md
project-discussion-user-experience-azure-tre.md
breakout-community-management.md
breakout-federation.md
breakout-tre-standardisation.md
breakout-information-governance.md
```


#RSE TRE Community - Report: Quarterly Meeting December 2022

Date: Monday 5th December 2022

## Useful links

* **Slack channel**: https://ukrse.slack.com/archives/C045ETUPPD0
* **RSECON Report (foundational event)**: https://rse-tre-community.readthedocs.io/en/latest/events/wg_workshops/rsecon22/index.html
* **Community GitHub**: https://github.com/rse-tre/community

## Schedule

| Time | Agenda item | Presenters | Notes |
|------|-------------|------------|-------|
|13:30-13:45 | Introduction | Hari Sood (Turing) & Simon Li (Dundee) | Introduction to day & community |
| 13:45-14:15 | DARE UK talk | Fergus McDonald (DARE UK) | Talk + discussion on funding & sustainability |
| 14:15-14:35| Project discussions 1 | Breakout | Breakout room 1: Managing software/package install and licences on secure environments without internet access - Lucy Cheesman & Jake Cooper (Sheffield) |
| | | | Breakout room 2: How best to whitelist software packages for secure environments - James Robinson (Turing) |
| 14:35-14:40 | Project discussions 1 feedback | Hari Sood (Turing) & Simon Li (Dundee) | Community shareout from first 'Project discussions' session |
| 14:40-15:00 | Project discussions 2 | Breakout | Breakout room 1: Cloud TREs: How do we fairly charge researchers? - Simon Li (HIC) |
| | | | Breakout room 2: User experience in the Azure OSS TRE - Alessandro Riccombeni (Microsoft) |
| 15:00-15:05 | Project discussions 2 feedback | Hari Sood (Turing) & Simon Li (Dundee) | Community shareout from first 'Project discussions' session |
| 15:05-15:15 | Break |
| 15:15-15:30 | Breakout discussion poll | Hari Sood (Turing), Simon Li (Dundee) & Fergus McDonald (DARE UK) | Mentimeter to decide breakout room discussions |
| 15:30-15:45 | Working Group Updates | Hari Sood (Turing), Simon Li (Dundee), Lucy Cheesman (Sheffield), Michelle Amugi (DARE UK) | Updates from working groups, and next steps |
| 15:45-16:05 | Breakout discussions: [**Community management, working groups and events**]() & [**Federation, discoverability & interoperability**:]()| Breakout | 2x breakout rooms for discussions |
| 16:05-16:30 | Breakout discussions 2:[**TRE standardisation & accreditation**:]() & [**Information Governance best practice**:]() | Breakout | 2x breakout rooms for discussions |
| 16:30-16:50 | Wrap up | Hari Sood (Turing) & Simon Li (Dundee) | Community next steps & signing up to working groups
| 16:50-17:00 | Working group planning | Breakout | Breakout rooms for working groups to plan next steps |

## Introduction to day & community

Hari Sood from Turing and Simon Li from Dundee University facilitated the meeting, starting by presenting the agenda and doing a quick recap on the community and reason for the meeting.

Main points are: [name=Hari] *do you have your notes to add key points here?*
- The RSE TRE Community aims to foster collaboration and knowledge sharing on Trusted Research Environment in order to arrive to common solutions and architechtures
- The community was formed after a satellite event during RSECON2022
- There will be quarterly meetings with at least one hybrid event each year
- 3 initial working groups were formed: Information Gathering, Funding & Sustainability and Community Management
    - Everyone is welcomed and encouraged to join one

## DARE UK talk
**Topic:** Funding and Sustainability
**Speaker:** Fergus McDonald, DARE UK + HDR UK

In this talk Fergus McDonald introduced DARE UK's efforts and challenges on how to fund TRE research and development for them to be self-sustainable. Raising questions to this community.

Key points:
- DARE UK programme: Data Analytics & Research Environment
- Funding has significantly increased for Digital Research Infrastructure (+300% increase from £17M in 21/22 to £70M in 24/25)
- In particular DARE, in its Phase 1: Design & Dialogue, has dedicated £3.0M (1a) up to Sept 22 and will invest £4.5M between Sept 22 and Oct 23 (Phase 1b)
- Phase 1b objectives
    - Architecture for federated network of TREs
    - Deliver federated network of TREs
    - Funding model for federated network of TREs

Questions raised by Fergus revolved around the third objective for phase 1b, **what funding model is required to deliver a sustainable federated network of TREs?**
- Where is the balance between innovation and sustainability?
- **How do we actually engage with the community and move forward?**
- If longer term funding is provided, what commitments to the community should be required in return?

The conversation explored these questions, underlying the importance to fund development of open code and shared infrastructures & architechtures. Several participants agreed on how funds can and should enable teams who are up for collaborating to do so (as their institutions may prioritize fundings more aligned with internal objectives), and how this encompasses more than technical development to include Information Governance principles and principles, or community building efforts.

[**full talk shared notes**]()

## Project discussion sessions

For these two breakout rooms were created for each, with participants joining whichever better aligned their interest. We then all reconvened to share summaries of the discussions
### Session 1

#### **Managing software/package install and licences on secure environments without internet access**

**Discussion prompts**
* How do we get users actually working on their projects? Code/libraries/software etc
* How do we manage licencing?

**Discussion**
Sheffield University shared their experiences where they have 2 TRE environments, one of which has no internet connection.
HIC (@hari what does it stand for?) has the same issues and approach it with open source solutions on [GitHub](https://github.com/hic-infra/shared-services-ansible-roles/). This means the environment actually has *some* internet connection, implementing automatic scan for viruses and controlling user access with squid proxy.

Limitations on how to work with data are obvious but reserchers *put up with it* because it is actually the only way to access this data.

Some other approaches and solutions were shared but making evident that so far they are small scale solutions that fit each projects

[**full notes**]()

#### **How best to whitelist software packages for secure environments**

James Robinson (Turing)

James presents the issue, which we have faced at the Turing. The need for knowing beforehand all the tools needed and making sure they work within the TREs. So we came up with a list of packages that are reasonable to have, but then it gets even more complicated as each package has versions, and each version different dependencies with other packages and different requirements. Maintaing the list and making them available becomes cumbersome. So open to all, how do we tackle this?

**Discussion:** The conversation started by taking a step back and asking why we need to whitelist in the first place and what makes packages unsafe. This is because some packages introduce ingress and egress possibilities that the rules for your TRE forbid, and having a whitelist prior to use is useful because at the point of usage it may be too late to analyse packages. This will be increasingly important as users require or demand new functionalities, data processing tools or installing github repos (not allowed in some current TREs but a growing demand observed)

It was agreed that the solutions vary and depend on both risk apetite and trustiness of packages (or rather of the communities developing and maintaning them). 

CHAT Qs/reflections:
- The dependency management issue is very much similar to that faced by HPC facilities. This adds an additional security challenge but the problem is familiar to HPC centre manager teams. {module files, spack, easy build etc}
- How hard/ time consuming is ^ the way HPC do things, would it be practical to copy their approach each time a cloud deployable TRE is set up?
- Whitelisting suggests making sure the software is compliant and safe before using it. Other processes can be used to verify nothing wrong happened in the environment AFTER the software was used. Cost of prevention vs. cost of remediation.
- . Is there a difference between interpreted vs compiled code in terms of TRE safety/risk?

**Actions/next steps**

* Possiblity for a shared list of 'trusted' software packages as part of this community

[**Full notes**]()

### Session 2

#### **Cloud TREs: How do we fairly charge researchers?**

Simon Li (HIC)

[name=Hari] Any summary???

Participants reflected on the balance between what can be offered for free and what should entail additional costs. There was a certain agreement on a level of offering not requiring to be charged but not so much yet as to where that stands.

Part of the difficulty in projects being charged lies in researchers not fully understanding the technical cost (both in hardware and developer time). An effective way of mitigating this is demoing researchers to show impacts on performance rather than listing computing specifications. Another part has been when charging for storage that if you do users have used their own storage under their desk but providing it free has meant projects not applying for grants to cover TREs costs.

Another thing to take into account is the different service model of AWS and Azure, the latter closing GPUs down when credits are consumed while AWS allows for over-expenditure.

While there are still no clear answers it looks like certain standarization across proejcts is needed, as well as a way to ensure at least some central funding for TREs at institutional and project levels.



[**Full notes**]()

#### **User experience in the Azure OSS TRE** 

Alessandro Riccombeni (Microsoft)

From Microsoft leads. tells a bout the UX in their TREs and the functionalities that an user need. A key Challenge as user of a TRE? What would solving the challenge unlock?
 ![](https://i.imgur.com/Gf8xjBz.png)
 
 This conversation acknowledged the confusing user experience that TREs can offer, even to participants themselves despite being "technical people". One of the biggest questions from users being "Why cant I just do that?" as they are used to work outside of TREs and struggle to grasp the importancy of TREs, it is not evident/known enough that without them they could do nothing.
 
 Users just want the experience they are used to in their local hardware. In clinical environments TREs have tried to replicate that experience as much as possible, but that changes from one user base to the next. The cloud seems to have offered more flexibility to provide users with what they want rather than trying users to change.
 
 Participants agreed in striving to achieve usable and not only useful systems.

[**Full notes**]()

## Working Group updates

Each of the 3 working groups updated us on their progress.

### Information gathering
- Survey out now. Combined with planned DARE UK survey. Please share the [survey link](https://corexmsc2tjhf4qmmsys.qualtrics.com/jfe/form/SV_3sWoWuzuQWAFaSO) widely.
- Survey is a first step in information gathering.
- Where to store / share the survey data? Could we use the survey data to seed a living view of the landscape?
- Could put on GitHub on the WG repo / webpage / doc site.
- To turn the snapshot into a living data set we should also think about how people can contribute to  / update the data between formal surveys. If on GitHub could let anyone open a PR.

### Funding & Sustainability
- Covered in earlier talk
- Please join up with the working group, we're trying to figure out where to go and how to get there - should be a journey.

### Community management
- [GitHub repository](https://github.com/rse-tre/community) and associated [ReadTheDocs site](https://rse-tre-community.readthedocs.io/) up and running. [Notes from first meeting](https://rse-tre-community.readthedocs.io/en/latest/events/wg_workshops/rsecon22/index.html) posted on ReadTheDocs site.
- [Slack channel](https://ukrse.slack.com/archives/C045ETUPPD0) up and running. Mailing lis to come.
- [Newcastle Commitment](https://docs.google.com/document/d/1F8TOilZlu0k8dojFFqbD-GuIyJIjCMCMhscJTEz7yKQ/edit): Principles for the community
- Q: Should we require / allow people to sign the commitment? A: Seems to be a consensus to allow people to sign the commitment but not require it.


## Breakout discussion

### Session 1

#### **Community management, working groups and events** 

This discussion focused on how to organise the community and the kind of involvement it should ask
** Quesitons addressed**

- Do we want industry involvement? If so, how to encourage/enable that?
- How can WGs align with organisations like DARE UK?
- How to ensure that WGs are output oriented (i.e. deliver something within a timeframe)? 
- How to prioritise WGs and their outputs? In a sense, how to groom the community backlog?
- How should future meetings be run?

There was a general agreement on keeping 4 yearly meetings like this one due to feasability, yet WGs should meet more often to actually do the agreed work. These WGs should also be free to self-organise.

Specific events, focus groups or community engagement between those 4 yearly meetings should still be encouraged if WGs see the necessity for them.

There is a shared preocupation with this community becoming or being perceived as too tech focused and driven by specific institutions whose members's roles include engaging with it (payed to do so), and at the same time balance the necessity for such people to ensure the delivery of work.

Working groups should ensure deliveries and a new one on Open Source TRE could be a good idea that both better aligns with other people daily activities and deliveres valuable work. The Information Governance (IG) working group is perceived as crucial moving forward and it is important that it sees more people getting involved, specially non-technical ones.



[**Full notes**]()

#### **Federation, discoverability & interoperability**: 

** Questions addressed**
* Qu1: What kind of things do we want to see e.g., share data between TREs, tighter integration between TREs...?
* Qu2: Why is interoperability important?

**Discussion points**
* Standardisation across TREs in terms of how to do it, is important. HPCs have similar problems to solve. Research questions to be addressed in a scalable way. Different issues, infrastructure, privacy, processes, can they all be addressed and standardised to keep from having to reinvent the wheel. This will make it easier to compare across TREs. Avoid continuing silo approach. 
* What is the minimal amount of standardisation necessary to be able to facilitate discoverability? 
* We need to understand the data in the TRE first before being able to address some of these questions (e.g., privacy). 
* Would like to see central management such as accreditation for TRE users (e.g., Scottish Safe Haven). Consistent userface to TREs. Governance is key to making some of this easier. 
* HDRUK alignment with data connectivity - expanding from COVID to wider subjects, avoid duplicating effort with what they are doing. 
* Interoperability (e.g., Docker as a standard) makes it easier for new institutions to engage with this and the exent to which collaboration can be achieved and deployed. 
* There may be challenges in getting researchers to engage in some of the tech required (like Git or Docker) so having consistency will help to reduce the learning costs for researchers to engage with TREs
* Need to answer big science questions and more pragmatically for data not to be locked behind artificial barriers. Makes sense to align and do things similarly across a region where data is similar - the tranfer of code will make it easier to get the same study working in a new dataset. 
* There is a concern that we are just creating more silos - how do we manage to not do that?


**Actions/next steps**

* Understand what is being used already across the research community? What tech? What data? Can we gain insight from the industry? 
* Make a list of the standards - understand the lay of this land and understand operability between them to see how these can be useful (e.g., operating systems and more granular systems like Docker)

[**Full notes**]()

### Session 2

#### **TRE standardisation & accreditation**: 

**Questions addressed**
* Is there a feasible minimum standard that can be achieved agnostic to the research/data domain?
* Who should be responsible for developing, maintaining, & accrediting such a standard? Who needs to provide input to this standard?
* Who's responsible for maintaining standard over time, who checks you're still compliant?
* What can we do so that a TRE operator using a standard TRE codebase or architecture can shortcut the accreditation process instead of having the full tech stack being audited from scratch

Participants shared experiences on current standarisation efforts in health and mentioned NERC is looking to setup a TRE for environmental data, at the sime time participants from the Alan Turing Institute saw lots of commonalities across TRE in different sector having worked mostly with non-health data. There are core requirments such as standarised logins or ingres/egress systems (and how these need to be written down and shared).

Two main aspects of standarisation efforts were highlighted, the need to communicate with potential researchers about what they mean and entail (e.g. data tiers and what fuctionalities toe xpect for each) and how to maintain said standards. As well as what type of body or isnstitution should watch for compliance, one modelled after the IEEE, one that arises from DARE working group or sector specific like the NHS for health data.


[**Full notes**]()
#### **Information Governance best practice**: 

**Questions addressed**
- How best to classify data?
- Do we see IG as a primary focus for this community? 
- Are there other communities of IG practitioners we need to engage with? 

**Communities we should engage with**

* [Safe Data Access Professionals network](https://securedatagroup.org/)
* PPIE/members of the public
* NHS Information Governance folk (who?) - ICS/ICBs
* Regulators?
    * Information Commissioner's Office. They have had an [anonymisation guide] for some years and are consulting on an update incorporating GDPR require
    * Financial Conduct Authority. They have a [regulatory sandbox](https://www.fca.org.uk/firms/innovation/regulatory-sandbox) to support experimentation in this space (have done hackathons on synthetic data)

The relationship (or lack of) with IT over the years is a shared comment and one issue to overcome. It would appear that the IG-IT relationship is an important thing to focus on.

The processes that we are going through, the documentation, which is mostly repos would be easy to transform into business processes for organisations. How much of this has been produced as part of our ways of work and how much produced explicitly to be read for people outside developing it?

Dundee make their [standard operating procedures](https://www.dundee.ac.uk/corporate-information/standard-operating-procedures-hic) available online

The Manchester Connected Health Cities TRE made their [Information Security Management System documents](https://github.com/connectedhealthcities/chc-gm-isms) available online.

[**Full notes**]()

## Working group planning

It was agreed to create a new Working Group, Open Source TREs.

- Community & Events
    - https://hackmd.io/xLeTgbEETMO11CgbSRIW3Q
- Open Source TREs
- Funding & Sustainability
    - Initial working group session in the new year, specific call for participation to go out on Slack/emmail channels. Email Fergus McDonald (Fergus.McDonald@dareuk.org.uk) if you want to join.
- Information Governance
    - Will look to have an initial WG session in the new year. Will put call for participation in Slack / email channels. Email Martin O'Reilly (moreilly@turing.ac.uk) if you want to join.
