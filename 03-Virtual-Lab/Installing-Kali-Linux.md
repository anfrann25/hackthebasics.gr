# Installing Kali Linux VM

Το **Kali Linux** είναι η πιο δημοφιλής διανομή για Cybersecurity, Penetration Testing και Ethical Hacking.

Σε αυτό το κεφάλαιο θα το εγκαταστήσεις στο VirtualBox.

---

## 📥 Βήμα 1: Κατέβασμα Kali ISO

Κατέβασε την τελευταία έκδοση από:

👉 https://www.kali.org/get-kali/#kali-installer-images

Επίλεξε **Installer ISO**.

---

## 🆕 Βήμα 2: Δημιουργία νέου VM

1. VirtualBox → **New**
2. Name: `Kali Linux`
3. Type: `Linux`
4. Version: **Debian (64-bit)**  
   (Το Kali βασίζεται στο Debian)

---

## 🧠 Βήμα 3: RAM

Προτείνεται:

- **2048MB–4096MB** ανάλογα με το σύστημά σου

---

## 💾 Βήμα 4: Virtual Hard Disk

- Create a virtual hard disk now  
- VDI  
- Dynamically allocated  
- **30GB** ή περισσότερο

---

## 📀 Βήμα 5: Φόρτωση ISO

1. Settings → Storage
2. Empty Disk → Choose a disk file
3. Επίλεξε το Kali ISO

---

## ▶️ Βήμα 6: Εγκατάσταση

1. Start
2. **Graphical Install**
3. Ακολούθησε τα βήματα:
   - Language: English
   - Keyboard: English (US)
   - Partitioning: **Guided – use entire disk**
   - User account: δημιούργησε έναν απλό χρήστη
   - Desktop Environment: **XFCE** (ελαφρύ και γρήγορο)

Μετά την εγκατάσταση, κάνε reboot.

---

## 🎉 Τι ακολουθεί;

Θα μάθεις πώς να χρησιμοποιείς **Snapshots** για να προστατεύεις το εργαστήριό σου.
