const video = document.getElementById("video");
const canvas = document.getElementById("canvas");

let you = 0;
let ai = 0;


navigator.mediaDevices.getUserMedia({video:true})
.then(stream=>{
    video.srcObject = stream;
});

async function playGame(){

    
    const cd = document.getElementById("countdown");
    for(let i=3;i>0;i--){
        cd.innerText=i;
        await new Promise(r=>setTimeout(r,700));
    }
    cd.innerText="GO!";
    await new Promise(r=>setTimeout(r,300));
    cd.innerText="";

    
    const ctx = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video,0,0);

    canvas.toBlob(async(blob)=>{

        const form = new FormData();
        form.append("image",blob,"frame.jpg");

        const res = await fetch("/predict",{
            method:"POST",
            body:form
        });

        const data = await res.json();

        document.getElementById("player").innerText=data.player;
        document.getElementById("computer").innerText=data.computer;
        document.getElementById("result").innerText=data.result;

        if(data.result.includes("You")){
            you++;
        }else if(data.result.includes("Computer")){
            ai++;
        }

        document.getElementById("youScore").innerText=you;
        document.getElementById("aiScore").innerText=ai;

    },"image/jpeg");

}
