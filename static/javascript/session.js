const app = angular.module('AstreonApp', []);

app.controller('LearningModesController', function($scope, $window) {
  $scope.isModalOpen = false;

  $scope.sessions = [
    { 
      title: 'Math In The Modern World',
      type: 'AI Study',
      icon: '../static/imgs/aichat.png',
      progress: 20
    },
    {
      title: 'English Communication',
      type: 'Quiz Me',
      icon: '../static/imgs/quiz.png',
      progress: 20
    },
    {
      title: 'Economical Transitions',
      type: 'Flashcards',
      icon: '../static/imgs/cards.png',
      progress: 20
    },
    {
      title: 'Dimensions of The Cybersecurity Cube',
      type: 'Learning Modes',
      icon: '../static/imgs/learn_mode.png',
      progress: 20
    }
  ];

  $scope.menuState = {};

  $scope.toggleMenu = function(sessionId) {
    $scope.menuState[sessionId] = !$scope.menuState[sessionId];
  };

  $scope.isMenuOpen = function(sessionId) {
    return $scope.menuState[sessionId] || false;
  };

  $scope.openModal = function() {
    $scope.isModalOpen = true;
  };

  $scope.closeModal = function() {
    $scope.isModalOpen = false;
  };

  $scope.goBack = function() {
    $window.history.back();
  };
});