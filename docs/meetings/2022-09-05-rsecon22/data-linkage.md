# TRE Satellite Event notes - Safe data linkage and quality control

## Prompts

- How do we easily and securely share data across environments?
- How can we safely link different and potentially disparate datasets together?
- How can we ensure data quality in huge, complex, and standalone datasets?

## Notes

- When you are linking datasets you can have false positives, with non-distinct UID.
- Can you rely on UIDs like NHS number? Not in all cases, there are edge-cases where even robust identifiers do not exist.
- In the medical domain the data quality is very poor. Encoding is inconsistent across trusts and people.
- In practical domains, like health, data that is created by practitioners is not always created to be used for data analysis. For example codes are mainly used within trusts to validate money expenditure (so may not follow precise details but rather broad categories).
- Even the same data in two different environments may be processed differently, leading to slightly different results when analysed.
- If we had access to the methods of processing, you could ttry either 1) different ways of processing the data, or 2) different TREs, then report the variance.
- Here we are talking about openness of processing. If every TRE that pulled data from a NHS data lake is clear about how they processed their data we could report that.Or perhaps we could give instructions/templates of how to process the data.
- Who is responsible for data processing of the raw data? Is it the TRE providers, or the data holders?
- Ideally, it is with the data holder, since then you can assure quality. But practically you do not have any leverage so the onus is with the data users to caveat the data.
- Does trusted research environments imply trusted data? (Flippantly) Should instead they be called Secure Research Environments instead?
- Perhaps data quality isn't being incentivised enough. Is there a way to commercialise the data quality assurance process? The current commercial options seem to have no incentive to make the data easy to use and access.
- It would be so useful to have a schema that all data providers need to abide by. But this would be a tall order and would require policy-level decision-making.
- An issue with a TRE provider doing data processing is that data processing requires a lot of domain expertise, which feels like it requires a researcher.
- Does anyone link data between environments currently? Not to our knowledge. This may require significant pseudo-anonymisation. Might require TRE to TRE negotiation or an overarching TRE defining.
- Perhaps a standard API between providers would facilitate moving data between TREs.

## Actions/next steps

- Next steps thought: who has responsibility for data quality? How do we pay them?
- Action: Talk to people providing TREs and see how willing they are to describe how they do processing.
- Does anyone link data between environments currently?
