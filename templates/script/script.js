const loadSpinner = document.getElementById('loadSpinner');
var url;
var dir;
var acc;
var urlJson;
var dirJson;
var accJson;

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

function goSettings() {
    generateSettings();
    pywebview.api.goTo('templates/settings.html', 'JARVIS | Settings');
}

function goLogin() {
    pywebview.api.goTo('templates/login.html', 'JARVIS | Login');
}

function goDashboard() {
    pywebview.api.goTo('templates/index.html', 'JARVIS | Dashboard');
}

function generateSettings() {
    pywebview.api.loadUrl().then(saveJson);
    pywebview.api.loadDir().then(saveJson);
    pywebview.api.loadAcc().then(saveJson);
    generateTables();
}

function saveJson(response) {
    if (response.type == "url"){
        url = response.message;
        urlJson = JSON.parse(url);
    } else if (response.type == "dir") {
        dir = response.message;
        dirJson = JSON.parse(dir);
    } else {
        acc = response.message;
        accJson = JSON.parse(acc);
    }
}

function generateTables() {
    pywebview.api.printSomething(urlJson);
    pywebview.api.printSomething(dirJson[0].facebook);
    pywebview.api.printSomething(accJson);

    pywebview.api.printSomething(urlJson["Object.keys(urlJson)[0]"]);

    var table1 = document.getElementById('table1');
    var table2 = document.getElementById('table2');
    var table3 = document.getElementById('table3');

    tbl1 = document.createElement('table');
    tbl1.style.width = '100%';
    tbl1.style.border = '1px';
    tbl1.setAttribute('contenteditable', 'true');

    for (var i=0; i<Object.keys(urlJson).length; i++) {
        var row = tbl1.insertRow(i);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);

        cell1.innerHTML = Object.keys(urlJson)[0];
        cell2.innerHTML = urlJson["Object.keys(urlJson)[0]"];
    }

    table1.appendChild(tbl1);
}