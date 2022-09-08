# TRE Satellite Event notes - Ingress/egress mechanisms/controls/policies

## Prompts

- How can we make it easier for users to ingress/egress files?
- Can the work of data governors who have to review files be partially automated?
- Is it acceptable to automatically proxy limited external repositories?
- How can we ensure all packages and software are up to date without compromising security?

## Notes

- M: Everything encrypted before transfer in. uploaded to a VM, then moved to each TRE location
  - Choke point, takes a while for file to be transfered from VM to TRE location
  - Data uploaded through a browser, time limited password protected URL given to uploader
  - Everything virus-scanned
  - Pre-defined IP address range
  - Had to teach people to use multi-part archive uploads. If dataset still too large then use hard-drive.
- J:
  - IG would prefer write-only anonymous drop that provides receipt
  - TRE admins don't do anything until submitter confirms receipt and says data is OK
- A:
  - Lot of people working form home, forced to access via institution's VPN
- J:
  - 7 zip
- R:
  - What managed file transfer software are people using?
  - NHS workstations very limited, can't install software, can't use VPN, so web-service for upload
- Bringing software in:
  - J: repo mirrors are too hard to manage
  - M: Take VM, remove mounted filestore, enable network, do update, remove network, add back to TRE
  - S: Partial CRAN mirror, IG approval for a one-way CRAN proxy with on-access scanning. Also conda
  - J: Main determinant is what damage could be done? If a researcher can only break their own VM it's not too bad. Still a problem because it invalidates the whole machine and data on that machine, can no longer trust anything created or analysed on that machine
  - R: User asks for a set of requirements.
  - S: Standard set of applications + some repository packages works for most people
  - T: Quite a custom platform, install whatever researchers need
  - J: How are Windows VMs updated? Do we assume not a problem since isolated? WSUS server with network access?
- Egress:
  - Output requested, approved by team
  - eDRIS: Egress approved by both eDRIS and by project PI
  - Generally prevent iandvertent data egress
  - HIC: One stage approval by IG
  - Some other institutes: two step. Approve by IG. Then IT has to approve that IG authorised to approve data egress.
  - How much security/approval: Maybe related to Turing data tiers?
  - J: Throwing ideas on how to quantify level of security for data
  - T: has application to calculate data classification and create TRE configuration

## Actions/next steps

- Try and agree data classifications across TREs, centralised severity rating
- Some form of guidance on how ingress (and egress) should work, e.g. all TREs with NHS data should receive information in the same way. Easier for TRE deployers and data controllers. "Soft" federation.
- R: might end up looking at different data classifications across TREs whilst applying for ISO certification in Sheffield
- Setup shared space so everyone can add their current data classifications (then meet up and rationalise later)
