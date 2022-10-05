# TRE Satellite event report

## Introduction

Trustworthy Research Environments (TREs), also known as Secure Research Environments (SREs) or Data Safe Havens (DSHs), are secure computing environments that allow approved researchers to conduct research with sensitive data.

TREs build upon the Five Safes framework for allowing secure research access to sensitive data.
TREs that are secure, open and easy to use can have myriad benefits.
Not only can they facilitate ground-breaking research with sensitive data, they can also improve collaboration and reproducible science between research teams, and increase public confidence in scientific research.

Across the UK and abroad, there is a lot of exciting work happening within the TRE space.
The Goldacre review, commissioned by the UK’s Secretary of State for Health and Care, addressed the need for a coordinated approach to the provision of secure data platforms for NHS data - echoed in a report released by DARE UK in late August.
DARE UK have funded, and will continue to fund, projects working in this space to develop this approach.

Researchers, Software Engineers (and Research Software Engineers) across the world have been building institutional solutions for their own research needs for years.
Whilst some are working independently, others are working in collaboration with commercial partners like Microsoft and AWS, who themselves provide their own implementations and infrastructure.
All this work is progressing at a fast-pace, and adapting to an ever-changing, data-intensive research environment.
As the TRE conversation develops, there are many questions for project teams developing the infrastructure to consider - how many solutions should exist? Who has access to these environments? How can we standardise data security requirements across institutions? Could aspects of the infrastructures be standardised to ease compatibility and collaboration? What industries require access to TREs, and how do their needs differ? And many more.

On 5th September, a satellite event at RSE Con was organised by University of Dundee and the Alan Turing Institute to bring project teams working on this infrastructure together to share knowledge and discuss key issues and problems facing their projects.
The aim of the day was to form the beginnings of a coordinated approach to TRE infrastructure development, and create a community space for continued collaboration.

The day was split into two sessions.
In the morning, individuals and groups gave presentations on their work, their thoughts and key considerations within TRE development.
In the afternoon, topics the group had voted on were discussed in small breakout groups, and possible next steps recorded.

The group came back together at the end of the day to share key points from the discussion groups, and agree on the next steps for the community.

It was agreed that a community space should be set up for collaboration and knowledge sharing, governed by a community ‘commitment’ that was drafted on the day.
It was also agreed that the group should meet quarterly, with at least one hybrid event organised each year.

Below are summaries of the presentations and breakout discussions.

## Morning Presentations

The morning presentations were split into three broad categories of ‘organisational overviews’, ‘TRE implementations’ and ‘using TREs’.

### Organisational overviews

#### ADR Scotland (ADR-S) at EPCC

_Michael Jackson_

ADR-S, a collaboration between the Scottish Government, Public Health Scotland, National Records of Scotland, and EPCC at The University of Edinburgh, is creating a reusable portfolio of de-identified, linkable, administrative data from across Scottish government departments and local authorities, and provides a secure route for accredited researchers to use both this data and de-identified health data from health authorities.

#### Health Research Authority

_Alan Smith_

HRA oversees and approves all health research that happens in the UK.
Their current work in the TRE space is to establish a form of certification for TREs that indicate they satisfy certain HRA approval requirements.

#### Safe Data Access Professionals

_Martin O’Reilly_

SDAP is an informal peer support group of professionals from different organisations running Trusted Research Environments.
The group has organised knowledge sharing and community events, and facilitated discussion on topics like developing a competency framework around running a data safe haven, statistical disclosure control, and training for users.

#### Microsoft UK for Precision Medicine

_Alessandro Riccombeni_

Microsoft started Precision Medicine work for the UK this year.
It is a workstream focused specifically on scientific impact, and facilitated through partnerships and collaborations with hospitals, academic institutions and more.
As part of this work, they have developed an open source Azure TRE codebase, created in collaboration with a number of UK institutions and partners.
It is driven by user needs, and they are very open to feedback on the codebase.

### TRE implementations

#### Secure workflows for HPC

_Harvey Richardson_

HPC/AI EMEA Research Lab is a research group distributed across Europe, who have been working on Proof-of-Concept technology to allow research teams to securely transfer applications and sensitive data to an environment that will allow them to utilise HPC resources.

#### The Outbreak Data Analysis Platform

_Andrew Brooks_

The ODAP project at EPCC grew around the ISARIC (International Severe Acute Respiratory Infection Consortium Clinical Characterisation Protocol) to provide rapid, flexible access to datasets, which was required when COVID hit.
As the need for more compute power became apparent, a ‘pseudo-TRE’ system was built on top of EPCC’s HPC resources.
Work is ongoing to incorporate HPC within a fully secure environment.

