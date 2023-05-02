const searchInput4 = document.getElementById('my_search_1');
const resultsBox = document.getElementById('results')
searchInput4.addEventListener('keyup', (e) => {
    if (e.target.value.length == 0) {
        resultsBox.classList.remove('d-none');



    }
    console.log("key is up ")
    if (resultsBox.classList.contains('d-none')) {
        resultsBox.classList.remove('d-none');
    }


    // sendSearchData(e.target.value);
});

console.log("key is up ")

searchInput4.addEventListener('focusout', (e) => {
    console.log("key is do")
    resultsBox.classList.add("d-none")
})