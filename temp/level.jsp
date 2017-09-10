<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<%@ page contentType="text/html;Charset=UTF-8" %>
<head>
    <link rel="stylesheet" href="css/index.css" />
    <script type="text/javascript" src="js/jquery1.5.js"></script>
	<title>锐安金融</title>
</head>
<body>
  <div class="head">
    <h1>锐安金融分析项目</h1>
    <h2>资金人层级关系展示<span>Capital Source</span></h2>
  </div>
  <div class="ralation">
        <div class="r_head clear">
          <div class="fl">
            <h3>资金人关系信息</h3>
            <p>Relation network</p>
          </div>
          <a  href="index.jsp" class="sql_btn fr" />返回</a>
        </div>
        <div class="r_pea_bg">
            <div class="father">
                <div class="fatheruser">
                    <p class="blue">资金人姓名：<span id="user_father" style="margin-right:83px"></span> 资金人账号：<%=request.getParameter("account")%></p>
                    <p>
                        <span>最近交易时间：<i id="lastTrade">2013-10-11</i></span>
                        <span>资金总收入：<i id="Income"><%=request.getParameter("income")%></i></span>
                        <span>资金总支出：<i id="Income"><%=request.getParameter("outcome")%></i></span>
                    </p>
                    <div class="r_page">
                        <a href="#" class="a1 page-dis" id="pageUp"><img src="img/san_left.png" alt="" /></a>
                        <a href="#" class="a2" id="pageDown"><img src="img/san_right.png" alt="" /></a>
                    </div>
                </div>
                </div>
            <div class="son_bg">
                <div class="sons clear">
                    
                </div>
            </div>
        </div>
  </div>
