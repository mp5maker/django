(function() {
    "use strict";

    window.onload = init;

    function init() {
        window.goToPostDetailsPage = ({year, month, day, slug} = {}) => {
            window.location.href = `/blogs/posts/${year}/${month}/${day}/${slug}`;
        }
    }
})()