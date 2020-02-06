import GameTextAdventure


where = GameTextAdventure.Contents('wintickets')
play = GameTextAdventure.Engine(where)
play.go()
