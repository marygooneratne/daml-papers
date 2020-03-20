import scholarly

API_ENDPOINT = "https://dukeappml.herokuapp.com//papers/new'
count = 0
search_query = scholarly.search_pubs_query('machine learning duke university 2019')
for pub in search_query:
    count = count + 1
    paper_details["title"] = pub.bib["title"]
    paper_details["abstract"] = pub.bib["abstract"]
    paper_details["authors"] = pub.bib["author"].split(" and ")
    # authors = pub.bib["author"].split(" and ")
    # for author in authors:
    #     if "Duke University" in next(scholarly.search_author(author)).affiliation:
    #         print(pub)
    print(paper_details)
    if count == 10:
        break

{
	# "title":"4D Sparse Minkowski Corn Kernals",
	# "abstract":"Something something",
	# "authorFirstName":"Yasa",
	# "authorLastName":"Truitt",
	# "publicationDate":"Jan 3, 2000",
	# "doi":"21231541231231"
}
