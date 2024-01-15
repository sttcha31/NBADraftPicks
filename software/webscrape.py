import selenium
from bs4 import BeautifulSoup
import requests
import random
#https://web1.ncaa.org/stats/StatsSrv/careersearch
#https://www.kaggle.com/datasets/benwieland/nba-draft-data
#https://www.sports-reference.com/cbb/players/kevin-durant-1.html

def performanceIndexCalculator(vector):
    return 0

stattemplate = {
    "Name": "",
    "YearDrafted": "",
    "College": "",
    "YearsInCollege": "",
    "Conference": "",
    "HomeCity": "",
    "HomeState": "",
    "Position": "",
    "Height(cm)": "",
    "Weight(kg)": "",
    "cG": "",
    "cGS": "",
    "cMP": "",
    "cFG": "",
    "cFGA": "",
    "cFG%": "",
    "c2P": "",
    "c2PA": "",
    "c2P%": "",
    "c3P": "",
    "c3PA": "",
    "c3P%": "",
    "cFT": "",
    "cFTA": "",
    "cFT%": "",
    "ceFG%": "",
    "cORB": "",
    "cDRB": "",
    "cTRB": "",
    "cAST": "",
    "cSTL": "",
    "cBLK": "",
    "cTOB": "",
    "cPF": "",
    "cPTS": "",
    "cSOS": "",
    "cWS": "",
    "PI": "",
    # "max" and "min" lists added
    "cGmax": "",
    "cGSmax": "",
    "cMPmax": "",
    "cFGmax": "",
    "cFGAmax": "",
    "cFG%max": "",
    "c2Pmax": "",
    "c2PAmax": "",
    "c2P%max": "",
    "c3Pmax": "",
    "c3PAmax": "",
    "c3P%max": "",
    "cFTmax": "",
    "cFTAmax": "",
    "cFT%max": "",
    "ceFG%max": "",
    "cORBmax": "",
    "cDRBmax": "",
    "cTRBmax": "",
    "cASTmax": "",
    "cSTLmax": "",
    "cBLKmax": "",
    "cTOBmax": "",
    "cPFmax": "",
    "cPTSmax": "",
    "cSOSmax": "",
    "cGmin": "",
    "cGSmin": "",
    "cMPmin": "",
    "cFGmin": "",
    "cFGAmin": "",
    "cFG%min": "",
    "c2Pmin": "",
    "c2PAmin": "",
    "c2P%min": "",
    "c3Pmin": "",
    "c3PAmin": "",
    "c3P%min": "",
    "cFTmin": "",
    "cFTAmin": "",
    "cFT%min": "",
    "ceFG%min": "",
    "cORBmin": "",
    "cDRBmin": "",
    "cTRBmin": "",
    "cASTmin": "",
    "cSTLmin": "",
    "cBLKmin": "",
    "cTOBmin": "",
    "cPFmin": "",
    "cPTSmin": "",
    "cSOSmin": "",
}

