"""ASCII world game."""


class Player(object):

    """Player object with some actions (just move for now)."""

    def __init__(self):
        """Initialize coordinates."""
        self.x = 1
        self.y = 1

    def move(self, dx, dy):
        """Move player to some position.

        :param dx: How much to move in the x axis
        :type dx: int
        :param dy: Move much to move in the y axis
        :type dy: int

        """
        # Ignore invalid movements
        if (self.x + dx) < 1 or (self.y + dy) < 1:
            return

        self.x += dx
        self.y += dy


class GameMap(object):

    """GameMap that shows where the player is."""

    X_OFFSET = 4

    def render(self, player):
        """Render map and player position."""
        def render_empty_row():
            """Render row in which there is no player."""
            print('.' * (player.x + self.X_OFFSET))

        for _ in range(player.y):
            render_empty_row()

        print('{} @ {}'
              .format('.' * (player.x - 1),
                      '.' * (self.X_OFFSET / 2)))
        render_empty_row()


class Command(object):

    """Command reader from stdin."""

    # Map text command to player movement
    CMD_TO_MOVE = {
        'u': (0, -1),
        'up': (0, -1),
        'd': (0, 1),
        'down': (0, 1),
        'l': (-1, 0),
        'left': (-1, 0),
        'r': (1, 0),
        'right': (1, 0),
    }

    # Default value for unknown command
    NO_MOVE = (0, 0)

    def read(self):
        """Read command (up, down, left, right) from stdin.

        The command is converted to a movement for the player using the same
        coordinate system.

        :returns: Player movement
        :rtype: tuple(int, int)

        """
        command_str = input('> ')
        return self.CMD_TO_MOVE.get(command_str, self.NO_MOVE)


class Game(object):

    """Game object to keep state and read command for next turn."""

    def __init__(self):
        """Get all the objects needed to run the game."""
        self.player = Player()
        self.game_map = GameMap()
        self.command = Command()

    def run(self):
        """Render map and read next command from stdin."""
        while True:
            self.game_map.render(self.player)
            self.player.move(*self.command.read())

if __name__ == "__main__":
    game = Game()
    game.run()