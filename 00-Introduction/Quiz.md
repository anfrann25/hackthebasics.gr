<div>
<h3>📝 Quiz Ενότητας: 01-Networking</h3>
<p>Απάντησε σωστά στο 70% (2 στις 3 ερωτήσεις) για να ξεκλειδώσεις το Linux!</p>
<hr>
<div>
<p><strong>1. Ποιο πρωτόκολλο είναι ασφαλές;</strong></p>
<label><input type="radio" name="net_q1" value="wrong"> HTTP</label><br>
<label><input type="radio" name="net_q1" value="correct"> HTTPS</label>
</div>
<div>
<p><strong>2. Σε ποιο layer του OSI ανήκει το IP routing;</strong></p>
<label><input type="radio" name="net_q2" value="correct"> Network Layer (Layer 3)</label><br>
<label><input type="radio" name="net_q2" value="wrong"> Data Link Layer (Layer 2)</label>
</div>
<div>
<p><strong>3. Τι κάνει το DNS;</strong></p>
<label><input type="radio" name="net_q3" value="correct"> Μετατρέπει ονόματα σε IP</label><br>
<label><input type="radio" name="net_q3" value="wrong"> Κρυπτογραφεί αρχεία</label>
</div>
<button onclick="checkSectionQuiz()">Υποβολή</button>
<p id="netQuizResult"></p>
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
res.innerHTML = "🎉 Μπράβο! Πέρασες! Η επόμενη ενότητα ξεκλειδώθηκε!";
localStorage.setItem('quiz_01-Networking_passed', 'true');
setTimeout(() => { window.location.hash = '#/02-Linux/README'; }, 1500);
} else {
res.style.color = "#f44336";
res.innerHTML = "❌ Απέτυχες. Προσπάθησε ξανά.";
}
}
</script>