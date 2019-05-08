(function() {
    "use strict";

    window.onload = init;

    function init() {
        window.goToPostDetailsPage = (slug) => {
            window.location.href = `/blogs/posts/${slug}`;
        }
    }
})()