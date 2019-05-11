(function() {
    "use strict";

    window.onload = init;

    function init() {
        const searchBar = document.getElementById('navigation-search-bar');

        searchBar.addEventListener('keypress', (event) => {
            if (event.key == 'Enter' && parseInt(event.keyCode) == 13) {
                window.location.href = `/blogs/posts/?search=${searchBar.value}`;
            }
        })

        window.goToPostDetailsPage = ({year, month, day, slug} = {}) => {
            window.location.href = `/blogs/posts/${year}/${month}/${day}/${slug}`;
        }

        window.search = () => {
            if (searchBar.value) {
                window.location.href = `/blogs/posts/?search=${searchBar.value}`;
            }
        }
    }
})()