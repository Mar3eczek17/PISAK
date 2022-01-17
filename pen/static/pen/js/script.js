window.addEventListener('load', function(){
//     function blink(btn) {
//         blink1(btn);
//     }
//     function blink1(btn1) {
//         //document.getElementById(btn1).className = ;
//         btn1.removeClass();
//         btn1.addClass("highlight");
//         setTimeout(function () { blink2(btn1); }, 750);
//     }
//
//     function blink2(btn2) {
//         //document.getElementById(btn2).className = "highlighted";
//         btn2.removeClass();
//         btn2.addClass("highlighted");
//         setTimeout(function () { blink1(btn2); }, 750);
//     }
//
//     blink($('#btn'));
    this.setInterval(a, 2000);
});
let i = -1;

function a() {
    i=(i+1)%9;
    j=i-1;
    if (i==0) {
        j=8;
    }
//    console.log(i)
//    console.log(j)
    document.getElementById(i).className = "highlight";
    document.getElementById(j).className = "highlighted";
}

document.onclick= function(event) {
    // Compensate for IE<9's non-standard event model
    //
    if (event===undefined) event= window.event;
    var target= 'target' in event? event.target : event.srcElement;

//    alert('clicked on '+target.tagName);
    if (i!=-1) {
        var text = document.getElementById('my_console').value;
        var update_text = text + document.getElementById(i).value;
        document.getElementById('my_console').value = update_text;
//        console.log(document.getElementById(i).value)
    }
};

//(()=>{
//  const console_log = window.console.log;
//  window.console.log = function(...args){
//    console_log(...args);
//    var textarea = document.getElementById('my_console');
//    if(!textarea) return;
//    args.forEach(arg=>textarea.value += `${JSON.stringify(arg)}`);
//  }
//})();

