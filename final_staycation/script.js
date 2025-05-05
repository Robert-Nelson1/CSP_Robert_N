function toggleExtra() {
    const extra = document.getElementById('extraContent');
    const button = document.querySelector('button');
    const style = window.getComputedStyle(extra);

    if (style.display === 'none') {
        extra.style.display = 'block';
        button.textContent = "View Less";
      } else {
        extra.style.display = 'none';
        button.textContent = "View More";
      }
    }

    function hover(){
    document.getElementById("img").src = "https://www.visitutah.com/azure/cmsroot/visitutah/media/site-assets/three-season-photography/southwestern-utah/southwestern-4/springdale_zion-national-park_dash-jay.jpg"
    }

    function leave(){
    document.getElementById("img").src = "https://www.nps.gov/zion/learn/nature/images/Big-Bend-11222021.jpg"
    }