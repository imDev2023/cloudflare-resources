---
description: Reference information for Download Cloudflare One Client LTS releases in Zero Trust.
title: Download Cloudflare One Client LTS releases
image: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/og.png?v=7fdfb7f83d0691d0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/cloudflare-one/llms.txt  
> Use this file to discover all available pages before exploring further.

# Download Cloudflare One Client LTS releases

Last updated Apr 17, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/lts-releases/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Long-Term Support (LTS) releases are stable releases that are guaranteed to continue receiving security bug fixes for at least 12 months or 90 days after the next LTS release, whichever is greater.

For more details on Cloudflare One Client support timelines and end-of-life (EOL) policies, refer to the [Support lifecycle](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/support-lifecycle/) page.

Note

No LTS releases are currently available, as Cloudflare is still rolling out our new LTS release process. When a stable release is declared an LTS release, it will be listed on this page and announced in the [Cloudflare One Client changelog](https://developers.cloudflare.com/cloudflare-one/changelog/cloudflare-one-client/).

## Windows

| **OS version** | Windows 10 LTSC, Windows 11, Windows 365 Cloud PC running Windows 11 |
| --- | --- |
| **Processor** | AMD64 / x86-64 or ARM64 / AArch64 |
| **.NET Framework version** | 4.7.2 or later |
| **vCPU** | 3 minimum, 4 recommended |
| **RAM** | 4 GB minimum, 8 GB recommended |
| **Disk space** | 250 MiB minimum, 500 MiB recommended |
| **Network interface type** | Wi-Fi or LAN |
| **MTU** | 1381 bytes recommended <sup>[1](#user-content-fn-1)</sup> |

## Footnotes

1. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) [↩](#user-content-fnref-1)

## macOS

| **OS version** | Sequoia 15.1+ (15.0.x is not supported), Tahoe 26.0+, Golden Gate 27.0+ |
| --- | --- |
| **Processor** | Intel or M series |
| **CPU cores** | 3 minimum, 4 recommended |
| **RAM** | 8 GB minimum |
| **Disk space** | 1 GiB minimum |
| **Network interface type** | Wi-Fi or LAN |
| **MTU** | 1381 bytes recommended <sup>[1](#user-content-fn-1)</sup> |

All supported Mac models meet the CPU and RAM requirements, so only disk space may be a constraint.

## Footnotes

1. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) [↩](#user-content-fnref-1)

## Linux

| **OS version** | RHEL 9 <sup>[1](#user-content-fn-1)</sup>, RHEL 10, Debian 12, Debian 13, Fedora 43, Fedora 44, Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 26.04 LTS |
| --- | --- |
| **Processor** | AMD64 / x86-64 or ARM64 / AArch64 |
| **vCPU** | 3 minimum, 4 recommended |
| **RAM without a desktop** | 1 GB minimum, 2 GB recommended (for example, Ubuntu Server) |
| **RAM with a desktop** | 4 GB minimum, 8 GB recommended (for example, Ubuntu GNOME) |
| **Disk space** | 250 MiB minimum, 500 MiB recommended |
| **Network interface type** | Wi-Fi or LAN |
| **MTU** | 1381 bytes recommended <sup>[2](#user-content-fn-2)</sup> |

## Footnotes

1. On RHEL 9 and later, enable the [Extra Packages for Enterprise Linux (EPEL) ↗︎](https://docs.fedoraproject.org/en-US/epel/) repository ( `sudo dnf install epel-release`) before installing `cloudflare-warp`. EPEL provides dependencies required by the client UI. [↩](#user-content-fnref-1)
2. Minimum 1281 bytes with [Path MTU Discovery](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/) [↩](#user-content-fnref-2)
