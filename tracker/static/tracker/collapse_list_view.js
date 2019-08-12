var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".has-children").classList.toggle("nested");
    this.classList.toggle("caret-down");
  });
}

var points = document.getElementsByClassName("syllabus-checkbox");
var j;

for (j=0; j < points.length; j++) {
    points[j].addEventListener("click", function () {
      var parent = this.parentElement;
      var child_points = parent.getElementsByTagName("input");
      var l;

      // Check all children
      if(this.checked === true){
          this.classList.add("checked");
          for(l = 0; l < child_points.length; l++){
          child_points[l].checked = true;
          child_points[l].classList.add("checked")
      }}

      // uncheck all children
      if (this.checked === false) {
          this.classList.remove("checked");
      for(l = 0; l < child_points.length; l++){
          child_points[l].checked = false;
          child_points[l].classList.remove("checked")
          }
      setIndeterminate()
      }

      // Set parents to indeterminate when activating a box
      if (this.checked === true) {
          var parents = $(this).parent().parents();
          var checkboxes = parents.filter('li');
          var m;
          for (m = 0; m < checkboxes.length; m++) {
              var boxes = checkboxes[m].children[0];
              boxes.indeterminate = true;
          }

      // clear the indeterminates if all children are also checkedd


      }
    });
}

function setIndeterminate() {
    var checkboxes = document.getElementsByClassName("syllabus-checkbox");
    var p;
    for (p = 0; p < checkboxes.length; p++) {
    var current_box = checkboxes[p];

    var all_selected = current_box.parentElement.querySelectorAll('.checked');
    if(all_selected.length) {
        current_box.indeterminate = true;
        current_box.checked = false;
        current_box.classList.remove('checked');
    }
    else{
        current_box.indeterminate = false;

    }
}


}

document.onload = setIndeterminate;