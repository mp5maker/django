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

    $(document).ready(init)

    function init() {
        const currentPage = $("[current-page]").attr('current-page');
        $(`.${currentPage}-nav`).addClass('active');

        $('a.like').click(function(event) {
            event.preventDefault();
            const url = $(this).data('url');
            const id = $(this).data('id');
            const action = $(this).data('action');
            let payload = {
                id: id,
                action: action
            }
            $.post(url, payload, function(data) {
                if (data['status'] = 'ok') {
                    var previous_action = $('a.like').data('action');
                    var isLike = previous_action == 'like'
                    $('a.like').data('action', isLike ? 'unlike' : 'like');
                    $('a.like').html(isLike ?
                        `<i class="fas fa-thumbs-down"></i>` :
                        `<i class="fas fa-thumbs-up"></i>`);
                    var previous_likes = parseInt($('span.count').text());
                    var like_counter = isLike ? previous_likes + 1 : previous_likes - 1;
                    if (like_counter == 1) {
                        $('span.count').text(like_counter + " Like");
                    } else {
                        $('span.count').text(like_counter + " Likes");
                    }
                }
            })
        })

        $('.on-card-click').click(function(event) {
            event.preventDefault();
            const id = $(this).data('id');
            const slug = $(this).data('slug');
            const url = '/images/details'
            window.location.href = `${url}/${id}/${slug}/`;
        })

        $('.on-user-card-click').click(function() {
            const username = $(this).data('username');
            const url = '/account/details'
            window.location.href = `${url}/${username}/`;
        })

        $('a.follow').click(function (event) {
            event.preventDefault();
            const url = $(this).data('url');
            const id = $(this).data('id');
            const action = $(this).data('action');
            let payload = {
                id: id,
                action: action
            }
            $.post(url, payload, function (data) {
                if (data['status'] = 'ok') {
                    var previous_action = $('a.follow').data('action');
                    var isFollow = previous_action == 'follow'
                    $('a.follow').data('action', isFollow ? 'unfollow' : 'follow');
                    $('a.follow').html(isFollow ?
                        `<i class="fas fa-heart"></i>` :
                        `<i class="far fa-heart"></i>`);
                    var previousFollows = parseInt($('.count.followers .total').text());
                    var followers = isFollow ? previousFollows + 1 : previousFollows - 1;
                    if (followers == 1) {
                        $('.count.followers .total').text(followers);
                    } else {
                        $('.count.followers .total').text(followers);
                    }
                }
            })
        })
    }
})();