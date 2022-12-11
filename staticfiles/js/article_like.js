// 게시글 좋아요
const likeBtn = document.querySelector('#like-btn')
    const csrftoken_like = document.querySelector('[name=csrfmiddlewaretoken]').value

    likeBtn.addEventListener('click', function (event) {
        console.log(event.target.dataset)
        axios({
            method: 'post',
            url: `/articles/${event.target.dataset.articleId}/like/`,
            headers: { 'X-CSRFToken': csrftoken_like }
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
                const likeCount = document.querySelector('#like-count')
                likeCount.innerText = response.data.likeCount
            })
    })