/*回到顶部*/
$(window).scroll(function () {
    if($(window).scrollTop() >= 300) {
        $('#toTop').removeClass('hidden');
        $('#toTop').fadeIn(300);
    }else {
        $('#toTop').fadeOut(300);
    }
});

$(function(){
    $('#toTop').click(function() {
        $('html, body').animate({scrollTop: 0}, 500);
    }); 
})


// canvas
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext('2d'); //因为是平面的,所以写2d
canvas.width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
canvas.height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
function rand(min, max) {
    return parseInt(Math.random() * (max - min + 1) + min);
}

function Round() {
    //随机大小
    this.r = rand(6, 12);
    //随机位置
    var x = rand(this.r,canvas.width - this.r);//仿制超出右边界
    this.x = x<this.r ? this.r:x;
    var y = rand(this.r,canvas.height - this.r);
    this.y = y<this.r ? this.r:y;
    //随机速度
    var speed = rand(1, 3);
    this.speedX = rand(0, 4) > 2 ? speed : -speed;
    this.speedY = rand(0, 4) > 2 ? speed : -speed;

}

Round.prototype.draw = function() {
    // ctx.fillStyle = 'rgba(200,200,200,0.5)';
    ctx.fillStyle = 'pink'
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.r, 0, 2 * Math.PI, true);
    ctx.closePath();
    ctx.fill();
}

ctx.arc(this.x, this.y, this.r, 0, 2 * Math.PI, true);

Round.prototype.move = function() {
    this.x += this.speedX/10;
    if (this.x > canvas.width  || this.x < 0) {
        this.speedX *= -1;
    }
    this.y += this.speedY/10;
    if (this.y > canvas.height  || this.y < 0) {
        this.speedY *= -1;
    }
}

Round.prototype.links = function(){
    for (var i=0;i<ballobj.length;i++) {
        var l = Math.sqrt((ballobj[i].x - this.x)*(ballobj[i].x - this.x)+(ballobj[i].y - this.y)*(ballobj[i].y - this.y));
        var a = 1/l *100;
        if(l<200){
            ctx.beginPath();
            ctx.moveTo(this.x,this.y);
            ctx.lineTo(ballobj[i].x,ballobj[i].y);
            ctx.strokeStyle = 'rgba(200,200,200,'+a+')';
            ctx.stroke();
            ctx.closePath();
        }
    }
}


var ballobj = [];
function init() {
    for (var i = 0; i < 40; i++) {
        var obj = new Round();
        obj.draw();
        obj.move();
        ballobj.push(obj);
    }
}
init();

function ballmove(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    for (var i=0;i<ballobj.length;i++) {
        var ball = ballobj[i];
        ball.draw();
        ball.move();
        ball.links();
    }
    window.requestAnimationFrame(ballmove);
}
ballmove();



// var canvas = document.getElementById('canvas');
// var ctx = canvas.getContext('2d');
// var rgb = '0';      // 线条颜色值
// var extendDis = 5;   // 可超出的画布边界
// var lineDis = 80;    // 连线距离
// lineDis *= lineDis;
// canvas.width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
// canvas.height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
// var RAF = (function() {
//   return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function(callback) {
//         window.setTimeout(callback, 1000 / 60);
//       };
// })();
// // 鼠标活动时，获取鼠标坐标
// var warea = {x: null, y: null};
// window.onmousemove = function(e) {
//   e = e || window.event;
//   warea.x = e.clientX - canvas.offsetLeft;
//   warea.y = e.clientY - canvas.offsetTop;
// };
// window.onmouseout = function(e) {
//   warea.x = null;
//   warea.y = null;
// };
// // 添加粒子
// // x，y为粒子坐标，xa, ya为粒子xy轴加速度，max为连线的最大距离
// var dots = [];
// for (var i = 0; i < 200; i++) {
//   var x = Math.random() * (canvas.width + 2 * extendDis) - extendDis;
//   var y = Math.random() * (canvas.height + 2 * extendDis) - extendDis;
//   var xa = (Math.random() * 2 - 1) / 1.5;
//   var ya = (Math.random() * 2 - 1) / 1.5;
//   dots.push({
//     x: x,
//     y: y,
//     xa: xa,
//     ya: ya
//   })
// }
// // 延迟100秒开始执行动画，如果立即执行有时位置计算会出错
// setTimeout(function() {
//   animate();
// }, 100);
// // 每一帧循环的逻辑
// function animate() {
//   ctx.clearRect(0, 0, canvas.width, canvas.height);
//   bubDrawLine([warea].concat(dots));
//   RAF(animate);
// }
// /**
//  * 逐个对比连线
//  * @param ndots
//  */
// function bubDrawLine(ndots) {
//   var ndot;
//   dots.forEach(function(dot) {
//     move(dot);
//     // 循环比对粒子间的距离
//     for (var i = 0; i < ndots.length; i++) {
//       ndot = ndots[i];
//       if (dot === ndot || ndot.x === null || ndot.y === null) continue;
//       var xc = dot.x - ndot.x;
//       var yc = dot.y - ndot.y;
//       // 如果x轴距离或y轴距离大于max,则不计算粒子距离
//       if (xc > ndot.max || yc > lineDis) continue;
//       // 两个粒子之间的距离
//       var dis = xc * xc + yc * yc;
//       // 如果粒子距离超过max,则不做处理
//       if (dis > lineDis) continue;
//       // 距离比
//       var ratio;
//       // 如果是鼠标，则让粒子向鼠标的位置移动
//       if (ndot === warea && dis < 20000) {
//         dot.x -= xc * 0.01;
//         dot.y -= yc * 0.01;
//       }
//       // 计算距离比
//       ratio = (lineDis - dis) / lineDis;
//       // 粒子间连线
//       ctx.beginPath();
//       ctx.lineWidth = ratio / 2;
//       ctx.strokeStyle = 'rgba(' + rgb + ', ' + rgb + ', ' + rgb + ', 1';
//       ctx.moveTo(dot.x, dot.y);
//       ctx.lineTo(ndot.x, ndot.y);
//       ctx.stroke();
//     }
//     // 将已经计算过的粒子从数组中删除
//     ndots.splice(ndots.indexOf(dot), 1);
//   });
// }
// /**
//  * 粒子移动
//  * @param dot
//  */
// function move(dot) {
//   dot.x += dot.xa;
//   dot.y += dot.ya;
//   // 遇到边界将加速度反向
//   dot.xa *= (dot.x > (canvas.width + extendDis) || dot.x < -extendDis) ? -1 : 1;
//   dot.ya *= (dot.y > (canvas.height + extendDis) || dot.y < -extendDis) ? -1 : 1;
//   // 绘制点
//   ctx.fillStyle = 'rgba(' + rgb + ', ' + rgb + ', ' + rgb + ', 1';
//   ctx.fillRect(dot.x - 0.5, dot.y - 0.5, 1, 1);
// }

var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?d1d114373d7d0d47ff3a2ff038ca6060";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
