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

TESTS_COUNT = 10


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
parser.add_option("-q", "--quiet",
                  action="store_false", dest="visual", default=True,
                  help="Don't print visualization of results")

options, optionsValues = parser.parse_args()
TESTS_COUNT = options.tests

print "You can use flags to change simulation properties, look into --help"

"""
    Calculated values for quick statistics
"""
randomStrategyStats = [(305, 5112, 512), (313, 5204, 512), (347, 5712, 512), (136, 1436, 128), (258, 3408, 256), (742, 15000, 1024), (353, 5812, 512), (227, 3104, 256), (172, 2272, 256), (298, 4088, 256)]
simpleStrategyStats = [(408, 6872, 512), (1446, 34264, 2048), (241, 3156, 256), (1230, 27600, 2048), (864, 17044, 1024), (464, 7764, 512), (618, 12152, 1024), (675, 13636, 1024), (1062, 23952, 2048), (525, 8580, 512)]
predictableStrategyStats = [(2881, 75860, 4096), (2959, 77424, 4096), (4499, 129168, 8192), (4106, 120940, 8192), (5924, 171736, 8192), (5776, 168328, 8192), (5205, 152296, 8192), (5810, 169704, 8192), (3664, 109144, 8192), (5810, 169232, 8192)]
predictableStrategyLevelsStats = [(3009, 77904, 4096), (2303, 59204, 4096), (5672, 167468, 8192), (3657, 108616, 8192), (5866, 170240, 8192), (4416, 127852, 8192), (8131, 262176, 16384), (4096, 120352, 8192), (1549, 35508, 2048), (4365, 127308, 8192), (3003, 78004, 4096), (3587, 107420, 8192), (2946, 77596, 4096), (2990, 78220, 4096), (5716, 167580, 8192), (3016, 78200, 4096)]

def printStats(attempt=None, stats = None):
    if attempt is not None:
        print str(attempt) + '.',
    if stats is not None:
        print 'moves:', str(stats[0]).ljust(7, ' '),
        print 'score:', str(stats[1]).ljust(7, ' '),
        print 'largest:', str(stats[2]).ljust(7, ' ')

if options.random or options.all:
    print
    print 'Random strategy:'

    randomStrategyStats = []
    for i in xrange(TESTS_COUNT):
        game = Game()
        randomStrategy = RandomStrategy(game)
        randomStrategy.play()

        stats = game.getStats()
        printStats(i + 1, stats)
        randomStrategyStats.append(stats)

if options.simple or options.all:
    print
    print 'Simple strategy:'

    simpleStrategyStats = []
    for i in xrange(TESTS_COUNT):
        game = Game()
        simpleStrategy = SimpleStrategy(game)
        simpleStrategy.play()

        stats = game.getStats()
        printStats(i + 1, stats)
        simpleStrategyStats.append(stats)

if options.predictable or options.all:
    print
    print 'Predictable strategy'

    predictableStrategyStats = []
    for i in xrange(TESTS_COUNT):
        game = Game()
        predictableStrategy = PredictableStrategy(game)
        predictableStrategy.play()

        stats = game.getStats()
        printStats(i + 1, stats)
        predictableStrategyStats.append(stats)

if options.levels:
    print
    print 'Predictable strategy levels'

    predictableStrategyLevelsStats = []
    for level in xrange(1, 5):
        print 'Level ' + str(level)
        for i in xrange(TESTS_COUNT):
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

    plt.figure(1)
    plt.subplot(131)
    plt.title('Random strategy')
    plt.plot(randomStrategyStats, 'o:')
    plt.ylim((0, 160000))

    plt.subplot(132)
    plt.title('Simple strategy')
    plt.plot(simpleStrategyStats, 'o:')
    plt.ylim((0, 160000))

    plt.subplot(133)
    plt.title('Predictable strategy')
    plt.plot(predictableStrategyStats, 'o:')
    plt.ylim((0, 160000))

    try:
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
    except:
        print "Unexpected error.."
    
    plt.show()

    fig = plt.figure(2)

    predictableStrategyLevelsAvgStats = []
    predictableStrategyLevelsAvgStats.append(0)
    for level in xrange(1, 5):
        a = 0
        for i in xrange(4):
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
        print "Unexpected error.."
    
    plt.show()
