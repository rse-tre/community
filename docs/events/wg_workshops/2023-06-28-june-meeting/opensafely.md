# OpenSAFELY community presentation/discussion notes

Speaker: Seb Bacon (Bennett Institute)

- OpenSAFELY is an open software, not a database
- Give researchers access to a huge amount of data through TPP & EMIS

  - 58 million patients' GP data
  - &gt; 70bn rows of primary care data
  - Key health datasets, e.g. death register, A&E, hospital cases etc.
  - Research datasets, e.g. ONS, ...

- Not a database

- Installed on top of for example TPP and EMIS (GP health record system providers)

  - TPP and EMIS are the ones running the database and providing safe infrastructure

- How did it gain rights/earned trust to manage this data?

- OpenSAFELY addressed 4 core problems:
  - Privacy
  - Transparency
  - Reproducibility
  - ....
- OpenSAFELY is giving access to data at arms length
- As a researcher you don't do data curation on the real data, you do it on randomly generated ~~synthetic~~ data (not synthetic, for reasons not explained today)
  - Code can be generated and tested to ensure it will work on real data
  - Code is run within SDE separate to the researcher
    - Researcher never has access to the SDE
  - Code for the platform is online, fully tested and documented
  - Every bit of research that has been run with sensitive data on the platform has to be open by design
    - Code can't be run unless it can be taken from GitHub
  - Earned trust through transparency
    - Latest job requests logs openly available
      - Inc info on project, who ran job, how long it ran for etc.
    - Linked from dashboard to code that was run
    - All outputs that have been output checked as safe to release viewable on the dashboard
- Code is rarely shared between projects
- Using the SNOMED codes but hard to know if these are as accurate as can be
- ehrQL: Special language created by OpenSafely for data curation
- Federated analysis: single codebase, executed in multiple locations. Moves code to data.

## Questions

Synthetic data:

- Is the synthetic data generating process published anywhere?
- Can OpenSAFELY produce synthetic data at event level?
- What's the difference between fake data and synthetic data?
  - External comment: I think synthetic data will always be something that retains some properties of the original data, because it has been generated _from_ the real data, using some kind of synthetic data generation algorithm. Fake data is just random, but structured in the same way as real data

Researchers:

- Are there limitations to the 'data at arms length' approach?
- Does arms length data access make code debugging more difficult?
- What's the scope of the research use cases you could use this approach for? All?
- How much buy-in have you received from researchers? Are they generally receptive once they understand, or do they go to other TREs instead?

Reproducibility and analysis:

- What happens to the history of auditable work if GitHub disappears?
  - We back up the code as well! (but not presently the entire history, just the executed versions; the full backup is on the roadmap)
- Have you thought about how the advantages of this system (data at arms length) can be applied to situations where there is less (or no) concern about public trust. For example, non-personal data owned by a private company, outputs not produced for public benefit, privately funded research, _etc._
  - the arms-length aspect is of less relevance in those cases, but I'd make the case that the "trojan horse" of it enforcing reproducible ways of working is pretty compelling for many use-cases
- how does a researcher validate the output? how do they know they've really got what they asked for and didn't make any mistakes in their code?
  - the usual epi/stats validation methods like dual coding, cross tabs, etc - it's the same problem whether it's arms-length or not. If you can see the raw data it can _feel_ a bit more convenient to eyeball the values but that can be misleading and give false reassurance, there's no substitute for using robust prespecified techniques
- When we refer to 'federation' here we're referring to federated analytics right? So sending the query?
  - broadly speaking I mean writing the code once and running it in several places without changes. it's a whole other presentation though!

Data:

- Who codes the data? Researcher, or some central function?
  - researchers with support from our experts
- Do you have a metadata catalogue (data dictionaries, file/table names, etc)?
  - yes, it's all there in https://docs.opensafely.org/ ; due to the way we expose data it's not quite in the form of table/file names though
- Do you get metrics on completeness, diversity etc? +1
  - of the data sources? by definition the GP data is basically all the population of the country (_almost_ - not quite space here to explain in detail!)

Outputs:

- Presume output dataset also doesn't leave environment, i.e. researcher sees virtually? And where _is_ the data, UoOx kit, cloud...?
  - researchers access over secure connections within secure environments provided by the backend (i.e. TPP and EMIS). This may be in the cloud, or not, depending on the backend
- GP data has known data quality issues i.e. speculative input of diagnosis codes. For example to ascertain epilepsy you might want to combine diagnosis codes with anti-seizure medication within a certain timeframe. Can OpenSAFELY allow this granularity?
  - yes 😀
- how are outputs checked? manually or automatically?
  - manually. we have some ideas for automatic stuff, but it's important to tread carefully here
- Do you have guidance or approvals for researchers on what outputs they're allowed - e.g. what level of granularity is allowed
  - Yes: https://docs.opensafely.org/releasing-files/

Governance:

- How are the research projects evaluated and approved? Is there a Data Access Committee of some sort?
  - NHSE is responsible for this due to our legal basis of operation
- For what uses can you access the data (i.e. only for COVID-related work, or other things too?)
  - Currently covid only, we'll be working on the possibility of wider legal bases over the next few months

Other:

- Where is this going for how people get access to data?
  - If we all keep doing what we're doing, eventually we'll converge & increment
  - There is a lot of support in the NHS for the OpenSAFELY approach
  - It isn't quite a TRE, it's a set of best practice, which can be deployed in any TRE
- How do you evaluate and approve research projects, and do all the output checking?
  - Evaluation/approval: did it with NHS England. Trying to help them prioritise research that would happen quickly.
  - Output checking: output checkers have to be approved by the output checking programme from UWE. There is tooling in OpenSAFELY to do that. In the future NHS England will start doing more output checking too
- Patient data is characteristically messy, being able to look at the event level is important for researchers to evaluate the quality of it. How do deal with that, are you able to create synthetic data at an event level?
  - It is messy, but also very rich
  - It is not really synthetic but dummy
  - Relies on a curated code list to match patients (good thing!)
- Buy in from researchers?
  - Enormous votes of confidence in it from various groups, after they've been given support on getting going (after a few weeks)
  - Service being slow can be mitigated by other parts of the software (documentation, ramdom data generated automatically)
- Does it make code debugging harder?
  - Not harder, slower. Focuses more on a unit testing approach
