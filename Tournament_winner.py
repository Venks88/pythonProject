class Tournament_winner:
    def tournamentWinner(self, competitions, results):
        winnerDict = dict([]);
        for i in competitions:
            winnerDict.append(i[0], 0)
            winnerDict.append(i[1], 0)

        return "";


obj = Tournament_winner();
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]];
results = [0, 0, 1];
obj.tournamentWinner(competitions, results);