#### The Alan Turing Institute’s Data Safe Haven

_James Robinson_

The Turing Institute Data Safe Haven constitutes a soon-to-be open source codebase to allow the reproducible deployment of TREs on the cloud (Azure).
It isn’t a service offered by Turing, rather code that will be available to be used by anyone in the way they require.
It is also accompanied by a data security framework for understanding data sensitivity.
Turing are looking for collaborators to work together on a common public codebase, which could be based on this or another project.

#### Sensitive Research Data Service

_University of Sheffield_

The University of Sheffield are building TRE capability on AWS using a software called RONIN.
They have both cloud and on-premises environments, the choice of which depending on the sensitivity of data, and the need for HPC resources.
There is ongoing work around data and digital infrastructure, end to end support, and community of practice to improve access and ease-of-use for researchers.

#### Design of a local TRE for process of patient records

_Thomas Arildsen_

The research support team CLAAUDIA at Aalborg University developed TRE capabilities to facilitate the transfer of highly sensitive, complete medical records from primary sector to university for research, for which there was a need for a secure platform to store and process data.
It used the ‘research service’ at Statistics Denmark for inspiration. Full patient records are ingested and pseudonymised within the environment, with researchers gaining access to a more open part of the platform at a later stage.

#### The TREEHOOSE Open Source Cloud TRE

_Chris Cole_

The Health Informatics Centre (HIC) at the University of Dundee focuses on delivering world leading health research.
They already have an on-premises TRE they have been running for many years. With support from AWS, they have been working on next-generation cloud-based TRE infrastructure.
Building off their own cloud-based TRE and AWS’s own cloud-based TRE development, it is infrastructure as code, with documentation and guidance on how to deploy yourself.

### Using TREs

#### Developing and Publishing Code for Trusted Research Environments: Best Practices and Ways of Working

_Ed Chalstrey_

In a collaboration with University of Swansea and University of Manchester, and using the SAIL Databank, Ed has written a report around best practices in developing research code for TREs.

The report covers topics like using GitLab, GitHub, notebooks, DOIs, and software licences, and explores questions of where researchers should develop code to be used inside a TRE, and what should be exported from a TRE.

#### Understanding researcher needs in TREs

_Meag Doherty_

The All of Us Research Program’s mission is to accelerate health research and medical breakthroughs, enabling individualised prevention, treatment and care for us all.
They have curated a diverse biomedical dataset of over a million participants across the US, and have developed a workbench to inform robust use of the dataset.
They work with researchers on design solutions to working with the dataset, and want to develop open-source design guidelines for working within TREs and with sensitive data.

## Breakout discussions

All links to raw notes for breakout discussions can be found here

### Community management

#### Prompts

- What tools & methods are we using to communicate?
- What are the areas that we should initially focus on?
- Who is involved?
- What should this community space be used for?
- What are our key principles for collaboration?

#### Discussion

In order to pull together all the work everyone is doing and facilitate collaboration, it is important to have a community space where people can share knowledge and coordinate efforts.
To begin with, it’s important to have a space that people know about, and it can be relatively free-form.
As the group develops, it can become more structured and formalised, depending on the direction it takes.

It was agreed that the group should remain decentralised and not be driven by any single voice/organisation, and that the group is governed by principles of inclusivity and impartiality.
Discussion needs to be had around how best to share responsibility and roles within the community at the initial stage, and whether it would be good to fund a role to be actively responsible for managing the community.

Ideas were discussed around what the group should focus on, while stressing the importance of facilitating collaborations and conversations arising organically and to not take a prescriptive approach to direction. Nevertheless, the community should from the outset consider wider questions around what the overarching shared mission of the community is, who should be involved (just engineering teams or also end-users, general public, or more), and how it should be governed.

A good initial activity would be to get a clear picture of what projects are currently working on TREs in the UK, and their key features.

#### Next steps

- Talk to communities that have grown successfully (e.g. RSECon, Turing Way, HPC-UK)
- Carry out a baseline ‘survey’ of who has done what in the TRE space in the UK, and possibly abroad
- Discuss possibility and method for funding time, or a role, to coordinate the community
- Agree on governing principles, target audience, and mission of community.

### Standardisation of information governance, certification & regulation

#### Prompts

- How do we standardise sticky issues around ethics?
- What definitely can/can’t be standardised?
- Can certifications and governance reviews be done once for each TRE code-base?
- Can information governance reviews be shared across TREs?

#### Discussion

Standardisation is made difficult due to a large variety in data, for instance different types of data, data sensitivity etc. requiring different approaches and governance.
The lack of definition for ‘TRE’ also makes standardisation difficult from the perspective of data providers.

