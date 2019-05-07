(function() {
    "use strict";

    window.onload = init;

    function init() {
        window.goToArticlesDetailsPage = (slug) => {
            window.location.href = `/articles/${slug}`;
        }
    }
})()