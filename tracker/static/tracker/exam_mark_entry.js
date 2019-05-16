let formChanged = false;

// Get all the mark boxes
const mark_boxes = document.getElementsByClassName('mark-box');


let changeMark = function(event) {
    // Do a comparision of the max score here

    const max_score = Number(event.currentTarget.parentElement.parentElement.getElementsByClassName('max_score')[0].innerHTML);
    if(event.target.value > max_score) {
        addOverMaxWarning(event.target, max_score);
    } else {
        removeOverMaxWarning(event.target);
    }

    if (!formChanged) {
        addChangedWarning();
        formChanged = true;
    }
}

// Add a warning if the entered score is greater than the maximum:
let addOverMaxWarning = function(target, max_score) {

    let warningDiv = target.parentNode.parentNode.parentNode.getElementsByClassName('score-warning')[0];
    warningDiv.innerHTML = 'You have entered a score greater than ' + max_score;
    warningDiv.style.display = 'block';

    target.classList.add('alert-danger');
    target.focus();
};

let removeOverMaxWarning = function(target) {
    target.classList.remove('alert-danger');
    let warningDiv = target.parentNode.parentNode.parentNode.getElementsByClassName('score-warning')[0];
    warningDiv.style.display = '';
};

// Add a warning at the top of the page that they have unsaved changed
let addChangedWarning = function() {
    let alertDiv = document.getElementById('alerts');
    let alertNode = document.createElement('div');
    alertDiv.appendChild(alertNode);
    alertNode.classList.add('alert');
    alertNode.classList.add('alert-warning');
    alertNode.classList.add('alert-dismissible');
    alertNode.classList.add('change-warning');
    let closeButton = document.createElement('a');
    alertNode.appendChild(closeButton)
    closeButton.href = '#';
    closeButton.className = 'close';
    closeButton.innerHTML = 'x';
    alertNode.innerHTML = 'You have unsaved changes on this page.';
};

// Function that takes a mark box element and assigns the onkeydown event:

for (var i = 0; i < mark_boxes.length; i++) {
    mark_boxes[i].addEventListener('focusout', changeMark, false);
}