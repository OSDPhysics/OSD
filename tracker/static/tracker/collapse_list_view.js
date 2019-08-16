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

      // When we check a box, check all children
      if(this.checked === true){
          this.classList.add("checked");
          for(l = 0; l < child_points.length; l++){
          child_points[l].checked = true;
          child_points[l].classList.add("checked")
      }}

      // When we uncheck a box...
      if (this.checked === false) {
          this.classList.remove("checked");
          // Clear all the parents (setIndeterminate will set them to indeterminate)
          var unchecked_parents = $(this).parent().parents();
          var parent_checkboxes = unchecked_parents.filter('li');
          var m;
          for (m = 0; m < parent_checkboxes.length; m++) {
              var parent_boxes = parent_checkboxes[m].children[0];
              parent_boxes.checked = false;
              parent_boxes.indeterminate = false;
              parent_boxes.classList.remove("checked")
          }

          // Uncheck all children
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
          setIndeterminate()
      }
    });
}

function setIndeterminate() {
    var checkboxes = document.getElementsByClassName("syllabus-checkbox");
    var p;
    for (p = 0; p < checkboxes.length; p++) {
        var current_box = checkboxes[p];

        if(current_box.checked) {
            current_box.classList.remove("nested");
            continue;
        }

        var all_selected = current_box.parentElement.getElementsByClassName('checked');
        var all_children = current_box.parentElement.getElementsByClassName("syllabus-checkbox");

        // Ticked if all the children are ticked.


        if(all_selected.length) {

            if (all_selected.length === all_children.length - 1) {
                current_box.indeterminate = false;
                current_box.checked = true;
                current_box.classList.add('checked');

            } else {
                current_box.indeterminate = true;
                current_box.checked = false;
                current_box.classList.remove('checked');

            }
        }

        else{
            current_box.indeterminate = false;
            current_box.classList.remove("nested")

        }
    }


}

window.onload = function(){
    setIndeterminate();
}