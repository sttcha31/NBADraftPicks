import selenium
from bs4 import BeautifulSoup
import requests
import re
import random
import csv
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
    "cTOV": "",
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
    "cTOVmax": "",
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
    "cTOVmin": "",
    "cPFmin": "",
    "cPTSmin": "",
    "cSOSmin": "",
}

ex = ["Name","YearDrafted","College","YearsInCollege", "Conference", "HomeCity", "HomeState", "Position", "Height(cm)", "Weight(kg)", "cG", "cGS", "cMP", "cFG", "cFGA", "cFG%", "c2P", "c2PA", "c2P%", "c3P", "c3PA", "c3P%","cFT","cFTA","cFT%","ceFG%","cORB","cDRB","cTRB","cAST","cSTL","cBLK","cTOV","cPF","cPTS","cSOS","cWS","PI"]
def main():
    nbadrafts = {
        "2003": "https://www.basketball-reference.com/draft/NBA_2003.html",
        "2004": "https://www.basketball-reference.com/draft/NBA_2004.html",
        "2005": "https://www.basketball-reference.com/draft/NBA_2005.html",
        "2006": "https://www.basketball-reference.com/draft/NBA_2006.html",
        "2007": "https://www.basketball-reference.com/draft/NBA_2007.html",
        "2008": "https://www.basketball-reference.com/draft/NBA_2008.html",
        "2009": "https://www.basketball-reference.com/draft/NBA_2009.html",
        "2010": "https://www.basketball-reference.com/draft/NBA_2010.html",
        "2011": "https://www.basketball-reference.com/draft/NBA_2011.html",
        "2012": "https://www.basketball-reference.com/draft/NBA_2012.html",
        "2013": "https://www.basketball-reference.com/draft/NBA_2013.html",
        "2014": "https://www.basketball-reference.com/draft/NBA_2014.html",
        "2015": "https://www.basketball-reference.com/draft/NBA_2015.html",
        "2016": "https://www.basketball-reference.com/draft/NBA_2016.html",
        "2017": "https://www.basketball-reference.com/draft/NBA_2017.html",
        "2018": "https://www.basketball-reference.com/draft/NBA_2018.html",
        "2019": "https://www.basketball-reference.com/draft/NBA_2019.html",
        "2020": "https://www.basketball-reference.com/draft/NBA_2020.html",
        "2021": "https://www.basketball-reference.com/draft/NBA_2021.html",
    }
    data = []
    with open(r"data\train.csv", 'a', newline='') as file:
        for year in range(2003, 2021+1):
            response = requests.get(nbadrafts[str(year)])
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                for index in range(0,62):
                    if index not in (29,30):
                        nbaLink = "https://www.basketball-reference.com"+soup.find("table", {"id": "stats"}).tbody.findAll("tr")[index].find("td", {"data-stat": "player"}).a["href"]
                        playerName = soup.find("table", {"id": "stats"}).tbody.findAll("tr")[index].find("td", {"data-stat": "player"}).a.text
                        if soup.find("table", {"id": "stats"}).tbody.findAll("tr")[index].find("td", {"data-stat": "college_name"})["csk"] != "Zzz":
                            collegeName = soup.find("table", {"id": "stats"}).tbody.findAll("tr")[index].find("td", {"data-stat": "college_name"})["csk"]
                            try:
                                collegeLink = secondary_link(nbaLink, True)
                                # data.append(collegeStats(collegeLink,playerName,str(year),collegeName))
                                stat = collegeStats(collegeLink,playerName,str(year),collegeName)
                                writer = csv.DictWriter(file, fieldnames=stat.keys())
                                writer.writerow(stat)
                            except:
                                print("")

                        # else:
                        #     preNbaLink = secondary_link(nbaLink, False)
                        #     if "gleague" in preNbaLink:
                        #         data.append(gleagueStats(preNbaLink, playerName,str(year)))
                        #     else:
                        #         return
            else:
                print("error")


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
            print(soup.find("div", {"id": "bottom_nav_container"}).findAll("ul"))
            return(soup.find("div", {"id": "bottom_nav_container"}).findAll("ul")[len(soup.find("div", {"id": "bottom_nav_container"}).findAll("ul"))-1].find("li").a.get('href'))
    else:
        print("error")

def collegeStats(playerurl, playername, draftclass, college):
     stats = stattemplate
     stats["Name"] = playername
     stats["YearDrafted"] = draftclass
     stats["College"] = college
     response = requests.get(playerurl)
     if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        #yearsInCollege
        stats["YearsInCollege"] = len(soup.findAll('table')[0].tbody.findAll('tr'))
        #conference
        stats["Conference"] = soup.findAll('table')[0].tbody.findAll('tr')[0].find('td', {'data-stat': 'conf_abbr'}).text
        #HomeCity
        try:
            hometown = soup.find('strong', string='Hometown:').parent.text
            init = hometown.index(" ") + 1
            sep = hometown.index(",")
            end = hometown.index("\n", sep) 
            stats["HomeCity"] =  hometown[init:sep]
            #HomeState
            stats["HomeState"] = hometown[sep+2:end] 
        except:
            stats["HomeCity"] = ""
            stats["HomeState"] = ""
        #Position
        if "Forward" in soup.find('strong', string=re.compile('Position:')).parent.text: stats["Position"] = "Foward"
        if "Guard" in soup.find('strong', string=re.compile('Position:')).parent.text: stats["Position"] = "Guard"
        if "Center" in soup.find('strong', string=re.compile('Position:')).parent.text: stats["Position"] =  "Center"
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
        stats["PI"] = "tbd"
        stats = progressionAndPeakStats(playerurl, stats)
        pretty_printv2(stats)
        return stats
     else:
        print(response.status_code)
        return stats
    #  ex = ["Name","YearDrafted","College","YearsInCollege", "Conference", "HomeCity", "HomeState", "Position", "Height(cm)", "Weight(kg)", "cG", "cGS", "cMP", "cFG", "cFGA", "cFG%", "c2P", "c2PA", "c2P%", "c3P", "c3PA", "c3P%","cFT","cFTA","cFT%","ceFG%","cORB","cDRB","cTRB","cAST","cSTL","cBLK","cTOV","cPF","cPTS","cSOS","cWS","PI"]
     

