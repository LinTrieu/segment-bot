jQuery(document).ready(function() {
    chrome.tabs.getSelected(null, function (tab) {
        api_url = "https://gp6j1kfg4g.execute-api.us-east-1.amazonaws.com/default/segment-bot?url=" + tab.url;
        $('#title').html('Target users for <b>' + url_domain(tab.url)) + '</b>';
        jQuery.get(api_url, function (data) {
            console.log(data);
            jQuery('#consumer').data('score', data['consumer']['score'])
            jQuery('#consumer').append( "<td style=\"width:39%\"> <b>Consumer</b><br /> Score: " + data['consumer']['score'] + "</td>" );
            jQuery('#consumer').append( "<td class='words'>" + data['consumer']['words'].join(', ') + "</td>" );
            jQuery('#prosumer').data('score', data['prosumer']['score'])
            jQuery('#prosumer').append( "<td style=\"width:39%\"> <b>Prosumer</b><br /> Score: " + data['prosumer']['score'] + "</td>" );
            jQuery('#prosumer').append( "<td class='words'>" + data['prosumer']['words'].join(', ') + "</td>" );
            jQuery('#self-serve').data('score', data['self-serve business']['score'])
            jQuery('#self-serve').append( "<td style=\"width:39%\"> <b>Self Serve Business</b><br /> Score: " + data['self-serve business']['score'] + "</td>" );
            jQuery('#self-serve').append( "<td class='words'>" + data['self-serve business']['words'].join(', ') + "</td>" );
            jQuery('#sales-assisted').data('score', data['sales-assisted business']['score'])
            jQuery('#sales-assisted').append( "<td style=\"width:39%\"> <b>Sales Assisted Business</b><br /> Score: " + data['sales-assisted business']['score'] + "</td>" );
            jQuery('#sales-assisted').append( "<td class='words'>" + data['sales-assisted business']['words'].join(', ') + "</td>" );
            $("#data-table-body").each(function () {
                $(this).html($(this).children('tr').sort(function (a, b) {
                    return ($(b).data('score')) > ($(a).data('score')) ? 1 : -1;
                }));
            });
            document.getElementById("robot").style.display = "none";
            document.getElementById("content").style.display = "block";
            $('.words').css('textTransform', 'capitalize');
        })
    })
});


function url_domain(data) {
  var    a      = document.createElement('a');
         a.href = data;
  return a.hostname.replace('www.', '');
}