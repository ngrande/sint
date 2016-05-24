import argparse
import io
from searcher import Searcher


args_parser = argparse.ArgumentParser(description='Search all files in a '
                                      'directory (including subdirectories) '
                                      'for a regex pattern')
args_parser.add_argument('-p', '--regex-pattern', help='regex pattern to '
                         'search for in the files in the directory',
                         required=True)
args_parser.add_argument('-o', '--output-file', nargs='?', help='output file '
                         'with matching lines (will be created after script '
                         'finished)', default='matches.txt', type=str)
args_parser.add_argument('-d', '--directory', nargs='?', type=str,
                         help='directory of files which will be scanned',
                         default='./')
args_parser.add_argument('-l', '--deactivate-live-output', help='This '
                         'argument turns off the live output'
                         'of a file in the console', action='store_false',
                         default=True)
args = args_parser.parse_args()

live_output = args.deactivate_live_output
matching_lines = Searcher().search_for_pattern_async(args.directory,
                                                     args.regex_pattern)


print('#### found {0!s} matching line(s) ####'.format(len(matching_lines)))
if len(matching_lines) > 0:
    with open(args.output_file, 'w+') as file:
        for line in matching_lines:
            file.writelines(line)
