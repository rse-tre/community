# Breakout discussion: Data sensitivity

_Chair: Will Crocombe_

## Notes

- Some work DARE UK funded previously on this: https://dareuk.org.uk/sprint-exemplar-project-priam/. Currently https://dareuk.org.uk/driver-project-sara/ and from an AI/ML risk perspective https://dareuk.org.uk/sprint-exemplar-project-graimatter/.
- Another group that may be useful to get in touch with more broadly on this: https://securedatagroup.org/
- The Genomics England (GEL) model, which is a well established 'TRE' in the genomics space (100,000 genomes project etc.), basically focuses on the 'safe outputs' component rather than evaluating the risk at the start. But this may be domain specific (e.g. genomics).
- Want data to be accessible, which model works for a TRE rather than per dataset, use automated tooling [RDMP](https://github.com/HicServices/RDMP) to anonymise data. Limit release e.g. if only 2 of 500 subjects meet requirement that wouldn't be allowed.
- How does pseudonymisation work in the context of classification? If there is a risk of de-anonymisation should that stay at high classification, even if the data released for research might be classified at a different tier considered in isolation?
- Where data comes from dictates necessity for different tiers. What does it mean in practice?
- Use tooling (RDMP) to provide data to researchers required for the project. Discussion with researchers to identify required data takes longer than selecting that data and providing it. All data is controlled ingress and egress under Tier 3.
- At Turing who makes decision about classification?
- Don't recommend use of TRE for Tier 1 and below. "Data controller has authority to publish the data on internet". Tier 2 and 3 have similar controls. Medical data stays at Tier 3.
