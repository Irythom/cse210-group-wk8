from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 20
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed Game"
WHITE = Color( 255, 255, 255 )
YELLOW = Color( 255, 255, 0 )

def main():
    
    # Create the cast.
    cast = Cast()

    # Create the player.
    x = int( MAX_X / 2 )
    y = int( 580 )
    position = Point( x, y )

    player = Actor()
    player.set_text( "#" )
    player.set_font_size( FONT_SIZE )
    player.set_color( WHITE )
    player.set_position( position )
    cast.add_actor( "player", player )

    # Create score.
    score = Score()
    score.set_position( Point( MAX_X // 55, 15 ) )
    score.set_color( YELLOW )
    cast.add_actor( "score", score )

    # Start the game.
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game( cast )

if __name__ == "__main__":
    main()