<script type="text/javascript">
	//页面加载chuangjian 
	var tradeName = randomName();
	$("#user_father").html(tradeName);
	createLevelFa();
    function createLevelFa()
    {
        var user_father = $("#user_father").html();
        var newfather = $('<div class="son">'+
                            '<div class="sontop clear">'+
                              '<div class="fl">'+
                                '<i class="num">01</i> '+
                                '<span class="grayB">'+user_father+'</span>'+
                              '</div>'+
                              '<a href="#" class="sel fr showSon">▼</a>'+
                            '</div>'+
                            '<ul class="sonlist">'+
                            '</ul>'+
                            '<div class="sonfoot">'+
                              '<p>共 <span class="blue">20</span> 个用户</p>'+
                            '</div>'+
                          '</div>');
        newfather.appendTo(".sons");
        var lison = "";
        var liLen = Math.round(Math.random()*10)+8;
        //if (liLen == 0) {
            //liLen = 1;
        //}
        for (var i = 0; i < liLen; i++) {
            lison += '<li><a href="#">'+
                        '<p>'+randomName()+'</p>'+
                        //'<p>'+i+'</p>'+
                        '<p class="gray">总支出：<span>'+randomNum(1, 30)+'</span> 万</p>'+
                        //'<p class="gray">总支出：<span>'+i+'</span> 万</p>'+
                      '</a></li>';
        }
        newfather.children(".sonlist").html(lison);
        
    }
    $(document).ready(function(){
        var $sona = $(".sonlist li a");
        $sona.live("click",function(){
            var no = $(".son").index($(this).parents(".son"));//当前索引值
            var num = no + 2;
            if (num < 10) {
                num = "0" + num;
            }
            //获取下级用户的名称
            var user = $(this).children("p").eq(0).html();
            
            //给该标签高亮显示
            $(this).parents(".sonlist").children("li").removeClass("select");
            $(this).parent("li").addClass("select");
            
            //新增标签
            var newson = $('<div class="son">'+
                            '<div class="sontop clear">'+
                              '<div class="fl">'+
                                '<i class="num">'+num+'</i> '+
                                '<span class="grayB">'+user+'</span>'+
                              '</div>'+
                              '<a href="#" class="sel fr showSon">▼</a>'+
                            '</div>'+
                            '<ul class="sonlist">'+
                            '</ul>'+
                            '<div class="sonfoot">'+
                              '<p>共 <span class="blue">20</span> 个用户</p>'+
                            '</div>'+
                          '</div>');
            $(".son:gt("+no+")").remove();//先将其右边的资金人信息移除
            $(this).parents(".son").after(newson);
            
            //循环将内容输出
            var lison = "";
            var liLen = Math.round(Math.random()*10);
            if (liLen == 0) {
                liLen = 1;
            }
            for (var i = 0; i < liLen; i++) {
                lison += '<li><a href="#">'+
                            '<p>'+randomName()+'</p>'+
                            //'<p>'+i+'</p>'+
                            '<p class="gray">总支出：<span>'+randomNum(1, 30)+'</span> 万</p>'+
                            //'<p class="gray">总支出：<span>'+i+'</span> 万</p>'+
                          '</a></li>';
            }
            newson.children(".sonlist").html(lison);
            
            /*每增加一列层级信息时，其宽度应该增加200px*/
            var lastNum = $(".son").length;
            var sWidth = lastNum*235;
            
            $(".sons").css({
                "width" : sWidth+"px"
            });
            return false;
        });
    });
    function randomName() {
			var nameList = new Array(
				"丁聪华", "夏潇琦", "曾帛员", "韩　松",
				"孙蝶妃", "江浩华", "田宇旺", "孔良超",
				"许娇翔", "庞　妍", "陈莲眉", "冉迪振",
				"崔子希", "曹娅娴", "张　红", "陈寿渊",
				"樊瑶芳", "唐亚升", "马桂蓓", "徐经岚",
				"阮恭琴", "任　希", "孙　花", "赵美珍",
				"姚道益", "汪冰蕴", "何　彦", "米泽升",
				"朱咏娴", "陆银兴", "宋牡馨", "邓材民",
				"郭秀晶", "康天鹏", "钱亚凤", "龚蓝莹",
				"古　璐", "严秋伶", "范　坤", "阮　龙",
				"袁庆轩", "曹欣丹", "田婕灵", "程杏倚",
				"戴　敏", "顾良龙", "熊月辰", "许永岚",
				"邹　雁", "程双民", "陆道根", "寇瑞生",
				"马庆炳", "龚元才", "黄敬甫", "魏怡玉",
				"孔睫薇", "崔喻晶", "阮菊斐", "康　晓",
				"江　斌", "曾　勇", "孔　苇", "冯添桂",
				"伍兆斌", "方艾健", "米希雨", "王瑶伶",
				"成萍娴", "余卓超", "严登武", "宋安璨",
				"江美婕", "谢晓香", "杨甚璨", "郑前岚",
				"樊革民", "伍一雨", "吴潇凤", "周　益",
				"寇　荔", "毛倚娴", "樊　颖", "沈天根",
				"吴均武", "冉欣彦", "罗　娟", "孟家鹏",
				"叶致玉", "陆　琴", "米　昆", "蒋瑜馨",
				"钱富武", "钟苇娇", "唐远先", "钱嘉澜",
				"赵　竣", "孔静香", "井　剑", "蒋天振"
			);
			return nameList[randomNum(0, nameList.length-1)];
	    }
	    function randomNum(low, high) {
	    	var range = high - low;
	    	return Math.round(Math.random() * range + low);
	    }
  </script>
  
    <script type="text/javascript">
	    $(document).ready(function(){
	        var now = 0;
	        $("#pageDown").click(function(){
	            var $parent = $(this).parents(".r_pea_bg");//根据当前元素获取父元素
	            var $v_show = $parent.find(".sons");
	            var $v_con  = $parent.find(".son_bg");
	            var v_width = $v_con.width();
	            var v_len   = Math.ceil($v_show.find(".son").length / 4);
	            $(this).siblings().removeClass("page-dis");
	            if (now >= v_len-1) {
	                now = v_len-1;
	            } else {
	                $v_show.animate({left:"-="+v_width+"px"},"slow");
	                now++;
	            }
	            if (now == v_len-1) {
	                $(this).addClass("page-dis");
	            }
	            return false;
	        });
	        $("#pageUp").click(function(){
	            var $parent = $(this).parents(".r_pea_bg");//根据当前元素获取父元素
	            var $v_show = $parent.find(".sons");
	            var $v_con  = $parent.find(".son_bg");
	            var v_width = $v_con.width();
	            var v_len   = $v_show.find(".son").length;
	            
	            $(this).siblings().removeClass("page-dis");
	            if (now <= 0) {
	                now = 0;
	            } else {
	                $v_show.animate({left:"+="+v_width+"px"},"slow");
	                now--;
	            }
	            if (now == 0) {
	               $(this).addClass("page-dis"); 
	            }
	            return false;
	        });
	    });
	</script>
	<script type="text/javascript">
	  $(document).ready(function(){
	    $("body").click(function(){
	        $(".choose").css("display","none");
	    });
	    $(".showSon").click(function(e){
	        var chooseUl = "";
	        var $Ulen = $(this).siblings("ul").length;
	        
	        if ($Ulen > 0) {
	            $(this).siblings("ul").toggle();
	        } else{
	            chooseUl =  $('<ul class="choose" onclick="stopPop(event)">'+
	                          '<li class="icon-money">按金额筛选用户</li>'+
	                          '<ol>'+
	                            '<li><a href="#">小于50万</a></li>'+
	                            '<li class="sel"><a href="#">50万~100万</a></li>'+
	                            '<li><a href="#">100万~200万</a></li>'+
	                            '<li><a href="#">200万~500万</a></li>'+
	                            '<li><a href="#">大于500万</a></li>'+
	                          '</ol>'+
	                          '<li class="icon-user"><a href="#">所有用户</a></li>'+
	                        '</ul>');
	            chooseUl.appendTo(this.parentNode);
	        }
	        return false;
	    });
	  });
	  function stopPop(e)
	  {
	    if (e && e.stopPropagation) { //非IE浏览器 
	    	e.stopPropagation(); 
	    } else {  //IE浏览器 
	        window.event.cancelBubble = true; 
	    } 
	  }
	</script>
</body>
</html>