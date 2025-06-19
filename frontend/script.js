fetch("http://127.0.0.1:8000/weight")
    .then(response => {
        return response.json();
    })
    .then(weightRecords => {
        console.log(weightRecords);
        const weightList = document.getElementById("weight-records-list");
        weightRecords.forEach(element => {
            const li = document.createElement("li");
            li.textContent = `${element.weight_kg} (${element.record_date})`;
            weightList.append(li);
        });
    })
    .catch(error => {
        console.error("Error fetching data", error);
    });