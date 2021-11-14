


// const fetch_data = ()=>{
//   console.log('test');
//   url = '/api'
//   let formData = new FormData(testform).get('num');
//   console.log(formData)
//   data = {'num':formData}
//   console.log(data)
//   $.ajax({
//     url: url,
//     dataType: "json",
//     type: "post",
//     contentType: "application/json",
//     data: JSON.stringify(data),
//   }).done((data)=>{
//     console.log(data)
//     $('#result').text(data.art)
//   }).fail((data)=>{
//     console.log(data)
//   })
// }

const display_selected_video = () => {
  const inputElement = document.getElementById("user-file");
  inputElement.addEventListener("change", handleFiles, false);
  function handleFiles() {
    const file = this.files[0];
    console.log(file)
    // ファイルのブラウザ上でのURLを取得する
    const blobUrl = window.URL.createObjectURL(file);
    // video 要素に表示
    const video = document.getElementById('selected-file');
    video.src = blobUrl;
}
}

const main = ()=>{
  display_selected_video();
}


window.onload = main;
