(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        document.body.appendChild(document.createElement('script')).src =
            'https://62b99e9a.ngrok.io/static/bookmarklet.js?r='+
            Math.floor(Math.random()*99999999999999999999);
    }
})();