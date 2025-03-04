document.getElementById("ddos-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const data = {
        source_port: document.getElementById("source_port").value,
        dest_port: document.getElementById("dest_port").value,
        packet_length: document.getElementById("packet_length").value,
        packets_time: document.getElementById("packets_time").value,
        highest_layer: document.getElementById("highest_layer").value,
        transport_layer: document.getElementById("transport_layer").value
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText = result.error ? "Error: " + result.error : 
        (result.prediction === 1 ? "🚨 DDoS Attack Detected!" : "✅ Normal Traffic");
});
