jQuery(document).ready(function() {
    chrome.tabs.getSelected(null, function (tab) {
        api_url = "https://gp6j1kfg4g.execute-api.us-east-1.amazonaws.com/default/segment-bot?url=" + tab.url;
        jQuery.get(api_url, function (data) {
            console.log(data);
            jQuery('#consumer').append( "<td style=\"width:30.5%\"> Consumer Score: " + data['consumer']['score'] + "</td>" );
            jQuery('#consumer').append( "<td>" + data['consumer']['words'] + "</td>" );
            jQuery('#prosumer').append( "<td> Prosumer Score: " + data['prosumer']['score'] + "</td>" );
            jQuery('#prosumer').append( "<td>" + data['prosumer']['words'] + "</td>" );
            jQuery('#self-serve').append( "<td> Self Serve Business Score: " + data['self-serve business']['score'] + "</td>" );
            jQuery('#self-serve').append( "<td>" + data['self-serve business']['words'] + "</td>" );
            jQuery('#sales-assisted').append( "<td> Sales Assisted Business Score: " + data['sales-assisted business']['score'] + "</td>" );
            jQuery('#sales-assisted').append( "<td>" + data['sales-assisted business']['words'] + "</td>" );
            document.getElementById("robot").style.display = "none";
            document.getElementById("content").style.display = "block";
        })
    })
});