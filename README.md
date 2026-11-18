# n8n Automation Portfolio

Real-world automation workflows built with **n8n**, **Python/JavaScript** and **LLM APIs**. Each project solves a problem I have in my own business, and ships with documentation, error handling and setup instructions.

## Projects

| # | Project | What it does | Stack |
| --- | --- | --- | --- |
| 01 | [Daily Shop Digest](flows/01-daily-shop-digest) | Reads Etsy shop stats daily, stores the history in Google Sheets, compares with the previous day and sends an AI-written summary to Telegram | n8n · Etsy API · Claude API · Google Sheets · Telegram |
| 00 | [Error Alert](flows/00-error-alert) | Reusable error workflow that notifies me on Telegram with the failing node and error message | n8n · Telegram |

More workflows will be added here.

## How the projects are built

- **Real data, real problems:** every workflow runs against my own Etsy shop.
- **Reliable by design:** idempotent writes, retries, fallbacks and an error-alert workflow.
- **Secrets never in the repo:** credentials live in n8n and a git-ignored `.env`. Workflows are exported with placeholders.
- **Documented:** each project has a README with a diagram, design decisions and setup steps.

## About me

Physics student at the Universidad de La Laguna, building an online business of digital products and automating it with n8n, Python and LLMs. Looking for a junior role in AI and automation.

- [LinkedIn](https://www.linkedin.com/in/jareedss)
- [Contact] jaredss268@gmail.com
