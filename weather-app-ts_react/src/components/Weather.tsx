import React, { useState } from 'react';
import axios from 'axios';

// Define TypeScript interfaces for weather data
interface WeatherData {
  temperature: number;
  condition: string;
  humidity: number;
  wind_speed: number;
}

const Weather: React.FC = () => {
  const [city, setCity] = useState<string>('');
  const [weather, setWeather] = useState<WeatherData | null>(null);
  const [error, setError] = useState<string>('');

  const fetchWeather = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/weather`, {
        params: { city },
      });
      setWeather(response.data);
      setError('');
    } catch (err) {
      setError('City not found or API error');
      setWeather(null);
    }
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    fetchWeather();
  };

  return (
    <div>
      <h1>Weather App</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Enter city"
          required
        />
        <button type="submit">Get Weather</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {weather && (
        <div>
          <h2>Weather in {city}</h2>
          <p>Temperature: {weather.temperature}°C</p>
          <p>Condition: {weather.condition}</p>
          <p>Humidity: {weather.humidity}%</p>
          <p>Wind Speed: {weather.wind_speed} kph</p>
        </div>
      )}
    </div>
  );
};

export default Weather;
