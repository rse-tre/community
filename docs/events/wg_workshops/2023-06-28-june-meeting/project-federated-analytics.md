# Problems with multiple technology solutions for federated analytics

**Session 2, Room 1**

Chair: Tom Giles (Nottingham)

## Outline

Installing and managing multiple federated analytics toolkits on Trusted Research Environments (TREs) can present a significant burden, requiring careful coordination, technical expertise, and ongoing maintenance. The process involves a range of challenges and considerations specific to deploying and managing federated analytics toolkits in a secure and potentially distributed environments.

Selecting and managing one or more federated analytics toolkits on a TREs can be complex and laborious. It involves evaluating features, compatibility, and performance, as well as installing, configuring, and integrating the toolkits with TREs.

Current factors that add to the burden of managing Federated infrastructure effectively:

1. Installation and Configuration: Installing and configuring multiple federated analytics toolkits on TREs is laborious. It involves managing software dependencies, libraries, and frameworks, with each toolkit having its own requirements. Technical expertise and attention to detail are necessary.

1. Integration with TREs infrastructure: Integrating federated analytics toolkits with TREs requires careful coordination due to specific requirements and interfaces. Ensuring compatibility, secure data exchange, and efficient communication may involve custom development or adaptation.

1. Security and Privacy Considerations: Managing security and privacy for multiple federated analytics toolkits on TREs is burdensome. It includes configuring secure communication, access controls, and ensuring compliance with privacy regulations.

1. Resource Management: Efficiently managing computational resources on TREs for multiple toolkits is complex. Optimizing resource allocation, load balancing, and scalability require planning and monitoring.

1. Upgrades and Maintenance: Regular updates and maintenance are needed for federated analytics toolkits. Managing multiple toolkits involves staying up to date, ensuring compatibility, and applying patches, which is resource-intensive.

1. Training and Support: Training TRE operators to handle toolkits and providing ongoing support can be time and resource-intensive. Troubleshooting may also be required, adding to the management burden.

## Prompts

1. What are the considerations and challenges involved when selecting which federated analytics toolkits TREs should run?
1. What are the challenges when combining federated analytics toolkits with a TRE's existing user authentication and disclosure control services?
1. What security and privacy considerations need to be addressed when managing federated analytics toolkits?
1. What are the tasks and challenges associated with upgrading and maintaining multiple federated analytics toolkits?
1. How can TREs ensure all federated analytic tools conform to the Five Safes framework?
1. Should frameworks be developed to standardise the plumbing for federated analytic tools and users?

## Notes

- Intro
  - Many federated analytics tool kits
  - Desire to use these
  - OpenSAFELY, DataShield - Open source
  - BCPlatforms (?), BitFont (?), IQVIA - proprietary/commercial
  - Integrating these requires installing a (large) stack, ensuring compatibility with IG
- **Why use a Federated Toolkit in a TRE?**
  - Network effect. If other TREs use one or user want one. Consistency across TREs would benefit research
  - However, supporting &gt;1 per TRE is a large burden. How to choose when to say yes, when to say no
- **How to combine a Federated Toolkit with existing authentication and disclosure control**
  - Reject requests if they are not compatible. Possibly reconsider if there is strong demand
  - Becomes harder to convince TREs to add a toolkit after they already have one
- **What extra security considerations are there?**
  - How do you maintain your standards/expectations?
  - Getting everyone to conform to 5 safes, logging the same information (to produce similar audit trails) is very difficult.
    Can TREs be standardised and leveraged to handle this? (move burden from federated toolkits)
  - Consideration of sensitivity level of data in a TRE. (DARE has a 1-7 scale). For example, access to strongly pseudonymised data is less risky than trivially identifiable personal data.
- Working on 'format' to describe 5 safes requirements for data objects. Could lead to a situation where any federated toolkit can be applied, conforming to the data objects 'rules'.
  Standardises audit trail
- Should be standardise this?
  - There are advantages yes. Getting buy in from enough (a majority) of TREs will be difficult (and necessary)
  - SDE network is an opportunity as they are (technically) similar
- Where to start? Target TREs with large impact, similar technology stacks?
  - DARE work focusing on 'proof of concept' with synthetic data across multiple TREs.
    Funding already in place to put into practice
- From NHS researchers perspective, understanding of term federated analytics may be different.
