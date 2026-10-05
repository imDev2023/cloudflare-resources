---
description: Secure Internet traffic and SaaS apps.
title: Understand and streamline policy creation
image: https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/og.png?v=89e5e1d83a570938
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/learning-paths/llms.txt  
> Use this file to discover all available pages before exploring further.

# Understand and streamline policy creation

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Before you begin building security policies, there are a few key details about Gateway to review.

The next few modules will cover the breadth of types of policies and actions that can be accomplished by sending traffic through the Cloudflare Gateway inspection engine. This implementation guide assumes that your goals are to block threat actors from using attack vectors on your user base (such as malware, complex phishing attempts, and credential theft), as well as detection and prevention of threats to your corporate data (data loss prevention). These security threats may take internal and external forms. Separately, we will detail building threat prevention that uses our Remote Browser Isolation technology to maximally reduce the theoretical attack surface for your users.

This guide will provide you with a baseline of recommended policies to build and address common questions about policy building and accomplishing explicit outcomes.

## Objectives

By the end of this module, you will be able to:

- Understand the order Gateway enforces policies for filtering traffic.
- Create reusable lists for Gateway policies.
- Subscribe to indicator feeds for advanced threat intelligence.
