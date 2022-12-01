// 댓글 삭제 비동기
const comment_delete = (e) => {
  const comment_id = document.querySelector(`#${e.id}`).id;
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
    const articlePK = response.data.articlePK

    for (let i = 0; i < commentData.length; i++) {
      if (user === commentData[i].user_id) {
        console.log("commentData", commentData)
        console.log("commentData_PK", commentData[i].commentPK)
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
  })
}