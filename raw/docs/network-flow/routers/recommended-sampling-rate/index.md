---
description: The best sampling rate recommendations for your network's traffic volume.
title: Recommended sampling rate
image: https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/og.png?v=590ca5d1a82b28d9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/network-flow/llms.txt  
> Use this file to discover all available pages before exploring further.

# Recommended sampling rate

Last updated May 7, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/network-flow/routers/recommended-sampling-rate/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Your router samples the traffic that passes through it to create NetFlow or sFlow data. The sampling rate determines how frequently your router captures a packet — for example, a rate of 1 in 100 means your router captures one out of every 100 packets.

Sampling more frequently (lower ratios like 1 in 100) produces more accurate flow data but uses more router memory and CPU. Sampling less frequently (higher ratios like 1 in 4,000) reduces resource usage and is suitable for networks with larger traffic volumes.

The following table provides general recommendations based on your traffic volume. Test different sampling rates to find the best option for your network.

| Traffic Volume | Router sampling recommendation |
| --- | --- |
| Low | Between 1 in 100 packets - 1 in 500 packets |
| Medium | Between 1 in 1,000 - 1 in 2,000 packets |
| High | Between 1 in 2,000 - 1 in 4,000 packets |

As a general rule, you may notice a loss in data accuracy (depending on your network volume) when your network flow sampling rate exceeds 1 in 5,000 packets.
