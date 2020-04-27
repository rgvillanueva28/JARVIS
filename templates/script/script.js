const loadSpinner = document.getElementById('loadSpinner');
var url;
var dir;
var acc;

function showResponse(response) {
    var container = document.getElementById('jarvisMessage');

    container.innerText = response.message;
    container.style.display = 'block';
    setTimeout(function () { setJarvisMessage("PRESS THE ARC REACTOR TO TALK", "hidden") }, 5000);
}

function setJarvisMessage(message, loadStatus) {
    loadSpinner.style.visibility = loadStatus;
    var container = document.getElementById('jarvisMessage');
    container.innerText = message;
}

function talkNow() {
    setJarvisMessage("DETECTING SPEECH", "visible");
    pywebview.api.talk().then(showResponse);
}

function showLoginResponse(response) {
    if (response.valid == "yes") {
        var container = document.getElementById('valid');
        document.getElementById('invalid').innerText = "";
    } else {
        var container = document.getElementById('invalid');
    }

    container.innerText = response.message;
    container.style.display = 'block';
}

function checkLogin() {
    var user = document.getElementById('uname').value;
    var passwd = document.getElementById('passwd').value;
    pywebview.api.checkCreds(user, passwd).then(showLoginResponse);
}

async function goSettings() {

    //alert(Object.keys(urlJson).length);
    pywebview.api.goTo('templates/settings.html', 'JARVIS | Settings');


}

function goLogin() {
    pywebview.api.goTo('templates/login.html', 'JARVIS | Login');
}

function goDashboard() {
    pywebview.api.goTo('templates/index.html', 'JARVIS | Dashboard');
}

function goUrl() {
    pywebview.api.goTo('templates/settingsUrl.html', 'JARVIS | URL Settings');
}

function goDir() {
    pywebview.api.goTo('templates/settingsDir.html', 'JARVIS | Directories Settings');
}

function goAcc() {
    pywebview.api.goTo('templates/settingsAcc.html', 'JARVIS | Accounts Settings');
}

function saveJson(response) {
    if (response.type == "url") {
        //url = response.message;
        url = JSON.parse(response.message);
        console.log("url isa an " + url);
        //urlJson = JSON.parse(url);
    } else if (response.type == "dir") {
        //dir = response.message;
        dir = JSON.parse(response.message);
        //console.log(dir);
        //dirJson = JSON.parse(dir);
    } else {
        acc = JSON.parse(response.message);
        //console.log(acc);
        //acc = response.message;
        //accJson = JSON.parse(acc);
    }


    //console.log(Object.keys(url).length);

    //callback();
}

async function generateTables(name) {
    if (name == "url") {
        await pywebview.api.loadUrl().then(saveJson);

        var len = Object.keys(url).length;
        //console.log(len);
        //console.log(url[Object.keys(url)[0]])



        tbl1 = document.createElement('table');

        console.log("dito");
        tbl1.setAttribute('contenteditable', 'true');
        tbl1.setAttribute('class', 'table table-striped table-bordered table-dark');



        for (var i = 0; i < len; i++) {

            console.log("odits");
            var row = tbl1.insertRow(i);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);

            cell1.innerHTML = Object.keys(url)[i];
            cell2.innerHTML = url[Object.keys(url)[i]];
            console.log(Object.keys(url)[i]);
            console.log(url[Object.keys(url)[i]]);
        }
        var stbl1 = document.getElementById("stbl");


        tblh1 = document.createElement('thead');
        tblh1.setAttribute('class', 'thead-light');
        r1 = tblh1.insertRow(0);
        d1 = r1.insertCell(0);
        d2 = r1.insertCell(1);
        d1.innerHTML = "Name";
        d2.innerHTML = "URL";
        
        tbl1.appendChild(tblh1);

        stbl.appendChild(tbl1);
       
    } else if (name == "dir") {
        await pywebview.api.loadDir().then(saveJson);

        var len = Object.keys(dir).length;
        tbl2 = document.createElement('table');

        console.log("table2");
        tbl2.style.width = '100%';
        tbl2.style.border = '1px';
        tbl2.setAttribute('contenteditable', 'true');
        tbl2.setAttribute('class', 'table table-dark');

        for (var i = 0; i < len; i++) {

            var row = tbl2.insertRow(i);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);

            cell1.innerHTML = Object.keys(dir)[i];
            cell2.innerHTML = dir[Object.keys(dir)[i]];
            console.log(Object.keys(dir)[i]);
            console.log(dir[Object.keys(dir)[i]]);
        }

        var stbl3 = document.getElementById("stblll");

        stbll.appendChild(tbl2);
    } else {
        await pywebview.api.loadAcc().then(saveJson);
        var len = Object.keys(acc).length;
        tbl3 = document.createElement('table');

        console.log("dito");
        tbl3.style.width = '100%';
        tbl3.style.border = '1px';
        tbl3.setAttribute('contenteditable', 'true');
        tbl3.setAttribute('class', 'table table-dark');

        for (var i = 0; i < len; i++) {

            console.log("odits");
            var row = tbl3.insertRow(i);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);

            cell1.innerHTML = Object.keys(acc)[i];
            cell2.innerHTML = acc[Object.keys(acc)[i]];
            console.log(Object.keys(acc)[i]);
            console.log(acc[Object.keys(acc)[i]]);
        }

        var stbl3 = document.getElementById("stblll");

        stblll.appendChild(tbl3);

    }

    console.log("dito na boss");

}