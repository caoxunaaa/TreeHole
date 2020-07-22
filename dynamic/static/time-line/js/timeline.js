/*
 算法思路：
 1、点击某个时间点，将该时间点上的li元素添加上active类
 2、去除上一个li上已添加的active类

 语法步骤：
 step1: 定义一个变量，记录当前已经添加active类的li的索引号
 step2: 查找所有被点击的元素对象
 step3: 查找所有li元素对象
 step4: 为每个被点击的对象绑定单击事件
 step5: 为被点击的时间点li添加active类
 step6: 根据索引号变量的值，去除上一个li的active类
 step7: 将索引号变量值更新为被点击的li的索引号

 */

window.onload = function () {
    var
        //记录当前已经添加active类的li的索引号
        curIndex = 0,

        //查找所有被点击的元素对象
        timeLine = document.getElementById("timeline"),
        clickArea = timeLine.getElementsByTagName("s"),

        //查找所有content元素对象
        timeContent = document.getElementsByClassName("content"),

        //查找所有li元素对象
        timePoint = timeLine.getElementsByTagName("li");

    timePoint[0].style.height = (timeContent[0].offsetHeight + 30) + "px";

    //为每个被点击的对象绑定单击事件
    for (var i = 0, len = clickArea.length; i < len; i++) {
        (function (i) {
            clickArea[i].onclick = function () {
                if (curIndex === i) {
                    if (timePoint[i].className === "active") {
                        timePoint[i].className = "";
                        timePoint[i].style.height = (timeContent[i].offsetHeight + 30) + "px";
                    } else {
                        timePoint[i].className = "active";
                        timePoint[i].style.height = (timeContent[i].offsetHeight + 30) + "px";
                    }
                } else {
                    //为被点击的时间点li添加active类
                    timePoint[i].className = "active";

                    //根据索引号变量的值，去除上一个li的active类
                    timePoint[curIndex].className = "";

                    //将索引号变量值更新为被点击的li的索引号
                    timePoint[curIndex].style.height = (timeContent[curIndex].offsetHeight + 30) + "px";
                    curIndex = i;
                    timePoint[i].style.height = (timeContent[i].offsetHeight + 30) + "px";
                }
                console.log(timePoint[i].offsetHeight);
                console.log(timeContent[i].offsetHeight + "px");
            };
        })(i);
    }
};