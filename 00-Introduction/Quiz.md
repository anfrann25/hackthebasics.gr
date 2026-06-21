# 📝 Quiz Ενότητας: 01-Networking

Δοκίμασε τις γνώσεις σου στα δίκτυα! Μόλις απαντήσεις σε όλες τις ερωτήσεις, πάτα το κουμπί στο τέλος για να δεις το σκορ σου.

<div id="quiz-container"></div>
<button id="submit-btn" style="padding: 12px 24px; background: #21262d; color: #c9d1d9; border: 1px solid #30363d; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 20px;">Υποβολή Απαντήσεων</button>
<div id="quiz-result" style="margin-top: 20px; font-weight: bold; font-size: 1.2rem;"></div>

<script>
// 1. Οι ερωτήσεις του Quiz σου
const questions = [
  {
    id: "q1",
    title: "1. Ποιο πρωτόκολλο είναι ασφαλές και κρυπτογραφημένο;",
    answers: ["HTTP", "HTTPS", "FTP"],
    correct: 1 // Η δεύτερη απάντηση (0-indexed, άρα 0=HTTP, 1=HTTPS)
  },
  {
    id: "q2",
    title: "2. Σε ποιο layer του OSI μοντέλου ανήκει το IP Routing;",
    answers: ["Data Link Layer (Layer 2)", "Network Layer (Layer 3)", "Transport Layer (Layer 4)"],
    correct: 1
  },
  {
    id: "q3",
    title: "3. Ποια είναι η κύρια λειτουργία του DNS;",
    answers: ["Να κρυπτογραφεί τα δεδομένα του browser", "Να μετατρέπει ονόματα (π.χ. google.com) σε IP διευθύνσεις", "Να μπλοκάρει τις επιθέσεις DDOS"],
    correct: 1
  }
];

// 2. Δημιουργία του Quiz στην οθόνη
const container = document.getElementById('quiz-container');
container.innerHTML = questions.map((q, qIdx) => `
  <div style="background: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d; margin-top: 15px;">
    <p style="font-weight: bold; margin-bottom: 10px; color: #f0f6fc;">${q.title}</p>
    ${q.answers.map((ans, ansIdx) => `
      <label style="display: block; margin-bottom: 8px; cursor: pointer; color: #c9d1d9;">
        <input type="radio" name="${q.id}" value="${ansIdx}" style="margin-right: 8px;">
        ${ans}
      </label>
    `).join('')}
  </div>
`).join('');

// 3. Έλεγχος Απαντήσεων και Υπολογισμός Σκόρ
document.getElementById('submit-btn').onclick = function() {
  let score = 0;
  
  questions.forEach(q => {
    const selected = document.querySelector(`input[name="${q.id}"]:checked`);
    if (selected && parseInt(selected.value) === q.correct) {
      score++;
    }
  });

  const pct = (score / questions.length) * 100;
  const resultDiv = document.getElementById('quiz-result');

  if (pct >= 70) {
    resultDiv.style.color = "#4caf50";
    resultDiv.innerHTML = `🎉 Συγχαρητήρια! Το σκορ σου είναι ${score}/${questions.length} (${pct.toFixed(0)}%). Είσαι έτοιμος για το επόμενο κεφάλαιο!`;
  } else {
    resultDiv.style.color = "#f44336";
    resultDiv.innerHTML = `❌ Προσπάθησε ξανά! Το σκορ σου είναι ${score}/${questions.length} (${pct.toFixed(0)}%). Χρειάζεσαι τουλάχιστον 70% για να περάσεις.`;
  }
};
</script>