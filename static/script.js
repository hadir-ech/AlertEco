document.getElementById("reportForm").addEventListener("submit", async function (e) {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const location = document.getElementById("location").value;

  await fetch("/add_report", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title, description, location })
  });

  document.getElementById("reportForm").reset();
  loadReports();
});

async function loadReports() {
  const res = await fetch("/get_reports");
  const data = await res.json();
  const list = document.getElementById("reportList");
  list.innerHTML = "";
  data.forEach(report => {
    const item = document.createElement("li");
    item.innerText = `${report.title} (${report.location}) : ${report.description}`;
    list.appendChild(item);
  });
}

loadReports();
