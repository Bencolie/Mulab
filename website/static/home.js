let intro = document.getElementById('intro_img')
let img_index= 0;

let img_list=[
    {
        image:"/static/z_Intro01.jpg",
    },
    {
        image:"/static/z_Intro02.jpg",
    },
    {
        image:"/static/z_Intro03.jpg",
    },
    {
        image:"/static/z_Intro04.jpg",
    }
];

function intro_load(img_index){
    intro.src = img_list[img_index].image;
}
intro_load(img_index);

function nextIntro(){
    if(img_index<img_list.length-1){
        img_index += 1;
        intro_load(img_index);
    }else{
        img_index =0;
        intro_load(img_index);
    }
}

function backIntro(){
    if(img_index>0){
        img_index -= 1;
        intro_load(img_index);
    }else{
        img_index = 3;
        intro_load(img_index);
    }
}