import requests
import os

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def fetch_jobs(skills):
    query = " ".join(skills[:3]) + " jobs India"
    url = f"https://serpapi.com/search.json?engine=google_jobs&q={query}&api_key={SERPAPI_KEY}"
    response = requests.get(url)
    data = response.json()

    jobs = []
    for job in data.get("jobs_results", [])[:5]:
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "link": job.get("apply_link"),
        })
    return jobs
