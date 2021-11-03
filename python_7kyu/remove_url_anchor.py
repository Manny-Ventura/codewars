#Write a function that returns the url with anything after the anchor (#) removed.
#Ex. "www.codewars.com#about" --> "www.codewars.com"

def remove_url_anchor(url):
    final = ''
    position = url.find('#')
    index = 0
    while index < position:
        final += url[index]
        index += 1
    if final == '':
        return url
    else:
        return final