/**
 * Created by liwenzhou on 2016/12/13.
 */
// 组件
"use strict";

angular.module("blogList").
    component("blogList", {
        // template: '<div class=""> <h1 class="new-class">{{ title }} </h1> <button ng-click="someClickTest()">Click me!</button> </div>',
        templateUrl: "templates/blog-list.html",
        controller: function ($scope) {

            var blogItems = [
                {title: "Some title", id:1, description: "This is a book."},
                {title: "Title", id:2, description: "This is a book."},
                {title: "Tea", id:3, description: "This is a book."},
                {title: "Lite", id:4, description: "This is a book."}

            ];
            $scope.items = blogItems;

            $scope.title = "Hi there";
            $scope.clicks = 0;
            $scope.someClickTest = function () {
                console.log("clicked!");
                $scope.clicks += 1;
                $scope.title = "Clicked " + $scope.clicks + " times";
        }
        }
    });
//     controller("BlogListController", function ($scope){
//         console.log("Hello");
//         $scope.title = "Hi there";
//         $scope.clicks = 0;
//         $scope.someClickTest = function () {
//             console.log("clicked!");
//             $scope.clicks += 1;
//             $scope.title = "Clicked " + $scope.clicks + " times";
//         }
//
// });
