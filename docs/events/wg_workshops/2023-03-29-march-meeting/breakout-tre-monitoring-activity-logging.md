# Breakout discussions: TRE monitoring and activity logging

## Prompts

- What tools do people use for monitoring (e.g. Grafana, Prometheus, Loki, Mimir etc.)? To what extent do people monitor?
- To what extent do people actively monitor / alert on logging activity (vs collecting for incident / post-incident management)

## Notes

- Essentially logging everything (with AWS). Previous group was talking about logging all the way to individual VMs etc.
- Pushing within EPCC for more application layer logging rather than just at the hardware layer, lots of pushback for monitoring of user activity (e.g. anonymisation of logs)
- Logs primarily used for monitoring our own systems rather than proactively checking behaviour of users.
- Often simply the fact that you're logging is really just a comfort factor for data providers, often they may not be used/read at all and deleted at some stage - but the point is more that if you need it then you've got it.
- To what extent do people monitor/alert logged data, rather than just access it for incident management/review?
  - Consensus is that in many TREs we don't pro-actively monitor alert on logging, but there is value in having it for incident management/review and for giving confidence to data owners.
- When is low level data access logging/monitoring appropriate?
  - Consensus that it's required when identifiable individual level data is accessible.
  - Ran out of time to determine to discuss whether/how much value it adds when data is de-identified and research is analysing the full dataset.
- Based on experience, there is a general disregard from users for the details of data governance.
