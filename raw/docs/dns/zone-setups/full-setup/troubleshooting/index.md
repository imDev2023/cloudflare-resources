---
description: Learn how to troubleshoot issues with a primary setup (full)
title: Troubleshooting
image: https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/og.png?v=21a55a939107386a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/dns/llms.txt  
> Use this file to discover all available pages before exploring further.

# Troubleshooting

Last updated Jul 29, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

If you see unexpected results when [changing your nameservers](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/), review the following troubleshooting questions.

Note

If your zone is still in **Pending Nameserver Update** status, refer to [Zone stuck in Pending Nameserver Update](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/pending-nameservers/) for a step-by-step check of the delegation at your registrar.

## Is a DS record present at your registrar?

You need to remove any pre-Cloudflare **DS** records at your registrar to update your authoritative nameservers. This will disable DNSSEC and allow Cloudflare to resolve your domain name.

You can then [re-enable DNSSEC](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/#4-re-enable-dnssec) in Cloudflare and at your registrar after you have changed your nameservers.

## Do the nameservers at your registrar exactly match the values provided by Cloudflare?

If the nameservers in your registrar do not exactly match those provided by Cloudflare, your domain will not resolve correctly.

## Are additional nameservers listed at your registrar?

If so, you should remove these nameservers.

You should have only Cloudflare nameservers listed at your registrar.

## Have you waited longer than 24 hours?

For some registrars, you will need to wait up to 24 hours for updates to your nameservers.
