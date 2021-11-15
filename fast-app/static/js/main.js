let user_file = null;
let is_conv = false;

const _sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

const create_animation = async (data)=>{
  const arr = data.art;
  for (let i = 0; i < arr.length; i++) {
    // $("#result").text(arr[i]);
    document.getElementById("result").innerHTML=arr[i];
    await _sleep(100);
  }
}

const switch_is_conv = ()=>{
  is_conv=!is_conv;
  if (is_conv) {
    document.getElementById("convImg").style.display = "";
  }
  else{
    document.getElementById("convImg").style.display = "none";
  }
}

const fetch_data = async ()=>{
  console.log('fetch start');
  console.log(user_file);
  let fd = new FormData();
  fd.append("video", user_file);

  switch_is_conv();

  // POST to API
  $.ajax({
      url:'/api',
      type:'post',
      data: fd,
      processData: false,
      contentType: false,
      cache: false
  }).done( async (data) =>{
      console.log('done!!');
      console.log(data)
      switch_is_conv();
      await create_animation(data);
  }).fail( ()=> {
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
