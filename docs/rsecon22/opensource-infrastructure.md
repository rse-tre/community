# TRE Satellite Event notes - Open source infrastructure and collaborations

## Prompts

- How many open-source TREs do we want?
- Do we need separate collaborations for each open-source TRE?
- Can we collaborate across different TRE platforms?

## Notes

### What are people currently using?

- On-prem
- Azure
- AWS

### What open-source solutions exist?

- TREEHOOSE (used at Dundee)
  - based on AWS service bench
- Turing Data Safe Haven
  - BSD licence
- Microsoft AzureTRE
  - MIT licence

### Who is able to work on a common codebase?

- Azure
  - Turing
- AWS
  - Dundee (HIC)
- If a single code base is too difficult to work in practice, it would still be very valuable to have some common governance, policy, guidelines, specifications.

### Who is interested in deploying and evaluating multiple TRE solutions?

- Turing
- UCL
- Sheffield
- Dundee

### Who is interested in working on common governance specification?

- Turing
- Dundee
- EPCC

### IAC

- On-prem open stack implementations using Terrafrom etc.
- Trade off between 'transferability' and 'conveniences/maintainability'
  - Can just use VMs, more transferable but adds managment burden
- Container based solutions _.e.g._ kubernetes. Another layer of abstraction that removes cloud-vendor dependencies.
  - Running graphical desktops is difficult (maybe impossible for Windows)

### How to include HPC?

- Burst out for running particular jobs?

## Actions/next steps

- Common governance - take the initiative to set this up
- Send invitation to a kick-off meeting
- Similiar discussion on code - What do we have already, do we want to combine or adopt a single codebase
