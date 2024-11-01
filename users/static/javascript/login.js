// Define AngularJS module and controller
angular.module('loginApp', [])
  .controller('LoginController', ['$scope', function($scope) {
    $scope.user = {
      username: '',
      password: '',
      rememberMe: false
    };

    $scope.login = function() {
      console.log("Username:", $scope.user.username);
      console.log("Password:", $scope.user.password);
      console.log("Remember Me:", $scope.user.rememberMe);
      alert('Login successful!');
    };
  }]);
