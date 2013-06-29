function PhoneCtrl($scope,$http) {
    
    $scope.message='dude';
    
    $scope.names=[];
    
    $scope.loading=false;
    
    function shownames() {
        $scope.loading=true;
        $scope.names=[];
        $http.get('getnames').success(function(data)
    {
        for (var x in data) {
            //code
            
            $scope.names.push(data[x]);
        }
        $scope.loading=false;
       // $scope.names=data;
        
    }
    ).error(function() {alert('error');});
    
    }
    
    //$scope.names=['david','jason'];
    $scope.changeme= function()
    {
      $scope.message="test3";
     shownames();
    };
}