# Author: Srini Pusuluri
# Date: 9/28/2025
# Description: ArXiv Research Bot - A web application to search and display arXiv papers using NiceGUI

from nicegui import ui
import requests
from bs4 import BeautifulSoup

# Global variable to track the starting index for arXiv search results
arxiv_start = 0

# Function to fetch arXiv search results based on query
def fetch_arxiv_results(query, topic_filter=None, max_results=10, start=0):
    query_encoded = query.replace(' ', '+')
    url = f"https://export.arxiv.org/api/query?search_query=all:{query_encoded}&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "xml")

    results = []
    # Parse each entry in the XML response
    for entry in soup.find_all('entry'):
        title = entry.title.text.strip()
        authors = ', '.join([author.find('name').text for author in entry.find_all('author')])
        abstract = entry.summary.text.strip()
        date = entry.published.text.strip()
        link = entry.id.text.strip()

        # Filter results based on topic if specified
        if topic_filter and topic_filter.lower() not in (title + abstract).lower():
            continue

        results.append({"title": title, "authors": authors, "abstract": abstract, "date": date, "link": link})
    return results



# Function to perform initial search and display results
def search(topic):
    global arxiv_start
    arxiv_start = 0  # Reset start index for new search
    ui.notify(f"Searching for {topic}...")
    arxiv_container.clear()
    results = fetch_arxiv_results(topic, topic_filter=topic, max_results=5, start=arxiv_start)
    arxiv_start += 5

    if not results:
        with arxiv_container:
            ui.label(f"❌ No results for {topic}").classes("text-red-500")
        return

    # Display each result in a card
    with arxiv_container:
        for r in results:
            with ui.card().tight().classes("w-full shadow-md m-2 p-4"):
                ui.label(r['title']).classes("text-lg font-bold")
                ui.label(f"Authors: {r['authors']}").classes("text-sm text-gray-600")
                ui.label(f"Date: {r['date']}").classes("text-sm text-gray-400")
                ui.label(r['abstract']).classes("text-sm mt-2")
                ui.link("🔗 Read Paper", r['link']).classes("text-blue-600 underline mt-2")
        ui.button("Next ArXiv", on_click=lambda: search_next_arxiv(topic_input.value))

# Function to load and display next set of arXiv results
def search_next_arxiv(topic):
    global arxiv_start
    results = fetch_arxiv_results(topic, topic_filter=topic, max_results=5, start=arxiv_start)
    arxiv_start += 5
    if results:
        # Append new results to the container
        with arxiv_container:
            for r in results:
                with ui.card().tight().classes("w-full shadow-md m-2 p-4"):
                    ui.label(r['title']).classes("text-lg font-bold")
                    ui.label(f"Authors: {r['authors']}").classes("text-sm text-gray-600")
                    ui.label(f"Date: {r['date']}").classes("text-sm text-gray-400")
                    ui.label(r['abstract']).classes("text-sm mt-2")
                    ui.link("🔗 Read Paper", r['link']).classes("text-blue-600 underline mt-2")
    else:
        ui.notify("No more arXiv results")



# UI Elements
ui.label("🔎 ArXiv Research Bot").classes("text-2xl font-bold mb-4")

# Input field for topic
topic_input = ui.input(label="Enter topic").props("outlined").classes("w-96")
# Search button
ui.button("Search", on_click=lambda: search(topic_input.value)).classes("bg-blue-500 text-white px-4 py-2 rounded")

# Container to hold search results
arxiv_container = ui.column()

# Refresh button to clear results
ui.button("Refresh", on_click=lambda: arxiv_container.clear()).classes("bg-gray-500 text-white px-4 py-2 rounded mt-4")

# Start the NiceGUI application on port 8081
ui.run(port=8081)
