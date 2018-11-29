var timerID;
var timerRunning = false;
var today = new Date();
var startday = new Date();
var secPerDay = 0;
var minPerDay = 0;
var hourPerDay = 0;
var secsLeft = 0;
var secsRound = 0;
var secsRemain = 0;
var minLeft = 0;
var minRound = 0;
var minRemain = 0;
var timeRemain = 0;
/* This function will stop the clock */
function stopclock() {
    if(timerRunning)
        clearTimeout(timerID);
    timerRunning = false;
}
/* This function will start the clock */
function startclock() {
    stopclock();
    showtime();
}
/* This function will display the count-up */
function showtime()
{
    // Thu Aug 9 08:51:46 2018 +0800
    startday = new Date("Aug 9, 2018 08:51:46");    // 加EDT是美国东部夏令时
    startday.setYear("2018");
    today = new Date();
    secsPerDay = 1000;
    minPerDay = 60 * 1000 ;
    hoursPerDay = 60 * 60 * 1000;
    PerDay = 24 * 60 * 60 * 1000;
    /* Seconds */
    secsLeft = (today.getTime() - startday.getTime()) / minPerDay;
    secsRound = Math.round(secsLeft);
    secsRemain = secsLeft - secsRound;
    secsRemain = (secsRemain < 0) ? secsRemain = 60 - ((secsRound - secsLeft) * 60) : secsRemain = (secsLeft - secsRound) * 60;
    secsRemain = Math.round(secsRemain);
    /* Minutes */
    minLeft = ((today.getTime() - startday.getTime()) / hoursPerDay);
    minRound = Math.round(minLeft);
    minRemain = minLeft - minRound;
    minRemain = (minRemain < 0) ? minRemain = 60 - ((minRound - minLeft) * 60) : minRemain = ((minLeft - minRound) * 60);
    minRemain = Math.round(minRemain - 0.495);
    /* Hours */
    hoursLeft = ((today.getTime() - startday.getTime()) / PerDay);
    hoursRound = Math.round(hoursLeft);
    hoursRemain = hoursLeft - hoursRound;
    hoursRemain = (hoursRemain < 0) ? hoursRemain = 24 - ((hoursRound - hoursLeft) * 24) : hoursRemain = ((hoursLeft - hoursRound) * 24);
    hoursRemain = Math.round(hoursRemain - 0.5);
    /* Days */
    daysLeft = ((today.getTime() - startday.getTime()) / PerDay);
    daysLeft = (daysLeft - 0.5);
    daysRound = Math.round(daysLeft);
    daysRemain = daysRound;
    /* Time */
    timeRemain = '<b>' + daysRemain + '</b>天<b>' + hoursRemain + '</b>小时<b>' + minRemain +
    '</b>分<b>' + secsRemain + '</b>秒';
    // document.up.face.value = timeRemain;
    $('.clock').html(timeRemain);
    timerID = setTimeout("showtime()",1000);
    timerRunning = true;
}


$(document).ready(startclock());