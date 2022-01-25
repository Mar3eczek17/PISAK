var start = false;

let i = -1;

function a() {
    i=(i+1)%38;
    j=i-1;
    if (i==0) {
        j=37;
    }
    document.getElementById(i).className = "highlight";
    document.getElementById(j).className = "highlighted";
}

document.onclick= function(event) {

   if (!start) {
        setInterval(a, 500);
        start = true;
   }

    if (event===undefined) event= window.event;
    var target= 'target' in event? event.target : event.srcElement;

    if (i>=0 && i<35) {
        var text = document.getElementById('my_console').value;
        var update_text = text + document.getElementById(i).value;
        document.getElementById('my_console').value = update_text;
    }

    if (i==35) {
        document.getElementById('jsform').submit();
    }

     if (i==36) {
        document.getElementById('my_console').value = "";
    }

    if (i==37) {
        var new_text = document.getElementById('my_console').value.slice(0, -1);
        document.getElementById('my_console').value = new_text;
    }

    document.getElementById(i).className = "highlighted";
    i = -1;
};

