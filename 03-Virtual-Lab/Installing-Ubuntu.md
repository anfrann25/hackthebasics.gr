
# Installing Ubuntu VM

Σε αυτό το κεφάλαιο θα δημιουργήσεις ένα **Ubuntu Virtual Machine** μέσα στο VirtualBox.

---

##  Βήμα 1: Κατέβασμα Ubuntu ISO

Κατέβασε την τελευταία έκδοση από: https://ubuntu.com/download/desktop

Το αρχείο που θα πάρεις είναι ένα `.iso`.

---

## Βήμα 2: Δημιουργία νέου VM

1. Άνοιξε το VirtualBox
2. Πάτα **New**
3. Συμπλήρωσε:
   - Name: `Ubuntu`
   - Type: `Linux`
   - Version: `Ubuntu (64-bit)`
4. Πάτα **Next**

---

##  Βήμα 3: RAM

Προτείνεται:

- **2048MB (2GB)** ελάχιστο
- **4096MB (4GB)** αν έχεις αρκετή RAM

---

##  Βήμα 4: Virtual Hard Disk

1. **Create a virtual hard disk now**
2. Τύπος: **VDI**
3. Storage: **Dynamically allocated**
4. Μέγεθος: **20GB** ή περισσότερο

---

##  Βήμα 5: Φόρτωση του ISO

1. VM → **Settings**
2. Storage → Empty Disk
3. Εικονίδιο CD → **Choose a disk file**
4. Επίλεξε το Ubuntu ISO

---

##  Βήμα 6: Εκκίνηση και εγκατάσταση

1. Πάτα **Start**
2. Επίλεξε **Install Ubuntu**
3. Ακολούθησε τα βήματα:
   - Language: Greek ή English
   - Keyboard: English (US)
   - Installation type: **Erase disk and install Ubuntu** (μόνο μέσα στο VM)
   - User account: ό,τι θέλεις

Μετά από λίγα λεπτά το Ubuntu VM σου θα είναι έτοιμο.

---

##  Τι ακολουθεί;

Θα δημιουργήσουμε τώρα ένα VM με **Kali Linux**.
