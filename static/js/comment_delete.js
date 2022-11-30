// 댓글 삭제 비동기
const comment_delete = (e) => {
  const comment_id = document.querySelector(`#${e.id}`).id
  console.log(event.target.dataset)
  console.log(comment_id)
  axios({
    method: 'post',
    url: `/articles/${event.target.dataset.postdelId}/comment_delete/${event.target.dataset.commentdelId}`,
    headers: {
      'X-CSRFToken': csrftoken
    }
  }).then(response => {
    const comments = document.querySelector("#comments")
    comments.textContent = ""
    const commentData = response.data.commentData
    const user = response.data.user

    for (let i = 0; i < commentData.length; i++) {
      if (user === commentData[i].user_id) {
        comments.insertAdjacentHTML('beforeend', `
        <div class="comment" data-comment-id="${commentData[i].commentPk}">
          <div class="comment-detail">
            <p class="comment-profile-name"><a class="comment-profile-name" href="#">${commentData[i].profile_name}</a></p>
            <p id="comment-update-${commentData[i].commentPk}-content" class="comment-content">${commentData[i].content}</p>
            <p class="comment-control-delete btn btn-outline-danger mb-2" onclick="comment_delete(this)" id="comment-delete-${commentData[i].commentPk}" data-postdel-id="${response.data.articlePk}" data-commentdel-id="${commentData[i].commentPk}">삭제</p>
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
  })
}