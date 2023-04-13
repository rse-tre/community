# Breakout discussion: TRE architectures

_Chair: Rob Baxter_

## Notes

Is there a single pattern for TREs?

- Are there multiple patterns? Where do you put you put your network isolation?
- Software defined TREs?
- Interested in abstract architectures (software implementations later)
- Abstract more important to begin with
- HDR Alliance green paper saying "This is what a TRE is" from 2021
- https://www.hdruk.ac.uk/news/new-principles-published-to-improve-public-confidence-in-access-and-use-of-data-for-health-research-through-trusted-research-environments/
- Maybe this group's first task is to update this doc?
- "Architecture": Functional (explicitly not technical), e.g. "network boxes with zones, how to they talk to each other, how does stuff come in or out"
- After the network architecture almost everything else is Governance?

At what level does an "architecture" start? Governance? 5 safes vs technical specification

- Multiple layers - Business, application, technology, service, data
- No good having a great implementation if the operating team isn't skilled
- Business architecture describes how actors interact with services
- Product agnostic, about capabilities not products
- Business layer == TRE Governance?
- How much of this is about operational security and legal/functional definitions, and how much is about data ethics?
- Former suggests there should be standards
- Latter (human ethics, no objective view) implies a TRE is what you think it is
- Operationalisation requires people to run a TRE, difficult to recruit people at the moment
- This group should think about holistic picture
- This group is the people SATRE wants to speak to, all input welcome. Lots of ways of expressing same thing, but seems like there's general alignment

Group could fous on "what does good look like"?

- Passible reference: Digital Economy Act (DEA) "standard", if you meet it UK Stats authority are happy you're safe to conduct research on UK stats data
- But maybe Governance should be the driver?
- Scottish National Safe Haven has achieved DEA accreditation
- Maturity scale to judge TREs, work backwards from DEA?
- Does DEA include things like ingress/egress? Not sure
- Approval of UKStats authority seems like a good aim, does their idea of a TRE align with ours? If so might as well go with them, but need to check if they have other requirements that might conflict with our aims and aren't applicable to all TREs
- SAIL Databank is another org that has gone through DEA. Bit like ISO27001, not proscriptive, instead asks "are the processes you've put in place suitable?"
- [Scottish Safe Haven charter](https://www.gov.scot/publications/charter-safe-havens-scotland-handling-unconsented-data-national-health-service-patient-records-support-research-statistics/pages/4/)? Criteria for accessing patient data in Scotland, and has been for 8 years \* Currently being reviewed due to age

### Final recap

How should architecture be _driven_?

- High level business diagram
- Connecting Governance and architecture is really important

How do we link together what governance needs and says with the technical definition of what TREs are?
