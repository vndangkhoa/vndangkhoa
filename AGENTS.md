# Agent Instructions: vndangkhoa/vndangkhoa

Welcome, AI Agent! This document provides context, conventions, and operational rules for working with this repository.

## Repository Overview
This is the personal GitHub profile repository for **Khoa Vo (`@vndangkhoa`)**.
The `README.md` file in this repository is displayed publicly on Khoa Vo's GitHub user profile (`https://github.com/vndangkhoa`).

## Essential Rules & Invariants

### 1. Dynamic Project Hook (CRITICAL)
- `README.md` contains exact automation boundary markers:
  ```markdown
  <!-- LATEST_REPO:START -->
  ... content ...
  <!-- LATEST_REPO:END -->
  ```
- **Rule**: Never remove, modify, or nest these markers within inline tags that disrupt regular expression matching.
- **Why**: `.github/scripts/update_latest_project.py` executes every 6 hours via GitHub Actions to query the GitHub API for Khoa's latest pushed repository and updates the section between these exact comments using regex replacement.

### 2. Contribution Snake Assets
- `snake.yml` generates two assets to the `output` orphan branch:
  - `dist/snake-dark.svg`
  - `dist/snake-light.svg`
- In `README.md`, both are rendered conditionally using HTML `<picture>` and `(prefers-color-scheme)` media queries via jsDelivr CDN.

### 3. Local Assets & Styling
- `assets/terminal.svg`: A standalone, pure SVG/CSS responsive terminal graphic representing Khoa's homelab. Do not add JavaScript or external fonts that trigger CORS or security sandbox warnings in GitHub Camo proxy.
- `donation.jpg`: Square QR image for VietQR donations, embedded inside the collapsible `<details>` section in `README.md`.

## Automation & Workflows
- `.github/workflows/update-project.yml`: Cron `0 */6 * * *` (Fetch latest pushed non-profile repo, update README.md, commit, and sync to Forgejo).
- `.github/workflows/snake.yml`: Cron `0 0 * * 0` (Generate contribution snake onto `output` branch).

## LLM Context Reference
- See `llms.txt` for clean, token-efficient developer profile metadata.
