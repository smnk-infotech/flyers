# Flyers Corporate NGO Portal

React + TypeScript + Vite + Tailwind + Firebase (Auth, Firestore, Storage).

## Quick Start

### 1. Install dependencies

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers\portal"
npm install
```

### 2. Firebase Project Setup

1. **Create a Firebase project** at [console.firebase.google.com](https://console.firebase.google.com/)
2. **Enable Authentication**:
   - Go to **Authentication** → **Sign-in method**
   - Enable **Email/Password**
   - Enable **Google** (add support email and save)
3. **Create Firestore Database**:
   - Go to **Firestore Database** → **Create Database**
   - Start in **test mode** (we'll deploy rules later)
4. **Register Web App**:
   - Go to **Project Settings** → **Your apps** → **Add app** → **Web**
   - Copy the Firebase config values
5. **Get Firebase Config**:
   - From Project Settings → Your apps, copy:
     - `apiKey`
     - `authDomain`
     - `projectId`
     - `storageBucket`
     - `messagingSenderId`
     - `appId`

### 3. Configure Environment Variables

Copy `.env.example` to `.env.local` and fill in your Firebase config:

```powershell
Copy-Item .env.example .env.local
```

Edit `.env.local`:

```dotenv
VITE_FIREBASE_API_KEY=your_api_key_here
VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=123456789
VITE_FIREBASE_APP_ID=1:123456789:web:abcdef
VITE_GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

### 4. Run the app

```powershell
npm run dev
```

It serves at `http://localhost:5173/portal` (basename set to `/portal`).

## Build & Preview

```powershell
npm run build
npm run preview
```

## Deploy (Firebase Hosting)

### Prerequisites

Step 1: Install Firebase CLI:

```powershell
npm install -g firebase-tools
```

Step 2: Login to Firebase:

```powershell
firebase login
```

Step 3: Initialize Firebase (from repo root if not already done):

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers"
firebase init
```

- Select **Hosting** and **Firestore** (and optionally Functions)
- Choose your Firebase project
- For hosting, set public directory to `portal/dist` or configure rewrites in `firebase.json`
- Configure as single-page app: **Yes**
- Don't overwrite existing `firebase.json`

### Deploy Steps

#### 1. Build the portal

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers\portal"
npm run build
```

#### 2. Deploy Firestore rules (first time)

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers"
firebase deploy --only firestore:rules
```

#### 3. Deploy hosting

```powershell
firebase deploy --only hosting
```

### Production Environment Variables

For production, set environment variables in your hosting provider or CI/CD:

- **Firebase Hosting**: Environment variables are baked into the build at build-time (Vite inlines them). Ensure you build with production `.env.local` or CI secrets.
- **GitHub Actions / CI**: Add Firebase config as repository secrets and inject them during build.

### Verify Deployment

1. Open your Firebase Hosting URL (e.g., `https://your-project.web.app/portal/login`)
2. Test Google sign-in:
   - Click "Sign in with Google"
   - Complete Google OAuth flow
   - Should redirect to portal dashboard (`/portal/`)
3. Check Firestore:
   - Go to Firebase Console → Firestore Database
   - Verify `users/{uid}` document was created with `role: "volunteer"`

### Post-Deploy: Authorize Domain

If Google sign-in fails with "unauthorized domain":

1. Go to **Firebase Console** → **Authentication** → **Settings** → **Authorized domains**
2. Add your production domain (e.g., `your-project.web.app` or custom domain)
3. Retry sign-in

## Cloud Functions (Optional)

Scaffolded under `portal/functions`.

```powershell
Set-Location "c:\Users\smnk2\Downloads\flyers\portal\functions"
npm install
npm run build
```

Deploy with Firebase CLI (from repo root):

```powershell
firebase deploy --only functions
```

## Firebase Rules

Deploy rules (optional):

```powershell
# Using Firebase CLI if initialized
firebase deploy --only firestore:rules
```

## Notes

- First-time registration creates a user doc in `users/{uid}` with role `volunteer`.
- Change a user's role by editing `users/{uid}.role` to one of: `admin`, `hr`, `finance`, `projects`, `volunteer`.
- Routes are role-gated; only Admin can access `/admin`, etc.
