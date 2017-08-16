/**
 * Created by Q1mi on 2017/7/25.
 */


var Car = function (loc) {
    this.loc = loc;

};

Car.prototype.move = function () {
    this.loc++;
};


// 子类
var Van = function (loc) {
Car.call(this, loc);
};

Van.prototype = Object.create(Car.prototype);
