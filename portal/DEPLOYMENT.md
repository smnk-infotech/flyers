# Deployment Checklist

## Firebase Project Configuration

### 1. Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **Add project** or select existing project
3. Note your **Project ID**

### 2. Enable Authentication

1. Navigate to **Authentication** → **Sign-in method**
2. Enable **Email/Password**:
   - Click **Email/Password**
   - Toggle **Enable**
   - Save
3. Enable **Google**:
   - Click **Google**
   - Toggle **Enable**
   - Set **Project support email** (your email)
   - Save

### 3. Create Firestore Database

1. Navigate to **Firestore Database**
2. Click **Create database**
3. Select location (choose closest to your users)
4. Start in **Test mode** (we'll deploy rules next)
5. Click **Enable**

### 4. Get Firebase Config

1. Go to **Project Settings** (gear icon) → **General**
2. Scroll to **Your apps** section
3. If no web app exists:
   - Click **Add app** → **Web** (</> icon)
   - Enter app nickname: `Flyers Portal`
   - Check **"Also set up Firebase Hosting"** if deploying to Firebase Hosting
   - Click **Register app**
4. Copy the config object values:
   - `apiKey`
   - `authDomain`
   - `projectId`
   - `storageBucket`
   - `messagingSenderId`
   - `appId`

### 5. Configure Local Environment

Create `portal/.env.local`:

```dotenv
VITE_FIREBASE_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=123456789012
VITE_FIREBASE_APP_ID=1:123456789012:web:abcdef123456
VITE_GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

## Build & Deploy

### Install Firebase CLI

```powershell
npm install -g firebase-tools
```

### Login to Firebase

```powershell
firebase login
```

### Initialize Firebase (if not done)

From repository root:

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers"
firebase init
```

Select:

- **Firestore** (deploy rules)
- **Hosting** (deploy portal)
- Choose your Firebase project
- Accept defaults or:
  - Firestore rules file: `firebase.rules` (or `firestore.rules`)
  - Public directory: `portal/dist`
  - Configure as SPA: **Yes**
  - Don't overwrite `firebase.json` if it exists

### Build Portal

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers\portal"
npm install
npm run build
```

Verify `portal/dist/` folder created with `index.html` and `assets/`.

### Deploy Firestore Rules

From repository root:

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers"
firebase deploy --only firestore:rules
```

### Deploy Hosting

```powershell
firebase deploy --only hosting
```

Note your deployment URL (e.g., `https://your-project.web.app`).

## Post-Deployment Setup

### 1. Authorize Domain for Google Sign-In

1. Go to **Firebase Console** → **Authentication** → **Settings**
2. Scroll to **Authorized domains**
3. Add your hosting domain:
   - Firebase Hosting: `your-project.web.app` and `your-project.firebaseapp.com` (usually auto-added)
   - Custom domain: `yourdomain.com`
4. Click **Add domain**

### 2. Test Authentication

1. Open `https://your-project.web.app/portal/login` (or your custom domain)
2. Click **"Sign in with Google"**
3. Complete Google OAuth flow
4. Should redirect to `/portal/` (dashboard)
5. Verify in Firebase Console → **Authentication** → **Users** that your user appears
6. Verify in Firebase Console → **Firestore Database** → `users` collection that your user document exists with:
   - `uid`: your Firebase auth UID
   - `email`: your Google email
   - `role`: `volunteer` (default)
   - `displayName`: your Google display name
   - `createdAt`: timestamp

### 3. Update User Roles

To grant admin access:

1. Go to **Firestore Database** in Firebase Console
2. Navigate to `users` collection
3. Find your user document (by UID)
4. Edit the `role` field
5. Change from `volunteer` to `admin`
6. Save
7. User must **sign out and sign back in** for role to take effect

Available roles:

- `admin` → Full access to all portal sections
- `hr` → HR dashboard access
- `finance` → Finance dashboard access
- `projects` → Projects dashboard access
- `volunteer` → Volunteers dashboard access (default)

## Connecting Static Site to Portal

The static site pages already have "Corporate Portal" buttons in the header linking to `/portal/login?redirect=/`.

### Verify Routing

Ensure `firebase.json` has the portal rewrite:

```json
{
  "hosting": {
    "public": "portal/dist",
    "rewrites": [
      {
        "source": "/portal/**",
        "destination": "/portal/index.html"
      }
    ]
  }
}
```

Or if serving static site as main:

```json
{
  "hosting": {
    "public": ".",
    "rewrites": [
      {
        "source": "/portal/**",
        "destination": "/portal/dist/index.html"
      }
    ]
  }
}
```

After updating `firebase.json`, redeploy:

```powershell
firebase deploy --only hosting
```

## Troubleshooting

### Google Sign-In fails with "unauthorized domain"

**Solution**: Add your domain to **Firebase Console** → **Authentication** → **Settings** → **Authorized domains**.

### User redirects to 404 after login

**Solution**: Verify `firebase.json` rewrite for `/portal/**` is configured and deployed.

### Role gate shows "Access Denied"

**Solution**: User's Firestore document `users/{uid}.role` must match allowed roles. Update role in Firestore and have user sign out/in.

### Firestore permission denied errors

**Solution**: Deploy Firestore rules with `firebase deploy --only firestore:rules`. Check `firebase.rules` has correct role-based access.

### Build fails with missing env vars

**Solution**: Ensure `portal/.env.local` exists with all required `VITE_FIREBASE_*` variables from Firebase project settings.

## Production Checklist

- [ ] Firebase project created
- [ ] Authentication enabled (Email/Password + Google)
- [ ] Firestore database created
- [ ] Web app registered and config copied
- [ ] `portal/.env.local` configured with Firebase config
- [ ] Portal built successfully (`npm run build`)
- [ ] Firestore rules deployed
- [ ] Hosting deployed
- [ ] Authorized domains configured for Google sign-in
- [ ] Test login flow (Google + Email/Password)
- [ ] Verify user documents created in Firestore
- [ ] Admin role assigned to at least one user
- [ ] Static site "Corporate Portal" links verified
- [ ] Protected routes tested (admin, hr, finance, projects, volunteers)
- [ ] Logout tested

## Quick Deploy Commands

After initial setup, use these for updates:

```powershell
# Build portal
Set-Location "c:\Users\smnk2\Downloads\flyers\portal"
npm run build

# Deploy everything
Set-Location "c:\Users\smnk2\Downloads\flyers"
firebase deploy

# Deploy only hosting (faster)
firebase deploy --only hosting

# Deploy only rules
firebase deploy --only firestore:rules
```
