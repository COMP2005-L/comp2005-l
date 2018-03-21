document.querySelector("#users-search").addEventListener("input", function(){
    var searchValue = document.querySelector("#users-search").value
    var selectedUsers = searchValue ? window.users.filter(function(user){
        return user.username.includes(searchValue)
    }) : []

    var html = selectedUsers.map(function(user){
        return '<input type="checkbox" name="groupMembers" value="'+user.id+'" />'+user.username+' <br />'
    }).join('')

    document.querySelector("#users").innerHTML = html
})