(function () {
  $.fn.extend({
    check: function () {
      this.children("input").each(function () {
        console.log(this);
        if($(this).attr("required") == "true") {
          
        }
      })
    }
  })
})();