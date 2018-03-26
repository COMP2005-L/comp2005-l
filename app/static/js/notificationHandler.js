var notificationToHTML = function(data){
        var title = '<h4>'+data.title+'</h4>'
        var body = '<p>'+data.body+'</p>'
        var notification = '<div><a href="'+data.ref+'"'+title+body+'</a></div>'
        return notification
}

socket.on("NOTIFICATION-ADDED", function(data){
    var data = JSON.parse(data)
    if(Number.parseInt(data.recipient) === userId){
        $("#notifications").prepend(notificationToHTML(data))
        $("#notification-count").text($("#notifications").children().length)
    }
})

$(function(){
  $("#notification-count").text($("#notifications").children().length)
  $("#notification-area .fa-bell").click(function(){ $("#notifications").toggle() })

  var parsedNotifications = notifications.map(function(notification){
    return notificationToHTML(notification)
  })

  parsedNotifications.forEach(function(html){
    $("#notifications").prepend(html)
  })
})