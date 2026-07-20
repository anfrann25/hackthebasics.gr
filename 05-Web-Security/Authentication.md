# Authentication

Οι περισσότερες Web Applications απαιτούν Login.

Για να αναγνωρίζει έναν χρήστη μετά το Login, ο Server χρησιμοποιεί Cookies και Sessions.

---

# Cookies

Τα Cookies είναι μικρά δεδομένα που αποθηκεύονται στον Browser.

Παράδειγμα:

```http
Cookie: session=7f8da93...
```

Συνήθως περιέχουν:

- Session ID
- User Preferences
- Authentication Information

---

# Sessions

Μετά το Login, ο Server δημιουργεί ένα Session.

```text
User Login
     │
     ▼
Web Server
     │
Creates Session
     │
Session ID
     │
Cookie
     │
Browser
```

Σε κάθε επόμενο Request, ο Browser στέλνει αυτό το Cookie στον Server.

Έτσι ο Server γνωρίζει ποιος είναι ο χρήστης.

---

# Authentication vs Authorization

## Authentication

Απαντά στην ερώτηση:

> Ποιος είσαι;

Παράδειγμα:

- Login
- Username
- Password

---

## Authorization

Απαντά στην ερώτηση:

> Τι επιτρέπεται να κάνεις;

Παράδειγμα:

Ένας απλός χρήστης δεν μπορεί να αποκτήσει πρόσβαση στο Admin Panel.

---

# Developer Tools

Κάθε σύγχρονος Browser διαθέτει Developer Tools.

Άνοιγμα:

```text
F12
```

Τα σημαντικότερα Tabs είναι:

- Elements
- Network
- Storage
- Console

Το **Network Tab** εμφανίζει όλα τα HTTP Requests και Responses και αποτελεί βασικό εργαλείο για κάθε Web Pentester.

---

# Common Web Vulnerabilities

Αφού κατανοήσεις τις βασικές έννοιες, μπορείς να μελετήσεις επιθέσεις όπως:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Directory Traversal
- File Upload Vulnerabilities
- Authentication Bypass
- IDOR
- CSRF

Όλες βασίζονται στις έννοιες που έμαθες σε αυτό το κεφάλαιο.

---

# Τι πρέπει να θυμάσαι

- Τα Cookies αποθηκεύονται στον Browser.
- Τα Sessions δημιουργούνται στον Server.
- Authentication σημαίνει "Ποιος είσαι;".
- Authorization σημαίνει "Τι επιτρέπεται να κάνεις;".