#!/usr/bin/env python3

"""cpuid.py module description."""


import argparse
import os
import sys
from google.protobuf import text_format

CPUID_DB_DIR = '%s/proj/cpuinfo' % os.environ['HOME']
CPUID_TXT_PROTO = '%s/cpuid.database.pbtxt' % CPUID_DB_DIR

sys.path.append(CPUID_DB_DIR)
import cpuid_pb2


def read_cpudatabase():
    f = open(CPUID_TXT_PROTO, 'r')
    database = cpuid_pb2.Database()
    text_format.Merge(f.read(), database)
    f.close()
    # convert proto into dictionary
    cpuids = {}
    for implementer in database.implementer:
        cpuids[implementer.id] = {'name': implementer.name}
    for part in database.part:
        if 'part' not in cpuids[part.implementer_id]:
            cpuids[part.implementer_id]['part'] = {}
        cpuids[part.implementer_id]['part'][part.id] = {'name': part.name}
    return cpuids


default_values = {
    'debug': 0,
    'infile': None,
    'outfile': None,
}


# create poker evaluator object
# p = PokerHand()


def do_something(options):
    cpuids = read_cpudatabase()

    # open infile
    lines = []
    with open(options.infile, 'r') as fin:
        # process infile
        cpu_implementer = None
        cpu_part = None
        for line in fin.readlines():
            line = line.strip()
            if 'CPU implementer' in line:
                cpu_implementer = '0x%02x' % int(line[17:], 16)
                line += ' (%s)' % cpuids[cpu_implementer]['name']
            elif 'CPU part' in line:
                cpu_part = '0x%03x' % int(line[10:], 16)
                try:
                    line += ' (%s)' % cpuids[cpu_implementer]['part'][cpu_part]['name']
                except KeyError:
                    line += ' (unknown)'
            lines.append(line)

    # open outfile
    with open(options.outfile, 'w') as fout:
        # dump output lines
        for line in lines:
            fout.write('%s\n' % line)


def get_options(argv):
    """Generic option parser.

    Args:
        argv: list containing arguments

    Returns:
        Namespace - An argparse.ArgumentParser-generated option object
    """
    # init parser
    # usage = 'usage: %prog [options] arg1 arg2'
    # parser = argparse.OptionParser(usage=usage)
    # parser.print_help() to get argparse.usage (large help)
    # parser.print_usage() to get argparse.usage (just usage line)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
            '-d', '--debug', action='count',
            dest='debug', default=default_values['debug'],
            help='Increase verbosity (use multiple times for more)',)
    parser.add_argument(
            '--quiet', action='store_const',
            dest='debug', const=-1,
            help='Zero verbosity',)
    parser.add_argument(
            'infile', type=str,
            default=default_values['infile'],
            metavar='input-file',
            help='input file',)
    parser.add_argument(
            'outfile', type=str,
            default=default_values['outfile'],
            metavar='output-file',
            help='output file',)
    # do the parsing
    options = parser.parse_args(argv[1:])
    return options


def main(argv):
    # parse options
    options = get_options(argv)
    # get infile/outfile
    if options.infile == '-':
        options.infile = '/dev/fd/0'
    if options.outfile == '-':
        options.outfile = '/dev/fd/1'
    # print results
    if options.debug > 0:
        print(options)
    # do something
    do_something(options)


if __name__ == '__main__':
    # at least the CLI program name: (CLI) execution
    main(sys.argv)
