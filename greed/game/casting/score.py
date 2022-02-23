from game.casting.actor import Actor


class Score( Actor ):
    """
    An item with the score of the game. 
    
    The responsibility of a Score is display a message with the score of the player.

    Attributes:
        _points ( int ): The points that the player has.
    """
    def __init__( self ):
        super().__init__()
        self._points = 0

    def get_points( self ):
        """Returns the current score.
        
        Returns:
            int: The current score.
        """
        return self._points

    def add_points( self, points ):
        """Updates the score.
        
        Args:
            points ( int ): The points to add.
        """
        self._points += points
        self.set_text( f"Score: {self._points}" )