


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

const main = ()=>{
  const inputElement = document.getElementById("user-file");
  inputElement.addEventListener("change", handleFiles, false);
    
  function handleFiles() {
    const file = this.files[0]; /* ファイルリストを処理するコードがここに入る */
    console.log(file)
  
    // ファイルのブラウザ上でのURLを取得する
    const blobUrl = window.URL.createObjectURL(file);
  
    // img要素に表示
    const img = document.getElementById('selected-file');
    img.src = blobUrl;
  
  }
}

window.onload = main;
