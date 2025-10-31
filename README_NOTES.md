# Project notes

This repo includes a few helper scripts and CI config to streamline deployment and fix a known CSS parsing issue from the WordPress export.

## Helpers

- Deploy helper without requiring a global Firebase CLI install:
  
  ```powershell
  # Tries global `firebase`, then `npx firebase-tools`, then `npm exec --package firebase-tools`
  .\deploy.ps1 -ProjectId <PROJECT_ID>
  ```

- Fix CSS variable parsing issue in inline styles (runs once):
  
  ```powershell
  # Replaces background-color:(--ast-global-dark-bg-style) with var(...) across all HTML files
  .\scripts\fix-css.ps1
  # Preview only:
  .\scripts\fix-css.ps1 -WhatIf
  ```

## CI

- A minimal workflow is provided at `.github/workflows/deploy-pages.yml` to ensure the YAML file is valid and the repo structure is checked on pushes.
