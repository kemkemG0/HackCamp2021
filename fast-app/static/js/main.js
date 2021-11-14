let user_file = null;

const fetch_data = ()=>{

  console.log('fetch start');
  console.log(user_file);

  let fd = new FormData();
  fd.append("video", user_file);

  // POST to API
  $.ajax({
      url:'/api',
      type:'post',
      data: fd,
      processData: false,
      contentType: false,
      cache: false,
  }).done(function (data) {
      console.log('done!!');
      console.log(data)
      $("#result").text(data.art);
  }).fail(function() {
      console.log('fail');
  });
}

const display_selected_video = () => {
  const inputElement = document.getElementById("user-file");
  inputElement.addEventListener("change", handleFiles, false);
  function handleFiles() {
    const file = this.files[0];
    user_file = file;
    console.log(file)
    // create URL of file on this site
    const blobUrl = window.URL.createObjectURL(file);
    const video = document.getElementById('selected-file');

    video.src = blobUrl;
  }
}

const main = ()=>{
  display_selected_video();
}


window.onload = main;
