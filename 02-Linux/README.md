# Linux Fundamentals

Το Linux είναι το βασικό λειτουργικό σύστημα που χρησιμοποιείται σε servers, cybersecurity εργαλεία και penetration testing περιβάλλοντα.

Σε αυτό το κεφάλαιο θα μάθεις όχι μόνο εντολές, αλλά και πώς “σκέφτεται” το Linux.

---

# Πώς σκέφτεται το Linux

Στο Linux τα πάντα είναι αρχεία:

- Φάκελοι = αρχεία  
- Συσκευές = αρχεία  
- Processes = αρχεία  
- Configuration = αρχεία  

Αυτό είναι πολύ σημαντικό για το Cybersecurity.

---

#  File System Structure

Βασικοί φάκελοι στο Linux:

```text
/
├── home   → χρήστες
├── etc    → ρυθμίσεις συστήματος
├── var    → logs & services
├── bin    → βασικές εντολές
├── tmp    → προσωρινά αρχεία
```

---

#  Navigation

## pwd (Print Working Directory)

### Τι κάνει
Δείχνει σε ποιον φάκελο βρίσκεσαι αυτή τη στιγμή.

### Παράδειγμα
```bash
pwd
```

### Έξοδος
```text
/home/student
```

---

## ls (List)

### Τι κάνει
Εμφανίζει αρχεία και φακέλους.

### Παράδειγμα
```bash
ls
```

### Με λεπτομέρειες
```bash
ls -la
```

- `-l` → λεπτομέρειες
- `-a` → κρυφά αρχεία

---

## cd (Change Directory)

### Τι κάνει
Μετακινείσαι σε άλλο φάκελο.

### Παράδειγμα
```bash
cd /home
```

### Πλοήγηση
```bash
cd ..   # πίσω
cd ~    # home
```

---

#  File Operations

## touch

Δημιουργεί νέο αρχείο:

```bash
touch notes.txt
```

---

## mkdir

Δημιουργεί φάκελο:

```bash
mkdir lab
```

---

## cat

Εμφανίζει περιεχόμενο αρχείου:

```bash
cat notes.txt
```

---

## cp (Copy)

Αντιγραφή αρχείων:

```bash
cp file1.txt file2.txt
```

---

## mv (Move / Rename)

Μετακίνηση ή μετονομασία:

```bash
mv file.txt /home/user/
mv old.txt new.txt
```

---

## rm (Remove)

Διαγραφή αρχείων:

⚠️ Δεν υπάρχει recycle bin

```bash
rm file.txt
rm -r folder/
```

---

#  Searching

## find

Βρίσκει αρχεία:

```bash
find /home -name "flag.txt"
```

---

## grep

Ψάχνει μέσα σε αρχεία:

```bash
grep "flag" file.txt
```

---

#  Permissions

## chmod

Αλλάζει δικαιώματα αρχείων:

```bash
chmod +x script.sh
./script.sh
```

---

#  Linux Challenges (CTF Mode)

Ο φάκελος `linux_challenges` δεν είναι απλά ασκήσεις.

Είναι ένα μικρό **CTF (Capture The Flag) environment** που έχει σχεδιαστεί για να σε βοηθήσει να μάθεις Linux μέσα από πραγματικά σενάρια.

---

#  Τι είναι αυτό το CTF;

Κάθε επίπεδο (`lvl1`, `lvl2`, κτλ.) περιέχει ένα μικρό challenge.

Ο στόχος σου είναι να βρεις το **flag** χρησιμοποιώντας Linux εντολές.


--- 

#  Δομή

Κάθε level είναι ένα μικρό puzzle:

```
linux_challenges/
├── lvl1
├── lvl2
├── lvl3
├── lvl4
├── lvl5
```
---

##  Installation

`Στον κεντρικό φάκελο του repository κάνε:`

```bash
chmod +x setup.sh
./setup.sh
```
`Για να κάνεις απεγκατάσταση κάνε:`

```bash
chmod +x uninstall.sh
./uninstall.sh
```
---
