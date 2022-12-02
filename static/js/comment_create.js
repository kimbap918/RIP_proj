
const commentForm = document.querySelector('#comment-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    // 기존 코드와 비교해서 딱히 바뀐것 없음 
    commentForm.addEventListener('submit', function (event) {
        event.preventDefault();
        axios({
            method: 'post',
            url: `/articles/${event.target.dataset.articleId}/comments/`,
            headers: { 'X-CSRFToken': csrftoken },
            data: new FormData(commentForm)
        }).then(response => {
            console.log(response.data)
            const comments = document.querySelector("#comments")
            comments.textContent = ""
            // views 에서 리턴한 commentData, user값 가져옴
            const commentData = response.data.commentData
            const user = response.data.user
            const articlePK = response.data.articlePK
            let likeBtn = "like-btn-comment";
            // commentData에 저장된 값을 순회하면서 값을꺼냄
            // 댓글들을 모두 출력(비동기)
            // console.log("commentData", commentData)
            // console.log("comment-Like", commentData.isLike)
            for (let i = 0; i < commentData.length; i++) {
                let like = "";
                if (commentData[i].isLike) {
                  like = "bi-hand-thumbs-up";
                }
                else {
                  like = "bi-hand-thumbs-up-fill";
                }

                // console.log("commentData_commentPk", commentData[i].commentPK)
                if (user === commentData[i].user_id) {
                  comments.insertAdjacentHTML('beforeend', `
                  <div class="div_comment">
                    <a class="keyboard-comment-user" href="#" style="text-decoration: none;">${commentData[i].profile_name}</a>
                    <i class="like-btn-comment bi ${like}" data-article-id="${articlePK}" data-comment-id="${commentData[i].commentPK}"></i>
                    <span class="like-count-comment">${commentData[i].count}</span>
                    <p>${commentData[i].content}</p>
                    <p class="comment-control-delete btn btn-outline-danger mb-2" onclick="comment_delete(this)" id="comment-delete-${commentData[i].commentPK}" data-postdel-id="${articlePK}" data-commentdel-id="${commentData[i].commentPK}">삭제</p>
                  </div>
                  <hr>
            `)
                } else {
                    comments.insertAdjacentHTML('beforeend', `
                    <div class="comment">
                      <a class="keyboard-comment-user" href="#" style="text-decoration: none;">${commentData[i].profile_name}</a>
                      <i class="like-btn-comment bi ${like}" data-article-id="${articlePK}" data-comment-id="${commentData[i].commentPK}"></i>
                      <span class="like-count-comment">${commentData[i].count}</span>
                      <p>${commentData[i].content}</p>
                      <p class="comment-control-delete btn btn-outline-danger mb-2" onclick="comment_delete(this)" id="comment-delete-${commentData[i].commentPK}" data-postdel-id="${articlePK}" data-commentdel-id="${commentData[i].commentPK}">삭제</p>
                    </div>
                  <hr>
            `)
                }
            }
            commentForm.reset()
        })
    })