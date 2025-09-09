import React from 'react';

interface ResultCardProps {
    title: string;
    snippet: string;
    citation: string;
}

const ResultCard: React.FC<ResultCardProps> = ({ title, snippet, citation }) => {
    return (
        <div className="border rounded-lg p-4 shadow-md">
            <h2 className="font-bold text-lg">{title}</h2>
            <p className="text-gray-700">{snippet}</p>
            <p className="text-gray-500 italic">{citation}</p>
        </div>
    );
};

export default ResultCard;