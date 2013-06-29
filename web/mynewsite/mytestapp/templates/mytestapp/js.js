function PhoneCtrl($scope,$http) {
    
    $scope.message='test';
    
    
    $http.get('names.json').success(function(data)
    {
        
        $scope.names=data;
    }
    ).error(function() {alert('error');});
    
    //$scope.names=['david','jason'];
    $scope.changeme= function()
    {
      $scope.message="test3";
      $scope.names.pop();
      $scope.names.push('123');
    };
}