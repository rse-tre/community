# Breakout discussion: Network access inside a TRE

_Chair: Simon Li_

## Notes

- What angle is this coming from?
- What do TRE admins see as acceptable
- Cloud services, e.g. blob storage, limited file shares outside TRE. Some users allowed to egress non-sensitive data outside TRE
- Limited proxy
- Full session recording for audit purposes? Tried it for central government projects, defence-in-depth. Discussions about security dominate
  - "Privileged access management" system: Brokers access to different endpoints for admins, so they can manage environment but everything is monitored so can be "replayed" at any point in future
  - https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=4AA8-1466ENW
  - Machine learning security controls for anomaly detection. Begins by learning pattern of normal behaviour.
  - False positives? How much work to investigate reports? How disruptive for users?
    - Start in learning mode for several months or longer. Can manually override rules if necessary. Only set to automatically block network connections after you're confident. Then need 24/7 team on hand to quickly investigate and remedy alerts depending on risk profile
- One worry with network access is DNS which could be used to egress data, so you need to run a secured dns service
- Thought about using AI tools to spot disclosive analysis patterns, but very complicated and variable input types. Analyse logs of what people have done, not just outputs
- Sheffield/AWS: ISO27001 defines requirements for network controls. Less focus on monitoring, network controls are to protect users from themselves.
  - Looking at something similar to HIC, with restricted network proxy. Can't close off environment completely, but need restrictions on what they can do.
  - Deciding whether to go cloud antive route or build own proxy
  - No developers in infrastructure team though (which drives use of cloud tooling as a primary option)
- Building everything in OpenStack
