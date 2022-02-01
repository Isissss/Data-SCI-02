// api url
const api_url =
    "https://api.thingspeak.com/channels/1642875/feed?days=1&average=60&round=2";
// Defining async function
    async function getapi(url) {

        // Storing response
        const response = await fetch(url);

        // Storing data in form of JSON
        var data = await response.json();
        console.log(data);
        if (response) {
            hideloader();
        }
        show(data);
    }

// Calling that async function
    getapi(api_url);

// Function to hide the loader
    function hideloader() {
        document.getElementById('loading').style.display = 'none';
    }

    function getTime(e) {
        d =new Date(e);
        d = d.toLocaleString('en-US', {
            weekday: 'short', // long, short, narrow
            day: 'numeric', // numeric, 2-digit
            year: 'numeric', // numeric, 2-digit
            month: 'long', // numeric, 2-digit, long, short, narrow
            hour: 'numeric', // numeric, 2-digit
            minute: 'numeric', // numeric, 2-digit
            second: 'numeric', // numeric, 2-digit
        });
    }


// Function to define innerHTML for HTML table
    function show(data) {
        let tab =
            `<tr>
          <th>Date</th>      
          <th>Humidity</th>
          <th>Temperature C</th>
          <th>Temperature F</th>
          </tr>`;

        for (let i of data.feeds) {
            getTime(i.created_at)
            tab += `<tr> 
          <td>${d}</td>
          <td>${i.field2}%</td>
          <td>${i.field3}º</td>
          <td>${i.field5}F</td>
          </tr>`;
        }
        // Setting innerHTML as tab variable
        document.getElementById("data").innerHTML = tab;
    }