def gleagueStats(playerurl, playername, draftclass):
    return
def progressionAndPeakStats(playerurl, stats):
    maxstats = ["cGmax", "cGSmax", "cMPmax", "cFGmax", "cFGAmax", "cFG%max", "c2Pmax", "c2PAmax", "c2P%max", "c3Pmax", "c3PAmax", "c3P%max", "cFTmax", "cFTAmax", "cFT%max", "cORBmax", "cDRBmax", "cTRBmax", "cASTmax", "cSTLmax", "cBLKmax", "cTOVmax", "cPFmax", "cPTSmax", "cSOSmax"]
    minstats = ["cGmin", "cGSmin", "cMPmin", "cFGmin", "cFGAmin", "cFG%min", "c2Pmin", "c2PAmin", "c2P%min", "c3Pmin", "c3PAmin", "c3P%min", "cFTmin", "cFTAmin", "cFT%min", "cORBmin", "cDRBmin", "cTRBmin", "cASTmin", "cSTLmin", "cBLKmin", "cTOVmin", "cPFmin", "cPTSmin", "cSOSmin"]
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
                    try:
                        if (current:=float(emptyStatCheck(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text))) > best:
                            best = current
                    except:
                        best = best
                else:
                    try:
                        if (current:=float(emptyStatCheck(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text))) < bestv2:
                            bestv2 = current 
                    except:
                        bestv2 = bestv2
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
                    try:
                        if (current:=float(emptyStatCheck(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text))) < worst:
                            worst = current
                    except:
                        worst = worst
                else:
                    try:
                        if (current:=float(emptyStatCheck(soup.findAll('table')[0].tbody.findAll('tr')[year].find("td", {"data-stat": metric}).text))) > worstv2:
                            worstv2 = current
                    except:
                        worstv2 = worstv2
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
def emptyStatCheck(value):
    if value == "":
        return 0
    else:
        return value

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
    nbastats = {
        "Seasons": "",
        "G":"",
        "GS":"",
        "MP":"",
        "FG":"",
        "FGA":"",
        "FG%":"",
        "3P":"",
        "3PA":"",
        "3P%":"",
        "2P":"",
        "2PA":"",
        "2P%":"",
        "eFG%":"",
        "FT":"",
        "FTA": "",
        "FT%":"",
        "ORB":"",
        "DRB":"",
        "TRB":"",
        "AST":"",
        "STL":"",
        "BLK":"",
        "TOV":"",
        "PF":"",
        "PTS":"",
        "PER":"",
        "TS%":"",
        "3PAr":"",
        "FTr": "",
        "ORB%": "",
        "DRB%": "",
        "TRB%": "",
        "AST%":"",
        "STL%": "",
        "BLK%":"",
        "TOV%":"",
        "USG%":"",
        "OWS":"",
        "DWS":"",
        "WS": "",
        "WS/48":"",
        "OBRM":"",
        "DBPM":"",
        "BPM":"",
        "VORP":"",
        

    }
# draftClassIteration("2003")

# collegeStats("https://www.sports-reference.com/cbb/players/chris-bosh-1.html?utm_medium=sr_xsite&utm_source=bbr&utm_campaign=2023_02_tbl_player_college_stats&utm_content=lnk_mcbb&utm_id=boshch01", "Chris Bosh", "2003", "Georgia Tech")
thing = collegeStats("https://www.sports-reference.com/cbb/players/carmelo-anthony-1.html", "Steph Curry", "2009", "Davidson")
with open(r"data\train.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=thing.keys())
    writer.writeheader()
main()
# secondar{y_link("https://www.basketball-reference.com/players/a/anthoca01.html", True)

# print(secondary_link("https://www.basketball-reference.com/players/w/wadedw01.html", True))

# response = requests.get("https://www.basketball-reference.com/draft/NBA_2003.html")
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     for index in range(0,62):
#         if index not in (30,31):
#             print(soup.find("table", {"id": "stats"}).tbody.findAll("tr")[index].find("td", {"data-stat": "college_name"}))
#             if soup.find("table", {"id": "stats"}).tbody.findAll("tr")[index].find("td", {"data-stat": "college_name"})["csk"] != "Zzz":
#                 print("here")
#             print(soup.find("table", {"id": "stats"}).tbody.findAll("tr")[index].find("td", {"data-stat": "player"}).a.text)

# print(secondary_link("https://www.basketball-reference.com/players/g/greenja05.html", False))