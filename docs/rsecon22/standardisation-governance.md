# TRE Satellite Event notes - Standardisation of information governance, certification & regulation

## Prompts

- How we do standardise sticky issues around ethics?
- What definitely can/can't be standardised?
- Can certifications and governance reviews be done once for each TRE code-base?
- Can information governance reviews be shared across TREs?

## Notes

- Standardisation is made difficult due to a large variety in data:
  - Types of data
  - Sensitivity
- Does this diversity make creating effective standards difficult
- M: Standards:

  - ISO27001
  - DSPT
  - Cyber Essentials (+)
  - from M's notes earlier!
    - What existing standards do builders of TREs attempt to adhere to?
    - What existing standards do data owners expect builders of TREs to adhere to
    - Is this likely/close to a complete set or are there gaps?
      What are those gaps?

- R: Experience approaching ISO27001 certification. More 'free form process' rather than a prescriptive set of requirements
- A: Lack of definition for 'TRE' also makes standardisation difficult from the perspective of data providers
  - Feedback from working on Goldacre report. Preference for a small number of TRE implementations
  - Alternatives could be many implementations of one (or small number of) specification, federated set of similar/compatible TREs
- Small number of large TREs will likely made data access/sharing/linkage easier as it will be easier to develop trust between the TREs and between all TREs and data providers
- NHSx (?) report on the future of TREs (SDEs) proposes 'soft' accreditation to make multiple projects on one TRE involve less friction
- H: 'Data lakes' for storing very large amounts of data - accredited TREs could get 'easy' access to this data
- How to get towards these ideas?
  - A single implementation which demonstrates the use of a data lake/passport
- S: How flexible can a passport be? Researchers may be told where they will work and not be able to choose. The benefit of a passport will depend on who/what (people/organisation/TRE) the passport applies to
  - R: Easier to apply some kind of accreditation to a TRE rather than people. TRE can 'guarantee' some level of security through technical controls and processes. This can be aligned with the expectations/requirements of data providers
  - A: For health data, there also needs to be a consideration of protecting the interests and rights of data subjects
  - A: Observation from work with HRA, governance is difficult to enforce with code alone
- R,A: Section 251 objection for a research project allows bypassing some GDPR requirement. Unclear if this kind of exception could apply to a whole TRE/secure data store.

## Actions/next steps

- Survey and take inspiration from what already works and is 'acceptable' in the UK. _E.g._ UK BioBank
- Create a clear definition of what a TRE is (and is not). This is important for data providers.
- Survey the 'hard requirements' for difficult organisations/types of data. _E.g._ Cyber Essentials + for MOD.
