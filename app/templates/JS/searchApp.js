function UserSearch($scope, $http) {

    $scope.send = function() {
        $http.post('/search', $scope.search)
             .success(function(){alert('User name  exist')})
             .error(function(){alert('User name does not exit')});
    }

}