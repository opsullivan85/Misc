import NN4 as file# @UnusedImport
import cProfile  # @UnusedImport
import pstats

cProfile.run('file.main()', 'restats')
p = pstats.Stats('restats')
#p.strip_dirs().sort_stats('tottime').print_stats()
p.strip_dirs().sort_stats('time').print_stats(10)
