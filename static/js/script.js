
$(document).ready(function() {
    // to make sidebar default to open
    $('.sidenav').sidenav();
    // to make select options on form visible
    $('select').formSelect();
    // to allow expansion of .collapsible item
    $('.collapsible').collapsible();
    // initialize modal
    $('.modal').modal();
    // to allow dropdown on side menu
    $('.dropdown-trigger').dropdown();
});

// sets href with category selection
document.getElementById('categorySelect').onchange = function() {
    window.location.href = this.children[this.selectedIndex].getAttribute('href');
}

// sets href with status selection
document.getElementById('statusSelect').onchange = function() {
    window.location.href = this.children[this.selectedIndex].getAttribute('href');
}