refresh = 1800
version = 20180116.01

urls = ['https://www.sr.de/',
	'https://www.sr-mediathek.de/',
	'http://www.sr.de/sr/sr1/index.html',
	'http://www.sr.de/sr/sr2/index.html',
	'http://www.sr.de/sr/sr3/index.html',
	'http://www.unserding.de/unserding/index.html',
	'http://mediathek.unserding.de/index.php?seite=2',
	'http://mediathek.unserding.de/index.php?seite=3',
	'http://www.sr.de/sr/antennesaar/index.html',
	'http://www.sr.de/sr/fernsehen/index.html']
regex = [r'https?:\/\/[^\/]*sr\.de', r'https?:\/\/[^\/]*sr-mediathek\.de', r'https?:\/\/[^\/]*unserding\.de', r'https?:\/\/[^\/]*sr_hls_od-vh\.akamaihd\.net']
videoregex = [r'\/fernsehen\/']
liveregex = []
wikidata = 'Q691047'

