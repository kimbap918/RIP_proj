const likeBtnComment = document.querySelector('#like-btn-comment')
    const csrftoken_comment = document.querySelector('[name=csrfmiddlewaretoken]').value

console.log(likeBtnComment)

    likeBtnComment.addEventListener('click', function (event) {
    console.log(event.target.dataset)
    axios({
        method: 'post',
        url: `/articles/${event.target.dataset.articleId}/like/${event.target.dataset.commentId}/`,
        headers: { 'X-CSRFToken': csrftoken_comment }
    })
        .then(response => {
            console.log(response)
            console.log(response.data)

            if (response.data.isLiked === true) {
                event.target.classList.add('bi-heart-fill')
                event.target.classList.remove('bi-heart')
            } else {
                event.target.classList.add('bi-heart')
                event.target.classList.remove('bi-heart-fill')
            }
            const likeCountComment = document.querySelector('#like-count-comment')
            likeCountComment.innerText = response.data.likeCount
        })
})