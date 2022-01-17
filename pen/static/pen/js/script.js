window.addEventListener('load', function(){
    this.setInterval(a, 2000);
});

let i = -1;

function a() {
    i=(i+1)%36;
    j=i-1;
    if (i==0) {
        j=35;
    }
    document.getElementById(i).className = "highlight";
    document.getElementById(j).className = "highlighted";
}

document.onclick= function(event) {
    if (event===undefined) event= window.event;
    var target= 'target' in event? event.target : event.srcElement;

    if (i!=-1 && i!=35) {
        var text = document.getElementById('my_console').value;
        var update_text = text + document.getElementById(i).value;
        document.getElementById('my_console').value = update_text;
    }

    if (i==35) {
        document.getElementById('jsform').submit();
    }
};