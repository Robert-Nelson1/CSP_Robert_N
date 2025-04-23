let images =["https://ac.blooket.com/marketassets/blooks/yeti.svg", "https://ac.blooket.com/marketassets/blooks/rabbit.svg"]
let counter = 0
function change(){
    if(counter < images.length){
        document.getElementById("img").src = images[counter]
        counter += 1
    }else{
        counter = 0
        document.getElementById("img").src = images[counter]
    }
    
}

function hello(){
    let name = window.prompt("What is your SSN?")
    document.getElementById("title").style.color = "orange"
    document.getElementById("title").innerHTML = "orange"
}

function hover(){
    document.getElementById("img").src = "https://ac.blooket.com/marketassets/blooks/whiterabbit.svg"
}

function leave(){
    document.getElementById("img").src = "https://ac.blooket.com/marketassets/blooks/yeti.svg"
}

function show(){
    document.getElementById("meme").style.display = "block"
}
function pop(){
    window.alert("ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
}