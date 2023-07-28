//variables
const play_button=document.getElementById('play_button');
let music = document.getElementById('music');
let artist = document.getElementById('artist');
let title = document.getElementById('title');
let image = document.getElementById('image');

//canvas 
const canvas = document.getElementById('canvas');
canvas.width = window.innerWidth*0.7;
canvas.height = window.innerHeight*0.7;
const ctx = canvas.getContext('2d');

// crate a point class with constructor
class Point{
    constructor(id,color,x,y,size){
        this.id = id;
        this.color = color;
        this.x =x;
        this.y=y;
        this.size=size;
    }
    draw(ctx){
        ctx.beginPath();
        ctx.arc(this.x,this.y,this.size,0,2*Math.PI);
        ctx.fillStyle= this.color
        ctx.fill();
        ctx.closePath();
    }
};

// PointsArray store instances of Point
const PointsArray = [];

// initial (x,y) position
const init_x=canvas.width/12;
const init_y=canvas.height/12;
// unit
const unit_x = canvas.width/12;
const unit_y = canvas.height/12;

let j_1 = j_2 = j_3 = j_4 = j_5 = j_6 =j_7 =j_8 = j_9 = j_10 = j_11 = 0;

//let's draw a lots od points!! ;"rgb(246, 202, 210)"
for(let i=0; i<121; i++ ){
    if(i%11==0){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+0*unit_x,init_y+unit_y*j_1,15));
        j_1+=1
    }else if(i%11==1){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+1*unit_x,init_y+unit_y*j_2,15));
        j_2+=1;
    }else if(i%11==2){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+2*unit_x,init_y+unit_y*j_3,15));
        j_3+=1;
    }else if(i%11==3){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+3*unit_x,init_y+unit_y*j_4,15));
        j_4+=1;
    }else if(i%11==4){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+4*unit_x,init_y+unit_y*j_5,15));
        j_5+=1;
    }else if(i%11==5){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+5*unit_x,init_y+unit_y*j_6,15));
        j_6+=1;
    }else if(i%11==6){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+6*unit_x,init_y+unit_y*j_7,15));
        j_7+=1;
    }else if(i%11==7){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+7*unit_x,init_y+unit_y*j_8,15));
        j_8+=1;
    }else if(i%11==8){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+8*unit_x,init_y+unit_y*j_9,15));
        j_9+=1;
    }else if(i%11==9){
        PointsArray.push(new Point(i,"#F6CAD2",init_x+9*unit_x,init_y+unit_y*j_10,15));
        j_10+=1;
    }else{
        PointsArray.push(new Point(i,"#F6CAD2",init_x+10*unit_x,init_y+unit_y*j_11,15));
        j_11+=1;
    }
}

let music_index= 0;

let music_list=[
    {
        name:'Flower',
        path:"/static/Flowers.mp3",
        image:"/static/z_cute01.gif",
        artist:'Ashamaluevmusic'
    },
    {
        name:'Heartsore',
        path:"/static/Heartsore.mp3",
        image:"/static/z_cute02.gif",
        artist:'Ashamaluevmusic'
    },
    {
        name:'Reverie',
        path:"/static/Reverie.mp3",
        image:"/static/z_cute04.gif",
        artist:'Ashamaluevmusic'
    }
];

//audio file
let audioElement;
let node_connected = false;
let audioSource, analyser,bufferLength,dataArray;

function music_load(music_index){
    music.src = music_list[music_index].path;
    image.src = music_list[music_index].image;
    title.innerHTML = music_list[music_index].name;
    artist.innerHTML = music_list[music_index].artist;
    play_button.innerHTML = '<i class="fa-regular fa-circle-play" style="color:#F65A83;"></i>'
    music.load();
}
music_load(music_index);


function nextSong(){
    if(music_index < music_list.length -1){
        music_index += 1;
        music_load(music_index);
    }else{
        music_index = 0;
        music_load(music_index);
    }
}

function previousSong(){
    if(music_index > 0){
        music_index -= 1;
        music_load(music_index);
    }else{
        music_index = 2;
        music_load(music_index);
    }
}

//ColorArray ; "#F6CAD2" is the canvas' background color
const ColorArray=['#C0EEE4','#CBFFA9','#B2A4FF','#3AA6B9',"#F6CAD2","#F4D160","#FF2171"];
//RandomArray
const RandomArray=Array.from({length:121},(_,index)=>index);
let animateId;
let music_durartion;

play_button.addEventListener('click',function(){
    //change the button icon
    play_button.innerHTML = '<i class="fa-regular fa-circle-pause" style="color:#F65A83;"></i>'

    audioElement = document.querySelector('audio');
    audioElement.play();
    music_durartion = audioElement.duration;

    //audio web api
    const audioContext = new AudioContext();
    //create note objets
    audioSource = audioContext.createMediaElementSource(audioElement);
    analyser = audioContext.createAnalyser();
    //connect the nodes
    audioSource.connect(analyser);
    analyser.connect(audioContext.destination);
    //musicSampling and convert outputFrequencyData into an arrayDataForm
    analyser.fftSize = 1024;
    bufferLength = analyser.frequencyBinCount;
    dataArray = new Uint8Array(bufferLength);
    function animate(){
        analyser.getByteFrequencyData(dataArray);
        /* Math.random() generates a value from 0 to 1, 
        therefore Math.ceil() and multiplication of RandomArray.length is needed */
        let lucky_num = Math.floor(Math.random()*(RandomArray.length-1));
        let color_num = Math.floor(Math.random()*ColorArray.length);
        for(let k=0; k<bufferLength; k++){
            //update the canvas
            ctx.clearRect(0,0,canvas.width,canvas.height);
            if(0<dataArray[k]<=85){
                PointsArray[lucky_num].color=ColorArray[color_num];
            }else if(85<dataArray[k]<=170){
                PointsArray[lucky_num].color=ColorArray[color_num];
            }else{
                PointsArray[lucky_num].color=ColorArray[color_num];
            }
            PointsArray.forEach((point) => {
                point.draw(ctx);
            });
        }
        animateId = requestAnimationFrame(animate);   
    }
    requestAnimationFrame(animate);
    /* stop the animation after some time! 
    (setTimeout(funtion(){},time in milliseconds)*/
    setTimeout(function(){
        cancelAnimationFrame(animateId);
        // need other solutions~
        audioSource.disconnect();
        // change the icon again
        play_button.innerHTML ='<i class="fa-regular fa-circle-play" style="color:#F65A83;"></i>'
    },music_durartion*1000);
});

