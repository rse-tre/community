# Project discussion: Managing software/package install and licences on secure environments without internet access

## Prompts

- How do we get users actually working on their projects? Code/libraries/software etc
- How do we manage licencing?

## Notes

- Sheffield has 2 environments in TRE, one secure with access to internet SDSTP accreditation, one very secure with no internet access, ISO27001
- Not open-source (RONIN) https://ronin.cloud and AWS TRE
- Looking for experiences of how other TREs have made it work
- HIC have the same issues - some open source solutions on [GitHub (ansible roles)](https://github.com/hic-infra/shared-services-ansible-roles/)
  - There is _some_ internet access
  - Stuff gets automatically scanned for viruses - squid proxy controls what users can/can't access (? maybe I got that wrong)
  - Use of a internal licence server for matlab
  - Researchers put up with the limitations given that it's the only way they can access the data
  - HIC have ISO27001 accreditation - this includes on prem TRE and extends to the cloud TRE now.
- KCL: OpenStack at the moment, looking at Azure
- Virtual box which can access external internet. Also use squid for scanning and filtering
- A lot of variation in what researchers request - but trying to hold a lot of stuff locally
- [Provide software (~23 applications)](https://www.ucl.ac.uk/isd/services/file-storage-sharing/data-safe-haven/software-and-services)
- Encrypt data
- Users aren't allowed to control their own software (for now) but there are exceptions - for example if users need access to specific websites for data
- Did research on global TREs and generated list of softwares based on this & requested lists from users/asked them to confirm they were happy with it
- [SCCM](https://en.wikipedia.org/wiki/Microsoft_Endpoint_Configuration_Manager) to allow users to install specific software without admin privileges (though it's possibly too big for the number of expected users)
- [Manage Engine - Endpoint Central](https://www.manageengine.com/products/desktop-central/) is free for up to 25 devices - above this only £18/year - cheap tool
- Tools like this are probably useful more widely across the group
- EPCC - one issue is the scale of setup, for long-term research projects encourage users to set up containers with the relevant software and then import these
- Also can let users assemble a VM and import this into the environment
- Some software stacks are complex and impose a huge resource cost onto the admin team - the users can accept the risk of importing that stack into the TRE - users generally happy to work in this way
