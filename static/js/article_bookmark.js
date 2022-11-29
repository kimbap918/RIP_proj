  // (1) 북마크 버튼
  const bookmarkBtn = document.querySelector('#bookmark-btn')
    
  // (2) 북마크 버튼을 클릭하면, 함수 실행
  bookmarkBtn.addEventListener('click', function (event) {
      // 서버로 비동기 요청을 하고 싶음
      console.log(event.target.dataset)
      axios({
          method: 'get',
          url: `/articles/${event.target.dataset.bookmarkId}/bookmark`
      })
          .then(response => {
              console.log(response)
              console.log(response.data)
              event.target.classList.toggle('bi-heart')
              event.target.classList.toggle('bi-heart-fill')
              if (response.data.isbookmark === true) {
                  event
                      .target
                      .classList
                      .add('bi-heart-fill')
                  event
                      .target
                      .classList
                      .remove('bi-heart')
              } else {
                  event
                      .target
                      .classList
                      .add('bi-heart')
                  event
                      .target
                      .classList
                      .remove('bi-heart-fill')
              }
              const bookmarkCount = document.querySelector('#bookmark-count')
              bookmarkCount.innerText = response.data.bookmarkCount
          })
  })
  // (1) 북마크 버튼
// const bookmarkBtn = document.querySelector('#bookmark-btn')
// // (2) 북마크 버튼을 클릭하면, 함수 실행
// bookmarkBtn.addEventListener('click', function (event) {
//     // 서버로 비동기 요청을 하고 싶음
//     console.log(event.target.dataset)
//     axios({
//         method: 'get',
//         url: `/articles/${event.target.dataset.articleID}/bookmark`
//     })
//     .then(response => {
//         console.log(response)
//         console.log(response.data)
//         // event.target.classList.toggle('bi-heart')
//         // event.target.classList.toggle('bi-heart-fill')
//         if (response.data.bookmark === true) {
//             event
//                 .target
//                 .classList
//                 .add('bi-heart-fill')
//             event
//                 .target
//                 .classList
//                 .remove('bi-heart')
//         } else {
//             event
//                 .target
//                 .classList
//                 .add('bi-heart')
//             event
//                 .target
//                 .classList
//                 .remove('bi-heart-fill')
//         }
//         const bookmarkCount = document.querySelector('#bookmark-count')
//         bookmarkCount.innerText = response.data.bookmarkCount
//     })
// })