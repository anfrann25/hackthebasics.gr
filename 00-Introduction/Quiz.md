<div style="background: #222; padding: 20px; border-radius: 8px; margin-top: 30px; border: 1px solid #444;">
    <h3>📝 Quiz Ενότητας: 01-Networking</h3>
    <p>Απάντησε σωστά στο 70% (2 στις 3 ερωτήσεις) για να ξεκλειδώσεις το Linux!</p>
    <hr style="border-color: #444;">

    <div style="margin-bottom: 15px;">
        <p><strong>1. Ποιο πρωτόκολλο είναι ασφαλές;</strong></p>
        <label><input type="radio" name="net_q1" value="wrong"> HTTP</label><br>
        <label><input type="radio" name="net_q1" value="correct"> HTTPS</label>
    </div>

    <div style="margin-bottom: 15px;">
        <p><strong>2. Σε ποιο layer του OSI ανήκει το IP routing;</strong></p>
        <label><input type="radio" name="net_q2" value="correct"> Network Layer (Layer 3)</label><br>
        <label><input type="radio" name="net_q2" value="wrong"> Data Link Layer (Layer 2)</label>
    </div>

    <div style="margin-bottom: 15px;">
        <p><strong>3. Τι κάνει το DNS;</strong></p>
        <label><input type="radio" name="net_q3" value="correct"> Μετατρέπει ονόματα σε IP</label><br>
        <label><input type="radio" name="net_q3" value="wrong"> Κρυπτογραφεί αρχεία</label>
    </div>

    <button onclick="checkSectionQuiz()" style="padding: 10px 20px; background: #007acc; color: white; border: none; border-radius: 4px; cursor: pointer;">Υποβολή</button>
    <p id="netQuizResult" style="margin-top: 15px; font-weight: bold;"></p>
</div>

<script>
function checkSectionQuiz() {
    let score = 0;
    if(document.querySelector('input[name="net_q1"]:checked')?.value === 'correct') score++;
    if(document.querySelector('input[name="net_q2"]:checked')?.value === 'correct') score++;
    if(document.querySelector('input[name="net_q3"]:checked')?.value === 'correct') score++;

    const pct = (score / 3) * 100;
    const res = document.getElementById('netQuizResult');

    if (pct >= 70) {
        res.style.color = "#4caf50";
        res.innerHTML = `🎉 Μπράβο! Πέρασες με ${pct.toFixed(0)}%. Η επόμενη ενότητα ξεκλειδώθηκε!`;
        
        // 1. Αποθήκευση της προόδου
        localStorage.setItem('quiz_01-Networking_passed', 'true');
        
        // 2. Μικρό "hack" για να ενημερωθεί το Docsify αμέσως:
        // Μετά από 1.5 δευτερόλεπτο, σπρώχνει τον χρήστη αυτόματα στο επόμενο README!
        setTimeout(() => {
            window.location.hash = '#/02-Linux/README';
        }, 1500);

    } else {
        res.style.color = "#f44336";
        res.innerHTML = `❌ Σκορ: ${pct.toFixed(0)}%. Χρειάζεσαι τουλάχιστον 70% για να συνεχίσεις.`;
    }
}
</script>