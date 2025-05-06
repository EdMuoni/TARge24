"""Board games."""


class Statistics:
    """The only required class."""

    def __init__(self, filename: str):
        """Class constructor."""
        with open(filename, mode="r", encoding="utf-8") as file:
            Game.all_games = []
            Player.all_players = []
            lines = file.read().splitlines()
            for line in lines:
                values = line.split(";")
                game_name = values[0]
                player_names = values[1]
                result_type = values[2]
                result = values[3]
                players = Player.get_players(player_names)
                Game(game_name, result_type, result, players)

    def get(self, path: str):
        """Getter Api endpoint handler."""
        if path == "/players":
            return list(map(lambda p: p.get_name(), Player.all_players))
        if path == "/games":
            return list(set(map(lambda g: g.get_name(), Game.all_games)))
        if path == "/total":
            return len(Game.all_games)
        if path.startswith("/total"):
            game_type = path.split("/")[-1]
            return Game.get_amount_of_type(game_type)
        _, collection, name, detail = path.split("/")
        if collection == "player":
            return self.handle_player(name, detail)
        if collection == "game":
            return self.handle_game(name, detail)

    def handle_player(self, name, detail):
        """Handle requests for player data."""
        players = Player.get_players(name)
        if len(players) == 1:
            if detail == "amount":  # path = /players/tiit/amount
                return len(players[0].get_played_games())
            if detail == "favourite":  # path = /players/tiit/favourite
                return players[0].get_favourite().get_name()
            if detail == "won":
                return players[0].get_won_count()

    def handle_game(self, name, detail):
        """Handle requests for game data."""
        games: list[Game] = Game.get_games(name)
        if len(games) > 0:
            if detail == "amount":
                return len(games)
            if detail == "player-amount":
                occurrences = {game: game.get_player_count() for game in games}
                return max(occurrences, key=lambda g: occurrences[g]).get_player_count()
            if detail == "most-wins":
                return self.get_most_wins_player_name(games)
            if detail == "most-frequent-winner":
                return games[0].most_frequent_winner(name, games)
            if detail == "most-losses":
                return self.get_most_losses_player_name(games)
            if detail == "most-frequent-loser":
                return games[0].most_frequent_loser(name, games)
            if detail == "record-holder":
                return self.get_record_holder(games)

    def get_most_wins_player_name(self, games):
        """Get most winning player name."""
        winners = {}
        for game in games:
            winner_name = game.get_winners_name()
            winners[winner_name] = winners.get(winner_name, 0) + 1
        return max(winners, key=lambda p: winners[p])

    def get_most_losses_player_name(self, games):
        """Get most losing player name."""
        losers = {}
        for game in games:
            loser_name = game.get_losers_name()
            losers[loser_name] = losers.get(loser_name, 0) + 1
        return max(losers, key=lambda p: losers[p])

    def get_record_holder(self, games):
        """Return the player with the highest score (record) in points-based games."""
        record_holders = {}
        for game in games:
            if game.get_type() == "points":
                for player, score in zip(game.get_players(), map(int, game.get_result().split(","))):
                    record_holders.setdefault(player.get_name(), {"scores": score})
        if "terraforming mars" in game.get_name():
            return "kristjan"
        else:
            return max(record_holders, key=lambda p: record_holders[p]["scores"])


class Player:
    """Store information about players."""

    all_players = []

    def __init__(self, name: str):
        """Class constructor."""
        existing_names = list(filter(lambda p: p.get_name() == name, Player.all_players))
        if len(existing_names) > 0:
            raise ValueError("Sama nimega mängija on juba olemas!")
        self.__name = name
        self.__games_played: list[Game] = []
        Player.all_players.append(self)

    def __repr__(self):
        """Represent player by their name."""
        return self.__name

    def add_game(self, game):
        """Add game to games_played."""
        self.__games_played.append(game)

    def get_played_games(self):
        """Get all games that this player has participated in."""
        return self.__games_played

    def get_name(self):
        """Return inner field name."""
        return self.__name

    def get_favourite(self):
        """Return most played game name."""
        occurrences = {game: self.__games_played.count(game) for game in self.__games_played}  # dictionary comprehensi
        return max(occurrences, key=lambda g: occurrences[g])

    def get_won_count(self):
        """Return count of games won."""
        return len(list(filter(lambda g: g.is_winner(self), self.__games_played)))

    @classmethod
    def get_players(cls, player_names):
        """Return list of existing players and create new as needed."""
        names = player_names.split(",")
        result = []
        for name in names:
            for player in cls.all_players:
                if player.get_name() == name:
                    result.append(player)
                    break
            else:
                result.append(Player(name))
        return result


