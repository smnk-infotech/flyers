# Email Link (Passwordless) Sign-In Setup

Follow these steps to enable passwordless authentication using secure email links on your custom domain `flyerscharitabletrust.org`.

## 1. Enable Providers in Firebase Console

1. Go to Firebase Console → Authentication → Sign-in method.
2. Under Email/Password:
   - Enable Email/Password (keep this ON for fallback).
   - Enable Email Link (Passwordless).
3. Click Save.
4. (Optional) Ensure your support email is set in Authentication → Settings.

## 2. Authorized Domains (Already Correct)

The following domains are authorized (no action needed):

- `localhost`
- `flyerscharitabletrust-site.firebaseapp.com`
- `flyerscharitabletrust-site.web.app`
- `flyerscharitabletrust.org` (primary custom domain)

If you add a custom domain later, add it here before sending links.

## 3. Link Handling Pages

Two pages were created:

- `login.html` – Collects email and sends sign-in link.
- `finish-signin.html` – Completes sign-in when the user clicks the link.

Both pages live at the site root. Deployment via Firebase Hosting makes them available:

- <https://flyerscharitabletrust.org/login.html>
- <https://flyerscharitabletrust.org/finish-signin.html>

## 4. Action Code Settings (Configured in Code)

The code uses:

```js
const actionCodeSettings = {
  url: 'https://flyerscharitabletrust.org/finish-signin.html',
  handleCodeInApp: true
};
```

Notes:

- `url` must match the deployed `finish-signin.html` page.
- `handleCodeInApp: true` is required for passwordless flow.
- Avoid local URLs in production links.

## 5. Firebase Config Values

Edit `email-link-auth.js` and replace placeholders:

```js
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "flyerscharitabletrust-site.firebaseapp.com",
  projectId: "flyerscharitabletrust-site",
  storageBucket: "flyerscharitabletrust-site.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};
```

Copy values from Firebase Console → Project Settings.

## 6. Sending the Email Link

Workflow in `login.html`:

1. User enters email.
2. `sendEmailLink(email)` calls `sendSignInLinkToEmail`.
3. Email stored in `localStorage`.
4. User clicks link in email → Opens `finish-signin.html`.

## 7. Completing Sign-In

On `finish-signin.html`:

1. Detects if URL is a valid sign-in link.
2. Tries stored email from `localStorage`.
3. If missing (different device), prompts user to enter email.
4. Calls `signInWithEmailLink`.
5. On success: shows portal link and user email.

## 8. Redirect After Success (Optional Enhancement)

To redirect automatically to the portal dashboard, modify `finish-signin.html` inside success blocks:

```js
window.location.href = '/portal/';
```

Or preserve deep links by appending a query parameter when sending links:

```js
const actionCodeSettings = {
  url: 'https://flyerscharitabletrust.org/finish-signin.html?redirect=%2Fportal%2Fprojects',
  handleCodeInApp: true
};
```

Then in `finish-signin.html` read:

```js
const params = new URLSearchParams(window.location.search);
const redirect = params.get('redirect') || '/portal/';
// after successful sign-in
window.location.href = redirect;
```

## 9. Testing Locally

You can test with localhost after enabling providers:

1. Serve static files:

```powershell
python -m http.server 8000
```

2. Open: `http://localhost:8000/login.html`
3. Send link using a real email you control.
4. Click email link (may open in your default browser). If it points to production domain, test in production instead.

## 10. Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Link opens but fails | Wrong `url` domain | Ensure `actionCodeSettings.url` matches deployed page |
| Prompt for email every time | Different device or cleared storage | Re-enter email; flow still works |
| "Invalid or expired" | Link reused or expired | Generate a new email link |
| Stuck on loading | Script error | Check browser console for errors |
| Redirect loop | Misplaced redirect code | Add redirect only after successful sign-in |

## 11. Security Notes

- Email link validity is controlled by Firebase; links expire automatically.
- Never embed secrets; Firebase config is safe to expose.
- Encourage users not to forward sign-in links.

## 12. Deployment Steps Recap

1. Enable Email Link in Firebase Console.
2. Add/confirm authorized domain (`flyerscharitabletrust.org`).
3. Fill Firebase config in `email-link-auth.js`.
4. Deploy hosting (`firebase deploy`).
5. Test `login.html` → email → `finish-signin.html`.
6. (Optional) Add auto-redirect to portal after success.

## 13. Next Enhancements (Optional)

- Add spinner/visual progress feedback.
- Display support contact if failure persists.
- Log analytics events (link sent / link completed).
- Consolidate styles by reusing global site CSS.

---
**Email Link Sign-In is now implemented.** You can proceed to configure and deploy.
