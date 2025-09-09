# Semantic-Search-Engine-SEC-Filings Frontend

## Overview
This frontend is built using React and Tailwind CSS, providing a user-friendly interface for searching SEC filings. It communicates with the FastAPI backend to retrieve search results and display them to the user.

## Features
- Search bar for inputting queries.
- Display of search results in a card format, including snippets and citations.
- Responsive design using Tailwind CSS.

## Getting Started

### Prerequisites
- Node.js and npm installed on your machine.

### Installation
1. Navigate to the frontend directory:
   ```
   cd frontend
   ```
2. Install the dependencies:
   ```
   npm install
   ```

### Running the Application
To start the development server, run:
```
npm start
```
This will launch the application in your default web browser.

### Folder Structure
- `src/components`: Contains reusable components like `SearchBar` and `ResultCard`.
- `src/App.tsx`: Main application component.
- `src/index.tsx`: Entry point for the React application.

## Deployment
For production builds, run:
```
npm run build
```
This will create an optimized build of the application in the `build` directory.

## License
This project is licensed under the MIT License.