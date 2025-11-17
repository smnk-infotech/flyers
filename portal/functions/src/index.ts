import * as functions from 'firebase-functions'
import * as admin from 'firebase-admin'

admin.initializeApp()

export const ping = functions.https.onCall(async () => {
  return { ok: true, ts: Date.now() }
})

// Placeholder callable for setting user role. Implement admin checks before use.
export const setUserRole = functions.https.onCall(async (data, context) => {
  if (!context.auth) {
    throw new functions.https.HttpsError('unauthenticated', 'Must be authenticated')
  }
  // TODO: Verify caller is admin via Firestore or custom claims before updating.
  const { uid, role } = data || {}
  if (!uid || !role) {
    throw new functions.https.HttpsError('invalid-argument', 'uid and role are required')
  }
  const db = admin.firestore()
  await db.collection('users').doc(uid).set({ role }, { merge: true })
  return { ok: true }
})
