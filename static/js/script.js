// to make sidebar default to open
            $(document).ready(function(){
                $('.sidenav').sidenav();
            });

            // to make select options on form visible
            $(document).ready(function(){
                $('select').formSelect();
            });

            // to allow expansion of .collapsible item
            $(document).ready(function(){
                $('.collapsible').collapsible();
            });

            // to allow dropdown on side menu
            $(".dropdown-trigger").dropdown();

            // initialize modal
            $(document).ready(function(){
                $('.modal').modal();
            });

            document.getElementById('categorySelect').onchange = function() {
                window.location.href = this.children[this.selectedIndex].getAttribute('href');
            }

            document.getElementById('statusSelect').onchange = function() {
                window.location.href = this.children[this.selectedIndex].getAttribute('href');
            }