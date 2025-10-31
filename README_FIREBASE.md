# Deploying this static site to Firebase Hosting

This guide shows how to host the static export in this folder on Firebase Hosting using a new Google/Firebase project. I cannot create the Firebase account or project for you — follow the steps below on your machine.

Prerequisites
- A Google account
- Node.js + npm installed (for the Firebase CLI). If you don't want npm, you can install the Firebase CLI via the standalone installer — see Firebase docs.

Quick PowerShell commands (copy & paste into a PowerShell window in this folder)

1) Install Firebase CLI (if not already installed)

```powershell
# Install globally (requires admin rights for global install)
npm install -g firebase-tools
# If you prefer a local install: npm install firebase-tools
```

2) Log in to Firebase

```powershell
firebase login
```

3) Create a Firebase project

Open the Firebase Console in your browser: https://console.firebase.google.com/ and create a new project. Note the Project ID (it looks like: my-project-12345). You can also create a project via the Firebase CLI but using the console is simple for a new account.

4) Set the project locally (replace <PROJECT_ID> with the project id you created)

```powershell
# Set the default project in this folder
firebase use --add <PROJECT_ID>
```

5) Deploy to Firebase Hosting

```powershell
# Deploy hosting only
firebase deploy --only hosting
```

Notes & recommended settings
- The included `firebase.json` sets `public` to the repository root ("."). This works for single-page exports where `index.html` is at project root. If you prefer to use a dedicated `public/` folder, move the contents into `public/` and update `firebase.json` accordingly.
- The `rewrites` entry in `firebase.json` will serve `index.html` for all routes (common for SPAs). If your site is purely static multi-page HTML that relies on normal 404s, you can remove or change the rewrite.
- For stronger protection against framing/hotlinking, configure `Content-Security-Policy` / `X-Frame-Options` headers at the CDN or by using Firebase Hosting headers in `firebase.json`. Example headers snippet (add to `firebase.json` > hosting > headers):

```json
"headers": [
  {
    "source": "**/*.@(html|htm)",
    "headers": [
      { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
      { "key": "Content-Security-Policy", "value": "frame-ancestors 'self'" }
    ]
  }
]
```

- Firebase Hosting has a free tier with a usage quota. If you expect high traffic, review Firebase billing and limits.

Troubleshooting
- If `firebase` is not recognized after `npm install -g firebase-tools`, you may need to reopen PowerShell or add npm global bin to your PATH.
- To change the project later: `firebase use <PROJECT_ID>` or `firebase use --add` to add a new alias.

Security reminder
- Do NOT commit private server-side keys or service-account JSON files into this repo. The static export should only contain public client assets.

If you want, I can also add optional hosting headers to `firebase.json` (frame-ancestors, CSP) and update `firebase.json` accordingly. Tell me whether you want `X-Frame-Options: DENY`, `SAMEORIGIN`, or a CSP `frame-ancestors` allowlist.

