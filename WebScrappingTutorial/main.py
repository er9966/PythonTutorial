from bs4 import BeautifulSoup
import requests
import time

# with open('home.html', 'r') as html_file:
    # content = html_file.read()
    # print(content)

    #create instance of beautiful soup, (what_content, parser)
    # lxml is a parser, I just installed.
    # There are other parsers like the python default ones
    # soup = BeautifulSoup(content, 'lxml')

    #create a tag
    #tags = soup.find('h5')
    # print out the tag, but it only prints out one??
    # print(tags)
    # get all tags, not just the first one
    #courses_html_tags = soup.find_all('h5')
    # print out all tag CONTENT
    #for course in courses_html_tags:
        #print(course.text)

    # add _ to class because class is a python keyword
    # course_card = soup.find_all('div', class_='card')
    # for course in course_card:
        # course_name = course.h5.text # h5 contain course title
        # a tags contain price information
        # text get rid of the A tags, but still have "course starts at 20$"
        # split()[index] grabs the numeric value + dollar
        # course_price = course.a.text.split()[-1]
        # print(course_name)
        # print(course_price)
        # print(f'{course_name} costs {course_price}')


# user can input skils they don't have
print("Put some skills that you are not familiar with")
unfamiliar_skill = input(">")
print(f"filtering out {unfamiliar_skill} . . .")

def find_jobs():
    # requests library: request information from a website, store in a
    # variable html_text, .text is to get the html text of the site
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')

    # find all the jobs that posted a few days ago
    # that contains the keyword Python

    # inspect the webpage, we want to get list with class name clearfix job-bx wht-shd-bx
    # soup.find_all: only going to bring result back from the first page
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx') # only find the first job that showed up
    #print(jobs)
    # .text gets text, get rid of white space
    for job in jobs:
        # we need to add a .span at the end because the content we want is inside another span tag!
        # only include the job if the job is posted "a few days ago"
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            # print(published_date)

            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            #print(company_name)
            # lets get skills of requirement
            skills = job.find('span', class_='srp-skills').text.replace(' ','')

            # get the link of the job, inside list, header, h2 tag, a tag
            # [] get the content inside the href attribute
            more_info = job.header.h2.a['href']

            # don't show skills that user is not familiar with
            if unfamiliar_skill not in skills:
                # create a new file in a directory
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info}")
                print(" ")
if __name__ == '__main__':
    while True:      # run this fuction every 10 minutes
        find_jobs()
        time_wait = 10
        print(f"waiting {time_wait} minutes ...")
        time.sleep(time_wait = 60)




