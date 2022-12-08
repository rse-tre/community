# Breakout: TRE standardisation & accreditation

## Prompts

- Is there a feasible minimum standard that can be achieved agnostic to the research/data domain?
- Who should be responsible for developing, maintaining, & accrediting such a standard?
  Who needs to provide input to this standard?

## Notes

Already standardisation efforts in Health, but NERC are looking to setup TRE for open environmental data

Lots of commonalities across TREs, Turing has mostly been handling non-health data (e.g. finance, Government).
Having a framework for categorising data was very helpful.

- Common core requirements across all projects/TREs such as standardised logins, ingress/egress systems
- Currently in people's heads, not yet written down

Two main aspects:

- Communication to potential researchers (what do tiers mean, what should they expect, what applications are required)
- Maintenance of standard, e.g. Docker/docker-compose can be used on laptops but also deployed on cloud

Who's responsible for maintaining standard over time, who checks you're still compliant?

- Community standards body, modelled after IEEE web groups/RFCs, or industry bodies like CNCF
  Validation more difficult, not as simple as an automated test suite.
- For NHS data NHS probably wants to be the final arbiter
- Can the DARE working groups (or RSE TRE WGs) take ownership?

Maybe rather than a _standard_ what we need are a minimum set of features that _define_ what it is to be a TRE (of a certain tier)

Turing deliberately spent a lot of effort on defining data tiers because potentially couldn't rely on 5 safes as much as other TREs, so technical controls were more important

- Reproducible deployment and tear-down built-in from beginning, each project has a disposable environment

What can we do so that a TRE operator using a standard TRE codebase or architecture can shortcut the accreditation process instead of having the full tech stack being audited from scratch

- DEA accreditation?
  Pathway for accrediting a processing environment
- Arguably too much focus on infrastructure as code, e.g. should also need focus on governance
