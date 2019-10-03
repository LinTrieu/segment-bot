jQuery(document).ready(function() {
    chrome.tabs.getSelected(null, function (tab) {
        api_url = "https://gp6j1kfg4g.execute-api.us-east-1.amazonaws.com/default/segment-bot?url=" + tab.url;
        jQuery.get(api_url, function (data) {
            console.log(data);
            jQuery('#list').append( "<li> Consumer: " + data['consumer']['score'] + "</li>" );
            jQuery('#list').append( "<p>" + data['consumer']['words'] + "</p>" );
            jQuery('#list').append( "<li> Prosumer: " + data['prosumer']['score'] + "</li>" );
            jQuery('#list').append( "<p>" + data['prosumer']['words'] + "</p>" );
            jQuery('#list').append( "<li> Self Serve Business: " + data['self-serve business']['score'] + "</li>" );
            jQuery('#list').append( "<p>" + data['self-serve business']['words'] + "</p>" );
            jQuery('#list').append( "<li> Sales Assisted Business: " + data['sales-assisted business']['score'] + "</li>" );
            jQuery('#list').append( "<p>" + data['sales-assisted business']['words'] + "</p>" );
        })
    })
});