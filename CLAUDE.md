# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Lord of Files analytics dashboard that visualizes score distributions for different department managers. The project consists of:

- A static HTML dashboard (`index.html`) with embedded data and Chart.js visualizations
- JSON data files in the `data/` directory containing leaderboard data for each manager
- JavaScript parser (`leaderboard-parser.js`) for extracting data from web elements
- Manager profile images in the `images/` directory

## Architecture

**Static Web Application**: Single-page HTML application with inline JavaScript and CSS, no build process required.

**Data Structure**: Each JSON file contains an array of user objects with rank, name, and score properties. Data is embedded directly in the HTML file for the current snapshot (June 4th, 2025).

**Visualization**: Uses Chart.js for rendering two chart types:
- Rank Distribution (power law analysis)
- Score Histogram with configurable bin sizes

**Department Managers**: Four managers with corresponding data files:
- `bully` (Bully The Kid) - data/dood-bully.json
- `doxmuddler` (Dox Muddler) - data/doxmuddler.json  
- `negativenancy` (Negative Nancy) - data/negativenancy.json
- `trollalot` (Sir TrollzALot) - data/trollalot.json

## Key Files

- `index.html`: Main dashboard with embedded data and complete application logic
- `leaderboard-parser.js`: Browser console script for extracting leaderboard data from DOM elements
- `data/*.json`: Raw leaderboard data files (used for data updates)
- `images/`: Manager profile images and background assets

## Development Workflow

**Viewing the Dashboard**: Open `index.html` directly in a web browser - no server required.

**Data Updates**: Update JSON files in `data/` directory, then manually embed the new data in the `rawData` object in `index.html`.

**Parsing New Data**: Use `leaderboard-parser.js` in browser console on leaderboard pages to extract user data in the required format.

## Data Format

Each manager's data follows this structure:
```json
[
  {
    "rank": "1",
    "name": "username",
    "score": "369"
  }
]
```

The dashboard converts string values to integers and adds `departmentManager` properties during processing.