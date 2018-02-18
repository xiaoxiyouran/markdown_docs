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
  //text-align: center;
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

$html$


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