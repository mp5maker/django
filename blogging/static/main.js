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

        window.fetchFeed = () => {
            const copyToClipboard = (responseText) => {
                const inputElement = document.createElement('input')
                inputElement.value = responseText;
                document.body.appendChild(inputElement)
                inputElement.select()
                document.execCommand("copy")
                document.body.removeChild(inputElement)
            }

            const fetchFeedAsync = async () => {
                let response = await fetch(url)
                let responseText = await response.text()
                return await copyToClipboard(responseText)
            }

            fetchFeedAsync()
        }
    }
})()