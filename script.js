const toggleBtn = document.querySelector('.button');
const toggleBtnIcon = document.querySelector('.button i');
const dropdown = document.querySelector('.dropdown');

function clicked() {
  dropdown.classList.toggle('open');
}

const openCameraBtn1 = document.getElementById('open-camera');
const openCameraBtn2 = document.getElementById('open-camera-2');

openCameraBtn1.addEventListener('click', () => {
  // Open the video stream in a new window
  const videoWindow = window.open('video.html', '_blank', 'width=640,height=480');

  // Wait for the new window to load
  videoWindow.addEventListener('load', () => {
    // Get the video element from the new window
    const video = videoWindow.document.getElementById('video-stream');

    // Add a click event listener to capture the photo when the user clicks the video
    video.addEventListener('click', () => {
      // Capture the photo from the video
      const canvas = videoWindow.document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
      const dataURL = canvas.toDataURL();

      // Display the captured photo in a new window
      const photoWindow = window.open('', '_blank', 'width=320,height=240');
      photoWindow.document.write(`<img src="${dataURL}" alt="Captured Photo">`);

      // Download the captured photo
      const link = document.createElement('a');
      link.download = 'photo.png';
      link.href = dataURL;
      link.click();
    });
  });
});

openCameraBtn2.addEventListener('click', () => {
  // Open the video stream in a new window
  const videoWindow = window.open('video.html', '_blank', 'width=640,height=480');

  // Wait for the new window to load
  videoWindow.addEventListener('load', () => {
    // Get the video element from the new window
    const video = videoWindow.document.getElementById('video-stream');

    // Add a click event listener to capture the photo when the user clicks the video
    video.addEventListener('click', () => {
      // Capture the photo from the video
      const canvas = videoWindow.document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
      const dataURL = canvas.toDataURL();

      // Display the captured photo in a new window
      const photoWindow = window.open('', '_blank', 'width=320,height=240');
      photoWindow.document.write(`<img src="${dataURL}" alt="Captured Photo">`);

      // Download the captured photo
      const link = document.createElement('a');
      link.download = 'photo.png';
      link.href = dataURL;
      link.click();
    });
  });
});
