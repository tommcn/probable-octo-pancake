window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
    startTime();
});


function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('time').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
    var days = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    var months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"];
    mm = months[today.getMonth()]
    d = today.getDate()
    y = today.getFullYear()
    da = days[today.getDay()];
    document.getElementById("date").innerHTML = 
    da + " " + d + " " + mm + " " + y;
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

function isInFuture(date) {
    var cur = new Date()
    var check = new Date(date)
    return cur.getTime() < check.getTime()
}

function changeDates() {
    var list = document.getElementById("classes");
    var childs = list.childNodes
    for (var i = 1; i <= childs.length; i++)
    {
        console.log(childs[i].childNodes[1])
        console.log(isInFuture(childs[i].childNodes[1].dataset.date))
    }
}
