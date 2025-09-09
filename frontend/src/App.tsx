import React, { useState } from 'react';
import SearchBar from './components/SearchBar';
import ResultCard from './components/ResultCard';

const App = () => {
    const [results, setResults] = useState([]);
    const [query, setQuery] = useState('');

    const handleSearch = async (searchQuery) => {
        setQuery(searchQuery);
        const response = await fetch(`/search?q=${encodeURIComponent(searchQuery)}`);
        const data = await response.json();
        setResults(data.snippets);
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">SEC Filings Search</h1>
            <SearchBar onSearch={handleSearch} />
            <div className="mt-4">
                {results.map((result, index) => (
                    <ResultCard key={index} snippet={result.snippet} citation={result.citation} />
                ))}
            </div>
        </div>
    );
};

export default App;