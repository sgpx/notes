# rate limits and usage

available in response headers when using the HTTP client

```
< cache-control: no-cache, must-revalidate
< openai-model: gpt-3.5-turbo-0125
< openai-organization: my-company-llc
< openai-processing-ms: 776
< openai-version: 2020-10-01
< strict-transport-security: max-age=15724800; includeSubDomains
< x-ratelimit-limit-requests: 200
< x-ratelimit-limit-tokens: 40000
< x-ratelimit-remaining-requests: 0
< x-ratelimit-remaining-tokens: 39977
< x-ratelimit-reset-requests: 23h55m16.126s
< x-ratelimit-reset-tokens: 34ms
< x-request-id: req_XXXXXXXXXXXX
```
