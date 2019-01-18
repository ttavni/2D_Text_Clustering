import re

def find_urls(text):
	"""Find all mentioned urls in a piece of text"""

	url_list = []
	myString_list = [item for item in text.split(" ")]

	# Re search for urls
	for item in myString_list:
		try:
			var = re.search("(?P<url>https?://[^\s]+)", item).group("url")
			url_list.append(var)
		except:
			var = ''
			url_list.append(var)

	# Filter out blanks
	url_list = list(filter(None, url_list))

	return url_list


def clean_text(text):
	text = str(text)
	### Remove URLs
	urls = find_urls(text)
	for url in urls:
		text = text.replace(url, '')

	### Remove Hashtags
	hashtags = [i for i in text.split() if i.startswith("#")]
	for hashtag in hashtags:
		text = text.replace(hashtag, '')

	### Remove @ signs
	text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

	cleantext = re.sub(re.compile('<.*?>'), '', text)
	cleantext = ''.join([i if ord(i) < 128 else ' ' for i in cleantext])
	removers = ['<p>', '</p>', '<em>', '</em>', '<a>', '<span>', '</span>',
				'</a>', '/n', '\n', '\t', '[', ']', "\'\\n", '=', '\n', ':', '*', '/',
				'|', '@', '#', '...', '"', "'", '. .', '. . .', '..', '. . . . .',
				'..', '.....', '........', '. . ', '?', '!', ';', ':']

	for remove in removers:
		cleantext = cleantext.replace(remove, '')

	cleantext = re.sub(r'<[^=>]*?>', '', cleantext)
	cleantext = re.sub('\s+', ' ', cleantext).strip()
	cleantext = re.sub(r'([^\s\w]|_)+', '', cleantext)

	return cleantext