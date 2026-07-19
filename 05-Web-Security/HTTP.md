# HTTP Fundamentals

Το HTTP (HyperText Transfer Protocol) είναι το πρωτόκολλο επικοινωνίας του Web.

Κάθε φορά που ανοίγεις μια ιστοσελίδα, ο Browser στέλνει ένα HTTP Request και ο Server επιστρέφει ένα HTTP Response.

---

# HTTP Request

Παράδειγμα:

```http
GET /login HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
```

---

# HTTP Response

Παράδειγμα:

```http
HTTP/1.1 200 OK

<html>
...
</html>
```

---

# HTTP Methods

## GET

Χρησιμοποιείται για ανάκτηση δεδομένων.

```http
GET /products
```

---

## POST

Χρησιμοποιείται για αποστολή δεδομένων.

```http
POST /login
```

---

## PUT

Χρησιμοποιείται για ενημέρωση δεδομένων.

```http
PUT /users/5
```

---

## DELETE

Χρησιμοποιείται για διαγραφή δεδομένων.

```http
DELETE /users/5
```

---

# Status Codes

## 200 OK

Το Request ολοκληρώθηκε επιτυχώς.

---

## 301 / 302

Redirect.

---

## 403 Forbidden

Δεν επιτρέπεται η πρόσβαση.

---

## 404 Not Found

Η σελίδα δεν υπάρχει.

---

## 500 Internal Server Error

Σφάλμα στον Server.

---

# URLs

Παράδειγμα:

```text
https://example.com/login?id=5
```

Ανάλυση:

```text
https://        → Protocol
example.com     → Domain
/login          → Path
?id=5           → Parameter
```

Οι Parameters αποτελούν πολύ συχνό σημείο εισόδου για επιθέσεις.

---

# Headers

Παράδειγμα:

```http
GET / HTTP/1.1

Host: example.com
User-Agent: Mozilla
Cookie: session=abc123
```

Οι Headers μεταφέρουν πληροφορίες σχετικά με το Request και τον Client.

---

# HTTPS

Το HTTPS είναι η ασφαλής έκδοση του HTTP.

Χρησιμοποιεί TLS Encryption ώστε τα δεδομένα να προστατεύονται κατά τη μεταφορά.

```text
HTTP  → Χωρίς Κρυπτογράφηση

HTTPS → Με Κρυπτογράφηση (TLS)
```

---

# Τι πρέπει να θυμάσαι

- Το HTTP χρησιμοποιείται για την επικοινωνία Browser και Server.
- Κάθε Request περιέχει Method, URL και Headers.
- Κάθε Response περιέχει Status Code και δεδομένα.