Nevertheless, it is easier to apply some kind of accreditation to a TRE rather than people.
TREs can ‘guarantee’ some level of security through technical controls and processes.
This can be aligned with the expectations/requirements of data providers.
NHSx has proposed a ‘soft’ accreditation for TREs to reduce friction for collaboration. This is worth exploring in more detail.

Additionally, there are already pre-existing standards that can be built off to approach TRE certification & governance, for instance ISO27001, DSPT, Cyber Essentials +. Understanding what already exists and how they are operated would be a useful next step.

#### Next steps

- Identify, survey and take inspiration from organisations that have pre-existing certifications and are seen as having good quality governance in place of what already works and is ‘acceptable’ in the UK. E.g. UK BioBank.
- Identify the ‘hard requirements’ for different organisations/types of data. E.g. Cyber Essentials + for MoD.
- Agree upon a clear definition of what a TRE is (and is not). This is important for data providers.

### Managing software development in a TRE

#### Prompts

- What tools and applications are needed inside a TRE to enable software development?
- How do we make it easier to share code inside and outside a TRE?
- Best practice for developing and publishing code used in a TRE?
- Does potential scalability need consideration as well, eg. for High Performance Clusters?

#### Discussion

In order to advocate for good development practices within TRE environments, it would be useful to promote guidelines for researchers on reproducible, accessible, and tested, code.
In short time frames (e.g. workshops) it can be difficult to both teach development processes and practices and ensure you can deliver reproducible results (even in long sessions that last days/weeks).

Any tools that can make tasks like revision control and automatic backups of working code easier can aid in the task of making outputs reproducible.
Further considerations need to be discussed around producing realistic dummy data for projects that isn’t noisy, dirty or hard to use.
This is especially pertinent for large, unstructured datasets.

#### Next steps

- Encourage researchers, TRE users, developers, and RSEs to join the community and share RSE good practices.
- Identify whether requirements discovery is done differently for TREs than for other research projects.
- Identify the minimum set(s) of software and data skills researchers need to have if doing data analysis within a TRE.
- Secure funding to run a study to identify researcher classes, software/data skills/knowledge required, and TRE options open for them.

### Community commitment

#### Discussion

This session developed the following draft commitment text

#### Next steps

- Publish an initial version of the commitment for community input to develop a final version for organisations to sign up to
- Proactively consult with key organisations we’d like to sign up to the commitment
- Set up a hosting location for the commitment and a mechanism to collect signatures
- Sheffield, Dundee, UCL and Turing will collaborate on deploying the following TREs and evaluating their suitability for these organisations contexts
  TREEHOOSE
  The Sheffield TRE
  The Turing Azure TRE
  The Microsoft Azure TRE

### User experience in TREs

#### Prompts

- What are the barriers to using TREs?
- Who are we designing TREs for?
- Are there design principles we can generalise and open source?

#### Discussion

A key issue is the lack of understanding and familiarity users already have with TREs.
They may not be clear on what TREs do, why they are needed, what they are able to do within them, and how to navigate the environment to use the tools they are used to.
This may be especially important if end users come from more non-technical backgrounds, for instance NHS staff/clinicians.
As well as training for both CLI and GUI tools, building interfaces that match the mental models and expectations of researchers is critical for users to feel comfortable in any TRE.

There are also key differences that make streamlining design across TREs difficult.
These could include the different aims and needs of users, the infrastructure design of different TREs, and even the different security/certification/education requirements for different data security and information governance processes.

Standardising the TRE user experience may make it easier to move between different TREs.
However, having different design set-ups that users can choose between may also lead to greater individual ease-of-use, productivity, and happiness.
A potential route forward is to have a knowable number of workflows that could be standard across TREs whilst also having custom design within a given domain.

#### Next steps

- Explore modular components for building researcher-specified TREs - workspaces, environments, data access, tooling etc.
- Make sure that datasets (data catalogue), TRE options etc. are all properly published, advertised, quickly accessible and well-described.
- Develop a central resource for TREs - (trustedresearch.ac.uk?) - for publicity, to manage a “trusted packages” repository of tools, catalogue all TREs, data catalogues and more

### Open source infrastructure and collaborations

#### Prompts

- How many open-source TREs do we want?
- Do we need separate collaborations for each open-source TRE?
- Can we collaborate across different TRE platforms?
- Is it worth considering scalability for TRE platforms?

#### Discussion