ex = ["Name","YearDrafted","College","YearsInCollege", "Conference", "HomeCity", "HomeState", "Position", "Height(cm)", "Weight(kg)", "cG", "cGS", "cMP", "cFG", "cFGA", "cFG%", "c2P", "c2PA", "c2P%", "c3P", "c3PA", "c3P%","cFT","cFTA","cFT%","ceFG%","cORB","cDRB","cTRB","cAST","cSTL","cBLK","cTOB","cPF","cPTS","cSOS","cWS","PI"]

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
    #  stats = [playername, draftclass, college]
     stats = stattemplate
     response = requests.get(playerurl)
     if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        #playerjake
        #yeardrafted
        #college
        #yearsInCollege
        stats["YearDrafted"] = len(soup.findAll('table')[0].tbody.findAll('tr'))
        #conference
        stats["Conference"] = soup.findAll('table')[0].tbody.findAll('tr')[0].find('td', {'data-stat': 'conf_abbr'}).text
        #HomeCity
        hometown = soup.findAll('p')[2].text
        init = hometown.index(" ") + 1
        sep = hometown.index(",")
        end = hometown.index("\n", sep)
        stats["HomeCity"] =  hometown[init:sep]
        #HomeState
        stats["HomeState"] = hometown[sep+2:end] 
        #Position
        if "Forward" in soup.findAll('p')[0].text: stats["Position"] = "Foward"
        if "Guard" in soup.findAll('p')[0].text: stats["Position"] = "Guard"
        if "Center" in soup.findAll('p')[0].text: stats["Position"] =  "Center"
        #Height
        physique = soup.findAll('p')[1].text
        hs = physique.index("(")+1
        he = physique.index("c")
        stats["Height(cm)"] = physique[hs:he]
        #Weight
        ws = physique.index(",", he)+2
        we = physique.index("k")
        stats["Weight(kg)"] = physique[ws:we]
        # College Games
        stats["cG"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'games'}).text
        # College Games Started
        stats["cGS"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'games_started'}).text
        # College Minutes Played
        stats["cMP"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'mp_per_g'}).text
        # College FG
        stats["cFG"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg_per_g'}).text
        # College FGA
        stats["cFGA"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fga_per_g'}).text
        # College FG%
        stats["cFG%"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg_pct'}).text
        # College 2P
        stats["c2P"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg2_per_g'}).text
        # College 2PA
        stats["c2PA"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg2a_per_g'}).text
        # College 2P%
        stats["c2P%"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg2_pct'}).text
        # College 3P
        stats["c3P"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg3_per_g'}).text
        # College 3PA
        stats["c3PA"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg3a_per_g'}).text
        # College 3P%
        stats["c3P%"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fg3_pct'}).text
        # College FT
        stats["cFT"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'ft_per_g'}).text
        # College FTA
        stats["cFTA"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'fta_per_g'}).text
        # College FT%
        stats["cFT%"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'ft_pct'}).text
        # College ceGF
        stats["ceFG%"] = soup.find('table', {"id": "players_advanced"}).tfoot.findAll('tr')[0].find('td', {'data-stat': 'efg_pct'}).text
        # College ORB
        stats["cORB"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'orb_per_g'}).text
        # College DRB
        stats["cDRB"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'drb_per_g'}).text
        # College TRB
        stats["cTRB"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'trb_per_g'}).text
        # College AST
        stats["cAST"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'ast_per_g'}).text
        # College STL
        stats["cSTL"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'stl_per_g'}).text
        # College BLK
        stats["cBLK"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'blk_per_g'}).text
        # College TOV
        stats["cTOV"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'tov_per_g'}).text
        # College PF
        stats["cPF"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'pf_per_g'}).text
        # College PTS
        stats["cPTS"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'pts_per_g'}).text
        # College SOS
        stats["cSOS"] = soup.findAll('table')[0].tfoot.findAll('tr')[0].find('td', {'data-stat': 'sos'}).text
        # College WS
        # thing = soup.find('div', {'class': 'stats_pullout'})
        stats["cWS"] = soup.find('div', {'class': 'stats_pullout'}).find('div', {'class': 'p3'}).findAll('p')[1].text
        # College PI
        stats["cPI"] = "tbd"
     else:
        print('error')
    #  ex = ["Name","YearDrafted","College","YearsInCollege", "Conference", "HomeCity", "HomeState", "Position", "Height(cm)", "Weight(kg)", "cG", "cGS", "cMP", "cFG", "cFGA", "cFG%", "c2P", "c2PA", "c2P%", "c3P", "c3PA", "c3P%","cFT","cFTA","cFT%","ceFG%","cORB","cDRB","cTRB","cAST","cSTL","cBLK","cTOB","cPF","cPTS","cSOS","cWS","PI"]
     stats = progressionAndPeakStats(playerurl, stats)
     pretty_printv2(stats)
     return stats

