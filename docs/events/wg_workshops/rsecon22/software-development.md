# TRE Satellite Event notes - Managing software development in a TRE

## Prompts

- What tools and applications are needed inside a TRE to enable software development?
- How do we make it easier to share code inside and outside a TRE?
- Best practice for developing and publishing code used in a TRE?

## Notes

Challenges:

1. How to produce realistic dummy data.
2. Develop code within TRE, or both inside/outside.
3. Encouraging researchers to use good development practices esp. version control.
4. Who does data cleaning and when - data providers, TRE operators, researchers.

Developer classes:

- Developers of code to provide TRE and services to researchers.
- Developers of code to do research.

Challenge of producing/getting realistic dummy data, noise, dirt and all, instead of an idealised subset. Especially pertinent to large, unstructured datasets.

5-6 attendees work with/as software developers in TREs.
Some attendees would prefer researchers provide code via Git repositories, but sometimes researchers have .tar files.
Useful to promote guidelines for researchers on reproducible, accessible, and tested, code. Relates to E's talk.
G ran a 2 week workshop, using Tier-2 level security TRE. Researchers could access internet but with restrictions on pipeline libraries. Relates to more general issue of how to allow developers to access specific pypy libraries. Workshop also required researchers to be familiar with Git prior to the workshop. It was challenging to teach processes and deliver reproducible results within a fortnight.
Some researchers do see the need for revision control.
Jupyter Notebook and challenges in using this with revision control. RMarkDown can be far better for this.
There are tools that provide pre-/post-commit hooks in GitHub to handle notebooks.
Anything which allows a researcher to record that "this seems to work" in an automated way can help with reproducibility.

TRE "driving tests" versus risk of imposing too high a barrier to researchers.

## Actions/next steps

- Encourage researchers to join the RSE community and adopt RSE good practices.
- Identify whether requirements discovery is done differently for TREs than for other research projects.
- Identify minimum set(s) of softrware and data skills researchers should/we would like them to have if doing data analysis within a TRE.
- Secure funding to run a study to identify researcher classes, software/data skills/knowledge required, and TRE options open for them.
