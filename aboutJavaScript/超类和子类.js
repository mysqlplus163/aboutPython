/**
 * Created by Q1mi on 2017/7/25.
 */


var Car = function (loc) {
    this.loc = loc;

};

Car.prototype.move = function () {
    this.loc++;
};

var Van = function (loc) {

};