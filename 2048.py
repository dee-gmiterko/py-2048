#!/usr/bin/env python
# coding=utf-8

from optparse import OptionParser
from Game import Game
from PredictableStrategy import PredictableStrategy
from RandomStrategy import RandomStrategy
from SimpleStrategy import SimpleStrategy

"""
Game simulations
"""

TESTS_COUNT = 20


parser = OptionParser()
parser.add_option("-r", "--random",
                  action="store_true", dest="random", default=False,
                  help="Simulate random strategy")
parser.add_option("-s", "--simple",
                  action="store_true", dest="simple", default=False,
                  help="Simulate simple strategy")
parser.add_option("-p", "--predictable",
                  action="store_true", dest="predictable", default=False,
                  help="Simulate predictable strategy")
parser.add_option("-a", "--all",
                  action="store_true", dest="all", default=False,
                  help="Simulate all strategies")
parser.add_option("-l", "--levels",
                  action="store_true", dest="levels", default=False,
                  help="Simulate levels of predictable strategy")
parser.add_option("-t", "--tests",
                  metavar="NUMBER", type="int",
                  dest="tests", default=TESTS_COUNT,
                  help="Change count of tests runned")
parser.add_option("-d", "--display",
                  action="store_true", dest="display", default=False,
                  help="Display map after every turn")
parser.add_option("-S", "--size",
                  metavar="NUMBER", type="int",
                  dest="size", default=Game.SIZE,
                  help="Change count of tests runned")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="visual", default=True,
                  help="Don't print visualization of results")

options, optionsValues = parser.parse_args()
TESTS_COUNT = options.tests
Game.DEBUG = options.display
Game.SIZE = options.size

print("You can use flags to change simulation properties, look into --help")

strategiesStats = []
predictableStrategyLevelsStats = None

def printStats(attempt=None, stats = None):
    if attempt is not None:
        print(str(attempt) + '.', end=' ')
    if stats is not None:
        print('moves:', str(stats[0]).ljust(7, ' '), end=' ')
        print('score:', str(stats[1]).ljust(7, ' '), end=' ')
        print('largest:', str(stats[2]).ljust(7, ' '))

if options.random or options.all:
    print()
    print('Random strategy:')

    randomStrategyStats = []
    for i in range(TESTS_COUNT):
        game = Game()
        randomStrategy = RandomStrategy(game)
        randomStrategy.play()

        stats = game.getStats()
        printStats(i + 1, stats)
        randomStrategyStats.append(stats)
    strategiesStats.append(("Random strategy", randomStrategyStats))

if options.simple or options.all:
    print()
    print('Simple strategy:')

    simpleStrategyStats = []
    for i in range(TESTS_COUNT):
        game = Game()
        simpleStrategy = SimpleStrategy(game)
        simpleStrategy.play()

        stats = game.getStats()
        printStats(i + 1, stats)
        simpleStrategyStats.append(stats)
    strategiesStats.append(("Simple strategy", simpleStrategyStats))

if options.predictable or options.all:
    print()
    print('Predictable strategy')

    predictableStrategyStats = []
    for i in range(TESTS_COUNT):
        game = Game()
        predictableStrategy = PredictableStrategy(game)
        predictableStrategy.play()

        stats = game.getStats()
        printStats(i + 1, stats)
        predictableStrategyStats.append(stats)
    strategiesStats.append(("Predictable strategy", predictableStrategyStats))

if options.levels:
    print()
    print('Predictable strategy levels')

    predictableStrategyLevelsStats = []
    for level in range(1, 5):
        print('Level ' + str(level))
        for i in range(TESTS_COUNT):
            game = Game()
            predictableStrategy = PredictableStrategy(game)
            predictableStrategy.PREDICTION_LEVELS = level
            predictableStrategy.play()

            stats = game.getStats()
            printStats(i + 1, stats)
            predictableStrategyLevelsStats.append(stats)

"""
Display results
"""
if options.visual:
    import matplotlib.pyplot as plt
    import numpy

    #display graph
    import plotStyle
    
    if len(strategiesStats) > 0:
        plt.figure(1)
        
        namesPerStrategy = []
        movesPerStrategy = []
        scorePerStrategy = []
        largestTilePerStragegy = []
        
        for strategiesStat in strategiesStats:
            strategyName, stats = strategiesStat
            mean = numpy.mean(stats, axis=0)
            
            moves, score, largestTile = mean
            
            namesPerStrategy.append(strategyName)
            movesPerStrategy.append(moves)
            scorePerStrategy.append(score)
            largestTilePerStragegy.append(largestTile)
        
        xses = numpy.arange(len(movesPerStrategy))
        
        plotStyle.subplotStyle(plt.subplot(131))
        plt.title('Moves')
        plt.bar(xses, movesPerStrategy, color=plotStyle.tableau20, tick_label=namesPerStrategy, align="center")

        plotStyle.subplotStyle(plt.subplot(132))
        plt.title('Score')
        plt.bar(xses, scorePerStrategy, color=plotStyle.tableau20, tick_label=namesPerStrategy, align="center")

        plotStyle.subplotStyle(plt.subplot(133))
        plt.title('Largest tile')
        plt.bar(xses, largestTilePerStragegy, color=plotStyle.tableau20, tick_label=namesPerStrategy, align="center")

        plotStyle.style(plt)

        try:
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
        except:
            print("Unexpected error..")

        plt.show()

    if predictableStrategyLevelsStats:
        fig = plt.figure(2)

        predictableStrategyLevelsAvgStats = []
        predictableStrategyLevelsAvgStats.append(0)
        for level in range(1, 5):
            a = 0
            for i in range(4):
                m, n, s = predictableStrategyLevelsStats[(level-1) * 3 + i]
                a += s
            predictableStrategyLevelsAvgStats.append(a / 3)

        plt.title('Predictable strategy levels')
        plt.plot(predictableStrategyLevelsAvgStats, '-')
        plt.grid()

        ax = fig.gca()
        ax.set_xticks(numpy.arange(0,5,1))

        try:
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
        except:
            print("Unexpected error..")

        plt.show()
