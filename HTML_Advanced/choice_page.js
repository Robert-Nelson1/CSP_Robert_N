function hover(){
    document.getElementById("img").src = "https://ac.blooket.com/marketassets/blooks/springrabbit.svg"
}

function leave(){
    document.getElementById("img").src = "https://ac.blooket.com/marketassets/blooks/whiterabbit.svg"
}

function hello(){
    const image = document.getElementById("rabbit");
    const text = document.getElementById("story");
    if (text.style.display === "none") {
        text.innerHTML = "My two lovely pets, Oreo and Precious, have made my days go by fast, as spending time with them is the best part of my day. Oreo, is always ready to entertain anyone with his playful hops and curious nose twitches. He always manages to make me laugh with all his sneaky behavior. This is especially true when he tries to steal snacks he's not supposed to get. Precious, is his opposite who is much gentler and more affectionate. Her favorite thing is to cuddle up next to me and let me pet her soft fur. Watching them interact and chase each other around, or just relax in their favorite corner brings a sense of joy that I didn't even realize I needed. No matter how stressful my day is, these two, always manage to lift my spirits up and remind me to slow down and appreciate the little things.";
        image.style.display = "block";
        text.style.display = "block";
    } else {
        text.style.display = "none";
        image.style.display = "none";
    }
}