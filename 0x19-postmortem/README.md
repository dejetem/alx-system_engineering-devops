0x19. Postmortem

# Postmortem

Learn how to write an incident report, also known as a postmortem. This postmortem follows the guidelines strictly used by Google engineers for submitting reports. The report consists of five parts: Problem Overview, Timeline, Root Cause Analysis, Solution and Recovery, and finally Corrective and Preventive Actions. Let's take a closer look at each of these parts.


##  Issue Summary

* Duration of the outage with start and end times (including timezone)
* what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
* what was the root cause


## Timeline
* when was the issue detected
* how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
* actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
* misleading investigation/debugging paths that were taken
* which team/individuals was the incident escalated to
* how the incident was resolved


## Root cause and resolution

* explain in detail what was causing the issue
* explain in detail how the issue was fixed


## Corrective and preventative measures

* what are the things that can be improved/fixed 
* a list of tasks to address the issue 