People are currently using a range of TREs, both on-prem and cloud-based.
There are a number of open-source solutions out there (e.g. TREEHOOSE, Turing, Microsoft) which can form the basis for collaboration.
IAC also has on-premises open-stack implementations using Terraform, and container-based implementations built on Kubernetes.
Sharing knowledge on these solutions will be useful to bring to the conversation.

A number of organisations are keen to work together on evaluating current solutions (Turing, UCL, Sheffield, Dundee) and exploring governance standardisation (Turing, Dundee, EPCC).
These are key areas to explore in the near future.
It may also be worth considering infrastructure for scaling computational power, and if connecting with groups like HPC-UK to ease scalability would be beneficial.

#### Next steps

- Establish methods to explore common governance, initially by sending invitation to a kick-off meeting
- Organise a similar discussion & exploration on code - What do we have already, do we want to combine or adopt a single codebase
- Connect with institutions that focus on scalability of computation and assess whether that could be helpful to consider in developing TRE standards.

### Safe data linkage and quality control

#### Prompts

- How do we easily and securely share data across environments?
- How can we safely link different and potentially disparate datasets together?
- How can we ensure data quality in huge, complex, and standalone datasets?

#### Discussion

In practical domains, like health, data that is created by practitioners is not always created to be used for data analysis.
Encoding may not follow precise details but rather broad categories.
Even if data is the same, if it is processed in two different environments it can lead to different results when analysed.
It would be useful to have a schema that all data providers need to abide by, but this would be difficult to implement and would require policy-level decision-making.

A way to resolve this could be to introduce clear reporting around data processing by TREs.
Templates and guidance on reporting, and processing data, could be developed.
However, further questions arise surrounding the responsibility for processing raw data, and whether that sits with the provider, or TRE team.
In either case, it would be difficult to ensure processing is happening in a standardised way.

Further options, like an API to share data across TREs, or incentives for data quality assurance, could help with the issue of data linkage.

#### Next steps

- Discuss and resolve the question of who has responsibility for data quality, and how they are incentivised
- Talk to people providing TREs and see how willing they are to describe how they do processing.
- Determine whether anyone links data between environments currently?

### Ingress/egress mechanisms/controls/policies

#### Prompts

- How can we make it easier for users to ingress/egress files?
- Can the work of data governors who have to review files be partially automated?
- Is it acceptable to automatically proxy limited external repositories?
- How can we ensure all packages and software are up to date without compromising security?

#### Discussion

There are different considerations to bear in mind depending on what is being ingressed or egressed.
For data, some organisations process the data before ingress, whilst others bring in raw data and process it within a TRE before making it available to researchers.

For software, it was noted that it can be hard to manage repository mirrors, and therefore processes were needed to update software and packages whilst maintaining security.
Some organisations operate on a partial CRAN/PyPi mirror, and have a process for requesting additional packages, whilst others operate more flexibly and provide users with the exact packages they request.
One key question to consider is the negative impact of software and file ingress being done incorrectly - could it just affect one machine and make it unusable, or could it affect the entirety of a research project?

Further discussion should be had around the best way to update virtual machines themselves, to ensure they are running with the latest OS updates and patches.

For egress, teams have a variety of approaches involving different stakeholders.
This can range from checks by team members, project investigators, IT teams and information governance officers.
It was agreed that some mechanism for quantifying the sensitivity of the egress outputs, and guidance on appropriate ways to carry out egress, could be useful - a starting point could be the Turing Institute’s data classification process.

#### Next steps

- Establish a shared method for data classifications across TREs, and explore what methods already exist at different institutions
- Form guidance on how ingress (and egress) should work, for instance whether all TREs with NHS data should receive information in the same way.
- Everyone to share their current data classifications with rest of the community

## Conclusion and next steps

The day wrapped up by bringing everyone back together for a washup, to share the main outputs from the breakout discussions and to agree on the best next steps for the community to take.
After some discussion, it was agreed that we should:

- Set up a space to communicate, and to share knowledge. It was agreed that initially the communication space would be a Slack channel, and the knowledge space equivalent to a ReadTheDocs site.
- Meet approximately quarterly remotely, and have one meeting per year that is hybrid remote/in person, and to schedule the next of these meetings for late November
- Finalise the community commitment and begin engaging relevant organisations and project teams
- Carry out information gathering on projects working in the TRE space, in the UK and (if possible) internationally
- Explore possible funding routes and pathways for collaborative proposals
- Over the next two months, work will be carried out in these areas. At the November meeting, we will have a progress report on each action, and as a community discuss how best to move forward into the future.

## Contact

If you have any questions, feedback, or thoughts to share, either about this report or anything else, please contact Hari Sood (hsood@turing.ac.uk)
