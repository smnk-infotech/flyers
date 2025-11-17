// Firebase Email Link Auth helper
// Fill in your Firebase config values. These are public (not secrets).
// You can copy them from portal/.env.local or Firebase Console > Project Settings.

const firebaseConfig = {
  apiKey: "AIzaSyAnT_fUHSa1alzzA9FORRl6VpW3tkQ0EUA",
  authDomain: "flyerscharitabletrust-site.firebaseapp.com",
  projectId: "flyerscharitabletrust-site",
  storageBucket: "flyerscharitabletrust-site.firebasestorage.app",
  messagingSenderId: "129609658335",
  appId: "1:129609658335:web:46d4db7392a392ebdf9e6a"
};

import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.0/firebase-app.js";
import { getAuth, sendSignInLinkToEmail, isSignInWithEmailLink, signInWithEmailLink } from "https://www.gstatic.com/firebasejs/11.0.0/firebase-auth.js";

// Initialize (singleton pattern safeguard)
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);

// Action Code Settings for Email Link Sign-In
// The URL must be an authorized domain that hosts finish-signin.html
export const actionCodeSettings = {
  url: 'https://flyerscharitabletrust.org/finish-signin.html',
  handleCodeInApp: true
  // dynamicLinkDomain: 'YOUR_DYNAMIC_LINK_DOMAIN' // Optional if using Firebase Dynamic Links
};

export async function sendEmailLink(email) {
  await sendSignInLinkToEmail(auth, email, actionCodeSettings);
  // Store the email locally so we can finish sign-in without asking again
  window.localStorage.setItem('emailForSignIn', email);
}

export async function completeEmailLinkSignIn() {
  if (isSignInWithEmailLink(auth, window.location.href)) {
    let email = window.localStorage.getItem('emailForSignIn');
    if (!email) {
      // Ask user if email not stored (e.g., opened on different device)
      email = window.prompt('Please enter your email to complete sign-in');
    }
    const result = await signInWithEmailLink(auth, email, window.location.href);
    // Clear stored email
    window.localStorage.removeItem('emailForSignIn');
    return result.user;
  }
  return null;
}
