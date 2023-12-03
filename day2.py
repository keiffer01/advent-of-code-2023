import utils

# key: color of cube, value: number of cubes
type Round = dict[str, int]
type Game = list[Round]
# key: Game ID, value: Game
type Games = dict[int, Game]

def _clean_input(input: str ) -> dict[int, list[dict[str, int]]]:
    lines = utils.read_input(day=2)
    
