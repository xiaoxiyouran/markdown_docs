#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
useage: python -W all main.py src docs
'''

import sys
import warnings

import os

import shutil
import time

sys.path.append('markdown');
from markdown import __main__

import generate_index
from generate_index import generate_index

def file_put_contents(relative_file_name, html):
    with open(relative_file_name,'w') as f:
        f.writelines(html); # 大概一次写入200M 的文件



def outBytemplate(template,outputFileName,markdown):
    # print template
    fRead = open(template,'r');
    fWrite = open(outputFileName,'w')
    # print markdown
    for s in fRead.readlines():
        s = s.replace('$title$',markdown['title'])
        s = s.replace('$base_url$',markdown['base_url'])
        s = s.replace('$html$',markdown['html'])
        fWrite.writelines(s)
    fRead.close()
    fWrite.close()


def default_template(markdown):
    html_header = '''
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

	<title>$title$</title>
	<meta name="keywords" content="xiaoxiyouran" />
	<meta name="description" content="xiaoxiyouran's Docs" />
	<link href="$base_url$/packages/css/bootstrap.min.css" rel="stylesheet" />
	<link href="$base_url$/packages/css/style.css" rel="stylesheet" />
	<link href="$base_url$/packages/css/monokai_sublime.min.css" rel="stylesheet">
	<!--
	<link href="<?php echo $base_url?>/css/bootstrap-theme.min.css" rel="stylesheet" />
	-->
	
	<!-- To generate the side tree of the document itself. -->
  <link rel="stylesheet" href="$base_url$/packages/generate_header_sidebar/css/zTreeStyle/zTreeStyle.css" type="text/css">
  <style>
  body {
  background-color: white;
  margin:0; padding:0;
  // text-align: center;
  overflow: scroll;
  }
  div, p, table, th, td {
    list-style:none;
    margin:8px; padding:0;
    color:#333; font-size:12px;
    font-family:dotum, Verdana, Arial, Helvetica, AppleGothic, sans-serif;
  }
  .ztree li a.curSelectedNode {
    padding-top: 0px;
    background-color: #FFE6B0;
    color: black;
    height: 16px;
    border: 1px #FFB951 solid;
    opacity: 0.8;
  }
  .ztree{
    overflow: auto;
    height:100%;
    min-height: 200px;
    top: 0px;
  }
  </style>

</head>
<body>
<TABLE border=0 height=600px align=left>
  <TR>
    <TD width=260px align=left valign=top style="BORDER-RIGHT: #999999 1px dashed">
      <ul id="tree" class="ztree">
        
      </ul>
    </TD>
    <TD width=770px align=left valign=top>

<!---------------------------------------------------------------------------------------------------------------------------->
<div class="container">
 
'''
    html_tail = '''


<hr/>
<div class="footer">
	Copyright &copy; xiaoxiyouran. All rights reserved.

</div>

</div> <!-- /container -->

<!---------------------------------------------------------------------------------------------------------------------------->

        </TD>
  </TR>
</TABLE>

<!-- 请注意，以下两个部分的代码执行是有顺序的，必须严格按照这个顺序来。另外，放在底部是为了优化界面，使加载速度更快 -->
<!-- 为了优化代码风格 -->
<script src="$base_url$/packages/js/jquery-1.9.1.min.js" ></script>
<script src="$base_url$/packages/js/bootstrap.min.js" ></script>
<script src="$base_url$/packages/js/highlight.min.js" ></script>
<script >hljs.initHighlightingOnLoad();</script>

<!-- 以下是为了生成文档的侧边栏 -->
<script type="text/javascript" src="$base_url$/packages/generate_header_sidebar/js/jquery-1.4.4.min.js"></script>
<script type="text/javascript" src="$base_url$/packages/generate_header_sidebar/js/jquery.ztree.core-3.5.js"></script>
<script type="text/javascript" src="$base_url$/packages/generate_header_sidebar/src/ztree_toc.js"></script>

<SCRIPT type="text/javascript" >
<!--
$(document).ready(function(){
  $('#tree').ztree_toc({
    is_auto_number : true,
    use_head_anchor: true
  });
});
//-->
</SCRIPT>

