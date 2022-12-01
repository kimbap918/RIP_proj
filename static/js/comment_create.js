
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
            const articlePK = response.data.articlePK
            // commentData에 저장된 값을 순회하면서 값을꺼냄
            // 댓글들을 모두 출력(비동기)
            console.log("commentData", commentData)
            for (let i = 0; i < commentData.length; i++) {
                console.log("commentData_commentPk", commentData[0].commentPk)
                if (user === commentData[i].user_id) {
                  comments.insertAdjacentHTML('beforeend', `
                  <div class="comment">
                    <span class="comment-profile-name"><a class="comment-profile-name" href="{% url 'accounts:detail' commentData[i].commentPk %}" style="text-decoration: none;">${commentData[i].profile_name}</a></span>
                    <i class="like-btn-comment bi bi-hand-thumbs-up" data-article-id="${articlePK}" data-comment-id="${commentData[i].commentPK}"></i>
                    <span class="like-count-comment">${commentData[i].count}</span>
                    <p class="comment-content">${commentData[i].content}</p>
                    <p class="comment-control-delete btn btn-outline-danger mb-2" onclick="comment_delete(this)" id="comment-delete-${commentData[i].commentPK}" data-postdel-id="${articlePK}" data-commentdel-id="${commentData[i].commentPK}">삭제</p>
                    <hr>
                  </div>
            `)
                } else {
                    comments.insertAdjacentHTML('beforeend', `
                    <div class="comment">
                    <span class="comment-profile-name"><a class="comment-profile-name" href="#" style="text-decoration: none;">${commentData[i].profile_name}</a></span>
                    <i class="like-btn-comment bi bi-hand-thumbs-up" data-article-id="${articlePK}" data-comment-id="${commentData[i].commentPK}"></i>
                    <span class="like-count-comment">${commentData[i].count}</span>
                    <p class="comment-content">${commentData[i].content}</p>
                    <p class="comment-control-delete btn btn-outline-danger mb-2" onclick="comment_delete(this)" id="comment-delete-${commentData[i].commentPK}" data-postdel-id="${articlePK}" data-commentdel-id="${commentData[i].commentPK}">삭제</p>
                    <hr>
                  </div>
            `)
                }
            }
            commentForm.reset()
        })
    })