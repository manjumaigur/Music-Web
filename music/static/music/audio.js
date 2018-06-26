window.onload= function() {
				var player = document.getElementsByClassName("ap")[0];
				var songTitle = document.getElementById("song");
				var myAudio = document.getElementById('myAudio');
				var toggleButton = document.getElementsByClassName("ap-toggle-btn")[0];
				var play = document.getElementsByClassName("ap--play")[0];
				var pause = document.getElementsByClassName("ap--pause")[0];
				var playNext = document.getElementsByClassName("ap-next-btn")[0];
				var playPrev = document.getElementsByClassName("ap-prev-btn")[0];
				var progressBar = document.getElementsByClassName("ap-bar")[0];
				var progressBarButton = document.getElementsByClassName("ap-progress-container")[0];
				var volumeButton = document.getElementsByClassName("ap-volume")[0];
				var volumeBar = document.getElementsByClassName("ap-volume-bar")[0];
				var muteButton = document.getElementsByClassName("ap--volume-off")[0];
				var volumeOn = document.getElementsByClassName("ap--volume-on")[0];
				var playButton = document.querySelectorAll('.playButton');
				var playAll = document.getElementById("playAll");
				var repeatButton = document.getElementsByClassName("ap-repeat-btn")[0];
				var ct = document.getElementById('currentTime');
				var dur = document.getElementById('Duration');
				var n = 0;
				var flag = false;

				if (flag == false) {
					myAudio.loop = false;
				}

				var audioPlay = function(audioFile) {
							return function(event) { 
								var audioSrc = audioFile.value;
								songTitle.innerHTML = audioFile.name; 
								player.style.display = "inline";
								if (myAudio.paused == true) {
									play.style.display = "none";
									pause.style.display = "inline";
								}
								myAudio.setAttribute("src", audioSrc);
								myAudio.play();
							};
						};

				for (var i = 0; i < playButton.length; i++) {
						var playAudio = audioPlay(playButton[i]);
						playButton[i].addEventListener('click', playAudio, false);
				}

				function clickHandler() {
					if (myAudio.readyState == 4) {
						if (myAudio.paused == true) {
							myAudio.play();
							play.style.display = "none";
							pause.style.display = "inline";
						}
						else {
							myAudio.pause();
							play.style.display = "inline";
							pause.style.display = "none";
						}
					}
				}

				function checkKey(e) {
					if(e.keycode == 32 || e.keycode ==32) {
						clickHandler();
					}
				}

				

				toggleButton.addEventListener('click', function() {
					clickHandler()
				});

				window.addEventListener('keypress', checkKey, false);

				playAll.addEventListener('click', audioPlay(playButton[n]), true);

				playNext.addEventListener('click', function() {
					n = n + 1;
					if (n == playButton.length) {
						n = 0;
					}
					var audioSrc = playButton[n].value;
					songTitle.innerHTML = playButton[n].name;
					myAudio.setAttribute("src", audioSrc);
					myAudio.play();
				});

				playPrev.addEventListener('click', function() {
					if (n == 0) {
						n = playButton.length;
					}
					n = n - 1;
					var audioSrc = playButton[n].value;
					songTitle.innerHTML = playButton[n].name;
					myAudio.setAttribute("src", audioSrc);
					myAudio.play();
				});

				myAudio.addEventListener('ended', function() {
					n = n + 1;
					if (n == playButton.length) {
						n = 0;
					}
					var audioSrc = playButton[n].value;
					songTitle.innerHTML = playButton[n].name;
					myAudio.setAttribute("src", audioSrc);
					myAudio.play();
				});

				myAudio.addEventListener('timeupdate', function() {
					var curMins = parseInt(myAudio.currentTime / 60);
					var curSecs = parseInt(myAudio.currentTime - curMins * 60);
					ct.innerHTML = curMins + ":" + curSecs;
					var mins = parseInt(myAudio.duration / 60);
					var secs = parseInt(myAudio.duration - mins * 60);
					dur.innerHTML = mins + ":" + secs;
					progressBar.style.width = parseInt(((myAudio.currentTime / myAudio.duration)*100), 10) + "%";
				})

				if (myAudio.currentTime == myAudio.duration && loopAudio != true) {
					play.style.display = "inline";
					pause.style.display = "none";
					progressBar.style.width = 0;
				}

				progressBarButton.addEventListener('click', function(e) {
					var clickedPosition = (e.offsetX)/this.offsetWidth;
					var clickedTime = clickedPosition * myAudio.duration;
					myAudio.currentTime = clickedTime;
				});

				volumeButton.addEventListener('click', function(e) {
					var clickedPosition = (e.offsetY)/this.offsetHeight;
					var clickedVolume = 1-clickedPosition;
					if (clickedVolume < 0.1) {
						myAudio.volume = 0;
						myAudio.muted = true;
						volumeBar.style.height = 0;
						volumeButton.style.display = "none";
						volumeOn.style.display = "none";
						muteButton.style.display = "inline";
					}
					else {
						myAudio.volume = clickedVolume;
						volumeBar.style.height = parseInt((clickedVolume * 100),10) + "%";
					}
				});

				muteButton.addEventListener('click', function(e){
					myAudio.muted = false;
					myAudio.volume = 0.5;
					muteButton.style.display = "none";
					volumeOn.style.display = "inline";
					volumeButton.style.display = "inline";
					volumeBar.style.height = "50%";
				});

				repeatButton.addEventListener('click', function(e){
					if (flag) {
						flag = false;
						myAudio.loop = false;
					}
					else {
						flag = true;
						myAudio.loop = true;
					}
				});

			}
