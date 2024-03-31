using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class PlayerViewModel
{
    public IList<Player> Players { get; private set; }

    public PlayerViewModel()
    {
        LoadDataFromCSV();
    }
    private void LoadDataFromCSV()
    {
        var lines = File.ReadAllLines("data.csv").Skip(1);

        Players = lines.Select(line =>  
        {
            var attr = line.Split(",");
            return new Player
            {
                Name = attr[0],
                HeadShot = attr[1]
            };
        }).ToList();
    }
}
