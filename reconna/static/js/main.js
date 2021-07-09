var screen_width = 0;

function initScreen() {
    screen_width = width = (window.innerWidth > 480) ? window.innerWidth : screen.width;
    //console.warn(screen_width)
    if (screen_width < 550) {
        var toggler = document.getElementById('toggler');
        var toggler_sm = document.getElementById('toggler-sm');
        var sidebar = document.getElementById('sidepanel');
        var mainbar = document.getElementById('mainbar-items');
        //console.warn(screen_width)
        sidebar.style.width = "0px";
        sidebar.style.marginLeft = "-10px"
        toggler_sm.style.display = "block";
        toggler.style.display = "none";
        mainbar.classList.remove("responsive-panel");
    }
}

function hidePanel() {
    var toggler = document.getElementById('toggler');
    var toggler_sm = document.getElementById('toggler-sm');
    var sidebar = document.getElementById('sidepanel');
    var mainbar = document.getElementById('mainbar-items');
    console.warn(screen_width)
    sidebar.style.width = "0px";
    sidebar.style.marginLeft = "-20px"
    toggler_sm.style.display = "block";
    toggler.style.display = "none";
    mainbar.classList.remove("responsive-panel");
}

function showPanel() {
    var toggler = document.getElementById('toggler');
    var toggler_sm = document.getElementById('toggler-sm');
    var sidebar = document.getElementById('sidepanel');
    var mainbar = document.getElementById('mainbar-items');
    sidebar.style.width = "255px";
    sidebar.style.marginLeft = "0px"
    toggler_sm.style.display = "none";
    toggler.style.display = "block";
    mainbar.classList.add("responsive-panel");
}

function loadScreen() {
    var width = (window.innerWidth > 550) ? window.innerWidth : "Desktop View"
    console.log(width);
}


function showAttributes(title) {
    var form = new FormData(document.getElementById(title));
    var preview = document.getElementById("preview-box");
    preview.style.display = "block";
    var name = form.get("name");
    var notes = form.get("notes");
    var user = form.get("username");
    var prop_1 = form.get("prop_1");
    var prop_2 = form.get("prop_2");
    var prop_3 = form.get("prop_3");
    var prop_4 = form.get("prop_4");
    var prop_5 = form.get("prop_5");
    var prop_6 = form.get("prop_6");
    document.getElementById('preview-title').innerText = name;
    document.getElementById('preview-notes').innerText = notes;
    document.getElementById('preview-client').innerText = user;
    document.getElementById('preview-prop_1').innerText = prop_1;
    document.getElementById('preview-prop_2').innerText = prop_2;
    document.getElementById('preview-prop_3').innerText = prop_3;
    document.getElementById('preview-prop_4').innerText = prop_4;
    document.getElementById('preview-prop_5').innerText = prop_5;
    document.getElementById('preview-prop_6').innerText = prop_6;
}

function hidePreview() {
    var preview = document.getElementById("preview-box");
    preview.style.display = "none";
}