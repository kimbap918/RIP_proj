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
                <p class="comment-profile-name"><a class="comment-profile-name" href="#">${commentData[i].profile_name}</a></p>
                <p id="comment-update-${commentData[i].commentPk}-content" class="comment-content">${commentData[i].content}</p>
                <form class="comment-update-form" id="form-comment-update-${commentData[i].commentPk}" action="/${response.data.postPk}/comment_update/${commentData[i].commentPk}" method="post" style="display:none;">
                  <input class="comment-update" id="comment-update-input-${commentData[i].commentPk}"  type="text" value="${commentData[i].content}">
                  <div class="d-flex">
                    <p class="comment-control-update" onclick="comment_update_ok(this)" id="comment-update-ok-${commentData[i].commentPk}" data-postup-id="${response.data.postPk}" data-commentup-id="${commentData[i].commentPk}">수정 완료</p>
                    <p class="comment-control-update-exit ms-3" onclick="comment_update_exit(this)" id="comment-update-${commentData[i].commentPk}">취소</p>
                  </div>
                </form>
                <div class="comment-control" id="control-comment-update-${commentData[i].commentPk}">
                    <button class="comment-delete-btn" id="comment-delete-{{ comment.pk }}" data-reviewdel-id="{{ article.pk }}"data-commentdel-id="{{ comment.pk }}">삭제</button>
                </div>
                <hr>
              </div>
            </div>
            `)
                } else {
                    comments.insertAdjacentHTML('beforeend', `
            <div class="comment">
              <div class="comment-detail">
                <p class="comment-profile-name"><a class="comment-profile-name" href="#">${commentData[i].profile_name}</a></p>
                <p class="comment-content">${commentData[i].content}</p>
              </div>
            </div>
            `)
                }
            }
            commentForm.reset()
        })
    })


    // commentForm.addEventListener('submit', function (event) {
    //     event.preventDefault();
    //     axios({
    //         method: 'post',
    //         url: `/articles/${event.target.dataset.articleId}/comments/`,
    //         headers: { 'X-CSRFToken': csrftoken },
    //         data: new FormData(commentForm)
    //     })
    //     .then(response => {
    //         console.log(response.data)
    //         const comments = document.querySelector('#comments')
    //         const p = document.createElement('p')
    //         p.innerText = `${response.data.content}`
    //         const hr = document.createElement('hr')
    //         comments.append(p, hr)
    //         commentForm.reset()
    //     })
    // })
