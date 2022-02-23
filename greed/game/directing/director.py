from game.casting.stone import Stone
from game.shared.point import Point
from game.shared.color import Color
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service ( KeyboardService ): For getting directional input.
        _video_service ( VideoService ): For providing video output.
    """

    def __init__( self, keyboard_service, video_service ):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service ( KeyboardService ): An instance of KeyboardService.
            video_service ( VideoService ): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game( self, cast ):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast ( Cast ): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs( cast )
            self._do_updates( cast )
            self._do_outputs( cast )
        self._video_service.close_window()

    def _get_inputs( self, cast ):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast ( Cast ): The cast of actors.
        """

        # Get direction to move from keyboard service.
        player = cast.get_first_actor( "player" )
        velocity = self._keyboard_service.get_direction()
        player.set_velocity( velocity )

    def _do_updates( self, cast ):
        """Updates the player's position and resolves any collisions with stones( gems and rocks ).
        
        Args:
            cast ( Cast ): The cast of actors.
        """
        # Colors
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        # Create the gems.
        gem = Stone()
        gem.set_text( "*" )
        gem.set_points( 1 )
        gem.set_velocity( Point( 0,5 ) )
        gem.set_position( Point( random.randint( 15, 885 ),15 ) )
        gem.set_color( color )
        cast.add_actor( "stones", gem )

        # Create the rocks.
        rock = Stone()
        rock.set_text( "O" )
        rock.set_points( -1 )
        rock.set_velocity( Point( 0,5 ) )
        rock.set_position( Point( random.randint( 15, 885 ),15 ) )
        rock.set_color( color )
        cast.add_actor( "stones", rock )

        # Move the cast.
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player = cast.get_first_actor( "player" )
        player_x = player.get_position().get_x()
        player_y = player.get_position().get_y()
        score = cast.get_first_actor( "score" )

        for actor in cast.get_actors( "stones" ):
            actor.move_next(max_x, max_y)
            
            # Check for touches.
            if actor.get_text() == "*":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()
                if ( ( player_x - 10 < actor_x < player_x + 10 ) and ( player_y - 10 < actor_y < player_y + 10 ) ):
                    score.add_points( 1 )
                if actor_y > max_y - 30 or( ( player_x - 10 < actor_x < player_x + 10 ) and ( player_y - 10 < actor_y < player_y + 10 ) ):
                    cast.remove_actor( "stones", actor )
                    
            elif actor.get_text() == "O":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()
                if ( ( player_x - 10 < actor_x < player_x + 10 ) and ( player_y - 10 < actor_y < player_y + 10 ) ):
                    score.add_points(-1)
                if actor_y > max_y - 30 or ( ( player_x - 10 < actor_x < player_x + 10 ) and ( player_y - 10 < actor_y < player_y + 10 ) ):
                    cast.remove_actor( "stones", actor )
                    
        # Move player.
        player.move_next( max_x, max_y )
        
    def _do_outputs( self, cast ):
        """Draws the actors on the screen.
        
        Args:
            cast ( Cast ): The cast of actors.
        """
        self._video_service.clear_buffer()
        player = cast.get_first_actor( "player" )
        score = cast.get_first_actor( "score" )
        score.set_text( f"SCORE: {score.get_points()}" )

        for actor in cast.get_actors( "stones" ):
            self._video_service.draw_actor( actor )

        self._video_service.draw_actor( player )
        self._video_service.draw_actor( score )
        self._video_service.flush_buffer()