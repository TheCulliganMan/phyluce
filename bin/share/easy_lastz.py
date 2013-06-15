#!/usr/bin/env python
# encoding: utf-8

"""
easy_lastz.py

Created by Brant Faircloth on 24 March 2010 23:09 PDT (-0700).
Copyright (c) 2010 Brant Faircloth. All rights reserved.
"""

import pdb
import sys
import os
import time
import argparse
from phyluce import lastz
from phyluce.helpers import FullPaths

#import pdb


def get_args():
    """Get arguments from CLI"""
    parser = argparse.ArgumentParser(
        description="""Run lastz in an easy way"""
    )
    parser.add_argument(
        "--target",
        required=True,
        type=str,
        action=FullPaths,
        help="""The path to the target file (2bit/fasta)"""
    )
    parser.add_argument(
        "--query",
        required=True,
        type=str,
        action=FullPaths,
        help="""The path to the query file (2bit/fasta)"""
    )
    parser.add_argument(
        "--output",
        required=True,
        type=str,
        action=FullPaths,
        help="""The path to the output file"""
    )
    parser.add_argument(
        "--identity",
        type=float,
        default=92.5,
        help="""The minimum percent identity to require for a match"""
    )
    cov_or_match = parser.add_mutually_exclusive_group(required=False)
    cov_or_match.add_argument(
        "--coverage",
        type=float,
        default=83.0,
        help="""The minimum coverage (%) required for a match"""
    )
    cov_or_match.add_argument(
        "--min_match",
        type=int,
        default=None,
        help="""The minimum number of base pairs required for a match"""
    )
    return parser.parse_args()


def main():
    start_time      = time.time()
    print 'Started: ', time.strftime("%a %b %d, %Y  %H:%M:%S", time.localtime(start_time))
    options, arg    = interface()
    alignment = lastz.Align(options.target, options.query, options.coverage, \
        options.identity, options.output)
    lzstdout, lztstderr = alignment.run()
    if lztstderr:
        raise IOError(lztstderr)
    end_time        = time.time()
    print 'Ended: ', time.strftime("%a %b %d, %Y  %H:%M:%S", time.localtime(end_time))
    print 'Time for execution: ', (end_time - start_time)/60, 'minutes'

if __name__ == '__main__':
    main()

