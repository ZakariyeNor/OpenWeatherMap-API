function getWeather() {
    const city = document.getElementById('cityInput').value;
    if(!city) {
        alert('Please enter a city name.');
        return;
    }

    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                const weatherDiv = document.getElementById('weather');
                weatherDiv.innerHTML = `
                        <h2>Weather in ${data.city}</h2>
                        <p>Temperature: ${data.temperature}°C</p>
                        <p>Description: ${data.description}</p>
                        <p>Humidity: ${data.humidity}</p>
                        <p>Wind Speed: ${data.wind_speed} m/s</p>
                        `;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while fetching the weather data.')
        });
}