// src/App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [url, setUrl] = useState('');
    const [prompt, setPrompt] = useState('');
    const [result, setResult] = useState('');

    const handleScrape = async () => {
        try {
            const response = await axios.post('http://localhost:5000/scrape', {
                url: url,
                prompt: prompt
            });
            setResult(response.data.result);
        } catch (error) {
            console.error("Error scraping website:", error);
            setResult("An error occurred while scraping the website.");
        }
    };

    return (
        <div className="App">
            <h1>Web Scraper and AI Parser</h1>
            <input
                type="text"
                placeholder="Enter website URL"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
            />
            <input
                type="text"
                placeholder="Enter AI prompt"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
            />
            <button onClick={handleScrape}>Scrape and Parse</button>
            <div>
                <h2>Result:</h2>
                <pre>{result}</pre>
            </div>
        </div>
    );
}

export default App;