// a helper mapping HTMLcollection onto iterable
function converter(htmlCollection) { return [].slice.call(htmlCollection);}

function getConfig() {
    raw = document.getElementsByClassName('timerdata').item(0).innerText;
    obj = JSON.parse(raw);
    //obj.interval = parseInt(obj.interval);
    return obj;
}

function setColor() {
    if (timerConfig.bkgCol != "beige") {
        elem = document.getElementsByClassName('timer')[0];
        elem.style.backgroundColor = timerConfig.bkgCol;
    }
}

//isolate callback into funtion for promise (see below)
function putData(response) {
    response = JSON.parse(response);

    iterFn = function (elem,i) {
        elem.innerText = response.minute;
    }

    converter(document.getElementsByClassName('minute')).forEach(iterFn);
}

// a loaded lib from github gives the gloavl shortcut ap for ajaxPromises
function askForTime() {
  ap.get(timerConfig.restUrl).then(putData);
}


//START HERE
// multiple reliance on onload might be probelmatic

window.onload =  function run() {
    window.timerConfig = getConfig();
    setColor();
    timerConfig.timerId = setInterval(askForTime,timerConfig.interval*1000);
}

