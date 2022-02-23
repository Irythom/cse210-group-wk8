from game.casting.actor import Actor

class Stone( Actor ):
    """
    A type of stone or gem. 
    
    The responsibility of a Stone is add or sum points to the player's score when the player touch it.

    Attributes:
        _points ( int ): The points that every Stone will give.
    """
    def __init__( self ):
        super().__init__()
        self._points = 0

    def set_points( self, points ):
        """Updates the points to the given one.
        
        Args:
            points ( int ): The given points.
        """
        self.points = points
    
    def get_points( self ):
        """Updates the score.
        
        Args:
            points ( int ): The points to add.
        """
        return self._points