</body>
</html>
    '''
    html_header = html_header.replace('$title$', markdown['title'])
    html_header = html_header.replace('$base_url$', markdown['base_url'])

    html_tail = html_tail.replace('$base_url$', markdown['base_url'])

    return html_header + markdown['html'] + html_tail



# file src/aa/ab.md
# output_dir docs/aa
def gen_doc(file,output_dir, template=None, base_url=''):
    unModified = True
    base_name = os.path.basename(file)    # src/aa/ab.md => ab.md
    name = os.path.splitext(base_name)[0] # aa.md ==> ab
    markdown={
        'name' : name,
        'input_file' : file,
        'output_file' : output_dir + os.path.sep + name + '.html',
        'title': '',
        'html' : '',
        'base_url': base_url
    };


    if os.path.isfile(markdown['output_file']) and (time.ctime(os.stat(file).st_mtime) < time.ctime(os.stat(markdown['output_file']).st_ctime)):
        print "[skip] " + markdown['input_file'] + "=>" + markdown['output_file'];
        return unModified;

    unModified = unModified and False;
    in_comment = False;
    with open(file, 'r') as f:
        cnt = 0
        for line in f.readlines():
            line = line.strip()  # 把末尾的'\n'删掉
            if line != '':
                if line[0] == '`':
                    if in_comment:
                        in_comment = False;
                    else:
                        in_comment = True;
                else:
                    cnt = cnt + 1   # 非注释

                if cnt < 20:
                    if line[0] == '#' and line[1] != '#' and (not in_comment):
                        line = line.strip()
                        line = line.strip('#')
                        line = line.strip()
                        markdown['title'] = line;
                        break;
                else:
                    break

    fflname = os.path.split(file)
    flname = fflname[-1]
    ext = os.path.splitext(flname)[-1]
    flname = flname.rstrip(ext)  # 删除尾部的扩展名字

    if markdown['title'] == '':
        markdown['title'] = flname

    try:
        markdown['html'] = __main__.called(file,'return')
    except UnicodeDecodeError:
        print 'UnicodeDecodeError==============================================================================================================>' \
              + file
    except:
        print 'OtherError======================================================================================================================>' \
              + file

    html = ''
    if template:
        print "[build] "+ markdown['input_file'] + "=>" + markdown['output_file'];
        outBytemplate(template,markdown['output_file'],markdown);
    else:
        html = default_template(markdown);
        print "[buildDefaultTemplate] "+ markdown['input_file'] + "=>" + markdown['output_file'];
        file_put_contents(markdown['output_file'],html)

    return unModified

def parse_dir(input_dir, output_dir,isDectionaryDefault = True,base_url='.'):
    unModified = True
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    template = input_dir+os.path.sep+"template.php"
    if not os.path.isfile(template):
        template = None # if template == None


    for file in os.listdir(input_dir):
        full_path = input_dir+os.path.sep+file;


        if os.path.isdir(full_path):
            if 'unmd' in full_path:
                continue

            if isDectionaryDefault and full_path == '../packages':
                continue;


            if isDectionaryDefault and full_path == '../output':
                new_output_dir = output_dir

            else:
                new_output_dir = output_dir + os.path.sep + file

            unModified_tmp = parse_dir(full_path,new_output_dir, isDectionaryDefault, base_url + os.path.sep + "..");
            unModified = unModified and unModified_tmp
        else:
            # print base_url
            ps = os.path.splitext(file)
            ext = ps[1]
            if 'md' in ext:
                unModified_tmp = gen_doc(full_path,output_dir,template,base_url);
                unModified = unModified and unModified_tmp
            elif not ('php' in ext):
                # 1. 原文件没有修改跳过  2. 自己复制给自己，跳过
                if (os.path.isfile(output_dir + os.path.sep + file) and (time.ctime(os.stat(full_path).st_mtime) < time.ctime(os.stat(output_dir + os.path.sep + file).st_ctime)) ) or \
                        (full_path == (output_dir + os.path.sep + file)):
                    print "[skipcopy] " + full_path + " => " + (output_dir + os.path.sep + file)

                # 1. 如果输出文件存在，原文件不存在，输出文件删除 2. 输出文件存在，原文件也存在，更新
                elif os.path.isfile(output_dir + os.path.sep + file):
                    unModified = unModified and False
                    delete = False;
                    if os.path.isfile(output_dir+os.path.sep+file):
                        os.remove(output_dir + os.path.sep + file)
                        delete = True;
                    if os.path.isfile(full_path):
                        shutil.copy(full_path,output_dir + os.path.sep + file ); # copy file or directory
                        delete = False

                    if delete is True:
                        print "[deletecopy] " + full_path + " => " + (output_dir + os.path.sep + file)
                    else:
                        print "[updatecopy] " + full_path + " => " + (output_dir + os.path.sep + file)

                # 输出文件不存在，从原文件那里创建
                else:                             # 从原文件创建也要保证源文件存在
                    if os.path.isfile(full_path):
                        shutil.copy(full_path,output_dir + os.path.sep + file ); # copy file or directory
                    print "[createcopy] " + full_path + " => " + (output_dir + os.path.sep + file)
                    unModified = unModified and False

    return unModified

if __name__=='__main__':
    # print '参数个数为:', len(sys.argv), '个参数。'
    # print '参数列表:', str(sys.argv)

    args = str(sys.argv)
    isDectionaryDefault = True;
    if len(sys.argv) == 3:  #
        isDectionaryDefault = False
        input_dir = sys.argv[1];
        output_dir = sys.argv[2];
    else:
        warnings.warn('You do not input a src file and output file! default--. and output will be used', DeprecationWarning);
        input_dir = "..";
        output_dir = "../output"


    # 去除首位空格
    input_dir = input_dir.strip()
    output_dir = output_dir.strip()
    # 去除尾部 \ 符号
    input_dir = input_dir.rstrip("\\")
    output_dir = output_dir.rstrip("\\")

    output_dir_copy = output_dir

    unModified = True
    unModified_tmp = parse_dir(input_dir,output_dir,isDectionaryDefault,base_url='..');

    unModified = unModified and unModified_tmp

    if not unModified:
        if not isDectionaryDefault:
            generate_index(output_dir_copy)
        else:
            generate_index()
    else:
        print '[-------------------------SKIP TO GENERATE INDEX-------------------------]'