def progressionAndPeakStats(playerurl, stats):
    maxstats = ["cGmax", "cGSmax", "cMPmax", "cFGmax", "cFGAmax", "cFG%max", "c2Pmax", "c2PAmax", "c2P%max", "c3Pmax", "c3PAmax", "c3P%max", "cFTmax", "cFTAmax", "cFT%max", "cORBmax", "cDRBmax", "cTRBmax", "cASTmax", "cSTLmax", "cBLKmax", "cTOBmax", "cPFmax", "cPTSmax", "cSOSmax"]
    minstats = ["cGmin", "cGSmin", "cMPmin", "cFGmin", "cFGAmin", "cFG%min", "c2Pmin", "c2PAmin", "c2P%min", "c3Pmin", "c3PAmin", "c3P%min", "cFTmin", "cFTAmin", "cFT%min", "cORBmin", "cDRBmin", "cTRBmin", "cASTmin", "cSTLmin", "cBLKmin", "cTOBmin", "cPFmin", "cPTSmin", "cSOSmin"]
    metrics =  ["games", "games_started", "mp_per_g", "fg_per_g", "fga_per_g", "fg_pct", "fg2_per_g", "fg2a_per_g", "fg2_pct", "fg3_per_g", "fg3a_per_g", "fg3_pct", "ft_per_g", "fta_per_g", "ft_pct", "orb_per_g", "drb_per_g", "trb_per_g", "ast_per_g", "stl_per_g", "blk_per_g", "tov_per_g", "pf_per_g", "pts_per_g", "sos" ]
    response = requests.get(playerurl)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        #best
        for metric in metrics:
            best = 0
            bestv2 = 100
            for year in range(len(soup.findAll('table')[0].tbody.findAll('tr'))):
                if metric != "tov_per_g" and metric != "pf_per_g":
                    if (current:=float(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text)) > best:
                        best = current
                else:
                   if (current:=float(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text)) < bestv2:
                        bestv2 = current 
            if metric != "tov_per_g" and metric != "pf_per_g":
                stats[maxstats[metrics.index(metric)]] = best
            else:
                stats[maxstats[metrics.index(metric)]] = bestv2
        #worst
        for metric in metrics:
            worst = 100 
            worstv2 = 0
            for year in range(len(soup.findAll('table')[0].tbody.findAll('tr'))):
                if metric != "tov_per_g" and metric != "pf_per_g":
                    if (current:=float(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text)) < worst:
                        worst = current
                else:
                    if (current:=float(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text)) > worstv2:
                        worstv2 = current
            if metric != "tov_per_g" and metric != "pf_per_g":
                stats[minstats[metrics.index(metric)]] = worst
            else:
                stats[minstats[metrics.index(metric)]] = worstv2 
        #max and min ceFG$
        best, worst = 0, 100
        for year in range(len(soup.find('table', {"id": "players_advanced"}).tbody.findAll('tr'))):
            if (current:=float(soup.find('table', {"id": "players_advanced"}).tbody.findAll('tr')[year].find('td', {'data-stat': 'efg_pct'}).text)) > best:
                best = current
            if current < worst:
                worst = current
        stats["ceFG%max"] = best
        stats["ceFG%min"] = worst

    return stats              
                        
def highSchoolStats():
    return
def overseasstats(internaturl, draftyear):
    return

def pretty_print(a, b):
    max_width = max(len(str(item)) for item in a)
    for item1, item2 in zip(a, b):
        print("{:<{}}   {}".format(item1, max_width, item2))

def pretty_printv2(dict):
    max_width = max(len(str(item)) for item in list(dict.keys()))
    for item1, item2 in zip(list(dict.keys()), list(dict.values())):
        print("{:<{}}   {}".format(item1, max_width, item2))

def performanceIndexCalculator(playerurl):
    stats = {}
# draftClassIteration("2003")

# collegeStats("https://www.sports-reference.com/cbb/players/chris-bosh-1.html?utm_medium=sr_xsite&utm_source=bbr&utm_campaign=2023_02_tbl_player_college_stats&utm_content=lnk_mcbb&utm_id=boshch01", "Chris Bosh", "2003", "Georgia Tech")
collegeStats("https://www.sports-reference.com/cbb/players/stephen-curry-1.html", "Steph Curry", "2009", "Davidson")

# secondar{y_link("https://www.basketball-reference.com/players/a/anthoca01.html", True)

