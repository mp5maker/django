(function() {
    "use strict";

    window.onload = init;

    function init() {
        window.goToBlogDetails = (slug) => {
            window.location.href=`/blogs/${slug}`;
        }
    }
})()