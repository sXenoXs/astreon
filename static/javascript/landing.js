// AngularJS App and Controller
angular.module('AstreonApp', [])
  .controller('LandingPageController', ['$scope', function($scope) {
    $scope.login = function() {
      // Logic for login
      console.log("Login button clicked");
    };

    $scope.signUp = function() {
      // Logic for sign-up
      console.log("Sign up button clicked");
    };

    $scope.tryItNow = function() {
      // Logic for "Try it now" button
      console.log("Try it now button clicked");
    };

    $scope.goToAbout = function() {
      // Navigate to the About page
      console.log("Navigate to About page");
    };

    $scope.goToCareers = function() {
      // Navigate to the Careers page
      console.log("Navigate to Careers page");
    };

    $scope.goToBlog = function() {
      // Navigate to the Blog page
      console.log("Navigate to Blog page");
    };

    $scope.goToHelpCenter = function() {
      // Navigate to the Help Center page
      console.log("Navigate to Help Center page");
    };
  }]);
