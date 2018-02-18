#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
'''

import sys
import warnings
import os

import generate_tree
from generate_tree import generate_tree


def parse_dir(input_dir, info , output_header):
    dir = []
    fil = []
    for file in os.listdir(input_dir):
        full_path = input_dir + os.path.sep + file;
        if os.path.isdir(full_path):
            dir.append(full_path)
        else:
            fil.append(full_path)
    dir.sort()
    fil.sort()

    # process dicrectory firstly.
    for di in dir:
        info.append([di.replace(output_header, '.'), 'dir'])
        parse_dir(di, info, output_header)

    for fi in fil:
        ps = os.path.splitext(fi)
        ext = ps[1]
        if 'html' in ext or 'pdf' in ext:
            info.append([fi.replace(output_header,'.'),'openfile'])
        else:
            info.append([fi.replace(output_header, '.'), 'unopenfile'])


def generate_index(input_dir = None):
    print '[-------------------------BEGIN TO GENERATE INDEX---------------------------]'
    if not input_dir:
        warnings.warn('You do not input a src file and output file! default--. and output will be used',
                      DeprecationWarning);
        input_dir = "../output";
    
    # 去除首位空格
    input_dir = input_dir.strip()
    # 去除尾部 \ 符号
    input_dir = input_dir.rstrip("\\")

    output_dir = input_dir

    info = []
    output_header = output_dir
    parse_dir(input_dir, info, output_header); # 无论如何，输出都会有上一级目录存在

    print '[-------------------------BEGIN TO GENERATE INDEX---------------------------]'

    print '[-------------------------BEGIN TO GENERATE TREE----------------------------]'
    generate_tree(info,output_dir);


if __name__=='__main__':
    # print '参数个数为:', len(sys.argv), '个参数。'
    # print '参数列表:', str(sys.argv)
    args = str(sys.argv)
    if len(sys.argv) == 2:  #
        input_dir = sys.argv[1];
    else:
        warnings.warn('You do not input a src file and output file! default--. and output will be used', DeprecationWarning);
        input_dir = "../output";

    # 去除首位空格
    input_dir = input_dir.strip()
    # 去除尾部 \ 符号
    input_dir = input_dir.rstrip("\\")

    output_dir = input_dir

    info = []
    output_header = output_dir
    parse_dir(input_dir, info, output_header); # 无论如何，输出都会有上一级目录存在

    generate_tree(info,output_dir);
