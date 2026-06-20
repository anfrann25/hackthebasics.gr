# Linux Fundamentals

Το Linux είναι το βασικό λειτουργικό σύστημα που χρησιμοποιείται σε servers, cybersecurity εργαλεία και penetration testing περιβάλλοντα.

Σε αυτό το κεφάλαιο θα μάθεις όχι μόνο εντολές, αλλά και πώς σκέφτεται το Linux.

---

# 🧠 Πώς σκέφτεται το Linux

Στο Linux τα πάντα είναι αρχείο:

* Φάκελοι = αρχεία
* Συσκευές = αρχεία
* Processes = αρχεία
* Configuration = αρχεία

Αυτό είναι πολύ σημαντικό για το Cybersecurity.

---

# 📁 File System Structure

Βασικοί φάκελοι:

```text id="fs1"
/
├── home      → χρήστες
├── etc       → ρυθμίσεις συστήματος
├── var       → logs & services
├── bin       → βασικές εντολές
├── tmp       → προσωρινά αρχεία
```

---

# 🧭 Navigation

## pwd

Δείχνει πού βρίσκεσαι:

```bash id="n1"
pwd
```

## ls

Δείχνει αρχεία:

```bash id="n2"
ls
ls -la
```

## cd

Μετακίνηση:

```bash id="n3"
cd /home
cd ..
cd ~
```

---

# 📂 File Operations

## Δημιουργία

```bash id="n4"
touch file.txt
mkdir lab
```

## Αντιγραφή

```bash id="n5"
cp file1.txt file2.txt
```

## Μετακίνηση / Μετονομασία

```bash id="n6"
mv file.txt /home/user/
mv old.txt new.txt
```

## Διαγραφή

```bash id="n7"
rm file.txt
rm -r folder/
```

---

# 📖 Reading Files

## cat

```bash id="n8"
cat file.txt
```

## less

Για μεγάλα αρχεία:

```bash id="n9"
less file.txt
```

## head / tail

```bash id="n10"
head file.txt
tail file.txt
tail -f logs.txt
```

---

# 🔎 Searching

## find

Βρίσκει αρχεία:

```bash id="n11"
find /home -name "flag.txt"
```

## grep

Ψάχνει μέσα σε αρχεία:

```bash id="n12"
grep "flag" file.txt
```

---

# 👤 Users & Permissions

## whoami

```bash id="n13"
whoami
```

## id

```bash id="n14"
id
```

## permissions

```text id="perm"
r = read
w = write
x = execute
```

## chmod

```bash id="n15"
chmod 777 file.txt
chmod +x script.sh
```

---

# ⚙️ Processes

## ps

```bash id="n16"
ps aux
```

## top

```bash id="n17"
top
```

## kill

```bash id="n18"
kill -9 PID
```

---

# 🌐 Networking Basics

## ip

```bash id="n19"
ip a
```

## ping

```bash id="n20"
ping google.com
```

## ports

```bash id="n21"
ss -tulpn
```

---

# 📦 Archives

## tar

```bash id="n22"
tar -cvf file.tar folder/
tar -xvf file.tar
```

## gzip

```bash id="n23"
gzip file.txt
gunzip file.txt.gz
```

# 🎯 Τι πρέπει να κρατήσεις

* Το Linux είναι file-based system
* Όλες οι ενέργειες είναι αρχεία
* Οι βασικές εντολές είναι το 80% της δουλειάς στο Cybersecurity
* Τα challenges είναι πιο σημαντικά από τη θεωρία
