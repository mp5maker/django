(function() {
    "use strict";

    $(document).ready(init)

    function init() {
        const currentPage = $("[current-page]").attr('current-page');
        $(`.${currentPage}-nav`).addClass('active');
    }
})();