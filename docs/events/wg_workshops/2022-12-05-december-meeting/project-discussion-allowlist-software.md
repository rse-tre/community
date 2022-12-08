# Project discussion: How best to whitelist software packages for secure environments

Issue faced at the Turing: the need to know beforehand all the tools needed and making sure they work within the TREs.
We came up with a list of packages that are reasonable to have, but then it gets even more complicated as each package has versions and each version has different dependencies with other packages and different requirements. Maintaining the list and making them available becomes cumbersome.
So open to all, how do we tackle this?

## Notes

- Why do you want to white list these software packages? What makes them 'un-safe'?
- There have been instances of malicious code as part of more standard software packages

Can we take first a step back and ask, why do we need a whitelist in advance? What makes a package unsafe?

- by the time you want to start the work within the TRE it is too late to go through the process of checking and installing
- When you are worried about ingress and egress certain packages can break the rules you established for it in the TRE

It's tough and depends on your risk apetite.
From a perspective of a Health TRE we make a single load at the beginning and people pick from there.
From a governance perspective we need to restrict the capacity for change of those using (not managing).
Even a mere technical check in the process to install already helps.
Not so sure what to do for installing GitHub repos which is not allowed but more and more people want to be able to do so.

- Reliance on curated repositories eg. CRAN, Conda (but not PyPI, conda-forge)
- Why use snapshot rather than live conda?
  - Historical (better for auditing?)
- Maybe we trust some sources more than others, a kind of community decision/preference.
  For example, Spack and Ubuntu repositories have more oversight than PyPi.

The dependency management issue is very much similar to that faced by HPC facilities.
This adds an additional security challenge but the problem is familiar to HPC centre manager teams (module files, Spack, Easy build etc).

- How hard/time consuming is the way HPC do things, would it be practical to copy their approach each time a cloud deployable TRE is set up?
- Usually done as a one-time thing for the env, updated periodically.

I think there might be a case to discuss (maybe another time, not sure) "before" and "after" validation.
Whitelisting suggests making sure the software is compliant and safe before using it.
Other processes can be used to verify nothing wrong happened in the environment _after_ the software was used.
Cost of prevention vs. cost of remediation.

Most environments are used with data analysis tools (R, Matlab, Excel).
There is to be expected more demand going forward for other tools.
How do we give that to people?
Possible road to take: Provide Dockerfile for ingress review, build the container outside in a managed service as part of the TRE codebase following positive review, ingress the container.

- Consider prescanning with eg. Snyk for vulnerabilities
- Compiled programs not necessarily higher risk.
- Is there a difference between interpreted vs compiled code in terms of TRE safety/risk?
- In principle, no, in practice yes.
  There aren't always repositories with source code for compilation (less trustworthy?)

## Summary

- How to provide secure packages to TREs, and how to give the balance of security and usability.
- Some TREs allow CRAN or Conda but not other repositories.
- We discussed the kind of repositories that we trust (for example those backed by a trusted community).
- So we need to come to a common agreement of what we trust.

## Actions/next steps

- Possibility for a shared list of 'trusted' software packages as part of this community
