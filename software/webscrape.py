import selenium
from bs4 import BeautifulSoup
import random
#https://web1.ncaa.org/stats/StatsSrv/careersearch
#https://www.kaggle.com/datasets/benwieland/nba-draft-data
#https://www.sports-reference.com/cbb/players/kevin-durant-1.html

user_agent_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',

]

def performanceIndexCalculator(vector):
    return 0

def get_info(player):
    custom_headers = {
            'user-agent':  random.choice(user_agent_list),
            'Accept-Language': 'en-US,en;q=0.9'
    }
    r = requests.get('https://www.sports-reference.com/cbb/'+playerf+"-"playerl+"1", headers= custom_headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    