# Maintenance burden and its impact on TRE development

**Session 1, Room 1**

Chair: Jim Madge (Alan Turing Institute)

## Outline

A major challenge in TRE projects in maintaining a TRE codebase.
The code can have a large number of lines, particularly as extra configuration is added to

- fix bugs,
- and improve security.

The code may also be, necessarily, complex involve many languages such as

- Programming languages (e.g. Python)
- Infrastructure as code language/frameworks (e.g. Terraform, Pulumi)
- Bootstrapping tools (e.g. CloudInit, ARM templates, ...)
- Container orchestration (e.g. Kubernetes, Compose)
- Configuration management (e.g. Ansible, Chef, Puppet, Salt)

Furthermore, writing the codebase requires good knowledge of the technologies a TRE is built on such as,

- Networking (e.g. subnets, masking)
- Internet protocol suite (e.g. DNS, SSL, TCP)
- Linux (e.g. Permissions and ACL, PAM, systemd, distributions, packages)
- Containers
- Virtual machines
- Cloud providers (.e.g. AWS, Azure, DigitalOcean)

These factors contribute in making codebases that are difficult to maintain.
Finding people with the skill set to work on these projects can be challenging.
Perhaps especially in academic/public sector spaces where wages are not competitive with roles using similar skills elsewhere.
Making progress can be difficult as the effort required keep a TRE working correctly uses a lot of developer time.

## Prompts

- Is your codebase difficult to maintain?
- How many people work on your codebase, how many do you think it needs?
- Do you struggle to find or recruit people with the skills you need?
- Does the complexity of your codebase hinder or prevent you making improvements?
- Are you looking to reduce complexity (for example by changing the tools used)?
- If you were to start again, what would you do differently?

## Notes

- **Setting the scene:**
  - TRE codebases are large and complex and grow with time
  - Could be/likely to be multi-lingual (software-wise)
  - Lots of config alongside code
  - First challenge is finding enough people with the right skills across a broad landscape
  - Second challenge is maintenance overhead is so great that it drowns out time for development
- **Funding and recruitment**
  - Big enough to break out into a different discussion.
    - Fought hard to pay RSEs more than default institution salaries
    - Make the work environment attractive e.g. nice place to work
  - Bennett Inst have found a way to pay engineers "sensible" salaries to attract the right skillsets; it's also a nice place to work (and that doesn't come for free - creating that environment takes a lot of effort)
  - Things like
    - Autonomy
    - Interesting work
    - Coming together regularly
    - Career development pathways focusing on tech rather than management
  - Turing RSEs also have permanent contracts - unusual in academia
- **Code complexity / maintenance:**
  - Onboarding new engineers into a big codebase project is difficult. Conversely, engineers leaving causes a leak of knowledge which is difficult to recover
  - Supporting multiple projects when each project is so different
  - Use code reviews
  - At Dundee it's based on a bigger codebase from AWS, therefore it's harder to wrap your head around a project as you have to understand the AWS codebase first
  - How can authors of code be sure that other developers understand their code / codebase?
  - Very good point in TRE land: if you don't understand the codebase, how can you trust it, and how can you convince the infomation governance authorities that it's trustworthy?
  - Documentation is on par with effort to writing the codebase (although is it the most useful way to impart knowledge? Does anyone read it...?)
  - Investing in comprehensive build systems (Bennett Inst use "just") is one way to manage technical debt
    - https://just.systems/man/en/
    - https://github.com/opensafely-core/job-server/blob/main/justfile
    - https://github.com/opensafely-core/ehrql/blob/main/DEVELOPERS.md
  - Difficult to experiment with codebases
  - Is there an argument for having owners of subsections of a TRE codebase rather than expecting a small number of people to understand all sections - a product management approach?
  - We are trying to do this in an ongoing rewrite
- **Hindering development:**
  - Feels like skills and funding are the large problems
  - Prioritisation is also important, particularly if we have a small team. Balancing maintenance and new features
    - Consider your stakeholders.
    - Your users rely on you
    - Academic funding does not support maintenance
  - In terms of team structuring, we have been inspired by https://teamtopologies.com/

## Actions/next steps

- On funding and sustainability, the [Funding & Sustainabilty WG](../../../structure/funding-sustainability) is planning to write a position paper on short-term funding/long-term operation headache. Do join in!
