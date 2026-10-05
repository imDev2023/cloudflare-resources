---
description: Learn how to use Keyless SSL with Google Cloud HSM.
title: Google Cloud HSM
image: https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/og.png?v=8ffa79efbf13d164
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/ssl/llms.txt  
> Use this file to discover all available pages before exploring further.

# Google Cloud HSM

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This tutorial uses [Google Cloud HSM ↗︎](https://cloud.google.com/kms/docs/hsm) — a FIPS 140-2 Level 3 certified implementation.

---

## Before you start

Make sure that you have:

- Set up your [Google Cloud project ↗︎](https://cloud.google.com/kms/docs/quickstart#before-you-begin)

---

## 1. Create a key ring

To set up the Google Cloud HSM, [create a key ring ↗︎](https://cloud.google.com/kms/docs/hsm#kms-create-key-hsm-web) and indicate its location.

Note:

Only [certain locations ↗︎](https://cloud.google.com/kms/docs/locations#hsm-regions) support Google Cloud HSM.

---

## 2. Create a key

Create a key, including the following information:

| Field | Value |
| --- | --- |
| Key ring | The key ring you created in **Step 2** |
| Protection level | HSM |
| Purpose | Asymmetric Encrypt |

---

## 3. Import the private key

After creating a key ring and key, [import the private key ↗︎](https://cloud.google.com/kms/docs/importing-a-key).

Note:

You need to [convert your key ↗︎](https://cloud.google.com/kms/docs/formatting-keys-for-import#formatting_asymmetric_keys) from a PEM to DER format.

---

## 4. Modify your gokeyless config file and restart the service

Once you’ve imported the key, copy the **Resource name** from the UI. Then, add this value to the `gokeyless` YAML file under `private_key_stores`.

With the config file saved, restart `gokeyless` and verify it started successfully.

```sh
sudo systemctl restart gokeyless.service
sudo systemctl status gokeyless.service -l
```
