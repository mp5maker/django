(function() {
    "use strict";

    window.onload = init;

    function init() {
        let navbarToggler = document.getElementsByClassName('navbar-toggler')[0];
        navbarToggler.classList.add('collapsed');

        window.goToBlogDetails = (slug) => {
            window.location.href=`/blogs/${slug}`;
        }

        window.navbarToggle = (id) => {
            let navbar = document.getElementById(id)
            const isCollapsed = navbarToggler.classList.contains('collapsed');
            if (isCollapsed) {
                navbarToggler.classList.remove('collapsed')
                navbar.classList.add('show')
            }
            if (!isCollapsed) {
                navbarToggler.classList.add('collapsed')
                navbar.classList.remove('show')
            }
        }
    }
})()