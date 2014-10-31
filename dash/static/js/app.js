var app = angular.module('sidbar', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

function ProjectCtrl($scope, $http) {

    $scope.projects = [];

    $scope.loadProject = function() {
        var httpRequest = $http({
            method: 'GET',
            url: '/pv_json/',

        }).success(function(data, status) {
            $scope.projects = data;
        });

    };
    

}

