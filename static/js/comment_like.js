const clikeBtn1 = document.querySelector('#commentlike')
likeBtn1.addEventListener('click', function (event) {

    console.log(event.target.dataset)
    axios({
        method: 'get',
        url: `/articles/${event.target.dataset.articleId}/like/`
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