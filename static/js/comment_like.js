const likeBtnCommentDetail = document.querySelectorAll('.like-btn-comment')
// console.log("likeBtn", likeBtnComment)    

// 누르는 위치에 따라서 배열의 인덱스를 반환해 저장할 수 있다면?
// console.log(likeBtnComment[0]);

likeBtnCommentDetail.forEach((el, index) => {
el.onclick = () => {
    var x = index

    likeBtnCommentDetail[x].addEventListener('click', function (event) {
    // console.log("dataset", event.target.dataset)
    axios({
        method: 'get',
        // <int:article_pk>/like/<int:comment_pk>/
        url: `/articles/${event.target.dataset.articleId}/like/${event.target.dataset.commentId}/`,
        // headers: { 'X-CSRFToken': csrftoken_comment }
    })
        .then(response => {
            // console.log("response", response)
            // console.log("response.data", response.data)
            if (response.data.isLike === true) {
                event.target.classList.add('bi-hand-thumbs-up-fill')
                event.target.classList.remove('bi-hand-thumbs-up')
            } else {
                event.target.classList.add('bi-hand-thumbs-up')
                event.target.classList.remove('bi-hand-thumbs-up-fill')
            }
            const likeCountComment = document.querySelectorAll('.like-count-comment')
            likeCountComment[x].innerText = response.data.likeCount
        })
})
}
});
