# eBay Scraper with Seller Feedback

This is a web scraper built using Python and Flask that extracts and provides seller feedback for a specific product.

## Overview

This web application allows users to search for a product on eBay and view the seller feedback. The application is built using Python, Flask, and utilizes web scraping techniques with BeautifulSoup library.

## Setup

1. Ensure you have Python installed on your system. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Install the required libraries by running the following command:

```bash
pip install flask flask_cors beautifulsoup4
```

## How to Run

Clone the repository to your local machine.

Navigate to the project directory.

Run the Flask application by executing the following command:

```bash
python app.py
```
The application will start, and you can access it at http://localhost:5000.

Usage
Enter the search query in the provided input box (e.g., "iPhone11").

Click the "Search" button.

The application will fetch eBay search results for the query and display the seller's feedback for the top result.
