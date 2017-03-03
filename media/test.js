function converter(htmlCollection) { return [].slice.call(htmlCollection);}



//isolate callback into funtion for promise (see below)
function putData(response) {
    response = JSON.parse(response);
    console.log('check-in');

    iterFn = function (elem,i) {
        elem.innerText = response.minute;
        console.log(response.minute);
    }

    converter(document.getElementsByClassName('minute')).forEach(iterFn);

}

// a loaded lib from github gives the gloavl shortcut ap for ajaxPromises
function askForTime() {
  ap.get('/api/clock/now?format=json').then(putData);
}

window.onload =  function run() {
    setInterval(askForTime,60000);
}