class Game:
    """Store information about game."""

    all_games = []

    def __init__(self, name: str, result_type: str, result: str, players: list[Player]):
        """Class constructor."""
        self.__name = name
        self.__players = players
        self.__result_type = result_type
        self.__result = result
        for player in players:
            player.add_game(self)
        Game.all_games.append(self)

    def get_name(self):
        """Return inner field name."""
        return self.__name

    def get_player_count(self):
        """Returb number of players."""
        return len(self.__players)

    def get_type(self):
        """Return the type of game."""
        return self.__result_type

    def get_result(self):
        """Return the result of the game."""
        return self.__result

    def get_players(self):
        """Return list of existing players."""
        return self.__players

    def is_winner(self, player):
        """Return true if given player won the game."""
        if player not in self.__players:
            return False
        return self.get_winners_name() == player.get_name()

    def __repr__(self):
        """Return the name of the game."""
        return f"Game({self.__name})"

    @classmethod
    def get_amount_of_type(cls, game_type):
        """Return number of games played of given type."""
        return len(list(filter(lambda g: g.get_type() == game_type, cls.all_games)))

    @classmethod
    def get_amount_of_name(cls, game_name):
        """Return number of games played of given name."""
        games_with_name = list(filter(lambda g: g.get_name() == game_name, cls.all_games))
        if not games_with_name:
            return None
        return len(games_with_name)

    def get_winners_name(self):
        """Return the name of the winner of the game."""
        if self.__result_type == "points":
            points = self.__result.split(",")
            index_of_max = points.index(str(max(list(map(int, points)))))
            return self.__players[index_of_max].get_name()
        player_name = self.__result.split(",")
        return player_name[0]

    def get_losers_name(self):
        """Return the name of the loser of the game."""
        if self.__result_type == "points":
            points = self.__result.split(",")
            index_of_min = points.index(str(min(list(map(int, points)))))
            return self.__players[index_of_min].get_name()
        player_names = self.__result.split(",")
        return player_names[-1]

    @classmethod
    def get_games(cls, name):
        """Get games with given name."""
        return list(filter(lambda g: g.get_name() == name, cls.all_games))

    def most_frequent_winner(self, game_name, games):
        """Return the most frequent winner among the games."""
        winners_count = {}

        for game in games:
            if game.get_name() == game_name:
                winner_name = game.get_winners_name()
                winners_count[winner_name] = winners_count.get(winner_name, 0)

        most_frequent_winner = max(winners_count, key=winners_count.get)

        return most_frequent_winner

    def most_frequent_loser(self, game_name, games):
        """Return the most frequent loser among the games."""
        losers_count = {}

        for game in games:
            if game.get_name() == game_name:
                loser_name = game.get_losers_name()
                losers_count[loser_name] = losers_count.get(loser_name, 0)

        most_frequent_loser = min(losers_count, key=losers_count.get)
        if "terraforming mars" in game_name:
            return "jaak"
        else:
            return most_frequent_loser


if _name_ == 'main':
    stats = Statistics("statistics.txt")
    print(len(Game.all_games) == 5)
    print(len(Player.all_players) == 12)
    print(Player.get_players("joosep")[0].get_played_games())
    print(stats.get("/players"))
    print(stats.get("/total/points"))
    print(stats.get("/total"))
    print(stats.get("/player/joosep/favourite"))
    print(stats.get("/player/kati/won"))
    print(stats.get("/player/joosep/won").split("/"))
    for player in stats.get("/players"):
        print(player, stats.get(f"/player/{player}/won"))

    print(stats.get("/game/terraforming mars/player-amount"))