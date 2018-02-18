#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all generate_index.py doc
'''

import sys
import warnings
import os
import generate_sidebar
from generate_sidebar import generate_sidebar

divider_direc = '|----'
divider_file  = '|____'
divider_blank = '|    '


def write_to_file(content,output_dir):
    html_head = '''
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<title>xi's tree</title>
	<style type="text/css">
	body{
		margin: 4px;
		padding: 0;
		font-size: 14px;
		font-family: serif, arial;
		background: #fff;
	}
	ul{
		margin: 4px;
		padding: 0 0 0 14px;
	}
	
	a:link { 
	color:#FF0000; 
	text-decoration:underline; 
	} 
	a:visited { 
	color:#00FF00; 
	text-decoration:none; 
	} 
	a:hover { 
	color:#000000; 
	text-decoration:none; 
	} 
	a:active { 
	color:#0000FF; 
	text-decoration:none; 
	} 
	</style>
</head>
<body>
<pre><code>

'''
    html_tail = '''
    
    </code>
</pre>

</body>
</html>
'''
    with open(output_dir+ os.path.sep + 'global_tree.html','w') as f:
        f.writelines(html_head+content+html_tail);


def generate_tree(info,output_dir):
    # print info

    content = ''
    for path in info:
        pat = path[0]
        char = path[1]
        pat_div = pat.split(os.path.sep)

        level = len(pat_div) - 1
        ss = ''

        if pat == './global_tree.html' or pat == './global_sidebar.html' or pat == './top.html':
            continue;

        if char == 'dir':
            ss = divider_blank * (level -1) + divider_direc + pat_div[-1]
        else:
            ps = os.path.splitext(pat_div[-1])
            ext = ps[1]
            if 'html' in ext or 'pdf' in ext:
                ss = divider_blank * (level - 1) + \
                     divider_file + \
                     "<a href='" + pat + "'>"+\
                     pat_div[-1] +\
                    "</a>"
            else:
                continue;
                ss = divider_blank * (level -1) + divider_file + pat_div[-1]

        content = content + ss + '\n';

    write_to_file(content,output_dir)
    print '[-------------------------END TO GENERATE TREE------------------------------]'

    #-------------------------------------------------------------------开始产生左侧的sidebar
    print '[-------------------------BEGIN TO GENERATE SIDEBAR-------------------------]'
    global_tree = '.' + os.path.sep + 'global_tree.html'
    generate_sidebar(global_tree, output_dir, info)
