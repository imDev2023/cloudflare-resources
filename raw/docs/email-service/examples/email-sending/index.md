---
description: Advanced patterns and examples for sending transactional emails with Email Service.
title: Email sending
image: https://developers.cloudflare.com/email-service/examples/email-sending/og.png?v=c52f52e1d819eca1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/email-service/llms.txt  
> Use this file to discover all available pages before exploring further.

# Email sending

Last updated Jun 9, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/email-service/examples/email-sending/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Advanced patterns and examples for sending emails with Cloudflare Email Service. Most examples use the [Workers binding](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/); the same [`EmailMessageBuilder`](https://developers.cloudflare.com/email-service/api/send-emails/workers-api/#send-method) fields (`to`, `from`, `subject`, `html`, `text`, `cc`, `bcc`, `replyTo`, `attachments`, `headers`) apply to the [REST API](https://developers.cloudflare.com/email-service/api/send-emails/rest-api/) as JSON in your HTTP request body. The [Send email over SMTP](https://developers.cloudflare.com/email-service/examples/email-sending/smtp/) example covers sending over SMTP from several languages and clients.

- [Specify recipients](https://developers.cloudflare.com/email-service/examples/email-sending/recipients/)
- [User signup flow](https://developers.cloudflare.com/email-service/examples/email-sending/signup-flow/)
- [Magic link authentication](https://developers.cloudflare.com/email-service/examples/email-sending/magic-link/)
- [Email attachments](https://developers.cloudflare.com/email-service/examples/email-sending/email-attachments/)
- [Send email over SMTP](https://developers.cloudflare.com/email-service/examples/email-sending/smtp/)
- [Sync recipient records](https://developers.cloudflare.com/email-service/examples/email-sending/sync-recipient-records/)
