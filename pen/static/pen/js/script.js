window.addEventListener('load', function(){

    // function blink(btn) {
    //     blink1(btn);
    // }
    // function blink1(btn1) {
    //     //document.getElementById(btn1).className = ;
    //     btn1.removeClass();
    //     btn1.addClass("highlight");
    //     setTimeout(function () { blink2(btn1); }, 750);
    // }

    // function blink2(btn2) {
    //     //document.getElementById(btn2).className = "highlighted";
    //     btn2.removeClass();
    //     btn2.addClass("highlighted");
    //     setTimeout(function () { blink1(btn2); }, 750);
    // }

    // blink($('#btn'));


    this.setInterval(a, 2000);


});
let i = -1;

function a() {
    i=(i+1)%8;
    j=i-1;
    if (i==0) {
        j=7;
    }
    console.log(i)
    console.log(j)
    document.getElementById(i).className = "highlight";
    document.getElementById(j).className = "highlighted";

}