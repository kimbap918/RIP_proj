const likeBtnComment = document.querySelector('.like-btn-comment')
console.log("likeBtn", likeBtnComment)    
// const csrftoken_comment = document.querySelector('[name=csrfmiddlewaretoken]').value

    likeBtnComment.addEventListener('click', function (event) {
    console.log("dataset", event.target.dataset)
    axios({
        method: 'get',
        // <int:article_pk>/like/<int:comment_pk>/
        url: `/articles/${event.target.dataset.articleId}/like/${event.target.dataset.commentId}/`,
        // headers: { 'X-CSRFToken': csrftoken_comment }
    })
        .then(response => {
            console.log("response", response)
            console.log("response.data", response.data)
            if (response.data.isLike === true) {
                event.target.classList.add('bi-hand-thumbs-up-fill')
                event.target.classList.remove('bi-hand-thumbs-up')
            } else {
                event.target.classList.add('bi-hand-thumbs-up')
                event.target.classList.remove('bi-hand-thumbs-up-fill')
            }
            const likeCountComment = document.querySelector('.like-count-comment')
            likeCountComment.innerText = response.data.likeCount
        })
})