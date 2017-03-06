// a helper mapping HTMLcollection onto iterable
function converter(htmlCollection) { return [].slice.call(htmlCollection);}

//helper leading 0
function pad(num, size) {
    var s = "00" + num;
    return s.substr(s.length-size);
}

// helpers for setting the the timer
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

    elements = ['hour', 'minute', 'second'].forEach(function(name) {
        //closure
        iterFn = function (elem,i) {
            padded = pad(response[name],2)
            elem.innerText = padded;
        }

        converter(document.getElementsByClassName(name)).forEach(iterFn);
    })
 
}

// a loaded lib from github gives the global shortcut ap for ajaxPromises
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

// re-learn no global names tricks like OO or IIFE