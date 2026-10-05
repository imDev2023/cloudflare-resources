---
description: Partnering with Black Forest Labs to bring their latest FLUX.2 model to Workers AI
title: Launching FLUX.2 [dev] on Workers AI
image: https://developers.cloudflare.com/changelog/post/2025-11-25-flux-2-dev-workers-ai/og.png?v=537bcaccbe24de37
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 25, 2025

## Launching FLUX.2 \[dev] on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-25-flux-2-dev-workers-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've partnered with Black Forest Labs (BFL) to bring their latest FLUX.2 \[dev] model to Workers AI! This model excels in generating high-fidelity images with physical world grounding, multi-language support, and digital asset creation. You can also create specific super images with granular controls like JSON prompting.

Read the [BFL blog ↗︎](https://bfl.ai/flux2) to learn more about the model itself. Read our [Cloudflare blog ↗︎](https://blog.cloudflare.com/flux-2-workers-ai) to see the model in action, or try it out yourself on our [multi modal playground ↗︎](https://multi-modal.ai.cloudflare.com/).

Pricing documentation is available on the [model page](https://developers.cloudflare.com/workers-ai/models/flux-2-dev/) or [pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/). Note, we expect to drop pricing in the next few days after iterating on the model performance.

#### Workers AI Platform specifics

The model hosted on Workers AI is able to support up to 4 image inputs (512x512 per input image). Note, this image model is one of the most powerful in the catalog and is expected to be slower than the other image models we currently support. One catch to look out for is that this model takes multipart form data inputs, even if you just have a prompt.

With the REST API, the multipart form data input looks like this:

```bash
curl --request POST \
  --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: multipart/form-data' \
  --form 'prompt=a sunset at the alps' \
  --form steps=25
  --form width=1024
  --form height=1024
```

With the Workers AI binding, you can use it as such:

```javascript
const form = new FormData();
form.append('prompt', 'a sunset with a dog');
form.append('width', '1024');
form.append('height', '1024');

//this dummy request is temporary hack
//we're pushing a change to address this soon
const formRequest = new Request('http://dummy', {
  method: 'POST',
  body: form
});
const formStream = formRequest.body;
const formContentType = formRequest.headers.get('content-type') || 'multipart/form-data';

const resp = await env.AI.run("@cf/black-forest-labs/flux-2-dev", {
  multipart: {
    body: formStream,
    contentType: formContentType
  }
});
```

The parameters you can send to the model are detailed here:

<details>

<summary>JSON Schema for Model</summary>



**Required Parameters**

- <code>prompt</code> (string) - Text description of the image to generate

**Optional Parameters**

- <code>input_image_0</code> (string) - Binary image
- <code>input_image_1</code> (string) - Binary image
- <code>input_image_2</code> (string) - Binary image
- <code>input_image_3</code> (string) - Binary image
- <code>steps</code> (integer) - Number of inference steps. Higher values may improve quality but increase generation time
- <code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely
- <code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920
- <code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920
- <code>seed</code> (integer) - Seed for reproducibility

</details>

````plaintext
## Multi-Reference Images

The FLUX.2 model is great at generating images based on reference images. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generate images. You would use it with the same multipart form data structure, with the input images in binary.

For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.

Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2` for it to work correctly. All input images must be smaller than 512x512.

```bash
curl --request POST \
  --url 'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: multipart/form-data' \
  --form 'prompt=take the subject of image 1 and style it like image 0' \
  --form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \
  --form input_image_1=@/Users/johndoe/Desktop/me.png \
  --form steps=25
  --form width=1024
  --form height=1024
````

Through Workers AI Binding:

```javascript
//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
  const reader = stream.getReader();
  const chunks = [];

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    chunks.push(value);
  }

  return new Blob(chunks, { type: contentType });
}

const image0 = await fetch("http://image-url");
const image1 = await fetch("http://image-url");
const form = new FormData();

const image_blob0 = await streamToBlob(image0.body, "image/png");
const image_blob1 = await streamToBlob(image1.body, "image/png");
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1and style it like image 0')

//this dummy request is temporary hack
//we're pushing a change to address this soon
const formRequest = new Request('http://dummy', {
  method: 'POST',
  body: form
});
const formStream = formRequest.body;
const formContentType = formRequest.headers.get('content-type') || 'multipart/form-data';

const resp = await env.AI.run("@cf/black-forest-labs/flux-2-dev", {
    multipart: {
        body: form,
        contentType: "multipart/form-data"
    }
})
```

#### JSON Prompting

The model supports prompting in JSON to get more granular control over images. You would pass the JSON as the value of the 'prompt' field in the multipart form data. See the JSON schema below on the base parameters you can pass to the model.

<details>

<summary>JSON Prompting Schema</summary>



```json
{
  "type": "object",
  "properties": {
    "scene": {
      "type": "string",
      "description": "Overall scene setting or location"
    },
    "subjects": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": { 
            "type": "string", 
            "description": "Type of subject (e.g., desert nomad, blacksmith, DJ, falcon)" 
          },
          "description": { 
            "type": "string", 
            "description": "Physical attributes, clothing, accessories" 
          },
          "pose": { 
            "type": "string", 
            "description": "Action or stance" 
          },
          "position": { 
            "type": "string",
            "enum": ["foreground", "midground", "background"],
            "description": "Depth placement in scene"
          }
        },
        "required": ["type", "description", "pose", "position"]
      }
    },
    "style": {
      "type": "string",
      "description": "Artistic rendering style (e.g., digital painting, photorealistic, pixel art, noir sci-fi, lifestyle photo, wabi-sabi photo)"
    },
    "color_palette": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 3,
      "maxItems": 3,
      "description": "Exactly 3 main colors for the scene (e.g., ['navy', 'neon yellow', 'magenta'])"
    },
    "lighting": {
      "type": "string",
      "description": "Lighting condition and direction (e.g., fog-filtered sun, moonlight with star glints, dappled sunlight)"
    },
    "mood": {
      "type": "string",
      "description": "Emotional atmosphere (e.g., harsh and determined, playful and modern, peaceful and dreamy)"
    },
    "background": {
      "type": "string",
      "description": "Background environment details"
    },
    "composition": {
      "type": "string",
      "enum": [
        "rule of thirds",
        "circular arrangement",
        "framed by foreground",
        "minimalist negative space",
        "S-curve",
        "vanishing point center",
        "dynamic off-center",
        "leading leads",
        "golden spiral",
        "diagonal energy",
        "strong verticals",
        "triangular arrangement"
      ],
      "description": "Compositional technique"
    },
    "camera": {
      "type": "object",
      "properties": {
        "angle": { 
          "type": "string",
          "enum": ["eye level", "low angle", "slightly low", "bird's-eye", "worm's-eye", "over-the-shoulder", "isometric"],
          "description": "Camera perspective"
        },
        "distance": { 
          "type": "string",
          "enum": ["close-up", "medium close-up", "medium shot", "medium wide", "wide shot", "extreme wide"],
          "description": "Framing distance"
        },
        "focus": { 
          "type": "string",
          "enum": ["deep focus", "macro focus", "selective focus", "sharp on subject", "soft background"],
          "description": "Focus type"
        },
        "lens": { 
          "type": "string",
          "enum": ["14mm", "24mm", "35mm", "50mm", "70mm", "85mm"],
          "description": "Focal length (wide to telephoto)"
        },
        "f-number": { 
          "type": "string", 
          "description": "Aperture (e.g., f/2.8, the smaller the number the more blurry the background)" 
        },
        "ISO": { 
          "type": "number", 
          "description": "Light sensitivity value (comfortable range between 100 & 6400, lower = less sensitivity)" 
        }
      }
    },
    "effects": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Post-processing effects (e.g., 'lens flare small', 'subtle film grain', 'soft bloom', 'god rays', 'chromatic aberration mild')"
    }
  },
  "required": ["scene", "subjects"]
}
```

</details>

#### Other features to try

- The model also supports the most common latin and non-latin character languages
- You can prompt the model with specific hex codes like `#2ECC71`
- Try creating digital assets like landing pages, comic strips, infographics too!

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-25-flux-2-dev-workers-ai/#page","headline":"Launching FLUX.2 [dev] on Workers AI","description":"Partnering with Black Forest Labs to bring their latest FLUX.2 model to Workers AI","url":"https://developers.cloudflare.com/changelog/post/2025-11-25-flux-2-dev-workers-ai/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-25-flux-2-dev-workers-ai/og.png?v=537bcaccbe24de37","dateModified":"2025-11-25","datePublished":"2025-11-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
