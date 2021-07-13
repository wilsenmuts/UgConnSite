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

function showNote(formId) {
    var Note = document.getElementById("note-box");
    Note.style.display = "block";
    var form = new FormData(document.getElementById(formId));
    var agent_name = form.get("agent_name");
    var client_name = form.get("client_name");
    var client_names = form.get("client_names");
    document.getElementById("note_agent").innerText = agent_name;
    document.getElementById("note_client").innerText = client_names;
    document.getElementById("clientname").value = client_name;
    hidePreview();
}

function submitAgentNote() {
    var form = new FormData(document.getElementById("note_form"));
    var agent_name = form.get("agentName");
    var client_name = form.get("clientname");
    var title = form.get("title");
    var body = form.get("body");
    $.ajax({
        url: "/kunai/ajax34/submitAgentNote/",
        data: {
            'agent_name': agent_name,
            'client_name': client_name,
            'title': title,
            'body': body,
        },
        //method:GET
        dataType: 'json',
        success: function(data) {
            alert(data.alert);
        },
        error: function() {
            alert("We caught an error. Try re-assigning agent");

        }
    })
    console.log("Finished processing" + agent_name);
    closeNote();
}

function closeNote(formId) {
    var Note = document.getElementById("note-box");
    Note.style.display = "none";
}

function readClientNote(text) {
    var note_id = text;
    //alert(note_id);
    $.ajax({
        url: "/flashcards/justSeenNote/",
        data: {
            "note_id": note_id
        },
        dataType: 'json',
        error: function() {
            alert("We caught an error. Try re-sending signal");

        }
    })
}

function sendClientComment(text, body, user) {
    var note_id = text;
    var comment = document.getElementById(body).value;
    $.ajax({
        url: "/flashcards/justSendComment/",
        data: {
            "note_id": note_id,
            "body": comment,
            "user": user
        },
        dataType: 'json',
        success: function() {
            let comments = document.getElementById("comment_sect_" + note_id);
            let block_to_insert = document.createElement("div");
            block_to_insert.style.margin = "10px";
            //block_to_insert.position="left"
            block_to_insert.style.borderRadius = "10px";
            block_to_insert.classList.add("bg-greysan", "padding");
            block_to_insert.innerHTML = (
                ' <small style="color:wheat;">Reply by ' + user + ' just now </small><br><p style="font-size:.85em">' + comment + '</p>'
            );
            comments.appendChild(block_to_insert);
            document.getElementById(body).value = "";

        },
        error: function() {
            alert("We caught an error. Try re-sending signal");
        }
    })
}

function readAgentNote(text) {
    var note_id = text;
    //alert(note_id);
    $.ajax({
        url: "/kunai/justSeenNote/",
        data: {
            "note_id": note_id
        },
        dataType: 'json',
        error: function() {
            alert("We caught an error. Try re-sending signal");

        }
    })
}

function sendAgentComment(text, body, user) {
    var note_id = text;
    var comment = document.getElementById(body).value;
    $.ajax({
        url: "/kunai/justSendComment/",
        data: {
            "note_id": note_id,
            "body": comment,
            "user": user
        },
        dataType: 'json',
        success: function() {
            let comments = document.getElementById("comment_sect_" + note_id);
            let block_to_insert = document.createElement("div");
            block_to_insert.style.margin = "10px";
            block_to_insert.style.position = "relative";
            block_to_insert.style.right = "2px";
            block_to_insert.style.maxWidth = "85%";
            block_to_insert.style.borderRadius = "10px";
            block_to_insert.classList.add("bg-greysan", "padding");
            block_to_insert.innerHTML = (
                ' <small style="color:wheat;">Reply by ' + user + ' just now </small><br><p style="font-size:.85em">' + comment + '</p>'
            );
            comments.appendChild(block_to_insert);
            document.getElementById(body).value = "";

        },
        error: function() {
            alert("We caught an error. Try re-sending signal");
        }
    })
}