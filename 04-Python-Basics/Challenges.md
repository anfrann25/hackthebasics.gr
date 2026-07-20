# Python Challenges 

```text
               _   _
              | | | |
  _ __  _   _ | |_| |__   ___  _ __
 | '_ \| | | || __| '_ \ / _ \| '_ \
 | |_) | |_| || |_| | | | (_) | | | |
 | .__/ \__, | \__|_| |_|\___/|_| |_|
 | |     __/ |
 |_|    |___/
```

## Mission Briefing

Καλώς όρισες στο επόμενο στάδιο της εκπαίδευσής σου.

Το Linux CLI σου έδωσε την πρόσβαση και τον έλεγχο του συστήματος. Τώρα ήρθε η ώρα να αποκτήσεις το απόλυτο εργαλείο κάθε **Cybersecurity Professional**: την **Python**.

Σε αυτή την ενότητα δεν θα μάθεις μόνο θεωρία. Στόχος είναι να μάθεις Python μέσα από πρακτικά challenges, όπως θα τη χρησιμοποιούσες σε ένα πραγματικό περιβάλλον εργασίας.

---

# The HTB CLI

Για να ελέγχεις τις λύσεις σου και να ολοκληρώνεις τα challenges, θα χρησιμοποιείς το εργαλείο **`htb`**.

Η διαδικασία είναι η ίδια για κάθε Level.

## 1Δημιουργία της λύσης

Μέσα στον φάκελο του challenge δημιούργησε ένα αρχείο:

```text
solution.py
```

και γράψε εκεί τον κώδικά σου.

---

## Έλεγχος της λύσης

Εκτέλεσε:

```bash
htb test solution.py -l <level_number>
```

Παράδειγμα:

```bash
htb test solution.py -l 3
```

Αν η λύση είναι σωστή, το CLI θα εμφανίσει το αντίστοιχο **Flag**.

---

## Εξαργύρωση του Flag

Μόλις αποκτήσεις το Flag, κάνε redeem:

```bash
htb redeem -m python -l <level_number> -f <THE_FLAG>
```

Παράδειγμα:

```bash
htb redeem -m python -l 3 -f HTB{example_flag}
```

Αν όλα είναι σωστά, το challenge θα καταχωρηθεί ως ολοκληρωμένο.

---

##  Διαθέσιμες Εντολές

| Command | Περιγραφή |
|---------|-----------|
| `htb test solution.py -l <level>` | Ελέγχει τη λύση σου |
| `htb redeem -m python -l <level> -f <FLAG>` | Καταχωρεί το Flag |
| `htb reset` | Επαναφέρει το challenge στην αρχική κατάσταση |
| `htb score` | Δείχνει την πρόοδο σου |     
---

## Installation

`Για να ξεκινήσεις το challenge πρέπει να συνδεθέις στο ίδιο docker που είχαμε συνδεθεί στο κεφάλαιο: 02-Linux, όμως πρίν από αυτό θα πρέπει να βάλουμε τα python_challenges στο παιχνίδι.`

```bash
    sudo docker cp 04-Python-Basics/python_challenges/ linux-lab:/home/player
    sudo docker start -ai linux-lab
```



##  Objective

Ο στόχος σου δεν είναι απλώς να περάσεις τα tests.

Κάθε challenge έχει σχεδιαστεί ώστε να σε φέρει πιο κοντά στον τρόπο που χρησιμοποιείται η Python στον πραγματικό χώρο της κυβερνοασφάλειας.

**Happy Hacking! 🐍**


