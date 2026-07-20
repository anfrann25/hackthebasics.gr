# Web Basics

Το μεγαλύτερο μέρος των εφαρμογών που χρησιμοποιούμε καθημερινά είναι web applications.

Facebook, Gmail, Instagram, ηλεκτρονικές τράπεζες και e-shops λειτουργούν μέσω του Web.

Για αυτόν τον λόγο, η ασφάλεια των web εφαρμογών αποτελεί έναν από τους σημαντικότερους τομείς του Cybersecurity.

Σε αυτό το κεφάλαιο θα μάθεις πώς λειτουργεί το Web και πώς σκέφτεται ένας Web Pentester.

---

# Πώς σκέφτεται το Web

Ένας browser δεν επικοινωνεί απευθείας με μία βάση δεδομένων.

Η επικοινωνία γίνεται πάντα μέσω ενός Web Server.

```text
Browser
    │
HTTP Request
    │
    ▼
Web Server
    │
Application
    │
Database
```

Ο Browser στέλνει ένα **HTTP Request**.

Ο Server επεξεργάζεται το Request.

Ο Server επιστρέφει ένα **HTTP Response**.

Οι περισσότερες Web Vulnerabilities βασίζονται στην κατανόηση αυτής της επικοινωνίας.

---

# Client vs Server

## Client

Ο Client είναι η συσκευή του χρήστη.

Παραδείγματα:

- Chrome
- Firefox
- Edge
- Safari

Ο Client στέλνει Requests και εμφανίζει το αποτέλεσμα στον χρήστη.

---

## Server

Ο Server φιλοξενεί την εφαρμογή.

Παραδείγματα:

- Apache
- Nginx
- IIS

Ο Server επεξεργάζεται τα Requests και επιστρέφει Responses.

---

# HTML

Η HTML δημιουργεί τη δομή μιας ιστοσελίδας.

Παράδειγμα:

```html
<h1>Hello World</h1>

<form>

<input>

<button>Login</button>
```

Η HTML περιγράφει τι θα εμφανιστεί στον Browser.

---

# JavaScript

Η JavaScript εκτελείται στον Browser.

Χρησιμοποιείται για:

- Dynamic Content
- Forms
- Buttons
- API Calls

Η JavaScript βελτιώνει την εμπειρία του χρήστη, όμως δεν πρέπει ποτέ να χρησιμοποιείται ως μηχανισμός ασφαλείας, καθώς ο κώδικας μπορεί να προβληθεί και να τροποποιηθεί από οποιονδήποτε.

---

# Τι πρέπει να θυμάσαι

- Ο Browser στέλνει Requests.
- Ο Server επιστρέφει Responses.
- Οι περισσότερες επιθέσεις εκμεταλλεύονται την επικοινωνία μεταξύ Client και Server.