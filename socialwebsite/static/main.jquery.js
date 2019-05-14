(function() {
    var csrftoken = Cookies.get('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $(document).ready(function() {
        if (window.myBookmarklet !== undefined) {
            myBookmarklet();
        } else {
            let randomNumber = Math.floor(Math.random() * 99999999999999999999);
            let script = document.createElement('script')
            script.src = `/static/js/bookmarklet.js?r=${randomNumber}`;
            document.body.appendChild(scripts)
        }
    })

})();
