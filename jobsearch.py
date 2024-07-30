import webbrowser

def search_jobs(job_title, location, experience):
    base_urls = [
        "https://www.indeed.com/jobs?q=",
        "https://www.linkedin.com/jobs/search?keywords=",
        "https://www.glassdoor.com/Job/jobs.htm?sc.keyword="
    ]
    linkedin_url = f"https://www.linkedin.com/jobs/search?keywords={job_title}&location={location}&f_E={experience}"
    indeed_url = f"https://www.indeed.com/jobs?q={job_title}&l={location}&explvl={experience}"
    glassdoor_url = f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={job_title}+{location}+{experience}"

    webbrowser.open(indeed_url)
    webbrowser.open(linkedin_url)
    webbrowser.open(glassdoor_url)

if __name__ == "__main__":
    job_title = input("Enter job title: ").replace(' ', '+')
    location = input("Enter location: ").replace(' ', '+')
    experience = input("Enter experience level (entry_level, mid_level, senior_level): ").replace(' ', '+')
    search_jobs(job_title, location, experience)
