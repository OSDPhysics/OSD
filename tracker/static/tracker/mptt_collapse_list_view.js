var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    $(this).siblings().filter('ul')[0].classList.toggle("nested");
    this.classList.toggle("caret-down");
  });
}

var points = document.getElementsByClassName("syllabus-checkbox");
var j;

for (j=0; j < points.length; j++) {
    points[j].addEventListener("click", function () {
      var child_points = this.parentElement.getElementsByTagName("input");
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

      }
      setIndeterminate();
    });
}

function setIndeterminate() {
    var checkboxes = document.getElementsByClassName("syllabus-checkbox");
    var p;
    for (p = 0; p < checkboxes.length; p++) {
        var current_box = checkboxes[p];

        if(current_box.checked) {
            current_box.classList.add("checked");
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

function initial_classes() {
    let checkboxes = document.getElementsByClassName("syllabus-checkbox");
    let p;
    for (p = 0; p < checkboxes.length; p++) {
        let current_box = checkboxes[p];

        if (current_box.checked) {
            current_box.classList.add("checked");
            current_box.classList.remove("nested")
        }

    }
}

function initial_nested() {
    let uls = document.getElementsByClassName('has-children')

    let p;
    for (p = 0; p < uls.length; p++) {
        let ul = uls[p];

        if(ul.getElementsByTagName('input')[0].indeterminate === true) {
            ul.classList.remove('nested');
        }

        if(ul.getElementsByTagName('input')[0].checked === true) {
            ul.classList.remove('nested');
        }

    }
}
window.onload = function(){
    initial_classes();
    setIndeterminate();
    initial_nested();
}
