import selenium
from bs4 import BeautifulSoup
import requests
import random
#https://web1.ncaa.org/stats/StatsSrv/careersearch
#https://www.kaggle.com/datasets/benwieland/nba-draft-data
#https://www.sports-reference.com/cbb/players/kevin-durant-1.html

def performanceIndexCalculator(vector):
    return 0


def draftClassIteration(draftclass):
    url = "https://www.basketball-reference.com/draft/NBA_"+ draftclass + ".html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for row in soup.find_all('tr'):
                player_cell = row.find('td', {'data-stat': 'player'})
                if player_cell != None:
                    print(player_cell.a.text)
            # print()
    else:
        print("error")
def secondary_link(playerurl, boolean):
    response = requests.get(playerurl)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if boolean:
            return(soup.find("div", {"id": "all_college_stats_sh"}).find("div", {"class": "section_heading_text"}).ul.findAll("li")[0].a.get('href')) 
        else:
            return None
    else:
        print("error")

def collegeStats(playerurl, playername, draftclass, college):
     stats = [playername, draftclass, college]
     response = requests.get(playerurl)
     if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        #yearsInCollege
        stats.append(len(soup.findAll('table')[0].tbody.findAll('tr'))) 
        #conference
        stats.append(soup.findAll('table')[0].tbody.findAll('tr')[0].find('td', {'data-stat': 'conf_abbr'}).text)
        #HomeCity
        hometown = soup.findAll('p')[2].text
        init = hometown.index(" ") + 1
        sep = hometown.index(",")
        end = hometown.index("\n", sep)
        stats.append(hometown[init:sep])
        #HomeState
        stats.append(hometown[sep+2:end]) 
        #Position
        if "Forward" in soup.findAll('p')[0].text: stats.append("Foward")
        if "Guard" in soup.findAll('p')[0].text: stats.append("Guard")
        if "Center" in soup.findAll('p')[0].text: stats.append("Center")
        #Height
        physique = soup.findAll('p')[1].text
        hs = physique.index("(")+1
        he = physique.index("c")
        stats.append(physique[hs:he])
        #Weight
        ws = physique.index(",", he)+2
        we = physique.index("k")
        stats.append(physique[ws:we])
        #College Games
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'games'}).text)
        #College Games States
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'games_started'}).text)
        #College Minutes Played
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'mp_per_g'}).text)
        #College FG
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg_per_g'}).text)
        #College FGA
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fga_per_g'}).text)
        #College FG%
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg_pct'}).text)
        #College 2P
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg2_per_g'}).text)
        #College 2PA
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg2a_per_g'}).text)
        #College 2P%
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg2_pct'}).text)
        #College 3P
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg3_per_g'}).text)
        #College 3PA
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg3a_per_g'}).text)
        #College 3P%
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg3_pct'}).text)
        #College FT
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'ft_per_g'}).text)
        #College FTA
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fta_per_g'}).text)
        #College FT%
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'ft_pct'}).text)
        #College ceGF
        stats.append(soup.findAll('table')[3].tfoot.findAll('tr')[0].find('td', {'data-stat': 'efg_pct'}).text)
        #College ORB
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'orb_per_g'}).text)
        #College DRB
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'drb_per_g'}).text)
        #College TRB
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'trb_per_g'}).text)
        #College AST
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'ast_per_g'}).text)
        #College STL
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'stl_per_g'}).text)
        #College BLK
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'blk_per_g'}).text)
        #College TOV
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'tov_per_g'}).text)
        #College PF
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'pf_per_g'}).text)
        #College PTS
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'pts_per_g'}).text)
        #College SOS
        stats.append(soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'sos'}).text)
        #College WS
        # thing = soup.find('div', {'class': 'stats_pullout'})
        stats.append(soup.find('div', {'class': 'stats_pullout'}).find('div', {'class': 'p3'}).findAll('p')[1].text)
        #College PI
        stats.append("tbd")
     else:
        print('error')
     ex = ["Name","YearDrafted","College","YearsInCollege", "Conference", "HomeCity", "HomeState", "Position", "Height(cm)", "Weight(kg)", "cG", "cGS", "cMP", "cFG", "cFGA", "cFG%", "c2P", "c2PA", "c2P%", "c3P", "c3PA", "c3P%","cFT","cFTA","cFT%","ceFG%","cORB","cDRB","cTRB","cAST","cSTL","cBLK","cTOB","cPF","cPTS","cSOS","cWS","PI"]
     pretty_print(ex, list(map(str, stats)))
     return stats

def highSchoolStats():
    return
def overseasstats():
    return

def pretty_print(a, b):
    max_width = max(len(str(item)) for item in a)
    for item1, item2 in zip(a, b):
        print("{:<{}}   {}".format(item1, max_width, item2))
def performanceIndexCalculator(playerurl):
    stats = {}
# draftClassIteration("2003")

# collegeStats("https://www.sports-reference.com/cbb/players/chris-bosh-1.html?utm_medium=sr_xsite&utm_source=bbr&utm_campaign=2023_02_tbl_player_college_stats&utm_content=lnk_mcbb&utm_id=boshch01", "Chris Bosh", "2003", "Georgia Tech")
# collegeStats("https://www.sports-reference.com/cbb/players/stephen-curry-1.html", "Steph Curry", "9", "Davidson")

secondary_link("https://www.basketball-reference.com/players/a/anthoca01.html", True)