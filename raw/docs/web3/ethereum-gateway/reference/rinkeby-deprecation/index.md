---
description: Deprecation notice for the Rinkeby test network.
title: Rinkeby deprecation
image: https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/og.png?v=e3ac60cec79e29e7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/web3/llms.txt  
> Use this file to discover all available pages before exploring further.

# Rinkeby deprecation

Last updated May 5, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/web3/ethereum-gateway/reference/rinkeby-deprecation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Though Cloudflare's Ethereum Gateway launched with support for the Rinkeby testnet, Rinkeby did not run through [The Merge ↗︎](https://ethereum.org/en/upgrades/merge/) and - as a result - will no longer be a reliable staging environment for mainnet.

Cloudflare will be deprecating support for Rinkeby on January 30, 2023.

## Migration

To avoid any issues with your Web3 development or debugging, you should switch over to the [Sepolia testnet](https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/), which is fully supported with your Ethereum Gateway.

To migrate, you should update the endpoints you use when [reading from or writing to](https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/) the Ethereum network.

For example, you might have been using the previous endpoints to interact with your Ethereum Gateway.

*Previous curlbash*

```bash
curl https://web3-trial.cloudflare-eth.com/v1/rinkeby \
--header 'Content-Type: application/json' \
--data '{
  "jsonrpc": "2.0",
  "method": "eth_getBlockByNumber",
  "params": ["0x2244", true],
  "id": 1
}'
```

*Previous JS Fetch APIjs*

```js
await fetch(
  new Request('https://web3-trial.cloudflare-eth.com/v1/rinkeby', {
    method: 'POST',
    body: JSON.stringify({
      jsonrpc: '2.0',
      method: 'eth_getBlockByNumber',
      params: ['0x2244', true],
      id: 1,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })
).then(resp => {
  return resp.json();
});
```

To migrate away from Rinkeby, change the end of your endpoint to use another testnet.

*New curlbash*

```bash
curl https://web3-trial.cloudflare-eth.com/v1/sepolia \
--header 'Content-Type: application/json' \
--data '{
  "jsonrpc": "2.0",
  "method": "eth_getBlockByNumber",
  "params": ["0x2244", true],
  "id": 1
}'
```

*New JS Fetch APIjs*

```js
await fetch(
  new Request('https://web3-trial.cloudflare-eth.com/v1/sepolia', {
    method: 'POST',
    body: JSON.stringify({
      jsonrpc: '2.0',
      method: 'eth_getBlockByNumber',
      params: ['0x2244', true],
      id: 1,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })
).then(resp => {
  return resp.json();
});
```
