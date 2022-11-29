    const commentForm = document.querySelector('#comment-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    // 기존 코드와 비교해서 딱히 바뀐것 없음 
    commentForm.addEventListener('submit', function (event) {
        event.preventDefault();
        console.log(event)
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
            // commentData에 저장된 값을 순회하면서 값을꺼냄
            // 댓글들을 모두 출력(비동기)
            for (let i = 0; i < commentData.length; i++) {

                if (user === commentData[i].user_id) {
                    comments.insertAdjacentHTML('beforeend', `
            <div class="comment" data-comment-id="${commentData[i].commentPk}">
              <div class="comment-detail">
                <span class="comment-profile-name"><a class="comment-profile-name" href="#">${commentData[i].profile_name}</a></span>
                <i class="bi bi-heart" data-review-id="{{ article.pk }}" data-comment-id="{{ comment.pk }}" id="commentlike"></i>
                <p id="comment-update-${commentData[i].commentPk}-content" class="comment-content">${commentData[i].content}</p>
                <div class="comment-control" id="control-comment-update-${commentData[i].commentPk}">
                  <p class="comment-control-delete btn btn-outline-danger mb-2" onclick="comment_delete(this)" id="comment-delete-${commentData[i].commentPk}" data-postdel-id="${response.data.articlePk}" data-commentdel-id="${commentData[i].commentPk}">삭제</p>
                </div>
                <hr>
              </div>
            </div>
            `)
                } else {
                    comments.insertAdjacentHTML('beforeend', `
            <div class="comment">
              <div class="comment-detail">
                <span class="comment-profile-name"><a class="comment-profile-name" href="#">${commentData[i].profile_name}</a></span>
                <p class="comment-content">${commentData[i].content}</p>
              </div>
            </div>
            `)
                }
            }
            commentForm.reset()
        })
    })